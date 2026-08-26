# Diagram 10 — Modern MCP Request

![An exploded layer view on dark navy. Four glowing slabs are stacked vertically, each connected by a thin teal line to a labelled card on the left: VERSION HEADER showing a 2026-07-28 tile, METHOD HEADER showing a tools/list tile, JSON-RPC BODY showing white braces around code lines, and PER-REQUEST META showing an avatar tile and a clock. A large teal arrow leaves the stack and enters a blue server tower marked with a globe.](../diagrams/10-modern-mcp-request.png)

**Module:** 2 — MCP capabilities
**Role in the course:** reading the wire envelope
**Layout:** four exploded layers with a labelled key, feeding one server

---

## At a glance

One request, pulled apart into its four layers. A version, a method, a body, and metadata — stacked, labelled, and then delivered as a single thing to a server.

This is the most literal diagram in the library. It is not a metaphor for a request; it is a picture of one. The two concrete values on the slabs — **2026-07-28** and **tools/list** — are real, and putting real values on the picture is what makes it usable for debugging rather than just for orientation.

---

## What the diagram teaches

### 1. Four layers, and each answers a different question

The exploded view separates concerns that arrive fused on the wire.

**VERSION HEADER — "which rules apply?"** The slab carries the tile **2026-07-28**. This is the protocol revision the request is written against. It tells the server how to interpret everything below it: which fields are expected, which are optional, what the shapes mean, and which behaviours are in effect.

**METHOD HEADER — "what am I asking for?"** The tile reads **tools/list**. The operation being invoked, named at the envelope level rather than buried in the body. Being able to see the method without parsing the payload is what makes routing, logging, rate limiting and access control possible at the edge.

**JSON-RPC BODY — "with what arguments?"** Drawn as white braces wrapping rows of code lines. The actual call: the parameters, the request identifier, the structured content.

**PER-REQUEST META — "in what circumstances?"** An avatar tile, text lines, and a small clock. Who is asking, and the situational data attached to this particular request — identity, trace context, timing.

The separation is not cosmetic. Each layer is consumed by a different part of the stack, often before the layers below it have been read at all.

### 2. Version travels with the request, not with the connection

The topmost slab carries a date. That placement — at the top of every request, not agreed once at connection time — is a deliberate design property and it is the same claim the stateless diagram makes:

![Two mirrored platforms, REQUEST 1: COMPLETE carrying a V1 tile and REQUEST 2: COMPLETE carrying a V2 tile, both pointing at one server, with NO SESSION MEMORY in coral beneath.](../diagrams/09-stateless-mcp.png)

There, two requests carry V1 and V2 simultaneously against the same server. Here you can see the mechanism that makes that possible: the version is a header on the envelope.

The practical consequences:

- **Staged rollouts are safe.** Old and new clients coexist without a coordinated cutover.
- **Mixed-version traffic is normal.** A load balancer can route any request to any instance regardless of revision.
- **Version bugs are visible.** When something misbehaves, the revision is right there in the request rather than being an inference about when the connection was established.

The date format is itself a choice worth noticing. A dated revision — rather than a semantic version number — communicates that the protocol evolves on a calendar rather than through a compatibility contract of major and minor numbers. You are asserting *which day's rules* you were built against.

### 3. The method sits outside the body for operational reasons

`tools/list` appears on its own slab, above the JSON-RPC body rather than inside it.

This is what allows everything in front of your handler to work without parsing the payload:

- **Routing.** Send `tools/list` to a cheap read path and mutating methods to a guarded one.
- **Rate limiting.** Different budgets for different methods, applied before the body is deserialised.
- **Authorisation.** Refuse a method the caller may not invoke without inspecting its arguments.
- **Observability.** Group and count by method in logs and metrics without a parsing step.
- **Auditing.** Record what was attempted even when the body was malformed and rejected.

That last one matters more than it sounds. A request whose body fails to parse should still produce an audit entry saying *what was attempted*. If the method is only knowable by parsing the body, a malformed request is unloggable in any useful way.

### 4. Per-request meta is where identity and trace context live

The bottom slab carries an avatar and a clock. Two categories of thing.

**Identity per request.** Who is asking, asserted here, evaluated here. Not established at connection and remembered. This is what makes permission revocation take effect immediately rather than at next reconnect.

**Trace and timing context.** The clock glyph. Correlation identifiers, deadlines, timeouts. This is the layer that lets you follow one user request across a dozen services and answer "which of these calls belonged to that ticket?"

