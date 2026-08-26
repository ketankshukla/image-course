# Diagram 12 — MCP Security Gates

![Five upright gate panels on tiered pedestals across dark navy, connected by teal arrows — AUTHENTICATE showing an ID badge on a lanyard, AUTHORIZE showing a green shield with a checklist of two ticks and a red warning, VALIDATE showing a code window with braces and a green check, RATE LIMIT showing a speedometer gauge, and AUDIT showing a printer issuing a checked slip.](../diagrams/12-mcp-security-gates.png)

**Module:** 2 — MCP capabilities
**Role in the course:** production API security review
**Layout:** five sequential gates on raised pedestals

---

## At a glance

Five gates, in order: **AUTHENTICATE → AUTHORIZE → VALIDATE → RATE LIMIT → AUDIT**.

The content is not the list — most engineers can produce that list. The content is the **ordering**, and the fact that each gate is drawn as a raised, upright barrier that a request must pass through rather than a checkbox on a review form. Get the order wrong and you have built five controls that do less than five controls' worth of work.

---

## What the diagram teaches

### 1. The order is the lesson

Each gate depends on the one before it. Reversing any adjacent pair either breaks the control or wastes it.

**Authenticate before authorize.** You cannot decide what someone may do until you know who they are. Obvious stated plainly, and violated constantly by systems that check a scope or an API key's permissions without ever establishing which principal is behind it.

**Authorize before validate.** Parsing and validating a payload for a caller who is not permitted to invoke the method at all is wasted work — and worse, it is *attacker-controlled* wasted work. Your validation layer is a parser, parsers are attack surface, and exposing it to unauthorised callers is exactly the wrong exposure. This is the pair most often reversed, because validation frameworks tend to sit in middleware that runs early.

**Validate before rate limit.** Counting malformed requests against a legitimate caller's budget lets a broken client exhaust its own quota with garbage. Rate limits should meter real work, not noise.

**Everything before audit — and audit regardless.** Audit is last because it records the outcome, and it records the outcome *whatever the outcome was*. A request refused at gate 1 must produce an audit entry as surely as one that passes all five.

### 2. Audit is not the same as logging, and it is a gate

Audit sits on a pedestal, in a gate frame, exactly like the four controls before it. That framing is deliberate: it is a **required stage of processing**, not a side effect that happens if the logging library is configured.

The distinction from ordinary logging is worth stating:

- **Logs are for you.** Debugging, performance, diagnosis. Sampled, rotated, best-effort.
- **Audit is for someone else.** A person, later, establishing what happened and who caused it. Complete, retained, tamper-evident.

The panel shows a printer producing a physical slip with a green check. Not a stream of text — a **discrete record per event**, produced deliberately.

The design consequence: if the audit write fails, the request has failed. Treating audit as fire-and-forget means the one time it matters, you discover the record is missing.

### 3. Refusals are the most important thing audit captures

A system that only records successful calls cannot answer the question that actually gets asked during an incident: *what did they try?*

Denied requests at gates 1 through 4 are the highest-signal events in the whole pipeline. A caller repeatedly failing authorization on a method they are not entitled to is either a misconfigured client or an attacker probing. Both need to be visible, and neither shows up if audit only fires on success.

The order of the gates makes this cheap to implement correctly: because audit is last and unconditional, every path through the pipeline — pass or refuse, at any gate — arrives there. There is no separate error path that has to remember to log.

### 4. Authorize is per-item, and the checklist says so

Look carefully at the second panel. Beside the shield is a strip showing **two green ticks and one red warning dot**.

This is the same claim the safe side-effect diagram makes at its authorize stage: authorization is a verdict on each element of a request, not a gate that opens or closes.

![Four numbered panels — CONFIRM, AUTHORIZE, IDEMPOTENCY KEY, CHANGE + RECEIPT — with a SAFE RETRY loop passing through a rejected duplicate write.](../diagrams/02-safe-side-effect.png)

The reason it recurs is that agent requests arrive as batches more often than human requests do. An agent proposes a plan touching six records; three are permitted, two are not, one requires elevation. A boolean gate handles this by refusing everything or permitting everything, and both answers are wrong.

### 5. Rate limiting is a correctness control, not just a cost control

The fourth gate is usually justified on economics: stop one caller consuming the capacity. That is true and it is the smaller half of the argument.

The larger half is that **agents fail in loops**. A misconfigured retry, a planning cycle that re-derives the same call, a task that polls too aggressively — these do not look like attacks and they generate attack-scale traffic. The failure mode is a well-intentioned client hammering a capability thousands of times in a minute because a condition it is waiting for will never become true.

Rate limiting is the control that turns that from an outage into a throttled client with a visible error. It is the difference between a bug in one integration and a degradation for everyone.

