# Diagram 147 — Recovery Drills, Runbooks, Ownership, and Receipts

![On dark navy, a top row of four blue platforms reads ALERT, TRIAGE, IDENTIFY WORKFLOW, FREEZE OR CONTINUE, connected by cyan arrows. Below each platform, a small teal shield icon is connected by a dashed line labelled RECEIPT CHAIN. A second row has RECONCILE EXTERNAL EFFECTS, REDRIVE OR COMPENSATE, VERIFY, CLOSE, also connected by cyan arrows and the same teal receipt chain. A coral dashed path from RECONCILE leads left to a red UNSAFE REPLAY box with a red X and a forbidden sign. To the right, a tall RUNBOOK panel lists OWNER, ACCESS, COMMANDS, SAFETY CHECKS, ROLLBACK, EVIDENCE with icons.](../diagrams/147-recovery-runbook-receipt-chain.png)

**Module:** Testing, correctness, and observability
**Role in the course:** how to turn a failure alert into a safe, rehearsed, attributable recovery sequence
**Layout:** two rows of recovery stages, a receipt chain under each, an unsafe replay path blocked, and a runbook panel on the right

---

## At a glance

**ALERT → TRIAGE → IDENTIFY WORKFLOW → FREEZE OR CONTINUE → RECONCILE EXTERNAL EFFECTS → REDRIVE OR COMPENSATE → VERIFY → CLOSE**.

A **RUNBOOK** on the side lists **OWNER, ACCESS, COMMANDS, SAFETY CHECKS, ROLLBACK, EVIDENCE**.

A **RECEIPT CHAIN** runs under every step.

And **UNSAFE REPLAY** is **BLOCKED**.

---

## What the diagram teaches

### 1. The runbook is an executable decision guide

The **RUNBOOK** is not a document for auditors. It is a guide the operator uses in the moment. It must answer the practical questions:

- **OWNER** — who is responsible for this recovery.
- **ACCESS** — who can run the commands.
- **COMMANDS** — which commands are allowed.
- **SAFETY CHECKS** — what to verify before each command.
- **ROLLBACK** — how to undo or compensate.
- **EVIDENCE** — what proves the recovery worked.

If any of these are missing, the operator will improvise. Improvisation in a live incident is how small failures become large ones.

### 2. The owner is a named role, not a hero

The **OWNER** in the runbook is a named role, not the person who happens to be online. It might be the on-call engineer, a domain lead, or a business owner.

Naming the owner matters because recovery decisions are business decisions. Approving a risky redrive, deciding to compensate, or closing an incident all have consequences. Somebody must own them.

The owner does not have to execute every command. But they are accountable for the recovery. They authorize the next step.

### 3. Access is scoped to the recovery role

**ACCESS** means the least-privilege commands the recovery role can run. Not every operator can redrive a payment. Not every operator can close an incident.

Scoped access prevents two things. It prevents an operator from running a command they do not understand. It also prevents an attacker who steals one credential from running arbitrary recovery commands.

Every recovery command should be previewed, confirmed, and attributed.

### 4. Commands are bounded and named

The **COMMANDS** in the runbook are not ad-hoc SQL. They are bounded, named, idempotent operations.

Examples: **reconcile external effects, redrive workflow, compensate action, close incident**. Each has a specific input, a safety check, an expected output, and a rollback path.

A runbook with open-ended commands is not a runbook. It is a suggestion.

### 5. Safety checks are the decision gate

Before any command, the operator runs the **SAFETY CHECKS**.

For **reconcile external effects**, the safety check might be: do we have the provider receipt? Do we know the workflow version? Do we know the expected state?

For **redrive**, the safety check might be: has the root cause stopped? Is the queue drained of duplicates? Is the idempotency key still valid?

Safety checks are not optional. They are the gate. The operator does not proceed until the check is documented.

### 6. Reconcile before redrive

The diagram shows **RECONCILE EXTERNAL EFFECTS** before **REDRIVE OR COMPENSATE**.

Reconciliation means comparing the internal state with the external truth. Did the payment happen? Does the provider have the idempotency key? Is there a receipt?

