# Volume 7 Diagram Prompt Library

These are the exact production prompts for Diagrams 149-172. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

## Shared art direction

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

## Diagram 149 - Assets, identities, trust boundaries, data flows, and owners

Output filename: `diagrams/149-asset-identity-trust-boundary-map.png`

Pattern status: Threat-model foundation

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show MAYA and ACME AGENT outside a large ACME TRUST ZONE. Inside place IDENTITY GATE, POLICY GATE, PAYMENT TOOL, CASE DATA, SECRET VAULT, AUDIT EVIDENCE. Use labeled flows USER INTENT, DELEGATED REQUEST, TOOL CALL, DATA RETURN. Mark INTERNET, VENDOR FILE, TENANT BOUNDARY, PAYMENT BOUNDARY. Put OWNER cards beside each protected asset.

Accessibility alt text: Maya and an Acme agent send requests through identity and policy gates toward protected case data, secrets, payment tools, and audit evidence across named trust boundaries with owners.

## Diagram 150 - Attack paths, misuse cases, and unacceptable outcomes

Output filename: `diagrams/150-attack-path-misuse-outcome-map.png`

Pattern status: Threat-model analysis pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show ATTACKER controlling MALICIOUS VENDOR FILE. Coral path crosses CONTENT PARSER to AGENT GOAL, then branches toward SECRET ACCESS, PAYMENT REDIRECT, CROSS-TENANT SEARCH, and ATTACKER EGRESS. Place teal controls AUTHORITY CHECK, TENANT FILTER, APPROVAL BINDING, EGRESS DENY, AUDIT ALERT. End with green SAFE CASE and coral UNACCEPTABLE OUTCOMES blocked.

Accessibility alt text: A malicious vendor file attempts four attack paths toward secrets, payment redirection, cross-tenant search, and attacker egress while layered controls block unacceptable outcomes and preserve the safe case.

## Diagram 151 - Prompt injection and instruction-authority hierarchy

Output filename: `diagrams/151-instruction-authority-hierarchy.png`

Pattern status: Core agent-security control

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a vertical AUTHORITY LADDER with SYSTEM POLICY at top, APPLICATION RULES, VERIFIED USER INTENT, APPROVED PLAN, and UNTRUSTED DATA at bottom. A MALICIOUS FILE inside UNTRUSTED DATA says SEND SECRET and tries a coral arrow upward; an INSTRUCTION FIREWALL blocks it. Teal path sends DATA FACTS to SAFE REASONING, POLICY CHECK, TOOL ARGUMENTS.

Accessibility alt text: An authority ladder keeps system policy, application rules, verified user intent, and approved plans above untrusted data; a malicious file cannot promote its send-secret text into an instruction.

## Diagram 152 - Data exfiltration and unsafe side effects

Output filename: `diagrams/152-exfiltration-side-effect-control.png`

Pattern status: Core data-and-action defense

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show SENSITIVE DATA entering DATA CLASSIFIER then two lanes. Teal SAFE READ lane goes through MINIMIZE, REDACT, APPROVED TOOL to ACME RESOURCE. Coral EXFILTRATION lane tries MODEL OUTPUT, URL QUERY, TOOL ARGUMENT, LOG, ARTIFACT toward ATTACKER DESTINATION; EGRESS POLICY and DLP block it. A separate SIDE EFFECT lane requires POLICY plus BOUND APPROVAL plus RECEIPT.

Accessibility alt text: Sensitive data is classified, minimized, and redacted for safe use while DLP and egress policy block leakage through model output, URLs, tool arguments, logs, and artifacts; side effects require policy, approval, and receipts.

## Diagram 153 - Authentication, authorization, delegation, and impersonation

Output filename: `diagrams/153-authentication-authorization-delegation.png`

Pattern status: Identity foundation

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show four gates in sequence labeled AUTHENTICATE, AUTHORIZE, DELEGATE, ACT. Identity cards: MAYA, ACME CLIENT, ACME AGENT, PAYMENT WORKLOAD, PAYMENT RESOURCE. A teal chain carries SUBJECT, CLIENT, ACTOR, TENANT, AUDIENCE, SCOPE. A coral IMPERSONATION shortcut skips gates and is blocked. End with DECISION RECEIPT.

Accessibility alt text: Maya, the Acme client, agent, payment workload, and payment resource remain distinct through authentication, authorization, delegation, and action while an impersonation shortcut is blocked.

