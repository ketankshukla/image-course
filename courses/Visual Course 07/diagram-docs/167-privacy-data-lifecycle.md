# Diagram 167 — Data Minimization, Retention, Consent, and Deletion

![On a dark canvas, a PERSONAL DATA card enters a PURPOSE GATE and a MINIMIZE gate. Approved fields flow through USE, STORE, SHARE, RETAIN, DELETE, and VERIFY DELETION. Each data card carries TENANT, PURPOSE, CONSENT or LEGAL BASIS, CLASS, OWNER, and RETENTION labels. Coral blocked paths show EXTRA FIELDS, PURPOSE DRIFT, FOREVER MEMORY, and SHADOW COPY being denied. A DELETION RECEIPT crosses DATABASE, VECTOR, CACHE, ARTIFACT, and LOG stores at the bottom of the diagram.](../diagrams/167-privacy-data-lifecycle.png)

**Diagram number:** 167  
**Slug:** `privacy-data-lifecycle`  
**Module ID:** `module-39`  
**Module:** Supply chain, privacy, and audit evidence  
**Stability:** Privacy engineering foundation  
**Role in the course:** how to design the full personal-data lifecycle instead of treating privacy as a checkbox on collection  
**Layout:** a personal-data card enters purpose and minimization gates, then flows through use, store, share, retain, delete, and verified-deletion stages, with blocked coral paths for extra fields, purpose drift, forever memory, and shadow copies, and a deletion receipt across database, vector, cache, artifact, and log stores

---

## At a glance

**PERSONAL DATA → PURPOSE GATE → MINIMIZE → USE → STORE → SHARE → RETAIN → DELETE → VERIFY DELETION**.

Each data card carries **TENANT, PURPOSE, CONSENT or LEGAL BASIS, CLASS, OWNER, and RETENTION**.

The diagram blocks four coral risks: **EXTRA FIELDS, PURPOSE DRIFT, FOREVER MEMORY, and SHADOW COPY**.

The final step is a **DELETION RECEIPT** that covers **DATABASE, VECTOR, CACHE, ARTIFACT, and LOG** stores.

This is the library-book view of privacy engineering: borrow only the books needed for one assignment, record why and when they are due, and return every copy instead of filling a permanent storeroom.

---

## What the diagram teaches

### 1. Privacy is a lifecycle, not a collection notice

The diagram starts with **PERSONAL DATA** and follows it through use, storage, sharing, retention, and deletion. The most dangerous privacy mistakes happen after collection. A field can be copied into a model prompt, embedded into a vector index, cached as an answer, written to a log, or retained by a processor long after the original row is gone.

The lifecycle must answer: what is the minimum data, why is it needed, who can use it, where it may go, how long it stays, and how it is removed from every derived copy. A privacy notice that cannot be enforced at each stage is a promise the system will break.

### 2. The purpose gate decides whether the data is allowed to enter

The first control is the **PURPOSE GATE**. Before personal data is used, it must have a named purpose tied to a business process, a legal basis, and a set of allowed operations. Data collected for refund fraud investigation may not be used for marketing, model training, or performance reviews unless a separate lawful basis exists. Without the purpose gate, an agent that can read a case can silently turn customer service into data mining.

### 3. Minimization removes fields before they reach the model, tool, or log

The second control is **MINIMIZE**. After purpose is confirmed, the system removes fields the next step does not need. A refund tool needs a case ID and an amount. A model prompt needs only the facts required to answer the question.

Minimization is not the same as redaction. Redaction hides a sensitive field that is still needed. Minimization removes the field entirely. The safest data is the data never collected, never placed in context, and never written to a log. The trace in the course begins: *"Remove unnecessary fields before model context, retrieval, tools, logs, or sharing."*

### 4. Every data card carries a six-field label

The diagram shows each data card carrying **TENANT, PURPOSE, CONSENT or LEGAL BASIS, CLASS, OWNER, and RETENTION**.

- **TENANT** — the customer organization that owns the record.
- **PURPOSE** — the reason it is being processed.
- **CONSENT or LEGAL BASIS** — what authorizes the processing.
- **CLASS** — how sensitive it is and which controls apply.
- **OWNER** — who is accountable for the record and its retention.
- **RETENTION** — when it must be deleted.

This contract must travel with the data through every copy. If the data is embedded, cached, logged, or shared, the contract must travel with it or the copy is invalid.

