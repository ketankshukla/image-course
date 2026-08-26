# Diagram 43 — Error Recovery Map

![A hub layout on dark navy. At centre, a blue platform labelled ERROR carrying a red warning triangle. Four white cards along the top — BAD INPUT with a torn document, NOT AUTHORIZED with a teal shield and padlock, TEMPORARY FAILURE with a cloud and clock, UNKNOWN SIDE EFFECT with a question mark and receipt. Four white cards along the bottom — FIX REQUEST with a checked clipboard, STOP with a red octagon and raised palm, RETRY with teal circular arrows, CHECK RECEIPT with a receipt and magnifier. Cyan arrows connect the hub to each card, except the arrow to STOP which is coral.](../diagrams/43-error-recovery-map.png)

**Module:** Agent behaviour
**Role in the course:** four kinds of failure and what to do about each
**Layout:** a central hub with four diagnosis cards above and four response cards below

---

## At a glance

One hub labelled **ERROR**, four kinds of failure across the top, and four responses across the bottom — each response sitting directly beneath the failure it belongs to.

**BAD INPUT → FIX REQUEST. NOT AUTHORIZED → STOP. TEMPORARY FAILURE → RETRY. UNKNOWN SIDE EFFECT → CHECK RECEIPT.**

The vertical pairing is the diagram. Errors are not one thing, and the single most damaging beginner habit is treating them as if they were — usually by retrying everything, which is the correct response to exactly one of these four.

---

## What the diagram teaches

### 1. Four categories, and they are distinguished by what you should do

The classification is not by where the error came from or what code it carried. It is by **what the correct response is**, which makes it immediately actionable.

**BAD INPUT** — the request was malformed or invalid. The torn document icon says it plainly: what you sent was broken. Nothing on the other side is wrong.

**NOT AUTHORIZED** — the request was well-formed and you are not permitted. The shield with a padlock is holding, not failing.

**TEMPORARY FAILURE** — nothing is wrong with the request or your permissions; the other side is momentarily unavailable. A cloud with a clock: a timing problem.

**UNKNOWN SIDE EFFECT** — the most dangerous category. You do not know whether it worked. A question mark beside a receipt: the answer exists somewhere, and you have to go and look.

### 2. Retrying is correct for one of four, and wrong for the others

The response most beginners reach for first is retry. Mapped onto this diagram, it is right in a quarter of cases and actively harmful in at least two.

**Retrying bad input** produces the same rejection forever. The request is broken; sending it again does not repair it. This is the most common cause of a client that hammers an endpoint thousands of times with an identical malformed payload.

**Retrying not-authorized** is worse. It generates a burst of denied requests from one principal, which is indistinguishable from an attack, and will get you rate-limited or blocked.

**Retrying an unknown side effect** is the one that costs money. If the first attempt may have succeeded, the retry may perform the operation a second time.

Only **temporary failure** is genuinely retryable, and even then with backoff rather than immediately.

### 3. Not authorized is the only coral arrow, and it is the only one that stops

Every arrow from the hub is cyan except one: the arrow to **STOP**, which is coral, matching the red octagon and raised-palm icon it points at.

Three of the four errors have a recovery. This one does not.

That is a genuine claim about what an authorization failure means. It is not a problem to work around — it is the system correctly declining. The right response is to stop, report it clearly, and let a person decide whether the permissions are wrong.

An agent that treats authorization failure as an obstacle to route around is an agent trying to circumvent a control. Drawing this arrow in coral, pointing at a stop sign, is the diagram saying that plainly.

### 4. Unknown side effect is the category beginners do not know exists

The fourth column, and the reason the diagram is worth teaching.

A timeout is the canonical case. You sent a request. The connection dropped before a response came back. **You do not know what happened.** The request may have arrived and been processed, arrived and failed, or never arrived at all. All three produce the identical symptom on your side.

Treating this as a failure and retrying is a coin flip. Treating it as a success and moving on risks acting on something that never happened.

The correct response is neither: **go and find out**. Which is what **CHECK RECEIPT** means.

### 5. Check receipt only works if you built receipts

This is where the diagram connects to everything else in both volumes.

Look back at the request pipeline, the frontend/backend boundary, the tool-call lifecycle, the storage map — every one of them ends with or contains a receipt. This diagram is where those receipts get used.

The recovery procedure is:

1. The operation carried an identifier — an idempotency key, a request ID, a task ID.
2. Query the audit log or task store for that identifier.
3. A receipt exists → it happened. Proceed.
4. No receipt exists → it did not happen. Safe to retry.

Without a receipt, that question is unanswerable and you are left guessing. The whole fourth column of this diagram is unavailable to a system that does not record what it does.

### 6. Fix request means fix it, and it needs a specific error to work

