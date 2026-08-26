# Diagram 129 — Queues, Workers, Leases, Acknowledgements, and Visibility

![On dark navy, a PRODUCER factory icon on a blue platform sends a cyan arrow to DURABLE QUEUE, a blue barrel with an envelope. A dashed cyan arrow from the queue to a WORKER A server reads 'Delivery creates LEASE / VISIBILITY WINDOW'. A cyan arrow from WORKER A runs through four white cards — PROCESS, RECEIPT, ACK and COMPLETE — with a teal baseline and upward arrows feeding each from below. A coral dashed arrow drops from WORKER A to a red WORKER CRASH server, then a red LEASE EXPIRE hourglass, then a teal SAME ITEM envelope, and finally a cyan arrow into WORKER B.](../diagrams/129-queue-lease-ack-visibility.png)

**Module:** Queues, workers, and backpressure
**Role in the course:** the first queue pattern — why a delivery is a lease, not ownership
**Layout:** a left-to-right flow with an upper success path and a lower crash/redelivery loop

---

## At a glance

**PRODUCER → DURABLE QUEUE → WORKER A**. Then **PROCESS → RECEIPT → ACK → COMPLETE**.

The arrow from the queue to the worker is **dashed**: the delivery creates a **LEASE / VISIBILITY WINDOW**.

And below, the failure story: **WORKER CRASH → LEASE EXPIRE → SAME ITEM → WORKER B**.

The sequence **PROCESS, RECEIPT, ACK, COMPLETE** is the success path. The **ACK** is not the end; it is the step that says *the end has already been made durable*.

---

## What the diagram teaches

### 1. Four stages, and the order is the contract

**PROCESS → RECEIPT → ACK → COMPLETE.**

Four white cards, left to right. Four separate steps. **PROCESS** — do the work. **RECEIPT** — record the result. **ACK** — tell the queue the work is finished. **COMPLETE** — the final durable state.

The most common beginner error is to put **ACK** before **RECEIPT**. The diagram places ACK third, and that position is the lesson: you do not tell the queue you are done until the thing you were doing has been recorded somewhere the queue does not control.

A queue that receives an ACK has one question: may I delete this item? The answer is yes only after the result would survive if the worker vanished immediately afterwards.

### 2. The queue is durable, the worker is not, and the lease is what bridges them

The **DURABLE QUEUE** is drawn as a solid barrel. The **WORKER A** is a server. The barrel persists; the server does not.

That asymmetry is why the queue cannot simply hand the item over and forget about it. It needs a **lease** — a contract that says: *this item is on loan to a worker for a bounded time. If the time expires, the loan is cancelled and the item is available again.*

The lease is the queue's assumption of risk. It knows workers crash. Rather than requiring perfect workers, it limits the damage a crashed worker can do by exposing the item again after the window.

### 3. A lease is a visibility window, and the dashed arrow is what it looks like

The dashed cyan arrow from the queue to **WORKER A** is labelled **LEASE / VISIBILITY WINDOW**. In most queue implementations the same idea has two names: a lease in some systems, a visibility timeout in others.

The dashes matter. A solid arrow would mean ownership transferred. A dashed arrow means temporary custody. The queue still owns the item; the worker only has the right to work on it until the window closes.

During that window the item is **invisible** to other workers. That is the visibility part. It prevents two workers from acting on the same item at the same time. But it does not prevent the same item being acted on twice in sequence, and that is what the lower path is about.

### 4. RECEIPT before ACK means proof before permission

Look at the arrow from **WORKER A** into the four cards. It enters **PROCESS** first, then **RECEIPT**, and only then does it reach **ACK**.

The **RECEIPT** is the durable record that the side effect happened. It might be a provider's acknowledgement of a payment, a file that was written, a confirmation code from an external service. Whatever it is, it is something the worker can produce if another worker later asks *has this already been done?*

If the worker crashes after **RECEIPT** but before **ACK**, the queue will redeliver, and the next worker can check the receipt and finish. If it crashes before **RECEIPT**, the work is genuinely incomplete, and a retry is the right thing.

This is the durable-workflow vocabulary from the previous volume: the worker does not emit **ACK** until a **RECEIPT** exists.

### 5. COMPLETE is the outcome, and it is different from the ACK

**COMPLETE** is the last card. It is the state the business record reaches when the whole chain has finished.

A worker can ACK the queue and the business record can still not be complete. The ACK is an act of handshaking with the transport; **COMPLETE** is a property of the workflow.

Conflating them is common: a function returns `200` and the developer writes the job off as done. But the `200` is the queue acknowledgement. The actual completion is a separate fact, sometimes several minutes later, and the diagram keeps them apart.

### 6. The lower path is the crash story, and every queue must be able to tell it

Below the success path, a coral dashed arrow drops from **WORKER A**. It leads to **WORKER CRASH**, then a red **LEASE EXPIRE** hourglass, then a teal **SAME ITEM** envelope, and finally a cyan arrow into **WORKER B**.

That is a three-sentence plot. Worker A receives the item. Worker A crashes. The lease expires. The queue makes the item visible again. Worker B receives it.

