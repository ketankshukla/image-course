# Diagram 73 — Typed Agent Event Stream

![An event pipeline on dark navy. Eight numbered event platforms run left to right — RUN STARTED, STEP STARTED, TEXT DELTA, TOOL CALL STARTED, TOOL CALL RESULT, STATE SNAPSHOT, ARTIFACT READY, RUN FINISHED. Cyan lines gather them into a REACT REDUCER panel captioned TURNS EVENTS INTO UI STATE. Below, cyan arrows fan out to five UI cards — CHAT, PROGRESS at 65%, TOOL CARD, STATE PANEL, ARTIFACT CARD. At the bottom, EVENT ID and RUN ID tags sit beside a coral RECONNECT badge leading to a card reading AFTER LAST EVENT — Resuming from latest known state.](../diagrams/73-typed-agent-event-stream.png)

**Module:** The complete system
**Role in the course:** turning a stream of typed events into a live interface
**Layout:** eight event types funnelling into a reducer, fanning out to five UI surfaces, with a reconnect path beneath

---

## At a glance

Eight **typed** events, a reducer that turns them into UI state, and five surfaces that render it. Underneath, an **EVENT ID** and a **RUN ID**, and a **RECONNECT** path that resumes **AFTER LAST EVENT**.

The word *typed* is the whole design. These are not log lines or chat chunks — they are named event kinds with defined shapes, and because they are typed, a client can render each one differently without parsing prose.

---

## What the diagram teaches

### 1. Eight event types, and each one enables a different piece of interface

**1 RUN STARTED** — work has begun. The UI can show that something is happening.
**2 STEP STARTED** — a named phase within the run. Enables a meaningful progress label rather than a spinner.
**3 TEXT DELTA** — incremental text. Enables streaming output as it is produced.
**4 TOOL CALL STARTED** — a capability is being invoked. Enables showing *what* the agent is doing, not just that it is busy.
**5 TOOL CALL RESULT** — that call returned. Enables showing outcomes per call.
**6 STATE SNAPSHOT** — the complete current state. The synchronisation point.
**7 ARTIFACT READY** — a deliverable exists. Enables offering it before the run completes.
**8 RUN FINISHED** — terminal.

The reason to type them rather than stream undifferentiated text: **a client can only render what it can distinguish.** A tool call rendered as a card with a name and a result is useful. The same information embedded in prose is not.

### 2. Text delta and state snapshot are two different transmission models

This is the most important technical distinction in the diagram.

**TEXT DELTA** is **incremental** — each event carries a fragment, and the client accumulates. Efficient, and it requires every fragment to arrive in order.

**STATE SNAPSHOT** is **complete** — each event carries the whole current state, replacing whatever the client held. Larger, and self-correcting.

Having both is deliberate. Deltas keep the stream light during normal operation; snapshots provide recovery points. A client that has missed deltas can be brought back into sync by the next snapshot without replaying anything.

The design question this raises — how often to send a snapshot — is a trade between bandwidth and recovery granularity, and the diagram does not answer it. Every few seconds, or at step boundaries, is typical.

### 3. The reducer is a single named component, and that is an architectural claim

The panel reads **REACT REDUCER — TURNS EVENTS INTO UI STATE**.

One place where events become state. Not five components each subscribing to the stream and maintaining their own view.

Two consequences.

**Consistency.** All five surfaces render from one state object, so they cannot disagree. A progress bar showing 65% and a tool card showing a call still in flight are derived from the same source.

**Testability.** A reducer is a pure function from events to state. You can replay a recorded event sequence and assert the resulting state, which makes UI behaviour testable without a browser.

### 4. Five surfaces, and each consumes a subset

**CHAT** — from text deltas.
**PROGRESS** — from step-started and run-lifecycle events. Shows **65%**.
**TOOL CARD** — from tool-call-started and tool-call-result.
**STATE PANEL** — from state snapshots.
**ARTIFACT CARD** — from artifact-ready.

Each surface subscribes to what it needs. Adding a sixth surface means deriving new state from existing events, not adding new events.

That is the payoff of typing them: the event vocabulary is stable, and the interface can evolve against it.

### 5. Two identifiers, and they do different jobs

**EVENT ID** — `evt_01H8ZWN3X7Q62Y5M`. Identifies one event.
**RUN ID** — `run_01H8ZWNA2J4C9B7F`. Identifies the whole run.

Both are needed and they are not interchangeable.

The run ID is what a client presents to resume. The event ID is what it presents to say **where it got to**. Without the second, a reconnecting client can only ask for the whole run again.

The identifiers are sortable — the format encodes time — which means "after this event" is a meaningful and cheap query.

### 6. RECONNECT resumes AFTER LAST EVENT, and that is the diagram's payoff

The coral **RECONNECT** badge leads to a card reading **AFTER LAST EVENT — Resuming from latest known state**.

A dropped connection is normal. Wi-Fi drops, a laptop sleeps, a proxy times out, a deploy cycles the server.

