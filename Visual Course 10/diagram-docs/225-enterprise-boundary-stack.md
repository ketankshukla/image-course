# Diagram 225 — Capability, context, model, tool, and authority boundaries

![An enterprise stack separates user, web app, agent service, model, MCP client, MCP server, tool, and business system with context, capability, identity, policy, and authority gates.](../diagrams/225-enterprise-boundary-stack.png)

**Module:** Reference architecture and contracts
**Role in the course:** Draw a complete trust-boundary view that separates what a component knows, can request, may execute, and is authoritative to commit.
**Layout:** TRUST ZONES USER begins on the left and the diagram flows toward BOUNDED REQUEST; a teal **BOUNDED REQUEST** path is the desired route and a coral **DIRECT MODEL TO BUSINESS WRITE** path is blocked or contained.

---

## At a glance

**Capability, context, model, tool, and authority boundaries** — Draw a complete trust-boundary view that separates what a component knows, can request, may execute, and is authoritative to commit.

- The central takeaway is: Let protocols carry bounded information and requests; let product policy and authoritative systems decide what can commit.
- The visual begins with **TRUST ZONES USER** and ends with the diagram's outcome, not a technology name.
- The safe or selected path is marked **teal**: BOUNDED REQUEST reaches RECEIPT.
- The blocked or dangerous path is marked **coral**: DIRECT MODEL TO BUSINESS WRITE is blocked.
- The analogy is: An office badge may open the lobby, a filing cabinet, or a laboratory, but entering the building does not authorize signing a bank transfer. Location, information access, and decision authority are different controls.

---

## What the diagram teaches

### 1. Capability, context, model, tool, and authority boundaries

The model generates candidates, the agent service coordinates, MCP exposes declared capabilities, tools perform bounded operations, and the business system establishes committed truth. MCP standardizes communication between a host, its clients, and servers that expose resources, prompts, or tools. These protocols meet at adapters; neither grants a model direct database authority. In the diagram, **DIRECT MODEL TO BUSINESS WRITE**, **MODEL**, **TOOL** appear at the left, turning this idea into something a reviewer can point at.

### 2. Name Components and Assign One Owned Job to Each.

The diagram should show these gates where they happen. The visual places **TRUST ZONES USER**, **WEB APP**, **AGENT SERVICE** at the center; the arrows between them are the physical expression of this principle. If this is skipped, when context, capability, and authority share one path, prompt injection can become a privileged business action instead of merely bad text.

### 3. Draw Every Network, Process, Tenant, Provider, and Privilege Boundary.

AG-UI streams typed interaction state to a frontend. Every crossing needs an input schema, output schema, authentication, authorization, tenant rule, time limit, size limit, retry rule, privacy class, audit event, and failure behavior. The trace asks the team to draw every network, process, tenant, provider, and privilege boundary. Look at **TRUST ZONES USER**, **WEB APP**, **AGENT SERVICE** on the top: the diagram uses those elements to show where this decision lives.

### 4. Separate Context, Capability, Identity, Policy, Consent, and Authority at Each Crossing.

Capability is an operation a component can request. Authority is permission to make a consequential decision. It does not remove the application's need to validate identity, tenant, arguments, policy, consent, and result receipts. The picture shows **CONTEXT**, **CAPABILITY**, **IDENTITY** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: The A2A adapter treats the content as an artifact, not executable authority.

### 5. Place Validation and Business Invariants Again Beside the Authoritative Effect.

A2A describes peer-agent discovery and task communication. A malicious document, model output, or remote agent still cannot invent scopes, cross tenants, alter an approved amount, or bypass the authoritative command handler. To put this into practice, the team should place validation and business invariants again beside the authoritative effect. At the bottom, **BUSINESS SYSTEM**, **DIRECT MODEL TO BUSINESS WRITE** is the element that makes this concept concrete before any code is written.

### 6. Test One Compromised or Unavailable Component Per Boundary and Record Containment Evidence.

A component boundary is useful only when it describes responsibility and trust. Combining them into one broad token or prompt makes review and containment difficult. The architecture fails safely when a powerful component is compromised. In the diagram, **TRUST ZONES USER**, **WEB APP**, **AGENT SERVICE** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, the architecture fails safely when a powerful component is compromised.

### 7. Let protocols carry bounded information and requests

Context is information supplied for one purpose. The visual places **BOUNDED REQUEST** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

