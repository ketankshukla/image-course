# Diagram 48 — Multi Round-Trip Requests

![Five numbered stages arranged around a central server on dark navy. 1 TOOL CALL shows a card with a teal gear. 2 INPUT REQUIRED, numbered in coral, shows a coral pause badge beside a white question card. 3 USER ANSWER shows a person at a laptop with a message bubble. 4 RETRY CALL shows a card carrying INPUT RESPONSES and REQUEST STATE rows. 5 FINAL RESULT shows a card with a teal check. Cyan arrows run from the user answer back into the server and from the retry call up into it.](../diagrams/48-multi-round-trip-request.png)

**Module:** Modern MCP
**Role in the course:** how a stateless call asks a question
**Layout:** a five-stage loop around a central server

---

## At a glance

A tool call pauses, asks a question, gets an answer from a person, and is **retried carrying both the answer and the original request state** — after which it completes.

The apparent contradiction is the lesson. The protocol holds no session, yet a call can span a human decision that takes minutes. The resolution sits on the card at stage 4: **INPUT RESPONSES** and **REQUEST STATE** travel with the retry. The client carries the continuity; the server carries none.

---

## What the diagram teaches

### 1. Input required is a first-class outcome, not an error

Stage 2 is numbered in **coral** — the only coral numeral in the sequence — and shows a **pause badge** beside a question card.

Pause, not stop. The call did not fail. It reached a point where it genuinely could not proceed without information only a person has, and it said so in a structured way.

The distinction matters because the alternatives are both bad. A tool that guesses produces confident wrong outcomes. A tool that errors produces an operator who re-submits the identical call, which fails identically. Naming the state correctly is what allows the right thing to happen next.

The coral numeral is doing careful work: this is a stage that needs attention, and it is not a failure.

### 2. The question is an artefact, not a message

Stage 2's white card is a **structured question object**, not a chat line.

For a person to answer usefully, the pause has to carry what was being attempted, what is ambiguous, what the options are, and what happens with each. A pause that says "more information needed" produces a human who has to reconstruct the situation before they can answer.

This is the same requirement the agent decision loop's ask-human branch has, expressed at the protocol level rather than at the reasoning level.

### 3. The retry carries two things, and both are named on the card

Stage 4's card has two labelled rows, and they are different in kind.

**INPUT RESPONSES** — what the person answered. The new information.

**REQUEST STATE** — everything the original call had established before it paused. The work already done.

Separating them is the diagram's central technical claim. Without request state, the retry is a fresh call that must redo everything: re-resolve entities, re-fetch records, re-derive whatever it had worked out. That is expensive, and for anything with side effects it is dangerous.

Carrying request state means the retry resumes rather than restarts.

### 4. The retry goes to "any server", which is the point

The cyan arrows from stages 3 and 4 both converge on the **central server stack**, and the server is drawn as a generic instance rather than as the specific one that handled stage 1.

That is the whole reason both cards exist. Because the retry carries the answer *and* the state, it does not need to reach the instance that paused. Any instance can pick it up.

If the server held the paused call in memory, you would need affinity, and a call paused for twenty minutes across a deploy would be lost. The two cards are what buy you a pause that survives restarts, rebalancing, and time.

![A self-contained request envelope carrying METHOD, NAME, REQUEST ID and AUTH SCOPE, travelling through a server, a policy gate and a tool with a result returning.](../diagrams/47-stateless-mcp-request.png)

This is the previous diagram's envelope, refilled. The retry is itself a complete, self-contained request — it just happens to contain more than the first one did.

### 5. The loop is around a server, not along a line

The composition is circular: the five stages orbit the central server rather than proceeding left to right.

That geometry says the server is touched repeatedly by one logical operation. Stage 1 reaches it, stage 4 reaches it again, and stage 5 leaves from it. From the server's point of view these are two independent requests; from the user's point of view it is one piece of work that paused.

Holding both readings at once is the skill this diagram teaches.

