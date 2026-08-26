# Diagram 154 — OAuth, OpenID Connect, Resource Metadata, and Audiences

![On dark navy, a laptop labelled MCP CLIENT calls a server stack labelled MCP RESOURCE without a token. The resource returns a red 401 UNAUTHORIZED with a white PROTECTED RESOURCE METADATA card. The client then sends a cyan DISCOVER AUTHORIZATION SERVER arrow to a cobalt AUTHORIZATION SERVER, followed by AUTHORIZATION PLUS PKCE S256, VALIDATE ISSUER, REQUEST RESOURCE AUDIENCE, and receives an ACCESS TOKEN. The client calls the MCP RESOURCE with the token. Below, two coral dashed paths labelled WRONG AUDIENCE TOKEN and TOKEN PASSTHROUGH are blocked by red X circles.](../diagrams/154-oauth-resource-audience-flow.png)

**Module:** Identity, OAuth, and delegated authority
**Role in the course:** how the current MCP authorization flow uses discovery, audience binding, PKCE, and issuer validation
**Layout:** three platforms left to right — MCP CLIENT, MCP RESOURCE, AUTHORIZATION SERVER — with a discovery-and-token flow above and two rejected token paths below

---

## At a glance

The client first calls the **MCP RESOURCE** without a token. The resource answers with **401 UNAUTHORIZED** and **PROTECTED RESOURCE METADATA**.

The client uses that metadata to **DISCOVER AUTHORIZATION SERVER**, run **AUTHORIZATION PLUS PKCE S256**, **VALIDATE ISSUER**, request a **RESOURCE AUDIENCE**, and receive an **ACCESS TOKEN**.

The token is then used to call the **MCP RESOURCE**.

Two bad paths are rejected: a **WRONG AUDIENCE TOKEN** and a **TOKEN PASSTHROUGH**.

A wristband that names the venue is not a passport to every building owned by the same company.

---

## What the diagram teaches

### 1. The resource, not the client, drives the authorization contract

The flow starts with the **MCP CLIENT** making an unauthenticated call to the **MCP RESOURCE**. The resource does not say "go figure it out." It returns **401 UNAUTHORIZED** plus **PROTECTED RESOURCE METADATA**. That metadata is the contract. It tells the client where the resource is happy to accept tokens from, what authorization servers are trusted, and what audience the token must carry.

This is important because the client is often an agent or a browser that does not know the security topology of the resource. The resource publishes its own requirements. The client follows them. If the client had to guess the right authorization server, it would guess wrong, be phished, or use a generic issuer.

The protected-resource metadata also protects against hard-coded or discovered-by-search endpoints. The client does not ask the internet for the authorization server. It asks the resource, and it validates the metadata.

### 2. OpenID Connect and access tokens are different

OAuth gives a client limited access to a protected resource. OpenID Connect adds user authentication and identity claims. The diagram is about the access token that the MCP resource accepts, not the ID token that proves who Maya is.

A common mistake is to take the ID token from an OpenID Connect flow and present it to an MCP server as if it were an access token. The diagram rejects that confusion. The token that reaches the MCP resource must be an access token minted for that resource.

### 3. Discovery is the second step and must be SSRF-safe

After the client reads the protected-resource metadata, it discovers the authorization server. The diagram labels this **DISCOVER AUTHORIZATION SERVER**. This discovery is another place where a malicious redirect or an untrusted metadata document can break the flow. SSRF-safe URL handling means the client only fetches metadata from URLs that the resource explicitly vouched for, and it validates the content before trusting it.

Discovery is not authority. It is a way to find the right authority. The client must still validate the issuer, the keys, and the endpoints it discovers.

### 4. PKCE S256 binds the authorization code to the client instance

The client uses an **AUTHORIZATION PLUS PKCE S256** flow. PKCE is a proof key that ties the authorization request to the token exchange. It prevents an attacker who intercepts the authorization code from redeeming it for a token, because they do not have the matching code verifier.

S256 means the code challenge is a hash. The client keeps the original verifier secret. The authorization server stores the challenge. When the client later exchanges the code, it sends the verifier; the server hashes it and compares. This is especially important for public clients such as browser-based or mobile agents where a code alone could be stolen.

### 5. The authorization request must name the resource and the minimal scope

The client does not ask for a generic token. It requests a **RESOURCE AUDIENCE**. The token audience names the intended **MCP RESOURCE**. The token is also scoped narrowly. A refund scope is not a payment-admin scope. A file-read scope is not a payment scope.

The diagram shows **REQUEST RESOURCE AUDIENCE** as a distinct step because audience is not an afterthought. It is how the authorization server and the resource server agree on the token's purpose.

### 6. The resource validates signature, issuer, audience, expiry, and claims before policy

When the client calls the **MCP RESOURCE** with the **ACCESS TOKEN**, the resource does not skip to business logic. It validates the token first: signature from a trusted key, issuer that matches the expected authorization server, audience that names this resource, expiry and not-before times, and the claims that matter such as tenant, scope, and purpose.

Only after those validations does the resource apply its own policy. This ordering matters. A policy engine cannot make a safe decision from an unvalidated token.

