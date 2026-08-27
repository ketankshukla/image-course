# Diagram 139 — Ownership, Handoff, Artifacts, and Status Propagation

![On dark navy, a PARENT WORKFLOW on a blue platform holds a CASE folder and a person icon, with a green shield at top left reading CASE OWNERSHIP STAYS WITH PARENT. A blue arrow labelled DELEGATES A SCOPED TASK TO leads to a FINANCE AGENT robot on a blue platform, carrying an INPUT ARTIFACT and an ACCEPTANCE CONTRACT. Below, a HANDOFF LEDGER table shows columns FROM, TO, SCOPE, DEADLINE, with values PARENT WORKFLOW, FINANCE AGENT, SCOPED TASK, DATE / TIME. Teal ACKNOWLEDGEMENT and RECEIPT arrows loop back to the parent and agent. On the right, a STATUS SEQUENCE lists SUBMITTED, WORKING, INPUT REQUIRED, COMPLETED. Below, a teal dashed path leads through CHECKPOINT and RESUME to an OUTPUT ARTIFACT at the bottom. A coral dashed path on the left leads from the parent to a red FAILURE box.](../diagrams/139-ownership-handoff-artifact-status.png)

**Module:** Multi-agent collaboration, delegation, and A2A
**Role in the course:** how to delegate a task without losing ownership of the customer outcome
**Layout:** parent workflow on the left, agent on the right, handoff ledger in the centre, status sequence above, durable paths below

---

## At a glance

**PARENT WORKFLOW** owns the **CASE**.

It **DELEGATES A SCOPED TASK TO** a **FINANCE AGENT**, with an **INPUT ARTIFACT** and an **ACCEPTANCE CONTRACT**.

A **HANDOFF LEDGER** records: **FROM, TO, SCOPE, DEADLINE**.

The status sequence runs: **SUBMITTED → WORKING → INPUT REQUIRED → COMPLETED**.

The parent workflow never loses case ownership. The agent is responsible for the scoped task. The handoff ledger is the contract between them.

---

## What the diagram teaches

### 1. Ownership and responsibility are not the same thing

The parent workflow owns the case. The finance agent is responsible for the scoped task. Those are different objects, and the diagram keeps them apart.

Ownership means accountability for the customer outcome. Responsibility means accountability for a bounded piece of work. One does not replace the other.

When a parent delegates, it does not give away the case. It gives the agent a task with inputs, an acceptance contract, and a deadline. The ledger records that the task was given, not that the case was transferred.

### 2. The case stays with the parent, and the shield is the point

The green shield at the top left reads **CASE OWNERSHIP STAYS WITH PARENT**. That is not decoration. It is the diagram's central claim.

If the parent lost ownership when it delegated, there would be no one accountable for the overall outcome. The agent could complete the task and the case could still be wrong. The customer only cares about the case.

The shield means the parent remains the single point of accountability. The agent is a specialist working under contract.

### 3. The handoff ledger is the delegation contract

The **HANDOFF LEDGER** has four columns: **FROM, TO, SCOPE, DEADLINE**.

**FROM** — who delegated.
**TO** — who received.
**SCOPE** — what is included and what is not.
**DEADLINE** — when the task must be completed or escalate.

This is the durable record of the handoff. It is not an event log. It is a contract. If the agent fails to deliver by the deadline, the parent can read the ledger and decide what to do next.

The ledger also protects the agent. If the parent later asks for work outside the scope, the agent can point at the ledger and refuse or renegotiate.

### 4. Input artifact and acceptance contract are the task boundaries

The parent sends two things: an **INPUT ARTIFACT** and an **ACCEPTANCE CONTRACT**.

The input artifact is the data the agent needs. The acceptance contract is the criteria for success. Together they define the task boundaries.

The acceptance contract is what makes the completion decision objective. It is not the agent saying *I am done*. It is the parent checking the output against the contract.

### 5. Status is not the same as ownership

