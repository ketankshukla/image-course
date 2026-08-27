# Diagram 09 — Stateless MCP

![Two large mirrored platforms on dark navy. The left reads REQUEST 1: COMPLETE and holds a V1 tile, a teal user badge, a teal toolbox and a white document. The right reads REQUEST 2: COMPLETE and holds a V2 tile, a blue user badge, a blue toolbox and a white document. Both point inward at a central server stack. Below the server, a key struck through with a coral X sits above the words NO SESSION MEMORY in coral.](../diagrams/09-stateless-mcp.png)

**Module:** 2 — MCP capabilities
**Role in the course:** replacing handshake-era assumptions
**Layout:** two mirrored self-contained requests converging on one server, with a negation beneath

---

## At a glance

Two requests. Each one carries its own version, its own identity, its own tools, and its own payload. Both arrive at the same server. Underneath, a key crossed out in coral and the words **NO SESSION MEMORY**.

The composition is the argument: the two panels are deliberately drawn as **duplicates**. Everything the left request carries, the right request carries again. That duplication looks wasteful until you understand it is the point — nothing persists between them, so each must be complete on its own.

---

## What the diagram teaches

### 1. "Complete" is the word doing the work

Both headings say **COMPLETE**, not "request 1" and "request 2." That word is the claim.

A complete request is one that can be understood and served with no reference to anything that came before it. Everything needed to interpret it is inside it. If you deleted every prior interaction from the universe, this request would still mean exactly what it means.

The test is blunt and useful: **could this request be the first request the server has ever seen?** If the answer is no — if it refers to "the document we discussed" or relies on a mode set earlier or assumes a version negotiated at connection time — it is not complete, and it will fail in ways that are hard to reproduce.

### 2. The duplication is deliberate and it is the diagram's whole method

Look at what appears in both panels. A version tile. A user badge. A toolbox. A document. The same four categories, twice.

A less careful diagram would draw the shared things once, in the middle, and have both requests point at them. That would be a picture of a session. This one refuses to do that, and the refusal is the teaching: **there is no shared middle**. What the two requests have in common is that they each bring their own copy.

Note also that the two panels are not identical in detail. The left carries **V1** and is rendered in teal; the right carries **V2** and is rendered in blue. Different versions, in flight simultaneously, against the same server. That is only possible because neither request depends on a negotiated connection state.

### 3. Four things every request carries

The four objects in each panel map to four categories of thing that a stateful protocol would negotiate once and a stateless one must carry every time.

**Version.** The V1 and V2 tiles. Which revision of the protocol this request speaks. In a handshake model this is agreed at connection setup and then assumed. Here it rides on every request, which is why two different versions can be in flight at once.

**Identity.** The user badge. Who is asking. Not established at login and then remembered — asserted per request, and re-evaluated per request.

**Capabilities.** The toolbox. What is being invoked, described in full. The request does not refer to "the tool we set up earlier."

**Payload.** The document. The actual content of the request.

If your mental model is a connection that gets configured and then used, all four of these feel like overhead. If your mental model is independent deliveries, all four are just the address on the parcel.

### 4. The crossed-out key is a *session* key, not an auth key

The badge beneath the server shows a **key with a large coral ✗** through it. This is worth being precise about, because it is easy to misread as "no authentication."

It is the opposite. Authentication is present in every request — that is what the user badge in each panel is. What is absent is a **session key**: a token issued once at connection time that subsequent requests present as shorthand for "I am the connection you already know."

Stateless means every request re-establishes who is asking and what they may do. That is more work per request, and it buys you the properties in the next section.

### 5. What statelessness actually buys

The reason to accept the per-request overhead is that a stateless protocol survives things a stateful one does not.

**Any server can serve any request.** The two panels point at one server stack in the diagram, but nothing in either request depends on *which* server. Put ten behind a load balancer and the requests distribute freely.

**Restarts are invisible.** A server that restarts between request 1 and request 2 loses nothing, because it was holding nothing.

**Scaling is horizontal and trivial.** Add capacity by adding servers. No session affinity, no sticky routing, no shared session store, no distributed cache holding conversation state.

**Failures are isolated.** A request that fails takes nothing with it. There is no corrupted session to recover, no half-configured connection to reset.

**Version transitions are gradual.** The V1/V2 detail matters here. Old and new clients coexist without a coordinated cutover, because version travels with the request rather than being fixed at connection time.

### 6. Stateless protocol, stateful conversation

The most common objection is immediate: *agents obviously have memory — conversations refer backwards constantly.* Correct, and it does not conflict with anything here.

The state lives in the **client**, not the protocol. The agent maintains the conversation, decides what is relevant, and packs what the server needs into each request. The server never holds conversational context between calls.

That division is a feature. It means the thing that understands the conversation — the agent — owns it, and the thing that provides capabilities stays simple. It also means the client can be explicit about what it is sending, which is exactly what the context-minimisation gate later in the course requires:

![Five stages — MINIMIZE CONTEXT, ALLOWLIST AGENT, BIND TASK, VALIDATE ARTIFACT, LOCAL APPROVAL — with a funnel filtering a checklist and coral rejects dropping into a bin.](../diagrams/23-a2a-security-gates.png)

You can only minimise context that you control. A protocol that quietly accumulates session state on the server side gives you nothing to minimise.

There is a genuine exception, and the course handles it separately: work that legitimately takes minutes or hours needs an identity that outlives a single request. That is not session state — it is a durable task with an ID, covered in diagram 11.

---

## Case study — Aperture Analytics, the fleet that broke

Aperture provides a customer analytics platform. Their assistant answers questions about customer cohorts, retention, and campaign performance, backed by a capability server that queries their warehouse.

It ran on a single server instance for the first eight months. It worked well. Then it did not.

### The assumptions that had crept in

Nobody set out to build a stateful protocol. Three shortcuts accumulated, each reasonable in isolation.

**Version negotiated at connection.** The client and server agreed a protocol revision when the connection opened. Subsequent requests omitted it, because it had already been established. This saved a few bytes and felt tidy.

**Identity cached per connection.** The user was authenticated on connect. Their identity and permissions were held in memory against the connection and reused for every subsequent request. This avoided re-checking permissions on every call, which was measurably faster.

**Query context held server-side.** This was the significant one. Aperture's warehouse queries are expensive, and analysts often ask a series of related questions about the same cohort. The server started holding a "current cohort" against the connection, so follow-up questions could be answered without redefining it. An analyst could say "now break that down by region" and it worked.

All three were fine on one server.

### What happened at two

Growth forced a second instance behind a load balancer. The team expected a straightforward capacity change. What they got:

**Follow-up questions failed unpredictably.** "Now break that down by region" hit whichever instance the load balancer chose. Half the time it was the instance holding the cohort; half the time it was the other one, which had no idea what "that" referred to. The assistant would either error or — worse — silently answer about a *different* cohort held for a different analyst.

That second behaviour was the serious one. Two analysts working simultaneously could receive each other's cohort context. It was caught in week one by an analyst who noticed the row counts made no sense, but the potential for one customer's data to be described to another was real.

**Deploys became outages.** Every deploy dropped connections. Analysts lost their query context mid-session and had to redefine cohorts from scratch. The team started deploying only at 6am, which slowed everything down.

**Version handling broke during rollout.** During a staged rollout, some instances spoke the new revision and some the old. A client that negotiated the new version on connect could be routed to an old instance for its next request, which had no record of the negotiation and assumed the default. Requests were interpreted under the wrong revision, mostly harmlessly, occasionally not.

### The rebuild

They made every request complete. In practice, four changes.

**Version on every request.** Each request carries the protocol revision it is written against. During the next rollout, mixed-version traffic was a non-event — every request declared what it was and every instance could serve either.

**Identity on every request.** Authentication and permission evaluation moved to per-request. This cost about four milliseconds per call, which they measured and accepted. It also fixed a latent bug: permission changes had previously not taken effect until the analyst reconnected, so a revoked analyst kept their access for as long as their session lasted — in one case, most of a working day.

**Cohort definitions moved into the client.** This was the real work. The agent now holds the conversation's state, and when an analyst says "break that down by region," the client resolves what "that" means and sends a complete cohort definition with the request. The server receives a fully-specified query with no reference to anything prior.

The queries got bigger. A cohort definition can run to a few kilobytes. Nobody noticed the difference.

**Expensive results cached by content, not by connection.** They kept the performance benefit that the server-side context was originally for, but keyed it on a hash of the query definition rather than on the connection. Two analysts asking for the same cohort now share a cache entry — which is better than the old behaviour, where each connection computed it separately.

### What it enabled

They went from two instances to eleven over the following year with no further work on this. Deploys became routine and moved back into business hours. The cross-analyst context leak became structurally impossible rather than fixed-by-patching.

The change that surprised them was the permission one. Making identity per-request meant access revocations took effect immediately. Their security team had raised this as a finding twice and it had been deprioritised twice; it was resolved as a side effect of making requests complete.

### The part that stayed stateful, correctly

Aperture has one genuinely long-running operation: a cohort backfill that recomputes historical metrics and takes between four and forty minutes.

They did not try to make that a single request. It became a durable task with an ID — start it, get an identifier back, check on it, collect the result:

![Four numbered panels — START TASK, TASK ID, PROGRESS at 68%, RESULT — with a dashed timeline underneath looping from the progress stage back to the task ID stage.](../diagrams/11-durable-mcp-task.png)

The distinction the team articulated afterwards is worth repeating: **session state is the server remembering you; a task is the server remembering the work.** The first is an assumption you cannot verify and cannot scale. The second is an object with an identity that any instance can look up.

---

## Composition