## Diagram 154 - OAuth, OpenID Connect, resource metadata, and audiences

Output filename: `diagrams/154-oauth-resource-audience-flow.png`

Pattern status: Current MCP authorization profile

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show MCP CLIENT requesting MCP RESOURCE without token. Resource returns 401 plus PROTECTED RESOURCE METADATA. Client discovers AUTHORIZATION SERVER, performs AUTHORIZATION plus PKCE S256, validates ISSUER, requests RESOURCE AUDIENCE, receives ACCESS TOKEN, then calls MCP RESOURCE. Coral WRONG AUDIENCE TOKEN and TOKEN PASSTHROUGH are rejected.

Accessibility alt text: An MCP client discovers protected-resource and authorization-server metadata, uses authorization with PKCE S256, validates issuer and resource audience, then calls the MCP resource while wrong-audience and passthrough tokens are rejected.

## Diagram 155 - DPoP, sender-constrained tokens, and replay resistance

Output filename: `diagrams/155-dpop-sender-token-replay.png`

Pattern status: Stable OAuth standard; active MCP roadmap direction

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show CLIENT KEY creating DPoP PROOF with METHOD, URI, TIME, NONCE, TOKEN HASH. AUTHORIZATION SERVER issues KEY-BOUND TOKEN. MCP RESOURCE verifies TOKEN plus DPoP PROOF plus REPLAY CACHE. Coral attacker steals TOKEN ONLY and attempts REPLAY from NEW KEY; rejected. Teal legitimate retry uses fresh proof.

Accessibility alt text: A client key creates a DPoP proof that binds an access token to request details; the resource verifies proof and replay state, rejecting a stolen token used from another key.

## Diagram 156 - Workload identity, token exchange, and agent delegation

Output filename: `diagrams/156-workload-identity-token-exchange.png`

Pattern status: Stable standards plus evolving MCP agent-identity work

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show MAYA TOKEN entering ACME POLICY but not flowing downstream. ACME AGENT has WORKLOAD IDENTITY from TRUST DOMAIN. A TOKEN EXCHANGE gate receives SUBJECT AUTHORITY plus ACTOR ID plus TARGET AUDIENCE plus NARROW SCOPE and returns DELEGATED TOKEN to PAYMENT RESOURCE. Coral FULL USER TOKEN COPY is blocked. Include DELEGATION RECEIPT.

Accessibility alt text: Maya's token stops at Acme policy while an authenticated Acme workload exchanges bounded subject authority and actor identity for a narrow payment-resource token, blocking full user-token copying.

## Diagram 157 - Least-privilege tool and capability design

Output filename: `diagrams/157-least-privilege-capability-tools.png`

Pattern status: Core secure-tool pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show broad ADMIN TOOL as a large coral key rejected. Beside it, four narrow capability cards: READ CASE, EXTRACT INVOICE, QUOTE REFUND, ISSUE BOUND REFUND. Each card has TENANT, RESOURCE, ACTION, LIMIT, EXPIRY, DESTINATION. A CAPABILITY BROKER gives only one card to AGENT. POLICY and RECEIPT surround the high-impact tool.

Accessibility alt text: A broad administrator tool is rejected while a capability broker gives an agent one narrow card for a tenant, resource, action, limit, expiry, and destination, with policy and receipts around high-impact use.

## Diagram 158 - Policy as code, claims, context, and decision receipts

Output filename: `diagrams/158-policy-context-decision-receipt.png`

Pattern status: Mature authorization pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show POLICY ENFORCEMENT POINT collecting SUBJECT, ACTOR, TENANT, RESOURCE, ACTION, DATA CLASS, DESTINATION, RISK, APPROVAL. It sends INPUT to POLICY DECISION POINT with VERSIONED POLICY. Outputs ALLOW, DENY, STEP UP, REDACT plus OBLIGATIONS. A DECISION RECEIPT records INPUT HASH, POLICY VERSION, RESULT, REASONS, TIME.

Accessibility alt text: A policy enforcement point collects identity, tenant, action, data, destination, risk, and approval context for a versioned policy decision that returns allow, deny, step-up, or redact plus a decision receipt.

## Diagram 159 - Step-up authorization, approval, and transaction binding

Output filename: `diagrams/159-step-up-approval-transaction-binding.png`

