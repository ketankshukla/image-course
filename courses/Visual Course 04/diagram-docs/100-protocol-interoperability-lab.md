# Diagram 100 — Protocol Interoperability Lab

![A full architecture on dark navy. MAYA IN REACT UI on the left, with an AG-UI card listing RUN, TOOL, STATE and ERROR, connects by a double-headed AG-UI arrow to a central ORCHESTRATOR node tree. Two CALLS arrows lead right to POLICY MCP SERVER with an MCP card listing MCP DISCOVERY, TOOL AND RESOURCE, MRTR OR TASK, and to PAYMENT A2A AGENT, a purple robot with an A2A AGENT CARD listing TASK, STATUS, ARTIFACT. A CORRELATION SPINE bar beneath the orchestrator connects down to TRUST GATEWAY, DURABLE STORE, CONFORMANCE SUITE and TRACE AND AUDIT. At lower right, a red-bordered box holds DRAFT INTERRUPT ADAPTER with a red octagon and raised hand.](../diagrams/100-protocol-interoperability-lab.png)

**Module:** Capstone
**Role in the course:** all three protocols in one working system
**Layout:** a user interface, an orchestrator, two protocol destinations, a correlation spine over four shared services, and one draft component held apart

---

## At a glance

The whole volume, assembled. A named user — **Maya** — in a React interface, an orchestrator, an **MCP server**, an **A2A agent**, and four shared services hanging off a **correlation spine**.

And at lower right, inside a **red-bordered box**, held deliberately apart: **DRAFT INTERRUPT ADAPTER**.

That box is the most instructive element. A finished architecture diagram with one component visibly marked as not yet settled is more honest than one that pretends everything is decided.

---

## What the diagram teaches

### 1. Three protocols, three relationships, one orchestrator

**AG-UI** connects the interface to the orchestrator, drawn with a **double-headed arrow**. Bidirectional, because a user both receives progress and intervenes.

**CALLS** connects the orchestrator to the MCP server. One direction with a dashed return — a request and a result.

**CALLS** connects the orchestrator to the A2A agent. Same rendering, different meaning: a delegation and an artifact.

The orchestrator is the only component touching all three. It is where protocol selection happens, and it is why the correlation spine hangs from it.

### 2. Each protocol destination carries a card naming what it uses

**The MCP card** lists **MCP DISCOVERY**, **TOOL AND RESOURCE**, **MRTR OR TASK**.

Three capabilities of the protocol, and the third is a choice: multi round-trip *or* the tasks extension, depending on the operation.

**The A2A card** lists **TASK**, **STATUS**, **ARTIFACT**.

The three objects of the A2A model.

**The AG-UI card** lists **RUN**, **TOOL**, **STATE**, **ERROR**.

Four event categories the interface consumes.

Naming what each side actually uses — rather than just naming the protocol — makes the diagram a specification rather than a label.

### 3. Maya is named, and that is a deliberate choice

**MAYA IN REACT UI**, with a person glyph and a chat interface.

Naming the user rather than drawing a generic figure is unusual in this library. It signals that the capstone is a scenario, not an abstraction — there is a specific person doing a specific thing.

It also sets up the diagram's implicit narrative: Maya asks for something, the orchestrator routes it, one path reads policy and another moves money, and Maya sees what happened.

### 4. The correlation spine sits beneath the orchestrator and carries four services

A horizontal **CORRELATION SPINE** bar with a chain-link glyph, connected downward to four shared services:

**TRUST GATEWAY** (teal shield) — where agent cards, tokens and audiences are validated.

**DURABLE STORE** (blue database) — where tasks, checkpoints and state live.

**CONFORMANCE SUITE** (clipboard and gear) — where the requirement matrix runs.

**TRACE AND AUDIT** (magnifier and chart) — where the correlated record is assembled.

All four are **shared across both protocol paths**. There is not an MCP trust gateway and an A2A one.

### 5. CONFORMANCE SUITE as a runtime component is the volume's distinctive claim

