# Diagram 47 — A Stateless MCP Request

![A left-to-right journey on dark navy. CLIENT shows a person at a laptop. An open envelope holds four white cards labelled METHOD showing POST, NAME showing a person icon, REQUEST ID showing a hash, and AUTH SCOPE showing a shield. A cyan arrow leads to SERVER, then POLICY showing a teal shield with a check, then TOOL showing a toolbox with a wrench and gear. A coral arrow drops from POLICY to a red octagon labelled DENIED. A teal return path runs along the bottom through RESULT back to the client.](../diagrams/47-stateless-mcp-request.png)

**Module:** Modern MCP
**Role in the course:** the request shape that makes everything else scale
**Layout:** a self-contained envelope crossing four stages, with a denial branch and a return path

---

## At a glance

One request, drawn as an **open envelope containing four cards** — **METHOD**, **NAME**, **REQUEST ID**, **AUTH SCOPE** — travelling through a server, a policy gate, and a tool, with a result returning underneath.

The envelope is the diagram. Everything the request needs to be understood is inside it. Nothing is remembered from a previous request, nothing is negotiated at connection time, and nothing depends on which server instance receives it.

That single property is what makes every operational capability in the rest of this volume possible: horizontal scaling, gateway routing, per-request authorisation, and traces that survive restarts.

---

## What the diagram teaches

### 1. Four cards, and each removes a dependency on the past

**METHOD** — the card reads **POST**, with the operation category on it. What kind of thing this is. A gateway can route on it, rate-limit on it, and log it without parsing anything else.

**NAME** — a person icon. Which specific capability is being invoked. Method plus name together identify the operation completely, at the envelope level.

**REQUEST ID** — a hash symbol. This request's own identity. It is what makes the request traceable across every component it touches, and what makes a retry recognisable as a repeat rather than a new request.

**AUTH SCOPE** — a shield. Not just who is asking, but **what they are permitted to do on this request**. Carried per request, evaluated per request.

Take any one of these out and the request becomes dependent on something the server would have to remember. Remove the auth scope and you need a session that holds permissions. Remove the request ID and you cannot correlate a retry. Remove method and name from the envelope and every gateway decision requires parsing the body.

### 2. The envelope is open, and that is deliberate

The cards sit in an envelope drawn **open**, with all four visible.

A closed envelope would say "the request contains these things." An open one says **the important parts are readable without opening the payload**. That is the operational property: infrastructure between the client and the tool — gateways, proxies, rate limiters, tracers — can do their jobs from the envelope alone.

The consequence is worth stating plainly. If your routing needs the body, your gateway has to deserialise attacker-controlled input before it has authorised anything. Keeping method, name, identity and scope on the outside means the cheap decisions happen before the expensive parsing.

### 3. Policy sits between the server and the tool, not before the server

Look at the order: **SERVER → POLICY → TOOL**.

The request reaches a server first. The server then applies policy, and only a request that passes reaches the tool. The coral **DENIED** branch hangs off policy and nothing else.

This placement says that authorisation is a decision made **with knowledge of what is being asked and of the current state**, not a bouncer at the door. A gateway can reject obviously malformed or unauthenticated traffic, but the question "may this principal invoke this capability against this resource right now" needs the server's context.

Note also that the tool is the last stage before the result. Nothing between policy and tool can add permissions. The gate is the last word.

### 4. There is exactly one denial path and it is drawn at full weight

The coral arrow to the red octagonal **DENIED** platform is the only failure route in the picture.

Its presence in a diagram that is otherwise about request shape is a reminder that a well-formed request is not an authorised one. The envelope can be perfect and the answer can still be no.

### 5. The result returns along the bottom, and it returns to the client

A teal path runs from the tool, along the base of the frame, through a white **RESULT** card with a green check, and up into the client.

Two things follow.

The result is drawn as **its own object on its own platform** rather than as an arrow. A result is a thing that exists, can be recorded, and can be returned again — which matters when the same request ID arrives twice.

And the path returns to the client, not to the server that handled it. The client is the party that holds continuity; the server holds none.

### 6. Statelessness is what enables the fleet

The diagram shows one server. The reason the request has to be self-contained is that in production there is never one server.

