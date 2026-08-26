# Diagram 99 — ACP to A2A Migration

![Two bordered panels on dark navy. HISTORY ACP, subtitled HISTORICAL in coral, lists five rows on the left — AGENT MANIFEST, RUN, MESSAGE, OUTPUT, CUSTOM STREAM. CURRENT TARGET A2A 1.0 lists five on the right — AGENT CARD, TASK, MESSAGE PARTS, ARTIFACT, STATUS AND ARTIFACT EVENTS. Between them, a blue ADAPTER STRANGLER bridge spans the top two rows, and a vertical stack of four stages runs beneath it — DUAL READ, SHADOW TEST, CUTOVER, and a coral RETIRE with a bin icon — with teal arrows entering from the left rows and leaving to the right rows.](../diagrams/99-acp-to-a2a-migration.png)

**Module:** Choosing boundaries
**Role in the course:** moving from a retired model to the current one without a cutover event
**Layout:** two term panels joined by a bridge and a four-stage migration sequence

---

## At a glance

Five old terms on the left under **HISTORY ACP (HISTORICAL)**. Five current terms on the right under **CURRENT TARGET A2A 1.0**.

Between them: an **ADAPTER STRANGLER** bridge, and beneath it a four-stage sequence — **DUAL READ → SHADOW TEST → CUTOVER → RETIRE**.

The vocabulary mapping is the easy half. The four stages are the hard half, and the word **strangler** is what makes the difference between a migration and an outage.

---

## What the diagram teaches

### 1. Five mappings, and two of them are more than renames

**AGENT MANIFEST → AGENT CARD.** A manifest is an inventory; a card is an identity with attestation. The card adds signatures, security schemes and interfaces that a manifest had no place for.

**RUN → TASK.** A run executes; a task is a managed object with a lifecycle, an owner and states it can rest in.

**MESSAGE → MESSAGE PARTS.** Singular to plural, and typed. A message becomes a composition of text, file and data parts rather than a single blob.

**OUTPUT → ARTIFACT.** Output is what a function returned; an artifact is a typed, storable, referenceable deliverable — and there may be several.

**CUSTOM STREAM → STATUS AND ARTIFACT EVENTS.** A bespoke stream becomes two defined event categories.

The first three are largely translation. **Message parts and artifact are shape changes**, and the fifth is a replacement of something bespoke with something specified.

### 2. HISTORICAL in coral is a status, not a judgement

The subtitle beneath **HISTORY ACP** is set in coral.

Coral throughout this library marks retired concepts. It says this is not where you build — and it does not say the ideas were wrong.

Every one of the five left-hand concepts has a right-hand counterpart. Nothing was discarded. The vocabulary moved and the shapes were refined.

That matters for how you treat a team arriving with ACP knowledge: their model is sound, their words have moved, and two of their shapes need work.

### 3. The strangler bridge is a pattern with a name, and the name is the point

**ADAPTER STRANGLER** — a blue bridge spanning the top of the gap.

The strangler pattern: rather than replacing a system in one event, you grow a new one around the old one, redirect traffic piece by piece, and remove the old one when nothing uses it.

The name comes from a plant that grows around a host tree and eventually replaces it. Gradual, and at every moment something is standing.

For a protocol migration this means: an adapter accepts old-shaped requests and serves them from new-shaped implementations, so callers move at their own pace rather than on your schedule.

### 4. The four stages are ordered and each is a gate

**DUAL READ** — both models are read. The old path continues to serve; the new path is exercised in parallel.

**SHADOW TEST** — the new path's output is compared against the old path's, without being used. Divergences are found here, before anything depends on them.

**CUTOVER** — traffic moves to the new path. The old one remains available.

**RETIRE** — the old path is removed. Coral, with a bin.

Each is a gate. You do not shadow test until dual read is stable. You do not cut over until shadow testing shows agreement. You do not retire until nothing uses the old path — which you can only know if you measured.

### 5. Shadow test is the stage teams skip, and it is the one that finds the problems

Between building the new thing and using it.

