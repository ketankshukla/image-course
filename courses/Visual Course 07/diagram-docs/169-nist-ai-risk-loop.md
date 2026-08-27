# Diagram 169 — The NIST AI Risk Loop in Plain English

![On a dark navy field, the Acme agent system sits at the center of a continuous four-part loop: GOVERN, MAP, MEASURE, MANAGE. Cyan arrows run clockwise between the four cobalt platforms. GOVERN holds white cards for OWNERS, POLICIES, and CULTURE. MAP holds CONTEXT, PEOPLE, IMPACTS, and THREATS. MEASURE holds TESTS, METRICS, RED TEAM, and UNCERTAINTY. MANAGE holds PRIORITIZE, CONTROL, RESPOND, and MONITOR. A teal EVIDENCE REPOSITORY and a REVIEW DATE ring connect all four quadrants, with teal arrows showing evidence flowing into every function and a small coral path marking a documented residual-risk exception.](../diagrams/169-nist-ai-risk-loop.png)

**Module:** Governance and organizational control  
**Role in the course:** how to use the NIST AI Risk Management Framework as a repeating management loop instead of a one-time compliance checklist  
**Layout:** four cobalt platforms arranged in a loop around the Acme agent system, connected by cyan arrows, with an evidence repository and review date as a connecting ring  
**Standards status:** NIST AI RMF 1.0; revision underway

---

## At a glance

**GOVERN → MAP → MEASURE → MANAGE → GOVERN.**

The NIST AI Risk Management Framework becomes a **living management cycle**. **GOVERN** names owners, policies, and risk culture. **MAP** understands the use case, affected people, assets, and threats. **MEASURE** evaluates risk and controls with tests, metrics, red-team exercises, and an honest account of uncertainty. **MANAGE** prioritizes, treats, responds, and monitors. An **EVIDENCE REPOSITORY** and a **REVIEW DATE** connect every part, so the loop repeats whenever the system, threats, law, or business change.

The outcome: **use the NIST AI RMF as a repeating management loop instead of a one-time compliance checklist.**

---

## What the diagram teaches

### 1. Govern is the starting posture, not the finish line

**GOVERN** names the roles that own risk decisions, the policies that constrain them, the risk appetite that tells the organization what is acceptable, and the culture that makes people report problems. In the diagram, the GOVERN quadrant holds **OWNERS**, **POLICIES**, and **CULTURE** as live records. Like running a safe school, you set responsibilities first, understand the activities, inspect conditions, fix the biggest risks, and repeat as things change.

### 2. Map turns vague worry into named context and impact

**MAP** answers *what are we doing, and who gets hurt if it goes wrong?* It identifies the intended use, affected people, business and technical assets, dependencies, trust boundaries, threats, and unacceptable outcomes. The MAP quadrant holds **CONTEXT**, **PEOPLE**, **IMPACTS**, and **THREATS**. The Acme agent stops being "an AI project" and becomes a system that processes vendor attachments, handles refund payments, and could expose customer data or move money to the wrong account.

### 3. Measure replaces opinion with evidence and uncertainty

**MEASURE** proves or disproves risk claims. It runs evaluations, security tests, privacy reviews, red-team exercises, and reviews of incident data. It records **UNCERTAINTY** because not every risk can be quantified. A metric without a test is a vanity number. A test without an expected outcome is an experiment, not a control. The quadrant includes **TESTS**, **METRICS**, **RED TEAM**, and **UNCERTAINTY**.

### 4. Manage turns evidence into accountable action

**MANAGE** prioritizes risks, selects controls, decides whether residual risk is acceptable, deploys carefully, monitors for change, and responds when the evidence shifts. The MANAGE quadrant holds **PRIORITIZE**, **CONTROL**, **RESPOND**, and **MONITOR**. This is where Acme decides whether the attachment-assisted refund feature launches, launches with restrictions, or is blocked until controls improve. Every choice needs an owner and a review date.

