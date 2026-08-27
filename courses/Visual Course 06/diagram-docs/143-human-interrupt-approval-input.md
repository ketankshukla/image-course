# Diagram 143 — Human Interrupts, Approvals, and Missing Input

![On dark navy, a WORKFLOW play button sends a cyan arrow through a WAITING HUMAN gate to a large blue WAITING HUMAN platform. On it, three white cards: APPROVAL REQUEST with a person icon, MISSING INPUT with a question mark, and OPERATOR INTERRUPT with an alarm. The APPROVAL REQUEST card lists EXACT ACTION, EVIDENCE, RISK, AMOUNT, EXPIRY, APPROVER. From the WAITING HUMAN platform, four teal arrows fan right to APPROVE, DENY, EDIT, and SUPPLY INPUT. Below, a teal durable chain runs left to right: EVENT, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME. From RESUME, a red dashed arrow leads to STALE APPROVAL, then to REVALIDATE, with a red X on the stale step.](../diagrams/143-human-interrupt-approval-input.png)

**Module:** Human-in-the-loop, steering, and recovery
**Role in the course:** the human-in-the-loop pattern — pausing safely for a precise, attributable decision
**Layout:** workflow reaches a wait, three kinds of human request, four possible responses, and a stale-approval revalidation loop

---

## At a glance

A **WORKFLOW** reaches **WAITING HUMAN**.

Three possible cards: **APPROVAL REQUEST, MISSING INPUT, OPERATOR INTERRUPT**.

An approval request lists **EXACT ACTION, EVIDENCE, RISK, AMOUNT, EXPIRY, APPROVER**.

Four possible human responses: **APPROVE, DENY, EDIT, SUPPLY INPUT**.

And below, the durable chain: **EVENT, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME**.

A **STALE APPROVAL** is revalidated before it is used.

---

## What the diagram teaches

### 1. There are three reasons to wait for a human

**APPROVAL REQUEST** — the workflow has a proposed action that needs human authorization.
**MISSING INPUT** — the workflow needs a fact from a person.
**OPERATOR INTERRUPT** — a person needs to stop or steer the workflow because of an incident.

These are not the same. An approval is about permission. Missing input is about data. An interrupt is about control.

The diagram draws them as three cards on the same waiting platform because the workflow pauses in the same way, but the contract for each is different.

### 2. An approval request is a contract, not a blank cheque

The **APPROVAL REQUEST** card lists six items:

**EXACT ACTION** — not "issue refund" but "issue refund of £40.00 to account 12345 using operation key ABC".
**EVIDENCE** — the data the approver can review.
**RISK** — what could go wrong.
**AMOUNT** — the scope of the action.
**EXPIRY** — when the approval expires if not acted on.
**APPROVER** — the named role or person allowed to decide.

If the request is missing any of these, it is not a contract. The human is being asked to sign a blank cheque.

### 3. Missing input is a durable wait with a responsible responder

**MISSING INPUT** is a request for a fact. It is not a failure. It is a normal workflow state.

The missing input should identify exactly what is needed, who can supply it, and by when. The workflow must not make a business decision until the input arrives.

This is the same durable wait pattern from the scheduled and event-triggered diagram. The workflow releases the worker, checkpoints the wait, and resumes when the input arrives.

![On dark navy, three entry paths converge on a DEDUP + CORRELATION GATE. From the top, a WORKFLOW ID: SCHEDULE TIMER with a calendar. From the middle, a WORKFLOW ID: DOMAIN EVENT with an antenna. From the bottom, a WORKFLOW ID: EXTERNAL CALLBACK with a globe. The gate has a red path to UNKNOWN CALLBACK. Past the gate, WORKFLOW RUNNING leads to WAIT WITHOUT WORKER, then RESUME. A red path from WAIT WITHOUT WORKER leads to EXPIRED DEADLINE. From RESUME, four teal arrows fan to ACKNOWLEDGEMENT PATH, RECEIPT PATH, CHECKPOINT PATH, and DURABLE RESUME PATH.](../diagrams/136-schedule-event-external-resume.png)

