# Diagram 229 — Shared schemas, contracts, fixtures, and conformance cases

![A shared contract kit of schemas, APIs, events, examples, fixtures, errors, and version rules feeds TypeScript and Pydantic implementations, which must pass the same conformance runner.](../diagrams/229-shared-contract-conformance-kit.png)

**Module:** Dual-stack implementation blueprint
**Role in the course:** Create one framework-neutral behavior contract that both future stacks can implement and test without sharing application code.
**Layout:** CONTRACT KIT begins on the left and the diagram flows toward JSON SCHEMA; a teal **the safe path** path is the desired route and a coral **HANDWRITTEN DRIFT** path is blocked or contained.

---

## At a glance

**Shared schemas, contracts, fixtures, and conformance cases** — Create one framework-neutral behavior contract that both future stacks can implement and test without sharing application code.

- The central takeaway is: Share the contract, examples, and observable tests—not the accidental internals of either stack.
- The visual begins with **CONTRACT KIT** and ends with the diagram's outcome, not a technology name.
- The blocked or dangerous path is marked **coral**: HANDWRITTEN DRIFT is blocked.
- The analogy is: Two factories can use different machines to build the same plug. A shared drawing and gauge prove that every plug fits the socket; copying one factory's internal machine design would not be necessary.

---

## What the diagram teaches

### 1. Shared schemas, contracts, fixtures, and conformance cases

TypeScript and Pydantic types may be generated or handwritten, but the canonical contract and fixtures remain independent. In the diagram, **ERROR CASES**, **CONFORMANCE RUNNER**, **FIXTURES** appear at the left, turning this idea into something a reviewer can point at.

### 2. Inventory Commands, Queries, Events, Artifacts, Proposals, Decisions, Errors, and Receipts Shared by Both Stacks.

Consumer tests prevent a producer from breaking a real caller without noticing. Both projects may have different modules and libraries while still producing the same state transitions, errors, receipts, and user-visible outcomes. The visual places **CONTRACT KIT**, **JSON SCHEMA**, **ERROR CASES** at the center; the arrows between them are the physical expression of this principle. If this is skipped, consumer tests prevent a producer from breaking a real caller without noticing.

### 3. Start with Canonical Schemas Plus Semantic Rules for Identity, Authority, Ordering, Idempotency, Privacy

JSON Schema can describe payloads, OpenAPI can describe HTTP operations, and AsyncAPI can describe event channels, but examples, error semantics, authorization, ordering, and invariants still need explicit documentation and tests. Generated code does not prove business rules, and handwritten models must not silently reinterpret the schema. The trace asks the team to write canonical schemas plus semantic rules for identity, authority, ordering, idempotency, privacy, and versions. Look at **VERSION RULES** on the top: the diagram uses those elements to show where this decision lives.

### 4. Create Valid Examples and Adversarial Fixtures, Including Unknown and Stale Cases.

Conformance cases include happy paths, invalid values, duplicates, stale revisions, timeouts, denied authority, unknown versions, partial completion, and recovery. The picture shows **ERROR CASES**, **EXAMPLES**, **FIXTURES** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: The canonical schema identifies the wire name and forbids a missing evidence revision for a consequential proposal.

### 5. Run the Same Black-box Conformance Suite Against Typescript and Python Adapters.

A fixture is a stable example input, event sequence, or response. The conformance runner compares observable behavior, not internal architecture. To put this into practice, the team should run the same black-box conformance suite against TypeScript and Python adapters. At the bottom, **CONFORMANCE RUNNER**, **TYPESCRIPT** is the element that makes this concept concrete before any code is written.

### 6. Publish Compatibility Reports and Require Explicit Review for Every Contract Change.

Schema compatibility is more than whether JSON parses. The contract includes required and optional fields, nullability, defaults, unknown-field behavior, identifiers, timestamps, money, pagination, version negotiation, size limits, and privacy classification. Compatibility rules say which additions are safe, when a new major version is required, how old clients fail, and how adapters translate external protocol versions. In the diagram, **CONTRACT KIT** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, compatibility rules say which additions are safe, when a new major version is required, how old clients fail, and how adapters translate external protocol versions.

### 7. Share the contract, examples

A shared contract describes messages and behavior that must agree across stacks. The visual places **CONTRACT KIT**, **EXAMPLES** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

