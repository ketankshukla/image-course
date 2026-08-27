# Diagram 134 — Parallel Work, Fan-Out, Fan-In, and Joins

![On dark navy, a PARENT WORKFLOW platform sends four cyan arrows to four blue workers — POLICY WORKER, LEDGER WORKER, FRAUD WORKER, CUSTOMER HISTORY WORKER. Each worker returns a cyan RESULT arrow and a teal ACK arrow to a JOIN GATE, which shows four rows: REQUIRED ALL, QUORUM 3 OF 4, OPTIONAL NONE, DEADLINE 30s. The join gate emits a teal arrow through a green check to AGGREGATED EVIDENCE. Two coral dashed paths leave the workers to STRAGGLER and DUPLICATE boxes, each with a red X, showing rejected late or duplicate results.](../diagrams/134-fan-out-fan-in-join.png)

**Module:** Distributed workflow patterns
**Role in the course:** orchestrating independent work in parallel and deciding when the parent continues
**Layout:** a left-to-right fan with a central join gate and rejected side paths

---

## At a glance

One **PARENT WORKFLOW** fans out to four workers: **POLICY, LEDGER, FRAUD, CUSTOMER HISTORY**.

Each worker returns **RESULT** and **ACK** to a **JOIN GATE**.

The join gate has four rules: **REQUIRED ALL, QUORUM 3 OF 4, OPTIONAL NONE, DEADLINE 30s**.

Then **AGGREGATED EVIDENCE**.

And on the lower right, two coral paths: **STRAGGLER** and **DUPLICATE**, both with a red X.

The diagram is not about starting work in parallel. It is about knowing when to stop waiting and continue.

---

## What the diagram teaches

### 1. Four branches, but one parent owns the join

The **PARENT WORKFLOW** is the coordinator. It fans out commands to four independent workers, but the workers do not decide when the parent proceeds. The **JOIN GATE** does.

That is the core pattern. Parallel work without a join rule is just work that may finish at different times. The parent needs a declared policy for *when the next step can start*.

The four workers are specialists. Each does one thing. The parent needs the right combination of their results to make a decision.

### 2. The join gate is the contract, and it has four dimensions

**REQUIRED ALL** — every worker must return a valid result.
**QUORUM 3 OF 4** — three valid results are enough.
**OPTIONAL NONE** — no optional workers are waited for.
**DEADLINE 30s** — the parent will not wait beyond 30 seconds.

These four rules together define the join policy. A result can be required, optional, or part of a quorum. A worker can be in none of those categories and simply be ignored.

The diagram encodes this as rows on the gate. The rows are the contract. Without them, the parent would have to hard-code the join logic in its own state machine.

### 3. REQUIRED ALL is the default, and it is dangerous when misused

If every worker is required, the parent waits for everyone. That is the safest rule and the slowest one.

The common mistake is to make every branch required when some of them are only useful context. A slow optional worker then blocks the whole workflow, and the parent ends up waiting for a result it does not need.

The diagram shows **REQUIRED ALL** at the top because it is the strongest rule. It also shows **QUORUM** and **OPTIONAL** because most workflows need something weaker.

### 4. QUORUM and OPTIONAL are how speed becomes safe

**QUORUM 3 OF 4** means the parent can continue as soon as any three of the four workers have succeeded. It does not matter which three, as long as the policy says the fourth is not required.

**OPTIONAL NONE** means the parent is not waiting for optional workers. The customer-history worker might return late, but the workflow does not block for it.

The combination of these rules is what makes parallel speed useful. The parent does not wait for the slowest worker if the slowest worker is not required.

### 5. DEADLINE is the upper bound, and it is part of the policy

**DEADLINE 30s** is the fourth row on the gate. It says the parent will make a join decision after 30 seconds even if not all results have arrived.

The deadline is not a separate timeout bolted onto the workflow. It is part of the join contract. The parent, the workers, and the operator all know the maximum wait.