That diagram's three triggers — schedule, event, callback — are the same in principle as the human responses in this one. A missing input is an event or callback from a person. The workflow must authenticate it, deduplicate it, and resume from the checkpoint. The EXPIRED DEADLINE path is the same as an approval that expires before the human responds.

### 4. Operator interrupt is a control action, not a chat message

**OPERATOR INTERRUPT** is a person saying *stop, pause, or change direction*. It is not a casual message. It is an authenticated control event.

The interrupt must be correlated to a running workflow, verified as coming from an authorized operator, and recorded as a typed event. The workflow must respond to it as a command, not as a suggestion.

### 5. The four human responses are typed events

**APPROVE** — the human agrees to the exact action as described.
**DENY** — the human refuses it. The workflow must stop the action and record the refusal.
**EDIT** — the human modifies the action or the scope. The workflow must produce a new approval request for the edited action.
**SUPPLY INPUT** — the human provides the missing fact. The workflow resumes with the new data.

Each response is recorded as a typed event. It has an actor, a timestamp, and a correlation to the original request. The workflow does not move on from a human response until the response has been acknowledged and checkpointed.

### 6. Approval applies only to the reviewed state

The teal durable chain below the waiting platform — **EVENT, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME** — shows that the human's decision is made durable.

But the decision is only valid for the state that was reviewed. If the evidence, amount, policy, or inputs change after the approval, the approval is stale.

### 7. Stale approval is revalidated, not ignored

The red dashed path from **RESUME** to **STALE APPROVAL** to **REVALIDATE** is the diagram's safety rule.

A stale approval is an approval that was correct when given but no longer matches the current state. It is not ignored. It is revalidated. The workflow presents the new state to the approver and asks for a fresh decision.

This is the difference between an approval being *historically valid* and *currently usable*. A stale approval remains in the record as evidence of what the person saw. It just cannot be used to execute a changed action.

### 8. Human-in-the-loop is not a generic pause

The most common mistake is to use a generic *waiting for human* status with no contract. The workflow pauses, and at some point a person clicks something, and the workflow resumes with no record of what the person saw.

That is dangerous because the human cannot be held accountable for a decision they did not see. The workflow cannot explain why it acted on a vague click. The diagram forces the request to be specific and the response to be durable.

### 9. The approval contract must name the approver, the policy basis, and the scope

An approval request is not a generic yes-or-no prompt. It is a bounded authorization with an owner. The contract must name the **APPROVER** role or person, and the workflow must verify that the responder actually belongs to that role for the right tenant and amount.

It should also carry the **POLICY BASIS** — the rule, exception, or evidence version the request claims to satisfy. That basis gives the approver the context to decide and gives the workflow a way to detect a material change later. Without it, an approval can be replayed against a newer version of the rules and look the same even though the decision should not have been the same.

The workflow records the actor, role, and version so that every approval can be traced to an authorized decision.

### 10. Material changes are detected by comparing the reviewed state to the current state

A stale approval is not just an old approval. It is an approval whose reviewed state no longer matches the state at execution. The diagram calls this a **MATERIAL CHANGE**. A material change is any change that would affect the decision: amount, evidence, policy, scope, or risk.

The workflow must store the **ACTION**, **EVIDENCE VERSIONS**, **POLICY VERSION**, and **AMOUNT** inside the approval request so it can re-run the comparison just before execution. If the current state differs from the reviewed state, the workflow does not execute on the old approval. It goes back to the waiting platform with a new request that explains what changed and what is now proposed.

The old approval stays in history as evidence, but it cannot approve an action that has changed since it was reviewed.

---

## Case study — Wrenfield Payments, the £40 approval that became £60

Wrenfield processes customer refunds. A supervisor must approve refunds above a threshold.

### What they had

The agent generated a refund request and sent it to a supervisor for approval. The request showed the customer, the case ID, and a button to approve.

The button did not show the exact amount. It did not show the evidence the agent had used. It did not expire.

### The incident