### 6. It is bounded, and the diagram does not draw the bound

Honest gap. Nothing here shows what happens if the person never answers.

Every production implementation needs an expiry on the pause and a defined outcome when it elapses. Otherwise you accumulate paused work that nobody will ever resolve — the operational equivalent of a leak.

The approval-card diagram later in the volume shows the expiry made explicit, and the pattern transfers directly.

---

## Case study — Trelane Freight, the customs code question

Trelane arranges international freight for about 900 exporters. Their booking assistant creates shipments, and one step is assigning a customs commodity code — which determines duty, licensing requirements, and whether the shipment needs additional documentation.

Getting it wrong is expensive: a misclassified shipment can be held at the border for days, and repeated misclassification attracts regulatory attention.

### The problem with the first version

`assign_commodity_code(description)` took a goods description and returned a code.

For about 70% of shipments the description was unambiguous and the tool was right. For the remaining 30% it was not — and the tool had no way to say so.

The clearest recurring case: *"industrial fasteners, stainless."* That maps to at least four codes depending on whether the fasteners are threaded, whether they are for aerospace use, and their diameter. Duty rates differ by up to 6%.

The tool picked the most common match. Over a year that produced 47 shipments held at customs, two regulatory queries, and about £31,000 in duty adjustments and demurrage.

### What they changed

The tool gained the ability to pause.

**Stage 1 — Tool call.** `assign_commodity_code` is called with the description, the destination country, the declared value and the exporter's history.

**Stage 2 — Input required.** For the ambiguous case, the tool returns a structured pause rather than a code:

> Cannot determine code from description. Candidates: 7318.15 (threaded fasteners, non-aerospace, duty 3.7%), 7318.16 (nuts, duty 3.7%), 8803.30 (aerospace fasteners, duty 0%, requires end-use certificate). Need: are these threaded, and is the end use aerospace?

Three candidates, the consequence of each, and the two facts that would resolve it. A booking coordinator can answer without knowing anything about tariff schedules.

**Stage 3 — User answer.** The coordinator asks the exporter or checks the specification, and answers: threaded, non-aerospace.

**Stage 4 — Retry call.** The retry carries both cards.

*Input responses:* threaded = true, aerospace = false.

*Request state:* the parsed description, the destination, the declared value, the candidate set already computed, and the exporter-history lookup already performed. Recomputing the candidate set means re-querying the tariff database, which takes about 800ms — worth carrying rather than repeating.

**Stage 5 — Final result.** Code 7318.15, with the reasoning and the answers recorded against the shipment.

### What the request state bought them

Their first attempt did not carry request state. The retry sent only the answer, and the tool started again from the description.

Two problems appeared within a week.

**The candidate set could differ.** The tariff database is updated periodically. A retry twelve minutes after the original could recompute against a slightly different dataset, producing a candidate the coordinator had never been offered. Twice, a coordinator answered a question about three options and received a code from a fourth.

**Repeat work was measurable.** Roughly 30% of bookings paused, each pause meant a duplicated 800ms tariff lookup plus the exporter-history query, and at their volume that was a noticeable share of their tariff database's load.

Carrying the request state fixed both. The retry resumes against the candidate set the coordinator actually saw.

### The expiry they had to add

The diagram does not show one, and Trelane needed one within a month.

Coordinators pause bookings and go home. A pause with no expiry accumulated: after four weeks they had 180 paused classification calls, some of them for shipments that had been cancelled.

They set a 24-hour expiry. On expiry the pause resolves to a defined outcome — the shipment is flagged for manual classification and the booking cannot proceed to submission. Not a silent default to the most common code, which is what the old system effectively did.

### Results after nine months

- **Shipments held at customs for misclassification:** 47 in the preceding year, 3 since.
- **Pause rate:** about 28% of bookings, median answered in 11 minutes.
- **Expired pauses:** roughly 2%, nearly all cancelled shipments.
- **Duty adjustments and demurrage:** from £31,000 to under £2,000.

### The framing their operations director uses

