# Diagram 172 — Capstone: Acme Secure Agent Gateway and Policy Center

![On dark navy, Maya and Acme operators enter through an Identity and Tenant Gate on the left. In the center, a large Secure Agent Gateway platform is connected to Instruction Authority, Policy Decision, Capability Broker, Approval Binding, Secret Broker, Tenant Data Plane, Sandbox, Egress Gate, Discovery Trust, Provenance, and Audit Evidence. A teal arrow leads from the gateway to a Safe Refund card and a receipt. Coral arrows from a Malicious Attachment lead to Untrusted Data, Quarantine, Deny, Redact, and Step Up. An MCP Server and an A2A Agent connect through controlled edges. Around the whole system, an outer Governance Loop reads GOVERN, MAP, MEASURE, MANAGE.](../diagrams/172-acme-secure-agent-gateway-policy-center.png)

**Module:** Governance and organizational control  
**Role in the course:** how to turn every Volume 7 lesson into one connected, testable secure-agent architecture  
**Layout:** a central Secure Agent Gateway surrounded by named control platforms, with an Identity and Tenant Gate on the left, a teal safe-refund path to the right, coral denial and quarantine paths below, MCP and A2A edges above, and a GOVERN · MAP · MEASURE · MANAGE loop around the outside  
**Stability:** Capstone architecture  
**Outcome:** Protect Maya's case without preventing the legitimate agent workflow.

---

## At a glance

**MAYA + ACME OPERATORS → IDENTITY AND TENANT GATE → SECURE AGENT GATEWAY → INSTRUCTION AUTHORITY / POLICY DECISION / CAPABILITY BROKER / APPROVAL BINDING / SECRET BROKER / TENANT DATA PLANE / SANDBOX / EGRESS GATE / DISCOVERY TRUST / PROVENANCE / AUDIT EVIDENCE → SAFE REFUND + RECEIPT**.

The teal path is the legitimate refund. A **malicious vendor attachment** is routed to **Untrusted Data** and **Quarantine**. It cannot change the payee, request a secret, call an unapproved destination, or hand work to an unknown agent. **Deny**, **Redact**, **Step Up**, and **Quarantine** are the allowed responses to hostile branches.

The **MCP Server** and **A2A Agent** are not inside the trust zone. They connect through controlled edges and must pass the same policy center. The outer **GOVERN → MAP → MEASURE → MANAGE** loop means the architecture is never finished; it is reviewed when context, threats, or incidents change.

This is the airport view of agent security: identity checks, tickets, baggage screening, restricted doors, air-traffic control, customs, incident teams, and flight records cooperate so passengers travel without giving anyone unlimited access.

---

## What the diagram teaches

### 1. The gateway is a logical set of enforcement points, not one giant service

The **Secure Agent Gateway** is a boundary drawn around many small, coordinated controls. It is not a single product or a dashboard that forwards requests to the same broad APIs. Each platform—Instruction Authority, Policy Decision, Capability Broker, Approval Binding, Secret Broker, Tenant Data Plane, Sandbox, Egress Gate, Discovery Trust, Provenance, and Audit Evidence—can live in a different service, container, or runtime. That separation matters because a breach of one component should not automatically breach every other one. It also means an engineering team can start with the controls they need most and add the rest without redesigning the whole system.

The trace runs in five steps. First, authenticate Maya, the client, the agents, the workloads, the operators, the MCP resources, and the A2A agents while preserving subject and actor. Second, classify the attachment as untrusted data and keep instruction authority in trusted policy, user-intent, and approval channels. Third, evaluate tenant, audience, capability, policy, risk, transaction, secret, sandbox, and egress controls at execution. Fourth, preserve discovery, provenance, denial, approval, action, privacy, and tamper-evident evidence without logging secrets. Fifth, govern the full system through the NIST loop, OWASP coverage, named owners, reviews, incidents, and expiring exceptions.

### 2. Identity and tenant are the first gates

**Maya** and the **Acme operators** do not enter the gateway as anonymous traffic. They pass through an **Identity and Tenant Gate** that resolves who is asking, what software is acting, and which organization owns the case. The course treats authentication and authorization as separate jobs: authentication proves an identity, authorization decides what that identity may do in this exact context. A tenant is not a value submitted by the browser; it is a verified boundary that follows the request through the API, policy, database rows, vector indexes, queues, artifacts, and audit logs. If identity or tenant cannot be resolved, the request stops before it reaches any tool, secret, or data plane. The gateway never guesses.

