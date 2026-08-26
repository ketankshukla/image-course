# Diagram 141 — Planner, Executor, Reviewer, and Policy Roles

![On dark navy, a USER GOAL figure sends a cyan arrow to a PLANNER brain on a blue platform. The planner sends a cyan arrow to a BOUNDED PLAN card and a dashed red loop back. The bounded plan becomes PROPOSED ACTIONS entering a POLICY GATE shield. The policy gate emits ALLOWED STEPS to an EXECUTOR gear with TOOLS, which produces OUTPUT. The output goes to a REVIEWER magnifier, which compares it to ACCEPTANCE TESTS and EVIDENCE. Two red failure boxes sit below: PLAN CANNOT EXECUTE with a warning triangle, and REVIEWER CANNOT APPROVE OWN HIGH-RISK ACTION with a person and warning. A teal ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME chain runs vertically through the centre and feeds back to the bounded plan and to the executor.](../diagrams/141-planner-executor-reviewer-policy.png)

**Module:** Human-in-the-loop, steering, and recovery
**Role in the course:** the control separation pattern — no single role should silently own the whole decision
**Layout:** user goal → planner → bounded plan → policy gate → executor → reviewer, with two separation-of-duty warnings

---

## At a glance

**USER GOAL → PLANNER → BOUNDED PLAN → POLICY GATE → EXECUTOR → REVIEWER**.

The planner proposes. The policy gate allows or denies. The executor acts. The reviewer checks.

And two red warning boxes:
- **PLAN CANNOT EXECUTE**
- **REVIEWER CANNOT APPROVE OWN HIGH-RISK ACTION**

Separation of duties: the same entity cannot plan, permit, act, and approve.

---

## What the diagram teaches

### 1. The user goal is not the plan

A user says *I want a refund*. That is a goal. The **PLANNER** turns it into a **BOUNDED PLAN**.

The plan is a sequence of steps with dependencies and stop conditions. It says *verify, gather, approve, execute, notify*. The user does not care about the steps, but the system does.

The plan must be bounded. It must know where to stop, what to do when evidence is missing, and which steps require approval. A plan without boundaries will try to continue until it invents its own authority.

### 2. The planner proposes, the policy gate permits

The planner sends **PROPOSED ACTIONS** to the **POLICY GATE**. The gate is not another agent. It is deterministic authority: identity, resource, risk, and budget rules.

The policy gate can allow some steps and deny others. It can require human approval for a step. It can limit how many tool calls a step may use. It can reject the whole plan.

The most important thing the policy gate does is not permit. It prevents. It stops a plan from including a step the planner has no authority to execute.

### 3. The bounded plan is the contract for this execution

The **BOUNDED PLAN** card is the plan that has passed the policy gate, or at least the parts of it that are allowed. It becomes the contract for the executor.

The executor does not re-plan. It follows the bounded plan. If it needs to diverge, the plan is replanned, re-gated, and re-issued.

That means the executor is not smart in the sense of deciding what to do. It is smart in the sense of doing what the plan says, recording receipts, and handling failure.

### 4. The executor acts only through tools, and tools leave receipts

The **EXECUTOR** is a gear. Below it, a **TOOLS** box. The executor performs allowed steps by calling tools or workers.

Every tool call must produce a **RECEIPT**. The receipt is the evidence that the step happened and what it produced. The executor cannot declare a step done based on its own internal state. It needs an external receipt.

This is the same durable vocabulary from the rest of the course. Tools produce events, acknowledgements, receipts, checkpoints, and resumes.

### 5. The reviewer checks output against acceptance tests and evidence

The **REVIEWER** is a magnifier. It takes the **OUTPUT** and compares it to **ACCEPTANCE TESTS** and **EVIDENCE**.

Acceptance tests are the contract for success. Evidence is the durable record that the steps happened. The reviewer checks both.

The reviewer is not a cheerleader. It asks hard questions. Does the output match the expected schema? Is the evidence sufficient? Did every step have a receipt? Are there any policy violations?

