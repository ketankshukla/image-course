# Diagram 218 — Privacy controls, consent, memory settings, and deletion

![A privacy control center explains data purposes, categories, memory scopes, retention, connected apps, export, and deletion; consent is versioned and deletion propagates through primary stores, vectors, caches, logs, and backup schedules with verification.](../diagrams/218-privacy-consent-memory-settings-deletion.png)

**Module:** Agentic product operations
**Role in the course:** Give people understandable control over what an agent collects, remembers, shares, exports, and deletes across the complete data lifecycle.
**Layout:** The diagram shows DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE, with a coral risk path.

---

## At a glance

**Give people understandable control over what an agent collects, remembers, shares, exports, and deletes across the complete data lifecycle.**

- The diagram centers on **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE** and its relationship to **GHOST MEMORY**.

- The diagram separates the tested, legitimate flow from failure paths that must fail closed.

- Maya's case: Maya turns off long-term personalization and asks Acme to forget a customer note that has already been embedded and included in a cached summary.

---

## What the diagram teaches

### 1. Decline And Delete Should Be As Understandable As Accept

Decline and delete should be as understandable as accept and save; choices must not be bundled, repeatedly nagged, hidden behind jargon, or punished with unnecessary loss of core function. The diagram makes this concrete through **DELETE**, **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE**, **BUNDLED CONSENT**. If the team skips this, ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent. This is the lesson the case study ends with: Privacy control is enforceable data lineage: specific purpose, visible scope, revocation, propagated deletion, and verification.

### 2. Inventory Every Collected Field, Derived Value, Memory Item, Embedding, Artifact

This step asks the team to inventory every collected field, derived value, memory item, embedding, artifact, log, provider, purpose, retention, and recipient. The diagram shows this through **PURPOSE**, **RETENTION**, **LOG**, which make the abstract step visible and testable. Session context, project facts, personal preferences, retrieved documents, summaries, embeddings, logs, and provider records are different stores with different purposes and risks. Memory controls should show the remembered item, source, purpose, scope, creation and last-use dates, expiry, who can use it, and a way to edit, forget, or pause future use. If the team skips this, ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent. Maya's case makes this concrete: Maya turns off long-term personalization and asks Acme to forget a customer note that has already been embedded and included in a cached summary.

### 3. Separate Necessary Processing From Optional Purposes And Capture Versioned, Revocable

Here the product must separate necessary processing from optional purposes and capture versioned, revocable consent receipts for each optional category. In the drawing, **CONSENT RECEIPT**, **PURPOSE**, **BUNDLED CONSENT** carry this responsibility. Consent must be specific enough to choose. Separate what is necessary to complete the current request from optional long-term memory, product analytics, model improvement, third-party sharing, notifications, and device synchronization. Without this step, ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent. The result — Maya's choice changes actual memory behavior across the system instead of merely changing a toggle label. — depends on getting this right.
![User outcomes connect to minimized product events, feedback, quality evaluation, safety review, and accessibility evidence; every metric exposes its definition and denominator, while experiments require consent, risk review, fair allocation, stop rules, guardrails, and debriefing.](../diagrams/219-analytics-feedback-evaluation-experiment-ethics.png)

Diagram 219 — *Product analytics, feedback, evaluation, and experiment ethics* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 4. Expose Memory And Connected-app Controls Using The Same Identities

The diagram enforces this by showing the team how to expose memory and connected-app controls using the same identities and scopes enforced by write and retrieval paths. The visual anchors are **MEMORY OFF SESSION PROJECT LONG TERM**, **CONNECTED APPS**, **GHOST MEMORY**; without them the step would be invisible to the user. An off switch must affect retrieval and new writes, not merely hide the settings page. Data controls must resist dark patterns. The case study shows the risk: ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent. This is the lesson the case study ends with: Privacy control is enforceable data lineage: specific purpose, visible scope, revocation, propagated deletion, and verification.

### 5. Orchestrate Export And Deletion Across All Derived Stores With Idempotent

