# Diagram 156 — Workload Identity, Token Exchange, and Agent Delegation

![On dark navy, a white MAYA TOKEN card on the left sends a cyan arrow into a blue ACME POLICY platform. A cyan arrow continues from the policy platform to a blue ACME AGENT platform. Above the agent, a white WORKLOAD IDENTITY card and a white TRUST DOMAIN card with a bank icon feed into the agent and a blue trust-domain platform. In the center, a blue TOKEN EXCHANGE gate receives four white claim cards from the left — SUBJECT AUTHORITY, ACTOR ID, TARGET AUDIENCE, and NARROW SCOPE — on teal arrows. The exchange emits a teal arrow right to a white DELEGATED TOKEN card, then to a blue PAYMENT RESOURCE platform with a database and lock, and a teal arrow down to a white DELEGATION RECEIPT card. A coral dashed arrow from the exchange points to a white FULL USER TOKEN COPY card with a duplicate icon, then to a red X.](../diagrams/156-workload-identity-token-exchange.png)

**Module:** Identity, OAuth, and delegated authority  
**Role in the course:** how to let an authenticated Acme workload exchange bounded subject authority for a narrow payment-resource token that preserves Maya as the subject and the agent as the actor  
**Layout:** user token stops at policy, the agent proves a workload identity from a trust domain, a token exchange gate turns four claims into a delegated token, a blocked full-token-copy path, and a delegation receipt  
**Stability:** Stable standards plus evolving MCP agent-identity work

---

## At a glance

**MAYA TOKEN → ACME POLICY → ACME AGENT. WORKLOAD IDENTITY + TRUST DOMAIN → ACME AGENT. SUBJECT AUTHORITY + ACTOR ID + TARGET AUDIENCE + NARROW SCOPE → TOKEN EXCHANGE → DELEGATED TOKEN → PAYMENT RESOURCE. DELEGATION RECEIPT. FULL USER TOKEN COPY BLOCKED.**

Maya's token is the user's proof of identity, but it stops at the Acme policy boundary. The agent that will act is a workload with its own identity, issued from a trust domain. A token exchange takes the four claims, evaluates them against policy, and mints a token aimed only at the payment resource. The payment resource receives the delegated token and records both Maya as the subject and the agent as the actor. The blocked full-token-copy path is the anti-pattern the design rejects.

---

## What the diagram teaches

### 1. A user's token is a boundary credential, not a downstream API key

Maya's token proves that Maya is present and authenticated to Acme. It is an assertion of user identity at the Acme boundary. It is not a key the agent can drop into a downstream HTTP header and use as if it were the user.

The diagram makes this literal: the **MAYA TOKEN** card stops at the **ACME POLICY** platform. The cyan arrow to the **ACME AGENT** carries a policy decision, not the raw credential. If the design passes Maya's session credential into the payment provider, the provider cannot tell whether the request comes from Maya, the agent, a stolen browser cookie, or an attacker. The token's audience and lifetime are wrong, and the audit record collapses into a misleading "user did it" event.

### 2. The agent is a workload with its own identity

The **ACME AGENT** in the diagram is running software, not a person. It receives a **WORKLOAD IDENTITY** from a **TRUST DOMAIN**. That identity is distinct from Maya, the client, and the payment resource.

A workload identity might be a SPIFFE ID, a pod identity, a managed-identity credential, or a service account. Whatever the source, it tells the payment resource which software is acting. The agent does not borrow Maya's identity to become respectable. It proves its own identity and then separately proves that it is authorized to carry Maya's subject authority. The top-down arrows show that the agent must be recognized before it can begin the exchange.

### 3. Token exchange is a transformation, not a relay

**Token exchange** is the standard pattern of trading one security context for another. In OAuth it is described in RFC 8693. In SPIFFE and many cloud identity systems it is the way a workload obtains a token for a downstream resource without revealing the original credential.

The **TOKEN EXCHANGE** gate in the center is not a router. It does not forward Maya's token. It reads the available evidence and mints a new token whose audience is the **PAYMENT RESOURCE** and whose scope is the approved refund. The new token may carry the same subject, a different actor, a shorter lifetime, and a narrower audience. The exchange is a policy enforcement point, not a transport convenience.

### 4. The four claims are the policy inputs

The four white cards entering the exchange are the minimum claims a safe exchange needs.

- **SUBJECT AUTHORITY** — on whose behalf the action happens. This stays Maya.
- **ACTOR ID** — which workload is actually performing the action. This is the Acme agent or a payment worker.
- **TARGET AUDIENCE** — the resource the new token is meant for, such as the payment provider.
- **NARROW SCOPE** — the exact action, case, amount, or time window allowed.

Each claim is a control surface. The exchange can deny a request whose subject does not match the parent approval, whose actor is not the authenticated workload, whose audience is unexpected, or whose scope exceeds the policy decision. The four cards together replace a single over-trusted `user_id` field.