Redrive without reconciliation is unsafe replay. If the effect already happened, redrive will repeat it. If the effect did not happen, redrive is correct. The only way to know is to reconcile first.

### 7. Unsafe replay is blocked

The red **UNSAFE REPLAY** box has a red X and a forbidden sign. It is the shortcut that the diagram rejects.

Unsafe replay means resending all failed messages, restarting all failed workflows, or retrying all failed operations without understanding the state. It is the most common recovery mistake.

The diagram forces the operator to reconcile, choose redrive or compensate, verify, and close. Replay is not one of those choices.

### 8. The receipt chain makes recovery reviewable

Every step has a small teal shield below it. These are the **RECEIPT CHAIN**.

Every action produces a receipt. The alert receipt. The triage receipt. The workflow identity. The freeze decision. The reconciliation result. The redrive or compensate command. The verification. The closure.

The receipt chain is the audit trail. It makes the recovery as reviewable as the original automated work.

![On dark navy, a cyan arrow labelled CLIENT / AGENT / HUMAN INTENT passes through an INTAKE gate into a blue STATE LAYER MAP. The map is divided into four horizontal bands: PROPOSAL (cyan) with REQUEST and PLAN, DECISION (green) with APPROVAL and POLICY, EFFECT (red) with SIDE EFFECT and COMPENSATION, and RECORD (teal) with ARTIFACT and BUSINESS RECORD. Teal lines show ARTIFACT flowing down into BUSINESS RECORD. Red and teal arrows show that ARTIFACT goes into the business record only after a green check. A coral dashed arrow from SIDE EFFECT is labelled IRREVERSIBLE and joins a red X. A legend at bottom shows cyan for proposal, green for decision, red for effect, and teal for record.](../diagrams/128-artifact-receipt-business-record.png)

That diagram shows the same receipt idea for normal work. An artifact is the proof that a side effect happened, and it becomes the business record. In recovery, every step is also a side effect. The recovery command itself needs a receipt. The close step produces a receipt. The runbook is the policy gate that decides when the next effect may happen. Without this structure, recovery is just another effect with no proof.

### 9. Verify before close

**VERIFY** is the second-to-last step. The operator must check that the business state, queues, artifacts, receipts, customer communication, and follow-up actions are correct before closing.

Closing is not just clicking a button. It is the formal end of the incident. The close receipt must include the evidence that the recovery succeeded.

### 10. Recovery drills prove the runbook while the system is healthy

The runbook is not useful until it has been rehearsed. A **recovery drill** runs the runbook against a non-production or degraded environment to prove the commands and the receipt chain.

The drill should inject a controlled failure, follow the runbook, and verify the outcome. If the runbook does not work during a drill, it will not work during an incident.

### 11. The freeze decision protects the work that is still healthy

**FREEZE OR CONTINUE** is not an emergency stop for the whole system. It is a scoped decision that halts only the dangerous automation around the affected workflows.

A bad freeze can do as much harm as a bad redrive. If an operator stops every queue, payment, or worker while trying to recover five refunds, unrelated customers wait for no reason. The freeze must name the exact workflows or commands to pause and leave the rest running.

This is also the natural place for an escalation path. If the runbook says "freeze and escalate," the backup owner, the domain lead, and the business approver must already be written down. A runbook that runs out of instructions at three in the morning is a guess.

### 12. Every repair command is attributable and wrapped in evidence

A recovery command is not anonymous. It carries the actor who approved it, the reason for the intervention, the incident it belongs to, and the workflow it targets. That identity turns every repair action into a first class business event.

In the Next.js console, this means separate diagnose, approve, execute, and verify permissions. In the Python back end, commands need a reason and actor identity. A redrive without an owner is just a blind retry.

The command itself must be idempotent. The same reconcile, redrive, compensate, or close incident command, issued twice because a network call timed out, must produce the same receipt and must not change the business meaning. Idempotency lets the operator retry safely while the receipt chain shows what already happened.

After the command finishes, the system checks post recovery invariants and stores an evidence bundle. Counts match, no duplicate customer emails, queues are drained, receipts are present, and customer status is correct. The close step records that the evidence has already been produced.

---

## Case study — Acme Refunds, the outage that needed a safe redrive

