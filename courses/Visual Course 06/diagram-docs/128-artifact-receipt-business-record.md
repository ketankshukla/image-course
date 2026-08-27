# Diagram 128 — Durable Artifacts, Receipts, and Business Records

![On dark navy, a WORKFLOW platform sends cyan arrows into a column of three checked cards labelled TASK / STATE 1, 2 and 3. Cyan arrows fan right to three blue platforms — A2A ARTIFACT with a document and cube, SIDE-EFFECT RECEIPT with a checked receipt, and BUSINESS RECORD with a database — each carrying an identical white table reading ID, VERSION, HASH above ACTOR, TIME, CORRELATION. Teal dashed arrows leave all three into a descending chain of EVENT, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT and RESUME that ends at a large teal SOURCE REQUEST platform. A coral dashed line drops from the workflow to a coral speech bubble labelled CHAT ONLY and NOT PROOF.](../diagrams/128-artifact-receipt-business-record.png)

**Module:** Durable-system foundation
**Role in the course:** the last diagram of the foundation — what survives, and what it is allowed to prove
**Layout:** one workflow producing three identified outputs, each carrying six fields, with a lineage chain running back to the source request and chat refused as evidence

---

## At a glance

One workflow. Three outputs: **A2A ARTIFACT**, **SIDE-EFFECT RECEIPT**, **BUSINESS RECORD**.

Three different glyphs — a document, a receipt, a database — and beside each, the **same six fields**: **ID, VERSION, HASH, ACTOR, TIME, CORRELATION**.

Teal dashed lines run from all three into a descending chain ending at **SOURCE REQUEST**. And falling away from the workflow on a coral dashed line, a speech bubble: **CHAT ONLY**, labelled **NOT PROOF**.

Three durable outputs, three different claims. A fourth thing that looks like an output and proves nothing.

---

## What the diagram teaches

### 1. Three outputs, and each one proves a different kind of thing

**A2A ARTIFACT** — a document with a cube. The deliverable a task produced. It **explains**.

**SIDE-EFFECT RECEIPT** — a receipt with a check badge. Evidence that an operation was attempted outside the system, and what came back. It **proves an attempt**.

**BUSINESS RECORD** — a database cylinder. The fact the organisation acts on. It **owns truth**.

A consultant's report, a shop receipt and the bank ledger may all describe one purchase, and each proves something different. The failure this diagram prevents is substitution: taking the thing that explains and treating it as the thing that proves.

### 2. Six identical fields, and their identity is the contract

All three carry the same table: **ID, VERSION, HASH** above **ACTOR, TIME, CORRELATION**. Three objects, three owners, one minimum contract.

**ID** — a stable identity, not a row number or a path. **VERSION** — because a second version is a new object, not an edit. **HASH** — of the content or the payload. **ACTOR** — the agent and its card version, the caller, the domain service. **TIME** — when. **CORRELATION** — what this belongs to.

Six fields, three objects, eighteen values. Any output that cannot fill all six is not durable evidence; it is a log line.

### 3. HASH is the field that makes the other five worth having

Without it, an identified, versioned, attributed, timestamped, correlated record still only asserts that **something** was produced at that moment. It does not establish **what**.

A hash converts a reference into a claim about content — it lets a reconciliation job six months later say the payload it is re-reading is the payload that was sent, rather than one since re-serialised by newer code.

So hash the payload you sent, not a reconstruction of it. Systems that store parameters and rebuild the payload on demand find the rebuild stops matching the moment the serialisation changes.

### 4. The outputs come from the task column, not from the workflow

**WORKFLOW** feeds **TASK / STATE 1, 2 and 3**, and the arrows into the three outputs leave the *tasks*. Follow the long cyan arrow along the bottom: it leaves **TASK / STATE 3** and travels right into **BUSINESS RECORD**.

The business record is not updated by the workflow in passing. It is updated at a named stage, through the boundary that owns it — because systems that let any step write the system-of-record fact eventually have several that do, and no way to say which was authoritative.

### 5. Each output enters the lineage chain at a different point

**A2A ARTIFACT → EVENT.** An artifact appearing is something that happened, and nobody has acknowledged it yet.

