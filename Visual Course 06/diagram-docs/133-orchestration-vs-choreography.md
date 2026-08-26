# Diagram 133 — Orchestration versus Choreography

![A split canvas on dark navy. Left, under ORCHESTRATION, a blue COORDINATOR figure sends cyan COMMANDS down to three blue services — POLICY, FINANCE, NOTIFY — and teal RESULTS arrows return to the coordinator. Right, under CHOREOGRAPHY, the same three services publish FACT EVENTS through a central EVENT BUS, and each service independently reacts with its own EVENT, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT and RESUME chain. A coral FAILURE path loops from each service back to its own resume. Below, a four-row comparison table: GLOBAL VIEW versus PARTIAL VIEW, LOW COUPLING versus LOOSE COUPLING, CENTRALIZED RECOVERY versus DISTRIBUTED RECOVERY, CENTRALIZED OWNERSHIP versus DISTRIBUTED OWNERSHIP, with green checks and red crosses.](../diagrams/133-orchestration-vs-choreography.png)

**Module:** Distributed workflow patterns
**Role in the course:** the first distributed-workflow choice — where does the decision live
**Layout:** a side-by-side comparison with a trade-off table across the bottom

---

## At a glance

Two halves. **ORCHESTRATION** on the left, **CHOREOGRAPHY** on the right.

Orchestration: one **COORDINATOR** sends **COMMANDS** to **POLICY, FINANCE, NOTIFY**, and receives **RESULTS**.

Choreography: the same three services publish **FACT EVENTS** through an **EVENT BUS**. Each reacts independently.

And below, the trade-off table. **GLOBAL VIEW, LOW COUPLING, CENTRALIZED RECOVERY, CENTRALIZED OWNERSHIP** for orchestration. **PARTIAL VIEW, LOOSE COUPLING, DISTRIBUTED RECOVERY, DISTRIBUTED OWNERSHIP** for choreography.

The diagram does not say one is better. It says the choice is about where the owner of the end-to-end decision lives.

---

## What the diagram teaches

### 1. Commands and events are different messages with different owners

In orchestration, the arrows are **COMMANDS**. A command says *do this*. It comes from the coordinator and goes to a participant. The participant can refuse.

In choreography, the arrows are **FACT EVENTS**. An event says *this happened*. It is published by a participant, and other participants decide whether to react.

That difference is the whole distinction. A command is a request with an owner who is waiting. An event is a fact with no owner who is responsible for the reaction.

The same three services — **POLICY, FINANCE, NOTIFY** — appear in both halves. The only thing that changes is the message type and the controller.

### 2. Orchestration gives a global view at the cost of coupling

The coordinator in the left half knows the full sequence. It knows which step is next, which results have arrived, and where the workflow is stuck.

That global view is what makes recovery possible. If the workflow is in a bad state, a human can open the coordinator and see the end-to-end status. The owner is named.

The cost is coupling. Every participant must understand the coordinator's command language. A change to the flow often means a change to the coordinator and possibly to every participant.

### 3. Choreography gives loose coupling at the cost of a partial view

In the right half, no participant knows the whole journey. **POLICY** publishes an event. **FINANCE** and **NOTIFY** each react, but neither knows whether the other has done so.

That loose coupling is powerful. A service can be added or removed without changing the others. The event contract is narrow.

But the partial view is real. If something goes wrong, there is no single place to look. The business journey is spread across many event handlers, and the only way to reconstruct it is to read the events.

### 4. The trade-off table is the diagram's argument

The bottom of the image is a four-row table.

**GLOBAL VIEW** — orchestration has it, choreography does not.
**LOW COUPLING / LOOSE COUPLING** — both reduce coupling, but choreography does it more.
**CENTRALIZED RECOVERY / DISTRIBUTED RECOVERY** — orchestration has one place to recover; choreography spreads the responsibility.
**CENTRALIZED OWNERSHIP / DISTRIBUTED OWNERSHIP** — the most important row.