If every request carries its own method, name, identity, scope and ID, then any instance can serve any request. Instances can be added, removed, restarted, deployed and rebalanced without any request noticing. A gateway can round-robin freely.

The moment a request depends on something established earlier — a negotiated version, a cached identity, a session-held context — you need affinity, and affinity is the thing that makes fleets fragile.

It is also what allows a gateway to exist at all:

![A gateway diagram showing MCP-METHOD and MCP-NAME headers entering a GATEWAY with ROUTE, AUTHORIZE, RATE LIMIT and TRACE, fanning out to tool, resource and prompt servers, with a coral HEADER BODY MISMATCH path and a cache return carrying TTL MS and CACHE SCOPE.](../diagrams/50-mcp-routing-and-cache.png)

Every function in that gateway reads the envelope's outer cards. None of it is possible if the identifying information is buried in a body that only the destination server can interpret.

---

## Case study — Lindwall Systems, the fleet that could not grow

Lindwall provides field-service management software to about 400 industrial maintenance companies. Their platform exposes an MCP layer that internal assistants and customer integrations call — around 40 capabilities covering work orders, asset records, parts, and engineer scheduling.

It ran on three server instances for eighteen months. Attempting to grow to twelve took four months and a rewrite of how requests were shaped.

### What had accumulated

Nobody set out to build a stateful protocol. Three shortcuts arrived independently.

**Auth was resolved once per connection.** On connect, the server verified the caller's token, resolved their principal and permissions, and held them in memory against the connection. Requests then carried only an operation name. This was measurably faster and it felt tidy.

**The capability catalogue was negotiated at connect.** The client asked what was available, the server answered once, and both sides assumed the answer held for the connection's life.

**A "current tenant" was set by a separate call.** Integrations serving multiple customer organisations would set the active tenant and then issue a sequence of requests against it. Convenient, and it meant the tenant was not on the request.

### What happened at scale

**Cross-tenant leakage, nearly.** The third shortcut was the dangerous one. When they added instances behind a load balancer, a `set_tenant` call would land on one instance and the subsequent requests on another. The other instance had no tenant set, and the default was the caller's *primary* tenant.

For most integrations this was harmless because their primary tenant was the one they meant. For eleven partner integrations serving multiple customers, it meant a request intended for customer B could execute against customer A.

They caught it in staging, during load testing, because a test integration returned work orders from the wrong organisation. Had it reached production it would have been a serious data incident.

**Permission revocation was ineffective.** Because permissions were resolved at connect, revoking a caller's access did nothing until they reconnected. Long-lived integration connections ran for days. A partner whose contract ended retained working access for most of a week.

**Deploys dropped work.** Every deploy terminated connections and everything they held.

### The rebuild

They made every request carry the four cards.

**Method and name on the envelope.** Their gateway could now route, rate-limit and log without deserialising bodies. This turned out to matter independently: they had been parsing request bodies at the gateway to decide routing, which meant unauthenticated callers could reach their parser.

**Request ID on every request.** Generated by the client, carried through every component, recorded in every log line and every audit entry. This is what made the observability work later in the volume possible at all.

**Auth scope per request.** Token verified and permissions evaluated on every call. Cost: about 3ms. Revocation became immediate, which closed a finding their security team had raised twice.

**Tenant on the request, always.** `set_tenant` was deleted. Every request names the tenant it operates against, and the auth scope is evaluated against that specific tenant. The cross-tenant path became structurally impossible rather than defended against.

### What it enabled

They went from three instances to twelve in a fortnight, and to twenty-eight over the following year, with no further work on request shape.

More importantly, three capabilities that had been blocked became straightforward:

- **A gateway** that routes on method and name, applies per-caller rate limits, and traces — none of which was possible when the identifying information was in the body.
- **Blue-green deploys**, because no instance held anything worth preserving.
- **End-to-end tracing**, because the request ID was already on every call.

Their platform lead's summary: *we thought statelessness was a purity argument. It was the prerequisite for everything on our roadmap.*

### The measurement that convinced their finance team

Per-request auth cost 3ms. Across their traffic that was about £400/month of additional compute.

The connection-affinity load balancer they were able to delete cost £2,100/month, and the engineer-days spent on session-related incidents in the preceding year came to roughly nine weeks.

---

## Composition

A left-to-right journey across the upper two-thirds of the frame, with a return path along the base.

