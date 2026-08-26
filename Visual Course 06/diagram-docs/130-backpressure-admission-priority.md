# Diagram 130 — Backpressure, Rate Limits, Admission Control, and Priorities

![On dark navy, a stack of white cubes labelled REQUEST FLOOD sends three cyan arrows into a tall blue ADMISSION GATE, which shows four white stacked panels — CAPACITY, TENANT LIMIT, PRIORITY, DEADLINE. A cyan arrow labelled ACCEPTED leaves the gate into three blue queues — HIGH, NORMAL, BULK — each with a signal-strength bar. Each queue sends a cyan arrow to a worker pool: HIGH WORKER POOL (FEW, FAST), NORMAL WORKER POOL (MORE), BULK WORKER POOL (MANY). A red OVERLOAD arrow leaves the bottom of the gate to a red RETRY LATER clock on a red platform. A dashed teal CAPACITY SIGNAL arrow loops from the worker pools back to the left side of the gate.](../diagrams/130-backpressure-admission-priority.png)

**Module:** Queues, workers, and backpressure
**Role in the course:** the second queue pattern — deciding what gets in, and in what order
**Layout:** a vertical admission gate on the left feeding three horizontal lanes, with an overload path and a capacity signal loop

---

## At a glance

A **REQUEST FLOOD** of white cubes meets a tall blue **ADMISSION GATE**. Inside the gate, four checks: **CAPACITY, TENANT LIMIT, PRIORITY, DEADLINE**.

Accepted work flows into three lanes: **HIGH, NORMAL, BULK**. Each lane has its own queue and its own worker pool: **few and fast, more, many**.

A red arrow labelled **OVERLOAD** drops to **RETRY LATER**. And a dashed teal **CAPACITY SIGNAL** loops from the worker pools back to the gate.

This is not a queue diagram. It is a *before-the-queue* diagram. The gate makes an honest promise before the work enters the system.

---

## What the diagram teaches

### 1. There are four reasons to reject work, and they live in one gate

**CAPACITY** — do we have enough workers, memory, time, budget, or external quota to handle this?

**TENANT LIMIT** — has this customer or team already used more than their share?

**PRIORITY** — how urgent is this relative to everything else already inside?

**DEADLINE** — can we still meet this before it becomes useless or dangerous to do?

Four checks, drawn as four white panels stacked in a single blue gate. The stack says the gate is one decision: each panel can reject, and any rejection is final. The work does not get to try the next lane.

### 2. The gate is an honest promise, and that is why it comes first

The most common failure mode is the absence of this gate. Requests arrive, queues grow, and the system pretends it can absorb them. Eventually the queue becomes a reservoir of work that has no realistic chance of completing on time. The only honest answer at that point is too late.

The admission gate exists so the system can say **no, retry later** while the caller still has time to do something useful. A `429 Too Many Requests` or a `202` with a truthful retry time is a better outcome than accepting a request that will sit in a queue until its deadline passes.

### 3. Three lanes, and the worker pools are different sizes on purpose

**HIGH, NORMAL, BULK** are not three instances of the same queue. They are three contracts.

**HIGH QUEUE → HIGH WORKER POOL (FEW, FAST).** Reserved capacity for small, urgent, interactive work. Few workers, but they are the fastest path through the system.

**NORMAL QUEUE → NORMAL WORKER POOL (MORE).** General work. More workers than high, but not starved by bulk.

**BULK QUEUE → BULK WORKER POOL (MANY).** Large, slow jobs. Many workers, but they draw from the longest queue and have the lowest priority.

The different pool sizes are the fairness mechanism. If bulk work consumed every worker, high and normal would stall. If high had many workers, bulk would always wait. The diagram encodes a weighted share of capacity.

### 4. PRIORITY without capacity and fairness becomes starvation

The **PRIORITY** panel sits in the gate, but the worker pools beside the queues are what make priority real. A priority system without separate pools and limits simply means *the urgent thing runs first until it uses everything*.

That is why the three lanes exist. Priority is not just a sort key. It is a separate queue with a separate budget, so one urgent tenant cannot become all-consuming.

TENANT LIMIT enforces the same idea across customers: one tenant cannot fill every lane.

### 5. DEADLINE is a rejection reason, not just a queue order

The **DEADLINE** panel is inside the gate, not beside the queues. That is significant. A deadline is not a suggestion about how fast to run; it is an *admission criterion*.

If the system cannot finish the work before its deadline, the honest response is to reject or defer it immediately. Accepting it and then watching it expire is worse — the work consumes capacity, fails, and must be cleaned up. The red **OVERLOAD → RETRY LATER** path is the honest answer to *there is no path that completes in time*.

### 6. The capacity signal flows backward, and the loop is the whole point

The dashed teal arrow labelled **CAPACITY SIGNAL** leaves the worker pools and curves back to the left side of the **ADMISSION GATE**.

