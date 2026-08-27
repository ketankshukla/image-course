# Diagram 231 — Python and FastAPI responsibility map

![A Python service separates API routers, domain core, policy, orchestration, MCP, A2A and AG-UI adapters, repositories, workers, and audit under Pydantic boundary contracts.](../diagrams/231-python-fastapi-responsibility-map.png)

**Module:** Dual-stack implementation blueprint
**Role in the course:** Assign the future Python and FastAPI project clear domain, orchestration, policy, persistence, and protocol responsibilities.
**Layout:** PYTHON SERVICE begins on the left and the diagram flows toward API ROUTERS; a teal **the safe path** path is the desired route and a coral **FAT ROUTE** path is blocked or contained.

---

## At a glance

**Python and FastAPI responsibility map** — Assign the future Python and FastAPI project clear domain, orchestration, policy, persistence, and protocol responsibilities.

- The central takeaway is: Keep FastAPI at the edge, business rules in the core, and protocols behind adapters.
- The visual begins with **PYTHON SERVICE** and ends with the diagram's outcome, not a technology name.
- The blocked or dangerous path is marked **coral**: FAT ROUTE and MODEL DIRECT TO DB are blocked.
- The analogy is: A restaurant's waiter accepts an order, the kitchen applies recipes and safety rules, suppliers provide ingredients, and accounting records payment. The waiter should not become the recipe, supplier, and bank at the same time.

---

## What the diagram teaches

### 1. Python and FastAPI responsibility map

Background work needs a durable boundary when it must survive process restarts or exceed an interactive request. In the diagram, **PYTHON SERVICE** appear at the left, turning this idea into something a reviewer can point at.

### 2. Organize Routers Around Product Capabilities Rather Than Provider or Protocol Names.

External protocols enter through versioned adapters that produce product commands and events. The visual places **API ROUTERS** at the center; the arrows between them are the physical expression of this principle. If this is skipped, a large asynchronous route can look concise while hiding business authority, unbounded retries, leaked provider errors, and untestable side effects.

### 3. Define Application Use Cases and Domain Invariants Independently from Transport and Persistence.

Routers accept validated transport input, resolve identity and dependencies, call application use cases, and translate results into stable responses. The trace asks the team to define application use cases and domain invariants independently from transport and persistence. Look at **DOMAIN CORE** on the top: the diagram uses those elements to show where this decision lives.

### 4. Place Model, MCP, A2A, AG-UI, Policy, Identity, and Storage Behind Explicit Ports and Adapters.

It should remain understandable without knowing MCP, A2A, AG-UI, a model provider, or a database driver. Pydantic validates shapes at boundaries, but business authorization and invariants still require explicit code. The picture shows **MODEL DIRECT TO DB**, **POLICY** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: Maya separates the refund-review use case from transport and defines its domain inputs, decisions, and results.

### 5. Choose Synchronous, Durable Worker, and Compensation Paths from Effect and Recovery Needs.

The orchestration layer coordinates retrieval, peer agents, tools, durable tasks, timeouts, compensation, and progress. Transactions protect local invariants, while idempotency and sagas or compensations handle effects across services. A lightweight in-process background helper is not a substitute for a durable queue and worker when loss matters. To put this into practice, the team should choose synchronous, durable worker, and compensation paths from effect and recovery needs. At the bottom, **WORKERS** is the element that makes this concept concrete before any code is written.

### 6. Test Domain Rules, Adapter Conformance, Repositories, Workflow Replay, Security, and API Acceptance Separately.

Repositories isolate operational state, evidence, artifacts, memory, audit, and authoritative integrations. Tests must prove that a well-formed malicious request cannot cross tenant or authority boundaries. In the diagram, **API ROUTERS**, **DOMAIN CORE**, **MCP ADAPTER** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, a large asynchronous route can look concise while hiding business authority, unbounded retries, leaked provider errors, and untestable side effects.

### 7. Keep FastAPI at the edge, business rules in the core

FastAPI is the service entry layer, not the entire architecture. The domain core owns business language and invariants such as evidence freshness, proposal binding, human authority, refund limits, and receipt semantics. The visual places **DOMAIN CORE** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

