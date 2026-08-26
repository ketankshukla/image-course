# Diagram 145 — Races, Duplicates, Out-of-Order Events, and Stale State

![On dark navy, four hazards sit on the left: RACE between two commands, DUPLICATE EVENT, OUT OF ORDER event 12 before 11, and STALE WRITE version 7 against current 9. Each hazard sends a white command/event card into a row of four blue CORRECTNESS GUARDS: EXPECTED VERSION, UNIQUE KEY, SEQUENCE, and MONOTONIC STATE. Each guard has a red X at the bottom to show a failed gate and a green check for a passed gate. Past the guards, teal and red arrows point to the STATE STORE on the right, which shows CURRENT VERSION: 9 and LATEST SEQUENCE: 11. To the far right, OUTCOMES list ACCEPTED STORE / APPLY with a green check and REJECTED GUARD FAILED with a red X. Below, a legend shows cyan for command/event flow, teal dashed for durable paths, green check for acknowledgement/receipt, red X for rejection, and teal dot for checkpoint/resume.](../diagrams/145-race-duplicate-order-stale-state.png)

**Module:** Testing, correctness, and observability
**Role in the course:** the four concurrency hazards and the guards that stop them
**Layout:** four hazard rows on the left, four guards in the centre, state store on the right, outcomes on the far right

---

## At a glance

Four hazards: **RACE, DUPLICATE EVENT, OUT OF ORDER, STALE WRITE**.

Four guards: **EXPECTED VERSION, UNIQUE KEY, SEQUENCE, MONOTONIC STATE**.

Commands and events pass through the guards before they reach the **STATE STORE**.

The state store keeps **CURRENT VERSION** and **LATEST SEQUENCE**.

And two outcomes: **ACCEPTED STORE / APPLY** or **REJECTED GUARD FAILED**.

No single lock or queue prevents all four hazards. You need the right guard for each one.

---

## What the diagram teaches

### 1. The four hazards are different

**RACE** — two commands try to change the same state at the same time.
**DUPLICATE EVENT** — the same event or command arrives twice.
**OUT OF ORDER** — a later sequence arrives before an earlier one.
**STALE WRITE** — a command is based on an old version of the state.

Each hazard is a different failure mode. A queue prevents some ordering issues but not stale writes. A lock prevents races on one server but not across services. You need to match the guard to the hazard.

### 2. Expected version catches stale writes and races

The **EXPECTED VERSION** guard checks the version the command thinks is current. If the state has moved on, the command is rejected.

This is compare-and-set. The command says "I expect version 8." If the store is at version 9, the command fails. The actor can refresh and retry from the current version.

Expected version is the right guard for races and stale writes. Both happen when a command is based on an old version.

### 3. Unique key catches duplicates

The **UNIQUE KEY** guard checks that the effect of this command or event has not already been seen. If the key is already present, the input is a duplicate.

The key is not the message ID. It is the identity of the effect. For a refund, the effect key might be *refund for case X on date Y by actor Z*. The same request resubmitted with a different message ID is still the same effect.

This is idempotency. Duplicate detection is the right guard for duplicates.

### 4. Sequence catches out-of-order delivery

The **SEQUENCE** guard checks that the incoming sequence number is the next expected one. If event 12 arrives before event 11, it is held or rejected.

This is the right guard for out-of-order delivery. It is not the same as the expected version. Version is about state. Sequence is about the order of facts.

A system can accept events out of order if it can buffer them and apply them in the correct order. But the guard must enforce that order before the state changes.

### 5. Monotonic state catches illegal transitions

The **MONOTONIC STATE** guard checks that the requested state change is legal from the current state. A completed refund cannot be approved again. A rejected case cannot be rejected again.

This is the business-rule guard. It does not care about version or sequence. It cares about whether the state machine allows the transition.

Terminal states should be monotonic unless there is an explicit reopen event. A reopen event is a deliberate business action, not an accidental re-delivery.

### 6. All four guards can be needed for one command

A single command may be checked against expected version, unique key, sequence, and monotonic state. Each guard answers a different question.

- Is this command based on current state? (expected version)
- Have we already done this? (unique key)
- Is this the next fact in the sequence? (sequence)
- Is this transition legal? (monotonic state)

A command that passes all four can be stored and applied. A command that fails any one is rejected with an observable outcome.

### 7. Rejected inputs are observable outcomes, not silent drops

The far right shows two outcomes: **ACCEPTED STORE / APPLY** and **REJECTED GUARD FAILED**.

A rejection is not a crash. It is a durable outcome. The system must record why the input was rejected: which guard failed, what the expected and actual values were, and what the actor should do next.

Observable rejections make the system debuggable. Silent drops make concurrency bugs invisible.

A related view shows how idempotency keys, deduplication stores, and retry budgets protect work from exactly these failures:

![On dark navy, a CLIENT sends a cyan command through a red RETRY BUDGET box and a red RETRY COUNTER. The command carries a yellow IDEMPOTENCY KEY tag. It enters a DEDUPLICATION STORE with an IN-PROGRESS and COMPLETED ledger. A green check path leads to PROCESS. A red path leads to a POISON / DEAD LETTER QUEUE. A red circular arrow around the client side is labelled INFINITE LOOP PREVENTION.](../diagrams/131-retry-idempotency-poison-work.png)

