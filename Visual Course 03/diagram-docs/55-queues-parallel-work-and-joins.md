# Diagram 55 — Queues, Parallel Work, and Joins

![A fan-out and fan-in on dark navy. ORCHESTRATOR shows a person at a board of cards. A cyan arrow leads to QUEUE, a stack of cards. Three cyan arrows fan out to BANK CHECK with a bank icon, POLICY CHECK with a shield, and TICKET CHECK with a ticket icon. All three converge on JOIN GATE, a teal node-network tile, which passes three green-checked cards onward to DECISION, a teal diamond. Two coral arrows drop from the join gate to TIMEOUT, a red clock, and FAILED PART, a red warning triangle.](../diagrams/55-queues-parallel-work-and-joins.png)

**Module:** Durable workflows
**Role in the course:** doing several things at once and waiting for all of them
**Layout:** orchestrator to queue, fan-out to three parallel checks, fan-in at a join gate with two failure exits

---

## At a glance

Work is queued, fanned out to **three independent checks running in parallel**, and then reassembled at a **JOIN GATE** before a decision is made.

The join gate is the diagram. Fanning out is easy. Waiting correctly for several things that may finish at different times, may fail individually, and may never finish at all — that is where parallel workflows actually break, and it is why the gate has two coral exits.

---

## What the diagram teaches

### 1. The queue is a stage, and it decouples the orchestrator from the work

**QUEUE** sits between the orchestrator and the fan-out, drawn as a stack of cards.

Its presence says the orchestrator does not perform the work and does not wait for it inline. It puts work down; something else picks it up.

Three properties follow, and they are the reason the queue is drawn rather than assumed:

- **Absorption.** A burst of requests does not overwhelm the checks; it lengthens the queue.
- **Survivability.** Work in a queue outlives the process that enqueued it.
- **Independent scaling.** Each check can have its own number of workers, sized to its own throughput.

Without the queue, the orchestrator holds the work in memory, and a crash loses it.

### 2. Three checks, and their independence is the reason to parallelise

**BANK CHECK**, **POLICY CHECK**, **TICKET CHECK** — three different icons, three separate platforms, three parallel arrows.

They are parallelisable because none depends on another's result. That is the test: if check B needs check A's output, they are sequential and drawing them side by side is a lie.

The benefit is wall-clock time. Three checks taking 2s, 5s and 3s take 5 seconds in parallel and 10 sequentially. For a user waiting, that is the difference between acceptable and not.

The cost is that you now have three things that can fail independently, in different ways, at different times — which is what the join gate exists to handle.

### 3. The join gate waits for all three, and produces one result

The **JOIN GATE** — a teal node-network tile — receives all three arrows and emits **three green-checked cards** onward to the decision.

Two things it does.

**It waits.** The decision cannot be made until all three have reported. The gate holds until they have.

**It aggregates.** Three separate results become one collection that the decision stage consumes. The decision does not know or care that the checks ran in parallel.

The three checked cards on the output side are showing the assembled set — all three present, all three passed.

### 4. Two failure exits, and they are genuinely different problems

**TIMEOUT** (a red clock) and **FAILED PART** (a red warning triangle), both reached by coral arrows from the join gate.

**TIMEOUT** — one or more checks did not report in time. You do not know their result. They may still be running. This is the unknown-outcome case: the check might complete a second after you gave up.

**FAILED PART** — a check reported, and its answer was a failure. You know the result and it is bad.

These need different responses. A timeout might warrant waiting longer, retrying that check, or proceeding on partial information with the gap noted. A failed part is a definite answer that the decision stage can reason about.

Collapsing them into "the join failed" throws away the distinction, and it is the distinction that determines what you do next.

### 5. The join gate is where the hard policy questions live

The diagram shows the gate and does not show its rules, so this is where the teaching has to add to the picture. Four questions have to be answered:

**How long do you wait?** A deadline for the whole join, not just per check. Without one, a hung check hangs the workflow.

**Do you need all three?** Sometimes a decision can be made on two of three. If policy check fails but bank and ticket pass, is that a definite no, or a decision with a caveat? This is a domain question, not a technical one.

**What happens to the others when one fails?** If policy check returns a hard refusal at second one, do you cancel the other two? Cancelling saves resources; letting them finish gives you complete evidence for the record.

**Is a partial result recorded?** Two checks completed and one timed out — that is information, and discarding it means repeating work on retry.

That last question is the checkpointing question, asked of a fan-out rather than a sequence:

![A workflow with alternating steps and teal bookmark checkpoints, a coral crash branch, and a resume path reading from a dashed checkpoint store back into COMPLETE.](../diagrams/53-checkpoint-and-resume.png)

A join gate that holds completed results in memory loses them exactly as a workflow without checkpoints does. Each check should write its result as it lands.

### 6. Parallel work multiplies the failure surface, and that is the trade

One sequential path has one place to fail. Three parallel paths have three, plus the join, plus the timeout, plus the partial-failure combinations.

That is not an argument against parallelism — the latency benefit is usually decisive — but it is an argument for the join gate being designed rather than assumed. Most implementations get the fan-out right on the first attempt and the join wrong.

---

## Case study — Northmoor Credit Union, the loan decision that hung

Northmoor is a credit union with about 85,000 members, offering personal loans, car finance and small business lending. A loan application requires three independent verifications before a decision:

- **Bank check** — open banking data to verify income and outgoings. External provider, typically 3–8 seconds, occasionally 40.
- **Policy check** — the member's standing against Northmoor's lending criteria. Internal, typically under a second.
- **Ticket check** — whether the member has any open service issues or disputes that should block lending. Internal, typically under a second.

None depends on the others. They ran sequentially in the first build, and total time was dominated by the bank check.

### Moving to parallel

The change was straightforward and the result was immediate: median decision time went from about 9 seconds to about 4.

Then a bank-data provider outage exposed everything they had not thought about.

### What the outage did

The provider did not fail cleanly. It accepted requests and returned nothing — no error, no response, just an open connection.

Northmoor's join gate had **no deadline**. It waited for all three.

Policy and ticket checks completed in under a second, as always. The bank check never returned. The join waited.

**Over four hours, 340 applications entered the join gate and stayed there.** Members saw "checking your application" and nothing else. The contact centre received 200 calls. Nobody at Northmoor could see what was happening, because the applications were not failed, not completed, and not visible on any dashboard that only showed terminal states.

### The four questions they then had to answer

**How long do you wait?** They set a 15-second join deadline. Above the bank check's 95th percentile, well below a user's patience threshold.

**Do you need all three?** This turned out to be the interesting one, and the answer was different per check.

*Policy check failing is decisive.* If the member fails lending criteria, the decision is no, regardless of what the other checks say. The gate now short-circuits on a policy refusal and cancels the other two.

*Bank check timing out is not decisive.* Their lending team's position: an application with policy and ticket passing but no bank data is not a refusal, it is an incomplete application. It routes to a human underwriter with the two completed checks attached and a note that bank data is unavailable.

*Ticket check timing out is not decisive either*, and it defaults to blocking pending manual review, because an unchecked dispute is a risk they will not automate past.

**What happens to the others when one fails?** They cancel on a decisive failure (policy refusal) and let them complete otherwise. The reasoning: for a decisive refusal, the other results have no value; for anything routing to a human, complete evidence is worth the resource.

**Is a partial result recorded?** Yes. Every completed check is written to the application as it lands, not held in the join gate's memory. A join that times out leaves two recorded results and one gap, so a retry only re-runs the missing check.

That last one was a direct consequence of the outage. During recovery they wanted to re-run the 340 stalled applications and found they had to re-run all three checks on each, because nothing partial had been recorded.

### The timeout/failure distinction in practice

They separated the two explicitly, and it changed their metrics.

Before: a single "check failure rate" that mixed provider outages with genuine refusals. It was around 4% and told them nothing.

After: a **timeout rate** (infrastructure health) and a **refusal rate** (lending outcomes). The timeout rate is now an alert threshold; the refusal rate is a business metric. Neither had been visible before.

### The monitoring gap they closed

The most damaging part of the incident was not the hang. It was that nobody knew about it for four hours.

Their dashboards showed applications by terminal state — approved, declined, referred. An application stuck in the join gate was in none of those.

They added a **work-in-progress view**: applications by non-terminal state, with age. Anything in the join gate for more than 30 seconds now appears on it, and anything above 5 minutes pages someone.

This generalises well beyond joins. Terminal-state dashboards make stuck work invisible, and stuck work is the failure mode that produces the longest incidents.

### Results

- **Applications hung indefinitely:** 340 in the incident, 0 since.
- **Median decision time:** ~4 seconds, retained.
- **Join timeouts:** about 0.3% of applications, all routed to underwriters with partial evidence rather than stalling.
- **Time to detect a stalled join:** four hours, now under a minute.

---

## Composition

A fan-out and fan-in reading left to right.