When the deadline fires, the join gate applies the other rules. If three required results have arrived and the fourth is missing, the quorum rule may allow the parent to continue. If a required result is missing, the deadline rule turns the missing result into a typed failure, not a silent stall.

### 6. STRAGGLER and DUPLICATE are visible, and that is why they are drawn

The **coral dashed paths** to **STRAGGLER** and **DUPLICATE** are not failures to ignore. They are events to handle.

A **STRAGGLER** is a result that arrives after the join has already made its decision. A result cannot be late and also used. The diagram rejects it with a red X.

A **DUPLICATE** is a result that has already been counted once. If a worker retries and returns the same result again, the join gate must ignore the duplicate, not double-count it.

Both paths are drawn explicitly because they are easy to overlook in code. A join that does not handle stragglers and duplicates will eventually use stale or double evidence.

### 7. The join result is AGGREGATED EVIDENCE, not a merged state

The output of the gate is **AGGREGATED EVIDENCE**. Not a new worker, not a merged object, not a decision. Just evidence.

The parent uses the evidence to make its next decision. The join gate does not make the business decision. It enforces the contract for *when the parent may continue*.

That separation is important. The join gate owns the waiting. The parent owns the business logic that consumes the evidence. If the parent also owned the waiting, the join policy would be scattered through the workflow code.

Once the parent has enough evidence, it often must act through a longer sequence of compensable and irreversible steps:

![On dark navy, a play button leads left-to-right through three blue steps — RESERVE FUNDS, UPDATE CASE, SEND REFUND — each with an acknowledgement loop. A PIVOT / POINT OF NO RETURN padlock sits before SEND REFUND. Failure in RESERVE FUNDS or UPDATE CASE triggers coral compensation steps — RELEASE FUNDS or RESTORE CASE — with their own acknowledgements. A coral dashed box encloses both compensation paths and ends in COMPENSATION FAILURE leading to MANUAL REVIEW, a red platform with a person and magnifier.](../diagrams/135-saga-compensation-irreversible-effects.png)

The join gate in this diagram tells the parent when the evidence is complete. The saga takes over and decides what to do with that evidence. RESERVE FUNDS and UPDATE CASE are compensable, so the parent can still reverse them if the join turns out to be wrong. SEND REFUND is the point of no return; after that, the parent cannot safely compensate, so it proceeds to completion or to manual review. The two diagrams are the boundary between *gathering evidence* and *acting on it*.

### 8. Branch identity, typed outcomes, and cancellation are part of the contract

The diagram labels each worker because results must be attributed. A **RESULT** arrow without a branch identity is evidence that cannot be traced. The parent creates stable branch identities, and the join gate uses them to decide which combination has arrived.

The join gate collects success, typed failure, timeout, and cancelled outcomes as separate cases. A missing required result is different from a slow optional result. A result that arrives after cancellation is a straggler. Without these types, the parent conflates "did not answer" with "answered no."

Cancellation belongs in the contract. The customer-history worker is optional, so the parent stops waiting after five seconds. The background worker can keep running, but its late result is a straggler, not a missing requirement. **Temporal Child Workflows** make this explicit: the parent owns the join and records which branches were started, cancelled, or timed out.

### 9. First-success is a join rule, but only when one answer is enough

A first-success rule says the parent continues as soon as any one branch returns a valid result. It is useful when workers are alternatives, not collaborators. If the four workers are four identity providers and any valid one is enough, first-success is the fastest correct rule.

The checkpoint asks when first-success is safe. The answer is: only when any valid branch independently satisfies the business need and the lost results do not violate policy. In the Pendle case, policy, ledger, and fraud are not interchangeable; they are different kinds of evidence. First-success would discard evidence the parent needs.

If the room uses **Promise.any** or **asyncio.wait**, ask whether the branches are alternatives or required collaborators. If they are collaborators, first-success is a bug. If they are alternatives, make the rule explicit, add a deadline, and decide what to do with slower branches.

---

## Case study — Pendle Underwriting, the slow history check