**SIDE-EFFECT RECEIPT → RECEIPT.** Below acknowledgement, because a receipt is what you produce *after* the acknowledgement, and it is what lets you resume safely.

**BUSINESS RECORD → RESUME.** Past checkpoint — what a restarted process reads to find out what is already true.

Three altitudes on one chain, encoding how much of the durable-workflow vocabulary each output has already passed through.

### 6. The chain runs to SOURCE REQUEST, and the direction is the whole idea

**EVENT → ACKNOWLEDGEMENT → RECEIPT → CHECKPOINT → RESUME → SOURCE REQUEST.**

Lineage is the ability to walk from any durable output back to the thing that asked for it, and **CORRELATION** on all three tables is what makes the walk possible.

The lines are **dashed** — reference, not containment. The receipt does not contain the request; it points at it, and the pointer survives independently of both.

This is the correlation column of the volume's first diagram, drawn as a path:

![Four horizontal lanes for conversation, agent run, A2A task and business workflow, each carrying its own ID, owner, lifetime and store card and an identical seven-stage sequence, joined by dashed correlation lines, with all four failure paths converging on a cracked merged session store labelled lost ownership.](../diagrams/125-state-layer-map.png)

**CORRELATION** here is that diagram's dashed link, stored on the object rather than drawn between lanes. The three outputs map onto three of its four lanes: the artifact to the A2A task, the receipt to the agent run that attempted the call, the business record to the business workflow. The conversation lane produces nothing — which is what the coral branch is about.

### 7. CHAT ONLY has no table, and that absence is the argument

Every other output carries six fields. The coral speech bubble carries none, and that is not an oversight in the drawing.

Chat text has no stable ID, no version, no hash, no actor beyond "the model", and no correlation that survives the conversation being cleared. It cannot be reconciled, because there is nothing to reconcile against.

Its line is **dashed**, like the lineage lines, because chat *does* refer to the work. It describes what the system believes happened; it is not evidence that it did.

The rule is narrow and absolute: **a pleasant message must never be the only record that money moved or a case closed.**

---

## Case study — Kelsford Energy, the refunds that only existed in chat

Kelsford supplies gas and electricity to about 1.1 million domestic customers. Refunds arise constantly — an account closed in credit, an estimate corrected by a meter reading, a tariff applied wrongly — and run at roughly 9,000 a month.

Their refund assistant handled the whole path: assess the balance, decide the amount, call the payment provider, tell the customer.

### What they had

An agent that produced a refund summary and posted it into the customer service console.

Their case system had a `refund_status` field — free text, written by the agent. The payment provider's response went to application logs with 30-day retention.

Three representations of one refund, and the only one anybody looked at was the chat message.

### The six hours

Their payment provider deployed a change to its disbursement queue. For about six hours the API accepted refund requests, returned `202 Accepted` with an operation ID, and enqueued them onto a queue that was purged during the same deployment's rollback.

Kelsford's agent saw a 2xx and did what it always did. It wrote a message:

*I've processed a refund of £248.19 to your account. You should see it within 3–5 working days.*

**1,431 refunds. £361,000. None of them executed.**

Nothing in Kelsford's system disagreed, because nothing in Kelsford's system had an opinion. The `refund_status` field said `refunded` because the agent had written that, and the provider's `202` responses rolled off after 30 days.

The first escalation arrived five weeks later. Three customers went to the energy ombudsman, Kelsford was asked to evidence that the refunds had been issued, and produced a chat transcript.

**The ombudsman's position was that a message the supplier generated about its own conduct is not evidence of that conduct.** All three complaints were upheld.

### The nine days

How many others were there? Kelsford could not answer from their own systems.

They pulled a settlement export from the provider and reconciled it by hand. There was no shared key — the export was keyed on the provider's operation ID, which Kelsford had logged and discarded — so they matched on amount, date and a partial account reference.

**Fifty-four thousand refunds, nine days, four people.** The 1,431 were found on day six.

### The rebuild into three objects

**The artifact.** Their balance-analysis agent's refund assessment, as an A2A artifact with typed parts: the calculated entitlement, the readings it rests on, the tariff version applied. Artifact ID, version, SHA-256 of content, actor as agent card ID plus card version, time, correlation as the case ID.

