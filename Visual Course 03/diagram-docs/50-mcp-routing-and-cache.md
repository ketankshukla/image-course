# Diagram 50 — Routing, Caching, and Gateways

![A gateway diagram on dark navy. MCP REQUEST on the left shows two cards, MCP-METHOD with a code glyph and MCP-NAME with a cube. A cyan arrow leads to GATEWAY, a wide platform holding four tiles — ROUTE with a signpost, AUTHORIZE with a padlock, RATE LIMIT with a gauge, TRACE with a magnifier. Cyan arrows fan right to TOOL SERVER, RESOURCE SERVER and PROMPT SERVER. A dashed coral path leads from the gateway to a red HEADER BODY MISMATCH card. Along the bottom, dashed cyan arrows carry CACHE SCOPE, TTL MS and LIST RESPONSE leftward into CLIENT CACHE.](../diagrams/50-mcp-routing-and-cache.png)

**Module:** Modern MCP
**Role in the course:** the infrastructure layer between clients and servers
**Layout:** headers into a four-function gateway, fanning to three server types, with a cache return path

---

## At a glance

Two headers — **MCP-METHOD** and **MCP-NAME** — let a gateway do four things before anything is parsed: **ROUTE, AUTHORIZE, RATE LIMIT, TRACE**. The request then reaches one of three server types. Along the bottom, list responses travel back carrying **CACHE SCOPE** and **TTL MS** into a client cache.

Two independent ideas share the frame, and they are both about **not doing work you do not have to do**. Headers let infrastructure act without deserialising. Cache metadata lets clients avoid re-asking. The coral **HEADER BODY MISMATCH** path is what stops the first idea becoming a security hole.

---

## What the diagram teaches

### 1. Two headers, and they are outside the body on purpose

**MCP-METHOD** carries the operation category. **MCP-NAME** carries the specific capability.

Together they identify the request completely — and they sit in headers, where a gateway can read them without touching the payload.

Everything in the gateway platform depends on that. Routing to the right server type, deciding whether this caller may invoke this capability, applying the right rate budget, and starting a trace span, all happen from two string values.

The alternative is a gateway that deserialises attacker-controlled JSON before it has authorised anything. That is a large amount of parser surface exposed to unauthenticated callers, and it is the arrangement this design exists to avoid.

### 2. Four gateway functions, and their order matters

**ROUTE** — a signpost. Which server type serves this. A dispatch decision, not a security one.

**AUTHORIZE** — a padlock with a check. May this caller invoke this capability at all? A coarse check at the edge, before any server is involved.

**RATE LIMIT** — a gauge. Is this caller within budget? Applied per method and per name, so an expensive capability can carry a tighter budget than a cheap one.

**TRACE** — a magnifier. Start the span. Everything downstream inherits it.

Authorize before rate limit means an unauthorised caller cannot consume a legitimate caller's budget. Trace last means the span covers the work rather than the gate.

Note what the gateway does **not** do: it does not make the fine-grained authorisation decision. That needs resource-level context the gateway does not have, and it belongs at the server's policy gate.

![A self-contained request envelope carrying METHOD, NAME, REQUEST ID and AUTH SCOPE, travelling through a server, a policy gate and a tool with a coral denial branch.](../diagrams/47-stateless-mcp-request.png)

The gateway is a coarse filter; the policy stage in that diagram is the fine one. Two gates, different questions.

### 3. Header body mismatch is a security control, not a validation nicety

The **coral dashed path** from the gateway leads to a red-flagged card reading **HEADER BODY MISMATCH**.

This is the attack the header design invites, and the control that closes it.

If the gateway routes and authorises on `MCP-NAME: get_refund_status`, and the body actually invokes `issue_refund`, then every gateway decision was made about a different operation than the one that will execute. The caller has authorised themselves for a read and delivered a write.

The control is straightforward and non-negotiable: **the server must verify that the headers match the body, and reject the request if they do not.** Not correct one from the other — reject.

The mismatch path being dashed and coral, leaving the gateway rather than continuing to a server, is the right rendering: this request does not proceed.

### 4. Three server types, and the split is the primitive split

The fan-out goes to **TOOL SERVER**, **RESOURCE SERVER**, and **PROMPT SERVER** — the three MCP primitives, each with its own backend.

That separation has real operational consequences. The three have completely different profiles: tools mutate and need tight rate limits; resources are read-heavy, cacheable, and benefit from being served close to the caller; prompts are small, change rarely, and are almost pure cache.

Splitting them means each can be scaled, cached, secured and rate-limited according to what it actually is, rather than everything inheriting the strictest and most expensive configuration.

### 5. The cache path is the diagram's second idea and it runs backwards

Along the bottom, **dashed cyan arrows** carry three cards leftward into **CLIENT CACHE**: **CACHE SCOPE**, then **TTL MS**, then **LIST RESPONSE**.

