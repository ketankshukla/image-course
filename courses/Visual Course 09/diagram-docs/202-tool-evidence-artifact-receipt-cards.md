# Diagram 202 — Tool cards, evidence cards, artifacts, and receipts

![Separate tool, evidence, artifact, and receipt cards link a proposed action through source versions and durable output to a verified business outcome, unlike an unsupported chat claim.](../diagrams/202-tool-evidence-artifact-receipt-cards.png)

**Module:** Progress, tools, artifacts, and recovery
**Role in the course:** Choose the right card for transient execution, supporting evidence, durable output, and proof of a decision or effect.
**Layout:** The diagram shows a TOOL CALL card with PROPOSED, RUNNING, RESULT, with a coral risk path, and a teal safe path.

---

## At a glance

**Choose the right card for transient execution, supporting evidence, durable output, and proof of a decision or effect.**

- The diagram centers on **TOOL CALL** and its relationship to **VERIFIED OUTCOME**.

- The teal **VERIFIED OUTCOME** path shows the safe, authoritative, or consented route.

- Maya's case: Acme tells Maya that a refund exception was approved, but support can find only a successful policy lookup and no refund record.

---

## What the diagram teaches

### 1. It Is Not A Dump Of Telemetry

It is not a dump of telemetry. The diagram makes this concrete through **TOOL CALL**, **PROPOSED**, **RUNNING**. If the team skips this, one generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success. This is the lesson the case study ends with: Tools attempt, evidence supports, artifacts persist, and receipts prove decisions or effects.
![A partially successful workflow preserves completed research and an artifact, names the failed and unfinished stages, and offers retry, continue-later, human-help, or cancel-remainder choices.](../diagrams/203-partial-success-preserved-unfinished-work.png)

Diagram 203 — *Partial success, preserved work, and unfinished work* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 2. Tool Card From Typed Lifecycle And Result Events While Keeping

This step asks the team to render a tool card from typed lifecycle and result events while keeping privileged arguments server-side. The diagram shows this through **RESULT**, **TOOL CALL**, which make the abstract step visible and testable. Tool calls, evidence, artifacts, and receipts are related but not interchangeable. A tool card should expose the user-relevant purpose, status, safe arguments, result category, retries, and whether an external effect occurred. If the team skips this, one generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success. Maya's case makes this concrete: Acme tells Maya that a refund exception was approved, but support can find only a successful policy lookup and no refund record.

### 3. Attach Versioned Evidence Cards With Freshness, Authority, Scope, And Selection

Here the product must attach versioned evidence cards with freshness, authority, scope, and selection reason. In the drawing, **EVIDENCE**, **SOURCE VERSION FRESHNESS AUTHORITY** carry this responsibility. An evidence card needs source name, version, authority, freshness, scope, and why it matters. A citation without version or selection reason can make stale evidence look current. Without this step, one generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success. The result — Maya and support can distinguish useful research from an authorized completed refund. — depends on getting this right.

### 4. Durable Artifact Cards Whose State And Permissions Outlive The Transient

The diagram enforces this by showing the team how to create durable artifact cards whose state and permissions outlive the transient run stream. The visual anchors are **ARTIFACT**; without them the step would be invisible to the user. An artifact card survives the run. The case study shows the risk: one generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success. This is the lesson the case study ends with: Tools attempt, evidence supports, artifacts persist, and receipts prove decisions or effects.

### 5. Issue A Receipt Only From The Authoritative Decision Or Effect

This is the discipline that makes the product issue a receipt only from the authoritative decision or effect boundary and include recovery references. This idea sits on **RECEIPT** and reaches the rest of the diagram through **RECEIPT**, **ACTOR DECISION EFFECT TIME**, **NO RECEIPT**. A tool call describes attempted execution; evidence supports a conclusion; an artifact is a durable output; a receipt proves a decision, effect, or user-visible transition. A receipt should be concise and durable: actor, proposal or command, decision, effect reference, time, policy or evidence version, and reversal or support information. Missing this is how products end up with one generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success. In the walkthrough, The tool card shows that policy evaluation succeeded but the refund tool was never called..

### 6. Link Cards By Explicit References Without Merging Their Different IDs

The team must link cards by explicit references without merging their different IDs, retention, access, or ownership rules before the interface can be trustworthy. The diagram shows this through **TOOL CALL**, **PROPOSED**, **RUNNING**, which make the abstract step visible and testable. Cards should share correlation references but retain their own identities. A system that ignores this will eventually face one generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success. The danger the case warns about, Acme tells Maya that a refund exception was approved, but support can find only a successful policy lookup and no refund record. should make this clear.

### 7. The standard in practice

