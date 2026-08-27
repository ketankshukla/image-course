# Diagram 243 — Portfolio evidence, README, case study, and demonstration plan

![A portfolio evidence chain connects requirement, architecture, contract, code, tests, deployment, and measured results, supported by a README, case study, demo, decisions, threat model, evaluations, and runbooks with scenario and measured evidence clearly separated.](../diagrams/243-portfolio-evidence-story-map.png)

**Module:** Final capstone and project handoff
**Role in the course:** Explain the project as a credible engineering story whose claims can be traced to artifacts, tests, deployments, and honestly measured results.
**Layout:** MEASURED RESULT begins on the left and the diagram flows toward CASE STUDY; a teal **the safe path** path is the desired route and a coral **INFLATED CLAIM** path is blocked or contained.

---

## At a glance

**Portfolio evidence, README, case study, and demonstration plan** — Explain the project as a credible engineering story whose claims can be traced to artifacts, tests, deployments, and honestly measured results.

- The central takeaway is: Make every claim traceable, every demo reproducible, and every limitation visible.
- The visual begins with **MEASURED RESULT** and ends with the diagram's outcome, not a technology name.
- The blocked or dangerous path is marked **coral**: INFLATED CLAIM and SCREENSHOT ONLY blocked.
- The analogy is: A science-fair project is credible when the question, method, materials, observations, failures, and repeatable results are visible. A polished poster with an unsupported percentage is not stronger evidence.

---

## What the diagram teaches

### 1. Portfolio evidence, README, case study, and demonstration plan

It shows visible state, evidence, human authority, committed receipt, and recovery while making clear which providers or effects are synthetic. Until then, the course supplies definitions and evidence plans, not invented success percentages. In the diagram, **CASE STUDY**, **README** appear at the left, turning this idea into something a reviewer can point at.

### 2. Start with the One-sentence User Problem, Constraints, Unacceptable Outcomes

A strong portfolio story begins with the user problem, constraints, and unacceptable outcomes. The visual places **MEASURED RESULT**, **CASE STUDY**, **THREAT MODEL** at the center; the arrows between them are the physical expression of this principle. If this is skipped, a strong portfolio story begins with the user problem, constraints, and unacceptable outcomes.

### 3. Link Requirements to Diagrams, Contracts, Code Locations, Tests, Deployment, and Evidence Manifests.

Evidence artifacts include diagrams, contracts, ADRs, threat model, evaluation plan, accessibility report, conformance results, game-day report, runbooks, release manifest, screenshots, and traces. The trace asks the team to link requirements to diagrams, contracts, code locations, tests, deployment, and evidence manifests. Look at **CODE**, **DEPLOYMENT** on the top: the diagram uses those elements to show where this decision lives.

### 4. Create a Reproducible README and a Case Study That Explains Trade-offs and Failures Honestly.

The case study explains the situation, choices, trade-offs, evidence, setbacks, and outcome. The picture shows **CASE STUDY**, **README** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: She removes the unsupported claim and labels the course scorecard values as illustrative targets.

### 5. Rehearse a Short Happy-path and Failure-path Demonstration Using Synthetic Data and Explicit Boundaries.

It then shows architecture decisions, implementation boundaries, verification, deployment, operations, and learning—not a list of libraries. The README is the reproducible entry point: product overview, architecture, repository map, prerequisites, setup, configuration, synthetic data, commands, tests, deployment, security, privacy, accessibility, limitations, and demonstration script. The demonstration follows one user journey and one failure path. To put this into practice, the team should rehearse a short happy-path and failure-path demonstration using synthetic data and explicit boundaries. At the bottom, **MEASURED RESULT**, **CASE STUDY**, **THREAT MODEL** is the element that makes this concept concrete before any code is written.

### 6. Audit Every Claim as Blueprint, Simulated, Proposed, or Measured and Attach the Supporting Evidence.

It distinguishes blueprint decisions, simulated exercises, proposed targets, and measured production or test results. Claims use measured numbers only when the later project records method, denominator, environment, sample, time window, and limitations. In the diagram, **MEASURED RESULT**, **INFLATED CLAIM**, **MEASURED** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, unsupported metrics, hidden synthetic behavior, or a screenshot-only demo can damage trust when a reviewer asks how the result was measured or reproduced.

### 7. Make every claim traceable, every demo reproducible

Each should have a version and clear purpose. The visual places **INFLATED CLAIM**, **DEMO** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