It is downloadable, it is quotable to a customer, and it proves nothing about money.

**The receipt.** Immutable, written before acknowledgement, one per attempt: Kelsford's idempotency key, the provider's operation ID, the HTTP status, both timestamps, and a hash of the exact serialised payload sent. Secrets are redacted before the record is written rather than before it is displayed.

The provider operation ID is now **stored**, not logged — the single change that makes reconciliation a join instead of a fuzzy match.

**The business record.** The case record, written only by their billing domain service. States: `REFUND_PROPOSED`, `REFUND_SUBMITTED`, `REFUND_SETTLED`, `REFUND_FAILED`.

### The mistake they made in the rebuild

The first version moved the case to `REFUND_SETTLED` on a provider success status — which would have behaved identically during the six hours.

Their reviewer caught it. A receipt proves an **attempt and its immediate result**, and a `202` is not a settlement. The state was split: `REFUND_SUBMITTED` on the receipt, `REFUND_SETTLED` only on the provider's settlement notification confirmed against the daily statement.

The gap is normally about four hours and is visible in the console. Agents disliked telling customers a refund was "submitted" rather than "done". That was the correct amount of discomfort.

### The reconciliation job

Nightly and on demand, joining receipts to the provider statement on operation ID and business records to receipts on correlation ID. It reports four categories, of which two are alarms: settled with no matching receipt, and receipt with no matching provider record.

Replayed against the outage window in a test environment, it flagged all 1,431 within twenty minutes of the window closing.

### Results

- **Refunds shown as complete that never executed:** 1,431 over six hours, undetected for five weeks → detected within ~20 minutes by reconciliation.
- **Answering "did this refund actually happen":** 9 days, 4 people, fuzzy matching → a single join on stored operation IDs.
- **Provider operation IDs retained:** logged for 30 days → stored immutably on the receipt.
- **Ombudsman complaints upheld on inability to evidence:** 3 → 0 in the following 14 months.
- **Duplicate refunds from operators re-running failed jobs:** 20–30/month → 0, via idempotency keys carried on receipts.
- **Chat text as the system of record:** eliminated. The console reads the business record and labels it.

### The line in their operations standard

*A message is not a receipt. If the only place a payment exists is in something we wrote about ourselves, it did not happen.*

---

## Composition

A left-to-right expansion: one source, a task column, three outputs, a descending lineage chain, and a rejected branch below.

**Left:** **WORKFLOW** — a blue platform holding a rounded cube with a white node-and-branch glyph.

**Left-centre:** three white cards on blue platforms — **TASK / STATE 1**, **2** and **3** — each with two checked rows and a **blue circled check**, fed by **cyan arrows** from the workflow and joined downward to each other.

**Centre-right:** three blue platforms, each with a rounded 3D icon and a white two-row table — **A2A ARTIFACT** (a document with a cube), **SIDE-EFFECT RECEIPT** (a receipt with a check badge), **BUSINESS RECORD** (a database cylinder). Each table reads **ID** (badge), **VERSION** (layers), **HASH** (fingerprint) above **ACTOR** (person), **TIME** (clock), **CORRELATION** (link).

**Cyan arrows** fan from the task column into the artifact and the receipt; a **long cyan arrow** runs from beneath **TASK / STATE 3** along the bottom and up into **BUSINESS RECORD**.

**Right:** a descending **teal** chain of pill badges — **EVENT** (bell), **ACKNOWLEDGEMENT** (check), **RECEIPT** (document), **CHECKPOINT** (flag), **RESUME** (play) — joined by **teal dashed arrows** and ending at a large **teal platform** with an inbound-tray glyph labelled **SOURCE REQUEST**. Dashed teal enters it from the artifact into **EVENT**, the receipt into **RECEIPT**, and the business record into **RESUME**.

**Lower left:** a **coral dashed line** drops from the workflow to a **coral speech bubble with three dots**, with two stacked coral bars reading **CHAT ONLY** and **NOT PROOF**.

## Element by element

**WORKFLOW** — one source, three durable outputs.
**TASK / STATE 1–3** — the stages that actually produce them.