Pendle Underwriting reviews claims for several travel insurers. A typical claim needs evidence from four sources: a policy check, a ledger balance, a fraud risk, and customer history.

### What they had

A sequential workflow. It ran the four checks one at a time. Policy, then ledger, then fraud, then customer history. If any check took a long time, the whole claim was delayed.

Customer history was sometimes slow. It called an old system with unpredictable response times, occasionally over ten seconds. Policy, ledger, and fraud usually finished in under a second.

### The problem

A claim could not be approved until all four checks completed. If customer history took ten seconds, every claim took at least ten seconds, even when the other three checks were enough.

Worse, customer history was often just confirming context. The actual approval decision was based on policy, ledger, and fraud. History was useful, but not required.

### The fan-out

The workflow was rebuilt with a fan-out to four workers and a join gate.

- **Policy** — required.
- **Ledger** — required.
- **Fraud** — required.
- **Customer history** — optional.

**Quorum:** required all of the three required workers.
**Deadline:** five seconds for the optional customer history worker.

If policy, ledger, and fraud returned successfully, the join produced aggregated evidence and the approval step began. The customer-history worker continued in the background. If it returned before the deadline, its evidence was attached to the case record. If it was late, it was rejected as a straggler.

### Handling duplicates and stragglers

The customer-history worker had retries. If a retry delivered the same result twice, the join gate ignored the duplicate.

If the first result was late and the second result was on time, the on-time one was used. The join gate tied each result to a branch attempt, not to a wall-clock time, so it could tell which result belonged to which fan-out.

### Results

- **Mean approval time for claims where customer history was slow:** 10–12 seconds → 1.5 seconds.
- **Claims blocked by optional context:** 100% → 0.
- **Duplicate history evidence used in decisions:** 0.4% of claims → 0.
- **Stragglers attached to the case as optional late context:** 0 before the fix → 8% of cases, surfaced as a clearly labelled late artifact.
- **Approval decisions delayed by an optional check:** eliminated.

### The line in their underwriting standard

*Make every branch required only if the decision is genuinely impossible without it. Otherwise, declare it optional with a deadline and a rule for late or duplicate results.*

---

## Composition

A left-to-right fan: parent workflow on the left, four workers in the middle, join gate on the right, aggregated evidence at the end, with two rejected side paths below.

**Far left:** **PARENT WORKFLOW** — a blue platform with a flowchart icon.

**Four cyan arrows** fan right to four blue worker platforms:
- **POLICY WORKER** — shield icon.
- **LEDGER WORKER** — ledger icon.
- **FRAUD WORKER** — magnifier icon.
- **CUSTOMER HISTORY WORKER** — person icon.

**From each worker:** a **cyan arrow labelled RESULT** and a **teal dashed arrow labelled ACK** return to the **JOIN GATE**.

**JOIN GATE** — a tall blue structure with four white rows:
- **REQUIRED ALL** — green check.
- **QUORUM 3 OF 4** — three people icon.
- **OPTIONAL NONE** — grey dash.
- **DEADLINE 30s** — clock icon.

**Right:** a **teal arrow** from the join gate through a **green check** to **AGGREGATED EVIDENCE** — a blue platform with a document and database icon.

**Lower right:** two **coral dashed paths** from the workers to **STRAGGLER** and **DUPLICATE** — red boxes with white X marks.

## Element by element

**PARENT WORKFLOW** — the orchestrator.
**POLICY / LEDGER / FRAUD / CUSTOMER HISTORY WORKERS** — parallel branches.

**RESULT** — the typed outcome from a worker.
**ACK** — the durable acknowledgement that the result was received.

**JOIN GATE** — the contract that decides when the parent continues.
**REQUIRED ALL / QUORUM 3 OF 4 / OPTIONAL NONE / DEADLINE 30s** — the four join rules.

**AGGREGATED EVIDENCE** — the combined result the parent uses.

**STRAGGLER** — a late result that cannot be used.
**DUPLICATE** — a result already counted once.