A science-fair project is credible when the question, method, materials, observations, failures, and repeatable results are visible. A polished poster with an unsupported percentage is not stronger evidence. Look at **MEASURED RESULT**, **CASE STUDY**, **THREAT MODEL** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: Maya prepares a portfolio page that says Acme reduced review time by 60 percent, but the project has not been implemented or measured.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Document routes, server/client boundaries, accessible UI fixtures, local setup, environment variables, browser tests, Vercel preview, and production deployment path.
- Provide a seeded synthetic demo mode that reliably shows progress, approval, expiry, partial success, recovery, and receipts.
- Capture visual evidence together with semantic and test reports so screenshots support rather than replace engineering proof.

Together these choices prevent the mistakes in the Acme case—Maya prepares a portfolio page that says Acme reduced review time by 60 percent, but the project has not been implemented or measured.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Document package boundaries, service and worker commands, migrations, fixtures, protocol adapters, tests, telemetry, deployment, and recovery procedures.
- Ship a deterministic synthetic provider suite so reviewers can run the product without external accounts before optional live integration.
- Export contract, evaluation, security, workflow, and game-day manifests in stable machine-readable and human-readable forms.

These boundaries make the Acme case—Maya prepares a portfolio page that says Acme reduced review time by 60 percent, but the project has not been implemented or measured.—testable and replaceable.
![One enterprise blueprint hands shared contracts, fixtures, user journeys, acceptance, threats, evaluations, operations, and evidence to separate Next.js React and Python FastAPI projects that converge on one Acme demonstration and portfolio proof.](../diagrams/244-dual-project-graduation-handoff.png)

Diagram 244 — *Graduation map and handoff to the two separate coding projects* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

---

## Case study — Maya prepares a portfolio page that says Acme reduced review

Maya prepares a portfolio page that says Acme reduced review time by 60 percent, but the project has not been implemented or measured.

### The walkthrough

1. She removes the unsupported claim and labels the course scorecard values as illustrative targets.
2. The case study instead demonstrates the evidence architecture, conformance suite, threat gates, and planned measurement method.
3. After the later project runs controlled tests, Maya may publish actual results with denominator, environment, versions, and limitations.
4. The demo script clearly distinguishes synthetic refund effects from any real external integration.

### The result

The portfolio remains impressive because it is reproducible and honest, not because it inflates outcomes.

### The danger

Unsupported metrics, hidden synthetic behavior, or a screenshot-only demo can damage trust when a reviewer asks how the result was measured or reproduced.

### The takeaway

Make every claim traceable, every demo reproducible, and every limitation visible.

---

## Composition

The picture is a portfolio evidence chain. From left to right, a path of seven cards—**REQUIREMENT**, **ARCHITECTURE**, **CONTRACT**, **CODE**, **TEST**, **DEPLOYMENT**, **MEASURED RESULT**—runs across the center. Above and below the chain, supporting artifacts—**README**, **CASE STUDY**, **DEMO**, **ADR**, **THREAT MODEL**, **EVAL**, **RUNBOOK**—float. Two labels, **SCENARIO** and **MEASURED**, are attached to separate parts of the chain. Two coral blocked paths—**INFLATED CLAIM** and **SCREENSHOT ONLY**—are stopped. The composition shows a credible story backed by linked evidence.

## Element by element

- **MEASURED RESULT** — a labeled visual element in this diagram; the prompt shows it as REQUIREMENT to ARCHITECTURE to CONTRACT to CODE to TEST to DEPLOYMENT to MEASURED RESULT chain.
- **CASE STUDY** — The case study explains the situation, choices, trade-offs, evidence, setbacks, and outcome.
- **THREAT MODEL** — Evidence artifacts include diagrams, contracts, ADRs, threat model, evaluation plan, accessibility report, conformance results, game-day report, runbooks, release manifest, screenshots, and traces.
- **INFLATED CLAIM** — the coral anti-pattern of presenting an unsupported metric or result.
- **SCREENSHOT ONLY** — the coral anti-pattern of relying on a screenshot as the only evidence.
- **REQUIREMENT** — a labeled visual element in this diagram; the prompt shows it as REQUIREMENT to ARCHITECTURE to CONTRACT to CODE to TEST to DEPLOYMENT to MEASURED RESULT chain.
- **ARCHITECTURE** — It then shows architecture decisions, implementation boundaries, verification, deployment, operations, and learning—not a list of libraries.
- **CONTRACT** — a labeled visual element in this diagram; the prompt shows it as REQUIREMENT to ARCHITECTURE to CONTRACT to CODE to TEST to DEPLOYMENT to MEASURED RESULT chain.
- **CODE** — Link requirements to diagrams, contracts, code locations, tests, deployment, and evidence manifests.
- **TEST** — It distinguishes blueprint decisions, simulated exercises, proposed targets, and measured production or test results.
- **DEPLOYMENT** — It then shows architecture decisions, implementation boundaries, verification, deployment, operations, and learning—not a list of libraries.
- **README** — The README is the reproducible entry point: product overview, architecture, repository map, prerequisites, setup, configuration, synthetic data, commands, tests, deployment, security, privacy, accessibility, limitations, and demonstration script.
- **DEMO** — Make every claim traceable, every demo reproducible, and every limitation visible.
- **ADR** — the ADR card shown in this diagram; it is one of the labeled elements the architecture uses.
- **EVAL** — the EVAL card shown in this diagram; it is one of the labeled elements the architecture uses.
- **RUNBOOK** — the RUNBOOK card shown in this diagram; it is one of the labeled elements the architecture uses.
- **SCENARIO** — a label that separates exercise, simulated, or proposed evidence from measured results in the portfolio.
- **MEASURED** — It distinguishes blueprint decisions, simulated exercises, proposed targets, and measured production or test results.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **MEASURED RESULT**, **CASE STUDY**, **THREAT MODEL**, **REQUIREMENT**, **ARCHITECTURE**, **CONTRACT** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **TEST**, **DEPLOYMENT** carry the forward motion of the architecture.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **INFLATED CLAIM**, **SCREENSHOT ONLY** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **CASE STUDY**, **REQUIREMENT**, **CONTRACT**, **TEST** are the readable records the diagram communicates.

