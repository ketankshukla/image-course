# Diagram 135 — Sagas, Compensations, and Irreversible Effects

![On dark navy, a play button starts a left-to-right SAGA with three blue steps — RESERVE FUNDS, UPDATE CASE, SEND REFUND. The first two steps have teal acknowledgement loops and coral dashed arrows dropping to compensation steps — RELEASE FUNDS under RESERVE FUNDS, RESTORE CASE under UPDATE CASE. A PIVOT / POINT OF NO RETURN padlock sits before SEND REFUND, with a forward path leading to RECEIPT, CHECKPOINT and RESUME. The two coral compensation paths are enclosed in a dashed coral box that ends in a red COMPENSATION FAILURE arrow to a red MANUAL REVIEW platform with a person and magnifier.](../diagrams/135-saga-compensation-irreversible-effects.png)

**Module:** Distributed workflow patterns
**Role in the course:** the saga pattern — a long business transaction of local steps, compensations, and a point of no return
**Layout:** a left-to-right step chain with compensations below and a manual-review exit for failed compensation

---

## At a glance

A **SAGA** of three steps: **RESERVE FUNDS → UPDATE CASE → SEND REFUND**.

The first two steps are **compensable**. Under each, a coral dashed arrow drops to a compensation: **RELEASE FUNDS**, **RESTORE CASE**.

Before **SEND REFUND**, a **PIVOT / POINT OF NO RETURN** padlock.

After the pivot, the forward path leads to **RECEIPT, CHECKPOINT, RESUME**.

And if both compensations fail, a **COMPENSATION FAILURE** arrow leads to **MANUAL REVIEW**.

A saga breaks a large operation into local transactions. Each step records how to counteract it, until the pivot makes reversing impossible.

---

## What the diagram teaches

### 1. A saga is not a distributed transaction

The diagram does not show two-phase commit, resource managers, or a transaction monitor. It shows business steps, each with its own local state and its own compensation.

A distributed transaction tries to make many systems commit or abort together. A saga accepts that each system commits independently, and uses compensating actions to keep the overall process valid.

That means a saga cannot *roll back* the world. It can only run new commands that counteract the effects of previous commands. The difference is not subtle. A rollback deletes history. A compensation appends it.

### 2. Compensable steps record their own counteractions

**RESERVE FUNDS** has **RELEASE FUNDS** beneath it. **UPDATE CASE** has **RESTORE CASE** beneath it.

The compensation is not an afterthought. It is part of the step's design. When the forward step succeeds, the system records the information needed to run the compensation — the reservation ID, the previous case state, the actor and time.

That information must be durable before the saga advances. If the workflow crashes after the step succeeds but before the compensation data is recorded, the step cannot be safely undone.

### 3. The pivot is the boundary between reversible and irreversible

The **PIVOT / POINT OF NO RETURN** padlock sits before **SEND REFUND**. After that point, the external effect has happened, or will happen, and the previous compensations no longer make sense.

You cannot release funds that have already been sent. You cannot restore a case to its previous state once the customer has been told the refund is in motion.

The pivot is not a technical boundary. It is a business boundary. The system must have authority, validation, and durable compensation data before it passes the pivot.

### 4. Forward recovery after the pivot is usually the right answer

After the pivot, the only safe path is forward. If **SEND REFUND** fails, the saga retries. If it cannot succeed, the workflow enters **MANUAL REVIEW**.

The diagram does not draw a coral compensation arrow from **SEND REFUND**. It is not because the step cannot fail. It is because the effect is irreversible, so a compensation is not a valid counteraction.

This is the hardest thing to explain to rooms raised on transaction systems: sometimes the right answer is not to undo, but to finish or to ask a human.

### 5. Compensation is a first-class command, not a database undo

The compensation boxes **RELEASE FUNDS** and **RESTORE CASE** are red with circular arrows. They are not dashed lines back to the start. They are new commands.

Each compensation must be validated by the same invariants as a forward step. Releasing funds may require a manager's authority. Restoring a case may not be allowed if another process has since changed it.

And each compensation must produce its own receipt. The saga is not compensated until the compensation receipt is durable.

The previous volume's diagram on deadlines and cancellation made the same point. COMPENSATE A was a new side effect, not a rewind.

![On dark navy, a teal USER CANCEL figure sends a dashed arrow to a CANCELLATION speech bubble that reaches STEP A and STEP B. A TIMER clock sends a dashed arrow to a TIMEOUT hourglass that also reaches both steps. A yellow POINT OF NO RETURN pin sits between the steps; before it, a coral dashed arrow drops from STEP A to a red COMPENSATE A box. After the pin, the cyan arrow leads to a blue MANUAL RECOVERY box with a red X. A teal chain of ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT and RESUME runs below.](../diagrams/132-deadline-cancel-timeout-compensation.png)

The saga in this diagram extends that single-step idea into a sequence. Each compensable step has its own counter-command, and the point of no return is shared across the whole saga.

### 6. Compensations can fail, and that is not exceptional

The two coral compensation paths are enclosed in a dashed coral box that ends at **COMPENSATION FAILURE → MANUAL REVIEW**.

