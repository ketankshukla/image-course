# Diagram 132 — Deadlines, Cancellation, Timeout, and Compensation

![On dark navy, a teal USER CANCEL figure sends a dashed teal arrow to a CANCELLATION speech bubble, which sends dashed arrows to STEP A and STEP B. A teal TIMER clock sends a dashed arrow to a TIMEOUT hourglass, which also sends dashed arrows to both steps. STEP A is a white gear card on a blue platform; a dashed coral arrow drops from it to a red COMPENSATE A box with circular arrows. A teal chain labelled ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT and RESUME runs below the steps. A cyan arrow leads from STEP A to STEP B, then past a yellow POINT OF NO RETURN pin to a blue MANUAL RECOVERY box with a red X.](../diagrams/132-deadline-cancel-timeout-compensation.png)

**Module:** Queues, workers, and backpressure
**Role in the course:** the last queue pattern — how to stop, and what to do when stopping is no longer enough
**Layout:** a left-to-right step chain with cancellation and timeout inputs above, compensation below, and a point-of-no-return marker before manual recovery

---

## At a glance

A workflow with **STEP A** and **STEP B**. A yellow pin marks **POINT OF NO RETURN** between them.

From the left, two inputs: **USER CANCEL** and **TIMER** → **TIMEOUT**. Both send dashed arrows into the steps.

Below **STEP A**, a red box: **COMPENSATE A**. And along the bottom, the durable chain: **ACKNOWLEDGEMENT → RECEIPT → CHECKPOINT → RESUME**.

**Cancel before the point of no return, compensate after the first reversible step, and manual recovery after the irreversible one.**

---

## What the diagram teaches

### 1. Four different concepts, and conflating them is the most expensive mistake

**DEADLINE, CANCELLATION, TIMEOUT, COMPENSATION.**

Four words that are often used interchangeably in conversation and mean completely different things in a durable workflow.

A **deadline** is a business time. A **cancellation** is a request. A **timeout** is a system decision. A **compensation** is a new side effect.

The diagram keeps them apart by giving each one a distinct glyph: a user figure, a clock, a timer, a circular-arrow box. They do not live in the same lane because they are not the same thing.

### 2. The deadline travels with the work, and the point of no return is derived from it

A deadline is not a property of the scheduler. It is a property of the work. It says: *after this time, the result is no longer useful.*

The yellow **POINT OF NO RETURN** pin sits between **STEP A** and **STEP B**. It is derived from the remaining time, not from the step list. If Step A is fast and Step B is slow, the point of no return may arrive before Step B begins.

A workflow that does not carry its own deadline cannot make this decision correctly. It will either cancel too late and waste work, or give up too early and miss a window.

### 3. Cancellation is a request, and a request can be refused

The **USER CANCEL** figure sends a dashed arrow to a **CANCELLATION** speech bubble, and the speech bubble sends dashed arrows to both steps.

Dashed because it is a *request*, not an immediate kill signal. A step may need to reach a safe checkpoint before it can stop. A step that has already crossed the point of no return may not be cancellable at all.

The most common beginner error is treating cancellation as `process.kill()`. That aborts the computation but leaves the business effect in an unknown state. The provider may have already accepted the refund, the label may already have been printed, the email may already have been sent.

Cancellation is the user saying *I would like this to stop.* The workflow's job is to figure out whether it safely can, and if it cannot, to follow the recovery path.

### 4. Timeout is the system deciding, not the user

**TIMER** → **TIMEOUT**. A clock with a dashed arrow to an hourglass, and the hourglass sends dashed arrows to the steps.

A timeout is not a user action. It is the system's answer to *we have waited longer than we said we would.*

That distinction matters because the recovery is different. When a user cancels, the system can often ask the user what to do next. When a timeout fires, the system must make a decision on its own, using the rules that were set before the wait began.

Timeouts need a deadline. Without one, the system has no basis for deciding that the wait has been too long.

### 5. Compensation is not a rewind; it is a new side effect

Below **STEP A**, a red box with circular arrows: **COMPENSATE A**.

Compensation means doing something that counteracts a previous effect. It is not a database transaction rollback. It is a new command, validated by invariants, producing a new event and a new receipt.

A refund is the compensation for a charge. A return label is the compensation for a shipped package. A reversal request is the compensation for a payment that went through.

The diagram draws it in coral — the failure/recovery colour — and places it below the forward path because it is an alternate exit from a completed step, not a continuation of it.

### 6. The durable chain below the steps is what makes every decision accountable

Along the bottom of the diagram: **ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME.**

This is the same durable-workflow vocabulary from the state-layer map. It appears here because a stopped or compensated workflow is still a workflow. It still needs to record what happened, who asked, what effect was produced, and what the next allowed action is.