A supervisor approved a refund for Maya's case. At the time, the agent had calculated a £40 refund. Between approval and execution, the agent re-ran a calculation and discovered an additional charge. The refund amount changed to £60.

The workflow executed the £60 refund using the old approval. It did not re-validate. The supervisor had approved a refund, not a specific amount, so the system treated the approval as covering the new amount.

When the supervisor reviewed the monthly report, they saw a £60 refund they had not approved. The customer had received the correct amount, but the approval process had failed.

### The precise approval contract

The new workflow sends the supervisor an approval request with the exact action, evidence, risk, amount, expiry, and approver.

The exact action is: *Issue refund of £40.00 to account 12345 using operation key ABC.*

The evidence includes the original payment, the policy terms, and the calculation breakdown.

The risk notes that the refund is non-reversible once sent.

The amount is the specific number.

The expiry is 24 hours.

The approver is the supervisor role.

If any fact changes before execution, the workflow detects a stale approval. It does not execute. It sends a fresh request with the new £60 action.

### Results

- **Refunds executed at a different amount than approved:** 7 in one quarter → 0.
- **Approvals without exact action or amount:** 100% → 0.
- **Stale approvals executed without revalidation:** any number → 0.
- **Time to investigate an approval decision:** hours of log search → seconds, because the request and response are stored together.

### The line in their operations standard

*An approval is a contract with an exact action, evidence, risk, amount, expiry, and approver. If any of those change, the approval is stale and must be revalidated.*

---

## Composition

A left-to-right workflow with a central waiting platform, three human-request cards, four response paths, and a stale-approval loop.

**Left:** **WORKFLOW** — a blue platform with a play button.

**Cyan arrow** → **WAITING HUMAN** — a blue platform with a large central box.

**Inside the waiting human box, three white cards:**
- **APPROVAL REQUEST** — person icon, with six rows: **EXACT ACTION, EVIDENCE, RISK, AMOUNT, EXPIRY, APPROVER**.
- **MISSING INPUT** — question mark, with a puzzle-piece icon.
- **OPERATOR INTERRUPT** — alarm icon, with a red beacon.

**Right of the waiting box:** four teal arrows fan to:
- **APPROVE** — green check.
- **DENY** — red X.
- **EDIT** — pencil.
- **SUPPLY INPUT** — keyboard.

**Below:** a **teal durable chain** from left to right:
- **EVENT** — circle.
- **ACKNOWLEDGEMENT** — envelope.
- **RECEIPT** — document.
- **CHECKPOINT** — flag.
- **RESUME** — play button.

**From RESUME, a red dashed arrow** loops down and right to **STALE APPROVAL** — red box with a clock — then to **REVALIDATE** — red box with circular arrows.

## Element by element

**WORKFLOW** — the running process.
**WAITING HUMAN** — the durable pause state.

**APPROVAL REQUEST** — permission to act.
**MISSING INPUT** — request for a fact.
**OPERATOR INTERRUPT** — request to stop or steer.

**EXACT ACTION / EVIDENCE / RISK / AMOUNT / EXPIRY / APPROVER** — the approval contract fields.

**APPROVE / DENY / EDIT / SUPPLY INPUT** — the four human responses.

**EVENT / ACKNOWLEDGEMENT / RECEIPT / CHECKPOINT / RESUME** — the durable chain.

**STALE APPROVAL / REVALIDATE** — the safety loop for changed state.

## Colour and flow semantics

- **Cyan arrows** carry the workflow into the wait and the human responses back out.
- **Teal arrows** carry the durable event, acknowledgement, receipt, checkpoint, resume.
- **Red dashed** marks the stale-approval path — a changed state that must be re-approved.
- The **three request cards** inside one box show that the wait is one pattern with three triggers.
- The **four response cards** show that the human can approve, deny, edit, or supply input.

## How to present it

**Ask how their system asks a human for approval.** Does it show the exact action, evidence, risk, amount, expiry, and approver? If any are missing, the human is not informed.

**Point at the three wait cards and ask which one the room uses most.** Most use approval. Fewer use missing input as a durable wait. Fewer still have operator interrupts.