**A2A ARTIFACT** — the deliverable. It explains.
**SIDE-EFFECT RECEIPT** — evidence of an attempt and its result. It proves an attempt.
**BUSINESS RECORD** — the authoritative fact. It owns truth.

**ID / VERSION / HASH / ACTOR / TIME / CORRELATION** — six fields, three objects, eighteen values.

**EVENT → ACKNOWLEDGEMENT → RECEIPT → CHECKPOINT → RESUME → SOURCE REQUEST** — the lineage chain, entered at three different altitudes.

**CHAT ONLY / NOT PROOF** — the only output with no table.

## Colour and flow semantics

- **Cyan arrows** carry forward work: workflow into tasks, tasks into the three outputs.
- **Teal** marks the lineage chain, matching the volume's event, acknowledgement, receipt, checkpoint and resume vocabulary.
- **Teal dashed** carries lineage — a reference back to the source request, not a flow of work.
- **Coral dashed** carries the chat branch, and its dashes say the same thing: chat refers to the work without evidencing it.
- The **identical tables** on three visually different objects are the diagram's central device, and the **absent table** on **CHAT ONLY** is its argument.

## How to present it

**Open with the analogy before the diagram.** A consultant's report, a shop receipt and the bank ledger can all describe one purchase, and each proves something different. Then ask which of the three their agent produces.

**Give each glyph a verb.** Artifacts explain, receipts prove attempts, business records own truth. Then ask which one their user interface is reading.

**Point at the three identical tables.** Six fields, three objects, eighteen values. Ask the room to fill in the eighteen for one real operation; the exercise reliably strands on **HASH** and **CORRELATION**.

**Make the hash point concretely.** Hash the payload you sent, not a reconstruction of it. Ask whether they could re-derive last March's request byte for byte after two serialisation changes.

**Trace the long bottom arrow into the business record.** It leaves a named task, not the workflow. Then ask how many places in their codebase can write their system-of-record status.

**Read the three lineage entry points separately.** Artifact into EVENT, receipt into RECEIPT, business record into RESUME — then note the dashes: reference, not containment.

**Tell the six hours.** The provider returned `202`, enqueued, and purged the queue on rollback. 1,431 refunds, £361,000, and a cheerful message about three to five working days. Then give them the ombudsman's line: a message the supplier generated about its own conduct is not evidence of that conduct.

**Tell the nine days.** Fifty-four thousand refunds matched by hand on amount, date and partial reference, because the provider's operation ID had been logged and not stored. Kelsford's single most valuable change was storing one identifier.

**Present the mistake in the rebuild, not just the rebuild.** Their first version settled the case on a `202` and would have behaved identically during the outage. A receipt proves an attempt; settlement is a separate fact.

**Close on the coral branch and the missing table.** Every other output has six fields; this one has none. Then read the standard: *a message is not a receipt.*

**Timing.** Twenty-five minutes. Thirty-five if the room fills in the eighteen values for a real operation, which usually reveals that their receipts have no stable identity.

---

## Lab and checkpoint

**Lab:** Pick one real operation in your system and fill in the six fields for its artifact, receipt, and business record: id, operation, payload, hash, who, and correlation. Identify which object each consumer reads. If the consumer only has a chat message, write the receipt or record that is missing.

**Checkpoint:** Why is a message not a receipt?

**Answer:** Because a message is an explanation generated by the system or supplier. A receipt is a durable, hashable record of an attempt that can be verified later. A message can be cheerful and false; a receipt must be tied to a specific operation with a stable identity.

## Glossary

- **Artifact** — an explanation or produced object returned by a task.
- **Business record** — the authoritative, durable truth about a completed operation.
- **Chat only** — the anti-pattern of treating a conversational message as a system output.
- **Correlation** — the link to the original request or task.
- **Event** — the lineage entry point for an artifact.
- **Hash** — the value that proves the payload has not changed.
- **Lineage** — the chain from output back to source request.
- **Receipt** — the durable proof that an attempt was made.
- **Resume** — the lineage entry point for a business record.
- **Source request** — the original request that started the operation.

## Sources

- Artifacts, receipts, and business records
- Durable workflow outputs and lineage
- Hashing and idempotency for operations