Ownership is not the same as implementation. Choreography does not mean nobody owns the outcome. It means the ownership is distributed across every participant. That is fine, as long as each participant owns its own reaction and the contracts are clear. But if the end-to-end business decision requires agreement across all three, choreography makes that agreement implicit and hard to debug.

### 5. The durable chain on the choreography side is not decoration

Each choreography participant has its own **EVENT, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME** chain. The same durable vocabulary as the rest of the volume.

That matters because choreography is often mistaken for *fire and forget*. The diagram shows that every reaction is still a durable workflow. Each participant still acknowledges, records receipts, checkpoints, and resumes.

The difference is that the checkpoint and resume are local, not global. Each participant can recover itself, but no single participant can recover the whole.

### 6. Choreography works best for reactions to facts, not for ordered business decisions

The right half is a good fit when the business process is *a thing happened, and several other things can happen in response*. A refund was settled, so the case can close, a notification can be sent, and analytics can be updated.

The left half is a good fit when the order and recovery of the steps matters. A refund cannot be sent until the policy check passes. The policy check cannot be skipped. If the notification fails, the refund should still be considered done.

The diagram's conclusion is not to pick one. It is to know which one you are using and why.

### 7. Most real systems are a hybrid, and the question is where the boundary sits

The diagram is a clean split, but production systems usually mix both. A central workflow may orchestrate the ordered, compensable steps, then publish a domain event and let choreography handle the side effects.

The boundary is the point where a single owner is no longer needed. The diagram helps locate that point. If a step is in the orchestration half, the coordinator owns its ordering and recovery. If a step is in the choreography half, each participant owns its own reaction.

### 8. The durable record must outlast the coordinator and the message bus

The same durable vocabulary appears on the choreography side because a cross-service workflow is still a workflow even when no single runtime owns every step. Whether the pattern is orchestration or choreography, the record must say what was requested, which identity owns it, what changed, which attempt produced the change, and what may legally happen next.

In orchestration the coordinator keeps that record as explicit state. In choreography the record is distributed: the event bus keeps the fact, each participant keeps its own acknowledgement, receipt, checkpoint, and resume, and a correlation identity stitches the fragments back into one business journey. A retry, a lost worker, or a revised proposal must never change the business meaning.

This is why ownership is a contract, not a framework convenience. When tests replay the same fixture of commands, events, states, and error outcomes without network calls, the contract is visible and the pattern becomes incidental.

### 9. Commands and events are a server-side contract, not a client-side choreography

A common beginner mistake is to put the orchestration or choreography in the browser. A client component calls one service, waits, calls another, and subscribes to events through a WebSocket, behaving like a tiny coordinator. That shifts the owner of the end-to-end decision to a runtime that can disappear when the tab closes.

The diagram is about backend boundaries. Commands should leave the browser through protected server APIs that return a stable ID or receipt. Status events should reach the browser through adapters that translate durable workflow facts into a read-only view. The case timeline should stay coherent even when the backend mixes both patterns. Keep distributed coordination out of client components. The browser owns the user, not the business decision.

The next diagram shows what orchestration looks like when the coordinator fans work out to several workers and then joins the results.

![On dark navy, a PARENT WORKFLOW sends cyan arrows to four workers — POLICY, LEDGER, FRAUD, CUSTOMER HISTORY. Each worker returns RESULT and ACK arrows to a JOIN GATE, which lists REQUIRED ALL, QUORUM 3 OF 4, OPTIONAL NONE, DEADLINE 30s. The join gate emits a green check to AGGREGATED EVIDENCE. Coral dashed paths show STRAGGLER and DUPLICATE outcomes being rejected.](../diagrams/134-fan-out-fan-in-join.png)

This is still orchestration, but it shows that orchestration does not have to be one worker at a time. The parent can issue multiple commands in parallel, as long as the join gate defines the contract for when the parent may continue. The commands are still owned by a coordinator, and the join gate is the explicit owner of the continue-or-wait decision.

