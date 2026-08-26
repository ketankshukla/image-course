# Diagram 239 — Threat, evaluation, accessibility, privacy, and readiness gates

![A release candidate passes owned threat, evaluation, accessibility, privacy, and operations gates with evidence, explicit pass or fail, and expiring exceptions before release.](../diagrams/239-readiness-gate-system.png)

**Module:** Delivery and production readiness
**Role in the course:** Combine cross-functional proof into a transparent go, conditional-go, or no-go decision without letting one team self-certify the whole system.
**Layout:** RELEASE CANDIDATE begins on the left and the diagram flows toward REQUIRED PASS; a teal **RELEASE** path is the desired route and a coral **SELF APPROVAL** path is blocked or contained.

---

## At a glance

**Threat, evaluation, accessibility, privacy, and readiness gates** — Combine cross-functional proof into a transparent go, conditional-go, or no-go decision without letting one team self-certify the whole system.

- The central takeaway is: Release only when the exact candidate has the cross-functional evidence its risk requires.
- The visual begins with **RELEASE CANDIDATE** and ends with the diagram's outcome, not a technology name.
- The safe or selected path is marked **teal**: RELEASE only after REQUIRED PASS.
- The blocked or dangerous path is marked **coral**: SELF APPROVAL and PERMANENT EXCEPTION blocked.
- The analogy is: A building cannot open because the paint looks good. Structural, fire, electrical, accessibility, and occupancy reviews each examine different evidence, and unresolved critical findings stop the opening.

---

## What the diagram teaches

### 1. Threat, evaluation, accessibility, privacy, and readiness gates

Evaluation readiness covers representative tasks, slices, graders, human review, uncertainty, regression, adversarial evidence, and limitations. Accessibility readiness uses WCAG 2.2 as a baseline plus semantic inspection and human testing with keyboard, screen reader, zoom, reflow, touch, contrast, status, errors, and reduced motion. Privacy readiness verifies purpose, minimization, consent or other applicable basis, lineage, retention, access, provider transfer, export, correction, deletion, and incident response. In the diagram, **THREAT**, **EVALUATION**, **ACCESSIBILITY** appear at the left, turning this idea into something a reviewer can point at.

### 2. Define Required Evidence and Independent Reviewers for Each Readiness Domain.

A readiness gate turns an important quality into a decision with required evidence, reviewer, scope, result, exceptions, and expiry. The visual places **REQUIRED PASS**, **EVIDENCE** at the center; the arrows between them are the physical expression of this principle. If this is skipped, a broad production-ready label without domain evidence, independent review, and expiring exceptions becomes marketing rather than governance.

### 3. Run Threat, Evaluation, Accessibility, Privacy, and Operational Tests on the Exact Release Candidate.

It prevents security, evaluation, accessibility, privacy, or operations from becoming a final checklist nobody can enforce. The trace asks the team to run threat, evaluation, accessibility, privacy, and operational tests on the exact release candidate. Look at **RELEASE CANDIDATE**, **THREAT**, **EVALUATION** on the top: the diagram uses those elements to show where this decision lives.
![A layered test system combines unit, property, contract, integration, workflow, security, evaluation, accessibility, and acceptance tests using shared fixtures and failure injection to produce an evidence manifest.](../diagrams/238-production-test-pyramid.png)

Diagram 238 — *Contract, integration, workflow, security, and acceptance tests* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 4. Record Pass, Fail, Limitation, Residual Risk, Exception, Compensating Control, Owner, and Expiry.

Threat readiness covers trust boundaries, assets, actors, abuse cases, mitigations, residual risk, attack tests, dependency risk, and incident detection. A single average can hide failure for a policy, language, tenant, or high-impact case. Conditional exceptions are rare, owned, time-limited, visible, monitored, and paired with compensating controls and a removal plan. The picture shows **EXCEPTION EXPIRY**, **REQUIRED PASS**, **PERMANENT EXCEPTION** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: The accessibility and privacy gates fail independently of the quality average.

### 5. Block Release When an Unacceptable Outcome or Mandatory Gate Lacks Proof.

An automated scan alone is not conformance proof. To put this into practice, the team should block release when an unacceptable outcome or mandatory gate lacks proof. At the bottom, **RELEASE CANDIDATE**, **RELEASE** is the element that makes this concept concrete before any code is written.

### 6. Monitor After Release and Reopen the Decision When Models, Data, Tools, Users, Incidents

The course is architecture guidance and does not replace legal review. In the diagram, **RELEASE CANDIDATE**, **RELEASE** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, a broad production-ready label without domain evidence, independent review, and expiring exceptions becomes marketing rather than governance.

### 7. Release only when the exact candidate has the cross-functional evidence its risk

