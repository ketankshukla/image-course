# Diagram 140 — Aggregation, Disagreement, Escalation, and Final Authority

![On dark navy, three agents — POLICY AGENT, FINANCE AGENT, RISK AGENT — each on a blue platform, send FORWARD WORK arrows to their own RESULT CARDS with CLAIM, EVIDENCE, CONFIDENCE, and LIMITS. Each result card emits a teal EVENT arrow to a central AGGREGATOR, and receives teal ACKNOWLEDGEMENT and RECEIPT arrows. Below the aggregator, two white cards show AGREEMENT with a green check and CONFLICT with a red X. The aggregator sends a cyan arrow to a POLICY ENGINE gear, which fans to three outcomes: AUTO ACCEPT, REQUEST MORE, and HUMAN ESCALATE. A red MAJORITY VOTE box at the top right has a red X and is labelled NOT AUTHORITY. A teal CHECKPOINT / RESUME chain runs below, connecting all outcomes to a FINAL AUTHORITY shield on the right.](../diagrams/140-aggregation-disagreement-final-authority.png)

**Module:** Multi-agent collaboration, delegation, and A2A
**Role in the course:** how to combine specialist outputs without averaging away disagreement or letting model confidence replace authority
**Layout:** three agents on the left feeding result cards into an aggregator and policy engine, with a final-authority shield on the right

---

## At a glance

Three agents — **POLICY, FINANCE, RISK** — each produce a **RESULT CARD**: **CLAIM, EVIDENCE, CONFIDENCE, LIMITS**.

The result cards become **EVENT** arrows into an **AGGREGATOR**.

The aggregator sorts them into **AGREEMENT** and **CONFLICT**.

Then the **POLICY ENGINE** decides: **AUTO ACCEPT, REQUEST MORE, HUMAN ESCALATE**.

And a **MAJORITY VOTE** box is crossed out: **NOT AUTHORITY**.

Final authority is a named role, not a popularity contest.

---

## What the diagram teaches

### 1. Each result card has four fields, and they are not the same

**CLAIM** — what the specialist asserts.
**EVIDENCE** — the data or reasoning behind it.
**CONFIDENCE** — how certain the specialist is.
**LIMITS** — what the specialist does not know, what data it did not see, what assumptions it made.

The most common mistake is to reduce a result card to a single number or a single label. *Approve, 0.92 confidence* tells you almost nothing useful. The claim, evidence, confidence, and limits together make the result inspectable.

### 2. Aggregation is not synthesis

The **AGGREGATOR** receives the result cards as events. It does not average them. It does not vote on them. It identifies agreement and conflict.

Agreement means the claims support each other, or they address different aspects of the same question. Conflict means the claims cannot all be true, or they reach incompatible conclusions from the same evidence.

The aggregator's job is to preserve the distinction. It is not a model that writes a smooth summary. It is a structured comparison.

### 3. Agreement and conflict must both be visible

Below the aggregator, two cards: **AGREEMENT** with a green check, **CONFLICT** with a red X.

Both are outputs. A workflow that only reports agreement is hiding information. A workflow that only reports conflict is not making progress.

The diagram draws them side by side because both are material. Agreement gives confidence. Conflict tells you where the uncertainty is.

### 4. Majority vote is not authority

At the top right, a red **MAJORITY VOTE** box with a red X and the label **NOT AUTHORITY**.

This is the diagram's strongest claim. Three agents can agree, and they still do not have the authority to make a binding decision. The decision belongs to a named role or system.

Majority vote is only safe when the voting agents are peers with comparable authority and calibrated independent errors. That is a rare and explicit condition, not a default.

In most business workflows, the agents have different authority. A finance agent's claim about a payment is not equivalent to a policy agent's claim about eligibility. One cannot overrule the other by weight of numbers.

### 5. The policy engine has three outcomes, and each is deliberate

**AUTO ACCEPT** — the claims are consistent, the evidence is sufficient, the confidence is above threshold, and the decision is within the policy's delegated authority.

