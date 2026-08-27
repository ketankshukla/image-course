# Diagram 197 — The event-driven interface mental model

![An agent run emits typed lifecycle, text, tool, activity, state, artifact, approval, and error events that a reducer maps into dedicated interface regions instead of parsing prose.](../diagrams/197-event-driven-interface-mental-model.png)

**Module:** Event-driven agent interfaces
**Role in the course:** Explain why an agent interface should render typed events and explicit state rather than guess meaning from chat text.
**Layout:** The diagram shows AGENT RUN emitting typed cards RUN, TEXT, TOOL, ACTIVITY, STATE, ARTIFACT, APPROVAL, ERROR into an EVENT STREAM, with a coral risk path, and a teal safe path.

---

## At a glance

**Explain why an agent interface should render typed events and explicit state rather than guess meaning from chat text.**

- The diagram centers on **AGENT RUN** and its relationship to **EXPLAINABLE UI**.

- The teal **TYPED EVENT** path shows the safe, authoritative, or consented route.

- The coral **PARSE PROSE** path shows the risk the product must prevent.

- Maya's case: Maya asks for a refund-policy review. The old interface shows a typing bubble for twenty seconds and then suddenly presents a final paragraph.

---

## What the diagram teaches

### 1. Agent Interface Is Not Merely A Chat Box With Animated

An agent interface is not merely a chat box with animated text. It is a projection of a running product state into controls and evidence a person can understand. AG-UI models communication as typed events such as run lifecycle, message streams, tool calls, activities, snapshots, deltas, and errors. The diagram makes this concrete through **TEXT**, **CHAT**, **AGENT RUN**. If the team skips this, parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar. This is the lesson the case study ends with: Events describe what happened; reducers decide product state; components explain that state to a person.
![A versioned authoritative snapshot is reduced with ordered JSON Patch deltas; out-of-order, stale-base, and invalid-path updates cause conflict and trigger a fresh snapshot.](../diagrams/198-snapshots-deltas-reducers-conflicts.png)

Diagram 198 — *State snapshots, deltas, reducers, and conflict handling* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 2. Interface Must Not Inspect A Sentence For Phrases

The interface must not inspect a sentence for phrases such as 'I am searching' or 'approval needed' and then invent business state. Wording changes across models, languages, and prompts, while typed state can be tested and replayed. Do not display private chain-of-thought as progress. This is visible in the drawing as **STATE**, **APPROVAL**. Without this step, parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar. In the walkthrough, The new interface receives RUN_STARTED and creates a named review workspace instead of a generic spinner..

### 3. User-visible Outcome And The Interface Regions That Help The Person

This step asks the team to name the user-visible outcome and the interface regions that help the person understand or control it. The diagram shows this through **AGENT RUN**, **RUN**, **TEXT**, which make the abstract step visible and testable. An agent interface is not merely a chat box with animated text. It is a projection of a running product state into controls and evidence a person can understand. If the team skips this, parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar. Maya's case makes this concrete: Maya asks for a refund-policy review. The old interface shows a typing bubble for twenty seconds and then suddenly presents a final paragraph.

### 4. Supported AG-UI Or Product Event To One Validated Internal Event

Here the product must map each supported AG-UI or product event to one validated internal event type with stable identifiers. In the drawing, **EVENT STREAM**, **WRONG UI**, **TYPED EVENT** carry this responsibility. AG-UI models communication as typed events such as run lifecycle, message streams, tool calls, activities, snapshots, deltas, and errors. The event type says what happened; stable identifiers say which run, message, tool, or activity it belongs to. Without this step, parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar. The result — Maya can see what is happening, what evidence exists, and where control is required without seeing private reasoning or reading a machine diary. — depends on getting this right.

### 5. Reduce Events Into Explicit Chat, Progress, Tool, Artifact, Approval