Putting meta in the envelope rather than the body keeps it separable from the call's semantics. The arguments to `tools/list` have nothing to do with who is asking or which trace this belongs to, and mixing them makes both harder to handle.

### 5. It is four layers going in and one thing arriving

The composition explodes the request for teaching and then reassembles it: a single large teal arrow leaves the stack and enters the server tower.

That reassembly is worth pointing at. On the wire this is one message. The layers are conceptual — a way of thinking about what a request must carry — not four separate transmissions. The exploded rendering is a cutaway, like an engineering drawing of an assembly.

The consequence for debugging: **all four layers are present in every request you capture**. When something goes wrong, you do not have to reconstruct the version from deployment history or the identity from session logs. It is all in the message, and the diagram tells you where to look.

---

## Case study — Halyard, the fortnight of the silent version bug

Halyard runs a document processing platform. Their capability server exposes about forty tools to a fleet of internal clients — a web assistant, a batch processor, a CLI used by their support team, and two integrations built by other teams.

They upgraded their capability server to a newer protocol revision. The rollout was staged over two weeks, and for eleven days of it something was subtly wrong.

### The symptom

Their support team's CLI began occasionally reporting that documents had no extracted fields, when the documents plainly did. Not always — roughly one call in six. Retrying usually worked.

The support team did what support teams do: they retried, it worked, and they stopped reporting it. It surfaced properly when a support engineer mentioned in passing that the CLI was "a bit flaky lately."

### Why it was hard to find

Every obvious explanation was wrong.

**Not the extraction.** They pulled document IDs from the failing calls and re-processed them directly. Fields extracted correctly every time.

**Not the tool.** Direct calls to `documents/extract` from a test harness worked consistently.

**Not load.** The failures did not correlate with traffic. They happened at 3am with one user as readily as at midday.

**Not one instance.** They suspected a bad deploy on one server. Failures were spread evenly across the fleet.

Three days went into this before anyone captured a raw request.

### What the envelope showed

They logged complete requests — all four layers — for an hour, and the pattern appeared almost immediately.

The **version header** on the failing requests read a revision older than the one succeeding requests carried. Two different revisions were in flight from what everyone believed was a single client.

The cause was mundane. The support CLI was distributed as a binary that engineers installed locally and updated when they remembered. Roughly a third of the support team was running a build from before the protocol upgrade. Those builds sent the older revision.

Under the older revision, the response shape for `documents/extract` nested extracted fields one level deeper. The newer server honoured the older revision correctly and returned the older shape — exactly as designed. The **old CLI parsed it fine**. But some support engineers had *partially* updated: new CLI binary, cached old configuration that pinned the version header to the previous revision. So a new client, which expected the new shape, was declaring an old version and receiving the old shape, and reading an empty field list from the wrong nesting level.

The server was correct throughout. The client was correct throughout. The **version header was lying** about which client this was.

### Why the four-layer view found it

The team's logging before this incident captured the method and a summarised body. It did not capture the version header, because nobody had thought of the version as request data — it was a deployment property, something you knew from what was installed.

The diagram's top slab is precisely the correction to that assumption. Version is request data. It travels on every message and it can be wrong independently of what the client actually is.

Once they added the version header to their structured logs, the query took thirty seconds: group failures by declared revision, observe that they are entirely in one bucket.

### What they changed

**All four layers are logged.** Version, method, identity and trace, on every request. Bodies are sampled; the envelope is always captured.

**Version mismatch is a first-class metric.** They chart request volume by declared revision. A revision that should have been retired showing non-zero traffic is now an alert rather than a discovery.

**The CLI stopped pinning the version in config.** The declared revision is now compiled into the binary alongside the code that depends on it. A client cannot declare a revision its code was not built for, because there is no separate place to configure it.

**Malformed-body requests produce audit entries.** During the investigation they found that requests failing to parse produced no useful log line at all. Because the method lives in the envelope, they could start recording *what was attempted* even when the body was unreadable. That closed a hole they had not known about.

### The wider finding

The review's conclusion was that the team had been treating the request as its body. Everything they logged, monitored and reasoned about was the JSON-RPC payload. The three envelope layers were plumbing — assumed correct, therefore invisible, therefore unfalsifiable.

Eleven days of intermittent failure came from an assumption about a value that was present in every single request the whole time.

---

## Composition

The frame is an exploded assembly view. Four glowing slabs are stacked vertically at centre-left, angled in isometric perspective and separated by visible gaps so that each can be read independently. Thin teal connector lines run from each slab leftward to a dark labelled card.

