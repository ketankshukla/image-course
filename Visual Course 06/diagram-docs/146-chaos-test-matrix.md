# Diagram 146 — Fault Injection and Agent Workflow Chaos Tests

![On dark navy, a large CHAOS MATRIX grid with six rows and six columns. Rows on the left are BEFORE COMMIT, AFTER SIDE EFFECT, DURING ACK, DURING APPROVAL, DURING HANDOFF, DURING COMPENSATION. Columns across the top are CRASH, TIMEOUT, DUPLICATE, REORDER, PARTITION, STALE INPUT. Each cell contains two icons: a source hazard icon and a destination icon. Green checks mark cells with expected invariants, orange metrics, purple recovery tools, and red paths mark failures. To the right, four vertical OUTCOME panels: EXPECTED INVARIANT with a green shield, RECEIPT with a green envelope, METRIC with an orange bar chart, and RECOVERY with a purple wrench.](../diagrams/146-chaos-test-matrix.png)

**Module:** Testing, correctness, and observability
**Role in the course:** how to prove workflow safety by injecting failure at business boundaries
**Layout:** a 6x6 matrix of workflow boundaries by failure modes, with outcome types on the right

---

## At a glance

A **CHAOS MATRIX**: six rows, six columns.

**Rows** — the workflow boundaries:
- **BEFORE COMMIT**
- **AFTER SIDE EFFECT**
- **DURING ACK**
- **DURING APPROVAL**
- **DURING HANDOFF**
- **DURING COMPENSATION**

**Columns** — the failure modes:
- **CRASH**
- **TIMEOUT**
- **DUPLICATE**
- **REORDER**
- **PARTITION**
- **STALE INPUT**

Every cell asks: what should happen when this failure occurs at this boundary?

The answer is not *the process restarts*. The answer is one of four outcomes:
- **EXPECTED INVARIANT**
- **RECEIPT**
- **METRIC**
- **RECOVERY**

---

## What the diagram teaches

### 1. Chaos testing needs a hypothesis, not random destruction

The matrix is not a list of things to break. It is a list of questions to answer.

Each cell is a hypothesis: *if a crash happens before a commit, what is the expected invariant? Is it durable? Is there a receipt? Is there a metric? Is there a recovery path?*

Randomly restarting servers is not chaos testing. It is noise. The value comes from testing a known boundary with a known expectation.

### 2. The rows are the dangerous business boundaries

**BEFORE COMMIT** — the command is in memory, not yet durable. A crash here should lose nothing important.

**AFTER SIDE EFFECT** — the system has called an external provider. A crash here must not lose the provider's receipt or cause the side effect to be repeated.

**DURING ACK** — the queue message is being acknowledged. A crash here must not double-process the message.

**DURING APPROVAL** — a human is deciding. A failure here must not execute a stale or unapproved action.

**DURING HANDOFF** — responsibility is being transferred between systems or agents. A failure here must not create orphan tasks.

**DURING COMPENSATION** — the system is trying to undo an effect. A failure here must not leave the system in an inconsistent state.

These are the points where durable state, external state, and human decisions meet. They are the natural injection points.

### 3. The columns are the common failure modes

**CRASH** — a process or worker stops.
**TIMEOUT** — a response does not arrive in time.
**DUPLICATE** — a message or effect is repeated.
**REORDER** — events arrive in the wrong order.
**PARTITION** — a network or service split.
**STALE INPUT** — a decision is based on old data.

These are the same hazards that appear in the concurrency and queue diagrams. The matrix applies them to each business boundary.

![On dark navy, four hazards sit on the left: RACE between two commands, DUPLICATE EVENT, OUT OF ORDER event 12 before 11, and STALE WRITE version 7 against current 9. Each sends a white command/event card into a row of four blue CORRECTNESS GUARDS: EXPECTED VERSION, UNIQUE KEY, SEQUENCE, and MONOTONIC STATE. Past the guards, arrows point to a blue STATE STORE showing CURRENT VERSION: 9 and LATEST SEQUENCE: 11. To the right, ACCEPTED STORE / APPLY or REJECTED GUARD FAILED outcomes.](../diagrams/145-race-duplicate-order-stale-state.png)