Notice that the item is not a copy; it is the **same item**. The queue did not lose it, did not create a new one, did not merge two. It just waited, and when the lease expired it offered the same work again.

This is where the design lives. The queue's job is not to guarantee exactly once. The queue's job is to guarantee at-least-once delivery with a lease, and the rest is the worker's responsibility.

The next diagram picks up that responsibility: what the worker does when it sees the same item again.

![On dark navy, a WORK ITEM carrying an IDEMPOTENCY KEY splits into ATTEMPT 1 and ATTEMPT 2. Each attempt begins with CHECK DEDUP STORE, then a green 'RECEIPT FOUND' path returns the same result through ACKNOWLEDGEMENT to COMPLETE, while a red 'NO RECEIPT FOUND' path drops to PROCESS WORK. In ATTEMPT 1, PROCESS WORK leads to TIMEOUT and a dashed 'NO ACKNOWLEDGEMENT' loop back to the work item. In ATTEMPT 2, PROCESS WORK leads to PERMANENT FAILURE, then RETRY BUDGET, then 'BUDGET EXHAUSTED' enters a red POISON / DEAD LETTER box with a skull. A green shield labelled NO INFINITE LOOP sits to the right.](../diagrams/131-retry-idempotency-poison-work.png)

**Redelivery without a receipt check is how one becomes two.** This diagram's CHECK DEDUP STORE is the same question the redelivered worker in 129 must answer: *has anyone already produced a durable result for this item?* If the answer is yes, return the same result and ACK. If the answer is no, you are genuinely continuing the work. If you ignore the question, the side effect happens again.

### 7. Acknowledge after durable success, and only then

The safety rule the whole diagram encodes is narrow: a work item is acknowledged only after the result or receipt needed for recovery is durable.

That means the ACK is not the worker patting itself on the back. It is the worker telling the queue: the world has been changed in a way that I can prove, and I no longer need this item.

Until that point, the lease is the queue's safety net. If the worker crashes, the queue cancels the lease and the work resurfaces. If the worker ACKs too early and then crashes before the effect is durable, the queue deletes the item and the work is lost forever.

---

## Case study — Moorland Financial, the refund that left the queue twice

Moorland processes payments and refunds for about 470,000 small-business accounts. Refunds are typically under £5,000 and are normally settled within a few minutes. Their queue processed roughly 2,800 refunds a day.

Their worker called the payment provider, recorded the provider's response in a database row, and then acknowledged the queue.

### What they had

A single worker per queue. A database transaction that wrote the provider response and the queue ACK in one commit.

If the provider call succeeded but the database commit failed, the work was not ACKed. The queue redelivered. The worker called the provider again. Most days this produced a duplicate refund once or twice, which operations caught and reversed by hand.

### The hour

A data-centre cooling fault took down the worker's host at 14:17. The worker had just received a provider `202 Accepted` for a £12,400 refund when the power went. The database commit did not complete. The queue's lease expired after 30 seconds.

The failover worker came online. It picked up the same item. It had no receipt to check, because the first worker's provider response had never been committed. It called the provider again. The provider, seeing a new request, processed a second refund.

The first refund was not yet settled, so the second one also completed. The business received £24,800 back from its own refund.

### What the queue did correctly

It redelivered the item when the lease expired. That is exactly what the diagram says should happen.

The queue was not the problem. The problem was that the worker's **RECEIPT** step was inside the same transaction as its **ACK** step. A crash between the provider `202` and the commit meant no receipt existed, so redelivery looked like a brand new job.

### The fix

**Receipt outside the ACK transaction.** The provider response is written to an immutable side-effect receipt as soon as it arrives, before the ACK.

**Receipt before idempotency.** A redelivered worker now checks the dedup store first. If a receipt exists, it does not call the provider. It returns the existing result and ACKs.

**Lease heartbeats.** The worker extends the lease only while it is actively processing, not while it is waiting for the provider. If the provider is slow, the worker's heartbeat prevents the lease expiring mid-call.

**Visibility matched to commit time.** The visibility window was increased from 30 seconds to five minutes, long enough to cover the provider round-trip and the receipt write, but short enough that a crashed worker does not hold an item for an unacceptable time.

### Results

- **Duplicate refunds from queue redelivery:** 1–2 per day → 0.
- **False reprocessing after provider `202` and no commit:** 1 incident, £12,400 recovered → structurally impossible.
- **Average refund completion time:** unchanged, because the extra receipt write is local and cheap.
- **Time to detect a stuck in-flight refund:** reduced from hours to the length of one missed heartbeat.

### The line in their engineering standard

*Commit the receipt before you acknowledge the queue. The ACK is not the result; it is proof that the result has already been made durable.*

---

## Composition

A horizontal flow across the upper portion, with a failure loop running below and rejoining from the left.

**Left:** **PRODUCER** — a blue platform holding a factory icon with a chimney.

**Cyan arrow** → **DURABLE QUEUE** — a blue barrel on a blue platform, with a white envelope visible inside.

**Dashed cyan arrow** → **WORKER A** — a blue server on a blue platform, with a gear on its face. Above the arrow, in cyan text: **Delivery creates LEASE / VISIBILITY WINDOW**.