**REQUEST MORE** — there is agreement or no conflict, but the evidence is not sufficient, or the confidence is below threshold. The workflow needs more input before deciding.

**HUMAN ESCALATE** — there is conflict, or the decision is outside the policy engine's authority. A named final authority must decide.

These are not labels. They are next actions. Each one must be wired to a concrete step.

### 6. Final authority is a named role, not a number

The **FINAL AUTHORITY** shield on the right is the named role. It might be a system, a human, or a combination. It must be explicit.

A named role means the workflow can answer the question: *who can overrule the agents?* If the answer is "the one with the highest confidence," the system has no final authority. It has a model popularity contest.

The shield is connected to all three policy outcomes. Even an AUTO ACCEPT must ultimately trace back to a final authority that defined the policy. Even a HUMAN ESCALATE must route to the right person.

### 7. Checkpoint and resume make the decision durable

The **CHECKPOINT / RESUME** chain at the bottom connects the aggregator, policy outcomes, and final authority.

A decision to request more evidence must be checkpointed. An escalation must be resumable when the human responds. The decision is not complete until the durable record contains the result cards, the aggregation, the policy outcome, and the final authority.

This is the same durable vocabulary from the rest of the course. Aggregation is not an exception. It is a workflow step.

### 8. Confidence is a local signal, not a voting weight

Confidence is a statement about the evidence the specialist used. It is not a score that can outrank another, and it is not a vote. A risk agent may be 99% confident in an identity match; a finance agent may be equally confident that the transaction cannot be found. Those two confidences live on different claims, so the **POLICY ENGINE** must ask which source or role is authoritative for each claim and what threshold of confidence and evidence is required. The rule is explicit because the final authority cannot be hidden inside a softmax or a synthesis prompt. A **SpecialistResult** schema should capture the four fields before any synthesis prompt, with the UI showing each claim and its limits. A high confidence with a material limit is an incomplete authority for the final decision.

### 9. The durable record is the contract, not the chat

The **FINAL AUTHORITY** shield is not the end of the story. The workflow must also produce a durable record that says what was requested, which identity owns it, what changed, which attempt produced the change, and what may legally happen next. The record is not the protocol messages, queue receipts, or model reasoning. A transport can retry, a worker can disappear, and an agent can revise its proposal. The durable record is the business truth that survives those changes.

This is why the **CHECKPOINT / RESUME** chain is drawn as a separate chain. It connects the result cards, the aggregation, the policy outcome, and the final authority. Store the aggregation manifest and final decision receipt together, and model commands, events, states, and error outcomes as typed records so tests can replay the same fixture without network calls. An auditor can read the same record and see who had the authority and why.

The same idea appears when parallel workers return results and a join gate decides how many are enough:

![On dark navy, a PARENT WORKFLOW sends cyan arrows to four workers — POLICY WORKER, LEDGER WORKER, FRAUD WORKER, CUSTOMER HISTORY WORKER. Each worker returns a cyan RESULT arrow and a teal ACK arrow to a JOIN GATE, which lists REQUIRED ALL, QUORUM 3 OF 4, OPTIONAL NONE, DEADLINE 30s. The join gate emits a teal arrow through a green check to AGGREGATED EVIDENCE. Two coral dashed paths show STRAGGLER and DUPLICATE outcomes being rejected.](../diagrams/134-fan-out-fan-in-join.png)

That diagram's join gate is the same shape as this diagram's policy engine. Many results arrive, each with its own identity, but the parent does not proceed until a declared rule is satisfied. In the join diagram the rule is quorum and deadline. In this diagram the rule is agreement, conflict, and authority. Both are explicit contracts for when the parent may continue.

---

## Case study — Corvus Underwriting, the two-to-one refund

Corvus processes refund requests for a travel insurer. Three specialist agents evaluate each request: a policy agent checks eligibility, a finance agent checks the payment record, and a risk agent checks identity confidence.

### What they had

A single model that read the outputs of the three agents and produced a single yes/no decision. The model was trained to be "nice" and to approve when the agents mostly agreed.

The result was a simple vote. If two agents said yes and one said no, the model usually approved.