The new path runs on real traffic, producing real output, and that output is **discarded** after comparison.

That is expensive — you are running everything twice — and it is the only way to find divergences under real conditions before they matter.

Synthetic tests find the cases you thought of. Shadow testing finds the ones you did not, on the data you actually have.

### 6. RETIRE is coral, and its position last is not negotiable

The only coral stage, with a **bin** icon.

Coral because removal is the irreversible step. Everything before it is additive; this one takes something away.

Its position matters because the temptation is to retire early — the old path is a maintenance burden, and once cutover is complete it feels finished.

It is not finished until nothing uses it, and knowing that requires measurement. A retirement based on the belief that everyone has migrated is how you discover the three clients who had not.

### 7. Teal arrows run left to right through the stages, and the direction is the migration

Arrows enter the stack from the **HISTORY ACP** rows and leave toward the **CURRENT TARGET** rows.

Each old concept passes through the four stages and emerges as its current counterpart.

The per-concept routing is worth noticing: this is not a single migration of the whole system. Each concept migrates through the four stages on its own timeline. Manifests may be at cutover while custom streams are still at dual read.

The right-hand panel is the destination, and its shapes are richer than the left's:

![Parts composing into a task carrying TASK ID, CONTEXT ID and STATUS, with a status path branching to INPUT REQUIRED, AUTH REQUIRED, FAILED, CANCELED and REJECTED, and artifacts and agent messages returning.](../diagrams/90-a2a-message-task-artifact-anatomy.png)

Comparing the two shows what the migration actually gains. **CONTEXT ID** has no ACP counterpart. Neither does **REJECTED** or **AUTH REQUIRED**. The Wenlock retry-storm finding below is precisely a missing state being discovered during shadow testing.

---

## Case study — Wenlock Robotics, the migration that took eleven months and broke nothing

Wenlock builds warehouse automation. Their platform coordinates fleets of picking robots, and their agent layer was built early — against ACP, because that is what existed when they started.

By the time A2A 1.0 stabilised they had 14 integrating customers, four of whom had built substantial automation against Wenlock's ACP-shaped interfaces.

### Why a cutover was impossible

Their customers' integrations were embedded in warehouse operations. A breaking change meant a customer's picking operation stopping.

Two customers ran 24-hour operations with no maintenance window at all.

A coordinated cutover across 14 customers with different release cycles, different engineering capacity, and in two cases no ability to take downtime, was not achievable.

### The strangler approach

They built an adapter layer accepting ACP-shaped requests and serving them from a new A2A-shaped implementation.

From a customer's perspective, nothing changed. Their existing integration continued working, against the same endpoints, with the same shapes.

Behind the adapter, the implementation was entirely new.

### The four stages, per concept

They migrated the five concepts independently, and the timelines differed substantially.

**AGENT MANIFEST → AGENT CARD.**

*Dual read* — the platform served both a manifest endpoint and a card endpoint from one source of truth. Two weeks.

*Shadow test* — for every manifest request, the equivalent card was generated and compared for semantic equivalence. Three weeks, and it found that their manifest had been declaring two capabilities the implementation did not actually support. Nobody had noticed because nobody had called them.

*Cutover* — new customers onboarded onto cards. Existing ones continued on manifests.

*Retire* — eleven months later, when the last manifest consumer had moved.

**RUN → TASK.** The most involved, because it was a shape change rather than a rename.

*Dual read* — every run created a corresponding task. Both were maintained in parallel, which meant duplicated state and a reconciliation job to catch drift.

Their drift reconciliation found divergences in about 0.3% of runs during the first fortnight, all traced to two edge cases in state mapping. Both were fixed before shadow testing began.

*Shadow test* — six weeks. The finding that justified the whole stage: the ACP run model had no equivalent of the A2A `rejected` state. Their ACP implementation had been returning a generic failure when a robot fleet declined work — because it was at capacity, or because the requested zone was closed.

Customers' retry logic, seeing a failure, retried. Against a fleet at capacity, that produced retry storms during peak periods that Wenlock had attributed to network issues for over a year.