The **STATUS SEQUENCE** on the right is **SUBMITTED, WORKING, INPUT REQUIRED, COMPLETED**.

These statuses describe the task, not the case. The agent updates the task status. The parent maps that status into the case status.

The most common mistake is to let the agent set the case status directly. The agent should report task status. The parent decides how that affects the case.

### 6. Input required is a status, not a failure

**INPUT REQUIRED** is a normal status. It means the agent needs more information before it can continue.

This is not a failure. It is a negotiation. The agent tells the parent what it needs. The parent provides the input, updates the handoff ledger, and the task resumes.

The status is part of the durable workflow. It should be checkpointed. If the parent crashes, the workflow resumes from the `INPUT REQUIRED` state, not from the beginning.

### 7. Acknowledgement and receipt travel in both directions

The teal arrows show **ACKNOWLEDGEMENT** from the agent to the parent and **RECEIPT** from the parent to the agent. This is the durable handshake.

The parent must acknowledge that it received the agent's status update. The agent must acknowledge that it received the input and the acceptance contract.

These acknowledgements matter because messages can be lost. A parent that sends an input artifact but never gets an acknowledgement does not know whether the task started. An agent that completes a task but never gets an acknowledgement does not know whether the parent saw the result.

### 8. Failure is a possible parent state, not a hidden exception

The coral dashed path on the left leads to a **FAILURE** box with a red X. The parent can mark the delegation as failed.

Failure is not the agent's decision alone. The parent, as the owner, decides whether the task has failed against the acceptance contract. It might cancel the task because the deadline passed, or because the agent returned an artifact that did not meet the contract, or because the case itself is no longer valid.

This is why ownership stays with the parent. The parent is the one that can make the business decision to fail and move into recovery.

### 9. The handoff contract must be explicit and durable

Delegation is a contract, not just a message. Before the first artifact crosses the boundary, the handoff record must state what was requested, who owns the parent case, what the agent may and may not touch, and when the work is due. The lab form captures the contract as owner, assignee, scope, inputs, forbidden data, deadline, status map, artifact schema, acceptance test, and escalation.

The important beginner move is to keep that contract as an explicit business record, not as hidden framework behavior. The transport can retry and the worker can disappear, but the authoritative workflow record must remain inspectable. If someone later asks what the agent was told to do, the answer must come from the ledger.

### 10. Completion means the parent accepts the artifact

The specialist's task can reach `COMPLETED`, but the case is not finished until the parent validates and accepts the artifact. The trace's final step is the same: validate and accept the returned artifact before completing the parent milestone.

The Next.js view should show case owner and task owner as separate labels, display requested input, deadline, and accepted artifact version, and keep the workflow state read-only. Mutations go through authenticated server boundaries and return stable IDs. In Python, persist a `HandoffRecord` before dispatch, translate remote task states into local domain events, and run artifact validation before marking the parent milestone complete. The safety rule is unchanged: exactly one named owner remains accountable for the customer outcome.

The handoff in this diagram is implemented through the A2A Protocol 1.0 message, task, and artifact lifecycle:

![On dark navy, a CLIENT AGENT on a blue platform resolves an AGENT CARD, then sends a MESSAGE carrying CONTEXT ID and REQUEST ID through an A2A INTERFACE to a REMOTE AGENT. The remote agent returns a TASK ID and WORKING STATUS, then later sends STATUS UPDATE and ARTIFACT. A red coral dashed path at the bottom labelled VERSION FALLBACK is blocked by a red X and a forbidden sign.](../diagrams/138-a2a-delegation-task-creation.png)

The parent is the client agent. The finance agent is the remote agent. The input artifact is sent in the message; the acceptance contract is the A2A interface and the output contract. The task ID is the durable identity of the delegated work. When the remote agent sends the final artifact, the parent validates it against the acceptance contract before it accepts it. The blocked VERSION FALLBACK path is another expression of the same rule: the contract is pinned and cannot be silently changed.

---

## Case study — Eastway Insurance, the agent that owned the wrong record