### 7. The wrong-audience token is the confused-deputy path

The first coral branch is **WRONG AUDIENCE TOKEN**. A token may be perfectly valid — right issuer, right signature, not expired — but minted for a different resource. If the payment MCP server accepted a token minted for the file service, the client could replay a file-service credential toward payment authority.

This is a confused deputy. The resource is the deputy. It must check that the token is intended for it, not just that the token is valid somewhere in the organization.

### 8. Token passthrough is the impersonation path

The second coral branch is **TOKEN PASSTHROUGH**. This is when the agent or client sends its own token onward to a downstream API, or when the MCP server forwards the client's token to a payment provider as if the client were directly authenticated by the provider.

The previous diagram shows why this matters.

![On dark navy, four blue platform gates read AUTHENTICATE, AUTHORIZE, DELEGATE, and ACT in sequence. White identity cards for MAYA, ACME CLIENT, ACME AGENT, PAYMENT WORKLOAD, and PAYMENT RESOURCE sit beside the flow. A teal chain carries SUBJECT, CLIENT, ACTOR, TENANT, AUDIENCE, and SCOPE beneath the gates. A coral IMPERSONATION shortcut tries to skip from Maya straight to the payment resource and is blocked by a forbidden sign. The flow ends with a DECISION RECEIPT.](../diagrams/153-authentication-authorization-delegation.png)

Diagram 153 keeps the identities separate. The client, the agent, the workload, and the resource each have their own identity and authority. Token passthrough collapses those identities. The MCP client receives a token for the MCP resource; it does not pass that token to a downstream payment provider. The payment workload gets its own delegated credential.

### 9. Every step produces evidence

A well-run OAuth flow leaves a trail: the metadata response, the authorization request, the PKCE challenge, the issuer validation, the audience in the token, the token validation at the resource, and the policy decision. This evidence is what makes an audit possible.

The system must preserve enough evidence to explain both allowed and denied outcomes. A denial at the resource because the audience is wrong should be logged with the expected and actual audiences. An allowed call should be logged with the token claims that authorized it.

### 10. The Next.js map keeps tokens out of the client surface

In a Next.js application, OAuth redirects and callbacks should live in server routes. State and PKCE verifiers must be protected, not exposed to the browser. Access tokens should be held in authenticated server code whenever possible. The React interface receives only the minimum display state.

Typed request, decision, denial, approval, and receipt records let the interface explain security state without inventing it. The server is the boundary that validates the token, resolves identity and tenant, and only then calls the MCP resource or policy engine.

### 11. The Python map uses standards-aware libraries and strict JWT validation

In Python, use a standards-aware OAuth library, strict JWT validation, and Pydantic models for identity, tenant, policy, data classification, and audit context. Cache trusted metadata with an expiry and apply SSRF protections to discovery fetches. Validate signature, issuer, audience, expiry, and claims in a single middleware step before any route handler runs.

Tests should cover both allow and deny paths with hostile synthetic fixtures. Test a valid token for the wrong audience, a token from the wrong issuer, an expired token, a missing PKCE verifier, and a metadata document that points to a malicious authorization server.

### 12. Access is a contract among client, resource, and authorization server

The whole diagram is a contract. The MCP resource says what it requires. The client discovers and follows. The authorization server mints a token for that specific resource. The resource validates that the token matches the contract.

A token is not a universal key. It is a credential for one resource, under one issuer, for one client, for a bounded time, with a bounded scope. That contract is what makes OAuth useful and what makes it dangerous if ignored.

---

## Case study — Acme payment MCP server

The Acme agent needs Maya-authorized access to the Acme payment MCP server.

### The walkthrough

The client learns the protected resource's authorization servers from the payment MCP server's metadata. Maya authorizes the narrow refund scopes through the expected issuer. The token audience names Acme's payment MCP resource. The server rejects a token minted for the file service or a downstream provider.

### The result

One token cannot be replayed as a universal credential across Acme services. The payment MCP server knows who issued the token, who the token is for, and what scopes it carries.

### The danger

Accepting any token from a familiar issuer, confusing an ID token with an access token, or passing an MCP token downstream creates a confused-deputy path. A file-service token could be replayed to the payment server. A client token could be forwarded to the payment provider, making the provider think Maya called it directly.

### The takeaway

Bind every access token to its issuer, resource, client flow, and minimal purpose.

---

## Composition

Three main platforms and a horizontal flow.

**MCP CLIENT** — the laptop on the left, where the OAuth flow begins.

**MCP RESOURCE** — the server stack in the center, which publishes metadata and validates tokens.

**AUTHORIZATION SERVER** — the server with the shield on the right, which issues the access token.

**Top flow:**
- **CALL MCP RESOURCE WITHOUT TOKEN**
- **401 UNAUTHORIZED** + **PROTECTED RESOURCE METADATA**
- **DISCOVER AUTHORIZATION SERVER**
- **AUTHORIZATION PLUS PKCE S256**
- **VALIDATE ISSUER**
- **REQUEST RESOURCE AUDIENCE**
- **ACCESS TOKEN**
- **CALL MCP RESOURCE**

