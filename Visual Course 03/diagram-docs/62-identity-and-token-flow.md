# Diagram 62 — Identity and Token Flow

![A five-column token flow on dark navy. USER signs in to APPLICATION, which requests a token for the MCP server from AUTHORIZATION SERVER and receives one stamped AUDIENCE MCP SERVER. The MCP SERVER requests a downstream token and receives one stamped AUDIENCE DOWNSTREAM API, and carries a VALIDATES panel listing ISSUER, AUDIENCE, EXPIRY and SCOPE with green ticks. A red dashed line runs along the bottom from the application to the downstream API through a red badge reading NO TOKEN PASSTHROUGH.](../diagrams/62-identity-and-token-flow.png)

**Module:** Security
**Role in the course:** how tokens move, and where they must not
**Layout:** five parties with token exchanges, and a prohibited path drawn along the base

---

## At a glance

A token is issued **for a specific recipient**, and every hop gets its own. The application holds a token whose audience is the MCP server. The MCP server holds a different token whose audience is the downstream API.

Along the bottom, in red, the thing that must not happen: **NO TOKEN PASSTHROUGH**. The application's token never reaches the downstream API.

The audience stamps are the mechanism. The prohibition is the point.

---

## What the diagram teaches

### 1. Audience is what makes a token safe to hold

Two token cards appear, and each carries an **AUDIENCE** stamp: **AUDIENCE MCP SERVER** and **AUDIENCE DOWNSTREAM API**.

The audience claim says *who this token is for*. A token issued for the MCP server is only valid at the MCP server. Presented anywhere else, it must be rejected.

That single property is what makes it safe for a service to receive a token at all. Without it, any service that receives a token can use it anywhere, and a compromised or curious service inherits the caller's full reach.

With it, the blast radius of a leaked token is exactly one recipient.

### 2. Each hop requests its own token, and the pattern is visible in the arrows

Read the top row: **REQUEST TOKEN FOR MCP SERVER**, then **REQUEST TOKEN FOR MCP SERVER** again, then **REQUEST DOWNSTREAM TOKEN**.

The MCP server does not reuse what it received. It **exchanges** — presenting its own credentials plus the context of the original caller, and receiving a new token scoped to the next hop.

This is the correct pattern for chained calls, and it preserves two things simultaneously: the identity of the original user flows through, and no single token is valid at more than one place.

### 3. NO TOKEN PASSTHROUGH is drawn as a long red dashed line, and the length is deliberate

The prohibited path runs the **full width of the frame**, from beneath the application to beneath the downstream API, passing through a red ✗ badge and a coral label.

Drawing it long makes the shortcut visible as a shortcut. The temptation is exactly this: the application already has a token, the downstream API accepts tokens, so pass it along and save a round trip.

What that costs:

**The audience check becomes meaningless.** If the downstream API accepts a token minted for the MCP server, the audience claim is decoration.

**The MCP server becomes a confused deputy.** It is now a proxy for whatever the user's token can do, not a service with its own bounded capability.

**Scope escalation.** The user's token likely has broader scope than this operation needs. Passing it through hands the downstream API a credential far wider than the task.

**Revocation and audit break.** The downstream API sees the user's token, not the MCP server's. Its logs cannot distinguish a direct user call from a call made via the MCP server.

### 4. The VALIDATES panel names four checks, and all four are necessary

Beneath the MCP server sits a panel headed **VALIDATES** with four green-ticked rows:

**ISSUER** — was this token minted by an authority we trust? Prevents tokens from an unrelated or attacker-controlled issuer.

**AUDIENCE** — is this token for *us*? The check that makes the audience claim mean something. A service that does not verify audience will happily accept a token intended for another service.

**EXPIRY** — is it still valid? Prevents replay of captured tokens.

**SCOPE** — does it permit this operation? Identity established is not permission granted.

Three of these are cheap and commonly implemented. **Audience is the one that gets skipped**, and it is the one that turns the whole model from a security boundary into a formality.

### 5. The authorization server is the only party that mints

Every token in the diagram originates at the **AUTHORIZATION SERVER**, drawn with a teal padlock shield.

Nothing else issues tokens. Services request them; they do not create them. That centralisation is what makes revocation possible — there is one place that knows what has been issued and can stop honouring it.

### 6. Identity flows through, but authority does not accumulate

Worth stating explicitly because it is the subtle part.

The **user's identity** is present at every hop — the downstream API can know that this call is being made on behalf of a specific user.

