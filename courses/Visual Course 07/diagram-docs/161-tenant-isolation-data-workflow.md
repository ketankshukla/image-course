# Diagram 161 — Tenant Isolation Through Every Data and Workflow Layer

![On dark navy, two vertical lanes run side by side: a blue lane for Tenant A on the left and a violet lane for Tenant B on the right. Each lane contains a sequence of cobalt platforms: IDENTITY GATE, API, POLICY, DATABASE ROWS, VECTOR INDEX, WORKFLOW, TOOL, ARTIFACT, and AUDIT. Every platform carries a small white TENANT KEY card. Cyan arrows carry requests down each lane; teal arrows carry safe results and evidence back. A coral arrow attempts to cross from the Tenant A lane to the Tenant B lane at the POLICY layer, but POLICY, ROW FILTER, INDEX FILTER, and RESOURCE CHECK block it with a red X. On the right side, an OPERATOR ACCESS path with a STEP UP icon leads to a privileged view that still respects tenant scope.](../diagrams/161-tenant-isolation-data-workflow.png)

**Module:** Isolation, sandboxing, and egress  
**Role in the course:** how to carry tenant identity through every layer instead of relying on one login-time filter  
**Stability:** Core multi-tenant security contract  
**Layout:** two vertical tenant lanes in blue and violet, a sequence of cobalt platforms from IDENTITY GATE through API, POLICY, DATABASE ROWS, VECTOR INDEX, WORKFLOW, TOOL, ARTIFACT, and AUDIT, each carrying a TENANT KEY, with a coral cross-tenant arrow blocked by POLICY, ROW FILTER, INDEX FILTER, and RESOURCE CHECK, and an OPERATOR ACCESS path with STEP UP on the side.

---

## At a glance

**TENANT A (blue lane) and TENANT B (violet lane)** both move through the same stack: **IDENTITY GATE → API → POLICY → DATABASE ROWS → VECTOR INDEX → WORKFLOW → TOOL → ARTIFACT → AUDIT**.

Every object in the stack carries a **TENANT KEY**.

A **CROSS-TENANT** request is stopped by **POLICY**, **ROW FILTER**, **INDEX FILTER**, and **RESOURCE CHECK**.

**OPERATOR ACCESS** with **STEP UP** still follows the same tenant rules.

An apartment building shares elevators and pipes, but every door, mailbox, meter, lease, and maintenance record still belongs to one apartment.

---

## What the diagram teaches

### 1. A tenant is an owner identity, not just a customer label

A tenant is one customer or organization sharing the service. It is not a marketing segment or a string passed in a form. Tenant isolation means its identities, rows, embeddings, work items, tools, artifacts, logs, keys, quotas, retention, and deletion cannot mix with another tenant's.

The diagram makes the tenant an owner identity that travels. Tenant A and Tenant B are not just colors; they are authoritative contexts that determine whether every later access is legitimate.

### 2. The tenant key must come from trusted identity, not from the request

The tenant key comes from verified identity and authoritative resource ownership, not from an editable `tenant_id` field in JSON. Just because the user is authenticated does not mean the API can trust a tenant ID the client submitted.

The IDENTITY GATE is the first platform in the lane for a reason. It resolves who is asking and which organizations that identity is allowed to represent. Everything downstream derives from that resolution.

### 3. Isolation has to hold at every layer, not just the API

The diagram lists nine layers: IDENTITY, API, POLICY, DATABASE ROWS, VECTOR INDEX, WORKFLOW, TOOL, ARTIFACT, and AUDIT. A cross-tenant leak can happen at any one of them. A tenant filter at the API will not help if the vector index returns embeddings from another tenant, or if an artifact download URL is guessable, or if an audit log records raw customer content from a different organization.

Each layer is a separate chance to enforce the tenant key. The system is only as isolated as the weakest of those layers.

### 4. Every protected object has one authoritative tenant owner

The safety rule is: every protected object has one authoritative tenant owner, and every access verifies that owner against trusted caller context. Database rows, queue messages, vector namespaces, cache entries, files, and receipts all belong to one tenant.

This means the tenant key is a property of the object, not a parameter of the query. A query that does not include the tenant predicate should be impossible to express, not just conventionally avoided.

### 5. Row filters and index filters must be enforced by the server

**DATABASE ROWS** and **VECTOR INDEX** are shown as separate platforms because both need server-side tenant predicates. A client-side filter is not isolation. A repository that expects the application to remember the tenant clause is one bug away from returning the wrong rows.