Most architecture diagrams place a test suite outside the system, in a build pipeline.

This one puts it **inside**, hanging off the correlation spine alongside the durable store and the audit trail.

The claim: conformance is not something you verify before shipping and then forget. It is a continuously-exercised property, checked against live behaviour, using the same correlation identifiers as everything else.

That placement is what connects the requirement matrix from the start of the volume to the running system at the end.

### 6. The draft interrupt adapter is boxed in red and connected to nothing

At lower right, inside a **red-bordered container**, a **red octagon with a raised hand**.

Two things about it.

**It is boxed.** Visually separated from the architecture rather than integrated into it.

**It connects to nothing.** No arrows enter or leave.

That is what "draft" means, drawn honestly. The component is anticipated, its shape is not settled, and it is not yet part of the system.

The raised-hand octagon is the interrupt glyph from the AG-UI material — the human-intervention path. Marking it as draft says the interrupt handling across protocol boundaries is the part of this architecture that is still being worked out.

### 7. Naming what is unfinished is the diagram's closing lesson

An architecture diagram that shows only settled components tells you what someone decided. One that marks the unsettled part tells you where the risk is.

For a capstone, that is the right note to end on. The volume has covered normative rules, negotiation, conformance, bindings, adapters and migration — and the honest conclusion is that cross-protocol human interruption is not fully solved.

Every boundary in this architecture was chosen by applying one question:

![A decision tree headed WHO OWNS THE OTHER SIDE branching to SAME PROCESS, APP TO CAPABILITY SERVER, AGENT TO INDEPENDENT AGENT and AGENT TO USER INTERFACE, producing INTERNAL FUNCTION, MCP, A2A and AG-UI, all routing into a coral banner reading DO NOT STACK PROTOCOLS WITHOUT A REAL BOUNDARY.](../diagrams/97-protocol-boundary-decision-tree.png)

Three of that diagram's four answers appear here as protocols. The fourth — **INTERNAL FUNCTION** — is everything inside the orchestrator that this diagram does not draw, and it is the largest part of the system by volume.

---

## Case study — the lab itself, built as a teaching system

This diagram describes a working reference implementation rather than a customer deployment. It is the system the volume's exercises are run against, and the case study is its construction.

### What it does

Maya is a payments operations analyst. She asks the assistant to investigate and, where appropriate, resolve a payment dispute.

The orchestrator:

- Retrieves the applicable dispute policy from the **policy MCP server**, using discovery to find the right resource and MRTR when the policy question is ambiguous.
- Delegates the financial assessment to the **payment A2A agent**, which returns a determination as an artifact.
- Streams progress to Maya over AG-UI, surfaces the artifact when it is ready, and pauses for her approval before anything moves money.

Three protocols, one operation, one correlated trace.

### Why each protocol is used where it is

**MCP for policy** because the policy server is a capability. It reads and returns; it has no view about whether a dispute should be resolved.

**A2A for assessment** because the payment agent is independent. It applies rules the payments team owns, it can decline, and it returns an artifact rather than a value.

**AG-UI for Maya** because the other side is a person who needs to see progress and be able to intervene.

Applying the ownership question from diagram 97 to each boundary produces exactly this allocation, and the lab exists partly to demonstrate that.

### The correlation spine in practice

Every operation carries the five identifiers from diagram 98. A single dispute investigation produces:

- One **trace ID**, spanning the AG-UI session, the MCP calls, the A2A task, and the audit record.
- One **case ID** — the dispute.
- One **task ID** for the A2A delegation.
- Several **tool call IDs** for the MCP invocations.
- One **idempotency key** on the settlement operation.

The trace and audit service assembles these into a single readable record. That record is what the exercises interrogate.

### What the conformance suite checks at runtime

The suite runs continuously against the lab, not only in CI.

It exercises the requirement matrix from diagram 80 — MUST, SHOULD and conditional MAY tests — against the live MCP server and the live A2A agent.

**It has caught three regressions** during the volume's development, all introduced by changes to the reference implementations:

