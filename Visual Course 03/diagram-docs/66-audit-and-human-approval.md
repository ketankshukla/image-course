# Diagram 66 — Audit and Human Approval

![A six-stage flow on dark navy. PROPOSED ACTION shows a card listing AMOUNT, TARGET, EVIDENCE and RISK. EVIDENCE shows a teal folder with an image and document. POLICY CHECK shows a checklist with three green ticks, one red cross and a teal shield. APPROVAL REQUIRED shows a teal person disc with a coral alert. HUMAN DECISION shows a person at a screen listing the same four fields. AUDIT RECEIPT shows a receipt listing WHO, WHAT, WHEN, POLICY and RESULT. Below, branches lead to APPROVE in teal, REJECT in coral, EXECUTE with a gear and play button, and a second AUDIT RECEIPT. A dashed cyan line returns along the base to the first three stages.](../diagrams/66-audit-and-human-approval.png)

**Module:** Security
**Role in the course:** the approval pipeline and the record it leaves
**Layout:** six stages with a three-way decision branch and a receipt on every path

---

## At a glance

An action is proposed, evidence is gathered, policy is checked, approval is required, a human decides, and a receipt is written. The decision branches three ways — **APPROVE**, **REJECT**, **EXECUTE** — and **every path produces an AUDIT RECEIPT**.

The receipt's contents are spelled out: **WHO, WHAT, WHEN, POLICY, RESULT**. Five fields, and they are the difference between a system you can explain and one you cannot.

---

## What the diagram teaches

### 1. The proposed action names four fields, and they are what a human needs

The first card lists **AMOUNT, TARGET, EVIDENCE, RISK**.

Those four appear again on the human's screen at stage 5, unchanged. That repetition is deliberate: **what is proposed is what is reviewed**. No summarisation, no reformatting, no additional interpretation between proposal and decision.

Each field answers a question a reviewer must be able to answer:

**AMOUNT** — how much is at stake? The magnitude that determines whether this needs approval at all.
**TARGET** — what or whom does it affect?
**EVIDENCE** — on what basis? Not the conclusion, the material.
**RISK** — what could go wrong, and how badly?

A proposal missing any of these produces a reviewer who has to go and find it, which in practice means a reviewer who approves without it.

### 2. Policy check runs before approval, and it can already say no

Stage 3 shows a checklist with **three green ticks and one red cross**, beside a teal shield.

Policy is evaluated *before* the human sees it. That ordering matters for two reasons.

**It filters.** Actions that policy refuses outright do not consume human attention. A reviewer's time is the scarcest resource in this pipeline.

**It informs.** The human sees which policy rules passed and which did not. The red cross is not necessarily a blocker — some policy failures are for a human to override with justification — but the reviewer knows it is there.

A policy check that runs *after* approval is a policy check that asks a human to approve something and then overrules them, which is both wasteful and corrosive to the reviewer's sense that their decision matters.

### 3. Approval required is its own stage, and it is a routing decision

Stage 4 — a teal person disc with a coral alert badge — sits between the policy check and the human.

It is the decision about **whether a human is needed at all**, and it is separate from the decision the human then makes.

That separation lets the threshold be explicit and tunable. Below a certain amount, with a clean policy check and low risk, an action may proceed without approval. Above it, or with any policy failure, or with elevated risk, it routes to a person.

Systems that lack this stage do one of two bad things: require approval for everything, which exhausts reviewers and produces rubber-stamping; or require it for nothing, which is the failure the whole pipeline exists to prevent.

### 4. Three outcomes, and execute is separate from approve

The branch produces **APPROVE**, **REJECT**, and **EXECUTE**.

Approve and execute being separate is the subtle part. Approval is a **decision**; execution is an **action**. They are drawn as different objects because they can fail independently.

An approved action that then fails to execute is a real state. So is an approved action that is executed later, or in a batch, or after a further condition is met. Collapsing them means you cannot distinguish "the human said yes and it worked" from "the human said yes."

The **REJECT** path is coral and terminates — and, critically, still produces a receipt.

### 5. Both terminal paths produce a receipt, and that is the diagram's core claim

Follow the arrows out of **REJECT** and out of **EXECUTE**. Both reach **AUDIT RECEIPT**.

A rejection is as auditable as an approval. That is not a nicety:

- It records that a human considered and declined, which is evidence of control operating.
- It creates a pattern that can be analysed. A rise in rejections of a particular action type means the proposal logic is drifting.
- It protects the reviewer. "I declined this" is a defensible position only if there is a record of it.

Systems that log only successful actions cannot demonstrate their controls work, because a control that has never visibly refused anything is indistinguishable from a control that does nothing.

### 6. The five receipt fields answer five different questions

**WHO** — which human decided. Named, not "a supervisor."
**WHAT** — the action, with its parameters.
**WHEN** — timestamp.
**POLICY** — which rules were evaluated and what they returned. Not just "policy passed" — the specific rules.
**RESULT** — what actually happened.

