# Diagram 153 — Authentication, Authorization, Delegation, and Impersonation

![On dark navy, four blue platform gates read AUTHENTICATE, AUTHORIZE, DELEGATE, and ACT in sequence. White identity cards for MAYA, ACME CLIENT, ACME AGENT, PAYMENT WORKLOAD, and PAYMENT RESOURCE sit beside the flow. A teal chain carries SUBJECT, CLIENT, ACTOR, TENANT, AUDIENCE, and SCOPE beneath the gates. A coral IMPERSONATION shortcut tries to skip from Maya straight to the payment resource and is blocked by a forbidden sign. The flow ends with a DECISION RECEIPT.](../diagrams/153-authentication-authorization-delegation.png)

**Module:** Identity, OAuth, and delegated authority  
**Role in the course:** how to keep proving identity, deciding permission, and delegating bounded authority as separate, reviewable steps  
**Layout:** four gates in a row, five identity cards, a teal claim chain, a blocked coral impersonation shortcut, and a decision receipt  
**Stability:** Identity foundation

---

## At a glance

**AUTHENTICATE → AUTHORIZE → DELEGATE → ACT.**

Maya, the Acme client, the Acme agent, the payment workload, and the payment resource are **five different identity cards**.

A **teal chain** carries **SUBJECT, CLIENT, ACTOR, TENANT, AUDIENCE, and SCOPE**.

**Impersonation** is **blocked**.

Every delegated action ends with a **DECISION RECEIPT**.

---

## What the diagram teaches

### 1. Authentication is only the first gate

**Authentication** answers one question: who or what presented this credential? It does not answer whether that identity may do anything, nor whether it may act in this tenant, on this resource, for this purpose, right now.

The diagram places **AUTHENTICATE** first, but it does not let the identity skip the rest. The client, the agent, the workload, and the resource each need their own authentication evidence. Knowing who knocked is not the same as opening the door.

### 2. Resolve every identity before deciding authority

The white cards in the diagram are **Maya, Acme client, Acme agent, payment workload, and payment resource**. They are not interchangeable labels. They are separate identities with separate trust sources and separate roles.

A secure design resolves at least these identities:

- **Subject** — the human whose request started the work, Maya.
- **Client** — the software Maya is using, such as the Acme web client or browser.
- **Agent** — the Acme agent service that plans and calls tools.
- **Workload** — the background worker or adapter that executes the payment call.
- **Resource** — the payment provider or protected service that performs the effect.
- **Tenant** — the organizational boundary that owns the data and the transaction.

Collapsing any of these into a single string such as `user_id` is the first step toward impersonation. The diagram keeps them on separate cards so the system can carry each one through the chain.

### 3. Authorization is a decision made in this exact context

**Authorization** asks whether the authenticated identity may perform this action now. That means checking tenant, role, case, amount, risk, current policy, and any required approval. It is not a static attribute like "Maya is an admin" or "Maya is allowed to refund."

A strong authorization gate treats the context as part of the decision: the same Maya may be allowed to refund one invoice but not another, or one amount but not a larger one.

### 4. Delegation shrinks authority, not copies it

**Delegation** lets one identity pass a smaller, bounded authority to another. It does not mean the agent or workload receives Maya's full credential and becomes Maya. The diagram shows a narrow grant from one gate to the next, with the teal chain carrying only the claims that are needed.

The analogy is a hotel guest asking a concierge to book a taxi. The guest does not hand over her bank password, credit card, house key, or passport. The concierge receives only the narrow authority needed for that one ride: destination, payment method already on file, and perhaps a time window. The concierge is not the guest.

In code terms, the system should create a **bounded delegation record** rather than copying Maya's broad credential. The record names the original subject, the delegated actor, the target resource, the allowed action, the scope, and an expiry. Anything broader is impersonation wearing delegation's clothes.

### 5. Impersonation is the shortcut the diagram blocks

The **coral IMPERSONATION shortcut** tries to jump straight from Maya to the payment resource, skipping the gates. The diagram shows it blocked with a forbidden sign. That shortcut is the central failure mode this lesson rejects.