### 5. Use, store, share, and retain are separate policy decisions

The diagram separates **USE, STORE, SHARE, and RETAIN** into distinct stages. A single access-control checkbox cannot answer all four. A role may use a field for support but not store it in a vector database. A processor may receive a redacted export but not the original. The diagram forces the team to ask the question for each stage.

### 6. Consent is one legal basis, not the only one

The data card says **CONSENT or LEGAL BASIS** because consent is not always the required or best basis. The correct basis depends on jurisdiction and purpose. The engineering job is to **represent the approved basis and enforce its constraints accurately**.

An agent system mixes many purposes: customer service, fraud prevention, product improvement, legal hold, and model training. A field with "consent for support" cannot be reused for training. A field under "legal hold" cannot be deleted until the hold is released. The policy engine must know the basis to know the rule.

### 7. The four blocked paths are the most common privacy failures

The diagram marks four coral risks: **EXTRA FIELDS, PURPOSE DRIFT, FOREVER MEMORY, and SHADOW COPY**.

- **EXTRA FIELDS** — data collected beyond the minimum necessary.
- **PURPOSE DRIFT** — use of data beyond the original basis.
- **FOREVER MEMORY** — data retained in model context, cache, or vector index past its retention.
- **SHADOW COPY** — a derived or backup copy that survives primary deletion.

These patterns make privacy promises empty. A customer deletes an account, but the embeddings, logs, and backup files remain. The blocked paths are the controls that make the lifecycle real.

![On a dark canvas, sensitive data enters a data classifier, then splits into a teal safe-read lane toward an approved Acme resource and a coral exfiltration lane toward an attacker destination. The exfiltration lane tries model output, URL query, tool argument, log, and artifact paths, but egress policy and DLP block them. A separate side-effect lane shows policy, bound approval, and a receipt before any real-world effect is allowed.](../diagrams/152-exfiltration-side-effect-control.png)

Diagram 152 — Data Exfiltration and Unsafe Side Effects shows the upstream controls that prevent personal data from leaving through the wrong channels. That diagram classifies, minimizes, and redacts data before it reaches model output, URL queries, tool arguments, logs, or artifacts. This diagram adds the lifecycle view: even when data is used safely, it still needs purpose, retention, consent, and a deletion route.

### 8. Deletion must be orchestrated, not just a SQL query

The diagram ends with **DELETE** and **VERIFY DELETION**. Deleting the primary database row is not enough. A personal-data record is also in the vector index, the cache, the model memory, the artifact store, the log sink, and the third-party processor. Each store must be reached by the deletion workflow and must return a status.

The verification step turns deletion into a trustworthy operation. A receipt that only says "row deleted" while embeddings and logs survive is a false promise. The deletion receipt crosses database, vector, cache, artifact, and log stores so the user can verify the full scope.

### 9. The Next.js map builds a server-side data and deletion interface

The Next.js guidance is to **provide a clear data-use and deletion interface backed by server-side inventory, export, consent or preference, retention, and deletion-workflow APIs.** The browser can display the user's data state and deletion options, but the inventory, consent records, and deletion jobs must run in authenticated server code.

Keep tokens, policy decisions, secrets, and privileged mutations in server code; send the browser only the minimum display state. Use typed request, decision, denial, approval, and receipt records so the React interface can explain security state without inventing it.

### 10. The Python map defines a data class registry and a deletion orchestrator

The Python guidance is to **define a `DataClass` registry and a deletion orchestrator with adapters for relational data, vectors, caches, blobs, memories, logs, and processors.** This is the engineering that makes the diagram executable.

Use Pydantic models plus explicit middleware or service boundaries for identity, tenant, policy, data classification, and audit context. Test allow and deny paths with hostile synthetic fixtures and dependency-injected identity, policy, storage, secret, and network adapters. A test can verify that a deletion request removes the row, embeddings, cache entries, and artifacts while preserving the minimum audit evidence required by legal hold.

### 11. The trace and the lab turn the diagram into an inventory

The course trace is a five-step recipe:

1. Inventory personal data and derived data by field, source, tenant, purpose, and classification.
2. Remove unnecessary fields before model context, retrieval, tools, logs, or sharing.
3. Record the relevant consent or other approved legal basis and purpose constraints.
4. Apply retention and access policy consistently to source and derived copies.
5. Orchestrate deletion across stores and produce a receipt listing completed, pending, exempt, and failed targets.