An office badge may open the lobby, a filing cabinet, or a laboratory, but entering the building does not authorize signing a bank transfer. Location, information access, and decision authority are different controls. Look at **TRUST ZONES USER**, **WEB APP**, **AGENT SERVICE** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: A remote research agent returns a recommendation containing a tool-like instruction to refund a customer immediately.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Keep secrets, provider calls, and privileged policy checks in server-only modules; send the browser only the state and controls it is allowed to render.
- Represent every proposal with resource, action, subject, evidence revision, tenant, actor, expiry, and recovery before enabling a decision control.
- Use route and component boundaries to make public, authenticated, tenant, administrator, and embedded-app zones visible and testable.

Together these choices prevent the mistakes in the Acme case—A remote research agent returns a recommendation containing a tool-like instruction to refund a customer immediately.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Create ports for model, MCP, A2A, policy, identity, audit, and business systems; adapters translate protocols without leaking their data types into the domain core.
- Validate tool intent before dispatch and validate returned evidence before it can influence a proposal.
- Require the authoritative command handler to recheck actor, tenant, policy, subject, revision, approval, and idempotency immediately before commit.
![A client experience uses AG-UI with an agent service, which uses MCP for tools and context, A2A for peer agents, HTTP for business APIs, queues for durable work, and internal calls within the domain.](../diagrams/227-protocol-boundary-routing-map.png)

Diagram 227 — *MCP, A2A, AG-UI, HTTP, queue, and internal boundaries* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

These boundaries make the Acme case—A remote research agent returns a recommendation containing a tool-like instruction to refund a customer immediately.—testable and replaceable.

---

## Case study — A remote research agent returns a recommendation containing a tool-like

A remote research agent returns a recommendation containing a tool-like instruction to refund a customer immediately.

### The walkthrough

1. The A2A adapter treats the content as an artifact, not executable authority.
2. The coordinator extracts evidence through a validated schema and creates a bounded proposal.
3. Maya reviews the proposal in the web app; her decision is bound to the current subject and evidence.
4. The payment command handler rechecks policy and commits once, returning the receipt through the normal event path.

### The result

Untrusted agent content can inform a decision without becoming a hidden command.

### The danger

When context, capability, and authority share one path, prompt injection can become a privileged business action instead of merely bad text.

### The takeaway

Let protocols carry bounded information and requests; let product policy and authoritative systems decide what can commit.

---

## Composition

The picture is a vertical trust-zone stack. From top to bottom, the zones are **USER**, **WEB APP**, **AGENT SERVICE**, **MODEL**, **MCP CLIENT**, **MCP SERVER**, **TOOL**, **BUSINESS SYSTEM**, each on a cobalt platform. Between the zones, gates—**CONTEXT**, **CAPABILITY**, **IDENTITY**, **POLICY**, **AUTHORITY**—appear as white cards. A teal **BOUNDED REQUEST** arrow descends from the user to a **RECEIPT** at the bottom. A coral **DIRECT MODEL TO BUSINESS WRITE** arrow is blocked by a red mark. The composition shows that no layer skips the one below it.

## Element by element

- **TRUST ZONES USER** — a labeled visual element in this diagram; the prompt shows it as stacked TRUST ZONES USER.
- **WEB APP** — Maya reviews the proposal in the web app; her decision is bound to the current subject and evidence.
- **AGENT SERVICE** — The model generates candidates, the agent service coordinates, MCP exposes declared capabilities, tools perform bounded operations, and the business system establishes committed truth.
- **MCP CLIENT** — the MCP CLIENT card shown in this diagram; it is one of the labeled elements the architecture uses.
- **MCP SERVER** — the MCP SERVER card shown in this diagram; it is one of the labeled elements the architecture uses.
- **BUSINESS SYSTEM** — The model generates candidates, the agent service coordinates, MCP exposes declared capabilities, tools perform bounded operations, and the business system establishes committed truth.
- **BOUNDED REQUEST** — the safe, verified, or authoritative element marked in teal; in this diagram BOUNDED REQUEST reaches RECEIPT.
- **DIRECT MODEL TO BUSINESS WRITE** — the coral anti-pattern where a model or its output can write directly to authoritative business records.
- **MODEL** — The model generates candidates, the agent service coordinates, MCP exposes declared capabilities, tools perform bounded operations, and the business system establishes committed truth.
- **TOOL** — A remote research agent returns a recommendation containing a tool-like instruction to refund a customer immediately.
- **CONTEXT** — Context is information supplied for one purpose.
- **CAPABILITY** — Capability is an operation a component can request.
- **IDENTITY** — It does not remove the application's need to validate identity, tenant, arguments, policy, consent, and result receipts.
- **POLICY** — It does not remove the application's need to validate identity, tenant, arguments, policy, consent, and result receipts.
- **AUTHORITY** — Authority is permission to make a consequential decision.
- **RECEIPT** — The payment command handler rechecks policy and commits once, returning the receipt through the normal event path.
- **USER** — a labeled visual element in this diagram; the prompt shows it as stacked TRUST ZONES USER.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **TRUST ZONES USER**, **WEB APP**, **AGENT SERVICE**, **BUSINESS SYSTEM** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **TRUST ZONES USER**, **WEB APP**, **AGENT SERVICE**, **MCP CLIENT** carry the forward motion of the architecture.
- **Teal arrow** — an authoritative decision, verified contract, passing gate, safe release, or recovered service. The teal elements **BOUNDED REQUEST**, **RECEIPT** show the path the design wants to keep open.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **DIRECT MODEL TO BUSINESS WRITE** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **IDENTITY**, **POLICY**, **AUTHORITY** are the readable records the diagram communicates.

