# Diagram 209 — Typed components, schemas, allowlists, and validation

![A model's declarative interface tree passes schema, component allowlist, property validation, action policy, and a version adapter before safe accessible components render; arbitrary code is rejected.](../diagrams/209-typed-components-schemas-allowlists-validation.png)

**Module:** Generative and embedded interfaces
**Role in the course:** Let an agent choose from safe interface building blocks without allowing it to execute arbitrary frontend code.
**Layout:** The diagram shows MODEL proposing a declarative UI TREE into JSON SCHEMA, COMPONENT ALLOWLIST, PROP VALIDATOR, ACTION POLICY, with a coral risk path, and a teal safe path.

---

## At a glance

**Let an agent choose from safe interface building blocks without allowing it to execute arbitrary frontend code.**

- The diagram centers on **MODEL** and its relationship to **ACCESSIBLE UI**.

- The diagram separates the tested, legitimate flow from failure paths that must fail closed.

- Maya's case: Maya asks Acme to compare three refund options. The agent proposes a table, an evidence notice, and an Approve exception button.

---

## What the diagram teaches

### 1. A2UI Follows This Server-driven Idea

A2UI follows this server-driven idea. The diagram makes this concrete through **MODEL**, **UI TREE**, **JSON SCHEMA**. If the team skips this, rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary. This is the lesson the case study ends with: Let the model compose a small typed catalog; let the product validate, render, and authorize everything.

### 2. Dynamic Composition Does Not Remove Human Control

Dynamic composition does not remove human control. A generated button is never authority by itself. This is visible in the drawing as **MODEL**, **UI TREE**, **JSON SCHEMA**. Without this step, rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary. In the walkthrough, The table and notice match approved schemas and render through accessible product components..

### 3. Bounded Declarative Payload With Protocol Version, Surface ID, Component Tree

This step asks the team to receive a bounded declarative payload with protocol version, surface ID, component tree, data model, and proposed actions. The diagram shows this through **MODEL**, **UI TREE**, **COMPONENT ALLOWLIST**, which make the abstract step visible and testable. The model proposes structure; the product owns rendering, behavior, security, and accessibility. A declarative payload names components such as Stack, Text, Table, Form, Chart, Notice, and Button. If the team skips this, rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary. Maya's case makes this concrete: Maya asks Acme to compare three refund options. The agent proposes a table, an evidence notice, and an Approve exception button.

### 4. Validate The Envelope And Convert The Supported A2UI Version Through

Here the product must validate the envelope and convert the supported A2UI version through a dedicated adapter. In the drawing, **VERSION ADAPTER** carry this responsibility. A version adapter converts the supported wire version into the application's smaller internal view model. Without this step, rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary. The result — The interface can adapt to Maya's task while Acme retains control over code, data, actions, accessibility, and authority. — depends on getting this right.

### 5. Walk The Tree Against Component, Property, Nesting, Binding, Size

The diagram enforces this by showing the team how to walk the tree against component, property, nesting, binding, size, and action allowlists. The visual anchors are **UI TREE**, **COMPONENT ALLOWLIST**, **ACTION POLICY**; without them the step would be invisible to the user. The case study shows the risk: rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary. This is the lesson the case study ends with: Let the model compose a small typed catalog; let the product validate, render, and authorize everything.

### 6. Resolve Approved Data Into Product-owned Accessible Components While Treating All

This is the discipline that makes the product resolve approved data into product-owned accessible components while treating all text and links as untrusted input. This idea sits on **ACCESSIBLE UI** and reaches the rest of the diagram through **ACCESSIBLE UI**. Generative interface design should mean assembling approved components from typed data, not asking a model to ship JavaScript into a person's browser. Missing this is how products end up with rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary. In the walkthrough, The table and notice match approved schemas and render through accessible product components..

### 7. Reject Unsafe Nodes With A Support Reference And Log

The team must reject unsafe nodes with a support reference and log the rule that blocked them without exposing private payload data before the interface can be trustworthy. The diagram shows this through **REJECT**, **ARBITRARY HTML SCRIPT UNKNOWN ACTION OVERSIZED PAYLOAD**, which make the abstract step visible and testable. A system that ignores this will eventually face rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary. The danger the case warns about, Maya asks Acme to compare three refund options. The agent proposes a table, an evidence notice, and an Approve exception button. should make this clear.

### 8. The standard in practice

The lesson is not a perfect prototype; it is a product contract. Let an agent choose from safe interface building blocks without allowing it to execute arbitrary frontend code.. The diagram makes that contract visible through **MODEL**, **UI TREE**, **JSON SCHEMA**, so the team can argue about the contract before choosing a framework. The contract is not framework-specific; it is the set of observable promises the product makes to the person using it. Maya's case warns that rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary. The practical standard is this: Let the model compose a small typed catalog; let the product validate, render, and authorize everything.

### 9. The Next.js and Python surfaces

The same contract appears in both stacks, but the boundary moves with the architecture.
**In Next.js / React:**
- Define a discriminated TypeScript union for the internal component catalog and validate wire payloads in a server-only boundary before passing them to React.
- Render through an exhaustive component map with no eval, Function constructor, injected event handlers, or dangerouslySetInnerHTML; unknown nodes use one safe fallback.
- Keep action execution separate from rendering: components emit named intents that Server Actions or route handlers revalidate against session, policy, revision, and approval state.
- Keep the most sensitive payloads and policy decisions on the server and stream only user-visible, safe view models to client components.
**In Python / FastAPI:**
- Use Pydantic discriminated unions for supported components and actions, with maximum depth, node count, string length, collection size, and URL rules.
- Translate A2UI payloads into a stable internal model so protocol upgrades require one adapter change rather than rewriting every interface.
- Return structured validation errors with a correlation ID; never echo secrets, raw HTML, stack traces, or an entire rejected payload to the browser.
- Treat every framework callback or protocol event as raw input; validate and transform it into the product's own event vocabulary before it reaches the reducer or domain model.
Both implementations must avoid the same trap: rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary.

### 10. Analogy

A model can arrange approved pieces in a museum display case, but it cannot cut new doors into the building, rewire the alarms, or hand visitors an unknown machine. The analogy keeps the lesson grounded. The diagram's **MODEL** plays the same role as the central object in the analogy: it must be visible, labeled, and trustworthy without the user having to infer meaning from a long narrative. The parallel works because both situations require separating the object from the record, the attempt from the proof, and the promise from the evidence.
![An MCP server declares a tool and UI resource; the host loads the app in a sandboxed iframe and permits only capability-negotiated, consented, origin-checked, minimized, audited communication through the app bridge.](../diagrams/210-mcp-apps-sandbox-consent-communication.png)

Diagram 210 — *MCP Apps, sandboxed frames, consent, and communication* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

---

## Case study — Maya

Maya asks Acme to compare three refund options. The agent proposes a table, an evidence notice, and an Approve exception button.

### The walkthrough

1. The table and notice match approved schemas and render through accessible product components.
2. One cell contains model-produced markup, so the renderer treats it as text instead of executable HTML.
3. The Approve intent is recognized, but policy converts it into a versioned proposal rather than executing it.
4. Maya reviews consequence, evidence, amount, customer, expiry, and recovery before the server accepts the separate decision request.

### The result

The interface can adapt to Maya's task while Acme retains control over code, data, actions, accessibility, and authority.

### The danger

Rendering model-authored HTML or accepting arbitrary component actions turns a presentation feature into a code-execution and confused-deputy boundary.

### The takeaway

Let the model compose a small typed catalog; let the product validate, render, and authorize everything.

---

## Composition

The picture is a single-view explainer for *Typed components, schemas, allowlists, and validation*. On the left, the diagram shows MODEL proposing a declarative UI TREE into JSON SCHEMA, COMPONENT ALLOWLIST, PROP VALIDATOR, ACTION POLICY. At the top, valid cards TABLE FORM CHART NOTICE render in a SAFE COMPONENT CATALOG. In the center, coral ARBITRARY HTML SCRIPT UNKNOWN ACTION OVERSIZED PAYLOAD go to REJECT. To the right, teal VERSION ADAPTER leads to ACCESSIBLE UI. The eye travels from **MODEL** through the central flow to **ACCESSIBLE UI**, with the contrast between coral risk paths and teal recovery paths giving the reader the core message at a glance.

## Element by element

- **MODEL** — the language model or agent that proposes a declarative interface structure.
- **UI TREE** — one of the items named by **MODEL**; this is the **UI TREE** item.
- **JSON SCHEMA** — the contract that defines which component, properties, and values are valid.
- **COMPONENT ALLOWLIST** — the finite catalog of approved interface components a model may request.
- **PROP VALIDATOR** — the layer that checks the type, size, and safety of each component property.
- **ACTION POLICY** — the rule that decides whether a proposed action is allowed in the current context.
- **TABLE FORM CHART NOTICE** — the table form chart notice Valid cards TABLE FORM CHART NOTICE render in a SAFE COMPONENT CATALOG..
- **SAFE COMPONENT CATALOG** — the product-owned set of accessible, tested components that render validated data.
- **ARBITRARY HTML SCRIPT UNKNOWN ACTION OVERSIZED PAYLOAD** — the arbitrary html script unknown action oversized payload go to REJECT..
- **REJECT** — the reject ARBITRARY HTML SCRIPT UNKNOWN ACTION OVERSIZED PAYLOAD go to REJECT.
- **VERSION ADAPTER** — the boundary that translates a supported wire protocol version into a stable internal model.
- **ACCESSIBLE UI** — the accessible ui VERSION ADAPTER leads to ACCESSIBLE UI.

---

## Colour and flow semantics

The course visual grammar applies directly to this diagram.

- **Cobalt platform** — A browser surface, state store, component catalog, product boundary, workspace, or learning-platform region. Here the cobalt surface under **MODEL** and the surrounding workspace frames the product boundary; it tells the reader that this is a bounded product region, not an uncontrolled chat surface. It marks the product's responsibility to keep the user's workspace distinct from raw model output or runtime internals.

- **Cyan arrow** — A typed event, validated state update, user action, artifact reference, notification, or navigation path. Cyan arrows carry the flow of events, updates, and proposals from left to right, linking the typed cards and records to the reducer or next gate. When the reader sees cyan, they should expect a deliberate, validated transition rather than an accidental or hidden connection.

- **Teal arrow** — Authoritative state, accessible completion, informed consent, safe approval, preserved work, or verified recovery. Teal marks the authoritative and safe path, such as the committed receipt or restored state, distinguishing it from the raw request. This color tells the reader that the product has enough evidence and authority to proceed safely.

- **Coral path** — Conflict, stale UI, unsafe rendering, deceptive state, expired approval, privacy failure, lost work, or blocked action. Coral marks the conflict, stale state, or blocked action that appears when a control is missing or bypassed. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.

- **White card** — An event, component, stage, proposal, artifact, receipt, consent record, lesson, checkpoint, or recovery option. The labeled cards and records throughout the diagram are white, marking them as structured events, proposals, receipts, or recovery options. The white background separates user-meaningful records from raw system logs or generated text.

The overall flow moves from the initiating actor or request, through validation and reduction, toward either the teal recovery or completion path or the coral failure path. The color of each arrow and card is a trust cue, not a decoration.

---

## How to present it

- **Start with the user moment.** Maya asks Acme to compare three refund options. Ask the room what they need to see to feel in control. Invite someone to describe the moment before any solution appears.

- **Point at MODEL and ask what it represents.** Then trace the flow from there through the next two or three elements, naming the color and direction of each arrow. Encourage them to name the incoming trigger, the visible state, and the decision the product must make.

- **Point at MODEL for step 1.** Bounded Declarative Payload With Protocol Version, Surface ID, Component Tree. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at VERSION ADAPTER for step 2.** Validate The Envelope And Convert The Supported A2UI Version Through. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at UI TREE for step 3.** Walk The Tree Against Component, Property, Nesting, Binding, Size. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at ACCESSIBLE UI for step 4.** Resolve Approved Data Into Product-owned Accessible Components While Treating All. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at REJECT for step 5.** Reject Unsafe Nodes With A Support Reference And Log. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Use the analogy.** A model can arrange approved pieces in a museum display case, but it cannot cut new doors into the building, rewire the alarms, or hand visitors an unknown machine. Draw the parallel to the diagram and ask what would break if the two situations were handled the same way.

- **Tell the case study.** Maya asks Acme to compare three refund options Walk through the walkthrough and stop at the moment the old design would have failed. Pause at the step where the old design would have failed and ask how the new interface prevents it.

- **Run the lab.** Design a twelve-component catalog for the visual course website. For each component define props, children, data bindings, accessible behavior, responsive rule, allowed actions, size limit, unsafe examples, and test fixtures. Reject at least six malicious payloads. Ask pairs to present one part of the diagram and explain how the other parts reference it without merging their identities.

- **Pose the checkpoint.** Is schema-valid generative UI automatically safe to render? Let the room answer before confirming the principle. Collect answers, then confirm the principle and note any exceptions the team should watch for.

- **Close on the contract.** Let the model compose a small typed catalog; let the product validate, render, and authorize everything. Ask the team what their own product's equivalent of the contract would be.

---

## Lab and checkpoint

**Lab:** Design a twelve-component catalog for the visual course website. For each component define props, children, data bindings, accessible behavior, responsive rule, allowed actions, size limit, unsafe examples, and test fixtures. Reject at least six malicious payloads.

**Checkpoint:** Is schema-valid generative UI automatically safe to render?

**Answer:** No. Schema validity is one gate. The product must also enforce component and action allowlists, data exposure rules, safe text and links, size limits, accessibility, policy, and contextual authorization.

---

## Glossary

- **Declarative UI** — data describing approved interface structure
- **Component allowlist** — finite catalog permitted to render
- **Version adapter** — boundary translating a wire version into a stable internal model

---

## Sources

- [A2UI specification versions](https://a2ui.org/)
- [A2UI v0.9 protocol](https://a2ui.org/specification/v0.9-a2ui/)
- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12)
- [OWASP DOM XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html)

## Related lessons

- Diagram 205 — Interrupt, input request, approval, rejection, and expiry
- Diagram 210 — MCP Apps, sandboxed frames, consent, and communication
- Diagram 212 — Interface security, data exposure, and safe rendering

---