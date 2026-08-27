# Diagram 125 — State Layer Map

![Four horizontal lanes on dark navy labelled CONVERSATION, AGENT RUN, A2A TASK and BUSINESS WORKFLOW. Each carries an ID, OWNER, LIFETIME and STORE card on the left and an identical seven-stage sequence — COMMAND, TASK, EVENT, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME — with a FAILURE badge at its right. Teal dashed CORRELATION ID lines run between the lanes. All four failure paths converge on a large red MERGED SESSION STORE with a crack down it, labelled LOST OWNERSHIP.](../diagrams/125-state-layer-map.png)

**Module:** Durable-system foundation
**Role in the course:** the first diagram — four kinds of state that must not become one
**Layout:** four parallel lanes with identical structure, correlated by dashed links, converging on a rejected merged store

---

## At a glance

Four lanes, each with its own **ID, OWNER, LIFETIME and STORE**. Each running the same seven-stage sequence. Each with its own failure path.

Dashed **CORRELATION ID** links running between them.

And on the right, a large red container with a **crack down its face**: **MERGED SESSION STORE**, labelled **LOST OWNERSHIP**.

Correlated, not merged. That distinction is the whole diagram, and the cracked container is what happens when it is ignored.

---

## What the diagram teaches

### 1. Four state layers, and they answer four different questions

**CONVERSATION** — what was said. Turns, messages, display text. Transient.

**AGENT RUN** — what one agent invocation did. A single reasoning episode with its plan, tool calls and output.

**A2A TASK** — what was delegated to another party. Its own lifecycle, owned by the specialist.

**BUSINESS WORKFLOW** — what the organisation is doing. The case, the claim, the order.

They are not layers of abstraction over one thing. They are four different things with four different lifetimes, and conflating them is the failure this volume opens with.

### 2. The four fields on every lane are what make them distinct

**ID, OWNER, LIFETIME, STORE** — identical labels on all four cards, and every one has a different value per lane.

**ID** — each layer has its own identifier. A conversation ID is not a run ID is not a task ID is not a case ID.

**OWNER** — who is responsible. The conversation belongs to the user interface. The run belongs to the agent. The task belongs to the specialist. The workflow belongs to the business.

**LIFETIME** — how long it lives. A conversation may last minutes; a case may last months.

**STORE** — where it is persisted. Different durability requirements mean different stores.

Four fields, four layers, sixteen values that must differ.

### 3. The seven stages repeat identically in every lane, and that is deliberate

**COMMAND → TASK → EVENT → ACKNOWLEDGEMENT → RECEIPT → CHECKPOINT → RESUME.**

The same sequence, four times.

That repetition says these are not four different mechanisms. Each layer has commands, produces events, acknowledges, records receipts, checkpoints and resumes — the same durable-workflow machinery at four scales.

Which means the patterns in the rest of the volume apply to all four. A checkpoint on an agent run and a checkpoint on a business workflow are the same idea with different lifetimes.

### 4. The teal upward arrows beneath each sequence are the layer's own recovery

Look beneath each lane's seven stages: a teal line runs along the bottom with arrows rising into every stage.

Each layer recovers independently. A crashed agent run resumes from its own checkpoint; it does not require the business workflow to restart.

That independence is the operational payoff of separating them. A failure in one layer is contained to that layer.

### 5. CORRELATION ID is dashed, and dashed means reference rather than containment

Teal dashed lines run from each lane's left edge, labelled **CORRELATION ID**, connecting the layers.

Dashed because it is a **reference**, not a containment relationship. The conversation does not contain the run; it refers to it.

That is the difference between correlation and merging. A correlation ID lets you assemble the full picture across four stores when you need it, while leaving each store owning its own data with its own lifetime.

Merging gives you the assembled picture permanently, at the cost of every layer inheriting the strictest requirements of all four.

### 6. The merged store is cracked, and the crack is the diagram's judgement

The red container on the right is drawn with a **jagged crack down its face**, with all four failure paths converging on it.

Four coral dashed lines, one per lane, all arriving at the same broken container.

The crack is not decorative. It says this structure fails, and the label says how: **LOST OWNERSHIP**.

### 7. LOST OWNERSHIP names the specific failure

Not "poor separation" or "coupling" — **lost ownership**.

When four layers share one store, nobody owns any of it. Concretely:

**Retention becomes impossible to reason about.** The conversation should be deleted in 30 days; the case must be retained for seven years. One store, one policy, and both requirements cannot be met.

**Deletion becomes dangerous.** Deleting a conversation deletes the workflow state it shares a record with.

**Concurrency becomes unmanageable.** Four layers writing to one record means four sources of contention with no clear precedence.

**Failure isolation disappears.** A corrupt conversation state takes the business workflow with it.

The opposite of the cracked merged store is a system where ownership is stored on every durable object rather than assumed from the container:

![On dark navy, a WORKFLOW platform sends cyan arrows into three checked TASK / STATE cards, then to three blue platforms — A2A ARTIFACT, SIDE-EFFECT RECEIPT, and BUSINESS RECORD — each carrying an identical white table with ID, VERSION, HASH, ACTOR, TIME and CORRELATION. A teal lineage chain runs back to SOURCE REQUEST, and a coral CHAT ONLY branch is labelled NOT PROOF.](../diagrams/128-artifact-receipt-business-record.png)

The three outputs in this diagram are what the four lanes above produce when ownership is preserved. Each one carries its own **ID, ACTOR and CORRELATION**, and each one belongs to one of the four lanes — artifact to A2A task, receipt to agent run, business record to business workflow. The conversation lane produces nothing there, which is why the chat branch is marked **NOT PROOF**. Ownership is not a document property; it is a field that travels with the object.

---

## Case study — Wrayford Insurance, the session that held the claim

Wrayford handles motor and property claims for about 340,000 policyholders. Their claims assistant supports handlers through the assessment and settlement process.

A claim takes between two days and eight months.

### What they built

A session store. One record per user session, holding everything: the conversation, the agent's working state, the tasks delegated to their assessment agents, and the claim's own progress.

It was simple, it was fast, and it worked for the first nine months.

### The first failure — retention

Their data protection review asked how long conversations were retained.

The answer was seven years, because conversations shared a record with claim state, and claim state is retained for seven years under their regulatory obligations.

Wrayford was holding the full text of every handler-assistant conversation — including handlers' unstructured notes and speculation — for seven years, because it lived in the same record as the claim.

**Their DPO's position:** conversation content is not claim evidence, is not subject to the seven-year requirement, and should not be retained beyond operational need.

There was no way to delete it without deleting the claim state.

### The second failure — the deletion that took a claim with it

A handler raised a support request about a session that had become corrupted — the assistant was producing incoherent responses, and the working state was clearly wrong.

Support's standard fix was to clear the session.

It cleared the claim's workflow state as well. The claim reverted to a state indicating no assessment had been performed, and the completed assessment steps were lost.

The claim had been three weeks into an eight-week assessment. Reconstructing it took four days of manual work from the handler's own notes and the receipts their payment system held.

### The third failure — concurrency

Two handlers working the same claim, as happens when one covers for another.

Both sessions loaded the shared record. Both wrote. The second write overwrote the first, silently.

That was discovered when a handler's completed eligibility check disappeared and had to be redone. It had happened, by their subsequent estimate, on roughly 40 claims over six months.

### The rebuild on four layers

**Conversation state.** Its own store, keyed by conversation ID, owned by their interface team, retained 30 days.

**Agent run state.** Its own store, keyed by run ID, owned by their platform team, retained 7 days. A run is a single reasoning episode and nothing outside that episode needs its intermediate state.

**A2A task state.** Owned by the specialist agents themselves. Wrayford's orchestrator holds task IDs, not task state.

That was the change with the biggest structural effect. Previously their session record held copies of the assessment agents' internal state, which meant Wrayford's store had to be updated whenever a specialist's model changed.

**Business workflow state.** Their claim record, keyed by claim ID, owned by their claims function, retained seven years, and — critically — the only one of the four with a defined state machine and invariants.

**Correlation IDs on everything.** A conversation record carries the run IDs it produced. A run record carries the task IDs it created and the claim ID it operates on. A claim record carries nothing about conversations, because the claim does not need to know.

That last asymmetry took a design discussion. Their instinct had been bidirectional references. Their claims function's requirement was that the claim record contain only claim evidence, and that reconstructing which conversations touched a claim be a query across stores rather than a field on the claim.

### What the separation enabled

**Retention became per-layer.** Conversations delete at 30 days. Runs at 7. Claims at seven years. Each policy is expressible because each store has one owner and one requirement.

**Session clearing became safe.** Support can clear a conversation and a run without touching claim state. That support procedure now runs about 20 times a month with no incidents.

**Concurrency became tractable.** Two handlers on one claim have two conversations and two runs, both correlating to one claim record — and the claim record has optimistic concurrency control with a version, which the two-handler case now exercises correctly.

**Specialist state stopped being Wrayford's problem.** Their assessment agents' internal state is theirs. Wrayford holds task IDs and reads status.

### The reconstruction test

Six months after the rebuild they tested whether they could still assemble a full picture.

Given a claim ID, they can find every run that touched it, every conversation those runs belonged to (within the 30-day window), every task delegated, and every receipt produced.

Assembly takes about 400ms across four stores. Under the merged design it had been a single read.

**That 400ms is the cost of separation, and they consider it obviously worth paying.**

### Results

- **Conversation retention:** 7 years → 30 days.
- **Claims lost to session clearing:** 1 incident, 4 days to reconstruct → structurally impossible.
- **Silent overwrites from concurrent handlers:** ~40 over six months → 0, via per-layer concurrency control.
- **Specialist state held in Wrayford's store:** eliminated.
- **Full-picture assembly:** one read → ~400ms across four stores.

### The line in their architecture standard

*Correlate the layers. Do not merge them. The moment one record holds four lifetimes, three of them are wrong.*

---

## Composition

Four horizontal lanes stacked vertically, with correlation links between them and a convergence on the right.