The direction is right to left — this is the response coming back — and the ordering tells you how to read it. The list response arrives **accompanied by** metadata that says how long it may be held and who it applies to.

**TTL MS** — how long this remains valid. In milliseconds, which is unusually precise and appropriate: catalogue freshness matters and hour-granularity is too coarse.

**CACHE SCOPE** — *who* this cached answer is valid for. This is the field that prevents the worst caching bug in this domain.

### 6. Cache scope is a security field

A capability catalogue is **per caller**. Two users of the same server see different tool lists because their permissions differ.

A client that caches a list response and serves it to a different principal has just told that principal about capabilities they cannot invoke — and, worse, may cause the client to plan around tools it will be refused.

**CACHE SCOPE** is the server saying who this answer belongs to. A response scoped to a principal must not be reused across principals; a response scoped to the server as a whole may be shared.

Treating TTL as the only cache dimension is the mistake. Freshness and audience are separate questions.

---

## Case study — Ravensworth Health Group, the catalogue that leaked capabilities

Ravensworth runs a network of private clinics. Their MCP gateway fronts about 60 capabilities used by clinical staff assistants, administrative tooling, and two partner integrations.

They introduced a gateway to solve a real problem — 60 capabilities across four backend services, with authorisation logic duplicated in each — and introduced two bugs in the process.

### What the gateway fixed

Before it, every backend service implemented its own authentication, its own rate limiting, and its own logging format. Adding a capability meant touching auth code, and the four implementations had drifted: one accepted a token format the others had deprecated.

Headers plus a gateway consolidated all four functions into one place. Adding a capability became a registration rather than an implementation.

Their gateway routes on `MCP-METHOD` and `MCP-NAME`, applies a coarse per-caller capability allowlist, rate-limits by name (their `search_patient_records` capability carries a far tighter budget than `get_appointment`), and starts the trace span.

### Bug one — the mismatch nobody had considered

Found by a penetration tester, not by the team.

The tester held a token authorised for read capabilities only. They sent a request with `MCP-NAME: get_appointment` in the header and a body invoking `cancel_appointment`.

The gateway routed it, authorised it against the header value, applied the read-capability rate limit, and passed it to the appointments service. The service parsed the body and cancelled the appointment.

Nothing had verified that the header described the body. Every gateway control had been correctly applied — to a different operation than the one that ran.

**The fix.** Each server now verifies that the incoming headers match the operation in the body, and rejects mismatches outright with a specific error. Not correcting the header, not preferring the body — rejecting.

They also added a metric on mismatch rejections. In normal operation it is zero; a non-zero value is either a client bug or a probe, and both need attention. It has fired twice in eighteen months, both times a client bug during a refactor.

### Bug two — the shared catalogue cache

Their client library cached list responses to avoid re-fetching the catalogue on every session. Sensible, and it cut catalogue traffic by about 90%.

It cached them **by server URL**.

Ravensworth's capability catalogue is per role. A consultant sees capabilities that a receptionist does not — including `view_clinical_notes` and `amend_diagnosis`. The cache key did not include the principal.

The observed symptom was confusing: receptionists' assistants occasionally proposed actions they could not perform, and were refused by the policy gate. No data leaked — the fine-grained gate at each server held — but the assistant was telling receptionists that clinical capabilities existed.

For a health provider, a receptionist's tool discovering the existence of `amend_diagnosis` was a finding in its own right, regardless of whether it could be invoked.

**The fix.** Their servers now return **CACHE SCOPE** on every list response, and the client library keys the cache on scope. Principal-scoped responses are cached per principal; the small number of genuinely server-wide responses are shared.

They set **TTL MS** deliberately per response type: tool catalogues at 300,000ms (5 minutes), resource catalogues at 900,000ms, prompt catalogues at 3,600,000ms. Prompts change rarely; tools change when permissions change, and five minutes was their tolerance for a revoked capability remaining visible.

### The freshness incident that set the TTL

During an early trial they had a 30-minute tool-catalogue TTL. A clinician's access was revoked following a role change, and their assistant continued proposing clinical capabilities for the remainder of the cached window.

The capabilities were correctly refused at the policy gate every time. But the assistant looked broken, the clinician did not understand why, and it generated a support escalation.

They shortened the TTL and added invalidation: any capability refusal triggers a catalogue re-fetch before the next plan. Refusal is a strong signal that your cached picture is wrong.

### Results

- **Auth implementations:** four, drifted, to one.
- **Catalogue traffic:** ~90% reduction retained after the scope fix.
- **Time to add a capability:** roughly two days to under an hour.
- **Mismatch rejections:** two in eighteen months, both caught as client bugs before release.

### The rule in their client library documentation

*A cached list is valid for a duration and for an audience. If you only key on the URL, you have got half of it.*

---

## Composition

A left-to-right flow with a fan-out on the right and a return path along the base.