**Trace the approval contract.** Exact action, evidence, risk, amount, expiry, approver. Write these down for one real approval. Is the action exact? Is the amount specific? Does it expire?

**Show the four responses.** Approve, deny, edit, supply input. Each is a typed event. What does their system record when a human clicks?

**Tell the Wrenfield story.** A £40 approval became a £60 execution because the request was not specific and the workflow did not revalidate. The fix: exact action, specific amount, evidence, risk, expiry, approver, and stale-approval revalidation.

**Point at the stale-approval loop.** An old approval is not invalid. It is historical. But if the state changed, it must be revalidated before execution.

**Emphasize that human-in-the-loop is not a pause button.** It is a durable contract. The request must be specific. The response must be recorded. The state must be revalidated.

**Ask how they verify who approved.** The request must bind to a named approver role, and the server must re-check that the person who clicked can approve this amount. A shared admin account or generic approval link breaks the contract.

**Map to the Next.js implementation path.** Show an accessible approval card with evidence links, exact action, amount, expiry, and clear approve/deny/edit/supply-input alternatives. Use server actions that verify the approver's authority and an expected version, then return an immutable decision receipt.

**Map to the Python implementation path.** Persist `ApprovalRequest` and `HumanResponse` as separate typed records. Use a signal or message handler that validates the responder's identity and the current version, then re-runs policy and material-change checks before the side effect.

**Run the approval-payload lab.** Ask the room to design one approval card for a real action in their system. Include actor, role, action hash, amount, evidence versions, policy version, expiry, alternatives, and a material-change rule. Draw the missing fields. If the card is missing a field, the human is not really informed.

**Test the stale-approval trap.** Present a $40 approval and then reveal the evidence changed to $60. Does the workflow execute, stop, or re-request? The old click must not be trusted after a material change.

**Ask the checkpoint question.** "Can an old approval remain historically valid but unusable now?" Answer: yes. The old approval stays in history as proof of what the person saw, but a material change means it must be revalidated before it can be used.

**Point to the related patterns and sources.** The durable wait in Diagram 136, the budget and planning gate in the previous lesson, and the steering/replanning flow in Diagram 144 all touch this boundary. The pattern also appears in Temporal's message passing, the A2A protocol, and the Azure compensating transaction pattern: each treats the decision as a durable, versioned event revalidated before use.

**Close on the standard.** *An approval is a contract with an exact action, evidence, risk, amount, expiry, and approver. If any of those change, the approval is stale and must be revalidated.*

**Timing.** Twenty minutes. Thirty if the room designs an approval card for one real action and checks whether it would survive a state change.

---

## Lab and checkpoint

**Lab:** Design an approval card for one real action in your system. Include actor, role, exact action, evidence, risk, amount, expiry, and approver. Write the human response types (approve, deny, edit, supply input) as typed events. Then define the material-change rule that revalidates the approval if the state changes.

**Checkpoint:** Why must an approval be revalidated if the state changes?

**Answer:** Because the approval was given for a specific state. If the action, amount, evidence, or risk changes, the original approval no longer covers the current situation. The old approval stays in history as proof of what was reviewed, but it must be revalidated before it can be used.

## Glossary

- **Approval** — a durable contract for a specific human decision.
- **Approval request** — the structured contract shown to the approver.
- **Approver** — the named person or role with authority.
- **Deny** — the response that refuses the action.
- **Edit** — the response that changes the proposal and returns it.
- **Evidence** — the material the approver reviews.
- **Expiry** — the time after which the approval is no longer valid.
- **Human-in-the-loop** — the pattern of pausing workflow for a human decision.
- **Human interrupt** — a durable wait for a typed human response.
- **Material change** — a change that makes the original approval stale.
- **Missing input** — a durable wait for a human to supply information.
- **Operator interrupt** — a control action, not a chat message.
- **Revalidate** — checking an old approval against the current state.
- **Supply input** — the response that provides missing information.

## Sources

- Human-in-the-loop and approval design
- Durable waits and typed human responses
- Revalidation and material-change detection