This is the discipline that makes the product orchestrate export and deletion across all derived stores with idempotent steps, retry, exception reasons, and visible progress. This idea sits on **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE** and reaches the rest of the diagram through **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE**, **DELETION FAN OUT**. Deletion is a workflow. The product needs a propagation map, exceptions, time bounds, retry, failure handling, and a verifiable status. Missing this is how products end up with ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent. In the walkthrough, The control center identifies the source note, memory scope, embedding index, cached summary, retention, and downstream provider status..

### 6. Verify That Deleted Or Disabled Data No Longer Appears

The team must verify that deleted or disabled data no longer appears in retrieval, personalization, search, sync, notifications, analytics, or future agent context before the interface can be trustworthy. The diagram shows this through **DELETE**, **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE**, **DATA CATEGORIES**, which make the abstract step visible and testable. Agent memory is a product data feature, not a magical property of the model. Primary records may feed object storage, vector indexes, caches, search, analytics, audit logs, downstream processors, and backups. A system that ignores this will eventually face ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent. The danger the case warns about, Maya turns off long-term personalization and asks Acme to forget a customer note that has already been embedded and included in a cached summary. should make this clear.

### 7. The standard in practice

The lesson is not a perfect prototype; it is a product contract. Give people understandable control over what an agent collects, remembers, shares, exports, and deletes across the complete data lifecycle.. The diagram makes that contract visible through **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE**, **USER CONTROL CENTER**, **PURPOSE**, so the team can argue about the contract before choosing a framework. The contract is not framework-specific; it is the set of observable promises the product makes to the person using it. Maya's case warns that ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent. The practical standard is this: Privacy control is enforceable data lineage: specific purpose, visible scope, revocation, propagated deletion, and verification.

### 8. The Next.js and Python surfaces

The same contract appears in both stacks, but the boundary moves with the architecture.
**In Next.js / React:**
- Build one privacy center with server-rendered current settings, granular forms, clear consequences, accessible confirmations, export progress, and a durable deletion status page.
- Do not put raw memory or consent decisions in unsigned client storage as authority; revalidate scope, policy version, and user identity on the server.
- Render provenance and last-use information for memory items, and provide edit, forget, pause, export, and revoke controls without relying on prechecked boxes or asymmetric button styling.
- Keep the most sensitive payloads and policy decisions on the server and stream only user-visible, safe view models to client components.
**In Python / FastAPI:**
- Model consent as immutable versioned grants and revocations scoped to purpose, data categories, recipient, subject, product, policy version, and expiry.
- Centralize memory retrieval behind a policy check and write a deletion saga covering source rows, documents, embeddings, caches, indexes, providers, and scheduled backup expiry.
- Produce a user-facing completion receipt and internal exception evidence, then run retrieval probes that prove deleted items no longer influence answers.
- Treat every framework callback or protocol event as raw input; validate and transform it into the product's own event vocabulary before it reaches the reducer or domain model.
Both implementations must avoid the same trap: ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent.

### 9. Analogy

A labeled filing cabinet tells you which drawer holds what, why it is kept, and who has a key. Shredding the index card while photocopies remain in five rooms is not deletion. The analogy keeps the lesson grounded. The diagram's **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE** plays the same role as the central object in the analogy: it must be visible, labeled, and trustworthy without the user having to infer meaning from a long narrative. The parallel works because both situations require separating the object from the record, the attempt from the proof, and the promise from the evidence.

---

## Case study — Maya

Maya turns off long-term personalization and asks Acme to forget a customer note that has already been embedded and included in a cached summary.

### The walkthrough

1. The control center identifies the source note, memory scope, embedding index, cached summary, retention, and downstream provider status.
2. Acme immediately blocks the item from new retrieval and starts an idempotent deletion workflow across primary and derived stores.
3. A failed cache purge retries without reopening access, while the interface reports partial completion and the affected system.
4. Verification probes confirm that future searches and agent context exclude the note; the receipt explains the backup-expiry schedule and any narrowly retained audit record.

### The result

Maya's choice changes actual memory behavior across the system instead of merely changing a toggle label.

### The danger

Ghost memory appears when a source record is deleted but embeddings, caches, summaries, provider data, or copied artifacts continue influencing the agent.

### The takeaway