**MCP REQUEST → GATEWAY → { TOOL SERVER, RESOURCE SERVER, PROMPT SERVER }**, connected by cyan arrows. A **dashed coral path** leaves the gateway and leads to the **HEADER BODY MISMATCH** card, which continues dashed to the prompt-server area.

Along the bottom, **dashed cyan arrows** run right to left through **CACHE SCOPE → TTL MS → LIST RESPONSE → CLIENT CACHE**.

## Element by element

**MCP REQUEST**
A dark tile with a teal person icon, beside two white cards: one with a teal `</>` tile reading **MCP-METHOD**, one with a teal cube tile reading **MCP-NAME**.

**GATEWAY**
A wide blue platform inside a thin outlined boundary, holding four dark tiles on small plinths: a **teal signpost** — **ROUTE**; a **teal padlock with a check** — **AUTHORIZE**; a **teal gauge** — **RATE LIMIT**; a **teal magnifying glass** — **TRACE**.

**TOOL SERVER / RESOURCE SERVER / PROMPT SERVER**
Three blue server stacks, each paired with a white card carrying a distinguishing icon — a **wrench**, a **database**, and a **message bubble** respectively.

**HEADER BODY MISMATCH**
A **red rounded warning tile** with a white exclamation, attached to a white card bearing the label. Reached and left by dashed coral lines.

**The cache path**
Three white cards, right to left: a teal layers icon and **CACHE SCOPE**; a teal clock and **TTL MS**; a teal list icon and **LIST RESPONSE**. Feeding **CLIENT CACHE** — a teal database stack with a dark **download** tile.

## Colour and flow semantics

- **Cyan solid arrows** carry the request into and out of the gateway.
- **Dashed cyan** carries the response and its cache metadata back to the client — dashed because it is a return path.
- **Coral dashed** carries the mismatch rejection, leaving the flow entirely.
- **Teal** marks every gateway function icon and every metadata card icon.
- The **gateway's outlined boundary** groups the four functions as one layer rather than four stages.

## How to present it

**Ask what a gateway needs in order to route.** If the answer involves the body, ask what that means — deserialising attacker-controlled input before authorising it. Then point at the two headers.

**Walk the four functions and ask about ordering.** Authorize before rate limit, so an unauthorised caller cannot eat a legitimate one's budget. Then ask what the gateway deliberately does *not* do — the fine-grained, resource-level decision, which needs context it lacks.

**Spend real time on the mismatch path.** Ask the room what happens if the header says `get_refund_status` and the body says `issue_refund`. Every gateway control was correctly applied to the wrong operation. Then tell the Ravensworth pen-test finding.

**Ask what the correct response to a mismatch is.** Some will say prefer the body, some the header. The answer is reject. Then suggest the metric: mismatch rejections should be zero, and a non-zero value is a bug or a probe.

**Ask why three server types rather than one.** Different profiles — tools mutate, resources are read-heavy and cacheable, prompts barely change. One backend means everything inherits the strictest configuration.

**Point at the two cache cards and ask which one people forget.** TTL is intuitive. **CACHE SCOPE** is not, and it is a security field. Then tell the receptionist story: no data leaked, but the assistant told a receptionist that `amend_diagnosis` existed.

**Ask how they would invalidate.** TTL alone is not enough. Ravensworth's rule — a capability refusal triggers a catalogue re-fetch — is the useful addition, because a refusal is strong evidence your cached picture is stale.

**Timing.** Twenty-five minutes. Thirty-five if you work through TTL and scope values for the room's own catalogue types.

---

## Lab and checkpoint

**Lab:** Design a gateway for one of your MCP-style servers. Define the four gateway functions — route, authorise, rate limit, trace — and their order. Then write a request whose header and body disagree and the exact response the gateway should return. Define the cache scope for one catalogue and the TTL and invalidation rule.

**Checkpoint:** Why should a header/body mismatch be rejected rather than resolved?

**Answer:** Because there is no safe way to decide which to trust. Preferring the body means the header can be forged to bypass routing and authorisation. Preferring the header means an attacker can smuggle a different operation in the body. Rejecting protects the gateway's integrity.

## Glossary

- **Authorise** — the gateway function that checks the caller may use the requested operation.
- **Cache scope** — the party or context a cached value belongs to, not just how long it lives.
- **Gateway** — the boundary that routes, authorises, rate-limits, and traces every request.
- **Header/body mismatch** — a request where the header names one operation and the body names another.
- **Rate limit** — the gateway function that protects the server from excessive volume.
- **Route** — the gateway function that directs the request to the correct server type.
- **Trace** — the gateway function that propagates the trace identifier.
- **TTL** — the time-to-live for a cached response.

## Sources

- MCP gateway and capability routing
- Header/body validation and gateway security
- Cache scope, TTL, and invalidation patterns
