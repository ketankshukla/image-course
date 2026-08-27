# Diagram 126 — Commands, Events, Invariants, and State

![A USER COMMAND person figure on dark navy leads to VALIDATE INVARIANTS, a teal shield with a check. A teal VALID branch leads to EVENT, then APPEND-ONLY HISTORY as stacked teal cylinders, then REDUCER as a teal gear, then into a dashed STATE panel showing OPEN with an open door above WAITING APPROVAL with an hourglass, joined by a teal STATE TRANSITION (VIA REDUCER) arrow. A coral INVALID branch leads to COMMAND REJECTED, a red octagon, whose coral dashed line to the state is cut by a red X labelled STATE UNCHANGED (OPEN REMAINS).](../diagrams/126-command-event-state-machine.png)

**Module:** Durable-system foundation
**Role in the course:** how state changes, and how it does not
**Layout:** a command validated into an event, appended and reduced into state, with a rejection that changes nothing

---

## At a glance

A command is **validated against invariants**. Valid, it becomes an **event**, is **appended to history**, and is **reduced into state**. Invalid, it is **rejected** — and a red X cuts the path to the state, labelled **STATE UNCHANGED (OPEN REMAINS)**.

Four object types, named in the legend: **COMMAND, INVARIANT, EVENT, STATE**.

A command is a request. An event is a fact. The gate between them is where correctness lives.

---

## What the diagram teaches

### 1. Four object types, and confusing any two is a design error

**COMMAND** — a request to change something. It can be refused. It expresses intent, and it may be wrong.

**INVARIANT** — a rule that must always hold. Not a validation of the command's shape; a property of the system that no state may violate.

**EVENT** — a record that something happened. Past tense, immutable, and it cannot be refused because it has already occurred.

**STATE** — the current situation, derived.

The most common conflation is command and event. A system that appends the request rather than the fact has recorded intentions, not history — and replaying intentions replays the guesses as well as the outcomes.

### 2. Validation happens before the event exists, and that ordering is everything

**USER COMMAND → VALIDATE INVARIANTS → EVENT.**

The shield sits between them.

That means an event is only created for a command that passed. There is no such thing as an invalid event in the history.

The consequence: **replaying history can never produce an invalid state**, because every event in it was validated at the moment it was created. That is what makes an append-only history trustworthy as a source of truth.

A system that appends first and validates later has a history containing events that should not have happened, and every replay reproduces them.

### 3. APPEND-ONLY is the property that makes history a fact

Stacked teal cylinders, labelled **APPEND-ONLY HISTORY**.

Events are added. Nothing is modified, nothing is removed.

Three things follow.

**History is auditable.** What is in it is what happened, and nobody edited it afterwards.

**State is reproducible.** Replaying the same events through the same reducer produces the same state, every time.

**Correction is additive.** A mistake is corrected by appending a corrective event, not by editing the erroneous one. The record shows both the error and its correction, which is usually what an auditor wants.

### 4. The REDUCER is a gear, and state is derived rather than stored

A teal gear between history and state.

State is not a thing you write. It is a thing you **compute** from history.

That inversion is the core of event sourcing, and it has a practical consequence worth stating: **the state is disposable**. If it is corrupted, lost, or found to be computed incorrectly, you rebuild it from history.

You cannot rebuild history from state.

### 5. The state panel shows two states and one transition, and both are drawn

Inside a dashed boundary: **OPEN** with an open door, above **WAITING APPROVAL** with an hourglass, joined by a teal arrow labelled **STATE TRANSITION (VIA REDUCER)**.

The parenthetical matters. The transition happens **via the reducer** — it is not something the command did directly.

A command does not set the state to waiting-approval. It produces an event, and the reducer's interpretation of that event produces the transition.

That indirection is what lets you change how state is derived without changing what was recorded.

### 6. The rejection path is cut, and the label states the consequence

**COMMAND REJECTED** — a red octagon — with a coral dashed line toward the state, **cut by a red X**, labelled **STATE UNCHANGED (OPEN REMAINS)**.

Drawing the path and then cutting it is stronger than omitting it. A rejected command *tried* to change the state and did not.

The parenthetical — **OPEN REMAINS** — names the specific outcome. The state is not "invalid" or "error"; it is exactly what it was before.

That is what a rejection should produce: no event, no history entry, no state change. The system is in the same condition as if the command had never been sent.

### 7. A rejection produces no event, which means it is invisible in history

Worth stating because it is a real gap.

Following the diagram literally, a rejected command leaves no trace. History contains only what happened, and the rejection did not happen.

Most production systems need rejections to be observable — for debugging, for detecting probing, for understanding why a user's action did not work.

The resolution is usually a separate rejection log rather than an entry in the event history, precisely so that the history remains a record of facts rather than a mixture of facts and refusals.

The reason the history must stay clean is that it is the source from which state can be rebuilt:

