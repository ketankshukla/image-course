# Diagram 241 — Architecture review and trade-off defense

![An architecture review compares options using requirements, value, risk, cost, complexity, reversibility, operations, and evidence, then records a decision, consequences, actions, and an architecture decision record.](../diagrams/241-architecture-review-tradeoff-defense.png)

**Module:** Final capstone and project handoff
**Role in the course:** Present and defend the blueprint as a set of evidence-based trade-offs rather than a collection of boxes or fashionable technologies.
**Layout:** ARCHITECTURE REVIEW BOARD begins on the left and the diagram flows toward DIAGRAM BY AUTHORITY; a teal **the safe path** path is the desired route and a coral **DIAGRAM BY AUTHORITY** path is blocked or contained.

---

## At a glance

**Architecture review and trade-off defense** — Present and defend the blueprint as a set of evidence-based trade-offs rather than a collection of boxes or fashionable technologies.

- The central takeaway is: Defend requirements and trade-offs, not brands or boxes.
- The visual begins with **ARCHITECTURE REVIEW BOARD** and ends with the diagram's outcome, not a technology name.
- The blocked or dangerous path is marked **coral**: DIAGRAM BY AUTHORITY and NO ALTERNATIVE blocked.
- The analogy is: A building review asks whether the design supports its occupants, site, loads, fire safety, accessibility, maintenance, and budget. A beautiful floor plan cannot answer every engineering question.

---

## What the diagram teaches

### 1. Architecture review and trade-off defense

An architecture review asks whether the design satisfies named requirements under known constraints. In the diagram, **ARCHITECTURE REVIEW BOARD** appear at the left, turning this idea into something a reviewer can point at.

### 2. Start with the User Problem, Requirements, Unacceptable Outcomes, and Quality Priorities.

The review pack contains context, user journey, requirements, unacceptable outcomes, quality attributes, diagrams, contracts, data map, threat model, evidence plan, deployment topology, delivery plan, and unresolved questions. The visual places **REQUIREMENTS** at the center; the arrows between them are the physical expression of this principle. If this is skipped, the review pack contains context, user journey, requirements, unacceptable outcomes, quality attributes, diagrams, contracts, data map, threat model, evidence plan, deployment topology, delivery plan, and unresolved questions.
![A portfolio evidence chain connects requirement, architecture, contract, code, tests, deployment, and measured results, supported by a README, case study, demo, decisions, threat model, evaluations, and runbooks with scenario and measured evidence clearly separated.](../diagrams/243-portfolio-evidence-story-map.png)

Diagram 243 — *Portfolio evidence, README, case study, and demonstration plan* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 3. Walk the End-to-end Journey Across Authority, Data, Protocol, Deployment, Failure, and Recovery Boundaries.

It examines boundaries, data, authority, protocols, failure, operations, delivery, and evidence—not visual neatness alone. The trace asks the team to walk the end-to-end journey across authority, data, protocol, deployment, failure, and recovery boundaries. Look at **DIAGRAM BY AUTHORITY** on the top: the diagram uses those elements to show where this decision lives.

### 4. Compare Credible Options with Evidence, Assumptions, Consequences, Reversibility, and Operating Cost.

For consequential choices, compare at least two credible alternatives, including the simpler non-agent option. State assumptions, evidence, rejected reasons, reversibility, migration path, and what would cause reconsideration. The picture shows **OPTIONS**, **CONSEQUENCES**, **EVIDENCE** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: Maya returns to the relationship map: peer-agent tasks use A2A, declared tools and context use MCP, and product contracts meet at adapters.

### 5. Record Decisions, Objections, Risks, Actions, Owners, Due Dates, and Recheck Triggers.

For example, a queue improves durability and burst handling but adds eventual consistency, operational ownership, and reconciliation work. An architecture decision record captures the decision, status, context, options, consequences, owners, date, and superseding record. To put this into practice, the team should record decisions, objections, risks, actions, owners, due dates, and recheck triggers. At the bottom, **ACTIONS** is the element that makes this concept concrete before any code is written.

### 6. Update Diagrams, Contracts, Backlog, Tests, and Evidence So the Review Decision Becomes Executable.

It is concise evidence, not a transcript of private reasoning. Review quality comes from challenge and traceability. Every concern becomes an accepted explanation, a design change, a risk acceptance by the authorized owner, an experiment, or an owned follow-up—not a forgotten meeting comment. In the diagram, **ARCHITECTURE REVIEW BOARD**, **DECISION**, **EVIDENCE** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, every concern becomes an accepted explanation, a design change, a risk acceptance by the authorized owner, an experiment, or an owned follow-up—not a forgotten meeting comment.

### 7. Defend requirements and trade-offs, not brands or boxes