Three possible behaviours on reconnect:

**Restart the run.** Wasteful and often impossible — side effects have occurred.
**Replay from the beginning.** Correct but slow, and it re-renders everything the user already saw.
**Resume after the last event received.** Correct and cheap.

The third requires the client to know its last event ID and the server to be able to serve from that point. Both are visible in the diagram.

The coral colouring is right: a reconnect is an abnormal condition being handled, not a normal path.

### 7. Artifact ready comes before run finished, and that ordering is useful

Event 7 precedes event 8.

A deliverable can exist before the run completes. A report generated at step four of six can be offered to the user while steps five and six continue.

Systems that only surface outputs at completion make users wait for work that is already done.

It also means artifacts survive a failure that happens later:

![Three columns — LIVE PROGRESS with four named steps, ARTIFACTS listing an evidence pack, decision summary and audit receipt with a COMPLETED EARLIER badge, and RECOVERY offering retry, continue, change input and contact human — joined by a coral PARTIAL FAILURE tile.](../diagrams/74-progress-artifacts-and-recovery-ux.png)

An artifact emitted at event 7 is still on the user's screen if the run fails at event 8. That is the interface consequence of emitting it early.

---

## Case study — Wardley Tax, the streaming rebuild

Wardley provides corporation-tax software to about 2,000 accounting practices. Their assistant prepares draft computations: it reads the trial balance, applies adjustments, checks reliefs, cross-references prior years, and produces a draft return with a working paper.

A full computation takes between 90 seconds and six minutes.

### The first version

Text streaming only. The assistant streamed its reasoning as prose, and the interface rendered it in a chat panel.

It looked responsive and it was close to unusable for the actual job.

**Accountants could not see what it was doing.** The prose described the work — "now checking capital allowances" — but there was no structure. Tool calls, retrievals and adjustments all appeared as sentences.

**A connection drop lost everything.** No run identity, no event identity. A reconnecting client had no way to resume, so the interface restarted the conversation. On a six-minute computation this happened often enough that accountants learned to not touch anything while it ran.

**Artifacts appeared only at the end.** The working paper existed after about 40% of the run, and nobody saw it until 100%.

**Nothing was testable.** UI behaviour could only be verified by running the system and watching.

### The rebuild as typed events

Eight event types, matching the diagram.

**STEP STARTED** carries a named phase: `reading_trial_balance`, `applying_adjustments`, `checking_reliefs`, `cross_referencing_prior_year`, `generating_working_paper`, `assembling_return`.

Six named steps meant a real progress indicator and, more importantly, a **meaningful label**. An accountant seeing "checking reliefs" for 40 seconds knows that is normal. Seeing "reading trial balance" for 40 seconds knows something is wrong.

**TOOL CALL STARTED and TOOL CALL RESULT** render as cards. Each shows what was called, against what, and what came back. This is what accountants asked for most: they wanted to see the figures being pulled, not a description of them being pulled.

**STATE SNAPSHOT every ten seconds and at each step boundary.** Carries the current computation state — adjustments applied so far, reliefs identified, running totals.

**ARTIFACT READY** fires when the working paper is generated, at roughly 40% of the run. Accountants can open it while the return assembly continues.

That change alone removed about 90 seconds of perceived wait on a typical computation, without making anything faster.

### The reconnect fix

Every event carries a sortable ID. The client stores the last one it received. On reconnect it sends the run ID and the last event ID, and the server replays from that point.

**Reconnects went from losing the session to being invisible.** In their telemetry, about 8% of computations experience at least one reconnect — laptops sleeping, office wifi, VPN cycling. Before, all 8% were restarts. Now none of them are visible to the user.

### The reducer, and the testing benefit they had not anticipated

One reducer, five surfaces.

The unanticipated benefit was testing. They recorded event sequences from real computations — including unusual ones, failures, and reconnects — and built a test suite that replays them against the reducer and asserts the resulting state.

**UI regressions became catchable in CI.** Previously, a change to the tool card rendering could only be verified by running a computation and looking. Now a recorded sequence from a computation with an unusual relief structure runs in milliseconds and asserts that the card shows the right figures.

They have 140 recorded sequences. Four of them are reconnect scenarios that would be almost impossible to reproduce manually.

### Results

- **Perceived wait on a typical computation:** reduced ~90 seconds by early artifact delivery, with no speed change.
- **Reconnects causing session loss:** 8% of runs → 0.
- **UI regressions reaching release:** roughly one per quarter → none in fourteen months.
- **Accountant-reported "I can't tell what it's doing":** eliminated as a support category.

### The line their front-end lead uses

*Streaming text tells you it is alive. Typed events tell you what it is doing.*

---

## Composition

Three horizontal bands.

**Upper:** eight numbered event platforms left to right, each a teal icon above a white card, connected by cyan arrows. Cyan lines descend from all eight and gather into a single arrow.

**Middle:** a dark bordered panel with a React atom glyph reading **REACT REDUCER** and, beneath, **TURNS EVENTS INTO UI STATE**.