### 6. A plan cannot execute itself

The red box on the left says **PLAN CANNOT EXECUTE**. The planner sends a dashed red loop back to itself when the plan cannot be executed.

This is the separation of proposing and acting. The planner is not the executor. If the plan fails policy, the planner must replan, not execute anyway.

A system that lets the same model propose and then immediately execute is not a planner/executor split. It is one model with two hats. The hats must be real, not rhetorical.

### 7. A reviewer cannot approve its own high-risk action

The red box on the right says **REVIEWER CANNOT APPROVE OWN HIGH-RISK ACTION**. This is the separation of acting and checking.

If the reviewer is the same entity as the executor, and the action is high-risk, the review is meaningless. The entity cannot fairly judge its own work.

High-risk actions require an independent reviewer. That reviewer might be a different agent, a human, or a deterministic rule set. But it cannot be the executor in disguise.

### 8. Policy, execution, and review are durable workflow steps

The vertical teal chain in the centre — **ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME** — runs through the whole diagram.

Each role acknowledges the plan. Each tool call produces a receipt. The workflow is checkpointed between roles. If it crashes, it resumes from the last checkpoint.

This is not an abstract pattern. It is the practical implementation of separation of duties in a durable workflow.

The same policy idea also applies when several specialists advise a decision before the final authority acts:

![On dark navy, three agents — POLICY AGENT, FINANCE AGENT, RISK AGENT — each send RESULT CARDS with CLAIM, EVIDENCE, CONFIDENCE, and LIMITS to a central AGGREGATOR. The aggregator produces AGREEMENT and CONFLICT cards, then sends a cyan arrow to a POLICY ENGINE, which chooses AUTO ACCEPT, REQUEST MORE, or HUMAN ESCALATE. A red MAJORITY VOTE box at the top right has a red X and is labelled NOT AUTHORITY. A teal CHECKPOINT / RESUME chain runs below to a FINAL AUTHORITY shield.](../diagrams/140-aggregation-disagreement-final-authority.png)

In that diagram, the policy engine is the same kind of gate as the policy gate here. It takes structured claims and evidence, and it produces one of three durable outcomes. The planner may propose any sequence, but the policy gate is what allows it to proceed. In both diagrams the final authority is a named role, not the model that produced the plan or the advice.

### 9. The durable record is the source of truth

The vertical teal chain is not decoration. It is the durable record that outlives any single process. The record must say what was requested, which identity owns the request, what changed, which attempt produced the change, and what may legally happen next.

A transport can retry, a worker can disappear, and a planner can revise its proposal. But the authoritative workflow record must stay inspectable and consistent. That is why the plan, the policy decision, the execution receipt, and the review result are stored together.

The trace also shows why this matters. Every step — plan, policy, execute, review — produces a typed record. Replanning or escalation should use explicit review findings, not vague dissatisfaction. The reviewer cannot just say “I don’t like this”; it must point at a missing schema field, an absent receipt, or a policy violation. Those findings become the next plan’s input. The same durable record discipline appears in Temporal Workflow Execution and the A2A Protocol 1.0 specification.

### 10. Roles are responsibilities, not titles

The checkpoint asks: *Must each role be a separate model?* The answer is no. A planner can be a deterministic route finder, a human, or a language model asked to propose steps. A policy gate can be a rule engine. An executor can be a worker. A reviewer can be a test suite. The responsibility split matters more than the labels.

In a Next.js interface, show plan, approvals, execution receipts, and review findings as separate timeline items. Keep policy evaluation on trusted server boundaries. In Python, define typed `PlanStep`, `PolicyDecision`, `ExecutionResult`, and `ReviewResult` records. Run deterministic policy before tool adapters and after any material replan. Type commands, events, states, and errors so tests can replay the same fixture without network calls.

Hartwell’s first design used one model with different prompt prefixes. The rebuilt system used separate services and a deterministic rule engine. The high-risk refunds were stopped because the roles were separated by code and record, not because the model was smarter.

---