Impersonation happens when the system copies Maya's session token downstream, sets a `user_id` field on an agent call, or forwards any identity card as if it were the original.

This is dangerous because it erases the actor. If the payment provider sees a request from the workload, it should know the workload is acting. If it sees Maya's credential, it cannot tell whether the workload, a stolen browser token, or an attacker is presenting it. Impersonation breaks both security and audit.

### 6. The teal chain of claims is the audit backbone

Beneath the four gates, a teal chain carries **SUBJECT, CLIENT, ACTOR, TENANT, AUDIENCE, and SCOPE**. These are the claims that make the delegated action reviewable.

- **Subject** — on whose behalf, e.g. Maya.
- **Client** — the software that presented the original request.
- **Actor** — the software that performs the action.
- **Tenant** — the data and policy boundary.
- **Audience** — the intended recipient.
- **Scope** — the narrow permission.

This chain is not decoration. It is the evidence bundle that lets the organization answer, after the fact, who asked, who acted, for which tenant, to which resource, and under what authority. Without it, every consequential action becomes an un-attributable event.

### 7. From identity to token: OAuth, protected resource metadata, and audience

The diagram stops at the boundary between identity and the token that carries it. The next diagram in the module shows how that token is obtained safely.

![On dark navy, an MCP client begins without a token. The MCP resource returns 401 plus protected-resource metadata. The client discovers the authorization server, runs an authorization-code flow with PKCE S256, validates the returned issuer, requests a resource audience, receives an access token, and then calls the MCP resource. A coral WRONG AUDIENCE TOKEN and a TOKEN PASSTHROUGH are rejected.](../diagrams/154-oauth-resource-audience-flow.png)

That diagram traces the current MCP authorization flow. The resource publishes **protected-resource metadata** so the client can discover the right authorization server. The client uses an **authorization-code flow with PKCE S256**, validates the returned **issuer**, and requests an **audience** that names the MCP resource. The resource then accepts only a token that is issued by the expected issuer and explicitly intended for that resource.

This is the bridge from the identity cards on this diagram to the tokens the next diagram validates. Authentication and authorization at Acme produce a subject and a decision. OAuth and audience binding produce a token that a specific resource can verify.

### 8. A token is not a passport to every service

The second diagram rejects two mistakes: a **wrong-audience token** and a **token passthrough**. A token minted for the file service must not be accepted by the payment service, and an agent token must not be forwarded to the provider as if the agent were the user. A resource that skips audience and issuer validation is a confused deputy. Maya's token is bound to the payment resource and cannot be replayed across Acme.

### 9. Every delegated action ends with a decision receipt

The last white card in the flow is the **DECISION RECEIPT**. It records the acting identity, the delegating identity, the authorization decision, and the result. This is not an afterthought. It is the final requirement of the trace.

A good receipt answers the same questions as the teal chain and also records denials. A blocked impersonation attempt can be more useful evidence than an allowed action.

The receipt turns a runtime decision into a durable business record. It supports audit, dispute resolution, incident response, and governance review.

### 10. The Next.js map: resolve identity in server code, attach a delegation record

The Next.js map in the JSON field gives three concrete implementation moves for this lesson.

- Resolve the signed-in user in server code, create a separate service identity for background work, and attach an explicit delegation record to protected mutations.
- Keep tokens, policy decisions, secrets, and privileged mutations in authenticated server code; send the browser only the minimum display state.
- Use typed request, decision, denial, approval, and receipt records so the React interface can explain security state without inventing it.



### 11. The Python map: distinct Pydantic types and dependency-injected tests

The Python map gives three corresponding implementation moves.

- Model Subject, Client, Actor, Workload, Tenant, Resource, and Delegation as distinct Pydantic types instead of one generic user string.
- Use Pydantic models plus explicit middleware or service boundaries for identity, tenant, policy, data classification, and audit context.
- Test allow and deny paths with hostile synthetic fixtures and dependency-injected identity, policy, storage, secret, and network adapters.

Typed identities and delegation records let tests catch impersonation attempts: a workload presenting a subject token, a missing actor, a wrong audience, or an over-broad delegation.