### 5. The loop feeds back through change

The arrow from MANAGE back to GOVERN is not decorative. Incidents, new threats, customer feedback, model updates, vendor changes, and legal developments all feed back into the loop. A risk register reviewed annually is already out of date. The review date is a trigger, not a deadline to miss.

### 6. Map makes unacceptable outcomes visible before controls are chosen

The most common mistake is to buy controls before the team agrees on what must not happen. Map draws the path from intended use to unacceptable business outcomes: a redirected refund, a cross-tenant answer, a leaked credential, a missing audit record. The safety rule is: no consequential flow crosses a trust boundary without an identified caller, intended resource, policy check, and evidence owner.

### 7. Evidence is the thread that stitches the loop together

Govern, Map, Measure, and Manage all consume and produce evidence. GOVERN needs policy versions and owner assignments. MAP needs asset inventories and threat scenarios. MEASURE needs test results and red-team reports. MANAGE needs control deployment records and residual-risk decisions.

That evidence must be trustworthy. It is not enough to write "we tested prompt injection" on a slide. The organization needs logs, receipts, hashes, redacted artifacts, and access records that an auditor or incident responder can review later.

![On a dark navy field, a horizontal chain of audit events runs from left to right through INPUT RECEIVED, IDENTITY VERIFIED, POLICY DECISION, APPROVAL, ACTION, RECEIPT, and REVIEW. Each event card contains TIME, ACTOR, TENANT, ACTION, RESULT, CORRELATION, and PREVIOUS HASH. A raw sensitive payload passes through a redaction gate into a sealed evidence store. A hash chain links the events, and a coral DELETE or EDIT event is shown breaking the chain and raising an alert.](../diagrams/168-tamper-evident-audit-chain.png)

This is the same evidence idea shown in Diagram 168. The audit chain preserves the who, what, when, and why of consequential decisions while redaction keeps secrets and personal data out of general logs. The risk loop cannot be credible without evidence that is tamper-evident, redacted, and reviewable.

### 8. Measure includes red team, privacy, and recovery tests, not only benchmarks

A benchmark score does not tell you whether a malicious attachment can redirect a refund. MEASURE includes **TESTS** for injection, tool misuse, identity abuse, cross-tenant leakage, and egress; **METRICS** for policy coverage and incident rates; **RED TEAM** exercises for realistic attacker paths; and **UNCERTAINTY** registers for risks that cannot yet be quantified. If a risk cannot be tested, it should still be documented with an owner and a plan to reduce uncertainty.

### 9. Govern is cross-cutting, not a phase that ends

The NIST AI RMF places **GOVERN** as a function that runs through every other function, not as a stage that finishes before Map begins. Owners, policies, and culture do not go away after the kickoff. If the owner, policy, or risk appetite changes, the whole loop is revisited.

### 10. Manage turns residual risk into an accountable decision

Every control leaves some risk behind. **Residual risk** is the risk that remains after treatment. The diagram marks it with a small coral path because it is not "green" safe; it is a deliberate exception that must be named, owned, documented, and reviewed. The PRIORITIZE step decides which risks to reduce, transfer, or accept. The decision is a governance record: the risk, rationale, controls, evidence, owner, and review date.

### 11. The framework is a baseline, not a certificate

NIST AI RMF 1.0 is the published baseline, and NIST is working on a revision. Using it means building the organizational machinery that makes the loop repeat. The diagram does not promise that the agent is safe. It promises a visible process that can be inspected, tested, and improved.

### 12. The loop becomes real in dashboards and services

The four functions need data structures and tooling.

**Next.js map:**
- Build a governance dashboard that reads versioned risk records, control evidence, owners, exceptions, review dates, incidents, and deployment manifests from server-authorized sources.
- Keep tokens, policy decisions, secrets, and privileged mutations in authenticated server code; send the browser only the minimum display state.
- Use typed request, decision, denial, approval, and receipt records so the React interface can explain security state without inventing it.