The **POLICY** field is the one most often reduced to a boolean, and it is the one that matters most in a review months later. Knowing that policy passed tells you nothing about *which version of which rules* passed, and rules change.

### 7. The dashed return feeds evidence back into the front of the pipeline

A **dashed cyan line** runs from the base of the diagram back into the first three stages — proposed action, evidence, and policy check.

Two readings, both useful.

**Rejections inform proposals.** A pattern of rejections should change what gets proposed.

**Receipts become evidence.** Prior decisions on similar actions are relevant context for the next one. A reviewer benefits from knowing that three similar proposals were declined last month.

What the reviewer actually interacts with is the approval card, which adds two things this diagram does not show — an expiry and an edit option:

![A flow from PLAN through CHECK POLICY to PAUSE, showing an APPROVAL CARD with proposed action, evidence, a graded risk bar, EXPIRES IN 10 MINUTES and APPROVE, REJECT and EDIT buttons, with steering controls alongside and a REVALIDATE branch to RESUME or INVALIDATE AND REPLAN.](../diagrams/75-interrupts-approval-and-steering.png)

The **EDIT** button is the significant addition. Without it, a reviewer who agrees with the intent and disagrees with a detail must either approve something not quite right or force a full replan.

---

## Case study — Redhaven Care Group, the approval nobody could explain

Redhaven operates 34 residential care homes. Their operations assistant handles supplier ordering, agency staffing bookings, and maintenance requests across the estate.

Agency staffing is the expensive one. A single shift booked through an agency costs between £180 and £420, and homes book them when their own staff are short. Roughly 900 shifts a month across the estate.

### The regulatory question they could not answer

During a routine inspection, a regulator asked Redhaven to demonstrate that agency bookings above their internal threshold had received appropriate authorisation.

Redhaven could show that the bookings had happened. They could not show who had authorised them, on what basis, or against what policy.

Their assistant recorded successful bookings. It did not record the approval that preceded them, because approval had been a UI interaction that produced no artefact. A manager clicked approve, the booking went through, and the booking record was the only thing written.

For a regulated care provider, being unable to evidence authorisation of expenditure is a finding.

### What the rebuild produced

**A proposed action with four named fields.**

> **Amount:** £340 (night shift, RGN, 12 hours, agency premium)
> **Target:** Oakfield House, Saturday 14th, night cover
> **Evidence:** rota shortfall confirmed, two internal staff declined overtime, resident dependency level requires RGN on site
> **Risk:** medium — regulatory minimum staffing breach if uncovered; cost 2.1× internal equivalent

That is what the manager sees, unchanged from what the assistant proposed.

**Policy checked before the human, with visible results.**

Four rules: within the home's monthly agency budget (passed), agency on approved supplier list (passed), rate within negotiated ceiling (passed), booking made more than 24 hours ahead (**failed** — this was a same-day booking).

The failed rule did not block. It routed the booking to a higher approval level and appeared on the manager's screen.

**An explicit approval threshold.** Bookings under £200, with all policy rules passing and low risk, proceed without approval. Everything else routes to a home manager. Anything above £400 or with two or more policy failures routes to a regional manager.

About 60% of bookings now proceed without human approval, which was the change that made the system usable — before the rebuild, an all-or-nothing design had managers approving 900 bookings a month, which is exactly the volume that produces rubber-stamping.

**Approve and execute separated.** A manager's approval creates an authorisation record. Execution — the actual agency booking — happens after, and can fail.

This mattered within the first month: an approved booking failed because the agency's system rejected it. Under the old design that would have been an unexplained gap. Now it is an approved-but-unexecuted state, visible, with a defined follow-up.

**Receipts on both paths.** Rejections are recorded with the same five fields and the reason.

### What the rejection records revealed

In the first six months, managers declined 218 bookings.

Analysis of those rejections found a pattern nobody had expected: **41 of them were at one home**, all for the same shift type, all declined because the manager knew a staff member was available who had not appeared in the rota system.

The rota system had a data problem — a member of staff whose contracted hours had been entered incorrectly, making them look unavailable. It had been costing that home unnecessary agency bookings for months, and the only reason it surfaced was that someone was reading the rejections.

Under the old system, those 41 rejections left no trace at all.

### The regulator's second visit

Redhaven demonstrated the receipt trail. The inspector asked for a specific booking from four months earlier and received: the proposal with all four fields, the four policy rules and their results including the failed one, the named manager who approved it, the timestamp, and the execution result.

The finding was closed.

### Results

- **Bookings with evidenced authorisation:** 100%, from effectively 0%.
- **Bookings proceeding without human approval:** 60%, freeing manager time.
- **Rejections recorded:** 218 in six months, previously invisible.
- **Process problems found through rejection analysis:** 3, including the rota data error.

### The framing their operations director uses

*We thought audit was for the regulator. It turned out the rejections were the most useful management information we had.*

---

## Composition

Six stages left to right across the upper portion, with a branch descending from the human decision.