### 12. The lab, the checkpoint, and the standard line

The lab asks the learner to write separate identity cards for Maya, browser client, Acme agent, workflow worker, payment adapter, and provider, and to add a trust source and allowed actions for each. That exercise forces the distinction that the diagram draws.

The checkpoint asks whether authentication proves that Maya may issue any refund she asks for. The answer is no. Authentication identifies her; authorization still checks tenant, role, case, amount, risk, policy, and approval.

The takeaway is: **preserve the subject, actor, client, workload, and delegation chain.** Impersonation is not a delegation pattern.

---

## Case study — Maya refunds one invoice

The case study is a refund that moves through the four gates.

### Situation

Maya authorizes Acme to refund one invoice, and a background payment workload performs the provider call.

### Walkthrough

- Maya authenticates to Acme; Acme does not send her session credential to the payment service.
- Policy authorizes a refund for the exact case and amount.
- The workload receives only the narrow delegated authority needed for that operation.
- The receipt records Maya as subject and the workload as actor.

### Result

Acme can explain who requested the refund, which software acted, and why that specific action was allowed. The audit is not "Maya did it" or "the agent did it." It is "Maya requested it, the agent planned it, the workload executed it, under this delegation, with this policy decision."

### Danger

One `user_id` field or token passthrough hides the real actor, expands compromise, and makes audit evidence misleading. If the payment provider sees Maya's session token in the request, it cannot tell whether the workload, a stolen token, or an attacker presented it. If the audit record only says "user 1732 refunded invoice 8842," it cannot explain which software actually moved the money.

### Takeaway

Preserve the subject, actor, client, workload, and delegation chain.

### The line in their identity standard

*Every delegated action records the subject, the actor, the client, the workload, the delegation parent, the policy decision, and the result. Impersonation is not a delegation pattern.*

---

## Composition

The diagram is built as a left-to-right pipeline of four blue platforms with five white identity cards on the top and a teal claim chain underneath.

**Four blue platform gates in sequence:**

- **AUTHENTICATE** — who presented the credential.
- **AUTHORIZE** — whether this identity may act in this context.
- **DELEGATE** — the bounded authority passed to the next actor.
- **ACT** — the final call to the protected resource.

**Five white identity cards above the flow:**

- **MAYA** — the human subject.
- **ACME CLIENT** — the software Maya is using.
- **ACME AGENT** — the agent service that plans and calls tools.
- **PAYMENT WORKLOAD** — the background worker that executes the call.
- **PAYMENT RESOURCE** — the protected payment provider or service.

**A teal chain** runs beneath the gates and is labelled with **SUBJECT, CLIENT, ACTOR, TENANT, AUDIENCE, and SCOPE**.

**A coral dashed arrow** labelled **IMPERSONATION** tries to skip from Maya to the payment resource. It ends at a red **BLOCKED** forbidden sign.

**A white card at the far right** is the **DECISION RECEIPT**.

## Element by element

**AUTHENTICATE** — the gate that proves identity. Maya and the client must each authenticate through the appropriate identity provider.

**AUTHORIZE** — the gate that decides permission. It checks the current context, policy, and any approval.

**DELEGATE** — the gate that creates a bounded grant. It narrows authority and records the parent-child relationship.

**ACT** — the gate that performs the final call. The payment resource receives a token or credential that is scoped to this action.

**MAYA** — the human subject whose request started the work.

**ACME CLIENT** — the browser or client software that presents the human's request.

**ACME AGENT** — the agent service that interprets the request and selects tools.

**PAYMENT WORKLOAD** — the background worker or adapter that executes the payment call.

**PAYMENT RESOURCE** — the protected service that performs the actual effect.

**SUBJECT** — the human on whose behalf the action happens.

**CLIENT** — the software that presented the original request.

**ACTOR** — the software that actually performs the action.

**TENANT** — the organizational or data boundary.

**AUDIENCE** — the intended recipient of any token or credential.

**SCOPE** — the narrow permission for this action.

**IMPERSONATION** — the forbidden shortcut that collapses identities.

**DECISION RECEIPT** — the durable record of the authorization and action.