### 3. Instruction authority lives in trusted channels

The **Malicious Attachment** is not destroyed; it is classified as **Untrusted Data** and may be quarantined for inspection. It can inform reasoning—extracting an invoice number or reading a case reference—but it cannot approve a refund, change a payee, request a credential, or choose a destination. **Instruction Authority** means the system obeys only trusted sources: the published policy, the verified user request, and the bound approval. This is the central defense against prompt injection and goal hijack. If any component tries to promote untrusted content into an instruction, the gateway either denies the action, redacts the sensitive output, or steps up to a human approver.

### 4. Policy is the decision center

The **Policy Decision** platform is the heart of the gateway. It receives a complete context—subject, actor, client, tenant, resource, action, data class, destination, risk, and approval state—and returns **allow**, **deny**, **redact**, **step-up**, or **quarantine** plus obligations. The policy is versioned, and every answer produces a **Decision Receipt**. That receipt is not decorative; it is the contract the enforcement points obey and the evidence the auditors review. A denial must explain why. A step-up must explain what is missing. An allow must list the obligations the tool must satisfy before it runs. When policy, context, and enforcement are connected, the architecture becomes explainable. When they are not, the system becomes a set of disconnected hopes.

### 5. Capabilities are narrow and brokered

The **Capability Broker** gives the agent one card at a time, not a master key. Each capability card names the tenant, resource, action, limit, expiry, and destination. The diagram rejects a broad, all-powerful tool because a confused or compromised agent should not be able to issue arbitrary provider requests, export credentials, or search across tenants. In Acme, the difference is between a generic `callPaymentProvider` function and a typed `issueApprovedRefund` operation with a bound case, amount, payee, and destination. The broker reads the policy decision and returns only the smallest useful power. If the model asks for something outside the card, the answer is deny.

### 6. Secrets, data, and sandboxes stay isolated by tenant

Three platforms hold the agent away from danger. The **Secret Broker** hands short-lived credentials directly to a protected adapter, not to the model or the browser. The **Tenant Data Plane** keeps rows, indexes, caches, queues, artifacts, and telemetry separated by tenant at every layer. The **Sandbox** runs code, browser, file, and MCP App previews in scoped, ephemeral environments with limited CPU, memory, lifetime, network, and file access. Together they mean a malicious attachment can be parsed, rendered, and summarized without gaining a path to host files, credentials, other customers' data, or unrestricted network. The tenant key travels with the identity, the data, the work, and the evidence.

### 7. Governance and accountability close the loop

![A governance table assigns owners, operators, reviewers, approvers, and accountable executives to risks, controls, evidence, incidents, exceptions, and deployments; exceptions require reason, scope, compensating controls, expiry, monitoring, and approval, while an escalation ladder rises from the agent through on-call, security, privacy, and finance to an accountable executive.](../diagrams/171-roles-exceptions-accountability-review.png)

The outer **Governance Loop** is **GOVERN · MAP · MEASURE · MANAGE**. It is the reminder that the architecture is never finished. New models, new attack patterns, new partners, and new regulations change the context, so the controls must be reviewed on a schedule or after a trigger. Diagram 171 shows the same idea from an organizational angle: a **Governance Table** assigns **Owner**, **Operator**, **Reviewer**, **Approver**, and **Accountable Executive** to every risk, control, evidence set, incident, exception, and deployment. Exceptions are not permanent sticky notes; they require reason, scope, compensating controls, expiry, monitoring, and approval. The **Escalation Ladder** rises from the agent through on-call, security, privacy, and finance to the accountable executive. The gateway is a technical expression of that accountability structure.

### 8. Egress, discovery, and provenance guard the outer edges

Before any outbound call, the **Egress Gate** checks the resolved destination, allowlist, method, path template, tenant, purpose, data class, payload, and rate. It does not accept a model-generated URL. **Discovery Trust** inspects MCP `server/discover` responses and A2A Agent Card metadata before sending credentials or delegating work; origin, TLS, signature, issuer, expiry, policy, and prior approved state all matter. **Provenance** records the source commit, dependency lock, build attestation, container digest, model identifier, prompt version, tool schema, policy version, configuration hash, and discovery snapshot that produced a run. These three controls prevent the agent from becoming an unwitting bridge to untrusted endpoints, from believing unverified remote claims, and from running without a traceable origin.

