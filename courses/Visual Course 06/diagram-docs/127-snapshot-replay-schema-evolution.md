# Diagram 127 — Snapshot, Replay, and Schema Evolution

![On dark navy, APPEND-ONLY EVENTS 1 TO 900 shows numbered cards leading to SNAPSHOT AT 800 with a camera, then REPLAY 801 TO 900 with a play button, then CURRENT STATE with a database. Above, CODE V1 and CODE V2 tiles feed a VERSION GATE archway which sends a cyan arrow down into replay and a coral arrow right to INCOMPATIBLE EVENT and MIGRATION TEST. From current state, six teal arrows fan to CLEAN HISTORY, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT and RESUME.](../diagrams/127-snapshot-replay-schema-evolution.png)

**Module:** Durable-system foundation
**Role in the course:** rebuilding state affordably, across code versions
**Layout:** a snapshot-plus-replay chain with a version gate above and outputs fanning right

---

## At a glance

Nine hundred events. A **snapshot at 800**. Replay of **801 to 900**. Current state.

Above it, **CODE V1** and **CODE V2** both feeding a **VERSION GATE** — because the events being replayed were written by one version of the code and are being read by another.

And a coral branch: **INCOMPATIBLE EVENT → MIGRATION TEST.**

Snapshots make replay affordable. The version gate makes it survivable when the code has changed underneath the history.

---

## What the diagram teaches

### 1. Snapshot plus replay is the answer to replay cost

Rebuilding state from event 1 works and does not scale. At 900 events it is fine. At 900,000 it is not.

A **snapshot** is state as of a known event number. Replay starts from there.

The numbers are specific and worth reading: snapshot at 800, replay 801 to 900. **One hundred events replayed instead of nine hundred.**

That ratio is the design lever. Snapshot frequency determines replay cost, and it is a straightforward trade — more snapshots mean cheaper replay and more storage.

### 2. The snapshot carries a green check, and the check is a claim

A **green tick** floats above the snapshot, connected by a dashed line.

A snapshot is a derived artefact, and a wrong snapshot is worse than no snapshot — it produces a confidently incorrect state from which replay proceeds.

The check says this snapshot has been verified: rebuilt from history and compared, or checksummed against a known-good rebuild.

Systems that snapshot without verifying accumulate the risk that one bad snapshot silently corrupts everything after it.

### 3. Both code versions feed the version gate, and that is the real problem

**CODE V1** and **CODE V2**, side by side, both arrowing into the **VERSION GATE**.

Events written months ago were serialised by code that no longer exists. The code reading them today is different.

That is not an edge case; it is the normal condition of any long-lived event-sourced system. History outlives code.

The gate is drawn as an **archway** — something every event passes through — rather than as a check applied occasionally.

### 4. INCOMPATIBLE EVENT is coral and leads to a migration test, not to a failure

The coral path from the gate leads to **INCOMPATIBLE EVENT** — a red exclamation — and then to **MIGRATION TEST**, a laboratory flask on a red platform.

The flask is the right glyph. An incompatible event is not an error to be logged; it is a **case to be tested**.

The workflow it implies: the gate detects an event shape the current code cannot interpret, and that becomes a test case for a migration — code that upgrades the old shape to the new one on read.

Migrations are then themselves tested against real historical events, which is what the flask represents.

### 5. The gate's output goes into replay, which is where migration must happen

Follow the cyan arrow from the gate: it descends into **REPLAY**.

Migration happens **on read**, during replay, not by rewriting history.

That is the important constraint. Rewriting historical events to a new shape destroys the append-only property and makes the history no longer a record of what was written.

Upgrading on read means the stored event is untouched and the code that interprets it handles both shapes.

### 6. CLEAN HISTORY appears on the output side, and its position is informative

Of the six outputs fanning from current state, the first is **CLEAN HISTORY** — a blue platform with a plus badge.

It is on the output side because a clean history is something the system *produces*, not something it starts with.

Practically: once every event has been migrated to a current shape and verified, an old snapshot can be taken as a new baseline and the events before it archived. That is history compaction, and it is only safe once the version gate has confirmed everything is interpretable.

### 7. Five of the six outputs are the durable-workflow vocabulary

**ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME** — with a paper-plane glyph beginning the list.

The same vocabulary as the state-layer diagram, appearing again as things a rebuilt state can produce.

That repetition says a rebuilt state is a fully functional state. It is not a degraded or read-only reconstruction; it can acknowledge, receipt, checkpoint and resume exactly as a continuously-maintained state could.

Which is only possible because every event in the history was validated before it was appended:

![On dark navy, a USER COMMAND person figure leads to VALIDATE INVARIANTS, a teal shield with a check. A teal VALID arrow leads through EVENT and APPEND-ONLY HISTORY to a REDUCER gear, then into a dashed STATE panel showing OPEN with an open door above WAITING APPROVAL. A coral INVALID arrow leads to COMMAND REJECTED, a red octagon, whose dashed line to the state is cut by a red X labelled STATE UNCHANGED.](../diagrams/126-command-event-state-machine.png)

The replay in this diagram assumes the history contains only valid events. If an invalid event could be appended, rebuilding state from history would reproduce invalid states, and the snapshot would become a confidently wrong baseline. The version gate in this diagram protects against *code* drift; the invariant shield in the previous diagram protects against *logic* drift. Both guards must hold for a rebuilt state to be trustworthy.

---

## Case study — Fennimore Trading, the replay that took eleven hours

Fennimore operates a trade lifecycle platform for commodity brokers. Every trade is an event-sourced aggregate: submitted, confirmed, amended, allocated, settled.

A large trade accumulates between 40 and several thousand events over its life.

### What they had

Event sourcing with no snapshots. State rebuilt from event 1 on every load.

For a new trade with 12 events, this took milliseconds. For a heavily-amended trade with 3,000 events, it took about 4 seconds.

That was tolerable until it was not.

### The incident

A deployment introduced a bug in their projection code. Their state projections — the read models their trading screens use — were being written incorrectly for about six hours before anyone noticed.

The fix was obvious: rebuild the projections from history.

**The rebuild took eleven hours.**

Fennimore's platform was effectively read-only for a full trading day. Traders could see trades and could not act on them, because the screens were rebuilding.

Their operations director's question afterwards was not about the bug. It was: *why does it take eleven hours to rebuild something we can recompute?*

### What the eleven hours consisted of

About 14 million events across roughly 90,000 open trades.

Every trade rebuilt from event 1. The long tail dominated: 3% of trades held 60% of the events.

### The rebuild

**Snapshots every 200 events, verified.**

Their verification is a rebuild-and-compare on a sample: 1% of snapshots are verified by rebuilding from event 1 and comparing, nightly.

That sample has caught two bad snapshots in eighteen months, both from a projection bug that produced a correct-looking but wrong intermediate state.

**Full rebuild time: eleven hours → 22 minutes.**

**A version gate, which they had not had.**

Building snapshots forced them to confront a problem they had been living with unknowingly.

Their event schemas had changed eleven times over four years. Their deserialisation code handled the changes by a chain of `if` statements checking for the presence of fields.

It worked. Nobody could say whether it worked for every historical shape, because nothing had tested it against real old events.

**The version gate made event shapes explicit.** Every event carries a schema version. The gate routes each to the appropriate upgrade path.

**Running the gate over their full history found 4 event shapes their code could not interpret.**

All four were from a period in year two where a bug had written events with a malformed field. Their deserialisation had been silently defaulting the field, which meant roughly 8,000 events had been replaying with a wrong value for two years.

The effect was small — the field affected a display label rather than a calculation — and it had been invisible.

**Migration tests.**

Each of the four incompatible shapes became a test case. The migration code upgrading them is tested against real historical events pulled from production.

That test suite has since caught two migration bugs before deployment.

**Migration on read, never on write.**

They considered rewriting the 8,000 malformed events. Their audit function refused: the events record what was written, and rewriting them destroys that record.

The malformed events remain malformed in storage. The read path upgrades them, and the upgrade is documented.

### The compaction they enabled

Once every event shape was interpretable and every migration tested, they could compact.

Trades settled more than two years ago have their pre-settlement events archived to cold storage, with a verified snapshot as the new baseline.

Their hot event store shrank by about 70%, which took a further six minutes off full rebuild time and reduced storage cost materially.

That compaction was only safe because the version gate had confirmed nothing in the archived range was uninterpretable.

### Results

- **Full projection rebuild:** 11 hours → 22 minutes → 16 minutes after compaction.
- **Uninterpretable event shapes found:** 4, affecting ~8,000 events over two years, previously silently defaulted.
- **Bad snapshots caught by sampled verification:** 2 in eighteen months.
- **Migration bugs caught by tests against real history:** 2.
- **Hot event store size:** down ~70% after compaction.

### The line in their platform standard

*Migrate on read. The stored event is what we wrote, and we do not get to change our minds about that later.*

---

## Composition

A horizontal chain across the lower portion, with a version gate above and outputs fanning right.

**Lower left:** **APPEND-ONLY EVENTS 1 TO 900** — a blue platform holding a row of white numbered cards reading **1, 2, 3, …, 900**, with a teal document badge at the left.

Cyan arrow → **SNAPSHOT AT 800** — a white card with a blue camera, with a **green tick** above connected by a dashed teal line.