Compensation is not guaranteed to work. The release-funds command may be rejected. The restore-case command may be blocked by a concurrent change. The provider may be down.

When a compensation fails, the saga cannot continue automatically. It escalates to a person. The diagram draws a red path, not a loop, because the machine has run out of valid automatic actions.

That is a feature, not a bug. A system that silently swallows a failed compensation is worse than one that escalates, because it appears clean while the business state is wrong.

The escalation is only safe if the operator has a runbook that traces every receipt in the chain. The first chain records the forward steps and the attempted compensation. The second chain records the operator's reconciliation, redrive, and verification. An unsafe replay — running the workflow again from the start — must be rejected because it could duplicate the original side effect. The runbook is the difference between a manual review that fixes the state and a manual review that guesses.

### 7. The durable chain on the right is the only way to make the saga auditable

After the pivot, the forward path runs through **RECEIPT, CHECKPOINT, RESUME**.

That chain is not optional decoration. It is what makes the saga safe. Each step produces a receipt. Each receipt is checkpointed. If the saga is suspended and resumed, it continues from the last checkpoint.

Without those artifacts, the saga cannot be restarted, audited, or explained. The durable record must say what was requested, which identity owns it, what changed, which attempt produced the change, and what may legally happen next.

### 8. Each step is owned by the service that commits its state

The diagram names the saga steps by what they do, but each local commit is owned by a service: the ledger owns the reservation, the case service owns the status, and the provider owns the refund. A compensable step must be undone by the same owner. The trace begins by listing local transactions and the service that owns each state change. A saga table should capture step, owner, local commit, compensation data, idempotency key, pivot status, timeout, and manual-recovery owner. Without this ownership, a compensation is a guess.

### 9. The UI and tests protect the durable record

The Next.js case view should explain pending, compensating, compensated, and manual states, but keep the workflow record read-only. Mutations go through authenticated server boundaries and return stable IDs or receipts. In Python, each step and compensation should be a durable, typed record; tests should fail after every forward and compensation boundary so fixtures can replay a partial failure without network calls. A restart can then continue from the last checkpoint without inventing new business meaning.

---

## Case study — Meridian Payments, the refund that could not be un-sent

Meridian processes B2B refunds for supply-chain customers. A refund workflow has three steps: reserve the funds in the ledger, update the case status, and send the payment through the provider.

### What they had

A workflow engine with a compensation feature. Every step had an associated compensation action that the engine would call if the workflow failed.

The engine's mental model was a transaction. If any step failed, the engine would run compensations in reverse order. That is a saga, but a naive one.

### The incident

A refund workflow ran: reserve funds, update case to `REFUND PENDING`, then call the provider.

The provider call returned a network timeout. The engine treated this as a step failure and triggered the compensation chain.

It released the reserved funds. It restored the case to its previous state. But the provider had already accepted the payment. The provider's response was delayed, not lost.

The customer received the refund. The case was restored to `OPEN`. The funds were released back to the general pool.

The same refund was then submitted again by a support agent who saw the case had reverted. The customer received it twice.

### Why the compensation was wrong

The **SEND REFUND** step had crossed the point of no return before the engine noticed the failure. The provider accepted the payment. The payment could not be un-sent.

The engine's reverse-compensation model assumed every step was undoable. It had no concept of an irreversible step. It treated the provider timeout as a failure of the step, not as an ambiguous external state.

### The saga redesign

**RESERVE FUNDS** — compensable. Release the reservation if the provider has not been called.

**UPDATE CASE** — compensable. Restore the previous case state if the provider has not been called.

**PIVOT / POINT OF NO RETURN** — before the provider call. The case is marked `REFUND SUBMITTED` and the payment is irreversible.

**SEND REFUND** — not compensable. If it times out, the workflow checks the provider using the stable operation key. If the provider accepted, the workflow completes forward. If the provider rejected, it may retry. If the answer is unknown, the workflow enters `MANUAL REVIEW`.

**Compensation failure** — if `RELEASE FUNDS` or `RESTORE CASE` fails, the workflow enters `MANUAL REVIEW` with full correlation and a description of the attempted compensation.

### Results

- **Refunds double-sent because compensation ran past the point of no return:** 2 in the month before the fix → 0.
- **Cases left in `REFUND PENDING` after the payment was sent:** 6 → 0.
- **Compensation actions that failed and were silently swallowed:** 4 → 0, because every failed compensation now escalates.
- **Average time to resolve a stuck refund:** 4 hours → 20 minutes, because the workflow exposes the manual-review state and the reason.

### The line in their engineering standard

*Before the pivot, compensation is a new command. After the pivot, the only honest choices are to finish, to reconcile, or to escalate to a person.*

---

## Composition

A left-to-right saga chain with compensations below and a failed-compensation exit.

**Left:** a **play button** on a blue platform, starting the **SAGA**.

**Three blue step platforms, left to right:**
- **RESERVE FUNDS** — database with a dollar icon.
- **UPDATE CASE** — folder with a gear icon.
- **SEND REFUND** — paper plane icon.