Privacy control is enforceable data lineage: specific purpose, visible scope, revocation, propagated deletion, and verification.

---

## Composition

The picture is a single-view explainer for *Privacy controls, consent, memory settings, and deletion*. On the left, the diagram shows DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE. At the top, uSER CONTROL CENTER has PURPOSE, DATA CATEGORIES, MEMORY OFF SESSION PROJECT LONG TERM, RETENTION, CONNECTED APPS, DOWNLOAD, DELETE. In the center, cONSENT RECEIPT versions policy. To the right, dELETION FAN OUT to PRIMARY, VECTOR, CACHE, LOG, BACKUP SCHEDULE with VERIFICATION. Across the middle, coral DARK PATTERN, BUNDLED CONSENT, GHOST MEMORY. The eye travels from **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE** through the central flow to **GHOST MEMORY**, with the contrast between coral risk paths and teal recovery paths giving the reader the core message at a glance.

## Element by element

- **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE** — the data lifecycle collect use store share remember export delete ..
- **USER CONTROL CENTER** — the interface where a person reviews data purpose, categories, memory, and deletion.
- **PURPOSE** — one of the items named by **USER CONTROL CENTER**; this is the **PURPOSE** item.
- **DATA CATEGORIES** — one of the items named by **USER CONTROL CENTER**; this is the **DATA CATEGORIES** item.
- **MEMORY OFF SESSION PROJECT LONG TERM** — one of the items named by **USER CONTROL CENTER**; this is the **MEMORY OFF SESSION PROJECT LONG TERM** item.
- **RETENTION** — one of the items named by **USER CONTROL CENTER**; this is the **RETENTION** item.
- **CONNECTED APPS** — one of the items named by **USER CONTROL CENTER**; this is the **CONNECTED APPS** item.
- **DOWNLOAD** — one of the items named by **USER CONTROL CENTER**; this is the **DOWNLOAD** item.
- **DELETE** — the delete DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE.
- **CONSENT RECEIPT** — the versioned record of a specific informed privacy choice.
- **DELETION FAN OUT** — the workflow that propagates deletion through primary, vector, cache, log, and backup stores.
- **PRIMARY** — one of the items named by **DELETION FAN OUT**; this is the **PRIMARY** item.
- **VECTOR** — one of the items named by **DELETION FAN OUT**; this is the **VECTOR** item.
- **CACHE** — one of the items named by **DELETION FAN OUT**; this is the **CACHE** item.
- **LOG** — one of the items named by **DELETION FAN OUT**; this is the **LOG** item.
- **BACKUP SCHEDULE** — one of the items named by **DELETION FAN OUT**; this is the **BACKUP SCHEDULE** item.
- **VERIFICATION** — the proof that deleted data no longer influences retrieval or outputs.
- **DARK PATTERN** — the dark pattern BUNDLED CONSENT, GHOST MEMORY..
- **BUNDLED CONSENT** — the bundled consent DARK PATTERN, BUNDLED CONSENT, GHOST MEMORY..
- **GHOST MEMORY** — the ghost memory DARK PATTERN, BUNDLED CONSENT, GHOST MEMORY..

---

## Colour and flow semantics

The course visual grammar applies directly to this diagram.

- **Cobalt platform** — A browser surface, state store, component catalog, product boundary, workspace, or learning-platform region. Here the cobalt surface under **DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE** and the surrounding workspace frames the product boundary; it tells the reader that this is a bounded product region, not an uncontrolled chat surface. It marks the product's responsibility to keep the user's workspace distinct from raw model output or runtime internals.

- **Cyan arrow** — A typed event, validated state update, user action, artifact reference, notification, or navigation path. Cyan arrows carry the flow of events, updates, and proposals from left to right, linking the typed cards and records to the reducer or next gate. When the reader sees cyan, they should expect a deliberate, validated transition rather than an accidental or hidden connection.

- **Teal arrow** — Authoritative state, accessible completion, informed consent, safe approval, preserved work, or verified recovery. Teal marks the authoritative and safe path, such as the committed receipt or restored state, distinguishing it from the raw request. This color tells the reader that the product has enough evidence and authority to proceed safely.