In that diagram, the DEDUPLICATION STORE is the UNIQUE KEY guard. The IDEMPOTENCY KEY is the effect key that lets the system say *this exact work has already happened*. The RETRY BUDGET and INFINITE LOOP PREVENTION are additional guards for the same out-of-order, duplicate, and stale inputs. The POISON / DEAD LETTER QUEUE is the observable rejection path.

### 8. The state store exposes current version and latest sequence

The **STATE STORE** shows **CURRENT VERSION: 9** and **LATEST SEQUENCE: 11**.

These are not internal implementation details. They are part of the contract. Commands include expected version. Events include sequence. The store publishes both so that actors can decide whether to proceed or refresh.

### 9. The compare-and-commit gate is an explicit contract

The guard row is not a decorative frame. It is the compare-and-commit boundary between outside intent and authoritative state. Before the state store changes, a command must answer four questions: does it know the current version, is its effect new, is it the next fact in order, and is the transition legal? That makes the guard row a published contract, not a hidden implementation detail.

This contract should travel with the command and the event. The command carries an expected version and a stable effect key. The event carries a sequence number and a causal identity. The store publishes current version and latest sequence so every actor can decide whether to proceed or refresh. When the contract is explicit, a transport retry, a worker crash, or an agent revising its proposal does not silently overwrite business truth. It produces a visible rejection that the durable record can explain: what was requested, which identity owned it, what changed, which attempt produced it, and what may legally happen next.

### 10. The guards shape what the user sees and how you test

Every guard has a user-visible response and a testable contract. Expected-version failure should tell the user the state has moved on and offer a refresh, not a blind retry. Unique-key failure should return the previous receipt, not a new attempt. Sequence failure should hold or reject the event and surface the gap. Monotonic-state failure should explain that the transition is not allowed and whether an explicit reopen is possible.

This is why the lab asks for a table with hazard, detection key, atomic guard, user response, metric, and recovery. In a Next.js system, send the version shown in the UI with every state-changing request and disable optimistic updates for irreversible actions until the server receipt returns. In Python, use unique constraints and conditional updates inside transactions, implement inbox deduplication and sequence handling per external source, and property-test transition functions with permutations and duplicate events.

---

## Case study — Thistledown Logistics, the double approval

Thistledown uses a workflow to approve package damage claims. Two supervisors can review the same claim from different offices.

### What they had

The system stored the claim status in a database. When a supervisor clicked approve or reject, the system updated the status directly.

There was no expected version. There was no unique effect key. The last click won.

### The incident

A claim was reviewed by two supervisors at nearly the same time. Supervisor A approved it. Supervisor B rejected it.

Both requests arrived at the server within a few milliseconds. The web server processed them on different threads. Both read the status as "pending." Supervisor B's update happened slightly later, so the claim was marked rejected.

The customer received a rejection. Supervisor A's approval was overwritten. When the customer complained, the audit log showed only one status change: to rejected. There was no record of the race or the lost approval.

### The guarded design

Every state-changing command now carries an expected workflow version and an effect key.

- Supervisor A sends *approve* with expected version 8 and effect key *approval-by-A-for-claim-12345*.
- Supervisor B sends *reject* with expected version 8 and effect key *rejection-by-B-for-claim-12345*.

The workflow processes A's command first. It checks expected version 8 against current version 8. It passes. It checks the effect key: not seen before. It passes. It checks sequence: next. It passes. It checks monotonic state: pending → approved is legal. It passes.

The command is stored. The workflow version becomes 9.

B's command arrives. It checks expected version 8 against current version 9. It fails. The command is rejected with a *stale write* outcome. Supervisor B is shown the current approved state and must explicitly reopen the claim if they want to change the decision.

### Results

- **Overwritten approvals or rejections due to races:** any number → 0.
- **Silent last-write-wins conflicts:** any number → 0, because every rejected command is an observable outcome.
- **Duplicate approval requests processed twice:** 3 in one month → 0, because the unique key catches the same effect.
- **Audit time to explain a state:** hours of log search → minutes, because the state store shows version and the rejection is recorded.

### The line in their claims standard

*Every state-changing command carries an expected version and an effect key. A transition commits only when version, uniqueness, sequence, and state all agree. Rejections are recorded and visible.*

---

## Composition

Four rows, each representing one hazard, with four guard columns and a shared state store.

**Left column — HAZARDS:** four red boxes stacked vertically:
- **RACE between two commands** — two running figures.
- **DUPLICATE EVENT** — two documents.
- **OUT OF ORDER event 12 before 11** — a calendar with 12 and 11.
- **STALE WRITE version 7 against current 9** — a database with a clock.

**Second column — COMMAND / EVENT:** four white cards:
- **COMMAND A / COMMAND B**
- **EVENT X, KEY: order-42**
- **EVENT, SEQUENCE: 12**
- **WRITE, VERSION: 7**