When a step is compensated, the system does not delete the step. It appends the compensation. When a workflow is cancelled, it does not vanish. It reaches a cancelled state with a receipt explaining why.

### 7. Point of no return means manual recovery, not automatic undo

After the yellow pin, the cyan arrow continues to **STEP B** and then to **MANUAL RECOVERY**, a blue box with a red X.

The red X matters. Past the point of no return, the system cannot compensate automatically. The effect is irreversible, or the compensation is too risky to run without a person reviewing it.

Manual recovery is not failure. It is an explicit state. It says: *this workflow has reached a condition that requires a human decision, and every step that led here is recorded and inspectable.*

The previous diagrams make this possible. The durable artifact, the side-effect receipt, and the checkpoint mean a human can see what was requested, what was attempted, what completed, and what the options are.

A longer workflow turns these one-step rules into a sequence of compensable and irreversible steps:

![On dark navy, a play button leads left-to-right through three blue steps — RESERVE FUNDS, UPDATE CASE, SEND REFUND — each with an acknowledgement loop. A PIVOT / POINT OF NO RETURN padlock sits before SEND REFUND. Failure in RESERVE FUNDS or UPDATE CASE triggers coral compensation steps — RELEASE FUNDS or RESTORE CASE — with their own acknowledgements. A coral dashed box encloses both compensation paths and ends in COMPENSATION FAILURE leading to MANUAL REVIEW, a red platform with a person and magnifier.](../diagrams/135-saga-compensation-irreversible-effects.png)

The same colour rules apply. Blue forward steps are business work. Coral steps are compensations — new side effects, not undos. The yellow pin is the point of no return, after which the only exit is forward or manual review. When two compensations both fail, the workflow does not invent a third one; it escalates to a person. That is the honest shape of a long-running cancellation.

---

## Case study — Alderman & Co, the cancellation that refunded twice

Alderman is a commercial lettings platform. When a tenant signs a contract, a sequence runs: credit check, deposit hold, first rent payment, welcome pack, access code.

### What they had

A workflow engine that allowed users to cancel a running process. Cancellation was implemented as an immediate `TerminateWorkflow` call.

The steps after the call stopped running, but any side effects already in flight were not checked. The workflow reached a `CANCELLED` state, and that was that.

### The cancellation

A tenant began signing a contract on a Friday afternoon. After the credit check passed and the deposit hold succeeded, the user changed their mind and pressed Cancel.

The workflow terminated. The deposit hold, however, had already been placed by the payment provider. The `CANCELLED` status told the tenant the process was stopped. It did not tell anyone that the deposit was held.

On Monday, the tenant signed a different property. Alderman's system started a new workflow. It placed a second deposit hold. The tenant's bank froze the account for suspected fraud, because two large holds from the same merchant appeared within hours.

The first hold expired automatically after five days, but the tenant had no access to funds until then.

### What they learned

The cancellation was treated as the end of the workflow, not as a state that required recovery.

The credit check was reversible — it was only a query. The deposit hold was reversible — a release could be issued. The first rent payment was the point of no return.

Their new workflow:
- **Credit check** — cancellable; no side effect.
- **Deposit hold** — reversible; on cancellation, the system issues a release command and waits for the provider's release receipt.
- **First rent payment** — point of no return; once the payment is sent, cancellation is no longer possible, and the workflow enters a manual recovery state.

### The fix

**Deadline carried with the contract.** Each offer has an expiry time. Steps derive their own timeouts from the remaining deadline.

**Cooperative cancellation.** A cancel request is an event, not a kill signal. Each step checks it at a safe checkpoint.

**Compensation as a first-class command.** A `ReleaseDeposit` command, validated, with its own receipt. It is not a database undo; it is a new side effect.

**Point of no return explicit.** The workflow records when the payment step begins and rejects cancellation after that.

**Manual recovery state.** If a payment is in an ambiguous state — provider accepted but receipt not yet confirmed — the workflow enters `MANUAL REVIEW` rather than `CANCELLED`.

### Results

- **Cancelled workflows with unrecorded side effects:** any number → 0.
- **Tenant deposit holds left in place after cancellation:** 14 in the month before the fix → 0.
- **New workflow starting before old side effect confirmed:** 3 → 0.
- **Mean time to resolve a cancellation:** 2–5 days → under 1 hour, because the workflow now emits explicit compensation commands and states.

### The line in their operations standard

*Cancel the computation after you cancel the effects, or admit that the effects are not cancelled and enter manual recovery.*

---

## Composition

A left-to-right step chain with two control inputs above, a compensation path below, and a point-of-no-return marker before the final recovery state.

**Upper left:** **USER CANCEL** — a teal person figure on a blue platform — sends a **dashed teal arrow** to **CANCELLATION** — a speech bubble on a teal platform. **CANCELLATION** sends **dashed teal arrows** to **STEP A** and **STEP B**.