**ORCHESTRATOR → QUEUE**, then three cyan arrows fanning to **BANK CHECK**, **POLICY CHECK** and **TICKET CHECK** stacked vertically. All three converge with cyan arrows on **JOIN GATE**, which emits three green-checked cards and a cyan arrow to **DECISION**.

Two **coral arrows** drop from the join gate to **TIMEOUT** and **FAILED PART**.

## Element by element

**ORCHESTRATOR**
A person standing at a large board showing stacked cards with teal markers, on a blue platform.

**QUEUE**
A blue tray holding a stack of three white cards with teal markers — work waiting to be picked up.

**BANK CHECK** — a white card with a **teal bank/institution icon**.
**POLICY CHECK** — a white card with a **teal shield**.
**TICKET CHECK** — a white card with a **teal ticket icon**.

**JOIN GATE**
A **teal rounded tile carrying a white node-network glyph** — three nodes converging on one. Emits three white cards each with a **green check disc**.

**DECISION**
A **teal diamond** carrying a white question mark — the only decision shape in the diagram.

**TIMEOUT**
A **red circular clock** on a blue platform.

**FAILED PART**
A **red warning triangle** on a blue platform.

## Colour and flow semantics

- **Cyan arrows** carry the fan-out, the fan-in, and the path to the decision.
- **Coral arrows** carry both failure exits from the join gate.
- **Teal** marks the working machinery — the check icons, the join tile, the decision diamond.
- **Red** distinguishes the two failures by shape: a clock for timeout, a triangle for a reported failure.
- The **three green-checked cards** on the gate's output show the assembled complete set.

## How to present it

**Ask when work can run in parallel.** The test: no check depends on another's output. Then ask the room for a set of three from their own system and check whether it passes.

**Do the arithmetic.** 2s, 5s and 3s: ten seconds sequential, five parallel. Then ask what it cost — three independent failure surfaces plus the join.

**Ask why the queue is drawn as its own stage.** Absorption, survivability, independent scaling. Then ask what happens without it: the orchestrator holds the work, and a crash loses it.

**Put the four join questions to the room.** How long do you wait, do you need all of them, what happens to the others when one fails, and is a partial result recorded. Most teams have not answered any of them explicitly.

**Ask about the second question specifically.** Northmoor's answer differed per check: policy refusal is decisive and cancels the rest; bank timeout is not decisive and routes to a human; ticket timeout blocks pending review. This is a domain question, and framing it that way stops engineers from choosing a uniform technical answer.

**Ask the difference between the two coral exits.** Timeout means you do not know; failed part means you know and it is bad. Then ask what their current metrics do — Northmoor had one 4% "check failure rate" that mixed provider outages with genuine loan refusals and told them nothing.

**Tell the four-hour hang.** 340 applications, members watching a spinner, and nobody at Northmoor aware because the dashboards only showed terminal states. Then ask what their dashboards show.

**Give them the work-in-progress lesson.** Terminal-state dashboards make stuck work invisible, and stuck work produces the longest incidents. This generalises well past joins and is worth stating as its own takeaway.

**Timing.** Twenty-five minutes. Thirty-five if you work through the four join questions for a real parallel step in the room's own system.

---

## Lab and checkpoint

**Lab:** Identify one parallel check in your system. Map it to the orchestrator, queue, three parallel checks, and join gate. Answer the four join questions: how long do you wait, do you need all of them, what happens when one fails, and is a partial result recorded? Then write the dashboard metric that would make stuck work visible.

**Checkpoint:** Why is a timeout different from a failed part?

**Answer:** A timeout means you do not know whether the part completed. A failed part means you know it did not. Mixing them in one metric makes provider outages, genuine refusals, and unknown states indistinguishable.

## Glossary

- **Decision** — the stage after the join that routes based on the assembled results.
- **Fan-out** — the arrows from the queue to the parallel checks.
- **Fan-in** — the arrows from the checks to the join gate.
- **Failed part** — a check that reported a failure, as opposed to a timeout.
- **Join gate** — the stage that waits for all parallel checks and assembles the result.
- **Orchestrator** — the controller that starts the parallel work.
- **Queue** — the buffer that holds work and decouples the orchestrator from the workers.
- **Timeout** — a check that did not respond within the wait window.
- **Work-in-progress** — the state of a task that has started but not reached a terminal state.

## Sources

- Queue-based fan-out/fan-in and join patterns
- Workflow orchestration and timeout handling
- Observability for work-in-progress and stuck work