## Case study — Hartwell Finance, the refund that planned itself

Hartwell runs a customer-service bot that can handle refund requests. The bot had a planner, an executor, and a reviewer, but they were all the same model with different prompt prefixes.

### What they had

The model received the user's goal: *refund order 12345*. It planned the steps, executed them, and returned a result. The "reviewer" was the same model asked to review its own output.

The policy gate was a list of rules in the prompt. The planner could propose any sequence, and the executor would run it as long as the prompt said it was allowed.

### The incident

A customer asked for a refund. The planner produced a plan: verify identity, check order, call refund provider, send confirmation email.

The policy gate was supposed to require human approval for the refund call. But the planner included the refund call as step three, and the "reviewer" confirmed that the plan was valid. The executor ran the call.

The refund went through. The customer was eligible, so no immediate harm. But the case was supposed to be reviewed by a supervisor because the amount was above the threshold. The supervisor was never notified.

A month later, an audit found that 47 refunds above threshold had been processed without supervisor approval. The bot had planned, executed, and reviewed its own high-risk actions.

### The redesign

The planner is now a separate service. It produces a bounded plan. The policy gate is a deterministic rule engine that runs before execution. It marks any money movement as approval-required.

The executor is a worker that only runs allowed steps. When it reaches an approval-required step, it pauses and requests human input.

The reviewer is a different service from the executor. It checks the output against acceptance tests: case state, receipt from provider, customer notification, and supervisor approval for high-risk refunds.

The review cannot be done by the executor. The policy gate logs every proposed action, every decision, and every execution.

### Results

- **Refunds above threshold without supervisor approval:** 47 in one month → 0.
- **Plans that included disallowed steps and executed anyway:** any number → 0, because the policy gate rejects them before execution.
- **Self-reviewed high-risk actions:** 100% → 0.
- **Mean time to audit a refund decision:** several hours of log reconstruction → minutes, because the plan, policy decisions, receipts, and review are stored together.

### The line in their operations standard

*The planner proposes, the policy gate permits, the executor acts, the reviewer checks. One service may not be all four.*

---

## Composition

A left-to-right control flow with two red separation-of-duty warnings.

**Far left:** **USER GOAL** — a person icon on a blue platform.

**Cyan arrow** → **PLANNER** — a blue platform with a brain icon.

**From planner, two paths:**
- **Cyan arrow down** → **BOUNDED PLAN** — a white card with three checked boxes.
- **Coral dashed arrow** → **PLAN CANNOT EXECUTE** — red box with a warning triangle, looping back to the planner.

**Cyan arrow** from BOUNDED PLAN, labelled **PROPOSED ACTIONS**, → **POLICY GATE** — a blue platform with a shield and check.

**Cyan arrow** from policy gate, labelled **ALLOWED STEPS**, → **EXECUTOR** — a blue platform with a gear.

**Below executor:** **TOOLS** — blue platform with a toolbox.

**Cyan arrow** → **OUTPUT** — white card with a bar chart.

**Cyan arrow** → **REVIEWER** — blue platform with a magnifier.

**From reviewer:** two teal arrows to **ACCEPTANCE TESTS** (clipboard with checks) and **EVIDENCE** (document).

**Coral dashed arrow** from reviewer → **REVIEWER CANNOT APPROVE OWN HIGH-RISK ACTION** — red box with a warning triangle and person icon.

**Vertical teal chain in the centre:** four stacked badges — **ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME** — with teal arrows feeding the planner, policy gate, executor, and output.

## Element by element

**USER GOAL** — the desired outcome.
**PLANNER** — the role that proposes a bounded plan.
**BOUNDED PLAN** — the proposed steps with dependencies and stop conditions.

**POLICY GATE** — the deterministic authority that allows, denies, limits, or escalates.
**PROPOSED ACTIONS / ALLOWED STEPS** — the plan before and after policy.

**EXECUTOR** — the role that performs permitted steps.
**TOOLS** — the external capabilities the executor uses.