**Lower left:** **TIMER** — a teal clock on a blue platform — sends a **dashed teal arrow** to **TIMEOUT** — an hourglass on a teal platform. **TIMEOUT** sends **dashed teal arrows** to **STEP A** and **STEP B**.

**Centre:** **STEP A** — a white card with a gear on a blue platform — then a **cyan arrow** to **STEP B** — an identical card. Between them, a **yellow map pin** labelled **POINT OF NO RETURN**.

**Below STEP A:** a **coral dashed arrow** drops to **COMPENSATE A** — a red box with circular arrows.

**Lower chain:** below the steps, four teal cards in a row — **ACKNOWLEDGEMENT** (check), **RECEIPT** (document), **CHECKPOINT** (flag), **RESUME** (play).

**Right:** from **STEP B**, a **cyan arrow** to **MANUAL RECOVERY** — a blue box with a red X.

## Element by element

**USER CANCEL** — a request from the outside.
**CANCELLATION** — the event that propagates the request.

**TIMER** — the system clock.
**TIMEOUT** — the system deciding the wait has exceeded its bound.

**STEP A / STEP B** — workflow stages. Step A is reversible; Step B is past the point of no return.

**POINT OF NO RETURN** — the boundary beyond which automatic cancellation is no longer safe.
**COMPENSATE A** — a new side effect that counteracts Step A.

**ACKNOWLEDGEMENT → RECEIPT → CHECKPOINT → RESUME** — the durable vocabulary, making every recovery decision auditable.

**MANUAL RECOVERY** — an explicit state for effects that cannot be undone automatically.

## Colour and flow semantics

- **Cyan arrows** carry the forward workflow from step to step.
- **Teal dashed arrows** carry cancellation and timeout — system or user control signals, not work.
- **Coral dashed** carries the compensation path — a recovery action, not a forward step.
- **Teal** on the bottom chain marks the durable-workflow vocabulary.
- **Red X** on **MANUAL RECOVERY** marks the end of automatic handling.
- **Yellow pin** is the visual warning: past this point, the workflow cannot be safely stopped.

## How to present it

**Open by naming the four concepts.** Deadline, cancellation, timeout, compensation. Then ask the room to define each. Most will blend at least two of them.

**Point at USER CANCEL and TIMER.** One is a person asking, the other is a system deciding. They both send dashed arrows to the steps, but the recovery may differ.

**Trace the deadline to the point of no return.** The yellow pin is not between any two arbitrary steps. It is where the remaining time makes continuing either safe or not useful.

**Make the cancellation point cooperative.** A cancel is not a kill. Ask what a safe checkpoint looks like for a real side effect in their system. If the answer is "we do not have one," that is the bug.

**Show compensation as a new side effect.** The red circular-arrow box is not a database rollback. Ask what the business inverse of their last committed step is. Usually it is another API call, another record, another event.

**Tell the Alderman story.** A cancelled workflow left a deposit hold in place. A new workflow placed a second hold. The bank froze the account. The fix was to issue a `ReleaseDeposit` compensation command and wait for its receipt.

**Point at MANUAL RECOVERY and ask when it is the right answer.** When the effect is irreversible or too risky to undo automatically. The red X says the system is no longer responsible alone.

**Close on the standard.** *Cancel the computation after you cancel the effects, or admit the effects are not cancelled and enter manual recovery.*

**Timing.** Twenty-five minutes. Thirty if the room maps one real workflow into cancellable, compensable, and irreversible steps, which usually finds a step currently treated as cancellable that is not.

---

## Lab and checkpoint

**Lab:** Map one real workflow in your system into cancellable, compensable, and irreversible steps. For each step, define the deadline, cancellation rule, timeout, and compensation. Identify any step treated as cancellable that is actually irreversible, and move it to manual recovery.

**Checkpoint:** Why is compensation a new side effect, not a rewind?

**Answer:** Because most real side effects cannot be rewound. A payment cannot be unmade; a deposit hold must be released by a new command. Compensation is the business inverse of the original effect, and it must be its own operation with its own receipt.

## Glossary

- **Cancellation** — a request from a user or system to stop the workflow.
- **Compensation** — a new side effect that offsets an earlier side effect.
- **Deadline** — the time by which the workflow must complete or stop.
- **Irreversible step** — a step whose effect cannot be undone, requiring manual recovery.
- **Manual recovery** — the human process that takes over when automatic compensation is unsafe.
- **Point of no return** — the step after which cancellation is no longer safe or useful.
- **Timeout** — the system deciding the workflow has taken too long.

## Sources

- Cancellation, timeout, and compensation patterns
- Sagas and irreversible side effects
- Workflow deadlines and points of no return
