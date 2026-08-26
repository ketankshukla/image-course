# Diagram 30 — Loan Document Review

![Five stages across dark navy. APPLICATION shows a teal folder labelled APPLICATION with green-ticked form pages. RAG RULES shows POLICY and REGULATION books with a magnifier and a card reading EVIDENCE RETRIEVED. MCP SYSTEMS shows a toolbox marked MCP with dashed lines to institution, identity and document blocks over a card reading SYSTEMS QUERIED THROUGH MCP. A2A RISK REVIEW shows two circulating robots with a card reading RISK REVIEW TASK DELEGATED TO SPECIALIST AGENT and a panel headed AGENT PROVIDES: EVIDENCE PACKAGE and RISK RECOMMENDATION. HUMAN DECISION shows a person at a REVIEW SUMMARY screen with teal APPROVE and coral DECLINE buttons. A full-width banner beneath reads AGENT SUPPLIES EVIDENCE & RECOMMENDATION, then an arrow, then HUMAN DECIDES.](../diagrams/30-loan-document-review.png)

**Module:** 6 — End-to-end use cases
**Role in the course:** high-stakes human-decision architecture
**Layout:** five stages with a full-width thesis banner beneath

---

## At a glance

A lending pipeline: **APPLICATION → RAG RULES → MCP SYSTEMS → A2A RISK REVIEW → HUMAN DECISION**, with a banner across the bottom spelling the architecture's thesis in words: **AGENT SUPPLIES EVIDENCE & RECOMMENDATION → HUMAN DECIDES**.

It is the only diagram in the library that states its argument in text rather than trusting the composition. That choice is appropriate here, because this is the use case where the boundary is a legal and regulatory obligation rather than a design preference, and ambiguity about it is not acceptable.

---

## What the diagram teaches

### 1. The banner is the diagram, and everything above it is supporting detail

Across the bottom: a robot icon with **AGENT SUPPLIES EVIDENCE & RECOMMENDATION** in teal, a long teal arrow, a person icon with **HUMAN DECIDES** in coral.

Two roles, one arrow between them, no ambiguity. The agents produce; the human decides. The arrow runs one way.

Spelling it out is a response to a specific risk in high-stakes domains: **decision authority drifts**. It starts as "the agent recommends and a human decides," and then the human is approving forty an hour, and then the well-evidenced ones are batched, and then the batch is the default. Nobody makes that decision; it accumulates.

A banner that says the thing in words is harder to erode than a composition that implies it.

### 2. Both outcomes are drawn, and both are buttons

The human decision stage shows two physical buttons: a **teal APPROVE** and a **coral DECLINE**, adjacent, similar in size.

Most human-in-the-loop diagrams show an approve button. This shows both, which asserts that **declining is a first-class outcome**, not an exception or a failure of the process.

That matters in lending specifically. A pipeline where approval is the drawn path and decline is unillustrated encodes an expectation, and expectations become defaults. A reviewer whose interface makes approval the obvious action is a reviewer who approves.

The colours are consistent with the library — teal for committed, coral for refused — but the equal weight is the design content.

### 3. Rules and systems are separated, and in lending the distinction is regulatory

**RAG RULES** shows two books: **POLICY** with a shield, and **REGULATION** with a government building icon. Below, a card reads **EVIDENCE RETRIEVED**.

**MCP SYSTEMS** shows a toolbox with dashed lines to three blocks — an institution, an identity record, a document store — over a card reading **SYSTEMS QUERIED THROUGH MCP**.

The split is the boundary lesson, and in lending it carries additional weight.

**Rules** are documents: the lender's credit policy and the applicable regulation. They change on a governance cycle, they are versioned, and a decision must be made against the version in force at the time. Retrieval must be able to answer not just "what does policy say" but "what did policy say on the date this application was assessed."

**Systems** are live: the applicant's bank data, identity verification, credit reference, and the submitted documents. They change constantly. Indexing them would produce decisions made on stale financial data, which in lending is a serious defect.

Two book icons rather than one is also deliberate. Internal policy and external regulation are different sources with different authorities, and where they conflict the regulation governs. A retrieval layer that flattens them into one corpus loses that.

### 4. The specialist provides two things, and the diagram lists them separately

The A2A stage carries a panel headed **AGENT PROVIDES:** with two rows:

- A document icon and **EVIDENCE PACKAGE**
- A **coral-shielded** icon and **RISK RECOMMENDATION**

Two distinct deliverables, and the separation is the point.

The **evidence package** is what was found: the applicant's position, the affordability calculation, the documents verified, the discrepancies noticed. Facts, assembled.

The **risk recommendation** is an opinion about what those facts mean. Coral-shielded because it is the thing that carries risk — not the risk of the loan, the risk of the recommendation being mistaken for a decision.