Two large mirrored platforms face each other across the frame, each drawn as a wide arrow-shaped slab angled inward.

The left platform is headed **REQUEST 1: COMPLETE** in cyan on a blue title bar. Inside its translucent panel sit four objects: a dark tile reading **V1**, a teal user badge, a teal toolbox with plug/gear/database tiles, and a white document.

The right platform is headed **REQUEST 2: COMPLETE** and holds the mirrored equivalents: a **V2** tile, a blue user badge, a blue toolbox, and a white document.

Both platforms point inward with cyan arrows at a single **blue server stack** in the centre. Below the server, a short dashed line drops to a circular badge containing a **key struck through with a large coral ✗**, and beneath that, in coral capitals: **NO SESSION MEMORY**.

## Element by element

**The two headings**
Both read **COMPLETE**. The word is the diagram's thesis — each request is self-sufficient.

**V1 and V2 tiles**
Different protocol revisions in flight simultaneously against the same server. Only possible because version travels per request rather than being negotiated at connection time.

**The user badges**
Identity, asserted in each request rather than established once. Teal on the left, blue on the right — different callers, or the same caller re-asserting.

**The toolboxes**
The capability being invoked, described in full. Note that both requests carry one; neither refers to a tool configured earlier.

**The white documents**
The payload.

**The central server stack**
One server, serving both. Nothing about either request depends on which instance receives it.

**The struck-through key**
A *session* key, not an auth key. Authentication is present in both panels as the user badge. What is absent is a token standing in for "the connection you already know."

## Colour and flow semantics

- **Cyan arrows** carry both requests inward to the server.
- **Coral** appears twice and only in the negation: the ✗ through the key and the words **NO SESSION MEMORY**. In a diagram about what is absent, coral marks the absence.
- The left/right teal/blue split distinguishes the two requests without implying that either is primary.
- The mirrored symmetry is the composition's argument — two independent, equivalent, self-contained deliveries.

## How to present it

**Ask what is duplicated and why.** Put the image up and let the room notice that both panels contain the same four things. Then ask why the diagram did not draw the shared items once in the middle. The answer — because there is no shared middle — is the whole lesson, and it lands better as a discovery than as a statement.

**Apply the first-request test to their own system.** Ask: could any single request your client sends be the first request the server has ever seen? Most rooms find at least one that could not. The usual culprits are a mode set earlier, a version agreed at connect, or a reference to something the server is assumed to still be holding.

**Handle the memory objection immediately.** Someone will say agents obviously have memory. Agree, then draw the distinction: the state is in the client, the protocol is stateless. The agent owns the conversation; the server owns capabilities. Ask which side of that line each piece of their state currently sits on.

**Point at V1 and V2 and ask how that is possible.** This detail is easy to miss and it is the cleanest illustration of why per-request version matters. Two protocol revisions, same server, same moment. Then ask what a staged rollout looks like under a connection-negotiated version. Aperture's mixed-version incident is a good story to tell here.

**Name the four properties you get.** Any server serves any request; restarts are invisible; scaling is horizontal; failures are isolated. Then ask which of those they currently have. Teams running a single instance often have none and do not know it, because nothing has forced the issue yet.

**Be precise about the key.** Ask what the crossed-out key is. Someone will say "no auth." Correct them by pointing at the user badges: authentication is in every request. What is gone is the shorthand token. That distinction is the difference between stateless and unauthenticated, and conflating them is a genuinely dangerous misreading.

**Close with the legitimate exception.** Long-running work needs an identity that outlives a request, and that is a task, not a session. The line worth giving them: *session state is the server remembering you; a task is the server remembering the work.*

**Timing.** Fifteen minutes. Twenty-five if the room has a scaling story of their own, which is usually the most valuable version of this session.

---

## Lab and checkpoint

**Lab:** Take one stateful endpoint in a system you know. Rewrite it as a stateless MCP request, identifying what state currently lives in the server and where that state must move: into the request, into a task, or out of the protocol entirely. Write the new request shape and the server-restart test that would prove no session was lost.

**Checkpoint:** What is the difference between stateless and unauthenticated?

**Answer:** Stateless means the server does not remember the client between requests; every request carries enough context to be handled on its own. Unauthenticated means no identity is checked. A stateless request can still be authenticated; the user badge is in every request, but there is no session key.

## Glossary

- **Authentication** — verifying who the caller is in every request.
- **Crossed-out key** — the symbol that no session key is carried or stored between requests.
- **Horizontal scaling** — adding identical server instances without changing request handling.
- **Request context** — all the state needed to handle one request, carried in the request itself.
- **Session** — server-stored state that remembers a client across multiple requests.
- **Stateless** — the server treats each request independently, with no memory of previous requests.
- **Task** — a long-running work identity that outlives a single request.

## Sources

- MCP 2026-07-28 stateless request model
- JSON-RPC 2.0 and per-request meta patterns
- Stateless service design and horizontal scaling guidance