The **user's authority** is not. Each token is scoped to what that specific hop needs. The chain preserves who, and narrows what.

Getting this backwards — preserving authority by passing the original token — is precisely the passthrough failure.

The scope each exchanged token carries is determined by what the capability actually needs:

![A coral DO EVERYTHING toolbox contrasted with narrow tools scoped by TENANT, RESOURCE, ACTION and LIMITS, filtered down to the two tools an agent is actually allowed.](../diagrams/63-least-privilege-tools.png)

Narrow tools and scoped tokens are the same discipline at two layers. A narrow tool executing with a wide credential is still a wide capability.

---

## Case study — Marchmont Wealth, the confused deputy

Marchmont provides investment platform services to about 40,000 retail clients and 300 independent financial advisers. Their MCP layer exposes portfolio, transaction and document capabilities, and calls a downstream custodian API for holdings and settlement data.

### The shortcut

The custodian API accepted the same OAuth tokens their platform issued, because both sat behind the same authorization server.

Their MCP server, receiving a user token, passed it straight through on downstream calls. It saved a token exchange per request — measurably, about 40ms — and it worked.

It ran for fourteen months.

### What the audit found

An external security review asked a simple question: *what can the MCP server do that its callers cannot?*

The intended answer was "less" — the MCP server should have narrow, task-scoped access. The actual answer was "exactly as much as whichever caller it is currently serving," because it was using their credentials.

That is the confused deputy problem. The MCP server had no authority of its own; it borrowed each caller's.

Three specific consequences.

**Scope was far wider than needed.** Adviser tokens carried scopes covering all of their clients' portfolios, document access, and transaction initiation. A capability that only needed to read one holding was executing with a credential that could initiate transactions across an adviser's entire book.

**The custodian's audit was wrong.** Their logs showed calls arriving with adviser identities. They could not distinguish an adviser calling the custodian directly from Marchmont's MCP server calling on their behalf. When the custodian investigated an anomalous access pattern, they attributed it to an adviser who had not made the calls.

**A capability bug became a scope problem.** A defect in one capability caused it to request a broader data range than intended. Because it was running with adviser scope, the request succeeded. Had the MCP server held a narrow, task-scoped token, it would have been refused.

That third one had actually happened, eight months earlier. It had been diagnosed as a data-range bug and fixed. Nobody had noticed that the reason it succeeded was a missing scope boundary.

### The rebuild

**Token exchange at every hop.** The MCP server now presents its own client credentials plus the user's token, and receives a new token with `audience: custodian-api` and a scope covering only what the specific capability needs.

The 40ms came back. Nobody noticed.

**Audience validation everywhere, enforced.** Their audit found that the custodian API had not been checking audience at all — it validated issuer, expiry and signature, and accepted any token from a trusted issuer.

This is the common gap and it is the one that makes passthrough possible in the first place. If the custodian had been checking audience, the passthrough would have failed on day one and been fixed then.

**Per-capability scopes.** Each MCP capability declares the downstream scopes it needs. The token exchange requests exactly those. `get_holding` receives a read scope for one account; `initiate_transfer` receives something narrower and more heavily gated.

**Identity preserved, authority narrowed.** The exchanged token carries the acting user as a claim. The custodian's logs now show both: the MCP server as the caller, and the user on whose behalf. Their previous ambiguity is gone.

### The incident that validated it

Four months after the change, a capability had a defect that caused it to request holdings for an account outside the requested portfolio.

The custodian refused it — the exchanged token's scope covered only the requested account.

Under the old design, that request would have succeeded, because the adviser's token covered their whole book. The defect would have returned data from an unrelated client account and nobody would have seen an error.

Their security lead's note: *the same bug, eight months apart, with two completely different outcomes. The only thing that changed was whose credential it was running on.*

### Results

- **Confused-deputy exposure:** eliminated.
- **Downstream scope per call:** from adviser-wide to per-account.
- **Custodian audit attribution:** now distinguishes direct from delegated calls.
- **Latency cost of token exchange:** ~40ms, mitigated by caching exchanged tokens for their short lifetime.

---

## Composition

Five columns left to right, with token exchanges drawn as paired arrows between them.

**USER → APPLICATION → AUTHORIZATION SERVER → MCP SERVER → DOWNSTREAM API**.

Between each pair, a **solid cyan arrow** labelled with a request and a **dashed cyan arrow** labelled **TOKEN** returning, each accompanied by a white card carrying an **AUDIENCE** stamp.