Two factories can use different machines to build the same plug. A shared drawing and gauge prove that every plug fits the socket; copying one factory's internal machine design would not be necessary. Look at **CONTRACT KIT**, **JSON SCHEMA**, **ERROR CASES** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: The Next.js project calls a field approvalId while the Python service changes it to decision_id and begins accepting an empty evidence version.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Generate or validate TypeScript types at the server boundary, then map them to narrower product state rather than passing raw protocol objects through the component tree.
- Keep canonical fixtures in a shared contract package and replay them through route handlers, reducers, and accessible UI states.
- Fail builds when generated types are stale, schemas change without review, or a consumer fixture produces a different error or receipt.

Together these choices prevent the mistakes in the Acme case—The Next.js project calls a field approvalId while the Python service changes it to decision_id and begins accepting an empty evidence version.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Validate canonical schemas with Pydantic adapters and keep domain models separate when business semantics are stronger than transport shapes.
- Parameterize the same fixture set across API, event, policy, and workflow tests, including timezone and decimal edge cases.
- Export an implementation compatibility report that records contract version, test commit, environment, and exact failed cases.
![One user journey crosses Next.js, a typed API, FastAPI, workflow adapters, protocols, and a business system under a shared trace, with mock, contract, integration, end-to-end, and failure tests.](../diagrams/232-cross-stack-adapter-test-loop.png)

Diagram 232 — *Cross-stack integration, adapters, and end-to-end tests* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

These boundaries make the Acme case—The Next.js project calls a field approvalId while the Python service changes it to decision_id and begins accepting an empty evidence version.—testable and replaceable.

---

## Case study — The Next.js project calls a field approvalId

The Next.js project calls a field approvalId while the Python service changes it to decision_id and begins accepting an empty evidence version.

### The walkthrough

1. The canonical schema identifies the wire name and forbids a missing evidence revision for a consequential proposal.
2. Both stacks regenerate or update adapters, while their internal naming remains local.
3. A stale-approval fixture is run against each implementation and must return the same safe problem response.
4. The compatibility report records the contract change and prevents deployment until both consumers pass.

### The result

The two projects evolve independently without drifting on the behavior users and services rely upon.

### The danger

Sharing copied interface files without a canonical schema and behavior suite creates the appearance of type safety while semantics quietly diverge.

### The takeaway

Share the contract, examples, and observable tests—not the accidental internals of either stack.

---

## Composition

The picture is a contract kit at the center. A **CONTRACT KIT** card holds seven white cards—**JSON SCHEMA**, **OPENAPI**, **ASYNCAPI**, **EXAMPLES**, **FIXTURES**, **ERROR CASES**, **VERSION RULES**. Cyan arrows feed a **TYPESCRIPT** implementation on the left and a **PYDANTIC** implementation on the right. Both enter a **CONFORMANCE RUNNER** and produce a **SAME BEHAVIOR** card at the bottom. A coral **HANDWRITTEN DRIFT** arrow is blocked. The composition shows the contract as the source of truth for both stacks.

## Element by element

- **CONTRACT KIT** — a labeled visual element in this diagram; the prompt shows it as CONTRACT KIT at center with JSON SCHEMA.
- **JSON SCHEMA** — JSON Schema can describe payloads, OpenAPI can describe HTTP operations, and AsyncAPI can describe event channels, but examples, error semantics, authorization, ordering, and invariants still need explicit documentation and tests.
- **ERROR CASES** — the ERROR CASES card shown in this diagram; it is one of the labeled elements the architecture uses.
- **VERSION RULES** — Compatibility rules say which additions are safe, when a new major version is required, how old clients fail, and how adapters translate external protocol versions.
- **CONFORMANCE RUNNER** — The conformance runner compares observable behavior, not internal architecture.
- **SAME BEHAVIOR** — A shared contract describes messages and behavior that must agree across stacks.
- **HANDWRITTEN DRIFT** — the coral divergence when hand-coded types silently reinterpret the canonical contract.
- **OPENAPI** — JSON Schema can describe payloads, OpenAPI can describe HTTP operations, and AsyncAPI can describe event channels, but examples, error semantics, authorization, ordering, and invariants still need explicit documentation and tests.
- **ASYNCAPI** — JSON Schema can describe payloads, OpenAPI can describe HTTP operations, and AsyncAPI can describe event channels, but examples, error semantics, authorization, ordering, and invariants still need explicit documentation and tests.
- **EXAMPLES** — JSON Schema can describe payloads, OpenAPI can describe HTTP operations, and AsyncAPI can describe event channels, but examples, error semantics, authorization, ordering, and invariants still need explicit documentation and tests.
- **FIXTURES** — TypeScript and Pydantic types may be generated or handwritten, but the canonical contract and fixtures remain independent.
- **TYPESCRIPT** — TypeScript and Pydantic types may be generated or handwritten, but the canonical contract and fixtures remain independent.
- **PYDANTIC** — TypeScript and Pydantic types may be generated or handwritten, but the canonical contract and fixtures remain independent.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **CONTRACT KIT**, **JSON SCHEMA**, **ERROR CASES**, **VERSION RULES**, **CONFORMANCE RUNNER**, **SAME BEHAVIOR** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **CONTRACT KIT**, **JSON SCHEMA**, **ERROR CASES**, **VERSION RULES** carry the forward motion of the architecture.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **HANDWRITTEN DRIFT** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **CONTRACT KIT**, **JSON SCHEMA**, **ERROR CASES**, **VERSION RULES**, **FIXTURES** are the readable records the diagram communicates.