A reviewer needs both, and needs them separable. A reviewer given only a recommendation is being asked to rubber-stamp. A reviewer given only evidence is being asked to do the analysis themselves, which defeats the purpose. Given both, they can check whether the recommendation follows from the evidence — which is the actual review task.

### 5. The task is labelled as delegated, in the diagram

The A2A stage carries a card reading **RISK REVIEW TASK DELEGATED TO SPECIALIST AGENT**.

Stating it in the architecture matters for a regulated process. Whoever audits this needs to know that risk assessment happened outside the primary system, by a different component, under a bounded task — because that affects what evidence exists, what the specialist saw, and who is accountable for the assessment.

The bounded delegation model applies directly, including the part where the lender's own policy never crosses to the specialist:

![A caller agent creating a task that crosses a bridge to a specialist agent and returns an artifact, with DOMAIN + POLICY on a separate platform connecting only to the caller.](../diagrams/21-a2a-delegation.png)

### 6. The application arrives as verified documents, not as raw input

Stage 1 shows a **teal folder labelled APPLICATION** with **green-ticked form pages** behind it.

The ticks say the application has already been checked for completeness before entering the pipeline. Not assessed — checked. All required fields present, required documents supplied, formats valid.

That pre-check is doing real work. An assessment pipeline running on incomplete applications produces assessments that must be redone, and — worse — assessments that silently treat a missing document as an absent liability.

### 7. There is no return loop, and the absence is meaningful

Every other use case in this module has a dashed return path. This one does not.

That fits the domain. A lending decision is a terminal act with a regulatory record attached. It does not loop back to refine the question. The applicant is approved or declined, the decision is recorded with its evidence, and if the applicant disagrees the route is an appeal — a separate governed process, not a re-run of the pipeline.

Worth naming when teaching, because a room that has seen diagrams 27, 28 and 29 will notice the missing line and should understand it as deliberate.

---

## Case study — Halstead Building Society, mortgage underwriting support

Halstead is a mid-sized mutual lender writing around 9,000 residential mortgages a year. Underwriting is done by a team of thirty-one underwriters, and it is regulated work — decisions must be explicable, consistent, non-discriminatory, and auditable for years.

They built an assistant to support underwriting. The regulatory position was established before a line of code: **the assistant may not make a lending decision, and every decision must be attributable to a named underwriter.**

### Stage 1 — Application

A complete application arrives: applicant details, income evidence, bank statements, credit report consent, property details, and the requested loan.

Completeness checking happens before the pipeline. Around 22% of submissions fail it and are returned for information — a routine step, and one Halstead deliberately kept separate from assessment so that an incomplete application is never assessed.

### Stage 2 — RAG Rules

Two distinct corpora, matching the diagram's two books.

**Policy** — Halstead's own lending criteria: income multiples, acceptable income types, property types, adverse credit tolerances, affordability stress rates. About 400 pages, revised roughly quarterly.

**Regulation** — the applicable conduct rules on responsible lending, affordability assessment, and vulnerable customers.

Two properties of their retrieval matter.

**Version-aware.** Every retrieval is qualified by the application's assessment date, so a decision made in March is assessed against March's policy. A decision reviewed a year later can be checked against what was actually in force. This was a regulatory requirement and it shaped the ingestion design — superseded policy versions are retained and retrievable, never deleted.

**Precedence-aware.** Where internal policy is more restrictive than regulation, policy governs. Where regulation is more restrictive, regulation governs. The assistant surfaces both and marks which applies, rather than resolving the conflict silently.

### Stage 3 — MCP Systems

The gateway reaches the three categories the diagram's blocks depict:

- **Institution data** — bank transaction data via open banking, with the applicant's consent.
- **Identity** — identity verification and the credit reference agency.
- **Documents** — the submitted evidence: payslips, accounts, the valuation.

All reads. There is no write capability anywhere in the assistant. It cannot mark an application, cannot issue an offer, cannot record a decision. The decision is recorded by the underwriter's own system when they press a button.

That constraint was an early design decision and it eliminated a whole category of concern in the regulatory review. There is no path by which the assistant can effect an outcome.

The assistant establishes the facts: verified income of £58,400 against declared £61,000 — a discrepancy — twelve months of transaction data showing stable commitments, one missed credit card payment fourteen months ago, and a property valuation £8,000 below the purchase price.

### Stage 4 — A2A Risk Review

Halstead's credit risk function operates its own assessment agent. It is separate from the underwriting assistant for the same reason a reviewer should not be the author: risk methodology is owned by credit risk, changes on their cycle, and is subject to its own model governance.