### The incident

A refund request came in. The policy agent said the customer was eligible. The risk agent said the identity match was 99% confident. The finance agent said the payment transaction could not be found.

The model saw two approvals and one objection. It approved the refund. The payment was issued to the customer, but there was no record of the original payment in the provider system.

The customer was happy. The finance team was not. They had paid a refund for a payment that had never been made. The loss was £4,200, but the real damage was that the model had overridden a material objection.

### The new design

Each specialist returns a result card with claim, evidence, confidence, and limits.

- **Policy agent:** claim = eligible, evidence = policy terms and dates, confidence = high, limits = does not know whether the payment was made.
- **Finance agent:** claim = transaction not found, evidence = ledger and provider query, confidence = high, limits = none.
- **Risk agent:** claim = identity verified, evidence = biometric match, confidence = 99%, limits = does not address payment existence.

The aggregator compares the claims. It sees that the finance agent's claim directly contradicts the implicit assumption behind the policy and risk approvals. The approvals are not about the same thing as the finance objection.

The policy engine is configured with a rule: *a refund requires proof of payment*. The finance agent's claim of *transaction not found* triggers **REQUEST MORE** if the customer can provide proof, or **HUMAN ESCALATE** if the contradiction is high-value.

A refund is never approved by majority vote. The final authority is the senior underwriter for refunds above £1,000, or a fully automated rule only when all three claims are consistent and payment proof is present.

### Results

- **Refunds approved while payment record was missing:** 3 in one quarter → 0.
- **Overruled specialist objections by majority:** any number → 0.
- **Escalations with complete evidence bundle:** 60% had incomplete context → 100% include all three result cards.
- **Mean time to resolve a disputed refund decision:** 4 hours → 25 minutes, because the aggregator shows the exact conflict.

### The line in their underwriting standard

*A model cannot overrule a material objection it does not understand. The final authority is named, and majority vote is not a decision rule.*

---

## Composition

Three agents on the left, each producing a result card, feeding an aggregator that separates agreement and conflict, then a policy engine with three outcomes, and a final authority shield.

**Left column:** three blue platforms stacked vertically:
- **POLICY AGENT** — person icon.
- **FINANCE AGENT** — person icon.
- **RISK AGENT** — person icon.

From each agent, a **cyan arrow labelled FORWARD WORK** points to a **RESULT CARDS** card.

**Each result card** has four rows:
- **CLAIM** — document icon.
- **EVIDENCE** — magnifier icon.
- **CONFIDENCE** — bar chart icon.
- **LIMITS** — shield icon.

From each result card, a **teal arrow labelled EVENT** points to the central **AGGREGATOR** — a blue platform with a database stack.

Dashed **teal arrows labelled ACKNOWLEDGEMENT** and **RECEIPT** return from the aggregator to each result card.

**Below the aggregator:** two white cards:
- **AGREEMENT** — green check.
- **CONFLICT** — red X.

**To the right of the aggregator:** **POLICY ENGINE** — a blue gear platform.

From the policy engine, three **cyan arrows** fan to:
- **AUTO ACCEPT** — green check.
- **REQUEST MORE** — question mark.
- **HUMAN ESCALATE** — person icon.

**Top right:** a **red MAJORITY VOTE** box with a red X and **NOT AUTHORITY**.

**Bottom:** a **teal dashed chain** labelled **CHECKPOINT / RESUME** connecting the policy outcomes to the **FINAL AUTHORITY** shield on the far right.

## Element by element

**POLICY / FINANCE / RISK AGENT** — the specialist advisors.
**RESULT CARDS** — the structured output of each agent.

**CLAIM / EVIDENCE / CONFIDENCE / LIMITS** — the four required fields.

**AGGREGATOR** — the comparison engine.
**AGREEMENT** — consistent or complementary findings.
**CONFLICT** — contradictory or incompatible findings.

**POLICY ENGINE** — the rule-based decision gate.
**AUTO ACCEPT / REQUEST MORE / HUMAN ESCALATE** — the three outcomes.