**Each lane**, top to bottom — **CONVERSATION**, **AGENT RUN**, **A2A TASK**, **BUSINESS WORKFLOW** — contains:

A **bordered card on the left** listing four rows with blue icons: **ID**, **OWNER**, **LIFETIME**, **STORE**.

A **wide blue platform** holding seven white stage cards connected by cyan arrows: **COMMAND** (speech bubble), **TASK** (clipboard), **EVENT** (teal bell), **ACKNOWLEDGEMENT** (teal shield with check), **RECEIPT** (teal envelope), **CHECKPOINT** (teal bookmark), **RESUME** (teal play).

A **teal line beneath the seven stages** with arrows rising into each.

A **coral FAILURE badge** at the lane's right end.

**Between lanes:** **teal dashed lines** labelled **CORRELATION ID**.

**Right:** all four coral failure paths converge on a large **red container with a jagged crack**, labelled **MERGED SESSION STORE**, with a **red warning triangle** beneath and **LOST OWNERSHIP** in coral.

## Element by element

**CONVERSATION** — what was said. Transient.
**AGENT RUN** — one reasoning episode.
**A2A TASK** — delegated work, owned elsewhere.
**BUSINESS WORKFLOW** — the case. Long-lived, authoritative.

**ID / OWNER / LIFETIME / STORE** — four fields, sixteen values that must differ.

**The seven-stage sequence** — identical machinery at four scales.

**CORRELATION ID** — dashed teal, a reference rather than containment.

**MERGED SESSION STORE** — a cracked red container. **LOST OWNERSHIP**.

## Colour and flow semantics

- **Cyan arrows** carry each lane's stage sequence forward.
- **Teal** marks the event, acknowledgement, receipt, checkpoint and resume icons, and the per-lane recovery line beneath each sequence.
- **Teal dashed** carries correlation between lanes — reference, not flow.
- **Coral** carries all four failure paths to the merged store.
- The **crack in the merged store** is the diagram's judgement, and **LOST OWNERSHIP** names it.

## How to present it

**Ask how many kinds of state their system has.** Most rooms say one or two. Then name four and ask which of the four their session record holds.

**Read the four fields and ask for their values per layer.** Sixteen values. Then ask which two layers in their system share a store — there is usually at least one pair.

**Point at the seven stages repeating.** The same machinery at four scales. That means every pattern in this volume applies to all four, which is worth saying at the start.

**Point at the teal line beneath each sequence.** Each layer recovers independently. Ask what happens when they share a store — a failure in one takes the others.

**Ask what dashed means on the correlation lines.** Reference, not containment. Then draw the distinction: correlation lets you assemble the picture when you need it; merging gives you the picture permanently at the cost of every layer inheriting the strictest requirement of all four.

**Point at the crack.** Then read the label: lost ownership. Not coupling — ownership.

**Tell the Wrayford retention finding.** Conversations retained seven years because they shared a record with claim state. Their DPO's position, and no way to delete one without the other.

**Tell the session-clearing incident.** Support's standard fix cleared the claim's workflow state. Three weeks into an eight-week assessment, four days to reconstruct.

**Give them the concurrency number.** Two handlers on one claim, second write overwriting the first silently, roughly 40 claims over six months.

**Note the asymmetric reference.** Wrayford's claim record holds nothing about conversations. Their instinct had been bidirectional; their claims function required the claim to contain only claim evidence.

**Give them the cost honestly.** Full-picture assembly went from one read to 400ms across four stores. Ask whether that trade is obviously worth it — it is, and saying the number makes the argument credible.

**Timing.** Twenty-five minutes. Thirty-five if you map the room's own state into four layers, which reliably finds two sharing a store.

---

## Lab and checkpoint

**Lab:** Map your own state into four layers: conversation, task, case, and business record. For each, define the four fields: scope, lifetime, owner, and recovery. Identify any two layers sharing a store and the failure that causes. Then design the recovery path for each layer independently.

**Checkpoint:** Why is the correlation line dashed?

**Answer:** Because dashed means reference, not containment. The layers are linked by a correlation ID rather than merged. This lets each layer have its own lifetime, owner, and recovery. A merged store means every layer inherits the strictest requirements of all, which leads to retention, deletion, and concurrency problems.

## Glossary

- **Business record** — the authoritative, durable fact about the world.
- **Case** — the long-running unit of work that contains tasks and conversations.
- **Conversation** — the message or interaction state between a user and the system.
- **Correlation ID** — the dashed reference that links layers without merging them.
- **Lifetime** — how long a layer retains its state.
- **Lost ownership** — the failure that occurs when layers are merged and ownership becomes unclear.
- **Owner** — who is responsible for and may act on a layer.
- **Recovery** — how a layer is restored after a failure.
- **Scope** — what the layer contains and covers.
- **State layer** — one of the four distinct kinds of state in the system.
- **Task** — the work item that is assigned, completed, and tracked.

## Sources

- State layering and separation in agent systems
- Conversation, task, case, and record lifetimes
- Correlation IDs and recovery design