- **Coral path** — Conflict, stale UI, unsafe rendering, deceptive state, expired approval, privacy failure, lost work, or blocked action. Coral marks the conflict, stale state, or blocked action that appears when a control is missing or bypassed. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.

- **White card** — An event, component, stage, proposal, artifact, receipt, consent record, lesson, checkpoint, or recovery option. **CONSENT RECEIPT** appear as white cards, showing that they are records, proposals, or evidence rather than raw data or system internals. The white background separates user-meaningful records from raw system logs or generated text.

The overall flow moves from the initiating actor or request, through validation and reduction, toward either the teal recovery or completion path or the coral failure path. The color of each arrow and card is a trust cue, not a decoration.

---

## How to present it

- **Start with the user moment.** Maya turns off long-term personalization and asks Acme to forget a customer note that has already been embedded and included in a cached summary. Ask the room what they need to see to feel in control. Invite someone to describe the moment before any solution appears.

- **Point at DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE and ask what it represents.** Then trace the flow from there through the next two or three elements, naming the color and direction of each arrow. Encourage them to name the incoming trigger, the visible state, and the decision the product must make.

- **Point at PURPOSE for step 1.** Inventory Every Collected Field, Derived Value, Memory Item, Embedding, Artifact. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at CONSENT RECEIPT for step 2.** Separate Necessary Processing From Optional Purposes And Capture Versioned, Revocable. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at MEMORY OFF SESSION PROJECT LONG TERM for step 3.** Expose Memory And Connected-app Controls Using The Same Identities. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE for step 4.** Orchestrate Export And Deletion Across All Derived Stores With Idempotent. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at DELETE for step 5.** Verify That Deleted Or Disabled Data No Longer Appears. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Use the analogy.** A labeled filing cabinet tells you which drawer holds what, why it is kept, and who has a key. Shredding the index card while photocopies remain in five rooms is not deletion. Draw the parallel to the diagram and ask what would break if the two situations were handled the same way.

- **Tell the case study.** Maya turns off long-term personalization and asks Acme to forget a customer note that has already been embedded and included in a cached summary Walk through the walkthrough and stop at the moment the old design would have failed. Pause at the step where the old design would have failed and ask how the new interface prevents it.

- **Run the lab.** Draw a data inventory and lineage map for one agent conversation through prompts, messages, artifacts, memory, vectors, logs, analytics, providers, exports, and backups. Specify consent, retention, access, revocation, deletion steps, failure recovery, exceptions, completion receipt, and five proof probes. Ask pairs to present one part of the diagram and explain how the other parts reference it without merging their identities.

- **Pose the checkpoint.** Is deleting the primary database row enough to say an agent has forgotten the information? Let the room answer before confirming the principle. Collect answers, then confirm the principle and note any exceptions the team should watch for.

- **Close on the contract.** Privacy control is enforceable data lineage: specific purpose, visible scope, revocation, propagated deletion, and verification. Ask the team what their own product's equivalent of the contract would be.

---

## Lab and checkpoint

**Lab:** Draw a data inventory and lineage map for one agent conversation through prompts, messages, artifacts, memory, vectors, logs, analytics, providers, exports, and backups. Specify consent, retention, access, revocation, deletion steps, failure recovery, exceptions, completion receipt, and five proof probes.

**Checkpoint:** Is deleting the primary database row enough to say an agent has forgotten the information?

**Answer:** No. Derived embeddings, caches, summaries, indexes, copied artifacts, provider records, analytics, and backups must follow a documented deletion or expiry policy, and retrieval behavior should be verified.

---

## Glossary

- **Purpose limitation** — using data only for the stated allowed reason
- **Consent receipt** — versioned record of a specific informed choice
- **Ghost memory** — deleted source data that survives in a derived or downstream store

---

## Sources

- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [MCP Apps stable specification](https://apps.extensions.modelcontextprotocol.io/)

## Related lessons

- Diagram 211 — Frontend tool calls and user-device actions
- Diagram 212 — Interface security, data exposure, and safe rendering
- Diagram 219 — Product analytics, feedback, evaluation, and experiment ethics

---