**MAJORITY VOTE** — explicitly not authority.
**FINAL AUTHORITY** — the named decision-maker.

**CHECKPOINT / RESUME** — durable workflow chain.

## Colour and flow semantics

- **Cyan arrows** carry forward work from agents to result cards, and from policy engine to outcomes.
- **Teal arrows** carry events from result cards to aggregator.
- **Teal dashed** carries acknowledgements, receipts, checkpoints, and resumes.
- **Red** on **CONFLICT**, **MAJORITY VOTE**, and the X marks conditions that do not resolve the decision.
- **Green** on **AGREEMENT** and **AUTO ACCEPT** marks positive but not final states.
- The **FINAL AUTHORITY shield** is the only blue authority symbol on the right.

## How to present it

**Start with the question of who decides.** Three agents give advice. Who has the authority? Most rooms will say the system or the user. Ask them if it is written down.

**Point at the result cards.** Claim, evidence, confidence, limits. Ask what their agents currently return. Usually it is one number or one sentence.

**Show the aggregator.** It is not a synthesizer. It compares structured cards. Agreement and conflict are both visible.

**Point at the red MAJORITY VOTE box.** This is the most important warning. Three agents agreeing does not grant them authority. A majority is not a decision rule.

**Trace the policy engine outcomes.** AUTO ACCEPT, REQUEST MORE, HUMAN ESCALATE. Each is a concrete next action. Ask which one their system takes when agents disagree.

**Name the final authority.** It must be a role, not a score. It could be a human, a policy system, or a combination. But it must be named.

**Tell the Corvus story.** Two approvals overrode a missing payment record. The model approved a £4,200 refund for a payment that never happened. The fix: result cards with limits, aggregator that detects conflict, policy engine rule requiring proof, named underwriter authority.

**Emphasize the durable chain.** The aggregation, the conflict, the policy outcome, and the final authority must be checkpointed. A disputed decision must be resumable.

**Close on the standard.** *A model cannot overrule a material objection it does not understand. The final authority is named, and majority vote is not a decision rule.*

**Run the checkpoint and the lab together.** Ask when majority vote is appropriate. Then ask the room for one case and have them produce three specialist result cards, define claim-specific authority, and choose escalation outcomes.

**Map the glossary to the diagram.** Aggregation is combining structured outcomes; disagreement is incompatible claims or evidence; final authority is the role allowed to bind the decision. Check the A2A Protocol 1.0 specification and A2A key concepts.

**Timing.** Twenty-five minutes. Thirty if the room maps one real multi-agent decision and checks whether conflicts are preserved or smoothed over.

---

## Lab and checkpoint

**Lab:** Pick one decision in your system that uses multiple agents or models. Define a structured result card with claim, evidence, confidence, and limits. Build an aggregator that compares cards, detects conflict, and routes to policy outcomes: auto accept, request more, or human escalate. Name the final authority for each outcome.

**Checkpoint:** Why is majority vote not a decision rule?

**Answer:** Because three agents agreeing does not give them authority if they all lack proof, if they are all wrong, or if an exception contradicts them. Authority is a named role or policy, not a count. A majority can produce confident, wrong decisions.

## Glossary

- **Aggregator** — the component that compares structured result cards.
- **Agreement** — the state where cards support the same claim.
- **Auto accept** — the outcome where the policy accepts the aggregated result.
- **Claim** — the conclusion a result card makes.
- **Confidence** — the local signal from one card, not a voting weight.
- **Conflict** — the state where cards make incompatible claims.
- **Evidence** — the support a card provides for its claim.
- **Final authority** — the named role or system that can bind the decision.
- **Human escalate** — the outcome where a person makes the decision.
- **Limits** — the bounds or caveats on a card's claim.
- **Majority vote** — a count that must not be the decision rule.
- **Policy engine** — the rule set that chooses the outcome.
- **Request more** — the outcome where additional evidence is needed.
- **Synthesis** — the attempt to merge answers into one; aggregation is not synthesis.

## Sources

- Multi-agent aggregation and final authority
- A2A protocol and specialist agent results
- Human escalation and policy engines