**Upper path:** from **WORKER A**, a cyan arrow runs right through four white cards on blue platforms — **PROCESS** (gear), **RECEIPT** (clipboard with check), **ACK** (circle with check), **COMPLETE** (flag). Beneath all four, a **teal baseline** with upward arrows feeds each card.

**Lower path:** a **coral dashed arrow** drops from **WORKER A** to **WORKER CRASH** — a red server with a white X on a red platform — then a **coral dashed arrow** to **LEASE EXPIRE** — a red hourglass on a red platform — then a **coral dashed arrow** to **SAME ITEM** — a teal envelope on a teal platform — and finally a **cyan arrow** to **WORKER B** — a blue server identical to WORKER A.

## Element by element

**PRODUCER** — the source of work.
**DURABLE QUEUE** — the store that outlives any worker.
**WORKER A / WORKER B** — interchangeable consumers. The labels A and B are roles, not identities.

**LEASE / VISIBILITY WINDOW** — temporary custody, drawn as a dashed arrow.
**PROCESS → RECEIPT → ACK → COMPLETE** — the success chain.

**WORKER CRASH** — the failure that triggers redelivery.
**LEASE EXPIRE** — the queue's mechanism for noticing the crash.
**SAME ITEM** — not a new item. The original work, made visible again.

## Colour and flow semantics

- **Cyan arrows** carry forward work and successful delivery.
- **Cyan dashed** carries the initial delivery as a lease — temporary, bounded, not ownership.
- **Teal baseline** with upward arrows carries the durable result/receipt into each stage, matching the event, acknowledgement, receipt and checkpoint vocabulary.
- **Coral dashed** carries the crash path and the sequence of lease expiry and redelivery.
- **Teal** on the **SAME ITEM** envelope marks that the work itself is still valid and durable; only the worker has failed.
- The **separation of ACK and COMPLETE** is the central device: handshaking with the transport is not the same as finishing the workflow.

## How to present it

**Start with the crash scenario.** Most rooms understand queues as *send and forget*. Ask what happens if the worker dies after receiving an item but before finishing. Then draw the lower path.

**Trace the four cards.** PROCESS, RECEIPT, ACK, COMPLETE. Ask which of the four the worker currently does first in their codebase. The most common answer is ACK before RECEIPT, and that is the bug.

**Point at the dashed arrow and ask what dashed means.** Temporary, not ownership. Then ask how they extend the temporary window — heartbeats, visibility timeouts, leases. If the answer is "the framework handles it," the framework is making this diagram's most important decision implicitly.

**Make the ACK/RECEIPT order concrete.** Acknowledging the queue means the queue may delete the item. What would survive if the worker vanished immediately after? If the answer is nothing, the ACK is too early.

**Show the crash-to-redelivery story.** Worker A crashes, lease expires, same item goes to Worker B. Then ask what Worker B should do. The honest answer is *it depends on whether a receipt exists*.

**Tell the Moorland hour.** A £12,400 refund doubled because the provider `202` and the queue ACK were in the same transaction. The commit failed, the worker died, the queue redelivered correctly, and the second worker had no receipt to find.

**Present the fix as reordering, not re-architecting.** Commit the provider response as an immutable receipt first, then ACK. Add a dedup check so redelivery returns the same result. That is the next diagram, and it is a direct continuation of this one.

**Point at COMPLETE and ask what it means in their system.** It is almost never the same moment as the queue ACK. Mapping the two is where the hidden coupling lives.

**Close on the standard.** *Commit the receipt before you acknowledge the queue. The ACK is not the result; it is proof that the result has already been made durable.*

**Timing.** Twenty-five minutes. Thirty-five if the room draws the four stages for one real queue in their system, which usually reveals that ACK and RECEIPT are not separated.

---

## Lab and checkpoint

**Lab:** Draw the four stages for one queue in your system: process, receipt, ack, complete. Identify whether the worker creates a durable receipt before it ACKs the queue. If not, reorder the steps and add a deduplication check so a redelivery returns the same receipt.

**Checkpoint:** Why must the receipt come before the ACK?

**Answer:** Because the ACK tells the queue the item can be deleted. If the worker crashes after ACK but before creating a durable receipt, the item is gone and the result is lost. A redelivery will then do the work again, potentially causing duplicates.

## Glossary

- **ACK** — the acknowledgement that the queue can remove the item.
- **Complete** — the final outcome of the work, which may differ from the ACK.
- **Deduplication** — the check that prevents redelivery from causing duplicate effects.
- **Lease** — the temporary window during which a worker has exclusive visibility of an item.
- **Process** — the first step where the worker starts handling the item.
- **Queue** — the durable buffer that holds work until a worker is ready.
- **Receipt** — the durable record that the work was attempted.
- **Redelivery** — the queue sending the same item to another worker after a failure.
- **Visibility window** — the time an item is hidden from other workers after it is leased.
- **Worker** — the component that processes items from the queue.

## Sources

- Queue leases, receipts, and acknowledgements
- Deduplication and at-least-once delivery
- Durable workflow crash recovery