The diagram enforces this by showing the team how to reduce events into explicit chat, progress, tool, artifact, approval, and recovery state. The visual anchors are **TOOL**, **STATE**, **ARTIFACT**; without them the step would be invisible to the user. Text belongs in the conversation, progress belongs in a stage view, proposals belong in approval cards, and durable outputs belong in artifact views. The interface must not inspect a sentence for phrases such as 'I am searching' or 'approval needed' and then invent business state. The case study shows the risk: parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar. This is the lesson the case study ends with: Events describe what happened; reducers decide product state; components explain that state to a person.

### 6. Unknown, Late, Duplicate, Or Invalid Events As Bounded Diagnostics Rather

This is the discipline that makes the product render unknown, late, duplicate, or invalid events as bounded diagnostics rather than corrupting visible state. This idea sits on **STATE** and reaches the rest of the diagram through **STATE**. Missing this is how products end up with parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar. In the walkthrough, The new interface receives RUN_STARTED and creates a named review workspace instead of a generic spinner..

### 7. Same Event Recording By Replaying It Into An Empty Interface

The team must test the same event recording by replaying it into an empty interface and comparing the reconstructed outcome before the interface can be trustworthy. The diagram shows this through **EVENT STREAM**, **TYPED EVENT**, which make the abstract step visible and testable. A system that ignores this will eventually face parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar. The danger the case warns about, Maya asks for a refund-policy review. The old interface shows a typing bubble for twenty seconds and then suddenly presents a final paragraph. should make this clear.

### 8. The standard in practice

The lesson is not a perfect prototype; it is a product contract. Explain why an agent interface should render typed events and explicit state rather than guess meaning from chat text.. The diagram makes that contract visible through **AGENT RUN**, **RUN**, **TEXT**, so the team can argue about the contract before choosing a framework. The contract is not framework-specific; it is the set of observable promises the product makes to the person using it. Maya's case warns that parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar. The practical standard is this: Events describe what happened; reducers decide product state; components explain that state to a person.

### 9. The Next.js and Python surfaces

The same contract appears in both stacks, but the boundary moves with the architecture.
**In Next.js / React:**
- Define a discriminated TypeScript event union at the server boundary, validate every payload, and convert protocol events into product events before React sees them.
- Use a reducer or external store keyed by run, message, activity, tool, and artifact IDs; render dedicated components rather than one component with dozens of string checks.
- Stream only deliberate user-facing state to client components; keep credentials, private prompts, hidden reasoning, and privileged policy evidence on the server.
- Keep the most sensitive payloads and policy decisions on the server and stream only user-visible, safe view models to client components.
**In Python / FastAPI:**
- Represent incoming AG-UI and internal events as Pydantic models with a discriminator, version, identifiers, timestamp, and bounded payload.
- Create one adapter per agent runtime so FastAPI emits the same product event vocabulary regardless of framework-specific callback names.
- Persist an append-only synthetic event fixture for replay tests while storing authoritative business records separately from transient UI events.
- Treat every framework callback or protocol event as raw input; validate and transform it into the product's own event vocabulary before it reaches the reducer or domain model.
Both implementations must avoid the same trap: parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar.

### 10. Analogy

A railway station has separate boards for arrivals, platform changes, cancellations, and safety messages. Staff do not hide every condition inside one long announcement and ask passengers to infer the timetable. The analogy keeps the lesson grounded. The diagram's **AGENT RUN** plays the same role as the central object in the analogy: it must be visible, labeled, and trustworthy without the user having to infer meaning from a long narrative. The parallel works because both situations require separating the object from the record, the attempt from the proof, and the promise from the evidence.

---

## Case study — Maya

Maya asks for a refund-policy review. The old interface shows a typing bubble for twenty seconds and then suddenly presents a final paragraph.

### The walkthrough

1. The new interface receives RUN_STARTED and creates a named review workspace instead of a generic spinner.
2. ACTIVITY and TOOL events update research and policy stages with user-safe labels and evidence counts.
3. An approval proposal becomes a separate card bound to the refund action, not a sentence buried in chat.
4. RUN_FINISHED closes progress, links the final artifact, and leaves the event receipt available for support.