**Python map:**
- Define `Risk`, `Control`, `Evidence`, `Evaluation`, `Exception`, `Incident`, `Owner`, and `Review` models and produce traceable reports from one governance service.
- Use Pydantic models plus explicit middleware or service boundaries for identity, tenant, policy, data classification, and audit context.
- Test allow and deny paths with hostile synthetic fixtures and dependency-injected identity, policy, storage, secret, and network adapters.

---

## Case study — Acme attachment-assisted refunds

Acme wants to launch a feature that lets customers upload an attachment while requesting a refund. A red-team test shows that a malicious file can inject instructions, and an egress test shows the agent could be redirected to send data to an attacker.

### The decision they had to make

Product wants to launch. Security wants to block until injection and egress are solved. Finance wants to protect the payment boundary. Privacy wants to know what personal data the attachment contains. Operations wants a clear owner and review cadence.

### What they did

The team runs the NIST AI risk loop:

1. **Govern:** Security owns the injection and egress risk, Finance owns the payment control, Privacy owns the data classification, Product owns the customer experience, and Operations owns the launch cadence. The risk appetite is written down: no refund moves to a new payee without a bound, step-up approval.

2. **Map:** They identify affected customers, payment assets, the attachment trust boundary, remote parsers, human reviewers, and unacceptable outcomes: a redirected refund, cross-tenant disclosure, and an unreviewed high-value refund.

3. **Measure:** They run injection tests against the content parser, cross-tenant tests, approval-binding tests, egress tests, privacy impact tests, and recovery tests. Results are stored with version, owner, and uncertainty notes.

4. **Manage:** They restrict the launch to low-value refunds under a human review queue. High-value refunds require an explicit approval bound to the original payee. The residual risk of low-value auto-routing is accepted with a documented exception and a 30-day review trigger.

### The result

Launch becomes an evidence-backed, accountable decision rather than a vague claim that the AI is safe. The team can show who owns each risk, what was tested, what controls are in place, and when the decision will be reviewed.

### What could have gone wrong

Filling a spreadsheet once and moving on would create paperwork, not risk management. No owner means no one fixes the controls. No measurement means no one knows the tests passed. No review date means the risk decays in place. No evidence means the launch cannot be explained after an incident.

### The line in their governance standard

*Every material agent risk has a context, impact, owner, measurement, treatment, residual-risk decision, evidence, and review trigger. The NIST loop repeats whenever the context changes.*

---

## Composition

The diagram is built around a central **ACME AGENT SYSTEM** node, surrounded by four cobalt platforms in a clockwise loop.

**Top platform:** **GOVERN** — with **OWNERS**, **POLICIES**, and **CULTURE**.  
**Right platform:** **MAP** — with **CONTEXT**, **PEOPLE**, **IMPACTS**, and **THREATS**.  
**Bottom platform:** **MEASURE** — with **TESTS**, **METRICS**, **RED TEAM**, and **UNCERTAINTY**.  
**Left platform:** **MANAGE** — with **PRIORITIZE**, **CONTROL**, **RESPOND**, and **MONITOR**.

**Cyan arrows** run clockwise from GOVERN → MAP → MEASURE → MANAGE → GOVERN.  
**Teal arrows** run from each platform toward a central **EVIDENCE REPOSITORY** and a surrounding **REVIEW DATE** ring.  
**Coral path:** a small residual-risk exception route from MANAGE back toward GOVERN.

## Element by element