OWASP guidance supplies scenarios, while Acme's architecture determines actual exposure. The same person who created a risky feature should not quietly approve its unresolved gate. The visual places **RELEASE CANDIDATE**, **EVIDENCE**, **RELEASE** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

A building cannot open because the paint looks good. Structural, fire, electrical, accessibility, and occupancy reviews each examine different evidence, and unresolved critical findings stop the opening. Look at **RELEASE CANDIDATE**, **EXCEPTION EXPIRY**, **REQUIRED PASS** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: A release improves evaluation averages, but keyboard approval fails after a streamed error and deletion verification has not reached the vector index.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Produce route-level accessibility, security-header, secret-exposure, authorization, privacy-control, and browser acceptance evidence for the exact build.
- Maintain fixture routes for denied, stale, slow, partial, expired, offline, reduced-motion, and assistive-technology states.
- Render release and exception status only to authorized reviewers, with evidence links and no exposure of sensitive vulnerability details.

Together these choices prevent the mistakes in the Acme case—A release improves evaluation averages, but keyboard approval fails after a streamed error and deletion verification has not reached the vector index.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Generate policy, dependency, secret, tenant, threat, evaluation, workflow, restore, and operational evidence from packaged service artifacts.
- Pin model, prompt, tool, MCP, A2A, AG-UI, policy, dataset, and schema versions in the readiness manifest.
- Enforce gate results in delivery automation while keeping final risk acceptance with the authorized human role.

These boundaries make the Acme case—A release improves evaluation averages, but keyboard approval fails after a streamed error and deletion verification has not reached the vector index.—testable and replaceable.

---

## Case study — A release improves evaluation averages

A release improves evaluation averages, but keyboard approval fails after a streamed error and deletion verification has not reached the vector index.

### The walkthrough

1. The accessibility and privacy gates fail independently of the quality average.
2. Acme blocks release, fixes focus recovery, and extends lineage-driven deletion to the index.
3. Human retesting and deletion evidence are attached to the same release candidate.
4. Only the authorized reviewers mark both gates passed; the decision receipt records remaining limitations.

### The result

A strong model score cannot hide an unusable interface or incomplete privacy control.

### The danger

A broad production-ready label without domain evidence, independent review, and expiring exceptions becomes marketing rather than governance.

### The takeaway

Release only when the exact candidate has the cross-functional evidence its risk requires.

---

## Composition

The picture is a readiness gate. A **RELEASE CANDIDATE** card at the left enters five gate platforms—**THREAT**, **EVALUATION**, **ACCESSIBILITY**, **PRIVACY**, **OPERATIONS**. Each gate has four white cards—**OWNER**, **EVIDENCE**, **PASS**, **FAIL**—and an **EXCEPTION EXPIRY** card. A teal **RELEASE** arrow on the right exits only after **REQUIRED PASS**. Two coral blocked paths—**SELF APPROVAL** and **PERMANENT EXCEPTION**—are stopped. The composition shows release as a cross-functional decision, not a single sign-off.

## Element by element

- **RELEASE CANDIDATE** — Run threat, evaluation, accessibility, privacy, and operational tests on the exact release candidate.
- **EXCEPTION EXPIRY** — Record pass, fail, limitation, residual risk, exception, compensating control, owner, and expiry.
- **REQUIRED PASS** — the safe, verified, or authoritative element marked in teal; in this diagram RELEASE only after REQUIRED PASS.
- **SELF APPROVAL** — the coral anti-pattern of the author certifying their own risk.
- **PERMANENT EXCEPTION** — the coral anti-pattern of leaving a waiver open forever.
- **THREAT** — Threat readiness covers trust boundaries, assets, actors, abuse cases, mitigations, residual risk, attack tests, dependency risk, and incident detection.
- **EVALUATION** — It prevents security, evaluation, accessibility, privacy, or operations from becoming a final checklist nobody can enforce.
- **ACCESSIBILITY** — It prevents security, evaluation, accessibility, privacy, or operations from becoming a final checklist nobody can enforce.
- **PRIVACY** — It prevents security, evaluation, accessibility, privacy, or operations from becoming a final checklist nobody can enforce.
- **OPERATIONS** — It prevents security, evaluation, accessibility, privacy, or operations from becoming a final checklist nobody can enforce.
- **OWNER** — Record pass, fail, limitation, residual risk, exception, compensating control, owner, and expiry.
- **EVIDENCE** — A readiness gate turns an important quality into a decision with required evidence, reviewer, scope, result, exceptions, and expiry.
- **PASS** — Record pass, fail, limitation, residual risk, exception, compensating control, owner, and expiry.
- **FAIL** — Record pass, fail, limitation, residual risk, exception, compensating control, owner, and expiry.
- **RELEASE** — Run threat, evaluation, accessibility, privacy, and operational tests on the exact release candidate.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **RELEASE CANDIDATE**, **EXCEPTION EXPIRY**, **THREAT**, **EVALUATION**, **ACCESSIBILITY**, **PRIVACY** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **RELEASE CANDIDATE**, **EXCEPTION EXPIRY**, **THREAT**, **EVALUATION** carry the forward motion of the architecture.
- **Teal arrow** — an authoritative decision, verified contract, passing gate, safe release, or recovered service. The teal elements **RELEASE**, **REQUIRED PASS** show the path the design wants to keep open.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **SELF APPROVAL**, **PERMANENT EXCEPTION** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **RELEASE CANDIDATE**, **EXCEPTION EXPIRY**, **THREAT**, **EVALUATION**, **ACCESSIBILITY**, **PRIVACY**, **OPERATIONS**, **OWNER** are the readable records the diagram communicates.