### The result

Maya can see what is happening, what evidence exists, and where control is required without seeing private reasoning or reading a machine diary.

### The danger

Parsing model prose into state can show an approval as complete, hide a failed tool, or expose invented progress simply because the wording looked familiar.

### The takeaway

Events describe what happened; reducers decide product state; components explain that state to a person.

---

## Composition

The picture is a single-view explainer for *The event-driven interface mental model*. On the left, the diagram shows AGENT RUN emitting typed cards RUN, TEXT, TOOL, ACTIVITY, STATE, ARTIFACT, APPROVAL, ERROR into an EVENT STREAM. At the top, a validated REDUCER updates separate CHAT, PROGRESS, TOOL, ARTIFACT, APPROVAL panels. In the center, the diagram also includes a coral PARSE PROSE path to WRONG UI and a teal TYPED EVENT path to EXPLAINABLE UI. The eye travels from **AGENT RUN** through the central flow to **EXPLAINABLE UI**, with the contrast between coral risk paths and teal recovery paths giving the reader the core message at a glance.

## Element by element

- **AGENT RUN** — the running agent process that emits typed lifecycle, text, tool, activity, state, artifact, approval, and error events.
- **RUN** — one of the cards named by **AGENT RUN**; this is the **RUN** card.
- **TEXT** — one of the cards named by **AGENT RUN**; this is the **TEXT** card.
- **TOOL** — one of the cards named by **AGENT RUN**; this is the **TOOL** card.
- **ACTIVITY** — one of the cards named by **AGENT RUN**; this is the **ACTIVITY** card.
- **STATE** — one of the cards named by **AGENT RUN**; this is the **STATE** card.
- **ARTIFACT** — a durable output that outlives the run, such as a file, summary, or recommendation.
- **APPROVAL** — one of the cards named by **AGENT RUN**; this is the **APPROVAL** card.
- **ERROR** — one of the cards named by **AGENT RUN**; this is the **ERROR** card.
- **EVENT STREAM** — the ordered channel that carries typed events from the agent run toward the interface reducer.
- **REDUCER** — the validated function that turns events and prior state into new product state without parsing prose.
- **CHAT** — one of the panels named by **REDUCER**; this is the **CHAT** panel.
- **PROGRESS** — the honest, observable state of the running task.
- **PARSE PROSE** — the parse prose path that leads to **WRONG UI and a teal TYPED EVENT path to EXPLAINABLE UI**.
- **WRONG UI** — one of the paths named by **PARSE PROSE**; this is the **WRONG UI** path.
- **TYPED EVENT** — one of the paths named by **PARSE PROSE**; this is the **TYPED EVENT** path.
- **EXPLAINABLE UI** — one of the paths named by **PARSE PROSE**; this is the **EXPLAINABLE UI** path.

---

## Colour and flow semantics

The course visual grammar applies directly to this diagram.

- **Cobalt platform** — A browser surface, state store, component catalog, product boundary, workspace, or learning-platform region. Here the cobalt surface under **AGENT RUN** and the surrounding workspace frames the product boundary; it tells the reader that this is a bounded product region, not an uncontrolled chat surface. It marks the product's responsibility to keep the user's workspace distinct from raw model output or runtime internals.

- **Cyan arrow** — A typed event, validated state update, user action, artifact reference, notification, or navigation path. Cyan arrows carry the flow of events, updates, and proposals from left to right, linking the typed cards and records to the reducer or next gate. When the reader sees cyan, they should expect a deliberate, validated transition rather than an accidental or hidden connection.

- **Teal arrow** — Authoritative state, accessible completion, informed consent, safe approval, preserved work, or verified recovery. The teal **TYPED EVENT** path shows the safe, authoritative, and consented route through the diagram. This color tells the reader that the product has enough evidence and authority to proceed safely.