*The tool didn't get smarter. It got permission to admit it didn't know, and a way to ask.*

---

## Composition

Five numbered stages arranged around a central server stack.

**1 TOOL CALL** (upper left) → **2 INPUT REQUIRED** (upper centre) → **3 USER ANSWER** (upper right), connected by cyan arrows. From stage 3, a cyan line runs down and left into the **central server**. **4 RETRY CALL** (lower right) sends a cyan arrow up into the server and another left to **5 FINAL RESULT** (lower left).

Stage numerals are cyan, except **2**, which is coral.

## Element by element

**1 TOOL CALL**
A white card with a **teal gear tile** and text lines, on a blue platform.

**2 INPUT REQUIRED**
A **coral rounded badge with a white pause symbol**, beside a white card carrying a large **teal question mark**. The coral numeral marks it as needing attention.

**3 USER ANSWER**
A person seated at a laptop, seen from behind, the screen showing a teal message bubble and text lines.

**4 RETRY CALL**
A white card with two labelled rows: a teal message-bubble tile beside **INPUT RESPONSES**, and a teal database tile beside **REQUEST STATE**.

**5 FINAL RESULT**
A white card with a large **teal check disc** and text lines.

**The central server**
A dark stacked server unit with teal indicator lights, on a blue platform. Drawn generically — any instance.

## Colour and flow semantics

- **Cyan arrows** carry every transition, including the pause and the retry — the whole loop is normal operation.
- **Coral** appears only on the pause badge and the stage-2 numeral, marking attention rather than failure.
- **Teal** marks the working elements: the gear, the question mark, the two retry cards' tiles, the final check.
- The **circular arrangement around one server** conveys that the server is touched twice by one logical operation.

## How to present it

**Ask what a tool does when it needs information it does not have.** Guess or fail. Both are common and both are wrong. Then show the third option.

**Point at the coral numeral on stage 2 and ask why it is not red-and-terminal.** It is a pause, not a failure. Then ask what happens operationally when a pause is reported as an error — an operator re-submits the identical call.

**Read the Trelane pause aloud.** Three candidates, their duty consequences, and the two facts needed. Ask whether a coordinator with no tariff knowledge could answer it. Then contrast with "more information required."

**Spend the most time on the two cards at stage 4.** Ask what each is for. Input responses is the new information; request state is the work already done. Then ask what happens without request state — and give them Trelane's two failures: a recomputed candidate set the user never saw, and duplicated expensive lookups.

**Ask which server the retry goes to.** Any of them. That is only possible because both cards travel with it. Connect back to the envelope diagram — the retry is another self-contained request.

**Name the missing bound.** Ask what happens if nobody answers. Trelane's 180 accumulated pauses, then a 24-hour expiry with a defined outcome — flagged for manual handling, not a silent default. The silent default is what the old system effectively did.

**Timing.** Twenty minutes. Twenty-five if you work through what request state would need to contain for one of the room's own tools.

---

## Lab and checkpoint

**Lab:** Design a multi-round-trip tool call for one capability that sometimes needs more information. Define the initial inputs, the pause condition, the extra input, the request state that must travel with the retry, and the final result. Then write the expiry rule and what happens if nobody answers.

**Checkpoint:** Why must request state travel with the retry, not live on the server?

**Answer:** Because the retry may land on any server instance. If state lives on one server, a retry to another instance would lose the work already done. Carrying request state in the retry makes the call self-contained and stateless.

## Glossary

- **Final result** — the completed outcome of the multi-round-trip call.
- **Input response** — the additional information the server needs to continue.
- **Multi-round-trip** — a tool call that pauses for input and resumes later.
- **Pause** — the state where the server has a partial result but needs more information.
- **Request state** — the work already done, carried with the retry so the server can resume.
- **Retry call** — the second request that carries the input response and request state.

## Sources

- Multi-round-trip and continuation-passing in tool calls
- State-carrying request patterns and stateless resumption
- MCP request/response and task pause models