### 9. Audit evidence makes the system reviewable

The **Audit Evidence** platform emits structured events for input received, identity verified, policy decision, tool denied, approval, action, receipt, and review. Each event carries time, actor, tenant, resource, action, result, reason, policy, correlation, and a previous hash. Sensitive payloads are redacted before the general telemetry path; sealed evidence is stored separately with purpose-bound access. If an event is deleted or edited, the hash chain breaks and the system alerts. This makes the safe refund reviewable and every hostile branch explainable. Without this evidence, a denial looks arbitrary and a successful refund looks unexplainable.

### 10. MCP and A2A are distinct but share the same policy center

The **MCP Server** and **A2A Agent** are not inside the trust zone. They connect through controlled edges. MCP 2026-07-28 uses `server/discover`, and A2A 1.0 uses `/.well-known/agent-card.json`, but both must pass through the same **Identity and Tenant Gate**, **Policy Decision**, **Capability Broker**, **Secret Broker**, and **Egress Gate**. The gateway does not trust a remote party just because it can speak a protocol. Discovery is a claim, not an authorization. A2A delegation preserves the same subject, actor, tenant, audience, and scope semantics as an MCP tool call. The policy center is protocol-agnostic; it cares about who is asking, what they want to do, and whether the action is allowed.

### 11. The Next.js and Python maps implement the same model in code

In **Next.js**, the work belongs in App Router server boundaries that resolve security context, policy, approval, tool mediation, evidence, and operator views. Tokens, policy decisions, secrets, and privileged mutations stay in authenticated server code, and the browser receives only the minimum display state. Typed request, decision, denial, approval, and receipt records let the React interface explain security state without inventing it. In **Python**, FastAPI and worker services use Pydantic models and explicit middleware or service boundaries for identity, tenant, policy, data classification, and audit context. The two stacks share the same fixtures so that a TypeScript Route Handler and a Python dependency make identical security decisions for the same case. The architecture is framework-neutral; the contracts are portable.

### 12. Graduation evidence, not the diagram, proves the capstone works

The diagram explains the design, but the system is not finished until it produces repeatable evidence. The lab prompt asks for a complete framework-neutral capstone contract: components, identities, tenants, tokens, policies, tools, data classes, sandboxes, egress, discovery, provenance, audit, privacy, governance, 30 negative tests, and graduation evidence. The checkpoint asks what proves the capstone works, and the answer is the evidence—repeatable allow and deny tests, policy and action receipts, isolation checks, incident drills, and governance review evidence—not the picture. That is the final lesson of the volume: security is a connected system of identity, authority, containment, data control, evidence, and accountable review.

---

## Case study — Maya's refund, the attachment, and the unknown finance agent

Maya asks Acme to refund a legitimate payment and uploads a vendor attachment. The attachment contains the invoice, but it also tries four hostile things: it asks the agent to export the payment API key, it asks the agent to redirect the refund to a new account, it asks the agent to fetch a "verification" URL that redirects to an attacker server, and it points to an unknown A2A "finance agent" that claims it can speed up the refund.

The **Identity and Tenant Gate** resolves Maya, the Acme client, the Acme agent, the payment workload, and the intended payment resource. The attachment remains evidence-bearing untrusted data. It is never allowed to influence instruction authority. **Instruction Authority** keeps Maya's verified refund request separate from the file's text. The **Policy Decision** platform evaluates the case, the amount, the original payee, the requested destination, and the risk signals. The malicious destination fails egress policy, the unknown A2A agent fails discovery trust, and the credential request fails because the agent has no tool that returns secrets.

For the legitimate refund, **Approval Binding** creates a transaction hash over the exact payee, amount, currency, and destination. Maya and a supervisor approve that hash. The **Capability Broker** returns a narrow `issueApprovedRefund` card tied to one case and one operation. The **Secret Broker** gives a short-lived credential directly to the payment adapter. The **Tenant Data Plane** ensures the case and the refund stay inside Maya's tenant. The **Sandbox** contains the attachment parsing. The **Egress Gate** allows only the approved payment provider. The **Provenance** platform records the build, model, prompt, tool, policy, and configuration identifiers for the run. The **Audit Evidence** platform writes a tamper-evident chain from intake through the policy decision, approval, action, and receipt.