Acme's payment provider has an outage. Five refund workflows are stuck in the queue. When the provider comes back, the team wants to clear the backlog.

### What they had

The operations dashboard had a button: **Retry All Failed**. It would re-send every failed message to the queue.

There was no runbook. No owner. No reconciliation. No verification. Just a retry button.

### The incident

The provider outage ended. The operator clicked **Retry All Failed**. The messages were re-sent to the queue. The workers picked them up.

Two of the workflows had already succeeded during the outage. The provider had accepted the refund but the local state had not been updated before the worker crashed. When the messages were retried, the workers re-sent the refund requests. The provider's idempotency key prevented duplicates, but the workers also updated the local state.

The local state had not been updated before the outage, so the workers saw the refund as not completed. They sent it again. The provider said "already done" and returned the same receipt. The workers then updated the local state.

No duplicate payment occurred, but five customers received two refund confirmation emails. The customer service team spent a day explaining the duplicate emails.

Worse, the retry did not reconcile the queues first. Some messages were out of order. One case was compensated twice because the compensating transaction was also retried.

### The runbook design

The new runbook for a payment-provider outage has these steps:

1. **ALERT:** provider-failure alert with affected workflow IDs.
2. **TRIAGE:** on-call owner confirms the provider is back and the root cause is resolved.
3. **IDENTIFY WORKFLOW:** list the affected refund workflows and their last known state.
4. **FREEZE OR CONTINUE:** freeze automatic redrive for these workflows.
5. **RECONCILE EXTERNAL EFFECTS:** query the provider with stable keys. Mark each workflow as provider-accepted, provider-rejected, or provider-unknown.
6. **REDRIVE OR COMPENSATE:**
   - provider-accepted: complete locally.
   - provider-rejected: follow the approved retry or compensation path.
   - provider-unknown: escalate.
7. **VERIFY:** check counts, receipts, customer status, and the absence of duplicates.
8. **CLOSE:** record the closure evidence and follow-up.

The runbook names the owner, the required access, the allowed commands, the safety checks, the rollback, and the evidence.

The **Retry All Failed** button is removed. It is replaced by a **Reconcile and Redrive** command that requires owner confirmation and produces a receipt.

### Results

- **Duplicate customer emails after outage recovery:** 5 → 0.
- **Double compensation after retry:** 1 → 0.
- **Time to safely clear a provider-outage backlog:** 4 hours of firefighting → 20 minutes of runbook execution.
- **Auditable recovery record:** none → every step has a receipt.

### The line in their operations standard

*Every known failure mode has a named owner, a scoped runbook, a reconciliation step, and a receipt chain. Unsafe replay is not a recovery command.*

---

## Composition

Two rows of recovery stages, a receipt chain, an unsafe-replay block, and a runbook panel.

**Top row (four blue platforms):**
- **ALERT** — bell.
- **TRIAGE** — clipboard with magnifier.
- **IDENTIFY WORKFLOW** — flow chart.
- **FREEZE OR CONTINUE** — snowflake and play button.

**Cyan arrows** connect the top row to the second row.

**Second row (four blue platforms):**
- **RECONCILE EXTERNAL EFFECTS** — globe and database.
- **REDRIVE OR COMPENSATE** — gear and dollar sign.
- **VERIFY** — shield with check.
- **CLOSE** — green check.

**Teal dashed line** under both rows, with small teal shield icons, labelled **RECEIPT CHAIN**.

**Coral dashed path** from **RECONCILE EXTERNAL EFFECTS** to a red **UNSAFE REPLAY** box, then to a red **BLOCKED** forbidden sign.

**Right side:** **RUNBOOK** panel with six rows:
- **OWNER** — person.
- **ACCESS** — lock.
- **COMMANDS** — terminal.
- **SAFETY CHECKS** — shield.
- **ROLLBACK** — undo arrow.
- **EVIDENCE** — folder.

## Element by element

**ALERT** — the failure signal.
**TRIAGE** — initial assessment.
**IDENTIFY WORKFLOW** — find the affected work.
**FREEZE OR CONTINUE** — stop dangerous automation.

**RECONCILE EXTERNAL EFFECTS** — compare internal and external truth.
**REDRIVE OR COMPENSATE** — repair by retry or undo.
**VERIFY** — check the result.
**CLOSE** — end the incident.