**Under each of the first two steps:** a **coral dashed arrow** drops to a red compensation platform:
- **RELEASE FUNDS** — circular arrows.
- **RESTORE CASE** — folder with a counter-arrow.

**Between UPDATE CASE and SEND REFUND:** a **PIVOT / POINT OF NO RETURN** padlock on a teal platform.

**Right of SEND REFUND:** a **teal arrow** through **RECEIPT, CHECKPOINT, RESUME** — three green badges.

**Compensation failure path:** a **dashed coral box** encloses both compensation steps and leads to a **red arrow labelled COMPENSATION FAILURE** → **MANUAL REVIEW** — a red platform with a person and magnifier icon.

## Element by element

**SAGA** — the long business transaction.
**RESERVE FUNDS / UPDATE CASE / SEND REFUND** — the local steps.

**ACKNOWLEDGEMENT** — the step's durable receipt.
**RELEASE FUNDS / RESTORE CASE** — compensations, not undos.

**PIVOT / POINT OF NO RETURN** — the boundary after which reverse compensation is no longer valid.

**RECEIPT / CHECKPOINT / RESUME** — the durable forward chain after the pivot.

**COMPENSATION FAILURE** — a compensation that could not be completed.
**MANUAL REVIEW** — the human escalation point.

## Colour and flow semantics

- **Cyan arrows** carry the forward saga steps.
- **Teal** marks the acknowledgement loop above each step and the forward chain after the pivot.
- **Coral dashed** carries the compensation paths — recovery, not forward progress.
- **Red** on compensation boxes and the failure-to-manual path marks the limit of automatic action.
- **Yellow padlock** marks the pivot as a deliberate, named boundary.
- The **enclosing dashed coral box** around the two compensations says compensation failure is a single class of outcome, not one failure per step.

## How to present it

**Start by asking what happens when a long workflow fails halfway.** Most rooms will say "rollback." Ask them to define rollback. Usually it means "undo." Then say the diagram has no undo.

**Point at the first two steps and their compensations.** RESERVE FUNDS can be RELEASED. UPDATE CASE can be RESTORED. These are new commands, not database undos.

**Point at the pivot.** The padlock is before SEND REFUND. After that, the money is in motion. Ask what the compensation for "send refund" would be. If the answer is "ask the bank to recall it," that is a manual process, not an automatic undo.

**Trace the compensation failure path.** Both compensations can fail, and the result is MANUAL REVIEW. Ask what their system does when a compensation cannot be completed. If the answer is nothing, that is a hidden failure.

**Tell the Meridian story.** Provider timeout after the payment was accepted. The engine compensated and reverted the case. A support agent resubmitted the refund. The customer got it twice.

**Emphasize forward recovery.** After the pivot, the only safe automatic path is to finish or to reconcile. The compensation model no longer applies.

**Ask the room to classify their own steps.** Which are compensable? Which are pivot? Which are irreversible? Most teams have at least one step treated as compensable that is not.

**Run the Acme thought exercise.** A reserve, a case update, then an ambiguous payment call. Did the provider accept the stable operation key? Finish forward if yes, compensate if no, pause for manual recovery if unknown.

**Pose the checkpoint question.** "Must compensation restore the exact original data?" No. It applies business-specific corrective work that returns the process to a valid state while respecting later concurrent changes.

**Use the trip analogy.** A trip can undo a hotel reservation, but boarding a flight is a point after which recovery must follow a new plan.

**Cite the sources.** The pattern comes from the original Saga paper, the Azure Saga pattern, and the Azure Compensating Transaction pattern.

**Close on the standard.** *Before the pivot, compensation is a new command. After the pivot, the only honest choices are to finish, to reconcile, or to escalate to a person.*

**Timing.** Twenty-five minutes. Thirty if the room maps one real multi-step workflow and marks the pivot, which usually exposes at least one irreversible step currently treated as compensable.

---

## Lab and checkpoint

**Lab:** Map one multi-step workflow into compensable, pivot, and irreversible steps. For each compensable step, write the compensation command and the failure path. For the pivot step, decide the forward-recovery rule and the manual-escalation path. Ensure every step is owned by the service that commits its state.

**Checkpoint:** Why is a saga not a distributed transaction?

**Answer:** Because a saga does not hold locks across services and cannot atomically roll back all steps. It uses local commits and compensating commands. Some steps are irreversible, and after the pivot the only honest choices are to finish, reconcile, or escalate.

## Glossary

- **Compensable step** — a step that can be undone by a counteracting command.
- **Compensation** — a first-class command that offsets a previous step.
- **Distributed transaction** — an atomic commit across multiple services, which a saga is not.
- **Durable chain** — the auditable history of the saga.
- **Forward recovery** — continuing the workflow after a pivot rather than undoing.
- **Irreversible step** — a step that cannot be undone and requires manual recovery.
- **Manual review** — the human process for a failed or ambiguous compensation.
- **Pivot** — the boundary between compensable and irreversible steps.
- **Saga** — a long-running workflow with local commits and compensations.
- **Step owner** — the service that commits state for a given step.

## Sources

- Saga pattern and compensating transactions
- Azure Saga and compensating-transaction patterns
- Forward recovery and manual escalation