A trade-off means an option improves some qualities while costing others. The visual places **REQUIREMENTS** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

A building review asks whether the design supports its occupants, site, loads, fire safety, accessibility, maintenance, and budget. A beautiful floor plan cannot answer every engineering question. Look at **ARCHITECTURE REVIEW BOARD**, **DIAGRAM BY AUTHORITY**, **NO ALTERNATIVE** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: A reviewer asks why Acme needs both A2A and MCP, why Python is separate from Next.js, and why a queue is worth the added complexity.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Demonstrate the web boundary with route maps, component states, data minimization, accessibility fixtures, error recovery, and Vercel topology evidence.
- Show why each client island exists and which simpler server-first path was selected elsewhere.
- Link review actions to concrete routes, components, contracts, tests, release gates, and owners.

Together these choices prevent the mistakes in the Acme case—A reviewer asks why Acme needs both A2A and MCP, why Python is separate from Next.js, and why a queue is worth the added complexity.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Demonstrate domain boundaries, ports, durable work, data authority, policy enforcement, protocol adapters, idempotency, and operational failure paths.
- Compare synchronous and queued designs, direct providers and adapters, storage options, and deployment choices using workload and recovery evidence.
- Keep architecture decision records beside code and require superseding decisions when assumptions change.

These boundaries make the Acme case—A reviewer asks why Acme needs both A2A and MCP, why Python is separate from Next.js, and why a queue is worth the added complexity.—testable and replaceable.

---

## Case study — A reviewer asks why Acme needs both A2A and MCP

A reviewer asks why Acme needs both A2A and MCP, why Python is separate from Next.js, and why a queue is worth the added complexity.

### The walkthrough

1. Maya returns to the relationship map: peer-agent tasks use A2A, declared tools and context use MCP, and product contracts meet at adapters.
2. The separate Python service owns durable coordination and policy, while Next.js owns the web experience and Vercel deployment lifecycle.
3. The queue is justified only for work that must survive the interactive request; simple commands remain synchronous.
4. The ADRs record alternatives, costs, recovery evidence, and conditions under which the choices should be simplified later.

### The result

The blueprint is defensible because every technology choice answers a named requirement and admits its cost.

### The danger

Architecture by slogan uses protocol names as justification and makes it impossible to tell what can be removed, replaced, or safely simplified.

### The takeaway

Defend requirements and trade-offs, not brands or boxes.

---

## Composition

The picture is an architecture review board. At the center, an **ARCHITECTURE REVIEW BOARD** ring encloses six white cards—**CONTEXT**, **REQUIREMENTS**, **OPTIONS**, **DECISION**, **CONSEQUENCES**, **EVIDENCE**. Two **OPTION** cards on the left are compared across six attribute cards—**VALUE**, **RISK**, **COST**, **COMPLEXITY**, **REVERSIBILITY**, **OPERATIONS**. On the right, output cards—**ADR** and **ACTIONS**—leave the board. Two coral blocked paths—**DIAGRAM BY AUTHORITY** and **NO ALTERNATIVE**—are stopped. The composition shows a review as an evidence-based comparison.

## Element by element

- **ARCHITECTURE REVIEW BOARD** — a labeled visual element in this diagram; the prompt shows it as ARCHITECTURE REVIEW BOARD around CONTEXT.
- **DIAGRAM BY AUTHORITY** — the coral anti-pattern of approving a picture instead of a defensible design.
- **NO ALTERNATIVE** — the coral anti-pattern of presenting only one option.
- **CONTEXT** — The review pack contains context, user journey, requirements, unacceptable outcomes, quality attributes, diagrams, contracts, data map, threat model, evidence plan, deployment topology, delivery plan, and unresolved questions.
- **REQUIREMENTS** — An architecture review asks whether the design satisfies named requirements under known constraints.
- **OPTIONS** — An architecture decision record captures the decision, status, context, options, consequences, owners, date, and superseding record.
- **DECISION** — An architecture decision record captures the decision, status, context, options, consequences, owners, date, and superseding record.
- **CONSEQUENCES** — An architecture decision record captures the decision, status, context, options, consequences, owners, date, and superseding record.
- **EVIDENCE** — It examines boundaries, data, authority, protocols, failure, operations, delivery, and evidence—not visual neatness alone.
- **OPTION** — A trade-off means an option improves some qualities while costing others.
- **VALUE** — a labeled visual element in this diagram; the prompt shows it as Compare two OPTION cards on VALUE.
- **RISK** — Every concern becomes an accepted explanation, a design change, a risk acceptance by the authorized owner, an experiment, or an owned follow-up—not a forgotten meeting comment.
- **COST** — Compare credible options with evidence, assumptions, consequences, reversibility, and operating cost.
- **COMPLEXITY** — A reviewer asks why Acme needs both A2A and MCP, why Python is separate from Next.js, and why a queue is worth the added complexity.
- **REVERSIBILITY** — State assumptions, evidence, rejected reasons, reversibility, migration path, and what would cause reconsideration.
- **OPERATIONS** — It examines boundaries, data, authority, protocols, failure, operations, delivery, and evidence—not visual neatness alone.
- **ADR** — architecture decision record.
- **ACTIONS** — Record decisions, objections, risks, actions, owners, due dates, and recheck triggers.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **ARCHITECTURE REVIEW BOARD**, **CONTEXT**, **REQUIREMENTS**, **OPTIONS**, **DECISION**, **CONSEQUENCES** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **ARCHITECTURE REVIEW BOARD**, **CONTEXT**, **REQUIREMENTS**, **OPTIONS** carry the forward motion of the architecture.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **DIAGRAM BY AUTHORITY**, **NO ALTERNATIVE** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **REQUIREMENTS**, **OPTIONS**, **DECISION**, **EVIDENCE**, **OPTION** are the readable records the diagram communicates.