Row-level security in the database and namespace or filter constraints in the vector store make the tenant boundary part of the storage contract. The same applies to search indexes, caches, queues, and blob paths: the tenant must be unforgeable and unavoidable.

### 6. Workflows, tools, and artifacts carry the tenant key too

The **WORKFLOW**, **TOOL**, and **ARTIFACT** platforms are inside the lane because work items, tool calls, and generated files all operate within one tenant. A workflow step that picks up a queue item must verify the tenant of that item before it acts. A tool call must include the tenant in its authorization context. An artifact must be stored under a tenant-scoped path and served through a tenant-bound URL.

This is where agents are especially dangerous. A model may produce a tool call that looks reasonable but references an identifier from the wrong tenant. The tool layer must re-verify the tenant before executing.

### 7. Tenant isolation is the continuation of the trust-boundary map

![Maya and an Acme agent stand outside the ACME TRUST ZONE. An IDENTITY GATE and a POLICY GATE guard the entrance. Inside are protected asset cards for PAYMENT TOOL, CASE DATA, SECRET VAULT, and AUDIT EVIDENCE, each paired with an OWNER icon. Cyan arrows show USER INTENT, DELEGATED REQUEST, TOOL CALL, and DATA RETURN. A TENANT BOUNDARY encloses the zone and a PAYMENT BOUNDARY wraps the payment tool. Two coral blocks for INTERNET and VENDOR FILE sit below the boundary with red X marks, showing untrusted external sources kept out.](../diagrams/149-asset-identity-trust-boundary-map.png)

Diagram 149 drew the museum floor plan: assets, identities, trust boundaries, data flows, and owners. Diagram 161 takes the same idea and turns the tenant boundary into a continuous thread. The TENANT BOUNDARY in Diagram 149 becomes the TENANT KEY that follows the data through every layer in this diagram. The policy gate from the earlier picture reappears as the POLICY, ROW FILTER, INDEX FILTER, and RESOURCE CHECK that block the cross-tenant arrow.

The second image is a reminder that isolation does not start with a database query. It starts with a clear picture of what belongs to whom.

### 8. Operator access also carries tenant scope and step-up

The **OPERATOR ACCESS** path with **STEP UP** on the right side is important. Support staff and administrators must not become a universal bypass. Their view is still scoped to a tenant, and it requires a stronger proof of identity and purpose.

Step-up means the operator must re-authenticate or re-approve before accessing high-risk tenant data. The tenant key in the operator view comes from the same trusted sources as the customer view, not from a dropdown in the support dashboard.

### 9. Tenant context must be tested for missing, changed, conflicting, and stale values

The trace ends with testing missing, changed, conflicting, stale, and operator tenant context at every layer. This is the adversarial part of the design. A request with no tenant key should fail. A request with a tenant key that does not match the authenticated identity should fail. A queue item with a tenant key that conflicts with the workflow should fail. A cache entry with a stale tenant context should be a miss, not a hit.

Negative tests are as important as positive tests. Every layer should have a cross-tenant denial case that proves the filter works.

### 10. Documents, retrieved text, and model output remain data until a control grants authority

The explanation repeats a course-wide rule: treat documents, retrieved text, model output, tool descriptions, remote cards, and external results as data until a trusted control deliberately grants them authority. A malicious document cannot declare which tenant it belongs to. A vector result cannot choose its own tenant filter. A model-generated tool call cannot override the tenant key.

The POLICY and RESOURCE CHECK platforms exist because data is not authority. Only a trusted control can bind a request to a tenant and allow it to proceed.

### 11. The Next.js and Python maps turn the diagram into code

In a Next.js application, the tenant is resolved from the authenticated server session and route parameters together, then passed as a server-created `TenantContext` to repositories and actions. Tokens, policy decisions, secrets, and privileged mutations stay in server code. The browser receives only the minimum display state. Typed request, decision, denial, approval, and receipt records let the React interface explain the security state without inventing it.

In a Python application, `TenantContext` is required in repository and service interfaces so unscoped reads are difficult to express. Pydantic models and explicit middleware keep identity, tenant, policy, data classification, and audit context separate. Database row-level security is added where supported. Tests run both allowed and deny paths with hostile synthetic fixtures and dependency-injected identity, policy, storage, secret, and network adapters.

### 12. This is a security contract, not a promise that a model will behave

The central message of the diagram is that isolation is a contract enforced by controls, not an assumption that the model will stay within its lane. Models can be confused, jailbroken, or misled by content. The system must verify the relevant identity and tenant, evaluate narrow authority against current context, constrain data and destinations, and preserve enough evidence to explain both allowed and denied outcomes.