Along the base, a **red dashed line** runs from beneath the application, through a red ✗ badge and a coral **NO TOKEN PASSTHROUGH** label, to beneath the downstream API.

## Element by element

**USER**
A person figure beside a white sign-in card with a teal avatar and a dot-masked password field.

**APPLICATION**
A browser window with a blue title bar and teal content blocks.

**AUTHORIZATION SERVER**
A blue server tower with a **teal shield bearing a white padlock**.

**MCP SERVER**
A blue server tower with a dark **`< >` code panel**, and beneath it a white panel headed **VALIDATES** listing four green-ticked rows: **ISSUER**, **AUDIENCE**, **EXPIRY**, **SCOPE**.

**DOWNSTREAM API**
A blue server tower with a **teal wireframe globe**.

**Token cards**
Three white cards, each with a **teal shield** and text lines, headed by a dark tag: **AUDIENCE MCP SERVER** (twice) and **AUDIENCE DOWNSTREAM API**.

**NO TOKEN PASSTHROUGH**
A **red circular ✗** attached to a coral label, on a long red dashed line spanning the frame.

## Colour and flow semantics

- **Solid cyan arrows** carry token requests forward; **dashed cyan arrows** carry issued tokens back.
- **Teal** marks every shield — the authorization server's padlock, and each token card's badge.
- **Red dashed** marks the prohibited path, and it is the longest line in the diagram.
- **Green ticks** in the VALIDATES panel mark the four checks as all required.
- The **AUDIENCE tags** are the only repeated labelling device, and they are the mechanism the whole diagram rests on.

## How to present it

**Ask what an audience claim is for.** Then ask whether their services check it. Most check issuer, expiry and signature. Audience is the one that gets skipped, and it is the one that makes the model work.

**Trace the red line with your finger.** Application to downstream API, bypassing the exchange. Ask why anyone would do it — it saves a round trip and it works. Then walk the four costs: meaningless audience check, confused deputy, scope escalation, broken audit.

**Explain confused deputy plainly.** A service with no authority of its own, borrowing each caller's. Ask the room: *what can your service do that its callers cannot?* If the answer is "the same things," they have one.

**Tell the Marchmont scope story.** A capability needing to read one holding, executing with a credential that could initiate transactions across an adviser's whole book. Fourteen months.

**Then tell the same-bug-twice story.** A data-range defect that succeeded under passthrough and was refused under scoped exchange. Same bug, eight months apart, two outcomes. This is the most persuasive item in the document because it shows the control working rather than the failure happening.

**Ask who was checking audience at the custodian.** Nobody. Point out that if they had been, the passthrough would have failed on day one. A missing check upstream is what makes a bad pattern downstream survivable.

**Separate identity from authority.** Identity flows through the chain — the downstream API knows which user this is on behalf of. Authority does not accumulate; each token is scoped to its hop. Preserving authority is the passthrough failure.

**Address the latency objection.** Marchmont's exchange cost 40ms and they cached exchanged tokens for their short lifetime. Ask what the room's equivalent shortcut is currently saving, and what it is spending.

**Timing.** Twenty-five minutes. Thirty-five if you trace an actual chained call in the room's system and identify which token is presented at each hop.

---

## Lab and checkpoint

**Lab:** Trace one chained call in your system. For each hop, write which token is presented, its audience, issuer, expiry, and scope. Identify any passthrough where a downstream service receives a token scoped for an upstream audience. Then design the exchange token that would give the downstream API only the authority it needs.

**Checkpoint:** Why is audience the most important claim to check?

**Answer:** Because audience proves the token is intended for the service that receives it. Without audience validation, a service can take a token meant for another service and use it. That leads to confused deputy, scope escalation, and broken audit trails.

## Glossary

- **Audience** — the intended recipient of a token, which the recipient must check.
- **Authorization server** — the server that issues tokens to callers.
- **Confused deputy** — a service with no authority of its own that borrows a caller's token and can act beyond its intended scope.
- **Downstream API** — the service at the end of the chain.
- **Exchange** — the act of swapping one scoped token for another at each hop.
- **Expiry** — the time after which the token is no longer valid.
- **Issuer** — the party that created and signed the token.
- **MCP server** — the server that validates the token before serving the capability.
- **No token passthrough** — the rule that a token must not be forwarded unchanged to a downstream service.
- **Scope** — the actions and resources the token is allowed to access.

## Sources

- JWT audience, issuer, and scope validation
- Token exchange and the confused-deputy problem
- OAuth 2.0 token exchange and audience-restricted tokens