**BAD INPUT → FIX REQUEST**, shown as a clipboard with a green check. Correct the request and resend.

This only functions if the error told you what was wrong. A bare `400` produces a caller who can only guess. A rejection naming the field and the reason produces a caller who fixes it — which is exactly the argument the schema-validation diagram makes with its four rejection chips:

![A left-to-right flow — INPUT DATA, JSON SCHEMA, VALIDATE with REQUIRED, TYPE, FORMAT and LIMITS rows — branching to a teal ACCEPTED card and a coral REJECTED card with four failure chips.](../diagrams/34-json-schema-validation.png)

The two diagrams are two halves of one idea: **produce specific rejections, and act on the specifics you receive.** That diagram's dashed correction loop and this diagram's **FIX REQUEST** card are the same arrow seen from either end.

---

## Case study — Kingsmoor Utilities, the night 1,400 customers were billed twice

Kingsmoor supplies water to about 90,000 domestic customers. Their billing system generates monthly charges and submits them to a payment processor.

On a Thursday night, 1,400 customers were charged twice.

### What happened

The payment processor had a partial outage between 23:10 and 23:35. Requests were being received and processed, but responses were timing out.

Kingsmoor's submission code had a single error handler. Any exception — timeout, connection reset, HTTP error, malformed response — was caught and retried, up to five times, with a two-second gap.

During the 25-minute window, 1,400 charge submissions timed out. Every one was retried. Every one of the originals had actually been processed by the payment provider. Every retry was processed again.

Charges ranged from £18 to £140. Total duplicate value about £61,000, across 1,400 households, overnight, with no warning.

### Why the code did this

The error handler treated everything as temporary failure. That is the middle column of this diagram applied to all four.

For a genuine timeout the reasoning is superficially sound: the request may not have arrived, so send it again. What the code could not distinguish is that a timeout is **not** a temporary failure — it is an **unknown side effect**. The distinction is exactly the third column versus the fourth, and their handler had only the third.

### What made it worse

Three aggravating factors, all of which are common.

**No idempotency key.** Each submission was a fresh request with no identifier tying it to the charge it represented. The payment provider had no way to recognise the second submission as a duplicate of the first — from its side they were two legitimate charges.

**No receipt check.** Even after the fact, establishing which charges had been submitted twice required reconciling Kingsmoor's records against the provider's export by hand. It took two people a full day.

**Retries were immediate.** Two seconds apart, five times, from a system already under stress, into a provider already in partial outage. The retry storm extended the outage.

### The rebuild

**Four distinct error classes**, mapped exactly onto this diagram.

*Bad input* — the provider rejected the charge as malformed or invalid. No retry. The charge is flagged for review with the provider's specific reason attached.

*Not authorized* — credentials rejected or the account not permitted. **Stop everything.** The entire submission run halts and an operator is paged. This is deliberately drastic: an authorization failure mid-run means something has changed that nobody expected, and continuing is the wrong instinct.

*Temporary failure* — an explicit 503, or a connection refused before any request was sent. Retry with exponential backoff, capped at four attempts.

*Unknown side effect* — a timeout, a connection reset mid-request, or any response they could not parse. **Do not retry.** Query the provider's status endpoint for the idempotency key. If a charge exists, record it and move on. If not, resubmit.

**Idempotency keys on every submission**, derived from the account, the billing period and the amount. The provider now recognises duplicates and returns the original charge rather than creating a second one — which means that even if the classification logic were wrong, the damage is bounded.

**A reconciliation job** running an hour after every submission run, comparing Kingsmoor's receipts against the provider's records. Discrepancies are reported before customers see them.

### The aftermath

Refunds were issued within four days. Kingsmoor covered bank charges for 31 customers whose accounts went overdrawn as a result. The regulator was notified. Two customers left.

The direct cost was about £9,000 in charges and compensation on top of the refunded £61,000. The reputational cost was larger and harder to quantify — the local press covered it.

### What they wrote in the incident report

*A timeout does not mean it failed. It means you do not know. We had four kinds of error and one response to all of them.*

Eight months later, during a longer provider outage, the new code encountered 3,100 unknown-side-effect responses. It retried none of them. It checked receipts for all of them, found 2,900 already processed, and resubmitted 200. Zero duplicates.

---

## Composition

A hub-and-spoke layout with the hub at centre.

**Centre:** a blue platform labelled **ERROR** in large white capitals, carrying a **red warning triangle** with a white exclamation.

**Top row:** four white cards on blue platforms — **BAD INPUT**, **NOT AUTHORIZED**, **TEMPORARY FAILURE**, **UNKNOWN SIDE EFFECT** — each connected to the hub by a **cyan arrow curving upward**.