![On dark navy, APPEND-ONLY EVENTS 1 TO 900 as numbered white cards lead to SNAPSHOT AT 800 with a camera and green tick, then a play-button card reads REPLAY 801 TO 900, and finally a database card labelled CURRENT STATE. Above, CODE V1 and CODE V2 feed a VERSION GATE archway; a cyan arrow from the gate enters replay, while a coral arrow leads to INCOMPATIBLE EVENT and MIGRATION TEST. Six teal outputs fan from CURRENT STATE, including CLEAN HISTORY, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT and RESUME.](../diagrams/127-snapshot-replay-schema-evolution.png)

This is what the command-event diagram makes possible once every event has been validated. Because only valid events enter the append-only history, the state can be deleted and rebuilt from that history. The green tick above the snapshot is the claim that the history is trustworthy enough to be the source of truth. A rejected command never appears in that history, so it never has to be explained away during replay.

---

## Case study — Aldermoor Building Society, the state that could not be rebuilt

Aldermoor is a mutual lender with about 190,000 members. Their mortgage application workflow runs from submission through underwriting to offer, and takes between three days and four months.

### What they had

A state column on the application record, updated in place, plus an audit table recording changes.

Applications moved through states: `submitted`, `documents_pending`, `underwriting`, `waiting_approval`, `offered`, `declined`, `withdrawn`.

### The first symptom

Applications appeared in states that should have been unreachable.

An application in `offered` with no underwriting decision. An application in `underwriting` that had already been declined. Roughly 200 applications over eighteen months in states their process did not permit.

Each one was investigated manually and corrected by setting the state to what it should have been.

### What was actually happening

Three causes, all of which the event-sourced design would have prevented.

**Concurrent updates.** Two processes writing the state column, second overwriting first. Their audit table recorded both writes, but the state column held only the last one.

**Direct updates.** Their operations team had a support tool that set the state directly, bypassing the transition logic entirely. It was used about 40 times a month for legitimate corrections, and each use could produce an invalid state.

**Failed multi-step transitions.** Moving from `underwriting` to `offered` involved writing the state, creating an offer record, and notifying the applicant. A failure partway left the state changed and the offer missing.

### The audit finding that forced the rebuild

Their internal audit function asked a question: **for a given application, reconstruct the sequence of decisions and who made them.**

The audit table recorded state changes with timestamps and user IDs. It did not record *why* — the evidence a decision rested on, the invariant that permitted it, or the command that requested it.

Worse, for the 200 corrected applications, the audit table recorded the correction and not the invalid state that preceded it, because corrections had been applied by direct update.

**They could show the states an application had been in. They could not show that any transition had been valid.**

### The rebuild as commands, events and a reducer

**Commands validated against invariants before any event exists.**

Their invariants, written down for the first time:

- An application cannot reach `offered` without a recorded underwriting decision.
- An application cannot re-enter `underwriting` after `declined` without an explicit reopening event.
- An application cannot be in `offered` and `withdrawn` simultaneously.
- The loan amount on an offer cannot exceed the amount underwritten.

Four invariants, and enumerating them was the most valuable part of the exercise. Two of them had never been enforced anywhere, and the 200 invalid applications were mostly violations of the first.

**Events appended, never modified.**

`ApplicationSubmitted`, `DocumentsReceived`, `UnderwritingDecisionRecorded`, `OfferIssued`, `ApplicationDeclined`, `ApplicationWithdrawn`, `ApplicationReopened`.

**State derived by a reducer.**

Their state column became a projection, rebuilt from events. It is still stored — for query performance — and it is no longer authoritative.

**The support tool was rebuilt to issue commands.**

This was the contentious change. Their operations team wanted the ability to set a state directly, because sometimes the right answer is a state that no command produces.

The compromise: a `StateCorrectionApplied` command that requires a reason, an approver, and produces an event like any other. It is validated against a reduced set of invariants — it can do things ordinary commands cannot — and it is fully recorded.

It is used about 12 times a month, down from 40, because two thirds of the previous uses had been correcting problems that no longer occur.

### The rebuild test

Six weeks after launch they deleted their state projection entirely and rebuilt it from events.

**Every application arrived at the same state**, except for four — all of which were applications whose state had been set by direct update before the migration, and whose event history therefore did not explain their state.

Those four were investigated and corrected with explicit correction events. Their history now explains them.

### What the audit function got

Given an application, they can now produce: every command issued, whether it was accepted or rejected and against which invariant, every event appended, the state after each event, and who issued each command.

Their audit lead's assessment: the previous audit table showed *what the state had been*; the event history shows *why it was permitted to become that*.

### Results

- **Applications in invalid states:** ~200 over eighteen months → 0.
- **Direct state updates:** ~40/month → 12/month, all recorded as commands with reasons and approvers.
- **Invariants enforced:** 2 of 4 → 4 of 4 (and enumerating them found the two that were not).
- **State rebuild from history:** newly possible; 4 discrepancies found on first run, all pre-migration.
- **Audit reconstruction:** state sequence only → full command, invariant, event and actor chain.

### The line in their engineering standard

*The state column is a cache. If you cannot delete it and rebuild it from history, it is not a cache — it is the only copy, and you have no history.*

---

## Composition

A left-to-right flow with a two-way branch and a state panel on the right.