An MCP server change that stopped returning cache scope on list responses, breaking the per-caller caching requirement.

An A2A agent change that collapsed `rejected` into `failed` — the same class of error as the Ferrisburgh case study, introduced accidentally in the very system built to teach it.

An AG-UI change that emitted a `RUN FINISHED` event without a preceding `STEP FINISHED`, violating the pairing requirement from diagram 93.

That second one is worth dwelling on. The team that wrote the case study about state collapse introduced state collapse. The suite caught it in under an hour.

### Why the interrupt adapter is still draft

The unsolved problem: **a human interrupt that arrives while work is in flight across two protocols.**

Maya clicks pause. At that moment:

- An MCP call may be in flight.
- An A2A task may be working.
- An AG-UI run is streaming.

Three protocols with three different cancellation semantics.

**MCP** has no cancellation for an in-flight call. A call either returns or does not. The tasks extension has `tasks/cancel`, but only for promoted calls.

**A2A** has task cancellation, and it races with completion — diagram 91's problem.

**AG-UI** ends the run with an interrupt outcome — diagram 95's model.

Reconciling three cancellation models into one coherent user-facing pause is genuinely hard, and the lab has not settled it.

**Three approaches have been prototyped**, and each has a defect:

*Cancel everything and reconcile afterwards.* Simple, and it leaves side effects that occurred between the pause and the cancellations propagating.

*Refuse to pause during effectful operations.* Safe, and Maya cannot pause when she most wants to.

*Pause at the orchestrator only, letting in-flight work complete.* Honest, and the interface must then explain that the pause is not immediate — which testing showed users do not reliably understand.

The box stays red until one of these is resolved or a fourth is found.

### The teaching value of leaving it unsolved

The lab's exercises include a task asking learners to design the interrupt adapter.

There is no reference answer, because there is not one yet. That is the point: a volume about protocol engineering that presented every problem as solved would be teaching the wrong thing about protocols.

---

## Composition

A full-width architecture with a user on the left, an orchestrator at centre, two protocol destinations on the right, a shared-services tier beneath, and a boxed draft component at lower right.

**Left:** **MAYA IN REACT UI** — a dark screen with a person glyph, chat bubbles and an input field, on a blue platform. Beneath, a white **AG-UI** card listing **RUN** (play), **TOOL** (wrench), **STATE** (database), **ERROR** (red triangle).

**Centre:** **ORCHESTRATOR** — a blue node-tree glyph on a large blue platform, connected to Maya by a **double-headed cyan arrow labelled AG-UI**.

**Right:** two **CALLS** arrows lead to **POLICY MCP SERVER** (a teal server unit) with a white **MCP** card listing **MCP DISCOVERY** (magnifier), **TOOL AND RESOURCE** (wrench), **MRTR OR TASK** (clipboard); and to **PAYMENT A2A AGENT** (a purple robot with a `$` badge) with a white **A2A AGENT CARD** listing **TASK**, **STATUS**, **ARTIFACT**. **Teal dashed arrows** return from both cards toward the spine.

**Beneath the orchestrator:** a **CORRELATION SPINE** bar with a chain-link glyph, connected by dotted lines down to four bordered panels — **TRUST GATEWAY** (teal shield), **DURABLE STORE** (blue database), **CONFORMANCE SUITE** (clipboard and gear), **TRACE AND AUDIT** (magnifier over a chart).

**Lower right:** a **red-bordered box** containing **DRAFT INTERRUPT ADAPTER** in coral, above a **red octagon with a white raised hand**. No connections.

## Element by element

**MAYA IN REACT UI** — a named user at a chat interface.

**AG-UI card** — four event categories the interface consumes.

**ORCHESTRATOR** — a node tree; the only component touching all three protocols.

**POLICY MCP SERVER** — a teal server with three named MCP capabilities.

**PAYMENT A2A AGENT** — a purple robot with the three A2A objects.

**CORRELATION SPINE** — a chain-link bar carrying identifiers to four shared services.