**Bottom flow:**
- **WRONG AUDIENCE TOKEN** — blocked at the MCP RESOURCE.
- **TOKEN PASSTHROUGH** — blocked at the MCP RESOURCE.

## Element by element

**MCP CLIENT** — the client that wants to call the MCP resource.

**MCP RESOURCE** — the protected server that requires a valid access token.

**AUTHORIZATION SERVER** — the trusted issuer of access tokens.

**CALL MCP RESOURCE WITHOUT TOKEN** — the initial unauthenticated request.

**401 UNAUTHORIZED** — the challenge response.

**PROTECTED RESOURCE METADATA** — the document that tells the client where and how to get a token.

**DISCOVER AUTHORIZATION SERVER** — the client fetches the authorization-server metadata.

**AUTHORIZATION PLUS PKCE S256** — the authorization-code flow with proof key.

**VALIDATE ISSUER** — the client checks the issuer of the authorization response.

**REQUEST RESOURCE AUDIENCE** — the client asks for a token scoped to the MCP resource.

**ACCESS TOKEN** — the credential returned by the authorization server.

**CALL MCP RESOURCE** — the authenticated request.

**WRONG AUDIENCE TOKEN** — a valid token for a different resource, rejected.

**TOKEN PASSTHROUGH** — forwarding a client token to another party, rejected.

## Colour and flow semantics

- **Cobalt platform** — a protected resource or governance boundary. The MCP CLIENT, MCP RESOURCE, and AUTHORIZATION SERVER are cobalt platforms.
- **Cyan arrow** — a request or delegated authority. The discovery, authorization, audience, and token arrows are cyan.
- **Teal arrow** — a verified identity, allowed decision, or safe result. The access token and the successful call are teal.
- **Coral path** — an injection, replay, privilege error, or data leak. The wrong-audience and passthrough paths are coral and blocked.
- **White card** — an identity, token, claim, or evidence record. The metadata and access token cards are white.

The flow reads left to right. The rejection paths sit below the main flow, visually marked as forbidden.

## How to present it

**Start with the wristband analogy.** A concert wristband names the venue and the event. It is not a passport to every building owned by the same company. Ask the room where their tokens currently become passports.

**Trace the flow from left to right.** Call without token, get 401 plus metadata, discover authorization server, run PKCE, validate issuer, request audience, get token, call resource. At each step ask what could go wrong.

**Point at the protected-resource metadata.** Why does the resource publish its own requirements? Because the client should not guess. Ask whether their clients discover authorization servers from the resource or from a configuration file that could be stale.

**Explain PKCE S256.** It is not a detail for mobile apps. It protects the authorization code from being redeemed by an attacker who captures it. Ask whether their authorization-code flow uses PKCE.

**Make the audience visible.** The token is for a specific resource. The diagram shows REQUEST RESOURCE AUDIENCE as a separate step. Ask whether their resources check audience or just signature.

**Show the two coral paths.** Wrong audience means a valid token for the wrong resource. Token passthrough means the client token is forwarded. Both are confused-deputy patterns.

**Use the case study.** Maya wants a refund. The token is for the payment MCP server, not the file service, and not the payment provider. The server rejects a file-service token and refuses to pass the token downstream.

**Map to Next.js.** OAuth redirects and callbacks are server routes. PKCE verifiers and access tokens stay in authenticated server code. The React UI gets only what it needs to display.

**Map to Python.** Use a standards-aware OAuth library, strict JWT validation, Pydantic models for claims, and SSRF-safe discovery. Test the deny paths: wrong issuer, wrong audience, expired token, missing PKCE.

**Run the lab as a drawing exercise.** Ask the room to draw the OAuth messages and write who validates state, PKCE, issuer, signature, audience, expiry, scopes, tenant, and policy at each step.

**Ask the checkpoint.** "Can the payment MCP server accept a valid Acme token whose audience is the file service?" The answer is no. Valid signature is not enough; the token must be intended for the payment resource.

**Cite the sources.** MCP authorization describes the current profile. OAuth Protected Resource Metadata and OAuth Resource Indicators define how the resource advertises its authorization requirements.

**Timing.** Twenty to twenty-five minutes. Thirty if the room traces their own OAuth flow and finds a missing audience or passthrough check.

---

## Lab and checkpoint

**Lab:** Draw the OAuth messages and record who validates state, PKCE, issuer, signature, audience, expiry, scopes, tenant, and policy at each step.

**Checkpoint:** Can the payment MCP server accept a valid Acme token whose audience is the file service?

**Answer:** No. Valid signature is not enough; the token must be intended for the payment resource.

---

## Glossary

- **Access token** — a credential that grants limited access to a protected resource.
- **Audience** — the intended recipient of a token, usually the resource server.
- **PKCE** — Proof Key for Code Exchange, a mechanism that binds an authorization code to the client that requested it.
- **Protected-resource metadata** — a document published by a resource that tells clients how to obtain valid tokens for that resource.
- **Token passthrough** — forwarding a token meant for one party to a different party, which can create impersonation or confused-deputy problems.

---

## Sources

- MCP authorization
- OAuth Protected Resource Metadata
- OAuth Resource Indicators
- OAuth PKCE