## Colour and flow semantics

- **Cyan arrows** carry commands from parent to worker and results from worker to join gate.
- **Teal dashed arrows** carry acknowledgements — durable receipt of the result.
- **Teal** on the final arrow marks the safe aggregated evidence.
- **Coral dashed** marks the straggler and duplicate paths — late or redundant results.
- **Red X** on straggler and duplicate means rejection, not failure.
- **Green check** marks the join as satisfied.
- The **four rows on the gate** make the policy readable as a single contract.

## How to present it

**Start with the problem of waiting.** Most rooms have seen a `Promise.all` or `gather` call that blocks on the slowest participant. Ask what happens if one of the calls is optional.

**Point at the four workers and ask which are required.** Most will say all four. Then ask whether the customer-history check is needed before the parent can decide. Often it is not.

**Read the join gate rows.** REQUIRED ALL, QUORUM 3 OF 4, OPTIONAL NONE, DEADLINE 30s. Ask which row the room has never written down.

**Make the point about stragglers and duplicates.** If a result arrives after the join has moved on, it is a straggler. If a retried worker returns the same result twice, it is a duplicate. Both need to be rejected explicitly, not silently accepted.

**Trace the Pendle case.** A slow customer-history check blocked every claim. The fix: fan out, mark history optional with a five-second deadline, use a quorum on the required checks, and surface stragglers as late context.

**Emphasize that AGGREGATED EVIDENCE is not a decision.** The join gate does not approve the claim. It tells the parent when it has enough evidence to make its own decision.

**Ask the room to write one join policy.** Four inputs, which are required, which are optional, what is the quorum, what is the deadline. Most will discover they do not have a written policy.

**Map first-success to the room's own code.** Ask who uses `Promise.any`, `Promise.all`, `gather`, or `asyncio.wait`. `Promise.all` is **REQUIRED ALL**. `Promise.any` is first-success. Most code does not declare the join type, so an optional timeout can fail everything or leave cancelled side effects running invisibly.

**Add the implementation maps.** In Next.js, render one progress card per branch. In Python, use structured concurrency and durable child tasks. Apply deadlines and cancellation through the parent, not ad hoc worker timers.

**Close on the standard.** *Make every branch required only if the decision is genuinely impossible without it. Otherwise, declare it optional with a deadline and a rule for late or duplicate results.*

**Timing.** Twenty minutes. Thirty if the room maps one real parallel call and finds an unwritten join rule.

---

## Lab and checkpoint

**Lab:** Identify one parallel call in your system. Write the join policy: which branches are required, which are optional, the quorum rule, the deadline, and the rules for stragglers and duplicates. Then implement it with structured concurrency or durable child tasks, with cancellation and deadlines driven by the parent.

**Checkpoint:** Why is REQUIRED ALL the dangerous default?

**Answer:** Because it forces the parent to wait for every branch even if some branches are not necessary for the decision. This creates unnecessary latency, allows slow optional checks to block the whole workflow, and hides the real dependency structure.

## Glossary

- **Aggregated evidence** — the combined result of the join, not a decision.
- **Branch** — one parallel worker in a fan-out/fan-in pattern.
- **Deadline** — the upper time limit for a branch or the whole join.
- **Duplicate** — a result that arrives twice from a retried worker.
- **Fan-in** — the phase where branch results are gathered.
- **Fan-out** — the phase where a parent sends work to parallel branches.
- **First-success** — a join rule that proceeds as soon as one sufficient answer arrives.
- **Join gate** — the contract that decides when enough evidence has arrived.
- **Optional** — a branch that is not required for the join.
- **Quorum** — a rule that proceeds when a defined subset of branches completes.
- **Required all** — a rule that requires every branch to complete.
- **Straggler** — a result that arrives after the join has moved on.

## Sources

- Fan-out/fan-in and join patterns
- Structured concurrency and durable tasks
- Quorum, optional branches, and straggler handling