Eastway uses a finance agent to calculate surrender values for life insurance policy cancellations. The parent workflow owns the customer case. It delegates the calculation to a finance specialist agent.

### What they had

The parent workflow created a task and sent the policy data to the agent. The agent calculated the value and wrote the result to a `surrender_value` field on the case record.

The agent had write access to the case. When the agent completed, it marked the case as `READY FOR CANCELLATION`.

### The incident

A policy had a special rider that the agent's calculation did not support. The agent produced a value, but the acceptance contract was ambiguous. It did not specify whether the rider should be included.

The agent wrote the value to the case and set the status. A downstream process saw `READY FOR CANCELLATION` and processed the cancellation. The customer received an incorrect payout.

When the error was discovered, the agent had already completed its task and moved on. There was no clear record of what the agent had been asked to do, what it had been told to include, or who had approved the status change.

### The handoff model

The parent workflow owns the case. It delegates the calculation as a scoped task.

- **Input artifact:** the policy data, the rider schedule, and the calculation rules.
- **Acceptance contract:** the output must include the base value, the rider value, and a breakdown, and it must be within a tolerance of the internal actuarial model.
- **Handoff ledger:** parent → finance agent, surrender calculation, two hours.
- **Agent status:** SUBMITTED, WORKING, INPUT REQUIRED, COMPLETED.

The agent returns an **OUTPUT ARTIFACT** with the calculation and breakdown. The parent validates it against the acceptance contract. Only then does the parent update the case status.

If the output is missing the rider breakdown, the parent moves the task to `INPUT REQUIRED` or `FAILURE`, not the case. The case status remains unchanged until the parent accepts the result.

### Results

- **Incorrect cancellations processed because the agent wrote case status directly:** 3 in two months → 0.
- **Disputed calculation because scope was not recorded:** 8 → 0.
- **Time to determine what the agent was asked to do:** hours of log search → seconds, from the handoff ledger.
- **Agent updates to case record:** full access → write only to the output artifact, read-only on the case.

### The line in their operations standard

*The agent owns the task. The parent owns the case. The handoff ledger is the contract. The case status changes only when the parent accepts the artifact.*

---

## Composition

A left-to-right delegation with a central ledger, status sequence, and durable paths.

**Left:** **PARENT WORKFLOW** — blue platform with a person icon and a **CASE** folder.

**Top left:** green shield with **CASE OWNERSHIP STAYS WITH PARENT**.

**Cyan arrow** from parent to agent, labelled **DELEGATES A SCOPED TASK TO**.

**Above the arrow:** two white cards — **INPUT ARTIFACT** (document icon) and **ACCEPTANCE CONTRACT** (clipboard icon).

**Right:** **FINANCE AGENT** — blue platform with a robot and a dollar sign.

**Status sequence (top right):** four stacked white cards:
- **SUBMITTED** — paper plane.
- **WORKING** — gear.
- **INPUT REQUIRED** — question mark.
- **COMPLETED** — green check.

**Centre bottom:** **HANDOFF LEDGER** — blue table with four columns:
- **FROM** — parent workflow icon.
- **TO** — finance agent icon.
- **SCOPE** — target icon.
- **DEADLINE** — calendar icon.

**Below the ledger:** **OUTPUT ARTIFACT** — white document card.

**Teal dashed loops:** **ACKNOWLEDGEMENT** from agent to parent, **RECEIPT** from parent to agent, and **CHECKPOINT / RESUME** paths.

**Coral dashed path:** from parent to **FAILURE** — red box with X.

## Element by element

**PARENT WORKFLOW** — the owner of the case.
**CASE** — the customer outcome.

**FINANCE AGENT** — the specialist responsible for the scoped task.

**INPUT ARTIFACT** — the data and rules the agent needs.
**ACCEPTANCE CONTRACT** — the success criteria.

**HANDOFF LEDGER** — the durable delegation record.

**STATUS SEQUENCE** — the lifecycle of the delegated task.
**OUTPUT ARTIFACT** — the agent's completed work.