On the right, a large teal arrow — partly solid, partly dashed — leaves the stack and enters a blue server tower marked with a teal globe, indicating that the four layers travel as one message.

## Element by element

**VERSION HEADER** *(top slab, blue)*
Carries a dark tile reading **2026-07-28** alongside text lines. Its key card on the left shows a small window icon displaying the same date. The protocol revision this request is written against.

**METHOD HEADER** *(second slab, teal)*
Carries a dark tile reading **tools/list**. Its key card shows a browser-style icon with the same method name. The operation being invoked, named at envelope level.

**JSON-RPC BODY** *(third slab, dark blue)*
Shows a large white opening brace `{` and closing brace `}` wrapping several rows of code lines in blue and teal. Its key card shows a document icon with `{ }`. The structured call — parameters, request id, content.

**PER-REQUEST META** *(bottom slab, teal)*
Shows an avatar tile, text lines, and a small clock glyph at the lower right. Its key card shows a contact-card icon. Identity, trace context and timing for this specific request.

**The server tower**
A blue upright unit with two indicator dots and a large teal globe on its face. The destination — one message arriving, not four.

## Colour and flow semantics

- The slabs alternate **blue and teal**, which visually groups them into pairs: version and body in blue, method and meta in teal. This is a legibility device rather than a semantic grouping.
- **Thin teal connector lines** link each slab to its label without implying flow — they are callouts, not arrows.
- The single **large teal arrow** on the right is the only directional element, and it carries all four layers together into the server.
- The slabs are **translucent and glowing**, suggesting layers of one object rather than four separate objects.

## How to present it

**Ask what they log about a request.** Before showing the diagram. Almost every answer is "the method and some of the body." Then reveal the four layers and ask which two they are not capturing. Usually version and per-request meta.

**Point at the two real values.** `2026-07-28` and `tools/list` are actual values, not placeholders. Ask what the date means and where it comes from. Then ask the question that matters: *how would you know if a client was declaring the wrong one?*

**Ask why the method is not in the body.** This is the best question in the session, because the answer is a list and the room can build it: routing, rate limiting, authorisation, metrics, and — the one they will not get — auditing malformed requests. Walk to that last one and ask what their logs contain when a body fails to parse. Most rooms discover a gap.

**Do the reassembly.** Point at the exploded slabs and then at the single arrow. Say plainly: this is one message. The layers are a cutaway. This prevents the misreading that these are four round trips.

**Connect it to statelessness.** Put the two diagrams together and let the version header explain the V1/V2 detail:

![Two mirrored platforms, REQUEST 1: COMPLETE with a V1 tile and REQUEST 2: COMPLETE with a V2 tile, converging on one server above NO SESSION MEMORY in coral.](../diagrams/09-stateless-mcp.png)

Diagram 09 asserts that two protocol revisions can be in flight at once. Diagram 10 shows the mechanism. Presented in that order, the second answers a question the first raised.

**Run the debugging drill.** Give the room a symptom — "one client in six gets empty results, retries work, all servers affected equally" — and ask which layer they would capture first. Then tell them the Halyard answer. The lesson is not the specific bug; it is that three of the four layers were invisible in their telemetry because they were assumed to be plumbing.

**Timing.** Fifteen minutes. Twenty-five with the debugging drill, which is worth running with any team that operates a server rather than only calling one.

---

## Lab and checkpoint

**Lab:** Pick one MCP-style request path in a system you operate. Write down what is currently logged for each of the four layers — version header, method header, body, and per-request meta. For any layer that is not logged, write the failure scenario that would be invisible without it and the log field that would make it visible.

**Checkpoint:** Why is the method not in the body?

**Answer:** Because the method is needed for routing, rate limiting, authorisation, metrics, and auditing malformed requests before the body is parsed. Keeping it in the header lets the server make decisions about the request before it has to understand the full body.

## Glossary

- **Body** — the JSON-RPC payload of the request.
- **Layer** — one of the four parts of a modern MCP request: version header, method header, body, and per-request meta.
- **Method header** — the named operation, such as `tools/list`, used for routing and policy.
- **Per-request meta** — context carried with the request, such as correlation IDs or identity claims.
- **Version header** — the protocol revision, such as `2026-07-28`, allowing multiple versions to coexist.
- **JSON-RPC** — the request/remote-call format used by MCP.

## Sources

- MCP 2026-07-28 request and protocol-version model
- JSON-RPC 2.0 specification
- Observability and per-request metadata design patterns