The contract is complete only when every layer can answer: which tenant does this object belong to, which tenant is the caller authorized to represent, and does the requested action keep them matched?

---

## Case study — the cross-tenant payment-history comparison

### What the situation looks like

Maya asks Acme to compare her payment history with another case. The attachment she includes happens to contain a case ID copied from a different Acme customer. A confused or manipulated agent might try to look up that foreign case and answer the comparison.

### Walking through the diagram

- Maya's identity resolves only her Acme tenant. The **IDENTITY GATE** gives the request a TENANT KEY that points to Maya's organization.
- The foreign case ID is submitted to the **API**, but before any data is returned the **POLICY** layer checks authoritative tenant ownership of the requested resource.
- The **DATABASE ROWS** filter applies the tenant predicate. The foreign case does not match Maya's tenant key, so the row is not returned.
- The **VECTOR INDEX** and **ARTIFACT** lookups both include server-enforced tenant filters. A similar-looking embedding or file from another tenant is outside the namespace.
- The denied cross-tenant attempt is recorded in **AUDIT** with the requested resource and the trusted tenant key. No other customer's data is exposed.

### Result

A guessed or injected identifier cannot move the agent across the tenant boundary. Maya gets only her own data, and the other customer's data remains invisible.

### The danger

Filtering the web page but using an unscoped backend query, vector index, queue, or artifact URL still leaks tenant data. One layer of isolation is not enough. The front end can hide a row that the back end returns, the vector index can return an embedding from another namespace, and a direct object URL can bypass the API entirely.

### Takeaway

The tenant key travels with identity, data, work, tools, and evidence. If it does not appear at a layer, that layer is not isolated.

---

## Composition

The picture is arranged as two parallel lanes that share the same horizontal services.

**Left lane — Tenant A (blue):**
- **IDENTITY GATE** — resolves Tenant A identity.
- **API** — receives a tenant-bound request.
- **POLICY** — evaluates the request against Tenant A authority.
- **DATABASE ROWS** — Tenant A row set.
- **VECTOR INDEX** — Tenant A namespace.
- **WORKFLOW** — Tenant A work queue or state.
- **TOOL** — Tenant A capability call.
- **ARTIFACT** — Tenant A output file.
- **AUDIT** — Tenant A evidence stream.

**Right lane — Tenant B (violet):**
- The same sequence of platforms, but each carries the Tenant B key.

**Objects shared across lanes:**
- Each platform has a small white **TENANT KEY** card that is either blue or violet.

**Blocked cross-tenant path:**
- A **CORAL CROSS-TENANT ARROW** tries to move from the Tenant A lane to the Tenant B lane at the POLICY layer.
- **POLICY**, **ROW FILTER**, **INDEX FILTER**, and **RESOURCE CHECK** block it.

**Operator path:**
- **OPERATOR ACCESS** with **STEP UP** appears on the right as a separate, still-tenant-scoped entry point.

## Element by element

**TENANT A** — one customer organization sharing the service, shown in blue.

**TENANT B** — another customer organization, shown in violet.

**IDENTITY GATE** — the control that resolves the caller and their authorized tenants.

**API** — the public or internal entry point that receives a tenant-bound request.

**POLICY** — the control that evaluates what the caller may do with the requested resource in this context.

**DATABASE ROWS** — tenant-scoped records, enforced by repository predicates and row-level security.

**VECTOR INDEX** — tenant-scoped embeddings or search index, enforced by namespace or filter.

**WORKFLOW** — tenant-scoped work items, queue envelopes, or state machine steps.

**TOOL** — an agent capability that re-checks tenant context before execution.

**ARTIFACT** — a generated file, download, or output that is stored under a tenant-scoped path.

**AUDIT** — the evidence stream that records allowed and denied tenant decisions.

**TENANT KEY** — the trusted owner identifier that travels with every object and request.

**ROW FILTER** — a server-side predicate that limits database results to the tenant.

**INDEX FILTER** — a server-side constraint that limits vector or search results to the tenant.

**RESOURCE CHECK** — a final authorization check that the requested resource belongs to the caller's tenant.

**CROSS-TENANT ARROW** — an attempted request that would move data or authority between tenants.

**OPERATOR ACCESS** — a privileged support or administrative view.

**STEP UP** — a stronger re-authentication or approval required for privileged access.

**Tenant** — one customer organization sharing a service.

**Tenant key** — a trusted owner identifier derived from identity and resource ownership.