---

## How to present it

- Point to **RELEASE CANDIDATE** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **REQUIRED PASS** and ask what would have to change for the team to define required evidence and independent reviewers for each readiness domain, and who would own that change.
- Point to **THREAT** and ask what evidence would show the team has already run threat, evaluation, accessibility, privacy, and operational tests on the exact release candidate, and what test would fail first if it is missing.
- Point to **EXCEPTION EXPIRY** and ask who else in the room must agree before the team can record pass, fail, limitation, residual risk, exception, compensating control, owner, and expiry, and what would change their mind.
- Point to **RELEASE** and ask what the smallest version of block release when an unacceptable outcome or mandatory gate lacks proof looks like, and what would be left out of that version.
- Point to **PERMANENT EXCEPTION** and ask what would have to change for the team to monitor after release and reopen the decision when models, data, tools, users, incidents, or scope change, and who would own that change.
- Trace the **teal** path (RELEASE only after REQUIRED PASS) and ask what evidence would prove the real system follows it, who collects that evidence, and how often it is refreshed.
- Show the **coral** path (SELF APPROVAL and PERMANENT EXCEPTION blocked) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Point to **OWNER** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Use the analogy: A building cannot open because the paint looks good. Structural, fire, electrical, accessibility, and occupancy reviews each examine different evidence, and unresolved critical findings stop the opening. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Create five gate templates with required evidence, owners, reviewers, pass rules, exceptions, compensating controls, expiry, and recheck triggers. Apply them to a synthetic release and write the decision receipt without inventing measured results.
- Pose the checkpoint: *Can a successful automated accessibility scan prove WCAG conformance?*

---

## Lab and checkpoint

**Lab:** Create five gate templates with required evidence, owners, reviewers, pass rules, exceptions, compensating controls, expiry, and recheck triggers. Apply them to a synthetic release and write the decision receipt without inventing measured results.

**Checkpoint:** Can a successful automated accessibility scan prove WCAG conformance?

**Answer:** No. Automated tools cover only part of the requirements; semantic inspection and human testing with real interaction and assistive technologies are also needed.

---

## Glossary

- **Readiness gate** — required evidence decision before release
- **Residual risk** — risk remaining after controls
- **Compensating control** — alternative protection used when a primary control is unavailable

---

## Sources

- NIST AI Risk Management Framework
- OWASP Agentic Applications 2026
- WCAG 2.2
- NIST Generative AI Profile

---

## Related lessons

- **Lesson 223** — Risk classification, human authority, and unacceptable outcomes (`risk-authority-unacceptable-outcomes`)
- **Lesson 224** — Success criteria, exit criteria, and evidence requirements (`success-exit-evidence-contract`)
- **Lesson 238** — Contract, integration, workflow, security, and acceptance tests (`production-test-pyramid`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for Threat, evaluation, accessibility, privacy, and readiness gates until the diagram is legible to every reviewer. Combine cross-functional proof into a transparent go, conditional-go, or no-go decision without letting one team self-certify the whole system. The trace moves through 5 decisions: Define required evidence and independent reviewers for each readiness domain.; Run threat, evaluation, accessibility, privacy, and operational tests on the exact release candidate.; Record pass, fail, limitation, residual risk, exception, compensating control, owner, and expiry.; Block release when an unacceptable outcome or mandatory gate lacks proof.; Monitor after release and reopen the decision when models, data, tools, users, incidents, or scope change.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—A release improves evaluation averages, but keyboard approval fails after a streamed error and deletion verification has not reached the vector index.—shows that Release only when the exact candidate has the cross-functional evidence its risk requires. If the team skips this, A broad production-ready label without domain evidence, independent review, and expiring exceptions becomes marketing rather than governance. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.