---

## Case study — Tresham Services, the notification that nobody owned

Tresham runs a field-service platform. When a job is completed, three things must happen: the case record is updated, the customer is notified, and the engineer's timesheet is updated.

### What they had

A choreography design. The field-service app published a `JobCompleted` event to a message bus. Three consumers updated the case, sent the notification, and updated the timesheet.

Each consumer owned its own reaction. There was no central coordinator. The event bus meant the consumers were loosely coupled.

### The failure

The notification consumer began failing silently. The email provider returned 5xx. The consumer retried, failed, retried, and eventually dropped the message into a dead-letter queue that nobody monitored.

The case and timesheet were updated correctly. The customer was never notified. The engineer marked the job as complete and moved on.

Two weeks later, the support team noticed a pattern: customers were calling to ask why they had not been told their job was done. Roughly 1,800 jobs over ten days.

### Why it was hard to find

There was no global view. The case record said `complete`. The timesheet said `complete`. The notification failure lived in a dead-letter queue on a different service. Reconstructing the missing notifications required reading three separate systems and joining them by job ID.

The business process — *notify the customer when a job is done* — had no owner. Each team owned its own consumer, and the handoff between them was implicit.

### The rebuild

They kept choreography for the case and timesheet updates, because both were local reactions to a stable fact.

They moved the notification into an orchestrated step. The coordinator now sent a `SendCustomerNotification` command and waited for a receipt before marking the job complete. If the notification failed, the job state moved to `NOTIFICATION_FAILED`, and a human could see the end-to-end status in one place.

The event bus still carried `JobCompleted`. But the notification, which had a clear business owner and a recovery requirement, became a command with a result.

### Results

- **Missing customer notifications due to unmonitored dead-letter queue:** 1,800 over ten days → 0.
- **Time to detect a failed notification:** two weeks → seconds, because the coordinator exposes the state.
- **Mean time to resolve a failed notification:** several hours of cross-system search → under five minutes, because the failure is visible on the case record.
- **Notification consumer ownership:** unowned → owned by the case workflow.

### The line in their engineering standard

*Choreography is fine for independent reactions. When the outcome requires ordered completion or human recovery, someone must own it as a command.*

---

## Composition

A split canvas with two halves and a comparison table across the bottom.

**Left half — ORCHESTRATION:** a large **COORDINATOR** figure on a blue platform at the top. Three **cyan arrows labelled COMMANDS** point down to three blue service platforms — **POLICY** (shield), **FINANCE** ($), **NOTIFY** (envelope). Three **teal arrows labelled RESULTS** point back up to the coordinator.

**Right half — CHOREOGRAPHY:** the same three service platforms arranged around a central blue **EVENT BUS** cylinder. Dashed teal arrows labelled **PUBLISH FACT EVENTS** leave each service and enter the bus, then fan out to the other services. Each service has a vertical chain of five teal badges: **EVENT, ACKNOWLEDGEMENT, RECEIPT, CHECKPOINT, RESUME**. A **coral dashed FAILURE** path loops from each service back to its resume.

**Bottom table:** four rows, two columns. Each row compares one quality: **GLOBAL VIEW / PARTIAL VIEW**, **LOW COUPLING / LOOSE COUPLING**, **CENTRALIZED RECOVERY / DISTRIBUTED RECOVERY**, **CENTRALIZED OWNERSHIP / DISTRIBUTED OWNERSHIP**. Green check marks show the strength; red crosses show the cost.

## Element by element

**COORDINATOR** — the owner of the end-to-end sequence.
**COMMANDS** — requests from the coordinator to participants.
**RESULTS** — responses back to the coordinator.

**POLICY / FINANCE / NOTIFY** — the same participants in both halves.

**EVENT BUS** — the shared channel in choreography.
**FACT EVENTS** — published facts, not requests.
**EVENT → ACKNOWLEDGEMENT → RECEIPT → CHECKPOINT → RESUME** — durable local workflow per participant.