The course lab asks the room to **build a data inventory for the Acme case with twelve fields**, including purpose, basis, classification, prompt use, storage, recipients, retention, deletion targets, exception, and evidence. This inventory becomes the policy table that drives the purpose gate, minimization, retention, and deletion. When a new model, cache, or processor is added, the inventory must be updated. If a field cannot be mapped to an inventory row, it should not be collected.

### 12. The final contract: identify, authorize, constrain, and preserve evidence

At the bottom of the lifecycle is the same security contract that runs through the whole course: **verify the relevant identity and tenant, evaluate narrow authority against the current context, constrain data and destinations, and preserve enough evidence to explain both allowed and denied outcomes.**

The privacy version says: collect only what you need, for a named purpose, under the right legal basis, with an owner and a retention rule, and delete every copy when the rule says so. If a stage cannot produce evidence that it did this, it is not governed.

---

## Case study — Maya asks for deletion after the refund investigation

### Situation

Maya has asked Acme to refund a legitimate payment and has uploaded a vendor attachment as evidence. After the investigation, she asks Acme to delete the attachment and any personal data no longer needed. This is a common request and also where most privacy designs fail.

### What the design does

1. **Policy identifies records required temporarily for fraud and audit evidence plus their lawful retention.** The system looks up the data class and legal basis for each record before deciding.

2. **Unneeded working copies, cache entries, embeddings, and artifacts are deleted promptly.** The attachment, the temporary file, the semantic cache answer, and any vector embeddings derived from the attachment are removed.

3. **Required evidence is minimized, access-restricted, and scheduled for later deletion.** Fields not needed for the legal purpose are removed, access is restricted to authorized roles, and a future deletion date is set.

4. **Maya receives a truthful receipt distinguishing completed deletion from retained exceptions.** The receipt lists which stores were cleared, which records are retained under exception, and when the retained records are scheduled for deletion.

### Result

Privacy promises match the real distributed data lifecycle instead of hiding surviving copies. Maya can trust the unneeded attachment is gone, while Acme retains the minimum evidence it is legally required to keep.

### The danger to avoid

Deleting the primary database row while embeddings, caches, model memories, logs, files, and vendor copies remain is incomplete and misleading. The customer believes the data is gone, but it can still be retrieved through search, chat, logs, or backups. The deletion receipt must cover every derived copy.

### Takeaway

Minimize before use and verify deletion across every derived copy.

---

## Composition

The diagram is a top-to-bottom lifecycle flow with blocked risk paths on the left and a deletion receipt across the bottom.

- **Top:** A `PERSONAL DATA` card enters a `PURPOSE GATE` and a `MINIMIZE` gate.
- **Main flow:** `USE` → `STORE` → `SHARE` → `RETAIN` → `DELETE` → `VERIFY DELETION`.
- **Data card labels:** `TENANT, PURPOSE, CONSENT or LEGAL BASIS, CLASS, OWNER, RETENTION`.
- **Coral blocked paths:** `EXTRA FIELDS, PURPOSE DRIFT, FOREVER MEMORY, SHADOW COPY`.
- **Bottom:** A `DELETION RECEIPT` crosses `DATABASE, VECTOR, CACHE, ARTIFACT, LOG`.

The vertical flow is the lifecycle. The card labels are the contract. The coral blocks are the risks. The bottom receipt is the proof.

---

## Element by element

- **PERSONAL DATA** — information about an identifiable individual, such as a name, email, address, payment token, case note, or attachment.
- **PURPOSE GATE** — the control that checks whether the use matches the recorded purpose.
- **MINIMIZE** — the step that removes fields the next component does not need.
- **USE, STORE, SHARE, RETAIN, DELETE, VERIFY DELETION** — the lifecycle stages.
- **TENANT** — the customer organization that owns the record.
- **PURPOSE** — the reason the data is being processed.
- **CONSENT or LEGAL BASIS** — the authority that allows the processing.
- **CLASS** — the sensitivity and control requirements of the data.
- **OWNER** — the accountable party for the data and its lifecycle.
- **RETENTION** — the rule that governs how long the data may be kept.
- **EXTRA FIELDS** — data collected beyond the minimum necessary.
- **PURPOSE DRIFT** — use of data beyond the original purpose.
- **FOREVER MEMORY** — data retained in model, cache, or index past its retention.
- **SHADOW COPY** — a derived or backup copy that survives primary deletion.
- **DELETION RECEIPT** — the record that reports the status of deletion across all stores.