Cyan arrow → **REPLAY 801 TO 900** — a white card with a blue play button, with a **teal play badge** above.

Cyan arrow → **CURRENT STATE** — a white card with a blue database, with a **teal database badge** above.

**Upper centre:** **CODE V1** and **CODE V2** — two blue platforms with `</>` tiles — each sending a cyan arrow into **VERSION GATE**, a blue archway on a hexagonal platform.

From the gate: a **cyan arrow down** into replay; a **coral line right** to **INCOMPATIBLE EVENT** — a red exclamation disc — then a coral arrow to **MIGRATION TEST**, a white flask on a **red platform**.

**Right:** six **teal arrows** fan from current state to teal circular badges with labels — a paper plane, then **CLEAN HISTORY** (a blue platform with a plus), **ACKNOWLEDGEMENT** (check), **RECEIPT** (envelope), **CHECKPOINT** (flag), **RESUME** (refresh).

## Element by element

**APPEND-ONLY EVENTS 1 TO 900** — the full history.
**SNAPSHOT AT 800** — state at a known point, with a verification tick.
**REPLAY 801 TO 900** — 100 events instead of 900.
**CURRENT STATE** — the rebuilt result.

**CODE V1 / CODE V2** — two versions reading one history.
**VERSION GATE** — an archway every event passes.
**INCOMPATIBLE EVENT / MIGRATION TEST** — a case to be tested, drawn as a flask.

**The six outputs** — clean history plus the durable-workflow vocabulary.

## Colour and flow semantics

- **Cyan arrows** carry the snapshot-and-replay chain and the version gate's output into replay.
- **Teal** marks the verification badges above each stage and all six outputs.
- **Coral** marks the incompatible-event path and the migration test's platform.
- The **archway form** of the version gate conveys that every event passes through it.
- The **flask** on a red platform frames incompatibility as a test case rather than an error.

## How to present it

**Ask how long it takes to rebuild their read models from history.** Most rooms have never tried. Then tell the Fennimore eleven hours and the read-only trading day.

**Read the numbers.** Snapshot at 800, replay 801 to 900. One hundred instead of nine hundred, and that ratio is the design lever.

**Point at the green tick above the snapshot.** A wrong snapshot is worse than none — it produces a confidently incorrect state that replay builds on. Ask how they would verify one. Fennimore rebuild 1% from event 1 nightly and compare.

**Point at the two code versions.** History outlives code. Ask what deserialises their four-year-old events, and whether anything has tested it against real old events.

**Tell the four incompatible shapes.** A bug in year two wrote malformed events; deserialisation silently defaulted the field; 8,000 events replayed with a wrong value for two years, invisibly.

**Point at the flask.** An incompatible event is a test case, not a log line. Then note that migrations get tested against real historical events pulled from production.

**Make the migrate-on-read point firmly.** Fennimore considered rewriting the malformed events; their audit function refused. The stored event is what was written.

**Point at CLEAN HISTORY on the output side.** Compaction is something you earn once every shape is interpretable. Fennimore's hot store fell 70%, and it was only safe because the gate had confirmed the archived range.

**Note that a rebuilt state is fully functional.** Five of the six outputs are the durable-workflow vocabulary. A rebuild is not a degraded reconstruction.

**Close on the standard.** *Migrate on read. The stored event is what we wrote.*

**Timing.** Twenty-five minutes. Thirty-five if you estimate the room's own rebuild time, which is usually longer than they expect.

---

## Lab and checkpoint

**Lab:** For one of your event-sourced models, estimate the time to rebuild from event one. Design a snapshot and replay strategy with a version gate that handles incompatible old events. Write a migration test using real historical events, and define how you verify the snapshot by rebuilding 1% from the start and comparing.

**Checkpoint:** Why is a wrong snapshot worse than no snapshot?

**Answer:** Because a wrong snapshot becomes the base state on which replay builds, producing a confidently incorrect result. No snapshot forces a full replay, which is slow but safe. A wrong snapshot creates an error that looks right.

## Glossary

- **Clean history** — the result of compaction after all events are interpretable.
- **Compaction** — the process of reducing storage by removing or summarising old events.
- **Incompatible event** — an old event whose shape the current code cannot read directly.
- **Migrate on read** — the rule that old events are migrated when they are read, not rewritten.
- **Migration test** — a test that replays real historical events through the version gate.
- **Read model** — the derived state used by queries.
- **Replay** — re-deriving state by processing events from the beginning.
- **Schema evolution** — the way event schemas change over time.
- **Snapshot** — a point-in-time copy of state used to reduce replay cost.
- **Version gate** — the component that decides how to handle events of different schema versions.

## Sources

- Event sourcing, snapshots, and replay
- Schema evolution and migration-on-read
- Durable workflow state and compaction