The lesson is not a perfect prototype; it is a product contract. Choose the right card for transient execution, supporting evidence, durable output, and proof of a decision or effect.. The diagram makes that contract visible through **TOOL CALL**, **PROPOSED**, **RUNNING**, so the team can argue about the contract before choosing a framework. The contract is not framework-specific; it is the set of observable promises the product makes to the person using it. Maya's case warns that one generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success. The practical standard is this: Tools attempt, evidence supports, artifacts persist, and receipts prove decisions or effects.

### 8. The Next.js and Python surfaces

The same contract appears in both stacks, but the boundary moves with the architecture.
**In Next.js / React:**
- Build a typed card registry that receives safe view models from server components and prevents raw tool payloads from leaking into client props.
- Give evidence and artifact cards stable URLs, accessible names, version labels, and explicit open, download, compare, or request-access actions.
- Render receipts from authoritative records and keep trace lookup as a support link rather than the only proof shown to users.
- Keep the most sensitive payloads and policy decisions on the server and stream only user-visible, safe view models to client components.
**In Python / FastAPI:**
- Separate Pydantic models and stores for tool execution, evidence references, artifact lifecycle, and business receipts.
- Create view-model adapters that redact or summarize provider-specific payloads before streaming any card data to the frontend.
- Resolve every receipt against authoritative effect state and expose support-safe references without coupling retention to telemetry.
- Treat every framework callback or protocol event as raw input; validate and transform it into the product's own event vocabulary before it reaches the reducer or domain model.
Both implementations must avoid the same trap: one generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success.

### 9. Analogy

In a workshop, the drill is the tool, the measurement sheet is evidence, the finished cabinet is the artifact, and the signed delivery note is the receipt. A photo of the drill proves none of the others. The analogy keeps the lesson grounded. The diagram's **TOOL CALL** plays the same role as the central object in the analogy: it must be visible, labeled, and trustworthy without the user having to infer meaning from a long narrative. The parallel works because both situations require separating the object from the record, the attempt from the proof, and the promise from the evidence.

---

## Case study — Maya

Acme tells Maya that a refund exception was approved, but support can find only a successful policy lookup and no refund record.

### The walkthrough

1. The tool card shows that policy evaluation succeeded but the refund tool was never called.
2. Evidence cards show the current policy and required supervisor decision.
3. The draft recommendation remains an artifact marked Needs approval rather than Completed.
4. No receipt is issued until approval and effect records exist, so the interface cannot present a false business outcome.

### The result

Maya and support can distinguish useful research from an authorized completed refund.

### The danger

One generic green 'tool complete' card can make data retrieval, proposal creation, approval, and external effect look like the same kind of success.

### The takeaway

Tools attempt, evidence supports, artifacts persist, and receipts prove decisions or effects.

---

## Composition

The picture is a single-view explainer for *Tool cards, evidence cards, artifacts, and receipts*. On the left, the diagram shows a TOOL CALL card with PROPOSED, RUNNING, RESULT. At the top, an EVIDENCE card with SOURCE VERSION FRESHNESS AUTHORITY. In the center, an ARTIFACT card with FILE VERSION STATUS. To the right, and a RECEIPT card with ACTOR DECISION EFFECT TIME. Across the middle, link all four by references. The eye travels from **TOOL CALL** through the central flow to **VERIFIED OUTCOME**, with the contrast between coral risk paths and teal recovery paths giving the reader the core message at a glance.

## Element by element

- **TOOL CALL** — a card that tracks a proposed, running, or completed tool execution.
- **PROPOSED** — one of the fields on the **TOOL CALL** card; this is the **PROPOSED** field.
- **RUNNING** — one of the fields on the **TOOL CALL** card; this is the **RUNNING** field.
- **RESULT** — one of the fields on the **TOOL CALL** card; this is the **RESULT** field.
- **EVIDENCE** — versioned support for a decision, with source, freshness, and authority.
- **SOURCE VERSION FRESHNESS AUTHORITY** — a field on the **EVIDENCE** card; this shows the **SOURCE VERSION FRESHNESS AUTHORITY** field.
- **ARTIFACT** — a durable output that outlives the run, such as a file, summary, or recommendation.
- **FILE VERSION STATUS** — a field on the **ARTIFACT** card; this shows the **FILE VERSION STATUS** field.
- **RECEIPT** — durable proof of a decision, effect, or user-visible transition.
- **ACTOR DECISION EFFECT TIME** — a field on the **RECEIPT** card; this shows the **ACTOR DECISION EFFECT TIME** field.
- **CHAT CLAIM** — the chat claim has NO RECEIPT.
- **NO RECEIPT** — the **NO RECEIPT** recorded by **CHAT CLAIM**.
- **VERIFIED OUTCOME** — the verified outcome has full chain.

---

## Colour and flow semantics

