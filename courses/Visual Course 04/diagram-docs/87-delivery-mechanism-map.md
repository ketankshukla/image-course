# Diagram 87 — Delivery Mechanism Map

![A DURABLE TASK STATE platform on the left of a dark navy frame fans to four labelled options — SAME RESPONSE PROGRESS with OPEN CONNECTION, SUBSCRIPTIONS LISTEN with OPT-IN EVENT TYPES, POLLING with RECONCILIATION READ, and WEBHOOK OR CHANNEL with SIGNED CALLBACK — each paired with a white card. Teal arrows from all four converge on a FINAL GET TASK clipboard on the right. A banner beneath reads CHOOSE BY: CONNECTION LIFETIME, CALLBACK REACHABILITY, RELIABILITY, USER EXPERIENCE.](../diagrams/87-delivery-mechanism-map.png)

**Module:** MCP at scale
**Role in the course:** four ways to learn that durable work progressed
**Layout:** one source fanning to four mechanisms, all converging on one authoritative read, with a selection banner beneath

---

## At a glance

**DURABLE TASK STATE** on the left. Four delivery mechanisms in the middle. **FINAL GET TASK** on the right — and every one of the four converges on it.

Beneath, a selection banner: **CHOOSE BY: CONNECTION LIFETIME, CALLBACK REACHABILITY, RELIABILITY, USER EXPERIENCE.**

Two claims. All four mechanisms are views of one durable state, not four independent channels. And whatever you choose, the authoritative answer comes from reading the task.

---

## What the diagram teaches

### 1. Durable task state is the source, and all four are derived

Everything begins at one platform: a clipboard with a database.

The four mechanisms do not each maintain their own view. They are four ways of learning about **one state that exists independently of all of them**.

That framing is what makes them interchangeable and combinable. A client can stream and also poll. A webhook can fail and polling can cover it. None of them is the truth; the task is.

### 2. Each mechanism carries a qualifying phrase, and the phrases are the design content

**SAME RESPONSE PROGRESS — open connection.** Progress delivered on the connection that made the request. Requires that connection to stay up.

**SUBSCRIPTIONS LISTEN — opt-in event types.** A stream the client subscribes to, selecting which event types it wants.

**POLLING — reconciliation read.** The client asks. The phrase "reconciliation read" is doing careful work: polling is not merely a way to get updates, it is a way to **reconcile** what you believe against what is true.

**WEBHOOK OR CHANNEL — signed callback.** The server calls the client. "Signed" is not optional decoration — an unsigned callback endpoint accepts anyone's claims about your work.

### 3. The four paired cards show what each mechanism actually delivers

**Same response progress** → a message-bubble card. Conversational, incremental.

**Subscriptions** → a document-with-funnel card. Filtered content — the funnel is the opt-in.

**Polling** → a circular-arrows card. Repetition made visible.

**Webhook** → a **red padlock shield** card. Security, and it is the only red element in the frame.

That red padlock is the diagram's most pointed detail. Three mechanisms are pulled by the client. One is pushed to it, which means exposing an endpoint, which is a different risk class entirely.

### 4. All four converge on FINAL GET TASK, and that is the reliability argument

Teal arrows from all four cards run right into a **clipboard with a check**.

Whatever mechanism delivered the news, the authoritative state is read from the task.

Three reasons this matters.

**Streams and callbacks can lie by omission.** A dropped stream or an undelivered webhook means the client's picture is stale, and nothing in either mechanism tells it so.

**Delivery is not confirmation.** A webhook saying "completed" is a claim. Reading the task is verification.

**It bounds the failure.** A client that treats delivery as advisory and the task read as authoritative degrades to slow rather than to wrong.

The practical rule: **use a push mechanism for latency, and a task read for truth.**

### 5. The four selection criteria are the actual decision procedure

The banner names four, and each rules out different options.

**CONNECTION LIFETIME.** Can the connection survive the work? Minutes, maybe. Hours, no. This rules out same-response progress for long work.

**CALLBACK REACHABILITY.** Can the server reach the client? A browser cannot receive a webhook. A service behind a firewall may not. This rules out webhooks for most client-side callers.

**RELIABILITY.** What happens when the mechanism fails? Polling degrades gracefully; streams and webhooks fail silently. This argues for a polling fallback under everything.

**USER EXPERIENCE.** Is a person watching? If yes, latency and incremental feedback matter and streaming earns its complexity. If no — a background service — polling or a webhook is fine and streaming is overhead.

Four criteria, and they frequently select different mechanisms for different interactions in the same system.

### 6. Opt-in event types is the detail that makes subscriptions scale

The subscription card's qualifier is **opt-in event types**, and the funnel icon reinforces it.

A subscription that delivers everything forces every client to receive and discard what it does not need. At scale that is significant traffic and significant client-side handling.