**CLIENT → [envelope] → SERVER → POLICY → TOOL**, connected by cyan arrows. From **POLICY**, a coral arrow drops to **DENIED**. From **TOOL**, a teal line runs down and left through **RESULT** and up into **CLIENT**.

## Element by element

**CLIENT**
A person seated at a laptop showing `{ }` braces on screen, on a blue platform.

**The envelope and its four cards**
A large open white envelope with a teal circular **send** button on its front. Standing inside it, four white cards, each labelled above with a dashed leader line:
- **METHOD** — a teal **POST** tile.
- **NAME** — a teal person icon.
- **REQUEST ID** — a teal **#** hash.
- **AUTH SCOPE** — a teal shield.

**SERVER**
A blue server tower with indicator lights and a teal wireframe globe on its face.

**POLICY**
A **teal shield with a white check** on a blue platform. The only stage with a denial branch.

**TOOL**
A blue toolbox with a grey **wrench** and a teal **gear** rising from it.

**DENIED**
A **red octagon with a white ✗** on a blue platform, reached by the single coral arrow.

**RESULT**
A white card with a **teal check disc** and text lines, sitting on its own platform on the return path.

## Colour and flow semantics

- **Cyan arrows** carry the request forward through all four stages.
- **Teal** marks the working machinery — the send button, the card icons, the policy shield, the gear, the result check — and the return path.
- **Coral** appears once, on the denial branch.
- The **open envelope** is the composition's argument: the identifying parts of the request are readable from outside.
- **RESULT is drawn as an object on a platform**, not as an arrow, marking it as something that exists and can be returned again.

## How to present it

**Ask what a server has to remember between requests.** The correct answer is nothing, and most rooms will name at least two things their own servers hold.

**Point at the four cards and remove them one at a time.** Take away auth scope — now you need a session holding permissions. Take away request ID — now a retry is indistinguishable from a new request. Take away method and name — now your gateway parses bodies to route. Each removal reintroduces a dependency on the past.

**Ask why the envelope is drawn open.** The identifying parts are outside the payload, so infrastructure can act on them without deserialising. Then ask what their gateway currently needs in order to route. If the answer involves the body, they are parsing untrusted input before authorising it.

**Ask why policy sits after the server rather than before it.** Because the question is not "is this caller known" but "may this principal do this thing to this resource now," and that needs context a door cannot have.

**Tell the Lindwall tenant story.** `set_tenant` on one instance, subsequent requests on another, default falling back to the primary tenant. Caught in load testing. Ask the room what state their own requests depend on that is not in the request.

**Use the revocation angle with security-minded rooms.** Per-connection auth means revocation takes effect at next reconnect, which for long-lived integrations can be days. Per-request auth makes it immediate. This often lands harder than the scaling argument.

**Give them the cost comparison.** 3ms per request versus a session-affinity load balancer and nine engineer-weeks of incidents. Statelessness is usually cheaper, and it is worth having the number.

**Timing.** Twenty minutes. Thirty if you audit what the room's own requests depend on, which reliably finds something.

---

## Lab and checkpoint

**Lab:** Take one real API request your server accepts and list every piece of state it depends on that is not inside the request itself. For each, write whether it can be moved into the request, turned into a per-request claim, or removed. Then design the stateless version and the test that would fail if a later request accidentally relied on server memory.

**Checkpoint:** Why must policy sit after the server rather than at the door?

**Answer:** Because the policy question is not just "who is this caller?" but "may this principal do this thing to this resource right now?" That needs request context, not just identity. A door or gateway can authenticate, but the authorisation needs the full request.

## Glossary

- **Auth scope** — the permissions carried with the request, outside the body.
- **Denial** — the refusal branch when the request fails policy.
- **Method and name** — the routing information outside the envelope.
- **Per-request auth** — authentication and authorisation that happen for every request, not just at connection time.
- **Policy shield** — the gate that decides whether the request is allowed.
- **Request ID** — the identifier that lets the server recognise a retry.
- **Result** — the returned object, produced without depending on server state.
- **Stateless** — a server that handles each request using only what is in the request.

## Sources

- Stateless API design and horizontal scaling
- Per-request authorisation and revocation patterns
- MCP request context and policy enforcement
