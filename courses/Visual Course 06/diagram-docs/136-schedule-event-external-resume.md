# Diagram 136 — Scheduled, Event-Triggered, and Externally Resumed Work

![On dark navy, three entry paths converge on a DEDUP + CORRELATION GATE. From the top, a WORKFLOW ID: SCHEDULE TIMER with a calendar. From the middle, a WORKFLOW ID: DOMAIN EVENT with an antenna. From the bottom, a WORKFLOW ID: EXTERNAL CALLBACK with a globe. The gate has a red path to UNKNOWN CALLBACK. Past the gate, WORKFLOW RUNNING leads to WAIT WITHOUT WORKER, then RESUME. A red path from WAIT WITHOUT WORKER leads to EXPIRED DEADLINE. From RESUME, four teal arrows fan to ACKNOWLEDGEMENT PATH, RECEIPT PATH, CHECKPOINT PATH, and DURABLE RESUME PATH.](../diagrams/136-schedule-event-external-resume.png)

**Module:** Distributed workflow patterns
**Role in the course:** how long workflows can sleep and wake up without holding a worker open
**Layout:** three trigger lanes feeding a gate, a wait state in the middle, and four durable resume paths on the right

---

## At a glance

Three ways to wake a workflow:

**SCHEDULE TIMER** — a calendar with a clock.
**DOMAIN EVENT** — an antenna.
**EXTERNAL CALLBACK** — a globe.

All three go through a **DEDUP + CORRELATION GATE**. Then the workflow runs, waits without a worker, resumes, and produces **ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, DURABLE RESUME PATH**.

And two red exits: **UNKNOWN CALLBACK** and **EXPIRED DEADLINE**.

A long workflow should sleep for minutes or months and resume from a trigger without holding a process open.

---

## What the diagram teaches

### 1. There are three legitimate triggers, and they are not interchangeable

**Schedule timer** — the workflow starts or resumes at a specific time. It is for periodic work, reminders, deadlines, and follow-ups.

**Domain event** — a business fact occurs and the workflow should react. It is for `RefundSettled`, `CaseApproved`, `PaymentReturned`, and so on.

**External callback** — an external system calls back. It is for webhooks, provider push notifications, and authenticated inbound messages.

The same workflow may accept all three, but each one has different safety rules. A timer cannot be forged. An event is a fact. A callback must be authenticated.

### 2. Every trigger must pass the DEDUP + CORRELATION GATE

The gate in the centre is the diagram's safety device. It does two things: **deduplicate** the trigger and **correlate** it to the right workflow.

Deduplication is necessary because timers can fire twice, events can be redelivered, and callbacks can be retried. Correlation is necessary because a callback without a workflow ID is just noise.

The gate rejects an **UNKNOWN CALLBACK** in red. If a callback arrives and there is no waiting workflow that expected it, the honest answer is not to guess. It is to reject the callback and log it.

The gate's checks are: is the trigger for this specific workflow ID; is the workflow currently waiting for this trigger type; has the trigger already been consumed; does the payload match the expected schema; and is the source authenticated. A timer passes because it is created by the workflow's own scheduler. A domain event passes because it is a fact the workflow subscribed to. An external callback passes only after signature or credential validation.

### 3. Wait without worker is the point of the pattern

After the workflow runs for a moment, it reaches **WAIT WITHOUT WORKER**. The hourglass says the workflow is waiting, and the label says no worker is holding it open.

That is the efficiency. A long-running workflow should not occupy a process for the duration of a two-day wait. It should persist its wait condition, release the worker, and resume when the trigger arrives.

The wait is durable. If the whole worker fleet restarts, the wait survives in the workflow store. When the trigger fires, a new worker can resume from the checkpoint.

### 4. Resume is not restart

The **RESUME** card is a play button. It says continue from the last checkpoint, not start from the beginning.

A workflow that is resumed must know where it was, what it was waiting for, and what the next allowed action is. That information is the durable resume path.