Opt-in also solves the versioning problem: adding an event type does not break a client that did not subscribe to it. That is the difference between an extensible event surface and a frozen one.

### 7. Signed is the word that makes webhooks acceptable

An endpoint on the internet that accepts "your work is done" messages needs four things, and the diagram names one of them.

**Signed** — the notification proves it came from the party you sent work to.

The other three, which the diagram implies rather than states: the notification must **correlate** to a task you created; handling must be **idempotent** because delivery can duplicate; and there must be a **fallback** because delivery can fail entirely.

That fallback is polling, which is why the convergence on **FINAL GET TASK** applies to the webhook path as much as to the others.

The durable state all four read from is the task object itself:

![A radial layout with a TASK HANDLE at centre, WORKING, INPUT REQUIRED, COMPLETED, FAILED and CANCELED around it, and TASKS GET, TASKS UPDATE and TASKS CANCEL entering from outside.](../diagrams/86-mcp-tasks-extension-lifecycle.png)

**FINAL GET TASK** here is **TASKS GET** there. The four mechanisms are four routes to one control operation.

---

## Case study — Ravenglass Media, four mechanisms in one product

Ravenglass provides video transcoding and media processing to broadcasters and streaming services. Their MCP layer exposes processing capabilities, and jobs range from four seconds to eleven hours.

They ran one mechanism — polling — for everything. It worked and it was wasteful in one direction and slow in another.

### The four interactions that needed different answers

**Thumbnail extraction.** 2–6 seconds. An editor is watching.

**Proxy generation.** 40 seconds to 4 minutes. An editor is watching, and partial output is useful — a proxy becomes scrubbable before it finishes.

**Full transcode.** 20 minutes to 11 hours. Nobody is watching. Triggered by an automated pipeline.

**Compliance analysis.** 5–30 minutes. Triggered by a scheduler, results consumed by another service.

Under uniform polling, the first was polled needlessly and the last three were polled expensively.

### Applying the four criteria

**Thumbnail extraction → same response progress.**

Connection lifetime: six seconds, trivially survivable. User experience: an editor is watching. Reliability: a failure means retry, which is cheap.

They stopped treating it as a durable task entirely for the sub-10-second case — it returns inline. The polling infrastructure around it was pure overhead.

**Proxy generation → subscriptions with opt-in event types.**

Connection lifetime: up to four minutes, and their editors' browsers hold connections that long reliably. User experience: incremental output is genuinely useful, because a partially-generated proxy is scrubbable.

They emit six event types. The editing client subscribes to three: progress, segment-ready, and completion. It does not subscribe to the three diagnostic types their operations dashboard uses.

That opt-in split is the thing that made the event surface extensible. They have added four event types since, and no client broke.

**Full transcode → webhook with polling fallback.**

Connection lifetime: eleven hours, impossible. Callback reachability: the caller is their customers' automated pipelines, which are services with reachable endpoints.

Webhooks are signed. The receiving side verifies the signature, correlates to a job it created, and handles idempotently.

**The fallback matters.** Any job with no callback after 130% of its estimated duration is polled directly. This fires on about 0.4% of jobs.

Of those, most are delivery failures — a customer's endpoint briefly unavailable. Three in a year were genuine lost notifications where the job had completed and the callback never arrived at all.

Without the fallback, those three would have been jobs their customers believed had never finished.

**Compliance analysis → polling.**

Callback reachability: the consuming service is internal and could receive a webhook, but the volume is low and the latency requirement is loose. Reliability: polling has no failure mode that needs covering.

They chose polling because it was the simplest thing that met the requirement, and the diagram's criteria gave them a defensible reason rather than an instinct.

### The security finding on the webhook path

Their initial webhook implementation verified signatures and did not correlate to a job.

A penetration test sent a correctly-formed but unsigned notification and observed it rejected. Then it sent a **correctly-signed** notification — obtained by replaying a legitimate one from a captured request — referencing a different job ID.

Their handler accepted it and marked a different customer's job as completed, causing a downstream pipeline to fetch an output that did not exist.

The fix was correlation: a notification must reference a job the receiving side actually created, for the customer the signature belongs to.

That is the "correlate to a task you created" obligation the diagram implies and does not draw, and it is the one that gets missed.

### Results

- **Polling requests:** down about 94%, concentrated on the one interaction that still uses it and the 0.4% fallback.
- **Thumbnail latency:** ~2.5 seconds of polling overhead removed.
- **Event types added since opt-in subscriptions:** 4, with 0 client breakages.
- **Lost webhook notifications caught by fallback:** 3 in a year.
- **Cross-job notification acceptance:** possible → closed.

### The line in their integration documentation

*Use the push for speed and the task read for truth. If you only have the push, you will eventually believe something that is not so.*

---

## Composition

A left-to-right fan-out and fan-in with a selection banner beneath.