**Left:** **USER COMMAND** — a blue person figure on a blue platform — a cyan arrow to **VALIDATE INVARIANTS** — a large **teal shield with a white check** on a blue platform.

**Upper branch:** a **teal arrow labelled VALID** to **EVENT** — a teal document glyph — then a teal arrow to **APPEND-ONLY HISTORY** — stacked teal cylinders — then a teal arrow to **REDUCER** — a teal gear — then a teal arrow into the state panel.

**Right:** a **dashed blue boundary** labelled **STATE**, containing a white card with an **open door** labelled **OPEN**, and beneath it a white card with an **hourglass** labelled **WAITING APPROVAL**, joined by a **teal arrow** labelled **STATE TRANSITION (VIA REDUCER)**.

**Lower branch:** a **coral arrow labelled INVALID** to **COMMAND REJECTED** — a **red octagon with a white ✗** on a blue platform — then a **coral dashed line** rightward toward the state, **cut by a large red ✗**, labelled **STATE UNCHANGED (OPEN REMAINS)** in coral.

**Legend:** four bordered tiles — a blue person and **COMMAND**; a teal shield and **INVARIANT**; a document and **EVENT**; an hourglass and **STATE**.

## Element by element

**USER COMMAND** — a request. Refusable.
**VALIDATE INVARIANTS** — a teal shield. Rules that must always hold.
**EVENT** — a fact. Past tense, immutable.
**APPEND-ONLY HISTORY** — stacked cylinders. Nothing modified, nothing removed.
**REDUCER** — a gear. State is computed, not written.
**STATE** — OPEN and WAITING APPROVAL, inside a dashed boundary.

**COMMAND REJECTED** — a red octagon, its path to the state cut.

## Colour and flow semantics

- **Cyan** carries the command into validation.
- **Teal** carries the valid path through event, history, reducer and into state — the volume's event and acknowledgement colour.
- **Coral** carries the invalid path to rejection, and the cut line beyond it.
- The **red ✗ on the rejection's path** is the diagram's key device: the attempt is drawn and stopped.
- The **dashed boundary** around the state marks it as derived rather than as another stage.

## How to present it

**Read the four legend tiles and ask for the difference between a command and an event.** A request that can be refused, and a fact that already happened. Then ask which their system appends.

**Point at where validation sits.** Before the event exists. Then give the consequence: replaying history can never produce an invalid state, because every event in it was validated when created.

**Ask what a system that appends first and validates later has.** A history containing events that should not have happened, reproduced on every replay.

**Explain append-only in terms of correction.** A mistake is corrected by appending a corrective event, not by editing. The record shows both, which is usually what an auditor wants.

**Point at the reducer and make the inversion explicit.** State is computed, not written. Which means state is disposable and history is not.

**Ask the rebuild question.** Can they delete their state and rebuild it from history? Then give Aldermoor's test: they did, and four applications did not arrive at the same state — all four with histories that did not explain them.

**Tell the invalid-states story.** 200 applications in states their process did not permit, from concurrent writes, direct updates and failed multi-step transitions.

**Give them the invariant-enumeration finding.** Writing down four invariants revealed that two had never been enforced anywhere, and that most of the 200 violated the first.

**Present the support-tool compromise.** Operations wanted direct state setting. The answer was a correction *command* with a reason, an approver, and an event — validated against a reduced invariant set, fully recorded, and used a third as often once the underlying problems stopped occurring.

**Point at the cut path and read the parenthetical.** *OPEN remains.* Not error, not invalid — exactly what it was.

**Name the gap.** A rejection leaves no trace in history. Most systems need a separate rejection log, precisely so history stays a record of facts.

**Close on the standard.** *The state column is a cache. If you cannot rebuild it, it is the only copy and you have no history.*

**Timing.** Twenty-five minutes. Thirty-five if you enumerate your own invariants, which reliably finds one that is not enforced.

---

## Lab and checkpoint

**Lab:** Pick one state in your system and re-model it with commands, events, and a reducer. Write one command, the validation it passes, the event it appends, and the reducer rule. Then attempt to rebuild the current state by replaying all events. Identify any state that cannot be rebuilt and any invariant that is not enforced.

**Checkpoint:** Why is the state panel a cache, not the source of truth?

**Answer:** Because the state is derived from the event history by the reducer. If the state is lost, it can be rebuilt from the append-only history. If it cannot be rebuilt, then the state is the only copy, and there is no durable record of what happened.

## Glossary

- **Append-only** — the property that history is never edited, only added to.
- **Command** — a request to change state, which can be refused.
- **Event** — a fact that has happened and is recorded in history.
- **Invariant** — a rule that state must always satisfy.
- **Reducer** — the function that computes state from a sequence of events.
- **Rejection** — a refused command, which produces no event.
- **Replay** — re-deriving state by reprocessing the event history.
- **State** — the derived view of the current condition.
- **State machine** — the allowed states and transitions for an object.
- **Validation** — the check that a command is allowed before an event is created.

## Sources

- Command, event, and reducer patterns
- Event sourcing and append-only history
- State machine invariants and validation