**Bottom row:** four white cards on blue platforms — **FIX REQUEST**, **STOP**, **RETRY**, **CHECK RECEIPT** — each connected to the hub by an arrow pointing down. Three are cyan; the arrow to **STOP** is **coral**.

Each bottom card sits directly beneath its paired top card.

## Element by element

**BAD INPUT → FIX REQUEST**
*Above:* a white document **torn in two**, with a red ✗ on the left half. *Below:* a teal **clipboard** with checklist rows and a **teal check disc**. Correct it and resend.

**NOT AUTHORIZED → STOP**
*Above:* a **teal shield containing a white padlock**. Holding, not failing. *Below:* a **red octagon with a white raised palm**. Reached by the only coral arrow.

**TEMPORARY FAILURE → RETRY**
*Above:* a **blue cloud** with a **teal clock** overlapping it. A timing problem. *Below:* two **teal circular arrows** forming a refresh cycle.

**UNKNOWN SIDE EFFECT → CHECK RECEIPT**
*Above:* a large **teal question mark** beside a white **receipt** slip. *Below:* a white **receipt** with a **teal magnifying glass** over it. Go and find out.

**ERROR hub**
A blue platform with a **red warning triangle**, from which all eight arrows radiate.

## Colour and flow semantics

- **Cyan arrows** connect the hub to seven of the eight cards — diagnosis and recovery.
- The **single coral arrow** points to **STOP**, marking the only error with no recovery path.
- **Teal** marks the working recovery machinery: the clipboard check, the retry arrows, the magnifier.
- **Red** appears on the hub triangle, the torn document's ✗, and the stop octagon.
- The **vertical alignment** of each pair is the diagram's structure — diagnosis above, response below.

## How to present it

**Ask what their code does when a request fails.** Most beginner answers are "retry" or "log it and move on." Then show four categories and ask which one retry is correct for. One of four.

**Walk the three wrong retries.** Bad input retries forever against a broken request. Not-authorized retries look like an attack and get you blocked. Unknown side effect retries duplicate the operation. Naming the harm for each is more persuasive than naming the rule.

**Ask why STOP has the only coral arrow.** An authorization failure is the system working correctly. An agent that routes around it is trying to circumvent a control. That framing matters in a course about building agents.

**Spend the most time on the fourth column.** Ask what a timeout means. Push past "it failed" to "you do not know." Three possibilities — arrived and processed, arrived and failed, never arrived — with one identical symptom.

**Then tell the Kingsmoor story.** 1,400 customers, £61,000, 25 minutes, one error handler. The detail that lands is that every original had succeeded — the retries were not recovering from failure, they were duplicating success.

**Ask how you would find out.** Get the room to the answer: the operation carried an identifier, so go and look for a receipt. Then point out that this only works if receipts exist, and connect back to every diagram in the volume that ends with one. This is where those receipts get used.

**Give them the classification exercise.** Take five real failures from the room's own systems and classify each. The arguments will be about which are temporary and which are unknown — which is exactly the distinction Kingsmoor got wrong, and the most valuable one to practise.

**Mention idempotency as the backstop.** Even with correct classification, a key means a duplicate submission is recognised and refused. Belt and braces: classify correctly *and* make the operation safe to repeat.

**Close on the sentence.** *A timeout does not mean it failed. It means you do not know.*

**Timing.** Twenty-five minutes. Thirty-five with the classification exercise, which is where the temporary-versus-unknown distinction gets properly learned.

---

## Lab and checkpoint

**Lab:** Collect five real errors from a system you work on. Classify each into one of the diagram's categories: bad input, not authorised, unknown side effect, timeout, or stopped. For each, write the correct response (correct and resubmit, ask a human, verify by receipt, retry with backoff, or stop) and the wrong response that would make it worse. Then check whether your code currently does the correct one.

**Checkpoint:** What does a timeout mean?

**Answer:** A timeout does not mean the operation failed. It means you do not know whether it arrived and succeeded, arrived and failed, or never arrived. The correct response is to go and look for a receipt, not to retry blindly.

## Glossary

- **Bad input** — an error caused by a malformed or invalid request.
- **Classification** — the step of deciding which kind of error has occurred.
- **Error hub** — the central point from which the eight error cards radiate.
- **Idempotency key** — a unique identifier that lets the system refuse duplicate operations.
- **Not authorised** — an error where the caller is correctly refused.
- **Retry** — repeating a request, appropriate only for temporary, known-safe failures.
- **Stopped** — an error where the only safe response is to stop and ask a human.
- **Timeout** — a failure to get a response within an expected time, without knowing what happened.
- **Unknown side effect** — an error where it is unclear whether the operation already changed state.
- **Verify** — checking for a receipt or state to find out what happened.

## Sources

- Error classification and retry safety in distributed systems
- Idempotency keys and duplicate-operation protection
- Timeout handling and receipt-based verification