That diagram is the static view of the same columns. EXPECTED VERSION maps to STALE INPUT and RACE. UNIQUE KEY maps to DUPLICATE. SEQUENCE maps to REORDER. MONOTONIC STATE and the state store decide the legal outcome for PARTITION and CRASH. The chaos matrix adds a temporal dimension: not just what the guard does, but what the workflow does at each boundary when the guard is stressed.

### 4. Every injected fault ends in a legal state

The diagram's safety rule is: **every injected fault ends in one legal state with no duplicate consequence and a discoverable recovery action.**

That is the pass condition. The system does not have to stay up. It does not have to be fast. It has to end in a legal, explainable, recoverable state.

A duplicate consequence is a failure. An unowned failure state is a failure. A crash that nobody can reason about is a failure.

### 5. The four outcomes are evidence, not opinion

**EXPECTED INVARIANT** — a business rule that must hold. For example, *the refund is not issued twice*.

**RECEIPT** — durable evidence that the system or provider saw the action. A provider receipt, an idempotency key, a checkpoint.

**METRIC** — an observable signal that the fault happened and was handled. Duplicate-detected, retry-exhausted, recovery-triggered.

**RECOVERY** — a documented path from the failure state back to a safe state. It can be automated or manual, but it must be written down and rehearsed.

A chaos test that does not produce evidence in at least one of these categories is a guess.

### 6. Fault injection points are before and after durable or external effects

The best injection points are the boundaries immediately before and after a durable commit, an external side effect, a queue acknowledgement, an approval, a handoff, or a compensation.

Those are the windows where something can go wrong and leave the system in an ambiguous state. If you inject a fault in the middle of a pure computation, you learn less. If you inject it right after the payment provider says yes, you learn a lot.

### 7. The same scenario must be repeatable

A chaos test is not a one-time event. The same scenario must be repeatable. Repeatability is what makes it a test.

Use deterministic fixtures, fake clocks, and stable operation identities. Use adapter interfaces to inject the fault. The scenario should produce the same outcome every time.

Repeatability also means the test can run in CI. A chaos test that only works in production on a Tuesday is not a test. It is an incident.

### 8. The recovery path must be closed

The trace says: **Repeat the same scenario to prove idempotency and close any unowned failure state.**

An unowned failure state is a state where nobody knows what to do. The runbook does not cover it. The alert does not route to anyone. The metric does not fire.

The chaos test is not done until the recovery path is documented, rehearsed, and proven.

### 9. The durable record, not the worker, decides the business meaning

The test is not checking whether the worker restarts. It is checking whether the durable record still tells the truth. The record must say what was requested, which identity owns it, what changed, which attempt produced the change, and what may legally happen next. A framework can store, replay, and resume that record in different ways, but a restart must never rewrite the business meaning. That is why the matrix separates transport behavior from workflow truth. A queue can retry, a worker can disappear, an agent can revise its proposal, and a payment provider can change its latency, but the authoritative workflow record must remain inspectable. In Python, model commands, events, states, and error outcomes as typed records so tests replay the same fixture without network calls. In a Next.js application, keep the browser view read-only with respect to workflow truth; mutations go through authenticated server boundaries and return stable IDs or receipts.

### 10. A chaos test is only valid when it is safe, repeatable, and attributable

A chaos test is still a test. It needs deterministic fixtures, a fake clock, stable operation identities, and adapter interfaces for fault injection so the scenario can run in CI and produce the same evidence every time. It also needs a safe containment boundary. Never expose production chaos controls to ordinary users; create operator-only synthetic demo pages that trigger named, safe fault fixtures and show expected and actual state, receipt, alert, and recovery outcome. Repeatability is what closes the recovery path: run the same failure, watch the same redelivery, prove idempotency, and prove no unowned failure state remains. The strongest pass condition for a side-effect chaos test is one legal business outcome, no duplicate effect, durable evidence, visible status, and successful documented recovery. If the test produces a different answer on Tuesday, it is an incident, not a test.