Note the gauge in the panel: the needle sits **mid-range**, in the teal-to-blue zone rather than pinned. Rate limiting is depicted as a working meter, not an alarm.

### 6. All five gates sit in front of every capability

The gates are drawn as a corridor. A request passes through all five, in order, on the way to the capability behind them.

The implication is architectural: these are **not per-tool implementations**. If each of your forty tools implements its own authorization, you have forty places to get it wrong and no single place to see what the policy is. The gate metaphor is a chokepoint metaphor.

This is also the practical argument for a capability server existing at all. Its value is not that it exposes tools — anything can expose tools. Its value is that it is a place where these five gates can be applied uniformly to everything behind it.

---

## Case study — Brightline Bank, the review that found four of five

Brightline is a mid-sized commercial bank. They built a capability server exposing account and transaction data to internal assistants used by relationship managers and the operations team. Before it could go to production it needed to pass an internal security review and an external penetration test.

It had four of the five gates. The review found the missing one, and then found that two of the four present were in the wrong order.

### What they had built

**Authenticate.** Solid. Mutual TLS between clients and the capability server, plus a signed token carrying the end user's identity. Both the calling service and the human behind it were established on every request.

**Authorize.** Present, but coarse. Permission was evaluated per *tool*: a relationship manager could call `get_account`, an operations user could call `get_account` and `get_transaction_history`. Whether the specific account being requested was one the caller should see was checked inside each tool's implementation.

**Validate.** Present, thorough, and running in middleware — before authorization.

**Rate limit.** Present, per calling service.

**Audit.** Absent as a distinct control. There was application logging, sampled at ten percent, retained for fourteen days.

### Finding 1 — no audit

The reviewer's question was simple: *a relationship manager is alleged to have looked up an account they had no business relationship with. Show me whether they did.*

The team could not. With ten percent sampling, most calls were not recorded. With fourteen-day retention, anything older was gone. And the sampled records did not include which account had been requested — only that `get_account` had been called.

This was the finding that blocked the release. A bank cannot expose customer account data through an interface that cannot answer who looked at what.

**The fix.** A distinct audit path, separate from application logging: every request, no sampling, seven-year retention, written to an append-only store. Each record carries the principal, the calling service, the method, the resource identifiers in the arguments, the outcome, and the gate that refused it if refused.

Audit writes became blocking. If the audit store is unavailable, the capability server refuses requests. That was contentious — it converts an audit outage into a service outage — and the bank accepted it, because the alternative is serving customer data without a record.

### Finding 2 — validate before authorize

The penetration tester found this one. Validation ran in middleware, before the authorization check.

The tester used a token for a low-privilege service account with no permission to call any account method, and sent deeply nested malformed payloads to `get_transaction_history`. Every one was rejected — but by the *validator*, after being fully parsed.

Two consequences. The parser was reachable by a caller with no permission to reach anything, which is a large amount of attack surface exposed to an unauthorised principal. And the rejections came back with detailed validation errors describing the expected schema, which let the tester map the interface without ever being authorised to use it.

**The fix.** Authorization moved ahead of validation. An unauthorised caller now receives a flat refusal before their payload is parsed, and learns nothing about the schema.

### Finding 3 — authorization was not per-item

The tool-level permission model meant `get_account` was either callable or not. Whether *this* caller could see *this* account was enforced inside the tool.

Two problems. The check was duplicated across eleven tools with three slightly different implementations, one of which had a gap for accounts in a particular closed state. And because the check lived inside the tool, a refusal happened after the tool had already begun work — including, in two cases, after it had read the data it was about to refuse to return.

**The fix.** Authorization became a per-item evaluation at the gate, taking the method *and* the resource identifiers from the arguments. The gate answers "may this principal read account 8841" before the tool runs at all. The eleven in-tool checks were deleted.

This is exactly the two-ticks-and-a-warning strip in the diagram: for a request touching three accounts, the gate now returns a verdict per account.

### Finding 4 — rate limiting metered the wrong thing

Limits were per calling service. There were three calling services and thousands of end users behind them. A single relationship manager's runaway client could consume the entire budget for their service, degrading every other user of that service.

**The fix.** Limits per principal as well as per service, with method-class differentiation — a much tighter budget on mutating methods than on reads.

They caught a real problem within a fortnight of shipping it. An assistant integration had a polling bug that re-checked a condition every two hundred milliseconds indefinitely. Under the old model it would have consumed the operations service's whole budget. Under the new one it throttled a single user, produced a visible error, and was fixed the same day.

### What the review taught them

The team's own summary was that they had built five controls and had thought of them as five *features* — each independently valuable, order irrelevant. The review's finding was that the pipeline is a sequence with dependencies, and that two of their controls were doing less work than they appeared to because of where they sat.

They now hold the ordering as a rule with a stated reason for each adjacency, and it is checked in design review before anything new goes behind the gates.