**Centre — CORRECTNESS GUARDS:** four blue shields in a row, repeated for each hazard:
- **EXPECTED VERSION** — V icon.
- **UNIQUE KEY** — key icon.
- **SEQUENCE** — 1, 2, 3 icon.
- **MONOTONIC STATE** — upward arrow.

Each guard shows a green check on success and a red X on failure.

**Right — STATE STORE:** a blue database with:
- **CURRENT VERSION: 9**
- **LATEST SEQUENCE: 11**

**Far right — OUTCOMES:** two cards:
- **ACCEPTED STORE / APPLY** — green check.
- **REJECTED GUARD FAILED** — red X.

**Bottom:** a legend with arrows: cyan for command/event flow, teal dashed for durable paths, green for acknowledgement, red for rejection, and teal dot for checkpoint/resume.

## Element by element

**HAZARDS** — the four concurrency failure modes.
**COMMAND / EVENT** — the input being guarded.

**EXPECTED VERSION** — compare-and-set guard.
**UNIQUE KEY** — idempotency guard.
**SEQUENCE** — ordering guard.
**MONOTONIC STATE** — business-transition guard.

**STATE STORE** — the authoritative record.
**CURRENT VERSION / LATEST SEQUENCE** — the published state identifiers.

**ACCEPTED / REJECTED** — the observable outcomes.

## Colour and flow semantics

- **Cyan arrows** carry commands and events forward into the guards.
- **Teal arrows** carry accepted inputs to the state store.
- **Red arrows** carry rejected inputs to the observable failure outcome.
- **Green checks** show guards that passed.
- **Red Xs** show guards that failed.
- The four hazard rows use the same guard columns, showing that the same guards apply to different inputs.
- The state store is drawn as a solid blue database because it is the single authoritative destination.

## How to present it

**Start with the question of what can go wrong when many actors change the same state.** Most rooms will list races and duplicates. Few will list out-of-order and stale writes until prompted.

**Point at the four hazards and ask which ones they handle.** Races are common. Duplicates are common. Out-of-order and stale writes are often ignored.

**Walk through the four guards.** Expected version for stale writes and races. Unique key for duplicates. Sequence for ordering. Monotonic state for illegal business transitions.

**Show that one command may need all four guards.** A refund command can be stale, duplicate, out of order, and illegal. The state store must check all four before accepting.

**Point at the outcomes.** Accepted or rejected. Rejections are observable, not silent. Ask how their system records a rejected command.

**Show the state store identifiers.** Current version and latest sequence are part of the API. Commands and events should include them.

**Tell the Thistledown story.** Two supervisors approved and rejected the same claim. Last write won. The approval was lost. The fix: expected version, unique effect key, monotonic state, observable rejections.

**Ask the checkpoint question.** "Does a FIFO queue prevent all stale writes?" Answer: no. Ordering may apply only within a queue or group; other actors and stores still need version and state checks.

**Close on the standard.** *Every state-changing command carries an expected version and an effect key. A transition commits only when version, uniqueness, sequence, and state all agree. Rejections are recorded and visible.*

**Ask the room to map one real command to the guard table.** A refund, an approval, or a shipment works well. For each of the four hazards, ask what detection key, atomic guard, user response, metric, and recovery look like.

**Connect to the implementation frame.** In Next.js, the version shown in the UI must travel with the request, and conflicts must refresh the view rather than silently retry. In Python, conditional updates, unique constraints, and per-source sequence inboxes make the guards durable and replayable.

**Cite the sources and set the release gate.** Google Pub/Sub exactly-once delivery, Amazon SQS visibility timeout, and RFC 9110 HTTP semantics reduce delivery and HTTP risk, but they do not replace explicit compare-and-set and idempotency at the application boundary.

**Timing.** Twenty-five minutes. Thirty if the room draws a state change and lists which guards it would pass or fail.

---

## Lab and checkpoint

**Lab:** Take one state-changing command in your system (refund, approval, shipment). Draw the guard table for the four hazards: race, duplicate, out-of-order, and illegal transition. For each, write the detection key, the atomic guard, the user response, the metric, and the recovery. Ensure the state store exposes current version and latest sequence.

**Checkpoint:** Why is a FIFO queue not enough to prevent stale writes?

**Answer:** Because a FIFO queue may only order messages within one queue or group. Other actors, caches, and stores may still see or write stale data. Expected version, unique keys, and monotonic state checks are still needed at the state store.

## Glossary

- **Compare-and-commit** — the atomic gate that applies a command only if all guards pass.
- **Duplicate** — the same command arriving twice.
- **Effect key** — a unique key that prevents duplicate effects.
- **Expected version** — the state version the command was based on.
- **Guard** — a check that prevents a class of concurrency hazard.
- **Illegal transition** — a state change that violates business rules.
- **Monotonic state** — the rule that state only moves through allowed transitions.
- **Out-of-order** — commands arriving in a different order than they were issued.
- **Race** — two commands trying to update the same state at the same time.
- **Rejected input** — a command that fails a guard and is recorded visibly.
- **Sequence** — the ordering key that detects out-of-order messages.
- **State store** — the durable store that enforces the guards.

## Sources

- Concurrency guards and compare-and-commit
- Idempotency and expected-version state changes
- Message ordering and duplicate suppression