**Left:** **DURABLE TASK STATE** — a clipboard with checked rows beside a blue database, on a wide blue platform.

**Centre:** four cyan arrows fan to four blue-bordered rows, each with an icon, a title, and a cyan qualifier:
- **SAME RESPONSE PROGRESS** / *open connection* (broadcast tower)
- **SUBSCRIPTIONS LISTEN** / *opt-in event types* (bell with a check)
- **POLLING** / *reconciliation read* (clock)
- **WEBHOOK OR CHANNEL** / *signed callback* (webhook glyph)

Each row is paired with a white card to its right: a **message bubble**, a **document with a funnel**, **circular arrows**, and a **red padlock shield**.

**Right:** **FINAL GET TASK** — a clipboard with a blue check disc on a blue platform, reached by **teal arrows** from all four cards.

**Beneath:** a bordered banner reading **CHOOSE BY:** followed by four items — **CONNECTION LIFETIME** (clock), **CALLBACK REACHABILITY** (teal globe), **RELIABILITY** (teal shield with a star), **USER EXPERIENCE** (person).

## Element by element

**DURABLE TASK STATE** — a clipboard with four checked rows beside a blue database stack. The single source.

**SAME RESPONSE PROGRESS** — a broadcast tower. Paired with a message-bubble card.

**SUBSCRIPTIONS LISTEN** — a bell with a green check. Paired with a document-and-funnel card, the funnel indicating opt-in filtering.

**POLLING** — a clock face. Paired with a circular-arrows card.

**WEBHOOK OR CHANNEL** — a webhook node glyph. Paired with a **red padlock shield** card — the only red in the frame.

**FINAL GET TASK** — a clipboard with a blue check disc.

## Colour and flow semantics

- **Cyan arrows** fan from the task state to the four mechanisms.
- **Teal arrows** converge from all four cards on the final task read.
- **Red** appears once, on the webhook's padlock card, marking the only mechanism that exposes an endpoint.
- **Cyan qualifier text** beneath each mechanism title carries the design constraint.
- The **convergence on one clipboard** is the reliability argument made structural.

## How to present it

**Ask how many delivery mechanisms their system uses.** Usually one, applied everywhere. Then ask whether the same choice suits a four-second job and an eleven-hour one.

**Read the four qualifiers aloud.** Open connection, opt-in event types, reconciliation read, signed callback. Each is a constraint, not a description.

**Point at the red padlock.** Three mechanisms are pulled; one is pushed. Ask what pushing requires — an endpoint on the internet accepting claims about your work.

**Ask what the convergence means.** All four arrive at one task read. Then give the rule: push for latency, task read for truth. A client that treats delivery as authoritative will eventually believe something stale.

**Walk the four criteria against a real interaction.** Take one of the room's own operations and apply connection lifetime, callback reachability, reliability, user experience. The criteria usually eliminate two options immediately.

**Tell the Ravenglass four-way split.** Same product, four interactions, four different mechanisms — including one that stopped being a durable task at all because it finishes in six seconds.

**Ask about opt-in.** Ravenglass added four event types with zero client breakages, because clients subscribe to what they want. A stream that delivers everything is a frozen surface.

**Tell the webhook penetration-test finding.** A correctly-signed notification, replayed, referencing a different customer's job — accepted, marking it complete. Signature verification without correlation is half a control.

**Ask about the fallback.** 0.4% of jobs polled because no callback arrived; three genuine lost notifications in a year. Without it, three customers would have believed jobs never finished.

**Timing.** Twenty-five minutes. Thirty-five if you apply the four criteria to three of the room's own interactions, which typically produces three different answers.

---

## Lab and checkpoint

**Lab:** Pick three different interactions in your product and apply the four criteria to each: open connection duration, callback reachability, reliability need, and user experience. Decide which delivery mechanism fits each: open connection, opt-in events, reconciliation read, or signed webhook. Then design the fallback to a final task read.

**Checkpoint:** Why must a client still do a final GET TASK even if it receives a notification?

**Answer:** Because push mechanisms are for latency, not truth. A notification can be stale, replayed, or refer to the wrong task. The final task read is the authoritative state and is the only thing a client should trust as the final result.

## Glossary

- **Callback** — a webhook or push sent to the client.
- **Delivery mechanism** — the way task state reaches the client.
- **Event types** — the categories of change a client may subscribe to.
- **Final GET task** — the authoritative read that all mechanisms converge on.
- **Open connection** — a long-lived connection such as SSE or WebSocket.
- **Opt-in** — the model where clients choose which event types they receive.
- **Reconciliation read** — a periodic poll that corrects state drift.
- **Signed webhook** — a callback that is cryptographically signed for authenticity.
- **Subscription** — the client-side registration for events or updates.

## Sources

- Task delivery patterns: polling, streaming, webhooks
- Signed webhooks and replay protection
- Event subscription and opt-in design