**The four comparison rows** — global view, coupling, recovery, ownership.

## Colour and flow semantics

- **Cyan arrows** carry commands and parallel work in orchestration.
- **Teal arrows** carry results in orchestration and local durable steps in choreography.
- **Teal dashed** carries published events — reference, not direct flow.
- **Coral dashed** carries the local failure-and-resume path in choreography.
- **Green checks and red crosses** in the table mark the strengths and costs directly, so the trade-off does not depend on colour alone.
- The **identical participants in both halves** make the comparison fair: only the message type and control structure change.

## How to present it

**Ask which one the room uses.** Most will say choreography because it feels modern. Then ask them to trace a failure. Who owns the recovery? Usually nobody.

**Read the left half first.** Coordinator, commands, results. This is the pattern where one runtime owns the end-to-end business decision.

**Read the right half second.** Services publish facts, others react. This is the pattern where each service owns its own reaction.

**Point at the bottom table.** Four rows, two columns. Ask which row matters most for the workflow they are about to design. Usually it is ownership or recovery.

**Make the commands-versus-events distinction concrete.** A command says *do this* and has a caller waiting. An event says *this happened* and the subscriber decides what to do. Ask whether their message bus is full of commands or events.

**Emphasize that choreography is not fire-and-forget.** Each participant still has event, acknowledgement, receipt, checkpoint, resume. The chain is local, not global.

**Tell the Tresham story.** A `JobCompleted` event, three consumers, the notification failed silently, and nobody owned the missing notifications. 1,800 customers over ten days. The fix: keep choreography for local updates, orchestrate the notification with a receipt.

**Point at the next diagram.** Orchestration can be parallel. The parent workflow fans out commands and joins the results through a gate. The coordinator is still the owner.

**Close on the standard.** *Choreography is fine for independent reactions. When the outcome requires ordered completion or human recovery, someone must own it as a command.*

**Run the Acme lab.** Ask the room to classify six steps as command or event reaction and to say who owns failure and completion for each.

**Use the Maya refund scenario.** A refund should close the case, notify Maya, update analytics, and invite a survey. Which steps need a coordinator and which can react to REFUND SETTLED?

**Ask the checkpoint.** Does choreography mean there is no business owner? The answer is no: it removes a central controller, not the need for ownership, contracts, observability, and recovery.

**Name the sources.** The Azure Saga pattern is a useful name for orchestrated long-running transactions; the CloudEvents primer describes the shape of a durable domain event.

**Timing.** Twenty minutes. Thirty if the room maps one real cross-service process and decides which steps are commands and which are events.

---

## Lab and checkpoint

**Lab:** Map one cross-service process in your system. For each step, decide whether it is a command with a coordinator and a waiting caller, or an event reaction where a subscriber decides. Identify who owns failure and recovery in each case. Then design the durable record for choreography steps so recovery is possible without a central coordinator.

**Checkpoint:** Why does choreography not remove the need for a business owner?

**Answer:** Because choreography removes a central controller, but it does not remove ownership. Each service still needs contracts, observability, event receipts, checkpoints, and recovery. If nobody owns the overall outcome, failures like the missing notification will be silently lost.

## Glossary

- **Choreography** — a pattern where services publish events and other services react independently.
- **Command** — a message that says *do this* and has a caller waiting for the result.
- **Coordinator** — the component that owns an orchestrated workflow.
- **Durable record** — the history that outlasts the coordinator and message bus.
- **Event** — a message that says *this happened*, and subscribers decide what to do.
- **Orchestration** — a pattern where one coordinator sends commands and owns the outcome.
- **Recovery** — the process of continuing or fixing a failed workflow.
- **Saga** — a long-running transaction pattern with local compensations.

## Sources

- Orchestration and choreography in distributed systems
- Commands versus events and saga patterns
- CloudEvents and durable domain events