### 5. The delegated token is target-specific and time-bounded

The **DELEGATED TOKEN** card on the right is the only token the payment resource sees. It is issued for one audience, one action, and one lifetime. It cannot be taken to the file service, the email service, or another payment provider and replayed.

The diagram binds the token to the **PAYMENT RESOURCE** with a teal arrow, not a coral one. That color choice matters. The token is a safe result. Its lifetime is short enough that a stolen copy is less useful, and its scope is narrow enough that a confused agent cannot redirect it. The downstream authority should never be broader or longer-lived than the parent authority that created it.

### 6. Impersonation is the anti-pattern the coral path blocks

The coral dashed arrow to **FULL USER TOKEN COPY** is the mistake the design refuses. Copying Maya's user token into the downstream request is not delegation; it is impersonation. The red X at the end of that path is a hard rule.

The course analogy is a company issuing a courier a one-delivery badge that names the employee's request, the courier, the destination, and an expiry; it does not hand over the employee's master badge. The full-user-token-copy path is exactly that master badge being carried downstream.

Impersonation erases the actor. If the payment provider sees Maya's token, it cannot tell that the agent was the one that moved the money. If the agent is compromised, the attacker now has a token that is valid for every service Maya can reach. If the token is logged or queued, it becomes a long-lived secret that can be replayed by anyone with read access.

### 7. This diagram extends the identity chain from lesson 153

The previous diagram in this module kept the same idea at the identity level: authenticate, authorize, delegate, act, while keeping subject, client, actor, tenant, audience, and scope distinct and blocking impersonation.

![On dark navy, four blue platform gates read AUTHENTICATE, AUTHORIZE, DELEGATE, and ACT in sequence. White identity cards for MAYA, ACME CLIENT, ACME AGENT, PAYMENT WORKLOAD, and PAYMENT RESOURCE sit beside the flow. A teal chain carries SUBJECT, CLIENT, ACTOR, TENANT, AUDIENCE, and SCOPE beneath the gates. A coral IMPERSONATION shortcut tries to skip from Maya straight to the payment resource and is blocked by a forbidden sign. The flow ends with a DECISION RECEIPT.](../diagrams/153-authentication-authorization-delegation.png)

That diagram traces the identity handoffs. The current diagram is the next hop: the agent, now a workload, uses token exchange to call the payment resource. The subject and actor claims are the same, but now they are carried inside the exchanged token. The audience and scope are also part of the token, so the payment resource can validate them without trusting Acme's server at runtime. The blocked impersonation path and the blocked full-token-copy path are the same rule: no actor may become the user, and no user token may become a universal credential.

### 8. Subject and actor are both needed in the same token

A delegated token that only says "Maya" hides the workload. A token that only says "Acme agent" hides the person whose case it is. The diagram keeps both in the same flow.

The **SUBJECT AUTHORITY** card is the reason the refund is allowed: Maya approved it. The **ACTOR ID** card is the entity that will execute it: the authenticated Acme workload. The payment resource needs both. It needs the subject for customer attribution and the actor for operational audit. When a dispute arrives, the organization must answer "Maya asked for this refund" and "the Acme payment workload issued it." A token that carries only one of those answers is an incomplete evidence record.

### 9. The delegation receipt makes the exchange reviewable

The **DELEGATION RECEIPT** card at the bottom is not a decorative badge. It is the durable record of the exchange. It should include the delegation parent, the target resource, the policy decision, the token identifier, the action, the scope, and the time.

Without the receipt, the downstream call is an un-attributable event. With it, an auditor can trace a payment back to Maya's request, the agent's workload identity, the token exchange policy, and the payment resource response. The receipt also records denied exchange attempts. A request blocked because the actor is wrong, the audience is unexpected, or the scope is too broad is often the most useful evidence that the control is working.

### 10. Token exchange is the delegated hop between authorization and action

The exchange is a policy gate, not just a token mint. The trace in the course is a five-step recipe:

1. Authenticate the Acme workload through a workload-identity trust domain.
2. Verify Maya's subject authority at Acme's boundary and keep her credential there.
3. Evaluate delegation policy for actor, tenant, target audience, action, scope, risk, and lifetime.
4. Exchange or mint a narrow target token that preserves subject and actor semantics.
5. Record delegation parent, target, policy decision, token identifier, action, and receipt.

This sequence shows that the exchange happens after the system knows who is acting and what is allowed, and before the resource is called. Skipping any step collapses the design into either impersonation or over-delegation.

### 11. The Next.js map: server-only exchange logic and signed delegation references

The Next.js map gives three concrete implementation moves for this lesson.

- Use server-only exchange logic for background jobs and carry a signed delegation reference — not a browser session token — through durable work records.
- Keep tokens, policy decisions, secrets, and privileged mutations in authenticated server code; send the browser only the minimum display state.
- Use typed request, decision, denial, approval, and receipt records so the React interface can explain security state without inventing it.