**Lower:** cyan arrows fan from the reducer to five white UI cards. Beneath them, **dashed cyan lines** connect to a row containing an **EVENT ID** tag, a **RUN ID** tag, a **coral RECONNECT badge**, and a card reading **AFTER LAST EVENT — Resuming from latest known state**.

## Element by element

**The eight events**
**1 RUN STARTED** (teal play disc) · **2 STEP STARTED** (teal gear) · **3 TEXT DELTA** (teal speech bubble with dots) · **4 TOOL CALL STARTED** (teal terminal `>_`) · **5 TOOL CALL RESULT** (teal check disc) · **6 STATE SNAPSHOT** (teal database stack) · **7 ARTIFACT READY** (teal document) · **8 RUN FINISHED** (chequered flag).

**REACT REDUCER**
A dark panel with a teal React atom and two lines of white text.

**The five surfaces**
**CHAT** (message bubble card) · **PROGRESS** (bar reading **65%**) · **TOOL CARD** (terminal glyph card) · **STATE PANEL** (database with bullet rows) · **ARTIFACT CARD** (document card).

**The identifiers**
Two outlined teal tags: **EVENT ID / evt_01H8ZWN3X7Q62Y5M** and **RUN ID / run_01H8ZWNA2J4C9B7F**.

**RECONNECT**
A **coral badge** with a warning triangle, with a coral arrow leading to a dark card reading **AFTER LAST EVENT** in white and **Resuming from latest known state** in coral.

## Colour and flow semantics

- **Cyan** carries events into the reducer and state out to the surfaces.
- **Dashed cyan** connects the surfaces to the identifier row, marking it as supporting infrastructure rather than flow.
- **Coral** marks only the reconnect path — an abnormal condition being handled.
- **Teal** marks all eight event icons and the surface icons.
- The **funnel-then-fan** shape asserts one reducer between many events and many surfaces.

## How to present it

**Ask what their agent streams.** Usually text. Then ask what a client can render from undifferentiated prose — a chat panel, and nothing else.

**Read the eight event names and ask what each enables.** Progress labels, tool cards, early artifacts. The typing is what makes each renderable as a distinct thing.

**Draw the delta/snapshot distinction carefully.** Incremental versus complete. Deltas are light and require ordered delivery; snapshots are heavy and self-correcting. Having both is what makes recovery cheap.

**Ask why one reducer rather than five subscribers.** Consistency — surfaces cannot disagree. And testability — a pure function from events to state can be tested by replaying recorded sequences.

**Tell the Wardley testing benefit.** 140 recorded sequences, four of them reconnect scenarios that would be nearly impossible to reproduce by hand, running in CI in milliseconds. This is usually the argument that convinces engineers.

**Ask what happens when the connection drops.** Three options: restart, replay from the beginning, resume after the last event. Then point at the two identifiers and show that the third needs both.

**Give them the 8% number.** Eight percent of Wardley's computations experience a reconnect — sleeping laptops, office wifi, VPN cycling. Before the rebuild all of them were session losses.

**Point out that artifact-ready precedes run-finished.** A deliverable that exists at 40% can be offered at 40%. Wardley removed 90 seconds of perceived wait without making anything faster.

**Ask about step names.** "Checking reliefs" for 40 seconds is normal; "reading trial balance" for 40 seconds is not. A named step turns a duration into a diagnosis.

**Close on the line.** *Streaming text tells you it is alive. Typed events tell you what it is doing.*

**Timing.** Twenty-five minutes. Thirty-five if you enumerate the event types the room's own interface would need, which usually finds three or four they do not emit.

---

## Lab and checkpoint

**Lab:** For one run in your system, list the events a client would need to render progress, tool calls, snapshots, artifacts, and completion. For each, define the event type, schema, and which UI surface it updates. Then write the reconnect rule using event and run IDs, and the reducer function that turns the event stream into UI state.

**Checkpoint:** Why are typed events better than streaming text for a UI?

**Answer:** Because undifferentiated text can only be rendered as a chat panel. Typed events can be rendered as progress bars, tool cards, state panels, and artifact cards. They also make the stream testable and make reconnect and resume possible from the last known event.

## Glossary

- **Artifact ready** — an event that signals a deliverable is available before the run finishes.
- **Delta** — an incremental event that requires ordered delivery.
- **Event ID** — the identifier for a single event.
- **React reducer** — a pure function that turns a stream of events into UI state.
- **Reconnect** — the path that resumes after the last event, not from the start.
- **Run ID** — the identifier for the whole run.
- **Snapshot** — a complete state event that is self-correcting and heavy.
- **Step started** — an event that begins a named step.
- **Text delta** — an incremental text update.
- **Tool call result** — an event that carries the result of a tool call.
- **Typed event** — an event with a known schema and type.

## Sources

- Typed event streams and reducers for agent UIs
- Reconnect and resume in streaming interfaces
- React reducer patterns and event sourcing