**PROPOSED ACTION → EVIDENCE → POLICY CHECK → APPROVAL REQUIRED → HUMAN DECISION → AUDIT RECEIPT**, connected by cyan arrows.

From **HUMAN DECISION**, cyan arrows descend to **APPROVE** and **EXECUTE**, and a **coral arrow** to **REJECT**. From **EXECUTE**, a cyan arrow leads to a second **AUDIT RECEIPT**; a **coral line** runs from **REJECT** into the same return path.

A **dashed cyan line** runs along the base leftward and rises into the first three stages.

## Element by element

**PROPOSED ACTION**
A white card with a teal pencil badge, listing four rows: **AMOUNT**, **TARGET**, **EVIDENCE**, **RISK**.

**EVIDENCE**
A white card holding a **teal folder**, a small image tile and a document tile.

**POLICY CHECK**
A white card with **three green ticks and one red cross**, behind a **teal shield with a white check**.

**APPROVAL REQUIRED**
A large **teal disc with a white person glyph**, with a **coral circular alert badge** at its lower right.

**HUMAN DECISION**
A person seated at a screen displaying the same four labels — **AMOUNT**, **TARGET**, **EVIDENCE**, **RISK** — reaching toward it.

**AUDIT RECEIPT**
A white receipt with a torn lower edge and a teal header tab, listing **WHO**, **WHAT**, **WHEN**, **POLICY**, **RESULT**, with a **teal shield** badge.

**The three outcomes**
**APPROVE** — a teal disc with a white check. **REJECT** — a red disc with a white ✗. **EXECUTE** — a teal gear with a play button.

## Colour and flow semantics

- **Cyan arrows** carry the pipeline and the approve/execute paths.
- **Coral** marks the rejection outcome and the alert badge on the approval-required stage.
- **Teal** marks the policy shield, the approval person, the execute gear, and both receipt badges.
- **Both terminal branches converge on a receipt**, which is the diagram's central claim.
- The **dashed cyan return** feeds outcomes back into proposal, evidence and policy.

## How to present it

**Read the four proposal fields and ask what a reviewer needs.** Amount, target, evidence, risk. Then point out they appear unchanged on the human's screen — what is proposed is what is reviewed, with nothing added or summarised in between.

**Ask what happens when a reviewer is missing one of the four.** They go and find it, or they approve without it. In practice, at volume, it is the second.

**Ask why policy runs before the human.** It filters, so scarce reviewer attention is not spent on things policy already refuses; and it informs, so the reviewer sees which rules passed. Then ask what a policy check *after* approval means — asking a human to decide and then overruling them.

**Point at the approval-required stage as a routing decision.** Separate from the decision the human makes. Then give the two failure modes without it: approve everything (rubber-stamping) or approve nothing (the failure the pipeline exists to prevent). Redhaven's 60% no-approval rate is what made theirs usable.

**Ask why approve and execute are separate.** They fail independently. An approved action that fails to execute is a real state, and Redhaven hit it in month one.

**Trace both terminal paths to the receipt.** Then ask what their system records when a human declines something. Usually nothing. Make the argument: a control that has never visibly refused anything is indistinguishable from a control that does nothing.

**Read the five receipt fields and dwell on POLICY.** Most implementations reduce it to a boolean. Ask what "policy passed" tells you in a review eighteen months later, when the rules have changed twice.

**Tell the rejection-analysis finding.** 41 rejections at one home, all traced to a rota data error that had been generating unnecessary agency cost for months. Invisible before, because rejections left no trace.

**Close with the reframing.** *We thought audit was for the regulator; the rejections were the most useful management information we had.* Audit built only for compliance is audit built too narrowly.

**Timing.** Twenty-five minutes. Thirty-five if you draft the five receipt fields for one of the room's own approved actions.

---

## Lab and checkpoint

**Lab:** Take one consequential action in your system and design the human-approval pipeline. Define the four proposal fields (amount, target, evidence, risk), the policy check, the approval-required routing, the human screen, and the five receipt fields (who, what, when, policy, result). Then write what happens to a rejection — whether it is recorded and how it can be analysed.

**Checkpoint:** Why are approve and execute separate?

**Answer:** Because they fail independently. An action can be approved but fail to execute, or execute without approval. Separating them makes each state visible and gives the system a place to record each outcome.

## Glossary

- **Approve** — the human decision that the proposed action may proceed.
- **Audit receipt** — the durable record of the proposal, approval, and outcome.
- **Evidence** — the material supporting the proposed action.
- **Human decision** — the stage where a person reviews the four proposal fields.
- **Policy check** — the automated filter that runs before the human sees the proposal.
- **Proposed action** — the action the agent wants to take, with its amount, target, evidence, and risk.
- **Reject** — the human decision that refuses the action, which must be recorded.
- **Risk** — the assessed danger or cost of the proposed action.
- **Target** — what or who the action applies to.

## Sources

- Human-in-the-loop approval and audit design
- Rejection analysis and operational audit
- Policy-as-code and attributable decision records