---

## Case study — Acme Refunds, the crash after payment

Acme processes refunds through a payment provider. The workflow sends a request, waits for the provider response, records the receipt, and completes.

### What they had

The system was tested for failures by randomly terminating pods. The tests showed that the service restarted and recovered. But they did not test the exact boundary between the provider accepting the refund and the local workflow recording the completion.

### The incident

A worker sent the refund request to the provider. The provider accepted it and returned a receipt. Before the worker could write the receipt to the workflow state, the container was killed.

A new worker picked up the same refund message from the queue. It did not have the provider receipt, so it sent the refund request again. The provider saw a second request with the same idempotency key and returned the existing receipt.

The second worker recorded the receipt and completed. The refund happened once, so the business outcome was correct. But the team did not know whether the system was safe at that boundary until the incident happened.

### The chaos test

The team built a chaos test for the boundary: **AFTER SIDE EFFECT** × **CRASH**.

They used a test fixture with a fake payment provider and a hook that crashed the worker immediately after the provider returned the receipt.

The expected invariant: the refund is recorded exactly once, no matter how many times the message is redelivered.

The expected receipt: the provider receipt is stored before the workflow completes.

The expected metric: duplicate-detected is emitted when the second request finds the existing idempotency key.

The expected recovery: the workflow resumes from the checkpoint, reads the provider receipt, and completes without re-sending the request.

The test ran in CI with a fake clock and deterministic fixtures. It passed. The team now had evidence that the boundary was safe.

### Results

- **Ambiguity at the payment boundary:** unknown → tested and documented.
- **Duplicate payment attempts in production after worker crashes:** 2 in one quarter → 0, because the idempotency path was proven.
- **Time to prove a new boundary is safe:** weeks of production anxiety → one deterministic CI test.
- **Incidents that started with "we think this is safe":** several → 0, because every risky boundary has a named test.

### The line in their engineering standard

*Every boundary around a durable commit, external side effect, queue ack, approval, handoff, or compensation has a named chaos test with expected invariant, receipt, metric, and recovery.*

---

## Composition

A 6x6 matrix with rows as workflow boundaries and columns as failure modes.

**Top header (six columns):**
- **CRASH** — lightning.
- **TIMEOUT** — hourglass.
- **DUPLICATE** — two overlapping documents.
- **REORDER** — shuffle arrows.
- **PARTITION** — split wall.
- **STALE INPUT** — database with clock.

**Left header (six rows):**
- **BEFORE COMMIT** — database with clock.
- **AFTER SIDE EFFECT** — gear with check.
- **DURING ACK** — message with check.
- **DURING APPROVAL** — person with check.
- **DURING HANDOFF** — two people.
- **DURING COMPENSATION** — undo arrow.

**Each cell** contains two icons: the hazard and the outcome. Outcomes are colour-coded:
- **Green check** — expected invariant met.
- **Orange bar chart** — metric.
- **Purple wrench** — recovery.
- **Red arrow / X** — failure path.

**Right side:** four vertical outcome panels:
- **EXPECTED INVARIANT** — green shield.
- **RECEIPT** — green envelope.
- **METRIC** — orange bar chart.
- **RECOVERY** — purple wrench.

## Element by element

**Rows** — the business boundaries where the workflow touches durable, external, or human state.
**Columns** — the failure modes to inject.

**Cells** — the hypothesis and expected outcome for each row-column pair.

**EXPECTED INVARIANT** — the business rule that must hold.
**RECEIPT** — the durable evidence.
**METRIC** — the observable signal.
**RECOVERY** — the documented recovery path.

## Colour and flow semantics

- **Green** means the expected outcome is met.
- **Orange** means a metric is emitted.
- **Purple** means a recovery action is taken.
- **Red** marks a failure path that the test must cover.
- The matrix is dense because every boundary can fail in every mode.
- The outcome panels on the right are the lenses through which each cell is judged.