A restaurant's waiter accepts an order, the kitchen applies recipes and safety rules, suppliers provide ingredients, and accounting records payment. The waiter should not become the recipe, supplier, and bank at the same time. Look at **PYTHON SERVICE**, **API ROUTERS**, **DOMAIN CORE** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: Acme's first FastAPI route validates input, calls the model, queries the database, invokes a refund tool, and formats AG-UI events in one function.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Consume a stable service contract and durable handles instead of depending on Python module layout or worker implementation.
- Render typed domain states and problem details; keep provider stack traces and privileged audit information on the service side.
- Use synthetic API and event fixtures so the web project can proceed while service adapters are still under construction.

Together these choices prevent the mistakes in the Acme case—Acme's first FastAPI route validates input, calls the model, queries the database, invokes a refund tool, and formats AG-UI events in one function.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Create packages for api, application, domain, ports, adapters, workers, persistence, policy, telemetry, and tests with a documented dependency direction.
- Use dependency injection at composition roots, not hidden global clients, so provider, clock, identity, and repository behavior can be replaced in tests.
- Make every effectful use case return an explicit domain result or receipt and record idempotency before retrying external work.
![One user journey crosses Next.js, a typed API, FastAPI, workflow adapters, protocols, and a business system under a shared trace, with mock, contract, integration, end-to-end, and failure tests.](../diagrams/232-cross-stack-adapter-test-loop.png)

Diagram 232 — *Cross-stack integration, adapters, and end-to-end tests* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

These boundaries make the Acme case—Acme's first FastAPI route validates input, calls the model, queries the database, invokes a refund tool, and formats AG-UI events in one function.—testable and replaceable.

---

## Case study — Acme's first FastAPI route validates input, calls the model

Acme's first FastAPI route validates input, calls the model, queries the database, invokes a refund tool, and formats AG-UI events in one function.

### The walkthrough

1. Maya separates the refund-review use case from transport and defines its domain inputs, decisions, and results.
2. Provider, retrieval, protocol, and repository calls move behind ports with synthetic test doubles.
3. The route becomes a narrow adapter, while durable work and compensation move to owned worker boundaries.
4. Domain tests now prove stale evidence and cross-tenant proposals fail without starting a model or database.

### The result

The Python project becomes easier to test, operate, replace, and explain because every layer has one job.

### The danger

A large asynchronous route can look concise while hiding business authority, unbounded retries, leaked provider errors, and untestable side effects.

### The takeaway

Keep FastAPI at the edge, business rules in the core, and protocols behind adapters.

---

## Composition

The picture is a Python service map. A **PYTHON SERVICE** platform in the center contains white cards for **API ROUTERS**, **DOMAIN CORE**, **POLICY**, **ORCHESTRATOR**, **MCP ADAPTER**, **A2A ADAPTER**, **AG-UI ADAPTER**, **REPOSITORIES**, **WORKERS**, and **AUDIT**. A **PYDANTIC CONTRACT** ring surrounds the boundary. On the right, two coral blocked paths—**FAT ROUTE** and **MODEL DIRECT TO DB**—are marked with red. The composition shows FastAPI as one edge of a layered domain.

## Element by element

- **PYTHON SERVICE** — a labeled visual element in this diagram; the prompt shows it as PYTHON SERVICE with API ROUTERS.
- **API ROUTERS** — a labeled visual element in this diagram; the prompt shows it as PYTHON SERVICE with API ROUTERS.
- **DOMAIN CORE** — The domain core owns business language and invariants such as evidence freshness, proposal binding, human authority, refund limits, and receipt semantics.
- **MCP ADAPTER** — Test domain rules, adapter conformance, repositories, workflow replay, security, and API acceptance separately.
- **A2A ADAPTER** — Test domain rules, adapter conformance, repositories, workflow replay, security, and API acceptance separately.
- **AG-UI ADAPTER** — Test domain rules, adapter conformance, repositories, workflow replay, security, and API acceptance separately.
- **FAT ROUTE** — the coral anti-pattern of putting the whole architecture in one FastAPI route.
- **MODEL DIRECT TO DB** — the coral anti-pattern of letting the model write to the database directly.
- **PYDANTIC CONTRACT** — a labeled visual element in this diagram; the prompt shows it as Pydantic CONTRACT surrounds boundaries.
- **POLICY** — Assign the future Python and FastAPI project clear domain, orchestration, policy, persistence, and protocol responsibilities.
- **ORCHESTRATOR** — the ORCHESTRATOR card shown in this diagram; it is one of the labeled elements the architecture uses.
- **REPOSITORIES** — Repositories isolate operational state, evidence, artifacts, memory, audit, and authoritative integrations.
- **WORKERS** — the WORKERS card shown in this diagram; it is one of the labeled elements the architecture uses.
- **AUDIT** — Repositories isolate operational state, evidence, artifacts, memory, audit, and authoritative integrations.
- **CONTRACT** — a labeled visual element in this diagram; the prompt shows it as Pydantic CONTRACT surrounds boundaries.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **PYTHON SERVICE**, **API ROUTERS**, **DOMAIN CORE**, **MCP ADAPTER**, **A2A ADAPTER**, **AG-UI ADAPTER** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **PYTHON SERVICE**, **API ROUTERS**, **DOMAIN CORE**, **MCP ADAPTER** carry the forward motion of the architecture.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **FAT ROUTE**, **MODEL DIRECT TO DB** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **PYDANTIC CONTRACT**, **POLICY**, **AUDIT**, **CONTRACT** are the readable records the diagram communicates.