---

## How to present it

- Point to **TRUST ZONES USER** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **WEB APP** and ask what would have to change for the team to list components and assign one owned job to each, and who would own that change.
- Point to **AGENT SERVICE** and ask what evidence would show the team has already draw every network, process, tenant, provider, and privilege boundary, and what test would fail first if it is missing.
- Point to **CONTEXT** and ask who else in the room must agree before the team can separate context, capability, identity, policy, consent, and authority at each crossing, and what would change their mind.
- Point to **BUSINESS SYSTEM** and ask what the smallest version of place validation and business invariants again beside the authoritative effect looks like, and what would be left out of that version.
- Point to **MCP SERVER** and ask what would have to change for the team to test one compromised or unavailable component per boundary and record containment evidence, and who would own that change.
- Trace the **teal** path (BOUNDED REQUEST reaches RECEIPT) and ask what evidence would prove the real system follows it, who collects that evidence, and how often it is refreshed.
- Show the **coral** path (DIRECT MODEL TO BUSINESS WRITE is blocked) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Point to **TRUST ZONES USER** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Point to **POLICY** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Point to **AUTHORITY** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Use the analogy: An office badge may open the lobby, a filing cabinet, or a laboratory, but entering the building does not authorize signing a bank transfer. Location, information access, and decision authority are different controls. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Draw the full Acme context diagram. For ten boundaries, record caller, receiver, data, capability, identity, tenant, policy, consent, authority, validation, timeout, retry, audit, and fail-safe behavior.

---

## Lab and checkpoint

**Lab:** Draw the full Acme context diagram. For ten boundaries, record caller, receiver, data, capability, identity, tenant, policy, consent, authority, validation, timeout, retry, audit, and fail-safe behavior.

**Checkpoint:** Does access to an MCP tool mean the model is authorized to use it for any customer?

**Answer:** No. Discovery or capability access is not business authorization. The application must enforce actor, tenant, purpose, arguments, policy, and consent for each operation.

---

## Glossary

- **Trust boundary** — place where assumptions and controls change
- **Capability** — bounded operation a component can request
- **Authority** — permission to decide or commit an effect

---

## Sources

- MCP 2026-07-28 specification
- MCP architecture
- A2A and MCP
- AG-UI architecture

---

## Related lessons

- **Lesson 221** — Problem, workflow, assistant, agent, and automation boundaries (`automation-boundary-map`)
- **Lesson 227** — MCP, A2A, AG-UI, HTTP, queue, and internal boundaries (`protocol-boundary-routing-map`)
- **Lesson 233** — Authentication, secrets, tenants, policy, and audit services (`identity-policy-audit-services`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for Capability, context, model, tool, and authority boundaries until the diagram is legible to every reviewer. Draw a complete trust-boundary view that separates what a component knows, can request, may execute, and is authoritative to commit. The trace moves through 5 decisions: List components and assign one owned job to each.; Draw every network, process, tenant, provider, and privilege boundary.; Separate context, capability, identity, policy, consent, and authority at each crossing.; Place validation and business invariants again beside the authoritative effect.; Test one compromised or unavailable component per boundary and record containment evidence.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—A remote research agent returns a recommendation containing a tool-like instruction to refund a customer immediately.—shows that Let protocols carry bounded information and requests; let product policy and authoritative systems decide what can commit. If the team skips this, When context, capability, and authority share one path, prompt injection can become a privileged business action instead of merely bad text. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.