This is backpressure. The workers tell the gate how full they are, and the gate uses that information to decide what to admit. Without the loop, the gate is just a rules engine guessing. With it, the gate is a closed loop that knows the system's current state.

The signal is not one number. It is a composite: queue depth, oldest item age, worker saturation, external quota, and the completion rate of each lane. The gate can then choose to admit more bulk, more high, or nothing at all.

### 7. Backpressure is what lets the previous pattern survive

The diagram to the left of this one in the course is the queue itself — durable, with a lease and a visibility window. Backpressure is what prevents that queue from becoming a place where work goes to wait indefinitely.

![A PRODUCER sends work to a DURABLE QUEUE, which leases it to WORKER A through a visibility window. WORKER A processes the work, writes a RECEIPT, ACKs the queue, and reaches COMPLETE. A coral dashed path shows WORKER A crashing, the LEASE EXPIRING, and the SAME ITEM being redelivered to WORKER B.](../diagrams/129-queue-lease-ack-visibility.png)

That queue does its job well: it decouples the producer's speed from the worker's speed. But if the producer is always faster than the worker, the queue grows without limit. The lease becomes irrelevant because the work will not be reached until it is already too late. Backpressure is the upstream signal that says the queue is full, the workers are saturated, and the producer must wait. It turns an unbounded buffer into a bounded system.

---

## Case study — Northway Support, the chat flood that buried the bulk jobs

Northway runs a multi-tenant support platform for about 400 enterprise customers. On a normal day, their admission layer routed around 80,000 requests: support chats, ticket updates, bulk report exports, scheduled data re-analysis.

Their worker pools were sized for normal load. They had one queue.

### What they had

A single queue fed a single worker pool. Work was prioritised by timestamp: first in, first out, with a manual override for VIP customers.

Bulk report jobs could take thirty seconds to two minutes. A support chat reply took under a hundred milliseconds. Both went into the same queue.

### The incident

A large customer launched a billing integration with a bug that submitted 15,000 bulk reconciliation jobs over six minutes. At the same time, a product outage began, and their public status page drove a spike of support chats.

The queue depth grew from 200 to 17,000 in four minutes. Support chat replies, which had averaged 120ms, began taking eight seconds. By the eight-minute mark, some customers saw their support sessions time out entirely.

The bulk jobs were not malicious. They were simply at the front of the queue, and everything behind them had to wait.

Operations stopped the bulk job source and restarted the worker pool. It took six hours to drain the queue. During that window, 1,900 support chats had failed before the timeout, and the customer-visible incident lasted far longer than the underlying outage.

### The admission gate

**CAPACITY.** Workers are measured in three dimensions: active tasks, queue depth, and oldest item age. If any lane crosses a threshold, admission tightens.

**TENANT LIMIT.** One customer cannot consume more than a fixed share of any lane. A tenant's bulk jobs are rate-limited independently of its support chats.

**PRIORITY and lanes.** Three queues with separate worker pools:
- **HIGH** for interactive support, with a small, fast pool and a hard cap on queue depth.
- **NORMAL** for ticket updates and routine work.
- **BULK** for report exports and reconciliation, with a large pool but bounded queue length.

**DEADLINE.** A bulk job that cannot start within its SLA is rejected with a `Retry-After` header. A support chat that cannot be admitted is a `429`, surfaced to the agent as a brief *system busy* rather than a silent timeout.

**CAPACITY SIGNAL.** The worker pools publish queue depth and oldest-item age back to the gate every second. The gate uses those signals, not static thresholds, to decide how much of each class to admit.

### Results

- **Single queue depth during a similar flood:** 17,000 → high lane capped at 80, normal at 400, bulk at 800.
- **Support chat timeout rate during overload:** 17% → 0.3%.
- **Bulk jobs rejected at the gate with a retry time, not lost:** 91% of the 15,000 were deferred rather than accepted into an overflowing queue.
- **Time to drain overload after the source stopped:** 6 hours → 18 minutes.
- **Manual operations intervention to protect interactive traffic:** required → not required.

### The line in their operations standard

*If the queue is longer than the work's deadline, the answer at the door is no. An honest rejection now costs less than a silent failure later.*

---

## Composition

A left-to-right flow with a vertical gate on the left and three horizontal lanes on the right, plus an overload path and a backward feedback loop.

**Far left:** **REQUEST FLOOD** — a blue platform holding a cluster of white cubes.

**Three cyan arrows** → **ADMISSION GATE** — a tall blue rectangular structure with a white top and four stacked white panels, each with an icon: **CAPACITY** (person), **TENANT LIMIT** (shield with check), **PRIORITY** (upward arrow), **DEADLINE** (clock).