The result: Maya receives the correct refund, and Acme can prove why the safe path was allowed and why every hostile branch was denied.

The danger is a decorative gateway that does not enforce policy at the protected resource. A dashboard in front of unchanged broad tools and data paths is theater, not security.

The takeaway: security is a connected system of identity, authority, containment, data control, evidence, and accountable review.

---

## Composition

The diagram is a single-page architecture map. On the left, **Maya** and the **Acme operators** stand outside the main trust zone. They enter through the **Identity and Tenant Gate**. In the center, a large cobalt platform reads **Secure Agent Gateway**. Around it, smaller cobalt platforms hold **Instruction Authority**, **Policy Decision**, **Capability Broker**, **Approval Binding**, **Secret Broker**, **Tenant Data Plane**, **Sandbox**, **Egress Gate**, **Discovery Trust**, **Provenance**, and **Audit Evidence**.

A teal arrow leaves the gateway toward a **Safe Refund** white card and a **Receipt**. Coral arrows leave an untrusted **Malicious Attachment** toward **Untrusted Data**, **Quarantine**, **Deny**, **Redact**, and **Step Up**. An **MCP Server** and an **A2A Agent** connect through controlled edges above the gateway. A large outer arc reads **GOVERN · MAP · MEASURE · MANAGE**, forming the Governance Loop.

## Element by element

- **Maya** — the human customer whose request starts the flow.
- **Acme operators** — the people who diagnose, approve, or recover agent work.
- **Identity and Tenant Gate** — resolves and separates human, client, agent, workload, operator, and resource identities and tenants.
- **Secure Agent Gateway** — the logical boundary where the coordinated controls meet.
- **Instruction Authority** — the trusted sources the system is allowed to obey.
- **Policy Decision** — the versioned policy engine that returns allow, deny, redact, step-up, or quarantine plus a receipt.
- **Capability Broker** — the service that hands out one narrow capability card at a time.
- **Approval Binding** — the mechanism that ties human approval to the exact transaction hash.
- **Secret Broker** — the service that provides short-lived credentials directly to adapters, never to the model.
- **Tenant Data Plane** — the cross-layer isolation that keeps rows, indexes, caches, queues, artifacts, and telemetry separated by tenant.
- **Sandbox** — the containment layer for code, browser, file, and MCP App execution.
- **Egress Gate** — the policy-aware control for outbound network requests.
- **Discovery Trust** — the evaluation of MCP and A2A remote metadata before credential or delegation.
- **Provenance** — the record of build, model, prompt, tool, policy, configuration, and discovery versions.
- **Audit Evidence** — the tamper-evident chain of security events.
- **MCP Server** — a connected Model Context Protocol resource.
- **A2A Agent** — a connected agent-to-agent party.
- **Malicious Attachment** — the untrusted document that tries to redirect the agent.
- **Untrusted Data** — the classification of external content before it is granted authority.
- **Quarantine** — the safe holding area for suspicious content and evidence.
- **Deny / Redact / Step Up** — the allowed responses to risky requests.
- **Safe Refund** — the allowed business outcome.
- **Receipt** — the durable, attributable evidence of an allow or deny.
- **Governance Loop** — the outer GOVERN · MAP · MEASURE · MANAGE cycle.

---

## Colour and flow semantics

The course visual grammar applies directly.

- **Cobalt platform** — a protected identity, policy, tenant, resource, sandbox, or governance boundary. The Identity and Tenant Gate, Secure Agent Gateway, Policy Decision, Capability Broker, and the rest of the named platforms are cobalt.
- **Cyan arrow** — a request, delegated authority, tool call, or intended data path. The flow from Maya and the operators through the gateway to the control platforms and on to the Safe Refund is cyan.
- **Teal arrow** — a verified identity, allowed decision, safe result, receipt, evidence, or review path. The Safe Refund and the Receipt are teal.
- **Coral path** — an injection, replay, privilege error, data leak, denial, quarantine, exception, or residual risk. The Malicious Attachment and its branches to Deny, Redact, Step Up, and Quarantine are coral.
- **White card** — an identity, token, claim, policy, tenant key, approval, artifact, audit event, or evidence record. Capability cards, the Safe Refund, the Receipt, and the governance exceptions are white cards.