Restarting from the beginning is sometimes possible, if the workflow is deterministic and every step is idempotent. But it is not the same as resume. Resume continues the existing run. Restart creates a new run.

The diagram draws a single path from WAIT to RESUME to the four outputs, because the workflow is the same identity before and after the wait.

### 5. Expired deadline is a trigger, not a silent failure

A **red arrow** from **WAIT WITHOUT WORKER** leads to **EXPIRED DEADLINE**. The workflow was waiting for something that did not arrive in time.

This is not the same as a timeout inside a single function. It is a durable deadline that spans the wait. When it fires, the workflow must make a business decision: escalate, cancel, compensate, or proceed with partial evidence.

The expired deadline is drawn as a rejected trigger because it is an expected condition. The workflow knows how to handle it because the deadline is part of its wait contract.

### 6. The four resume paths are the durable vocabulary again

From **RESUME**, four teal arrows fan to:
- **ACKNOWLEDGEMENT PATH**
- **RECEIPT PATH**
- **CHECKPOINT PATH**
- **DURABLE RESUME PATH**

These are the same outputs from the snapshot/replay diagram, because resuming a workflow is the same fundamental operation as rebuilding it from a snapshot. The durable resume path is what allows the workflow to continue after a restart.

![On dark navy, APPEND-ONLY EVENTS 1 TO 900 as numbered cards lead to SNAPSHOT AT 800 with a camera and green tick, then a play-button card REPLAY 801 TO 900, and a database card CURRENT STATE. Above, CODE V1 and V2 feed a VERSION GATE; a cyan arrow enters replay, and a coral arrow leads to INCOMPATIBLE EVENT and MIGRATION TEST. Six teal outputs fan from CURRENT STATE, including CHECKPOINT and RESUME.](../diagrams/127-snapshot-replay-schema-evolution.png)

The same pattern: a stable point, then replay or resume from that point. A workflow that has been waiting for a month should resume from its last checkpoint, replay only the events that matter, and not re-execute work that has already completed.

### 7. The resume gate must be secure, idempotent, and versioned

A callback is an inbound call from outside. It must be authenticated, correlated to a workflow, and checked against the workflow's current state. A callback for a completed workflow is a duplicate. A callback for a different workflow version may be invalid.

The diagram does not draw a **VERSION** box, but the gate implies it. Only an expected trigger for the current workflow version may advance the wait.

### 8. The same trigger can be consumed only once

A durable resume system must remember which triggers it has already processed. A callback that is delivered twice — because the provider retried, or because the network made the first ACK appear to fail — must not advance the workflow twice.

The consumption record is keyed by the trigger's durable identity: a timer's scheduled fire time, an event's event ID and offset, or a callback's nonce and signature. Once consumed, the trigger returns the existing state, exactly as a duplicate queue item returns the same result.

This is why the dedup check is in the gate, not in the workflow logic. By the time the workflow sees the trigger, the system has already decided whether it is new or duplicate.

### 9. The resume token record is the durable contract

A **durable timer** is a persisted future wake-up; a **signal** is any external input; a **callback** is a remote request that resumes known work. The **DEDUP + CORRELATION GATE** decides by reading a durable resume token that was written when the workflow reached **WAIT WITHOUT WORKER**. A good token contains the workflow ID, the wait name, the allowed actor, an expiry, a nonce, the consumed time, and the duplicate response.

This is the lab exercise in miniature: design the record before the gate. It is also the Maya refund case: the first signed callback records **APPROVAL RECEIVED**; the duplicate returns the existing state. If the record is incomplete, the gate cannot correlate, deduplicate, or expire correctly. The token is the source of truth; the worker is just a reader. The checkpoint answer — that worker sleep holds fragile compute and loses progress on restart — is why the stored state carries the contract.

### 10. Keep transport, framework, and business truth separate

A queue can retry, a worker can disappear, and an agent can revise its proposal, but the authoritative workflow record must stay inspectable. In **Next.js**, return `202 Accepted` with a status location and signed, replay-protected webhooks. In **Python**, model timers and external signals as workflow events, validate signatures, and use idempotent signal handlers that check state and correlation. Typed records let tests replay fixtures without the network. This underlies Temporal workflow execution and the CloudEvents 1.0.2 specification; a restart must never change the business meaning.