The course visual grammar applies directly to this diagram.

- **Cobalt platform** — A browser surface, state store, component catalog, product boundary, workspace, or learning-platform region. Here the cobalt surface under **TOOL CALL** and the surrounding workspace frames the product boundary; it tells the reader that this is a bounded product region, not an uncontrolled chat surface. It marks the product's responsibility to keep the user's workspace distinct from raw model output or runtime internals.

- **Cyan arrow** — A typed event, validated state update, user action, artifact reference, notification, or navigation path. Cyan arrows carry the flow of events, updates, and proposals from left to right, linking the typed cards and records to the reducer or next gate. When the reader sees cyan, they should expect a deliberate, validated transition rather than an accidental or hidden connection.

- **Teal arrow** — Authoritative state, accessible completion, informed consent, safe approval, preserved work, or verified recovery. The teal **VERIFIED OUTCOME** path shows the safe, authoritative, and consented route through the diagram. This color tells the reader that the product has enough evidence and authority to proceed safely.

- **Coral path** — Conflict, stale UI, unsafe rendering, deceptive state, expired approval, privacy failure, lost work, or blocked action. Coral marks the conflict, stale state, or blocked action that appears when a control is missing or bypassed. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.

- **White card** — An event, component, stage, proposal, artifact, receipt, consent record, lesson, checkpoint, or recovery option. **ARTIFACT**, **RECEIPT**, **NO RECEIPT** appear as white cards, showing that they are records, proposals, or evidence rather than raw data or system internals. The white background separates user-meaningful records from raw system logs or generated text.

The overall flow moves from the initiating actor or request, through validation and reduction, toward either the teal recovery or completion path or the coral failure path. The color of each arrow and card is a trust cue, not a decoration.

---

## How to present it

- **Start with the user moment.** Acme tells Maya that a refund exception was approved, but support can find only a successful policy lookup and no refund record. Ask the room what they need to see to feel in control. Invite someone to describe the moment before any solution appears.

- **Point at TOOL CALL and ask what it represents.** Then trace the flow from there through the next two or three elements, naming the color and direction of each arrow. Encourage them to name the incoming trigger, the visible state, and the decision the product must make.

- **Point at RESULT for step 1.** Tool Card From Typed Lifecycle And Result Events While Keeping. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at EVIDENCE for step 2.** Attach Versioned Evidence Cards With Freshness, Authority, Scope, And Selection. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at ARTIFACT for step 3.** Durable Artifact Cards Whose State And Permissions Outlive The Transient. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at RECEIPT for step 4.** Issue A Receipt Only From The Authoritative Decision Or Effect. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at EVIDENCE for step 5.** Link Cards By Explicit References Without Merging Their Different IDs. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Use the analogy.** In a workshop, the drill is the tool, the measurement sheet is evidence, the finished cabinet is the artifact, and the signed delivery note is the receipt. A photo of the drill proves none of the others. Draw the parallel to the diagram and ask what would break if the two situations were handled the same way.

- **Tell the case study.** Acme tells Maya that a refund exception was approved, but support can find only a successful policy lookup and no refund record Walk through the walkthrough and stop at the moment the old design would have failed. Pause at the step where the old design would have failed and ask how the new interface prevents it.

- **Run the lab.** Create schemas for four cards in Maya's refund flow. Give each its own ID, owner, required fields, privacy rules, lifecycle, allowed actions, retention, and cross-references. Write one false-success test for each card type. Ask pairs to present one part of the diagram and explain how the other parts reference it without merging their identities.

- **Pose the checkpoint.** Does a successful tool response prove that a business effect occurred? Let the room answer before confirming the principle. Collect answers, then confirm the principle and note any exceptions the team should watch for.

- **Close on the contract.** Tools attempt, evidence supports, artifacts persist, and receipts prove decisions or effects. Ask the team what their own product's equivalent of the contract would be.

---

## Lab and checkpoint

**Lab:** Create schemas for four cards in Maya's refund flow. Give each its own ID, owner, required fields, privacy rules, lifecycle, allowed actions, retention, and cross-references. Write one false-success test for each card type.

**Checkpoint:** Does a successful tool response prove that a business effect occurred?

**Answer:** Not necessarily. Verify authoritative state and issue a durable receipt from the effect boundary; transport success alone is insufficient.

---

## Glossary

- **Evidence card** — versioned support for a decision
- **Artifact** — durable output with lifecycle and ownership
- **Receipt** — durable proof of a decision, effect, or user-visible transition

---

## Sources

- [AG-UI events](https://docs.ag-ui.com/concepts/events)
- [MCP 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28)
- [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457)

## Related lessons

- Diagram 176
- Diagram 182
- Diagram 203 — Partial success, preserved work, and unfinished work

---