**Row-level security** — a database-enforced row access policy that applies tenant and authorization predicates.

---

## Colour and flow semantics

The course visual grammar applies directly to this diagram.

- **Cobalt platform** — a protected identity, policy, tenant, resource, sandbox, or governance boundary. IDENTITY GATE, API, POLICY, DATABASE ROWS, VECTOR INDEX, WORKFLOW, TOOL, ARTIFACT, and AUDIT are all cobalt platforms. They are places of protection.
- **Cyan arrow** — a request, delegated authority, tool call, or intended data path. The requests down each tenant lane are cyan arrows because they are active, unverified requests.
- **Teal arrow** — a verified identity, allowed decision, safe result, receipt, evidence, or review path. The safe results and audit evidence returning from each platform are teal.
- **Coral path** — an injection, replay, privilege error, data leak, denial, quarantine, exception, or residual risk. The CROSS-TENANT arrow is coral because it represents an attempted tenant boundary violation.
- **White card** — an identity, token, claim, policy, tenant key, approval, artifact, audit event, or evidence record. The small TENANT KEY labels on each platform are white cards showing the authoritative owner of the object.

The overall flow reads from top to bottom inside each lane. The two lanes are parallel so the viewer can see that both tenants use the same services but never share the objects inside them. The blocked coral arrow at the POLICY layer is the central warning: a request that would move sideways between tenants is denied and recorded.

---

## How to present it

**Start with the apartment-building analogy.** Ask the room how an apartment building keeps people separate. They will name doors, locks, mailboxes, and leases. Then point out that the building also shares elevators, pipes, and Wi-Fi, yet those shared services do not let one resident open another's mailbox. The diagram is the same idea for shared services and tenant data.

**Point at the two lanes and ask which services are shared.** The IDENTITY, API, POLICY, database engine, vector index, workflow, tool, artifact, and audit services are shared. The objects inside them are not.

**Trace one tenant key from top to bottom.** Identity resolves the tenant. API carries it. Policy checks it. Database rows, vector index, workflow, tool, artifact, and audit all enforce it. If any platform is missing the key, the chain is broken.

**Point at the coral cross-tenant arrow and the four blockers.** POLICY, ROW FILTER, INDEX FILTER, and RESOURCE CHECK all deny the cross-tenant request. Ask which of those four the room has today. A team with policy but no row-level security is still vulnerable. A team with row filters but no vector namespace filter is still vulnerable.

**Show Diagram 149 again.** The trust boundary in the earlier picture becomes the tenant key in this one. The IDENTITY GATE and POLICY GATE from Diagram 149 are the first two platforms in the tenant lane. This is how the museum floor plan turns into a multi-layer enforcement story.

**Point at OPERATOR ACCESS and STEP UP.** Support staff and administrators are not exempt. Ask how a support rep switches tenants today. If the answer is a dropdown, there is a design problem. Step-up should re-derive the tenant from trusted identity, not from a UI selection.

**Use the lab as a tracing exercise.** Have the room trace one tenant key through fifteen Acme components. For each component, identify where the key comes from, how it is enforced, what happens if it is missing, and one cross-tenant negative test. Five minutes per component is enough to find gaps.

**Ask the checkpoint question.** May the API trust a `tenant_id` submitted in JSON because the user is authenticated? The answer is no. The tenant must derive or verify against authenticated membership and authoritative resource ownership.

**Mention the related lessons in context.** Diagram 162 continues the same theme into cache, index, queue, artifact, and telemetry isolation. Diagram 167 connects tenant isolation to the privacy data lifecycle. Diagram 149 is the threat-model foundation that makes this picture meaningful.

**Close on the sources.** OWASP Multi-Tenant Security describes the controls that keep tenants separate across an application stack. NIST Zero Trust Architecture describes the principle that no implicit trust should exist simply because a request comes from inside a network.

**Timing.** Twenty to twenty-five minutes, plus five minutes for a component-tracing exercise.
## Lab and checkpoint


**Lab:** Trace one tenant key through fifteen Acme components. For each, identify where it comes from, how it is enforced, what happens if missing, and one cross-tenant negative test.


**Checkpoint:** May the API trust tenant_id submitted in JSON because the user is authenticated?


**Answer:** No. It must derive or verify tenant context against authenticated membership and authoritative resource ownership.

## Glossary

- **Tenant** — one customer organization sharing a service
- **Tenant key** — trusted owner identifier
- **Row-level security** — database-enforced row access policy

## Sources

- OWASP Multi-Tenant Security
- NIST Zero Trust Architecture