**ACKNOWLEDGEMENT / RECEIPT** — the durable handshake.
**CHECKPOINT / RESUME** — the durable workflow paths.

**FAILURE** — the parent's decision to abandon the task.

## Colour and flow semantics

- **Cyan arrows** carry the delegation and the output artifact.
- **Teal dashed** carries acknowledgements, receipts, checkpoints, and resumes.
- **Coral dashed** carries the failure path — a decision to stop, initiated by the owner.
- **Green shield** marks the non-transferable case ownership.
- The **HANDOFF LEDGER table** is central because it is the shared contract.

## How to present it

**Start with the question of who owns the customer outcome.** In a multi-agent system, many tasks are delegated. Ask the room who owns the result. The answer must be the parent, not the agent.

**Point at the green shield.** CASE OWNERSHIP STAYS WITH PARENT. That is the whole point. The agent does not take over the case.

**Read the handoff ledger columns.** FROM, TO, SCOPE, DEADLINE. Ask the room what their handoff records contain. If the answer is "nothing written," the delegation is not auditable.

**Explain the two artifacts.** Input artifact and acceptance contract. The input is what the agent gets. The acceptance contract is how the parent will judge the output.

**Trace the status sequence.** SUBMITTED, WORKING, INPUT REQUIRED, COMPLETED. These are task statuses, not case statuses. The parent maps them into the case.

**Tell the Eastway story.** The agent wrote the case status directly and an incorrect surrender value was processed. The fix: parent owns the case, agent writes only the output artifact, parent validates against acceptance contract, then updates the case.

**Point at INPUT REQUIRED.** It is a normal state. The agent should not guess. It should ask for input, and the handoff ledger should record the new scope.

**Point at the failure path.** The parent can decide the task has failed. The agent cannot fail the case on its own.

**Ask the completion question.** "When is delegated work complete for the parent?" Answer only when the specialist reaches a terminal state and the parent validates and accepts the artifact under the handoff contract. The agent's `COMPLETED` is local; parent acceptance moves the case.

**Walk Maya's `INPUT REQUIRED` pause and use the lab form.** The finance specialist pauses Maya's review because the payment reference is missing. Have participants fill out the lab handoff form and name the danger: informal handoffs create orphan tasks.

**Close on the standard.** *The agent owns the task. The parent owns the case. The handoff ledger is the contract. The case status changes only when the parent accepts the artifact.*

**Timing.** Twenty-five minutes. Thirty if the room maps one real delegation and checks who can write the parent record.

---

## Lab and checkpoint

**Lab:** Map one real delegation in your system. Identify the parent case, the delegated task, the handoff ledger fields (from, to, scope, deadline), the input artifact, the acceptance contract, and the terminal status. Ensure the specialist cannot write the parent case and that completion requires parent acceptance of the artifact.

**Checkpoint:** Why does the parent own the case, not the agent?

**Answer:** Because the parent is responsible for the customer outcome. The specialist agent owns the task, but the parent must validate and accept the artifact before updating the case. Letting the agent write the parent record can cause incorrect outcomes, as Eastway found with the wrong surrender value.

## Glossary

- **Acceptance contract** — the criteria the parent uses to judge the output artifact.
- **Agent** — the specialist that performs the delegated task.
- **Artifact** — the durable output the agent returns.
- **Case** — the parent workflow that owns the customer outcome.
- **Completion** — the terminal state when the parent accepts the artifact.
- **Delegation** — assigning a task from a parent to an agent.
- **Handoff ledger** — the durable record of the delegation contract.
- **Input artifact** — the material the parent gives to the agent.
- **Input required** — a normal status where the agent needs more information.
- **Ownership** — responsibility for the parent case and customer outcome.
- **Parent** — the orchestrator that owns the case.
- **Status** — the task-level condition, which is not the same as case ownership.

## Sources

- A2A delegation and ownership boundaries
- Parent-agent handoff and acceptance
- Case ownership and task status