The task is bounded. It carries the verified financial position, the affordability inputs, the credit history summary, the property position, and the loan requested. It does not carry the applicant's name, address, age, or any protected characteristic — a deliberate exclusion, both because those are not risk inputs under Halstead's methodology and because their presence in a risk assessment would be a discrimination exposure.

The agent returns the two things the diagram names.

**Evidence package** — the affordability calculation with its inputs and the stress rate applied, the income verification result including the £2,600 discrepancy, the credit summary, the loan-to-value at the valuation rather than the purchase price, and every policy rule evaluated with its outcome.

**Risk recommendation** — proceed with conditions: the income discrepancy requires explanation, and the LTV at valuation moves the case into a higher band requiring a larger deposit or a reduced advance.

### Stage 5 — Human decision

An underwriter reviews. Their screen shows the summary, the evidence package, the recommendation, the policy findings, and the discrepancies — and the two buttons.

In this case the underwriter approved, at the reduced advance the valuation supported, after obtaining an explanation for the income discrepancy (a bonus included in the declared figure that did not meet Halstead's criteria for sustainable income).

Note what the underwriter did that the agent could not: they contacted the applicant, evaluated an explanation, and applied judgement about whether the bonus history was sufficiently established. The recommendation was input to that.

### The drift they watched for

Six months in, Halstead audited concordance between recommendations and decisions. Underwriters agreed with the risk recommendation in 91% of cases.

Their compliance team treated that number as a question rather than a result. High concordance is consistent with two very different situations: a good recommendation engine, or underwriters deferring.

They investigated by examining the 9% of disagreements and, separately, sampling agreements to check whether the underwriter's recorded reasoning showed independent assessment or merely restated the recommendation.

The finding was mixed. Most agreements showed genuine independent reasoning. A minority — around 6% of the sample — recorded reasoning that was substantially a restatement.

**What they changed.** The interface no longer shows the recommendation first. The underwriter sees the evidence package, records their own assessment, and then sees the recommendation. If they differ, the underwriter is asked to reconcile before proceeding.

This slowed review by about ninety seconds per case. Concordance fell to 86%. Their compliance team regarded the fall as an improvement, because the remaining agreement is more likely to be genuine.

This is the decision-authority drift the banner exists to resist, caught early because someone treated a good-looking number as a question.

### What the architecture produced

- **Time per case** from an average of 47 minutes to 26.
- **Consistency** — variance in outcomes for materially similar applications narrowed substantially, which their conduct-risk function considers the most important result.
- **Audit reconstruction** — establishing the basis of a past decision went from hours to minutes, because the evidence package, policy versions, and underwriter reasoning are linked to the decision record.
- **Decisions made by the assistant**: zero, by construction.

### The line they hold

Halstead has been asked whether straightforward cases — strong applicants, no discrepancies, comfortable affordability — could be auto-approved.

They have declined, and their reasoning is regulatory rather than technical: **a lending decision must be attributable to a person who can explain it.** An auto-approved case is a decision with no author, and the fact that it was an easy case does not change what it is.

Their head of underwriting adds a second argument that generalises: the easy cases are what keep underwriters calibrated. A team that only ever sees difficult cases loses its sense of the distribution.

---

## Composition

Five stages run left to right, headed by white uppercase labels and connected by cyan arrows. Several stages carry explanatory cards beneath them. Across the bottom of the frame, a full-width bordered banner states the thesis.

**APPLICATION → RAG RULES → MCP SYSTEMS → A2A RISK REVIEW → HUMAN DECISION**

## Element by element

**APPLICATION**
A **teal folder** with a person icon, labelled **APPLICATION**, in front of two white form pages carrying **green-ticked rows**. A checked, complete submission.

**RAG RULES**
Two upright books: a blue one labelled **POLICY** with a **shield**, and a dark one labelled **REGULATION** with a **government building** icon. A **teal magnifying glass** sits at the lower left. A white card in front reads **EVIDENCE RETRIEVED** with two green-ticked rows.

**MCP SYSTEMS**
The green toolbox carrying a dark plaque reading **MCP**, with gear, plug and database tiles. Three **dashed cyan lines** descend to three blue blocks showing an **institution**, a **person record**, and a **document**. Below, a white card with a green check reads **SYSTEMS QUERIED THROUGH MCP**.

**A2A RISK REVIEW**
A blue cube robot above and a teal cube robot below with curved cyan arrows circulating between them. A white card reads **RISK REVIEW TASK DELEGATED TO SPECIALIST AGENT** with a green check. Below, a dark panel headed **AGENT PROVIDES:** in teal lists two rows — a document icon with **EVIDENCE PACKAGE**, and a **coral shield** icon with **RISK RECOMMENDATION**.

**HUMAN DECISION**
A person seated at a keyboard facing a large monitor headed **REVIEW SUMMARY**, showing a document icon, a **coral shield**, text rows and three green ticks. To the right of the desk sit two buttons: a **teal APPROVE** with a check, and a **coral DECLINE** with an ✗.

**The banner**
A full-width bordered panel across the base of the frame containing: a teal robot icon, the text **AGENT SUPPLIES EVIDENCE & RECOMMENDATION** in teal, a long **teal arrow**, a coral person icon, and the text **HUMAN DECIDES** in coral.

## Colour and flow semantics

- **Cyan arrows** carry the pipeline forward; **dashed cyan** descends to the three queried systems.
- **Coral** appears three times, each marking something that carries risk or refuses: the **RISK RECOMMENDATION** shield, the shield on the review summary, and the **DECLINE** button.
- **Teal** marks the application folder, the agent's supply role in the banner, and the **APPROVE** button.
- The two decision buttons are drawn at **equal size and adjacency**, refusing to make approval the default path.
- **There is no return loop**, unlike the other three use cases — a lending decision is terminal, with appeal as a separate governed process.

## How to present it

**Read the banner out loud before anything else.** Agent supplies evidence and recommendation; human decides. Then ask why this is the only diagram in the library that states its thesis in words. The answer — decision authority drifts, and a composition can be eroded where a sentence cannot — is the session's core.

**Point at the two buttons.** Ask what it means that decline is drawn at equal weight. Then ask what their own review interfaces look like: is declining as easy as approving, or is approval the obvious action? Interface design encodes expectations, and expectations become defaults.

**Separate the two books.** Internal policy and external regulation, different authorities, and a precedence rule where they conflict. Ask whether their retrieval distinguishes sources by authority, or flattens everything into one corpus.

**Ask about version-awareness.** What did policy say on the date the decision was made? Most retrieval systems cannot answer this, because superseded documents are removed. In regulated domains it is a requirement, and it has to be designed into ingestion rather than added later.

**Interrogate the two deliverables.** Evidence package and risk recommendation, listed separately. Ask what a reviewer given only the recommendation is doing. Rubber-stamping. Only evidence? Doing the whole analysis themselves. Both, separable, is what makes review a real task — the reviewer checks whether the recommendation follows from the evidence.

**Tell the concordance story.** 91% agreement, treated as a question rather than a result. The investigation, the 6% of restated reasoning, and the interface change that shows evidence before recommendation. This is the single most useful thing in this document, because it is a concrete method for detecting authority drift rather than merely warning about it.

**Ask what they would measure.** If a room says they have human oversight, ask how they would know if it had become nominal. Concordance rate, reviewer time per case, and whether recorded reasoning is independent or restated. Most have no measure at all.

**Run the auto-approve challenge.** Someone will propose it for easy cases. Give them both of Halstead's arguments: a decision must be attributable to a person who can explain it, and the easy cases are what keep reviewers calibrated. The second one is less obvious and often more persuasive.

**Note the missing return loop.** A room that has seen the other three use cases will notice. It is deliberate — a lending decision is terminal, and disagreement routes to appeal, not to a re-run.

**Timing.** Thirty minutes. Forty-five with the concordance discussion, which is the version worth running for anyone building human-in-the-loop systems in a regulated domain.

---

## Lab and checkpoint

**Lab:** Take one regulated decision in your domain and design a review workflow that produces two separable deliverables: an evidence package and a recommendation. Define the concordance metrics you would use to detect whether review has become nominal, and the version-aware retrieval rule that lets you answer "what did the policy say on the date of this decision?"

**Checkpoint:** Why should evidence and recommendation be listed as separate deliverables?

**Answer:** Because a reviewer given only a recommendation is rubber-stamping; a reviewer given only evidence is doing the whole analysis themselves. Separating the two lets the reviewer check whether the recommendation actually follows from the evidence, which makes review a real task.

## Glossary

- **Authority** — the source whose rule takes precedence when policy and regulation conflict.
- **Concordance** — the rate at which reviewer decisions agree with agent recommendations, used to detect review drift.
- **Evidence package** — the collected, cited sources that support a decision.
- **External regulation** — rules from outside the organisation that bind the decision.
- **Internal policy** — the organisation's own rules for the decision.
- **Recommendation** — the proposed decision derived from the evidence package.
- **Restated reasoning** — a reviewer explanation that merely repeats the agent's reasoning instead of being independent.
- **Version-awareness** — the ability to retrieve the policy or regulation as it existed on a specific date.

## Sources

- Regulated decision review and human-in-the-loop controls
- Citation, attribution, and concordance measurement
- Version-aware document retrieval and policy governance