In practice, the user identity is resolved in a server Route Handler, the background worker is authenticated through a workload identity, and the token exchange runs in a server-only service. The browser never sees an access token. The UI receives a displayable status such as "refund issued" with a delegation receipt identifier, not the token itself.

### 12. The Python map: explicit exchanged-token claims and dependency-injected tests

The Python map gives three corresponding implementation moves.

- Integrate workload credentials through a provider adapter and model exchanged-token claims explicitly, including subject, actor, audience, scope, tenant, and delegation parent.
- Use Pydantic models plus explicit middleware or service boundaries for identity, tenant, policy, data classification, and audit context.
- Test allow and deny paths with hostile synthetic fixtures and dependency-injected identity, policy, storage, secret, and network adapters.

The key design decision is to treat the exchanged token as a typed object, not a string. A function that receives the token can prove that its subject, actor, audience, and scope are present and consistent. The tests should include missing subject, wrong actor, wrong audience, excessive scope, expired parent, and a full user-token passthrough.

---

## Case study — Maya's refund continues after she closes her browser

Maya authorizes a refund in the morning and then closes her laptop. A durable Acme workflow resumes in the evening and must call the payment provider.

### Situation

The durable Acme workflow resumes after Maya has closed her browser and needs the payment service to issue the approved refund. The workflow cannot ask Maya to re-authenticate. It must act on the authority she already granted.

### Walkthrough

- The worker authenticates as the Acme payment workload. It presents a workload identity that the trust domain recognizes.
- It loads the still-valid bound approval and parent delegation. The policy system checks that the refund is still authorized, that the case is still open, and that the amount has not changed.
- Policy exchanges that context for a short-lived payment token with one audience and one action. The token carries Maya as subject and the workload as actor.
- The payment resource records both Maya's subject and the workload actor before it performs the refund.

### Result

The background action remains attributable and bounded without storing or replaying Maya's broad login credential. The provider can answer the audit question: "Maya requested this refund, and the Acme payment workload issued it under this policy decision."

### Danger

Copying a user bearer token through queues and agents increases theft, breaks audience boundaries, and erases which workload actually acted. If the token is exposed in logs or queues, an attacker can use it far beyond the refund. If the provider sees only Maya's credential, it cannot tell whether a compromised agent, a confused model, or a malicious worker performed the call.

### Takeaway

Delegate narrow authority to an authenticated workload; never turn it into the user.

### The line in their identity standard

*Every delegated workload call uses a target-specific token that preserves the subject, the actor, the audience, the scope, and the policy decision. User tokens do not leave the authorization boundary.*

---

## Composition

The diagram is built as a left-to-center flow into a central exchange gate, with two downward identity feeds and a blocked anti-pattern on the right.

**Left side:**
- **MAYA TOKEN** — a white card with a person icon, representing the user's authenticated credential.
- **ACME POLICY** — a blue diamond platform, the place where Maya's request is authorized.
- **ACME AGENT** — a blue diamond platform with a robot head, the workload that will act.

**Top side:**
- **WORKLOAD IDENTITY** — a white card, the identity assigned to the running agent.
- **TRUST DOMAIN** — a white card with a bank icon, the authority that issues workload identities.
- A blue trust-domain platform sits beneath the trust-domain card and feeds the agent.

**Center:**
- **TOKEN EXCHANGE** — a blue gate-like platform with a key icon.
- Four white claim cards enter from the left: **SUBJECT AUTHORITY**, **ACTOR ID**, **TARGET AUDIENCE**, **NARROW SCOPE**.

**Right side:**
- **DELEGATED TOKEN** — a white card with a key icon, the minted downstream credential.
- **PAYMENT RESOURCE** — a blue diamond platform with a database and lock, the protected service.
- **FULL USER TOKEN COPY** — a white card with a duplicate icon on a coral arrow, then a red X.

**Bottom:**
- **DELEGATION RECEIPT** — a white card with a badge, the evidence record of the exchange.

---

## Element by element

**MAYA TOKEN** — the user's credential, consumed at the Acme policy boundary.

**ACME POLICY** — the authorization and delegation decision point.

**WORKLOAD IDENTITY** — the identity of the running agent or worker.

**TRUST DOMAIN** — the issuer or authority that vouches for workload identities.

**ACME AGENT** — the workload that performs the token exchange and downstream call.

**SUBJECT AUTHORITY** — the human or originating identity on whose behalf the action is taken.

**ACTOR ID** — the software identity that actually performs the action.

**TARGET AUDIENCE** — the intended resource for the delegated token.

**NARROW SCOPE** — the limited action, case, amount, or time window the token permits.

**TOKEN EXCHANGE** — the gate that transforms the available claims into a target token.