---

## How to present it

- Point to **CONTRACT KIT** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **JSON SCHEMA** and ask what would have to change for the team to inventory commands, queries, events, artifacts, proposals, decisions, errors, and receipts shared by both stacks, and who would own that change.
- Point to **VERSION RULES** and ask what evidence would show the team has already write canonical schemas plus semantic rules for identity, authority, ordering, idempotency, privacy, and versions, and what test would fail first if it is missing.
- Point to **ERROR CASES** and ask who else in the room must agree before the team can create valid examples and adversarial fixtures, including unknown and stale cases, and what would change their mind.
- Point to **CONFORMANCE RUNNER** and ask what the smallest version of run the same black-box conformance suite against TypeScript and Python adapters looks like, and what would be left out of that version.
- Point to **CONFORMANCE RUNNER** and ask what would have to change for the team to publish compatibility reports and require explicit review for every contract change, and who would own that change.
- Show the **coral** path (HANDWRITTEN DRIFT is blocked) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Use the analogy: Two factories can use different machines to build the same plug. A shared drawing and gauge prove that every plug fits the socket; copying one factory's internal machine design would not be necessary. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Design a contract kit for task creation, progress event, evidence item, proposal, decision, receipt, and problem response. Add schemas, examples, twenty invalid fixtures, version rules, consumer matrix, and a conformance-run report format.
- Pose the checkpoint: *If both stacks accept the same JSON, are they conformant?*

---

## Lab and checkpoint

**Lab:** Design a contract kit for task creation, progress event, evidence item, proposal, decision, receipt, and problem response. Add schemas, examples, twenty invalid fixtures, version rules, consumer matrix, and a conformance-run report format.

**Checkpoint:** If both stacks accept the same JSON, are they conformant?

**Answer:** Not necessarily. They must also agree on validation, authority, state transitions, errors, ordering, idempotency, and observable outcomes.

---

## Glossary

- **Conformance** — demonstrated agreement with a defined contract
- **Consumer test** — test of what a caller depends on
- **Compatibility** — ability of versions to interoperate safely

---

## Sources

- JSON Schema 2020-12
- OpenAPI 3.1.1 specification
- AsyncAPI 3.0.0 specification
- Pydantic models

---

## Related lessons

- **Lesson 227** — MCP, A2A, AG-UI, HTTP, queue, and internal boundaries (`protocol-boundary-routing-map`)
- **Lesson 232** — Cross-stack integration, adapters, and end-to-end tests (`cross-stack-adapter-test-loop`)
- **Lesson 238** — Contract, integration, workflow, security, and acceptance tests (`production-test-pyramid`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for Shared schemas, contracts, fixtures, and conformance cases until the diagram is legible to every reviewer. Create one framework-neutral behavior contract that both future stacks can implement and test without sharing application code. The trace moves through 5 decisions: Inventory commands, queries, events, artifacts, proposals, decisions, errors, and receipts shared by both stacks.; Write canonical schemas plus semantic rules for identity, authority, ordering, idempotency, privacy, and versions.; Create valid examples and adversarial fixtures, including unknown and stale cases.; Run the same black-box conformance suite against TypeScript and Python adapters.; Publish compatibility reports and require explicit review for every contract change.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—The Next.js project calls a field approvalId while the Python service changes it to decision_id and begins accepting an empty evidence version.—shows that Share the contract, examples, and observable tests—not the accidental internals of either stack. If the team skips this, Sharing copied interface files without a canonical schema and behavior suite creates the appearance of type safety while semantics quietly diverge. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.