---

## Case study — Wrenfield Collections, the invoice that paid twice

Wrenfield handles overdue invoice collections for a finance software company. A collections workflow has three waits: a reminder wait, a payment arrival wait, and a final escalation wait.

### What they had

A background job that polled the payment provider every five minutes. The job held a process open for up to 30 days. When a payment arrived, the job updated the invoice and closed the case.

The job was not durable. If the worker restarted, the job was lost and had to be recreated from a database query. There was no workflow ID. There was no deduplication. There was no authentication of the payment notification.

The payment provider also offered a webhook, but the webhook was not tied to a workflow. The application accepted any inbound request with a matching payment reference and applied the credit immediately.

### The incident

A webhook from the payment provider arrived during a deployment. The webhook was not authenticated. It did not include an invoice or workflow ID. The application accepted it and tried to credit the payment.

The application found an invoice with a matching payment reference and applied the credit. Then the background job, still polling, found the same payment and applied it again.

The invoice was credited twice. The customer was overpaid, and the finance team spent three days reconciling the account.

### The durable design

The workflow is started when the invoice becomes overdue. It sets a schedule timer for the first reminder, a callback subscription for the payment provider, and a deadline for the final escalation.

Then it reaches **WAIT WITHOUT WORKER**. No process is held open.

When the payment provider calls back, the callback is authenticated with a signature and a workflow ID. The **DEDUP + CORRELATION GATE** checks that the workflow is waiting for this exact callback and that the callback has not already been consumed.

The workflow resumes from its checkpoint, verifies the payment, records a receipt, and closes the case. The background poll is eliminated.

If the deadline expires before the callback arrives, the workflow resumes into an escalation state, not a failure state.

### Results

- **Payment double-credited from unauthenticated callback + polling job:** 2 incidents in one quarter → 0.
- **Long-running processes held open for 30 days:** all collection cases → 0.
- **Time to resume after a worker restart:** unreliable recreation from query → immediate, from durable checkpoint.
- **Escalations that expired silently:** 14% → 0, because every expired deadline becomes an explicit workflow state.

### The line in their collections standard

*A workflow that waits must release the worker, carry the deadline, and verify every resume trigger as if it were a new command.*

---

## Composition

Three trigger lanes converge on a central gate, then flow through a wait state and resume into four durable paths.

**Left:** three blue platforms, each with a label and icon:
- **WORKFLOW ID: SCHEDULE TIMER** — calendar with a clock.
- **WORKFLOW ID: DOMAIN EVENT** — antenna with waves.
- **WORKFLOW ID: EXTERNAL CALLBACK** — globe.

**Centre:** a large blue **DEDUP + CORRELATION GATE** — shield with a check. A red path leads to **UNKNOWN CALLBACK** — red octagon with an X.

**Past the gate:** **WORKFLOW RUNNING** — flowchart icon; **WAIT WITHOUT WORKER** — hourglass on a blue platform; **RESUME** — play button.

**From WAIT WITHOUT WORKER:** a red arrow to **EXPIRED DEADLINE** — red box with an X.

**Right:** from **RESUME**, four teal arrows fan to:
- **ACKNOWLEDGEMENT PATH** — green check.
- **RECEIPT PATH** — document.
- **CHECKPOINT PATH** — flag.
- **DURABLE RESUME PATH** — circular arrows.

## Element by element

**SCHEDULE TIMER / DOMAIN EVENT / EXTERNAL CALLBACK** — the three trigger types.
**DEDUP + CORRELATION GATE** — the safety gate for every trigger.

**WORKFLOW RUNNING** — the workflow is active.
**WAIT WITHOUT WORKER** — the workflow is sleeping and no process is held.
**RESUME** — the workflow continues from its checkpoint.

**UNKNOWN CALLBACK** — a trigger that does not match a known wait.
**EXPIRED DEADLINE** — a wait that exceeded its time bound.