**Centre-right:** from the gate, a **cyan arrow labelled ACCEPTED** fans to three blue queue platforms:
- **HIGH QUEUE** with a signal-strength bar → **HIGH WORKER POOL (FEW, FAST)** with three small figures.
- **NORMAL QUEUE** with a signal-strength bar → **NORMAL WORKER POOL (MORE)** with four small figures.
- **BULK QUEUE** with a signal-strength bar → **BULK WORKER POOL (MANY)** with nine small figures.

**Lower:** a **red arrow labelled OVERLOAD** leaves the bottom of the gate and points right to **RETRY LATER** — a red clock on a red platform.

**Feedback:** a **dashed teal arrow labelled CAPACITY SIGNAL** leaves the worker-pool area, curves downward and left, and re-enters the left side of the gate.

## Element by element

**REQUEST FLOOD** — the unregulated demand.
**ADMISSION GATE** — the place where the system decides whether to accept.

**CAPACITY, TENANT LIMIT, PRIORITY, DEADLINE** — the four admission criteria.

**HIGH / NORMAL / BULK QUEUE** — three service classes.
**HIGH WORKER POOL (FEW, FAST) / NORMAL (MORE) / BULK (MANY)** — three differently-sized pools, not three copies of the same.

**OVERLOAD → RETRY LATER** — the honest answer when there is no capacity.
**CAPACITY SIGNAL** — the feedback loop that makes the gate respond to actual load.

## Colour and flow semantics

- **Cyan arrows** carry forward work and accepted traffic.
- **Cyan fanning** from the gate shows a routing decision based on the four checks.
- **Red** marks overload and the **RETRY LATER** outcome — a safe refusal.
- **Teal dashed** carries the **CAPACITY SIGNAL** backward, marking it as feedback rather than work.
- The **four stacked panels** inside one gate say the criteria are a single decision, not a sequence of filters.
- The **different worker-pool sizes** are the fairness mechanism: priority without its own pool is starvation.

## How to present it

**Start with the restaurant analogy.** A restaurant controls seating at the door because filling every hallway with waiting diners does not create more cooks. Ask what happens in their system when demand exceeds capacity. The answer is usually a queue that grows forever.

**Point at REQUEST FLOOD and then at the gate.** The gate is where the honest promise is made. If the promise is not made there, it is broken somewhere else.

**Read the four panels.** Capacity, tenant limit, priority, deadline. Ask which of the four their system checks before admitting work. Usually it is one or none.

**Show the overload path.** It is not a failure. It is the system saying *no, but try again in a known time*. Compare that to accepting work and letting it time out in a queue.

**Point at the three worker pools and ask what differs.** Few and fast, more, many. Then ask what would happen if bulk work had the fast pool. The answer is that interactive work would wait behind bulk jobs.

**Make the priority point directly.** Priority alone is starvation unless it has a separate pool. The tenant limit does the same thing across customers.

**Trace the teal capacity signal backward.** It is not a request. It is the workers telling the gate how full they are. Without it, the gate is guessing.

**Tell the Northway flood.** 15,000 bulk reconciliation jobs and a support chat spike in the same queue. Support chat timeouts at 17%, six hours to drain, manual intervention required.

**Present the fix as adding the door, not more cooks.** Separate lanes, tenant limits, deadlines, and a capacity signal. The result: bulk jobs are deferred, interactive traffic stays fast, and overload drains in eighteen minutes.

**Close on the standard.** *If the queue is longer than the work's deadline, the answer at the door is no.*

**Timing.** Twenty minutes. Thirty if the room maps their own work into three service classes, which usually exposes one class with no pool of its own.

---

## Lab and checkpoint

**Lab:** Identify three service classes in your system and map them to separate worker pools. Add an admission gate that checks capacity, tenant limits, priority, and deadline before accepting work. Ensure the capacity signal flows backward from workers to the gate, and define what happens when a job cannot meet its deadline.

**Checkpoint:** Why is it better to reject work at the door than to accept it and let it time out in a queue?

**Answer:** Because accepting work that cannot complete in time wastes resources and gives the caller a worse experience. Rejecting at the door is an honest promise: the system tells the caller immediately that it cannot handle the work, instead of letting it wait and fail later.

## Glossary

- **Admission gate** — the point where work is accepted or rejected.
- **Backpressure** — the signal that tells upstream components to slow down.
- **Capacity** — the available worker or system resources.
- **Deadline** — the time by which work must complete, used as a rejection reason.
- **Fairness** — the guarantee that every tenant or class gets a share of capacity.
- **Overload** — the state where demand exceeds capacity.
- **Priority** — the ranking that determines which work is handled first.
- **Queue** — the buffer holding admitted work.
- **Service class** — a category of work with its own pool and deadline.
- **Starvation** — a state where some work never gets resources.
- **Tenant limit** — the cap on work per tenant.
- **Worker pool** — the set of workers assigned to a service class.

## Sources

- Backpressure and admission control
- Priority, fairness, and service-class pools
- Queueing and deadline-aware scheduling
