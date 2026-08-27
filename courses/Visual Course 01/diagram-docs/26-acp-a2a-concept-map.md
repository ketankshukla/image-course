# Diagram 26 — ACP to A2A Concept Map

![A two-column translation table on dark navy. Five coral pills on the left — MANIFEST with a code document icon, RUN with a play button, INPUT with an inbox tray, OUTPUT with an outbox tray, and STATUS with a warning triangle — each connected by a cyan arrow to a teal pill on the right: AGENT CARD with an ID card, TASK with a checked clipboard, MESSAGE with a speech bubble, ARTIFACT with a document and cube, and TASK STATE with progress dots and a check. Column headers at the bottom read OLD TERMS in coral and CURRENT MODEL in teal.](../diagrams/26-acp-a2a-concept-map.png)

**Module:** 5 — ACP migration
**Role in the course:** migration inventory
**Layout:** two-column mapping, five rows

---

## At a glance

Five old terms on the left in coral, five current terms on the right in teal, one arrow each. **MANIFEST → AGENT CARD. RUN → TASK. INPUT → MESSAGE. OUTPUT → ARTIFACT. STATUS → TASK STATE.**

No architecture, no flow, no system. This is a translation table, and its usefulness is exactly its narrowness — it is the thing you hand to someone who has ACP-shaped knowledge and needs to speak the current vocabulary by this afternoon.

---

## What the diagram teaches

### 1. The one-to-one mapping is the reassurance

Every row has exactly one arrow. No concept splits into two, none merges, none is dropped, none appears on the right with no counterpart on the left.

That clean correspondence carries a message that matters as much as the content: **nothing was lost and nothing new was invented at the conceptual level.** The five things ACP identified as the necessary parts of agent interoperability are the same five things A2A identifies. They were renamed and refined, not replaced.

For someone who has invested in learning the old model, this is the difference between "your knowledge transfers" and "start again." The river diagram makes that argument visually; this one makes it structurally, row by row.

### 2. Each rename fixes an imprecision

The renames are not cosmetic. Each one corrects something the old term got slightly wrong.

**MANIFEST → AGENT CARD.** A manifest is a listing — a cargo inventory, a package's file list. It describes contents. An **agent card** describes an *identity*: who this agent is, what it can do, how to reach it, and how to verify it. The card metaphor carries identity and verification in a way "manifest" does not, which matters because the security checks in discovery are about identity rather than inventory.

**RUN → TASK.** A run is an execution — something that starts, executes, and ends. A **task** is a unit of work with an owner, a lifecycle, and a state that outlives any single execution. A task can be queued before it runs, can pause awaiting input, can be cancelled. "Run" implies a process; "task" implies a managed object.

**INPUT → MESSAGE.** Input is what you feed a function. A **message** is a communication with a sender, and it can be one of several in an exchange. The rename accommodates the fact that agent interactions are conversational — a task may involve several messages, including clarifying questions from the specialist.

**OUTPUT → ARTIFACT.** The most consequential rename. Output is whatever the function returned. An **artifact** is a produced deliverable with a type and a schema, which can be stored, referenced, validated, and rejected. That last property is what the entire artifact-validation gate depends on.

**STATUS → TASK STATE.** Status is a flag. **Task state** is a position in a defined lifecycle, with permitted transitions between positions. The rename makes it a state machine rather than a string.

### 3. Output to artifact is the one that changes code

Four of these are renames you can do with find-and-replace. This one usually is not.

The shape differences:

- **Cardinality.** Output tends to be singular. A task can produce **several artifacts** — a translation task returning one per locale, an analysis task returning a report and a dataset.
- **Typing.** An artifact declares what it is, which is what makes schema validation possible.
- **Independence.** An artifact persists beyond the exchange. It can be referenced in an audit record months later.
- **Rejectability.** Because it has a declared shape and inspectable content, an artifact can be refused on principled grounds.

That last property is load-bearing for the whole security model:

![Five stages — MINIMIZE CONTEXT, ALLOWLIST AGENT, BIND TASK, VALIDATE ARTIFACT, LOCAL APPROVAL — with a checklist of schema, signature, content and policy checks and a coral warning cube dropping into a bin.](../diagrams/23-a2a-security-gates.png)

A codebase that models returns as a single untyped output has no place to put four validation checks. The rename to artifact is what makes that gate implementable.

### 4. Status to task state is the second real change

A string field becomes a state machine, and state machines have properties strings do not: a defined set of values, permitted transitions, and terminal states.

The practical consequence is that migrating teams usually discover their old status enumeration was incomplete. The common gaps:

- **input-required** — the specialist needs a clarification before it can proceed. ACP-era models rarely had this, and without it a specialist facing ambiguity has to guess or fail.
- **rejected** — distinct from failed. The specialist declined to accept the task, which is different from accepting it and being unable to complete it.
- **cancelled** — the caller withdrew it.
- **queued** — accepted but not started, which callers need distinguished from running.