## How to present it

**Ask how the room tests failure.** Most will say they restart services or simulate network partitions. Ask them what they expect to happen at each business boundary.

**Point at the rows.** Before commit, after side effect, during ack, during approval, during handoff, during compensation. These are the dangerous boundaries.

**Point at the columns.** Crash, timeout, duplicate, reorder, partition, stale input. These are the failure modes.

**Show that every cell is a hypothesis.** Do not break things at random. For each cell, define the expected invariant, receipt, metric, and recovery.

**Tell the Acme story.** A worker crashed after the provider accepted a refund. The second worker re-sent the request and the provider returned the existing idempotency key. The business outcome was safe, but only by accident. The fix: a deterministic chaos test for the after-side-effect × crash cell with expected invariant, receipt, metric, and recovery.

**Emphasize repeatability.** The test must use deterministic fixtures and fake clocks. It must run in CI. It must produce the same evidence every time.

**Close on the standard.** *Every boundary around a durable commit, external side effect, queue ack, approval, handoff, or compensation has a named chaos test with expected invariant, receipt, metric, and recovery.*

**Run the checkpoint first.** Ask the room: what is the strongest pass condition for a side-effect chaos test? Let them answer before you show the matrix. Most will say uptime or automatic restart. Then reveal the answer: one legal business outcome, no duplicate effect, durable evidence, visible status, and successful documented recovery. Use that as the lens for every cell.

**Map the room's practice onto the matrix.** Ask which of the six boundaries they have tested recently, where duplicate external effects have happened, and which failure windows feel unowned. This turns the diagram from a course page into a diagnostic.

**Connect the implementation guards.** Mention that Python tests inject faults through adapter interfaces, use fake clocks and deterministic provider doubles, and assert domain invariants. Mention that a Next.js application keeps chaos controls operator-only and shows expected versus actual state, receipt, alert, and recovery. These details make the matrix reproducible.

**Turn the lab into a group design activity.** Hand the room a real workflow and ask them to fill three high-value cells with setup, injection, expected state, forbidden outcome, metric, and recovery proof. If they can write the recovery proof, the boundary is understood.

**Cite the sources and set a release gate.** Cite AWS idempotent APIs, Amazon SQS visibility timeout, and Temporal Events and Event History. Then set the release gate: every boundary around a durable commit, external side effect, queue ack, approval, handoff, or compensation has a named chaos test before the next commit.

**Timing.** Twenty-five minutes. Thirty if the room fills in one row of the matrix for a real workflow.

---

## Lab and checkpoint

**Lab:** Pick one real workflow and one dangerous boundary. Fill in one cell of the chaos matrix: the boundary, the failure mode, the injected fault, the expected invariant, the receipt, the metric, and the recovery. Make the test deterministic, repeatable, and run it in CI.

**Checkpoint:** What is the strongest pass condition for a side-effect chaos test?

**Answer:** The outcome is one legal business state, no duplicate effect, durable evidence of what happened, visible status, and a documented recovery path. Uptime or automatic restart are not enough; the business outcome and evidence are what matter.

## Glossary

- **Attributable** — the test can be traced to a specific fault and outcome.
- **Chaos test** — a deterministic test that injects a fault to check a boundary.
- **Duplicate** — the same command or effect happening twice.
- **Durable record** — the evidence that decides the business meaning after a failure.
- **Fault injection** — deliberately causing a specific failure to test recovery.
- **Invariant** — a rule that must remain true after the fault.
- **Legal state** — a valid business state, even if it is not the success path.
- **Partition** — a network split.
- **Recovery** — the documented path back to a correct state.
- **Repeatable** — the test uses deterministic fixtures and a fake clock.
- **Safe** — the test does not cause real harm.
- **Side effect** — an external change that must be guarded.
- **Timeout** — a delay that exceeds the allowed time.

## Sources

- Chaos engineering and deterministic fault injection
- Idempotent external effects and queue semantics
- AWS idempotency, SQS, and Temporal event history