*Cutover* — staged, customer by customer, over four months.

*Retire* — the run endpoints were removed after the last customer moved.

**MESSAGE → MESSAGE PARTS.** Straightforward. Their ACP messages had been carrying JSON blobs in a text field, which customers parsed. Typed parts made the structure explicit. Three months end to end.

**OUTPUT → ARTIFACT.** The shape change that customers noticed most, because outputs became plural.

A pick operation produces a completion record, an exception report, and — for operations involving damaged stock — a photograph. Under the old model these were packed into one output object. As artifacts they became three, each typed.

Two customers preferred the old shape and asked for it to be retained. Wenlock declined, and provided an adapter helper that reassembled the three into the old structure for anyone who wanted it. Both used it and both had migrated properly within six months.

**CUSTOM STREAM → STATUS AND ARTIFACT EVENTS.** The longest, at eleven months, because their custom stream had accreted 31 event types over four years, of which 12 were undocumented and 6 were used by exactly one customer each.

Shadow testing here was mostly archaeology: establishing what each event type meant and which of the two new categories it belonged to.

Four event types turned out to be entirely unused and were removed rather than migrated.

### The measurement that made retirement possible

Per-concept, per-customer usage tracking. Wenlock could see, at any moment, which customers were still calling which old-shaped endpoints.

Retirement of each concept happened when its usage reached zero and stayed there for 30 days.

Without that measurement, every retirement would have been a guess.

### The one thing that broke

A customer's integration broke once, for about forty minutes, during the message-parts cutover.

The cause was on the customer's side — their parser assumed a field order that had never been guaranteed and that changed incidentally.

Wenlock's shadow testing had not caught it because the shadow comparison was semantic, not byte-level, and semantically the two were identical.

Their conclusion: shadow testing catches divergences in meaning, and cannot catch a consumer depending on something that was never part of the contract. That is what a conformance suite is for.

### Results

- **Total migration:** eleven months, all five concepts.
- **Customer-visible breakage:** one incident, forty minutes, caused by an undocumented consumer assumption.
- **Latent problems found by shadow testing:** 2 unsupported declared capabilities, 1 missing state causing retry storms, 4 unused event types.
- **Retry storms during peak:** attributed to network issues for a year, resolved by the `rejected` state.

### The line in their migration retrospective

*We never had a cutover date. We had five of them, and each one arrived when the measurement said it could.*

---

## Composition

Two bordered panels flanking a central migration column.

**Left panel:** headed **HISTORY ACP** with **(HISTORICAL)** beneath in coral. Five rows, each with a blue icon and a white detail card: **AGENT MANIFEST** (person badge with `{}` card), **RUN** (play disc with a step-sequence card), **MESSAGE** (speech bubble), **OUTPUT** (inbox tray), **CUSTOM STREAM** (pipe with wave lines).

**Right panel:** headed **CURRENT TARGET A2A 1.0**. Five rows: **AGENT CARD** (ID card with `{}` card), **TASK** (checked clipboard), **MESSAGE PARTS** (speech bubble with a puzzle piece), **ARTIFACT** (tray with a cube), **STATUS AND ARTIFACT EVENTS** (bell with a list).

**Centre, upper:** a blue **ADAPTER STRANGLER** bridge with two piers, spanning the gap beside the top two rows.

**Centre, lower:** a vertical stack of four dark rounded stages connected by teal arrows — **DUAL READ** (teal database), **SHADOW TEST** (teal magnifier), **CUTOVER** (teal branch glyph), **RETIRE** (coral bin, on a coral-tinted tile).

**Teal arrows** enter the stack from the left panel's rows and leave toward the right panel's rows.

## Element by element

**AGENT MANIFEST → AGENT CARD** — inventory becomes identity with attestation.
**RUN → TASK** — execution becomes a managed object with a lifecycle.
**MESSAGE → MESSAGE PARTS** — one blob becomes typed components.
**OUTPUT → ARTIFACT** — a return value becomes typed, plural deliverables.
**CUSTOM STREAM → STATUS AND ARTIFACT EVENTS** — bespoke becomes specified.