Pattern status: High-impact action control

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show PROPOSED REFUND card with TENANT, CASE, PAYEE, AMOUNT, CURRENCY, DESTINATION, DATA. RISK ENGINE sends STEP UP to MAYA plus SUPERVISOR. Their APPROVAL signs TRANSACTION HASH plus EXPIRY. Teal exact transaction reaches PAYMENT TOOL. Coral changed PAYEE or AMOUNT creates HASH MISMATCH and APPROVAL STALE.

Accessibility alt text: A proposed refund is bound to tenant, case, payee, amount, currency, destination, and data; Maya and a supervisor approve its transaction hash, while any material change invalidates the approval.

## Diagram 160 - Secret managers, short-lived credentials, and rotation

Output filename: `diagrams/160-secret-manager-short-lived-credentials.png`

Pattern status: Mature secrets-management practice

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show AGENT and MODEL outside SECRET VAULT. WORKLOAD IDENTITY calls CREDENTIAL BROKER with TARGET, PURPOSE, POLICY, TTL. Broker returns SHORT-LIVED HANDLE directly to TOOL ADAPTER, not to model. ROTATION LOOP replaces credential. Coral ENV FILE, PROMPT, LOG, ARTIFACT copies flow to QUARANTINE. Include ACCESS RECEIPT.

Accessibility alt text: An authenticated workload uses a credential broker to give a short-lived secret handle directly to a tool adapter while the model never sees the secret; rotation and quarantine handle exposure paths.

## Diagram 161 - Tenant isolation through every data and workflow layer

Output filename: `diagrams/161-tenant-isolation-data-workflow.png`

Pattern status: Core multi-tenant security contract

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show TENANT A in blue lane and TENANT B in violet lane from IDENTITY GATE through API, POLICY, DATABASE ROWS, VECTOR INDEX, WORKFLOW, TOOL, ARTIFACT, AUDIT. Each object carries TENANT KEY. A coral CROSS-TENANT arrow is stopped by POLICY plus ROW FILTER plus INDEX FILTER plus RESOURCE CHECK. Include OPERATOR ACCESS with STEP UP.

Accessibility alt text: Tenant A and Tenant B remain in separate lanes through identity, API, policy, database, vector index, workflow, tools, artifacts, and audit while layered checks stop a cross-tenant path.

## Diagram 162 - Cache, index, queue, artifact, and telemetry isolation

Output filename: `diagrams/162-cache-index-queue-artifact-telemetry-isolation.png`

Pattern status: Cross-layer isolation pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a CENTRAL TENANT CONTEXT issuing scoped keys to CACHE KEY, VECTOR NAMESPACE, QUEUE ENVELOPE, ARTIFACT PATH, TRACE ATTRIBUTE, METRIC LABEL, LOG VIEW. Blue TENANT A and violet TENANT B values stay separate. Coral UNSCOPED KEY, SHARED RESULT, GUESSABLE URL, RAW LOG are blocked by VALIDATOR, ACCESS CHECK, REDACTION.

Accessibility alt text: Central trusted tenant context scopes cache keys, vector namespaces, queue envelopes, artifact paths, traces, metrics, and logs while unscoped keys, shared results, guessable URLs, and raw logs are blocked.

## Diagram 163 - Sandboxed code, browser, file, and MCP App execution

Output filename: `diagrams/163-sandbox-code-browser-file-mcp-app.png`

Pattern status: Core containment pattern; MCP Apps profile-specific

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show four separate sandboxes: CODE VM, BROWSER SESSION, FILE WORKSPACE, MCP APP IFRAME. Each has CPU, MEMORY, TIME, FILE, NETWORK, ORIGIN, PERMISSION limits. INPUT enters through SCAN plus CLASSIFY. OUTPUT exits through VALIDATE plus DLP. Coral HOST FILE, LOCAL CREDENTIAL, TOP NAVIGATION, ARBITRARY NETWORK attempts hit sandbox walls.

Accessibility alt text: Code, browser, file, and MCP App execution run in separate sandboxes with resource, file, network, origin, and permission limits; scanning and output validation block host access and arbitrary network behavior.

## Diagram 164 - Network egress, destination allowlists, and DLP

Output filename: `diagrams/164-network-egress-allowlist-dlp.png`