---

## Composition

Five upright panels stand in a row, each mounted on a **tiered pedestal** — a stepped base that raises the panel and gives it the appearance of a gate or turnstile. Teal arrows pass between them at mid-height, so the row reads as a corridor a request travels through.

Each panel carries a white uppercase heading:

**AUTHENTICATE → AUTHORIZE → VALIDATE → RATE LIMIT → AUDIT**

## Element by element

**AUTHENTICATE**
A teal **ID badge on a dark lanyard**, showing an avatar and text lines, resting on a glowing ring. Establishing who is asking.

**AUTHORIZE**
A **green shield with a white check** on a stepped blue plinth. To its right, a narrow dark strip listing three rows: **two green check circles and one red warning dot**. A verdict per item, not a single yes.

**VALIDATE**
An application window showing large teal **`{ }` braces** wrapping text lines, with a **green check badge** at its lower right. Structural checking of the payload.

**RATE LIMIT**
A **speedometer gauge** with a teal-to-blue arc and a needle sitting mid-range, above a small dark control block with three teal indicator lights. A working meter rather than an alarm.

**AUDIT**
A blue **printer emitting a white slip** carrying a green check and text lines, with a teal status light on its base. A discrete record per event, produced deliberately.

## Colour and flow semantics

- **Teal arrows** carry the request through the corridor in one direction.
- **Green** marks passed checks — the shield, the validation badge, the audit slip's check.
- **Red** appears once, as the warning dot in the authorize checklist, indicating a refused item within an otherwise-passing request.
- The **tiered pedestals** are the key compositional device: they raise each control into a barrier the request must clear, rather than a step it passes.
- Unusually for this library, the AUTHORIZE shield is **green rather than coral**, which differs from the coral policy shields used in the architecture diagrams. Read it as the same function.

## How to present it

**Have the room produce the list first.** Ask what controls belong in front of a production capability. They will name most of the five. Write them in whatever order they are offered — then reveal the diagram and compare. The order will be wrong, and that is the session.

**Then attack each adjacency.** For each pair, ask what breaks if you swap them:

- Authenticate/authorize — you decide permissions for an unknown principal.
- Authorize/validate — you expose your parser to unauthorised callers and leak your schema in error messages.
- Validate/rate limit — malformed traffic eats a legitimate caller's budget.
- Anything/audit — the record does not cover the refusals, which is the part that matters.

The second one is where most rooms discover they have it backwards, because validation middleware naturally runs early.

**Ask the account question.** "A user is alleged to have looked at a record they shouldn't have. Show me whether they did." This is the fastest way to find out whether a team has audit or just logging. Follow up with: what is your sampling rate, what is your retention, and do your records include *which resource* was accessed. Most teams fail on at least one.

**Ask whether refusals are recorded.** Almost always no. Then ask what an attacker probing their interface would look like in their telemetry. The answer — invisible — usually changes someone's sprint.

**Point at the two ticks and one warning.** Ask what a request touching six records returns when three are permitted. Teams with boolean authorization have no good answer, and discovering that in front of a picture is easier than discovering it in an incident.

**Reframe rate limiting.** Ask what happens when an agent's retry logic goes wrong. Loops, not attacks, are the common case, and framing the gate as protection against your own well-intentioned clients tends to move it up the priority list.

**Locate the gates architecturally.** Ask where these five live: in each tool, or in front of all of them. If the answer is per-tool, ask how many implementations of the authorization check exist and whether they agree. Brightline had three, and one had a gap.

**Timing.** Twenty-five minutes. Thirty-five if you run the ordering exercise properly, which is the part worth the time.

---

## Lab and checkpoint

**Lab:** Map the five security gates in this diagram — authenticate, authorize, validate, rate limit, audit — onto a real MCP-style server you operate or consume. For each gate, write where it currently lives, what it currently checks, and what would go wrong if it were removed. For any gate that is missing or duplicated, write the smallest change that would fix it.

**Checkpoint:** Why must audit record refusals, not just allowed requests?

**Answer:** Because refusals are often the signal of an attack or a misconfiguration. An allowed log only shows what succeeded; a refusal log shows what was tried. Without refusals, an attacker probing the interface is invisible.

## Glossary

- **Audit** — the gate that records what was attempted, permitted, and denied.
- **Authenticate** — the gate that proves who the caller is.
- **Authorize** — the gate that decides whether this caller may use this capability.
- **Rate limit** — the gate that protects the server from excessive or runaway request volume.
- **Security gate** — a check that every MCP request passes through before reaching the tool.
- **Validate** — the gate that checks the request shape and arguments against the capability schema.

## Sources

- MCP 2026-07-28 security and authorization considerations
- API gateway and layered security design patterns
- Audit logging and refusal-event retention guidance