**DELEGATED TOKEN** — the new credential issued for the payment resource.

**PAYMENT RESOURCE** — the protected downstream service.

**FULL USER TOKEN COPY** — the impersonation pattern the design rejects.

**DELEGATION RECEIPT** — the durable record of the exchange and its policy inputs.

---

## Colour and flow semantics

- **Cyan arrows** carry the request, delegated authority, or intended data path. Maya's token enters policy, policy passes a decision to the agent, and the workload identity and trust domain feed the agent.
- **Teal arrows** represent verified identity, allowed decisions, safe results, and evidence. The four claims enter the exchange on teal arrows because they are the verified input to the token mint. The delegated token, payment resource, and delegation receipt are also teal because they are the safe output.
- **Coral paths** mark injection, replay, privilege error, or residual risk. The full-user-token-copy path is coral because it would break audience boundaries and hide the actor.
- **Blue platforms** are protected identity, policy, tenant, resource, or governance boundaries. The policy, agent, trust-domain, and payment-resource platforms are all blue.
- **White cards** are identity, token, claim, policy, or evidence records. Maya's token, the four claim cards, the delegated token, and the receipt are all white cards.

---

## How to present it

**Ask the room what the agent should send to the payment provider.** Most will say "Maya's token" or "the agent acts as Maya." That answer is the setup for the lesson.

**Point at the MAYA TOKEN card and the ACME POLICY platform.** The token stops at the boundary. The arrow to the agent carries a policy decision, not the credential. Ask how many places in their system currently pass a user token downstream.

**Trace the top-down identity feeds.** WORKLOAD IDENTITY and TRUST DOMAIN. Ask whether their agent service has its own identity and how it is issued. If the agent is anonymous, it cannot be audited.

**Point at the four claim cards entering the exchange.** Subject, actor, audience, scope. Ask which of these their current tokens carry. If the token only contains a user ID, it does not carry enough policy context.

**Emphasize the blocked full-token-copy path.** This is the central warning. Do not copy Maya's bearer token into the payment request. Do not turn the agent into the user. The red X is a hard rule.

**Show the second diagram at this point.** Explain that lesson 153 keeps the same subject, client, actor, tenant, audience, and scope distinct across four gates, while this diagram turns those claims into a token exchange. The blocked impersonation path and the blocked full-token-copy path are the same idea.

**Trace the token exchange as a five-step gate.** Authenticate the workload, verify the subject authority, evaluate delegation policy, mint a narrow target token, record the receipt. Ask which step is missing in their current integration.

**Discuss the case study.** Maya closes her browser, but the durable workflow can still issue a narrow, attributable refund. Contrast it with the danger of copying her token through queues and agents.

**Talk about standards and roadmaps.** Token exchange is a stable OAuth standard in RFC 8693. SPIFFE provides workload identity. MCP agent identity, federation, and standardized exchange are active areas, so implementations must name their exact profile. The course sources are OAuth Token Exchange, SPIFFE specifications, the MCP current roadmap, and MCP enterprise-managed authorization.

**Run the lab as a five-minute exercise.** Have the room design the claims for one Acme exchange: subject, actor, tenant, audience, action, scope, case, amount ceiling, delegation parent, issue time, expiry, and policy ID.

**Ask the checkpoint question.** Why include both subject and actor? Let the room answer, then restate: the subject explains on whose behalf the action occurs; the actor identifies the software that actually performed it.

**Close on the standard line.** *Every delegated workload call uses a target-specific token that preserves the subject, the actor, the audience, the scope, and the policy decision. User tokens do not leave the authorization boundary.*

**Mention sources in context.** OAuth Token Exchange defines the pattern, SPIFFE specifications describe workload identity, the MCP current roadmap tracks agent-identity work, and the MCP enterprise-managed authorization post describes how organizations can govern these flows.

**Related lessons to mention.** **153 — Authentication, authorization, delegation, and impersonation** for the identity chain. **155 — DPoP, sender-constrained tokens, and replay resistance** for binding token use to a key. **168 — Tamper-evident audit chain** for preserving evidence across the whole lifecycle.

**Timing.** Twenty-five minutes. Thirty if the room designs claims for a real agent-to-provider flow.
## Lab and checkpoint


**Lab:** Design claims for one Acme exchange: subject, actor, tenant, audience, action, scope, case, amount ceiling, delegation parent, issue time, expiry, and policy ID.


**Checkpoint:** Why include both subject and actor?


**Answer:** The subject explains on whose behalf the action occurs; the actor identifies the software that actually performed it.

## Glossary

- **Workload identity** — identity for running software
- **Token exchange** — trading security context for a target token
- **Actor** — identity performing the delegated action

## Sources

- OAuth Token Exchange
- SPIFFE specifications
- MCP current roadmap
- MCP enterprise-managed authorization