Pattern status: Core outbound-control pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show AGENT TOOL REQUEST entering EGRESS GATE. Gate checks DNS and IP, DESTINATION ALLOWLIST, METHOD, PATH TEMPLATE, TENANT, PURPOSE, DATA CLASS, PAYLOAD DLP, RATE. Teal routes reach ACME API and APPROVED PAYMENT API through controlled adapters. Coral routes to PRIVATE IP, METADATA, REDIRECT, NEW DOMAIN, SECRET PAYLOAD go to DENY plus ALERT.

Accessibility alt text: An egress gate checks resolved destination, allowlist, method, path, tenant, purpose, data class, payload, and rate before approved APIs, denying private addresses, metadata, redirects, new domains, and secret payloads.

## Diagram 165 - MCP server discovery, A2A Agent Cards, signatures, and trust decisions

Output filename: `diagrams/165-mcp-discovery-a2a-card-trust.png`

Pattern status: Current MCP 2026-07-28 · A2A 1.0

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show two discovery lanes. MCP CLIENT sends server/discover to MCP SERVER and receives VERSION, CAPABILITIES, INSTRUCTIONS, RESOURCES. A2A CLIENT fetches /.well-known/agent-card.json and receives SKILLS, ENDPOINTS, SECURITY, SIGNATURES. Both enter TRUST EVALUATOR checking ORIGIN, TLS, SIGNATURE, ISSUER, EXPIRY, POLICY, CHANGE. Outputs TRUST, LIMIT, REVERIFY, REJECT.

Accessibility alt text: MCP server discovery and A2A Agent Card discovery feed a trust evaluator that checks origin, transport, signatures, issuer, expiry, policy, and change before trusting, limiting, reverifying, or rejecting the remote party.

## Diagram 166 - Dependency, model, prompt, tool, and configuration provenance

Output filename: `diagrams/166-execution-provenance-supply-chain.png`

Pattern status: Supply-chain assurance pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a PROVENANCE GRAPH feeding one AGENT EXECUTION: SOURCE COMMIT, DEPENDENCY LOCK, BUILD ATTESTATION, CONTAINER DIGEST, MODEL ID, PROMPT VERSION, TOOL SCHEMA, POLICY VERSION, CONFIG HASH, DISCOVERY SNAPSHOT. TRUSTED BUILD plus DEPLOY APPROVAL lead to RUN RECEIPT. Coral UNKNOWN PACKAGE, CHANGED PROMPT, UNPINNED TOOL go to QUARANTINE.

Accessibility alt text: Source, dependencies, build attestations, container, model, prompt, tool, policy, configuration, and discovery versions form a provenance graph leading to a run receipt while unknown or unpinned inputs are quarantined.

## Diagram 167 - Data minimization, retention, consent, and deletion

Output filename: `diagrams/167-privacy-data-lifecycle.png`

Pattern status: Privacy engineering foundation

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show PERSONAL DATA entering PURPOSE GATE and MINIMIZE. Approved fields flow through USE, STORE, SHARE, RETAIN, DELETE, VERIFY DELETION. Each card has TENANT, PURPOSE, CONSENT or LEGAL BASIS, CLASS, OWNER, RETENTION. Coral EXTRA FIELDS, PURPOSE DRIFT, FOREVER MEMORY, SHADOW COPY are blocked. Include DELETION RECEIPT across DATABASE, VECTOR, CACHE, ARTIFACT, LOG.

Accessibility alt text: Personal data passes purpose and minimization gates through use, storage, sharing, retention, deletion, and verified downstream deletion while extra fields, purpose drift, forever memory, and shadow copies are blocked.

## Diagram 168 - Tamper-evident audit, redaction, and chain of evidence

Output filename: `diagrams/168-tamper-evident-audit-chain.png`

Pattern status: Accountability and incident-evidence pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show ordered AUDIT EVENTS: INPUT RECEIVED, IDENTITY VERIFIED, POLICY DECISION, TOOL DENIED, APPROVAL, ACTION, RECEIPT, REVIEW. Each event has TIME, ACTOR, TENANT, ACTION, RESULT, CORRELATION, PREVIOUS HASH. Raw sensitive payload goes through REDACTION plus SEALED EVIDENCE STORE. HASH CHAIN leads to VERIFY. Coral DELETE or EDIT event breaks chain and alerts.

Accessibility alt text: Ordered identity, policy, tool, approval, action, receipt, and review events form a previous-hash chain; sensitive payloads are redacted into a sealed evidence store and tampering breaks verification.