The task lifecycle diagram shows the shape these states sit in:

![Five numbered panels — MESSAGE, TASK, WORKING at 65%, ARTIFACT, COMPLETED — with a bright cyan rail beneath whose arrows point up into every stage.](../diagrams/20-a2a-task-lifecycle.png)

### 5. The old column's icons are quietly critical

Look at the left-hand icons and compare them to the right.

**Manifest** is a code document; **agent card** is an ID card with a person on it. Inventory versus identity.

**Run** is a play button — press and it executes. **Task** is a clipboard with a check. Trigger versus managed object.

**Input** is an inbox tray; **output** is an outbox tray. A pair of trays, which is a *function* metaphor — things go in one side and out the other. On the right, **message** is a speech bubble and **artifact** is a document with a cube badge. Conversation and deliverable. Completely different mental model, communicated entirely through iconography.

**Status** is a **warning triangle** — an alert, something that fires when wrong. **Task state** is progress dots with a check — a position on a track. Exception versus lifecycle.

The icons are doing more teaching than the words.

### 6. Vocabulary alignment is the point, not correctness

A team using the old vocabulary internally is not broken. Their system works. What they lack is the ability to interoperate without a translation conversation at every boundary.

The value of a shared protocol is entirely in being shared. A private dialect of a public protocol delivers the design benefits and none of the interoperability benefits, which is most of the reason to adopt it.

---

## Case study — Kestrel Logistics, the two-day rename

Kestrel is a freight and warehousing company. During a platform inventory of their agent integrations, one squad's work was found to be built on ACP-era vocabulary — a manifest endpoint, a run API, input and output objects, and a status string.

The engineer had learned the model from material written before the merge. Nothing was broken. It had been in production for four months.

### Why it mattered

It surfaced when Kestrel's compliance team stood up their own dangerous-goods adjudication agent, built against current A2A. The two agents could not talk to each other without a translation layer, despite both being internal, both being well-built, and both implementing the same five concepts.

The cost was not conceptual. It was that Kestrel would have to build and maintain an adapter between two of their own services because they had used different names for the same things.

### The mechanical part

Four of the five were straightforward.

**Manifest → agent card.** Endpoint moved to the well-known path, field names updated. Half a day, mostly because the manifest was cached by two clients that needed updating in step.

**Run → task.** Renamed throughout, including the database table and its columns. The rename was easy; the migration of in-flight rows needed a maintenance window.

**Input → message.** Direct rename. Their design had only ever sent one input per run, so nothing structural changed — though they noted that message being plural-capable meant they could later support clarification exchanges, which they could not before.

**Status → task state.** Renamed, and then extended. Their old status enumeration had four values: `pending`, `active`, `complete`, `error`. They added `input_required`, `rejected` and `cancelled`.

The addition of `rejected` closed a real bug. Their old model had no way for a specialist to decline a task, so a specialist that could not accept work returned `error` — which the caller's retry logic interpreted as transient and retried, up to five times, against an agent that was never going to accept it.

### The part that was not mechanical

**Output → artifact** took most of the two days.

Their `output` was a single JSON object with no declared type. Migrating meant:

- **Making it a collection.** Straightforward, though it changed the response shape for every consumer.
- **Adding a declared type per artifact.** This required deciding what the types actually were, which surfaced that two different agents were returning structurally different objects both called "output," and no consumer had noticed because nothing was validating.
- **Adding schema validation on receipt.** This is the change that mattered. Within a week of enabling it, they caught an agent returning a field that had been renamed on its side three weeks earlier. Under the old untyped model, consumers had been reading `undefined` and treating it as an empty value.

That bug had been live for three weeks and had silently produced incorrect dangerous-goods classifications on a small number of shipments. It was found by the schema check, not by anyone noticing bad output.

### What the migration produced

Two days of work, one maintenance window, and:

- Direct interoperability with the compliance team's agent, no adapter.
- A retry bug fixed that had been re-submitting to a refusing agent.
- A silent field-rename bug caught that had been producing wrong classifications.
- Three lifecycle states added that they had needed and worked around.

The team's own assessment was that they went in expecting a cosmetic rename and came out having fixed three real defects — all of which existed because the old vocabulary had no place to express the distinctions that would have caught them.

### The rule they wrote down

*Use the public names for public concepts.* Internal naming is a matter of taste until it reaches a boundary, at which point a private dialect costs an adapter and hides the distinctions the public model was designed to make explicit.

---

## Composition

Two vertical columns of five rounded pills, connected row by row by horizontal cyan arrows.

The left column is **coral**; the right column is **teal**. Each pill carries an icon on its left and the term in white uppercase. Beneath each column sits a header platform: **OLD TERMS** in coral on the left, **CURRENT MODEL** in teal on the right, each with a small database icon in its own colour.