---

## How to present it

- Point to **PYTHON SERVICE** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **API ROUTERS** and ask what would have to change for the team to organize routers around product capabilities rather than provider or protocol names, and who would own that change.
- Point to **DOMAIN CORE** and ask what evidence would show the team has already define application use cases and domain invariants independently from transport and persistence, and what test would fail first if it is missing.
- Point to **MODEL DIRECT TO DB** and ask who else in the room must agree before the team can place model, MCP, A2A, AG-UI, policy, identity, and storage behind explicit ports and adapters, and what would change their mind.
- Point to **WORKERS** and ask what the smallest version of choose synchronous, durable worker, and compensation paths from effect and recovery needs looks like, and what would be left out of that version.
- Point to **MCP ADAPTER** and ask what would have to change for the team to test domain rules, adapter conformance, repositories, workflow replay, security, and API acceptance separately, and who would own that change.
- Show the **coral** path (FAT ROUTE and MODEL DIRECT TO DB are blocked) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Point to **DOMAIN CORE** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Point to **POLICY** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Point to **AUDIT** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Use the analogy: A restaurant's waiter accepts an order, the kitchen applies recipes and safety rules, suppliers provide ingredients, and accounting records payment. The waiter should not become the recipe, supplier, and bank at the same time. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Design the Python package tree and dependency rules for Acme. Include routers, use cases, domain models, ports, adapters, repositories, workers, policy, telemetry, migration, configuration, and unit, contract, integration, and workflow test locations.
- Pose the checkpoint: *Does Pydantic validation prove that a request is authorized?*

---

## Lab and checkpoint

**Lab:** Design the Python package tree and dependency rules for Acme. Include routers, use cases, domain models, ports, adapters, repositories, workers, policy, telemetry, migration, configuration, and unit, contract, integration, and workflow test locations.

**Checkpoint:** Does Pydantic validation prove that a request is authorized?

**Answer:** No. It proves the data shape. Authorization must still evaluate actor, tenant, resource, action, purpose, policy, and current state.

---

## Glossary

- **Domain core** — business concepts and rules independent of frameworks
- **Port** — interface the core uses to reach an outside capability
- **Composition root** — place where concrete dependencies are assembled

---

## Sources

- FastAPI bigger applications
- FastAPI testing
- FastAPI deployment concepts
- Pydantic models

---

## Related lessons

- **Lesson 229** — Shared schemas, contracts, fixtures, and conformance cases (`shared-contract-conformance-kit`)
- **Lesson 232** — Cross-stack integration, adapters, and end-to-end tests (`cross-stack-adapter-test-loop`)
- **Lesson 234** — Database, vector index, queue, cache, and artifact storage (`polyglot-storage-decision-map`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for Python and FastAPI responsibility map until the diagram is legible to every reviewer. Assign the future Python and FastAPI project clear domain, orchestration, policy, persistence, and protocol responsibilities. The trace moves through 5 decisions: Organize routers around product capabilities rather than provider or protocol names.; Define application use cases and domain invariants independently from transport and persistence.; Place model, MCP, A2A, AG-UI, policy, identity, and storage behind explicit ports and adapters.; Choose synchronous, durable worker, and compensation paths from effect and recovery needs.; Test domain rules, adapter conformance, repositories, workflow replay, security, and API acceptance separately.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—Acme's first FastAPI route validates input, calls the model, queries the database, invokes a refund tool, and formats AG-UI events in one function.—shows that Keep FastAPI at the edge, business rules in the core, and protocols behind adapters. If the team skips this, A large asynchronous route can look concise while hiding business authority, unbounded retries, leaked provider errors, and untestable side effects. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.