## Diagram 169 - The NIST AI risk loop in plain English

Output filename: `diagrams/169-nist-ai-risk-loop.png`

Pattern status: NIST AI RMF 1.0; revision underway

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a continuous four-part loop labeled GOVERN, MAP, MEASURE, MANAGE around ACME AGENT SYSTEM. GOVERN connects OWNERS, POLICIES, CULTURE. MAP connects CONTEXT, PEOPLE, IMPACTS, THREATS. MEASURE connects TESTS, METRICS, RED TEAM, UNCERTAINTY. MANAGE connects PRIORITIZE, CONTROL, RESPOND, MONITOR. EVIDENCE REPOSITORY and REVIEW DATE connect all four.

Accessibility alt text: The Acme agent system sits inside a continuous Govern, Map, Measure, Manage loop connected to owners, context, tests, controls, evidence, and review dates.

## Diagram 170 - OWASP Agentic Top 10 mapping and red-team coverage

Output filename: `diagrams/170-owasp-agentic-red-team-coverage.png`

Pattern status: OWASP Agentic Top 10 for 2026

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a ring of ten risk tiles around ACME AGENT: GOAL HIJACK, TOOL MISUSE, IDENTITY ABUSE, SUPPLY CHAIN, CODE EXECUTION, MEMORY POISONING, INSECURE AGENT COMMUNICATION, CASCADING FAILURE, HUMAN TRUST EXPLOITATION, ROGUE AGENT. Each maps inward to PREVENT, DETECT, RESPOND controls and outward to TEST, EVIDENCE, OWNER. A COVERAGE GRID highlights gaps.

Accessibility alt text: Ten OWASP Agentic risk categories surround the Acme agent and map to preventive, detective, and response controls, tests, evidence, owners, and a coverage grid that exposes gaps.

## Diagram 171 - Roles, exceptions, escalation, accountability, and review

Output filename: `diagrams/171-roles-exceptions-accountability-review.png`

Pattern status: Organizational governance pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a GOVERNANCE TABLE with rows RISK, CONTROL, EVIDENCE, INCIDENT, EXCEPTION, DEPLOYMENT and columns OWNER, OPERATOR, REVIEWER, APPROVER, ACCOUNTABLE EXECUTIVE. An EXCEPTION path requires REASON, SCOPE, COMPENSATING CONTROL, EXPIRY, MONITOR, APPROVAL. ESCALATION ladder rises from AGENT to ON CALL to SECURITY plus PRIVACY plus FINANCE to EXECUTIVE. REVIEW LOOP returns to policy.

Accessibility alt text: A governance table assigns owners, operators, reviewers, approvers, and accountable executives to risks, controls, evidence, incidents, exceptions, and deployments; exceptions require scope, compensation, expiry, monitoring, and approval.

## Diagram 172 - Capstone: Acme Secure Agent Gateway and Policy Center

Output filename: `diagrams/172-acme-secure-agent-gateway-policy-center.png`

Pattern status: Capstone architecture

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly agent-security diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal verified identity, permission, receipt, evidence, and safe-result paths, white identity, token, policy, data, task, or evidence cards, selective coral attack, denial, leak, replay, and quarantine paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show MAYA and ACME OPERATORS entering IDENTITY AND TENANT GATE. Center is SECURE AGENT GATEWAY connected to INSTRUCTION AUTHORITY, POLICY DECISION, CAPABILITY BROKER, APPROVAL BINDING, SECRET BROKER, TENANT DATA PLANE, SANDBOX, EGRESS GATE, DISCOVERY TRUST, PROVENANCE, AUDIT EVIDENCE. MCP SERVER and A2A AGENT connect through controlled edges. MALICIOUS ATTACHMENT goes to UNTRUSTED DATA and QUARANTINE. Teal path ends SAFE REFUND plus RECEIPT; coral paths end DENY, REDACT, STEP UP, QUARANTINE. Outer GOVERNANCE LOOP says GOVERN, MAP, MEASURE, MANAGE.

Accessibility alt text: The complete Acme architecture routes Maya and operators through identity and tenant gates into a secure agent gateway coordinating instruction authority, policy, capabilities, approvals, secrets, tenant data, sandboxes, egress, discovery trust, provenance, audit, MCP and A2A, with governance around the system and a safe refund receipt at the end.