The overall flow moves from authenticated actors on the left, through identity and policy, into the protected control platforms, and out to a teal safe result. Untrusted content and unapproved paths are shown as coral branches that end in controls, not in consequences.

---

## How to present it

- **Start with the airport analogy.** Ask the room to name the checkpoints an airport uses to keep passengers, crew, baggage, and planes safe. Then map each checkpoint to a platform on the diagram: identity, ticket, baggage screening, restricted doors, customs, air-traffic control, flight records.
- **Point at the Secure Agent Gateway and the surrounding platforms.** Ask which of these controls already exist in their stack and which are missing. The answer usually reveals a gateway that is really just a proxy.
- **Trace the teal path.** Walk from Maya and the operators through the Identity and Tenant Gate, into Policy Decision, through Capability Broker, Approval Binding, Secret Broker, Tenant Data Plane, and out to Safe Refund and Receipt. Ask who owns each step.
- **Trace the coral paths.** Show how the Malicious Attachment can branch to Untrusted Data, Quarantine, Deny, Redact, or Step Up. Ask whether a document in their system can currently change a payee, request a secret, or choose a destination.
- **Point at the second image, Diagram 171.** Explain that the Governance Loop is not a decoration. It needs owners, operators, reviewers, approvers, exceptions with expiry, and an escalation ladder. A gateway without governance becomes a one-time drawing.
- **Emphasize the protocol edges.** MCP and A2A are not trusted because they exist. They must pass the same identity, policy, capability, secret, and egress controls. Discovery is a claim; it must be evaluated.
- **Show the receipt chain.** Every consequential action should produce a policy decision, an approval record, an action record, and a final receipt. Ask what the close receipt for a refund must contain.
- **Use the case study.** The attachment tries four attacks at once. The gateway handles them with separate controls. Ask how many separate controls would be needed in the team's own system to stop the same four attacks.
- **Ask about graduation evidence.** The diagram is not the proof. What are the 30 negative tests? Where are the isolation checks? When is the next governance review? If the team cannot answer, the capstone is not done.
- **Use the lab prompt as a design exercise.** Have the room produce the framework-neutral contract: components, identities, tenants, tokens, policies, tools, data classes, sandboxes, egress, discovery, provenance, audit, privacy, governance, 30 negative tests, and graduation evidence.
- **Mention the sources in context.** The MCP 2026-07-28 specification and security best practices, the A2A 1.0 specification, the NIST AI Risk Management Framework, and the OWASP Agentic Top 10 2026 all describe parts of the same problem. The diagram connects them into one architecture.
- **Close on the takeaway.** Security is a connected system of identity, authority, containment, data control, evidence, and accountable review.

**Timing.** Thirty to thirty-five minutes, or forty-five if the room sketches their own capstone contract.

---

## Lab and checkpoint

**Lab:** Produce the complete framework-neutral capstone contract: components, identities, tenants, tokens, policies, tools, data classes, sandboxes, egress, discovery, provenance, audit, privacy, governance, 30 negative tests, and graduation evidence.

**Checkpoint:** What proves the capstone works: its diagram or its evidence?

**Answer:** The diagram explains the design; repeatable allow and deny tests, policy and action receipts, isolation checks, incident drills, and governance review evidence prove it works.

---

## Glossary

- **Secure gateway** — a coordinated set of enforcement boundaries, not a single service, that protects the path from authenticated intent to protected action.
- **Policy center** — a managed place for versioned policy decisions, decision receipts, obligations, reviews, and governance evidence.
- **Graduation evidence** — the proof required before a system is trusted, including tests, receipts, isolation checks, drills, and governance reviews.

---

## Related lessons

- **Diagram 149 — Assets, Identities, Trust Boundaries, Data Flows, and Owners** (Module 35). The threat-model foundation that names the boundaries the gateway protects.
- **Diagram 165 — MCP Server Discovery, A2A Agent Cards, Signatures, and Trust Decisions** (Module 39). The outer discovery and trust controls for the MCP and A2A edges.
- **Diagram 171 — Roles, Exceptions, Escalation, Accountability, and Review** (Module 40). The governance, exception, and escalation structure that sits outside the gateway.

---

## Sources

- MCP 2026-07-28 specification
- MCP security best practices
- A2A Protocol 1.0 specification
- NIST AI Risk Management Framework
- OWASP Agentic Top 10 2026