**OUTPUT** — the result of execution.
**REVIEWER** — the role that checks output against acceptance and evidence.
**ACCEPTANCE TESTS / EVIDENCE** — the criteria and proof.

**PLAN CANNOT EXECUTE** — a rejected plan loops back to replanning.
**REVIEWER CANNOT APPROVE OWN HIGH-RISK ACTION** — separation of acting and checking.

## Colour and flow semantics

- **Cyan arrows** carry forward work: goal → plan → proposed actions → allowed steps → output.
- **Teal arrows** carry durable state: acknowledgement, receipt, checkpoint, resume.
- **Coral dashed** marks the two separation-of-duty failure paths.
- The **vertical teal chain** runs through the centre, showing that every role is part of the durable workflow.
- The **red warning boxes** are visually heavy because they are the most important safety claims.

## How to present it

**Ask how many services handle plan, execute, and review in their system.** If the answer is one, there is no separation.

**Point at the planner and ask whether it can execute.** It cannot. The plan is a proposal. Only the policy gate and executor can act.

**Trace the policy gate.** It is not a suggestion. It is deterministic authority. Ask what rules it enforces: identity, resource, risk, budget, approval.

**Show the executor and tools.** The executor acts only through tools, and every tool leaves a receipt. A step without a receipt did not happen.

**Trace the reviewer.** It compares output to acceptance tests and evidence. It is not the executor checking itself.

**Point at the two red boxes and ask whether they are real.** PLAN CANNOT EXECUTE means the planner cannot bypass policy. REVIEWER CANNOT APPROVE OWN HIGH-RISK ACTION means the executor cannot review itself.

**Tell the Hartwell story.** One model with three prompt prefixes planned, executed, and reviewed its own refunds. 47 high-value refunds missed supervisor approval. The fix: separate services, deterministic policy gate, independent reviewer.

**Emphasize that roles are responsibilities, not labels.** The planner could be code or a human. The policy gate could be a rule engine. The executor could be a worker. The reviewer could be a test suite. The split matters more than the implementation.

**Close on the standard.** *The planner proposes, the policy gate permits, the executor acts, the reviewer checks. One service may not be all four.*

**Run the lab prompt.** Ask participants to take one five-step plan and label the planner output, policy decision, executor input, receipt, and reviewer acceptance for each step. A missing label usually reveals a missing boundary.

**Ask where the durable record lives.** The plan, policy decisions, receipts, and review must be stored together. If the evidence is scattered across model context or console logs, the split cannot be proved.

**Timing.** Twenty-five minutes. Thirty if the room maps one real workflow and labels which component currently plays each role, which usually reveals overlap.

---

## Lab and checkpoint

**Lab:** Take one real workflow and label the four roles: planner, policy gate, executor, and reviewer. For each step, write the planner proposal, the policy decision, the tool receipt, and the reviewer acceptance test. Ensure the planner cannot execute and the executor/reviewer cannot approve its own high-risk action.

**Checkpoint:** Why can a plan not execute itself?

**Answer:** Because the plan is a proposal, not an action. Separation of planning and execution ensures that a proposed plan must pass the policy gate and be carried out by tools that leave receipts. If the same component plans and executes, there is no independent control and high-risk actions can bypass approval.

## Glossary

- **Acceptance test** — the test the reviewer uses to judge output.
- **Durable record** — the stored plan, policy decisions, receipts, and review.
- **Execution** — the phase where tools perform the plan's steps.
- **Executor** — the role that acts through tools and leaves receipts.
- **Plan** — the proposed sequence of steps to achieve a goal.
- **Planner** — the role that proposes the plan.
- **Policy gate** — the deterministic authority that permits or denies parts of the plan.
- **Receipt** — the durable record that a tool was invoked.
- **Review** — the comparison of output against acceptance tests and evidence.
- **Reviewer** — the role that checks output but cannot approve its own high-risk action.
- **Role** — a responsibility in the workflow, not a job title.

## Sources

- Separation of planning, execution, and review
- Policy gates and deterministic authorisation
- Durable records and role separation