---

## How to present it

- Point to **ARCHITECTURE REVIEW BOARD** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **REQUIREMENTS** and ask what would have to change for the team to start with the user problem, requirements, unacceptable outcomes, and quality priorities, and who would own that change.
- Point to **DIAGRAM BY AUTHORITY** and ask what evidence would show the team has already walk the end-to-end journey across authority, data, protocol, deployment, failure, and recovery boundaries, and what test would fail first if it is missing.
- Point to **OPTIONS** and ask who else in the room must agree before the team can compare credible options with evidence, assumptions, consequences, reversibility, and operating cost, and what would change their mind.
- Point to **ACTIONS** and ask what the smallest version of record decisions, objections, risks, actions, owners, due dates, and recheck triggers looks like, and what would be left out of that version.
- Point to **DECISION** and ask what would have to change for the team to update diagrams, contracts, backlog, tests, and evidence so the review decision becomes executable, and who would own that change.
- Show the **coral** path (DIAGRAM BY AUTHORITY and NO ALTERNATIVE blocked) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Point to **DIAGRAM BY AUTHORITY** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Use the analogy: A building review asks whether the design supports its occupants, site, loads, fire safety, accessibility, maintenance, and budget. A beautiful floor plan cannot answer every engineering question. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Prepare a thirty-minute architecture review pack and ten ADRs. Include context, journey, alternatives, constraints, decisions, consequences, evidence, open risks, owners, and recheck triggers. Rehearse answers to twenty skeptical questions.
- Pose the checkpoint: *Is choosing a more flexible architecture always better?*

---

## Lab and checkpoint

**Lab:** Prepare a thirty-minute architecture review pack and ten ADRs. Include context, journey, alternatives, constraints, decisions, consequences, evidence, open risks, owners, and recheck triggers. Rehearse answers to twenty skeptical questions.

**Checkpoint:** Is choosing a more flexible architecture always better?

**Answer:** No. Flexibility adds complexity and operating cost. Choose only the flexibility supported by current requirements and credible change scenarios.

---

## Glossary

- **Trade-off** — gain in one quality with a cost in another
- **ADR** — architecture decision record
- **Quality attribute** — property such as reliability, security, usability, or maintainability

---

## Sources

- NIST AI Risk Management Framework
- MCP 2026-07-28 specification
- A2A 1.0 specification
- AG-UI architecture

---

## Related lessons

- **Lesson 225** — Capability, context, model, tool, and authority boundaries (`enterprise-boundary-stack`)
- **Lesson 228** — Deployment topology, failure domains, and ownership (`deployment-topology-failure-domains`)
- **Lesson 243** — Portfolio evidence, README, case study, and demonstration plan (`portfolio-evidence-story-map`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for Architecture review and trade-off defense until the diagram is legible to every reviewer. Present and defend the blueprint as a set of evidence-based trade-offs rather than a collection of boxes or fashionable technologies. The trace moves through 5 decisions: Start with the user problem, requirements, unacceptable outcomes, and quality priorities.; Walk the end-to-end journey across authority, data, protocol, deployment, failure, and recovery boundaries.; Compare credible options with evidence, assumptions, consequences, reversibility, and operating cost.; Record decisions, objections, risks, actions, owners, due dates, and recheck triggers.; Update diagrams, contracts, backlog, tests, and evidence so the review decision becomes executable.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—A reviewer asks why Acme needs both A2A and MCP, why Python is separate from Next.js, and why a queue is worth the added complexity.—shows that Defend requirements and trade-offs, not brands or boxes. If the team skips this, Architecture by slogan uses protocol names as justification and makes it impossible to tell what can be removed, replaced, or safely simplified. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.