**ACKNOWLEDGEMENT / RECEIPT / CHECKPOINT / DURABLE RESUME PATH** — the durable outputs of resuming.

## Colour and flow semantics

- **Cyan arrows** carry the triggers into the gate.
- **Cyan** also carries the workflow through running, waiting, and resume.
- **Teal** marks the four durable resume paths.
- **Red** marks **UNKNOWN CALLBACK** and **EXPIRED DEADLINE** — rejected or terminal conditions.
- The **convergence on the gate** shows that all three triggers must pass the same checks.
- The **hourglass** in **WAIT WITHOUT WORKER** is the visual promise: no worker is consumed during the wait.

## How to present it

**Ask how the room handles long waits.** Polling? Holding a process open? Manual cron jobs? All of those are the problem this diagram replaces.

**Point at the three trigger types and ask which they use.** Most use at least two, often without naming the difference. A schedule is not an event. A callback is not a schedule.

**Emphasise the gate.** Every trigger, regardless of source, passes through deduplication and correlation. The red **UNKNOWN CALLBACK** is the honest answer to *we got a callback for a workflow we are not expecting.*

**Show WAIT WITHOUT WORKER.** This is the efficiency. The hourglass means the workflow is waiting, but no worker is running. The wait is stored, and the worker is released.

**Distinguish resume from restart.** Resume continues. Restart begins again. Ask what their system does after a wait. If it re-runs the whole workflow, it may not be resuming.

**Tell the Wrenfield story.** Unauthenticated callback plus a polling job credited the same payment twice. The fix: authenticated callbacks, workflow ID, dedup and correlation, durable wait without worker, checkpoint resume.

**Point at EXPIRED DEADLINE.** It is not an error. It is an expected state. The workflow must decide what to do when a deadline expires.

**Trace the four resume paths.** Acknowledgement, receipt, checkpoint, durable resume path. These are the artifacts that make resume safe.

**Close on the standard.** *A workflow that waits must release the worker, carry the deadline, and verify every resume trigger as if it were a new command.*

**Run the resume-token lab.** Ask the room to list the fields a gate needs to tell a fresh callback from a duplicate: workflow ID, wait name, allowed actor, expiry, nonce, consumed time, and duplicate response. Then compare their list to the fields the diagram implies. This makes the gate concrete.

**Connect the pattern to the stack.** For Next.js, discuss `202 Accepted` with a status location and signed webhooks. For Python, discuss idempotent signal handlers and typed records. The pattern stays the same.

**Timing.** Twenty minutes. Thirty if the room maps one real long wait and checks whether callbacks are authenticated, correlated, and deduplicated.

---

## Lab and checkpoint

**Lab:** Identify one long wait in your system. Design it as a durable wait that releases the worker. List the three trigger types it accepts: schedule, external event, and callback. For each trigger, define the dedup and correlation gate fields. Write the resume token record and the rule for distinguishing resume from restart.

**Checkpoint:** Why is resume not restart?

**Answer:** Because resume continues the workflow from the checkpoint where it waited. Restart begins the workflow again. A restart may repeat already-completed side effects; a resume does not if the durable state is preserved.

## Glossary

- **Callback** — an external notification that triggers a resume.
- **Checkpoint** — the durable state saved before a wait, used to resume.
- **Correlation** — the link that matches a trigger to the correct workflow.
- **Deadline** — the time by which the workflow must resume or take a defined action.
- **Dedup** — the check that prevents the same trigger from being consumed twice.
- **External event** — a domain event from another system.
- **Resume** — continuing a workflow from where it paused.
- **Resume token** — the durable contract that records the wait and its triggers.
- **Schedule** — a time-based trigger.
- **Trigger** — a legitimate reason to resume a waiting workflow.
- **Wait without worker** — the pattern of releasing the worker while the workflow is paused.

## Sources

- Durable wait, schedule, and callback resume
- Deduplication and correlation of external triggers
- Resume tokens and idempotent continuation