**RECEIPT CHAIN** — the audit trail under every step.

**UNSAFE REPLAY** — the forbidden shortcut.

**RUNBOOK** — the executable guide.

## Colour and flow semantics

- **Cyan arrows** carry the recovery flow from alert to close.
- **Teal dashed** carries the receipt chain under every stage.
- **Coral dashed** marks the unsafe replay path, blocked by a red forbidden sign.
- The **RUNBOOK panel** is on the right because it is the reference for every step.
- The **receipt chain shields** are small and repeated, showing that evidence is collected at each step.

## How to present it

**Ask how the room recovers from a production alert.** Most will describe ad-hoc commands or a retry button. Ask them where the runbook is.

**Point at the runbook and read the six fields.** Owner, access, commands, safety checks, rollback, evidence. Ask which of these are written down for their common incidents.

**Trace the recovery flow.** Alert → triage → identify → freeze/continue → reconcile → redrive/compensate → verify → close. Ask how many of these steps they do today.

**Emphasize reconcile before redrive.** Redrive without reconciliation is unsafe replay. The external effect may already have happened.

**Point at the blocked unsafe replay.** This is the central warning. Do not retry all failed messages. Do not restart all failed workflows. Reconcile first.

**Show the receipt chain.** Every step produces a receipt. The recovery must be as reviewable as the original work.

**Tell the Acme story.** The Retry All Failed button caused duplicate emails and double compensation. The fix: a runbook with reconcile, redrive/compensate, verify, close, and a receipt chain. The retry button was removed.

**Talk about drills.** A runbook that has not been rehearsed is a wish. Run the runbook against a controlled failure in a safe environment.

**Close on the standard.** *Every known failure mode has a named owner, a scoped runbook, a reconciliation step, and a receipt chain. Unsafe replay is not a recovery command.*

**Ask who can redrive a failed workflow right now.** If the answer is "anyone with queue access," the recovery is not governed. A named command should require a named actor, a reason, and a workflow link.

**Ask what the close receipt must contain.** Counts, receipts, customer status, queue depth, and the absence of duplicates. If the team cannot list these, they are closing incidents on hope.

**Use the lab prompt as a five minute exercise.** Have the room write a one page runbook for an ambiguous refund completion with trigger, owner, access, diagnosis, freeze, reconciliation, repair, verification, escalation, and closure receipt.

**Mention the sources in context.** Amazon SQS dead letter queues hold the failed work, the Azure Compensating Transaction pattern describes undo, and OpenTelemetry messaging conventions make the recovery commands traceable.

**Timing.** Twenty-five minutes. Thirty if the room writes a one-page runbook for one real incident type.

---

## Lab and checkpoint

**Lab:** Write a one-page runbook for one real incident type in your system. Include trigger, owner, access, diagnosis, freeze, reconciliation, repair, verification, escalation, and closure receipt. Define the named, bounded repair commands and the evidence that must be collected. Ensure unsafe replay is not an option.

**Checkpoint:** Why must reconciliation come before redrive?

**Answer:** Because redrive without reconciliation is unsafe replay. The external effect may already have happened, and retrying could create duplicates. Reconciling first checks what actually happened before deciding whether to redrive, compensate, or close.

## Glossary

- **Close receipt** — the evidence collected when an incident is closed.
- **Compensate** — the repair action that offsets an external effect.
- **Freeze** — the step that protects healthy work while the incident is contained.
- **Named owner** — the role responsible for the runbook.
- **Receipt chain** — the durable records from every recovery step.
- **Reconcile** — the step that determines what actually happened before repair.
- **Recovery** — the process of returning the system to a correct state.
- **Redrive** — retrying work after it is safe to do so.
- **Rollback** — the plan for reversing changes.
- **Runbook** — the executable decision guide for an incident type.
- **Safety check** — the gate before a repair command is allowed.
- **Unsafe replay** — retrying work without reconciliation, which is blocked.
- **Verify** — the step that confirms the repair worked.

## Sources

- Incident runbooks and recovery design
- Reconciliation before redrive
- Dead-letter queues and compensating transactions