## Colour and flow semantics

- **Cyan arrows** carry the request or delegated authority from one gate to the next. They represent the intended data path of the legitimate flow.
- **Teal arrows** represent verified identity, allowed decisions, and safe results. The teal claim chain is the audit backbone of the diagram.
- **Coral paths** mark failures, shortcuts, and residual risk. The coral impersonation arrow is blocked because it tries to bypass the gates.
- **Blue platforms** are protected identity, policy, or governance boundaries. Each gate is a place where authority is checked or narrowed.
- **White cards** are identity, claim, or evidence records. Maya, the client, the agent, the workload, the resource, and the receipt are all records that must be carried safely.

## How to present it

**Ask the room what happens when the agent calls the payment provider.** Most will say "the agent uses Maya's token" or "the agent acts as Maya." That answer is the setup for the whole lesson.

**Point at the four gates and read them slowly.** Authentication. Authorization. Delegation. Action. Ask which of these the team's current code does in one step.

**Point at the five identity cards.** Maya, client, agent, workload, resource. Ask how many different strings or tokens the system currently creates, and how many of them are confused inside a `user_id` field.

**Trace the teal chain.** Subject, client, actor, tenant, audience, scope. Ask which of those claims the current logs and receipts contain. If the answer is "not all of them," the organization cannot explain a delegated action.

**Walk through the case study.** Maya authenticates, policy authorizes the refund, the workload gets a narrow delegation, the receipt records both Maya and the workload. Ask what would break if the agent simply forwarded Maya's session credential.

**Show the blocked impersonation shortcut.** This is the central warning. Do not let the agent become the user. Do not copy user tokens downstream. Do not collapse five identities into one.

**Introduce the second diagram around this point.** Explain that the identity chain in the first diagram becomes an OAuth token in the next lesson. The token has an issuer, an audience, scopes, and a lifetime. A token for one resource is not a passport to every resource.

**Discuss the Next.js and Python maps.** In Next.js, resolve identity in server code, separate service identity, attach delegation records, and keep tokens out of the browser. In Python, model the identities as distinct Pydantic types and test with hostile fixtures. Ask which parts of the current stack already do this and which parts still pass a generic user string.

**Run the lab as a five-minute exercise.** Have the room write identity cards for Maya, browser client, Acme agent, workflow worker, payment adapter, and provider. For each card, ask for the trust source and the allowed actions.

**Ask the checkpoint question.** Does authentication prove that Maya may issue any refund she asks for? Let the room answer, then restate the answer: no. Authentication identifies her; authorization still checks tenant, role, case, amount, risk, policy, and approval.

**Close on the standard line.** *Every delegated action records the subject, the actor, the client, the workload, the delegation parent, the policy decision, and the result. Impersonation is not a delegation pattern.*

**Mention the sources in context.** The MCP authorization specification describes how an MCP resource challenges and validates a client, and the NIST Zero Trust Architecture describes the continuous verification of identity and authority.

**Timing.** Twenty-five minutes. Thirty if the room writes identity cards for a real payment or agent workflow.

---

## Glossary, related lessons, and sources

**Glossary**

- **Authentication** — proving an identity.
- **Authorization** — deciding permission in a given context.
- **Delegation** — bounded authority passed from one actor to another.

**Related lessons**

- **154 — OAuth, OpenID Connect, resource metadata, and audiences** — the next step from identity to token binding.
- **156 — Workload identity, token exchange, and agent delegation** — how a workload gets its own identity and exchanges it for a target token.
- **168 — Tamper-evident audit chain** — preserving evidence across the whole agent lifecycle.

**Sources**

- MCP authorization
- NIST Zero Trust Architecture
## Lab and checkpoint


**Lab:** For Maya's refund, write separate identity cards for Maya, browser client, Acme agent, workflow worker, payment adapter, and provider. Add trust source and allowed actions.


**Checkpoint:** Does authentication prove that Maya may issue any refund she asks for?


**Answer:** No. Authentication identifies her; authorization still checks tenant, role, case, amount, risk, policy, and approval.

## Sources

- MCP authorization
- NIST Zero Trust Architecture