**TRUST GATEWAY / DURABLE STORE / CONFORMANCE SUITE / TRACE AND AUDIT** — four shared services, used by both protocol paths.

**DRAFT INTERRUPT ADAPTER** — a red octagon with a raised hand, boxed and unconnected.

## Colour and flow semantics

- **Cyan arrows** carry AG-UI bidirectionally and the two CALLS paths outward.
- **Teal dashed arrows** carry returns from both protocol destinations toward the spine.
- **Dotted lines** connect the spine to the four shared services, marking them as threaded rather than sequential.
- **Purple** distinguishes the A2A agent as an independent party, unlike the teal MCP server.
- **Red** appears only in the draft box, marking the one unsettled component.

## How to present it

**Do not walk every component.** It is the closing diagram of the volume, and a tour repeats what the previous 23 covered.

**Trace one operation end to end.** Maya asks; the orchestrator retrieves policy over MCP; it delegates assessment over A2A; it streams progress and pauses for approval over AG-UI. One path, naming each protocol's role.

**Ask why each boundary uses the protocol it does.** Apply the ownership question. Policy server is a capability. Payment agent is independent. Maya is a person. The allocation falls out.

**Point at the three cards and note what they list.** Not just protocol names — the specific capabilities each side uses. That makes the diagram a specification rather than a label.

**Ask why the conformance suite is inside the architecture.** Most teams place a test suite in a pipeline. Putting it on the correlation spine says conformance is a continuously-exercised runtime property.

**Tell the self-inflicted regression.** The team that wrote the case study about `rejected` collapsing into `failed` introduced exactly that, in the reference implementation, and the suite caught it in under an hour. That is the argument for runtime conformance in one story.

**Then go to the red box and make it the closing point.** Ask what it means that a component is boxed and connected to nothing.

**Lay out the interrupt problem.** Maya clicks pause; an MCP call is in flight, an A2A task is working, an AG-UI run is streaming. Three protocols, three cancellation models. MCP has none for un-promoted calls. A2A's races with completion. AG-UI ends the run.

**Give them the three prototypes and their defects.** Cancel everything and leak side effects. Refuse to pause when it matters most. Pause at the orchestrator only and confuse users. Ask the room which they would choose.

**Close on why it is left unsolved.** A volume about protocol engineering that presented every problem as solved would be teaching the wrong thing. The exercises ask learners to design this adapter, and there is no reference answer because there is not one yet.

**Timing.** Thirty minutes as a closing session. Forty-five if you run the interrupt-adapter design exercise, which is the best possible exit from the volume.

---

## Lab and checkpoint

**Lab:** Trace one operation through your own system and label each boundary with the correct protocol: same-process, MCP, A2A, or AG-UI. For each, justify the choice by ownership, deployment independence, and the inability to unilaterally change the contract. Then sketch a draft interrupt adapter for a pause that reaches across all three.

**Checkpoint:** Why is the conformance suite drawn as a runtime component on the correlation spine?

**Answer:** Because conformance is not a one-time test before release; it must be continuously exercised against real traffic and real implementations. Placing the suite on the correlation spine makes it a living part of the architecture that can catch regressions as the system changes.

## Glossary

- **AG-UI** — the protocol for agent-to-user interaction.
- **A2A** — the protocol for agent-to-agent collaboration.
- **Conformance suite** — the runtime tests that check protocol behaviour.
- **Correlation spine** — the shared identifiers and tracing that connect the services.
- **Draft interrupt adapter** — the unfinished component for pausing work across protocols.
- **MCP** — the protocol for app-to-capability-server calls.
- **Maya** — the user persona in the lab example.
- **Orchestrator** — the central agent that coordinates the three protocols.
- **Protocol boundary** — the edge where one protocol ends and another begins.
- **Runtime conformance** — the practice of testing protocol behaviour continuously in production.

## Sources

- MCP, A2A, and AG-UI interoperability
- Runtime conformance testing and correlation
- Protocol boundary and adapter design