**GOVERN** — establish accountability and how risk decisions are made.  
**MAP** — understand context, people, use, impacts, and boundaries.  
**MEASURE** — evaluate risk and controls with evidence and uncertainty.  
**MANAGE** — prioritize, treat, respond, and monitor risk.  
**ACME AGENT SYSTEM** — the system being managed, at the center.  
**EVIDENCE REPOSITORY** — shared record of policies, tests, decisions, approvals, incidents, and exceptions.  
**REVIEW DATE** — the trigger that forces the loop to repeat.  
**OWNERS, POLICIES, CULTURE** — governance records.  
**CONTEXT, PEOPLE, IMPACTS, THREATS** — mapping records.  
**TESTS, METRICS, RED TEAM, UNCERTAINTY** — measurement records.  
**PRIORITIZE, CONTROL, RESPOND, MONITOR** — management records.  
**Residual-risk exception** — documented, owned, and reviewed decision to accept remaining risk.

## Colour and flow semantics

- **Cobalt platforms** are protected governance functions and the Acme agent system at the center.
- **Cyan arrows** carry the management loop clockwise.
- **Teal arrows** carry evidence and review paths to the repository and the review date.
- **Coral path** marks a residual-risk exception: a documented and owned decision, not a failure to mitigate.
- **White cards** represent named records: owners, policies, context, tests, controls, and residual-risk decisions.

## How to present it

**Ask the room what a risk framework means in practice.** Most will describe a spreadsheet or a certification. Ask when it was last updated and who owns the update.

**Point at the four platforms and read the loop.** Govern → Map → Measure → Manage → Govern. The arrow back to Govern is the mechanism that keeps the framework alive.

**Read the GOVERN quadrant.** Owners, policies, culture. Ask who can name the owner of the most important agent risk. If no one can, Govern is incomplete.

**Trace the MAP quadrant.** Context, people, impacts, threats. Ask what the unacceptable outcomes are for their current agent feature. If the list is vague, Map is incomplete.

**Trace the MEASURE quadrant.** Tests, metrics, red team, uncertainty. Ask what the last red-team exercise tested and what evidence it produced. A benchmark is not a red team.

**Trace the MANAGE quadrant.** Prioritize, control, respond, monitor. Ask what a residual-risk decision looks like. If it is a verbal "we're fine," Manage is incomplete.

**Point at the evidence repository and review date.** Every function produces evidence and has a review trigger. Ask where the evidence lives and when the next review is scheduled.

**Show the second diagram, the tamper-evident audit chain.** Explain that the risk loop cannot exist without trustworthy evidence. If decisions can be silently edited or sensitive payloads are stored in plain logs, the loop collapses.

**Tell the Acme attachment-assisted refund story.** The product team wanted to launch; the framework forced them to name owners, map impacts, measure real attacks, and manage residual risk. Launch became an accountable decision, not a guess.

**Run the lab as a five-minute exercise.** Have each group create one risk register row for a redirected refund. Include context, affected people, owner, likelihood uncertainty, impact, controls, tests, evidence, residual decision, exception, trigger, and review date.

**Close with the checkpoint.** Ask: "Which NIST function happens first and then ends?" The answer: none is one-and-done. Govern is cross-cutting, and all four functions repeat as the system and evidence change.

**Mention the sources in context.** The NIST AI Risk Management Framework and AI RMF Core provide the functions; the NIST Generative AI Profile adds guidance for generative systems; and NIST Zero Trust Architecture, the OWASP Agentic Top 10, and Open Policy Agent decision logs provide the control and evidence mechanisms that make the loop concrete.

**Timing.** Twenty-five minutes. Thirty if the room writes a risk register row for a real feature.

---

## Glossary

- **Govern** — establish accountability and risk practice.
- **Map** — understand context and impacts.
- **Residual risk** — risk remaining after treatment.

## Lab and checkpoint


**Lab:** Create one risk register row for redirected refunds with context, affected people, owner, likelihood uncertainty, impact, controls, tests, evidence, residual decision, exception, trigger, and review date.


**Checkpoint:** Which NIST function happens first and then ends?


**Answer:** None is a one-and-done phase. Govern is cross-cutting and all four functions repeat as the system and evidence change.

## Sources

- NIST AI Risk Management Framework
- NIST AI RMF Core
- NIST Generative AI Profile