---

## Colour and flow semantics

- **Cyan arrows** carry the data through the lifecycle from purpose to verified deletion.
- **Teal paths** show allowed, governed stages and the final DELETION RECEIPT.
- **Coral paths** show blocked or risky behavior.
- **Cobalt platforms** represent the control gates and lifecycle stages.
- **White cards** represent the data contract fields carried with each record.
- **Green checks** mark a successful verification of deletion.

The vertical flow is a timeline. The card labels are repeated visually to show that the data contract must travel with every copy. The bottom receipt is the evidence that the lifecycle closed correctly.

---

## How to present it

**Start with the library-book analogy.** Ask the room how many books they would check out for one assignment, how they would record the due date, and whether they would keep every copy forever.

**Point at the purpose gate first.** Ask what purposes personal data serves in the current system. Many teams can list "customer service" but cannot break it into refund investigation, fraud detection, marketing, model training, and legal hold.

**Trace the lifecycle from top to bottom.** PERSONAL DATA → PURPOSE → MINIMIZE → USE → STORE → SHARE → RETAIN → DELETE → VERIFY DELETION. Ask which stages have explicit policy. Often, minimize, share, retain, and verify deletion are missing.

**Show the six data-card fields.** TENANT, PURPOSE, CONSENT or LEGAL BASIS, CLASS, OWNER, RETENTION. Ask whether the system can produce all six for every personal-data field it holds.

**Walk the four blocked paths.** EXTRA FIELDS, PURPOSE DRIFT, FOREVER MEMORY, SHADOW COPY. Ask the room for a real example of each.

**Insert the second image, Diagram 152, around the blocked paths.** Explain that leakage and lifecycle are two views of the same data. Diagram 152 prevents personal data from leaving through the wrong channels; this diagram prevents it from outliving its purpose.

**Use the checkpoint as a discussion question.** *"Is consent always the required or best legal basis for every processing activity?"* Let the room answer. Then explain that the engineering job is to represent the approved basis and enforce its constraints.

**Tell the Maya deletion story.** The refund investigation ends. Maya asks for deletion. Policy separates temporary working copies from required evidence. Unneeded copies are removed from the database, vectors, cache, artifacts, and logs. Required evidence is minimized and scheduled. Maya gets a truthful receipt.

**Run the lab as a five-minute exercise.** Ask the room to pick one real personal-data field and fill in the inventory: field, source, tenant, purpose, basis, classification, prompt use, storage, recipients, retention, deletion targets, exception, evidence.

**Mention the sources in context.** The `NIST Privacy Framework` provides a structure for identifying, assessing, and managing privacy risk throughout the data lifecycle. The `NIST Generative AI Profile` highlights the new risks that AI systems introduce, including data minimization, retention in models, and deletion from vector stores and memories.

**Connect to related lessons.** `Diagram 152` is the upstream exfiltration-and-side-effect control. `Diagram 161` covers tenant isolation, the boundary that keeps one customer’s data from becoming another’s. `Diagram 168` covers tamper-evident audit and evidence chains, which are needed to prove that the lifecycle rules were followed.

**Close on the glossary.** Define the three terms:

- **Data minimization** — using only the data that is necessary for the purpose.
- **Retention** — how long data is kept before deletion.
- **Purpose limitation** — preventing use of data for purposes beyond the original basis.

**Timing.** Twenty minutes for the lifecycle trace and the data-card exercise, plus ten minutes for the deletion story and the lab. If the room debates legal bases and exceptions, allow an extra ten minutes.
## Lab and checkpoint


**Lab:** Build a data inventory for the Acme case with twelve fields. Add purpose, basis, classification, prompt use, storage, recipients, retention, deletion targets, exception, and evidence.


**Checkpoint:** Is consent always the required or best legal basis for every processing activity?


**Answer:** No. The correct basis depends on jurisdiction and purpose; the engineering job is to represent the approved basis and enforce its constraints accurately.

## Glossary

- **Data minimization** — using only necessary data
- **Retention** — how long data is kept
- **Purpose limitation** — preventing unrelated reuse

## Sources

- NIST Privacy Framework
- NIST Generative AI Profile