- **Coral path** — Conflict, stale UI, unsafe rendering, deceptive state, expired approval, privacy failure, lost work, or blocked action. The coral **PARSE PROSE** path shows the risk, conflict, or blocked outcome the product must prevent. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.

- **White card** — An event, component, stage, proposal, artifact, receipt, consent record, lesson, checkpoint, or recovery option. **ARTIFACT**, **EVENT STREAM**, **TYPED EVENT** appear as white cards, showing that they are records, proposals, or evidence rather than raw data or system internals. The white background separates user-meaningful records from raw system logs or generated text.

The overall flow moves from the initiating actor or request, through validation and reduction, toward either the teal recovery or completion path or the coral failure path. The color of each arrow and card is a trust cue, not a decoration.

---

## How to present it

- **Start with the user moment.** Maya asks for a refund-policy review. Ask the room what they need to see to feel in control. Invite someone to describe the moment before any solution appears.

- **Point at AGENT RUN and ask what it represents.** Then trace the flow from there through the next two or three elements, naming the color and direction of each arrow. Encourage them to name the incoming trigger, the visible state, and the decision the product must make.

- **Point at AGENT RUN for step 1.** User-visible Outcome And The Interface Regions That Help The Person. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at EVENT STREAM for step 2.** Supported AG-UI Or Product Event To One Validated Internal Event. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at TOOL for step 3.** Reduce Events Into Explicit Chat, Progress, Tool, Artifact, Approval. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at STATE for step 4.** Unknown, Late, Duplicate, Or Invalid Events As Bounded Diagnostics Rather. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at EVENT STREAM for step 5.** Same Event Recording By Replaying It Into An Empty Interface. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Use the analogy.** A railway station has separate boards for arrivals, platform changes, cancellations, and safety messages. Staff do not hide every condition inside one long announcement and ask passengers to infer the timetable. Draw the parallel to the diagram and ask what would break if the two situations were handled the same way.

- **Tell the case study.** Maya asks for a refund-policy review Walk through the walkthrough and stop at the moment the old design would have failed. Pause at the step where the old design would have failed and ask how the new interface prevents it.

- **Run the lab.** Design a twelve-event recording for Maya's policy review. Include lifecycle, text, activity, tool, artifact, approval, and error events. For each event, name its stable ID, schema owner, visible component, privacy classification, and invalid-event behavior. Ask pairs to present one part of the diagram and explain how the other parts reference it without merging their identities.

- **Pose the checkpoint.** Should a frontend infer that a tool succeeded because the assistant says 'Done'? Let the room answer before confirming the principle. Collect answers, then confirm the principle and note any exceptions the team should watch for.

- **Close on the contract.** Events describe what happened; reducers decide product state; components explain that state to a person. Ask the team what their own product's equivalent of the contract would be.

---

## Lab and checkpoint

**Lab:** Design a twelve-event recording for Maya's policy review. Include lifecycle, text, activity, tool, artifact, approval, and error events. For each event, name its stable ID, schema owner, visible component, privacy classification, and invalid-event behavior.

**Checkpoint:** Should a frontend infer that a tool succeeded because the assistant says 'Done'?

**Answer:** No. A typed tool result and authoritative business receipt must establish success. The sentence may explain the result, but it is not the state transition.

---

## Glossary

- **Typed event** — schema-validated record with a named meaning
- **Reducer** — function that turns an event and prior state into new state
- **Projection** — user-facing view derived from underlying records

---

## Sources

- [AG-UI overview](https://docs.ag-ui.com/)
- [AG-UI events](https://docs.ag-ui.com/concepts/events)
- [AG-UI architecture](https://docs.ag-ui.com/concepts/architecture)

## Related lessons

- Diagram 198 — State snapshots, deltas, reducers, and conflict handling
- Diagram 201 — Progressive disclosure and observable stage labels
- Diagram 205 — Interrupt, input request, approval, rejection, and expiry

---