No flow, no architecture — a lookup table.

## Element by element

| Old term (coral) | Icon | → | Current term (teal) | Icon |
| --- | --- | --- | --- | --- |
| **MANIFEST** | White document with `</>` code marks | → | **AGENT CARD** | ID card showing a person and detail lines |
| **RUN** | Circular **play button** | → | **TASK** | Clipboard with a **green check badge** |
| **INPUT** | Blue **inbox tray** with a document descending into it | → | **MESSAGE** | White **speech bubble** with three dots |
| **OUTPUT** | Blue **outbox tray** with a document rising from it | → | **ARTIFACT** | White document with a **teal cube badge** |
| **STATUS** | Coral **warning triangle** with an exclamation | → | **TASK STATE** | Pill showing **progress dots and a teal check** |

**Column headers**
Two dark platforms at the bottom of each column: **OLD TERMS** in coral with a coral database icon; **CURRENT MODEL** in teal with a teal database icon.

## Colour and flow semantics

- **Coral** for the entire old column, consistent with coral meaning retired throughout the library.
- **Teal** for the entire current column.
- **Cyan arrows**, one per row, all identical in weight — no rename is presented as more significant than another, though in practice two are.
- The **icon pairs** carry the semantic shift: inventory→identity, trigger→managed object, tray-pair→conversation-and-deliverable, alert→lifecycle position.
- Rows are evenly spaced with no grouping, reinforcing that this is a lookup rather than an argument.

## How to present it

**Show the river first, then this.** The timeline establishes that migration is warranted and that nothing was wasted. This one is the actual work. Presented alone, this can read as arbitrary churn; presented second, it reads as the translation step of a lineage the room has already accepted.

**Read the five pairs aloud, then stop.** For someone with ACP knowledge, thirty seconds is genuinely enough to unblock them. Do not elaborate before they have had the list.

**Then ask which two are more than renames.** Let the room work it out. **Output → artifact** and **status → task state**. Both change shapes, not just names, and both are where the migration work actually is.

**Interrogate output → artifact.** Ask what an artifact can do that an output cannot. Build the list: multiple, typed, persistent, rejectable. Then ask what depends on rejectability — the artifact-validation gate, which cannot be implemented against an untyped single output. This is the clearest illustration that the renames encode capability, not fashion.

**Ask what states their status field has.** Then read out the four commonly missing ones: input-required, rejected, cancelled, queued. Ask what their system does today when a specialist needs a clarification. Kestrel's retry-against-a-refusing-agent bug is a good story here, because it is the kind of defect that hides for months.

**Do the icon reading.** Cover the words and ask what each pair of icons says. Inbox and outbox trays versus a speech bubble and a document — a function versus a conversation. This is a quick exercise and it makes the renames feel motivated rather than imposed.

**Ask where else the old vocabulary lives.** Not just code. Design documents, internal onboarding material, API documentation, database column names, log field names. Documentation is the one that propagates.

**Leave them the rule.** *Use the public names for public concepts.* Internal naming is taste until it reaches a boundary; then it costs an adapter.

**Timing.** Ten minutes. Fifteen if you work through the two shape changes properly, which is worth it for anyone actually migrating.

---

## Lab and checkpoint

**Lab:** Take a small inventory of one of your own services — its API resource names, its log field names, and any internal documentation — and list every place it uses an old or private name for a concept that has a public A2A equivalent. For each one, decide whether the name is purely internal (reaches no boundary) or reaches a public boundary. For every public-boundary case, write the migration path to the public term and one test that would fail if the private name leaked into a message or artifact.

**Checkpoint:** Why is *output → artifact* more than a rename?

**Answer:** Because an artifact is a typed, persistent, rejectable deliverable that can be plural. A single untyped output has no place to attach schema validation, cannot be rejected on principled grounds, and cannot carry multiple deliverables. The rename to artifact is what makes the artifact-validation gate implementable.

## Glossary

- **Agent card** — a discoverable identity record that describes who an agent is, what it can do, and how to verify it.
- **Artifact** — a produced deliverable with a declared type and schema, which can be stored, referenced, validated, and rejected.
- **Manifest** — an older ACP term for a listing of capabilities, with less emphasis on identity and verification.
- **Message** — a communication between agents, carrying sender identity and supporting multi-turn exchange.
- **Run** — an older ACP term for a single execution.
- **Status** — an older ACP string flag describing a current condition.
- **Task** — a unit of work with an owner, a defined lifecycle, and a state that can outlive any single execution.
- **Task state** — a position in a defined lifecycle state machine with permitted transitions and terminal states.

## Sources

- A2A Agent Card and Task lifecycle specification drafts
- ACP (Agent Communication Protocol) predecessor vocabulary
- Google A2A protocol documentation: agent-to-agent task and artifact model