**ADAPTER STRANGLER** — a blue bridge with piers, spanning the two panels.

**DUAL READ** — both models read in parallel.
**SHADOW TEST** — new output compared and discarded.
**CUTOVER** — traffic moves.
**RETIRE** — the old path removed. Coral, with a bin.

## Colour and flow semantics

- **Coral** appears twice: on the **(HISTORICAL)** subtitle and on **RETIRE** — the retired origin and the irreversible final step.
- **Teal arrows** carry each concept from the old panel, down through the four stages, and out to the new panel.
- The **bridge is blue** — neither old nor new, the transitional structure.
- The **four stages are stacked vertically**, marking them as a sequence each concept passes through independently.
- Both panels are given **identical structure**, making the five mappings readable as pairs.

## How to present it

**Read the five mappings and ask which are more than renames.** Message parts and artifact — both shape changes, both plural where the old model was singular.

**Point at HISTORICAL in coral and clarify what it means.** Not wrong, not discarded. Every left-hand concept has a right-hand counterpart. The vocabulary moved and two shapes were refined.

**Ask why the pattern is called a strangler.** Gradual replacement, and at every moment something is standing. Then ask what the alternative is — a cutover date, coordinated across every consumer.

**Ask the room whether they could achieve a coordinated cutover.** Wenlock had 14 customers, two of whom ran 24-hour operations with no maintenance window. The answer is usually no once stated concretely.

**Walk the four stages as gates.** Do not shadow test until dual read is stable; do not cut over until shadow testing agrees; do not retire until measurement says nothing uses it.

**Spend the most time on shadow test.** Running everything twice and discarding the output. Expensive, and the only way to find divergences on real data.

**Tell the missing-`rejected`-state finding.** A fleet declining work returned a generic failure; customers' retry logic retried; retry storms at peak had been attributed to network issues for over a year. Shadow testing found it.

**Point out that each concept migrates independently.** Wenlock's manifests were at cutover while their custom stream was still at dual read. Eleven months for the longest, three for the shortest.

**Ask how they would know when to retire.** Per-concept, per-customer usage measurement, zero for 30 days. Without it, retirement is a guess.

**Give them the honest limit.** Wenlock's one breakage was a customer depending on field order that was never guaranteed. Shadow testing compares meaning; it cannot catch a consumer relying on something outside the contract. That is a conformance-suite job.

**Close on the retrospective line.** *We never had a cutover date. We had five of them, and each arrived when the measurement said it could.*

**Timing.** Twenty-five minutes. Thirty-five if you map the room's own legacy concepts onto the four stages and estimate each timeline.

---

## Lab and checkpoint

**Lab:** Map one legacy concept in your system onto a target protocol concept. Write the mapping, identify whether it is a rename or a shape change, and design the strangler-fig migration with the four stages: dual read, shadow test, cut over, retire. Define the measurement that would tell you it is safe to retire.

**Checkpoint:** Why is shadow test a stage that teams must not skip?

**Answer:** Because running both old and new paths against real data is the only way to find divergences that unit tests miss. It is expensive, but it catches real-world behaviour differences before cutover, as Wenlock found with the missing `rejected` state.

## Glossary

- **ACP** — the earlier agent-communication protocol being replaced.
- **A2A** — the target agent-to-agent protocol.
- **Cut over** — the stage where traffic is moved from the old path to the new.
- **Dual read** — the stage where both old and new models are read and compared.
- **Historical** — the status of a concept that exists in the legacy protocol, not a judgement.
- **Mapping** — the correspondence between an old concept and a new concept.
- **Retire** — the stage where the old implementation is removed.
- **Shadow test** — the stage where both implementations process real traffic and their outputs are compared.
- **Strangler bridge** — the pattern of gradually replacing a system while it continues to run.

## Sources

- Strangler fig migration patterns
- Protocol migration from ACP to A2A
- Shadow testing and gradual cutover