---

## How to present it

- Point to **MEASURED RESULT** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **ARCHITECTURE** and ask what would have to change for the team to write the one-sentence user problem, constraints, unacceptable outcomes, and why the selected architecture fits, and who would own that change.
- Point to **CODE** and ask what evidence would show the team has already link requirements to diagrams, contracts, code locations, tests, deployment, and evidence manifests, and what test would fail first if it is missing.
- Point to **CASE STUDY** and ask who else in the room must agree before the team can create a reproducible README and a case study that explains trade-offs and failures honestly, and what would change their mind.
- Point to **THREAT MODEL** and ask what the smallest version of rehearse a short happy-path and failure-path demonstration using synthetic data and explicit boundaries looks like, and what would be left out of that version.
- Point to **INFLATED CLAIM** and ask what would have to change for the team to audit every claim as blueprint, simulated, proposed, or measured and attach the supporting evidence, and who would own that change.
- Show the **coral** path (INFLATED CLAIM and SCREENSHOT ONLY blocked) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Use the analogy: A science-fair project is credible when the question, method, materials, observations, failures, and repeatable results are visible. A polished poster with an unsupported percentage is not stronger evidence. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Draft the README outline, case-study outline, evidence index, ten-minute demo script, five-minute failure demo, setup checklist, claim audit, and a measurement template that forbids presenting illustrative targets as results.
- Pose the checkpoint: *May the blueprint's sample target be rewritten as a portfolio achievement?*

---

## Lab and checkpoint

**Lab:** Draft the README outline, case-study outline, evidence index, ten-minute demo script, five-minute failure demo, setup checklist, claim audit, and a measurement template that forbids presenting illustrative targets as results.

**Checkpoint:** May the blueprint's sample target be rewritten as a portfolio achievement?

**Answer:** No. Publish it as a proposed target or scenario until the implemented project measures and documents the actual result.

---

## Glossary

- **Reproducibility** — another person can follow the method and observe comparable behavior
- **Claim audit** — check that every statement has appropriate evidence
- **Demo mode** — controlled environment for showing product behavior

---

## Sources

- SLSA specification
- OpenSSF Scorecard
- GitHub Actions documentation
- OpenTelemetry semantic conventions 1.44.0

---

## Related lessons

- **Lesson 224** — Success criteria, exit criteria, and evidence requirements (`success-exit-evidence-contract`)
- **Lesson 241** — Architecture review and trade-off defense (`architecture-review-tradeoff-defense`)
- **Lesson 244** — Graduation map and handoff to the two separate coding projects (`dual-project-graduation-handoff`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for Portfolio evidence, README, case study, and demonstration plan until the diagram is legible to every reviewer. Explain the project as a credible engineering story whose claims can be traced to artifacts, tests, deployments, and honestly measured results. The trace moves through 5 decisions: Write the one-sentence user problem, constraints, unacceptable outcomes, and why the selected architecture fits.; Link requirements to diagrams, contracts, code locations, tests, deployment, and evidence manifests.; Create a reproducible README and a case study that explains trade-offs and failures honestly.; Rehearse a short happy-path and failure-path demonstration using synthetic data and explicit boundaries.; Audit every claim as blueprint, simulated, proposed, or measured and attach the supporting evidence.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—Maya prepares a portfolio page that says Acme reduced review time by 60 percent, but the project has not been implemented or measured.—shows that Make every claim traceable, every demo reproducible, and every limitation visible. If the team skips this, Unsupported metrics, hidden synthetic behavior, or a screenshot-only demo can damage trust when a reviewer asks how the result was measured or reproduced. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.