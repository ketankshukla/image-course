# Diagram 170 — OWASP Agentic Top 10 Mapping and Red-Team Coverage

![On dark navy, the ACME AGENT sits at the center of a ring of ten coloured risk tiles: GOAL HIJACK, TOOL MISUSE, IDENTITY ABUSE, SUPPLY CHAIN, CODE EXECUTION, MEMORY POISONING, INSECURE AGENT COMMUNICATION, CASCADING FAILURE, HUMAN TRUST EXPLOITATION, and ROGUE AGENT. Cyan arrows point from each tile toward an inner ring of PREVENT, DETECT, and RESPOND controls. Teal arrows point outward to TEST, EVIDENCE, and OWNER labels. A COVERAGE GRID below the ring highlights gaps, severity, and named remediation owners.](../diagrams/170-owasp-agentic-red-team-coverage.png)

**Diagram number:** 170  
**Slug:** `owasp-agentic-red-team-coverage`  
**Module ID:** `module-40`  
**Module:** Governance and organizational control  
**Stability:** OWASP Agentic Top 10 for 2026  
**Role in the course:** how to use the OWASP Agentic Top 10 as a coverage lens while mapping every category to Acme-specific attacker paths, controls, tests, evidence, and owners  
**Layout:** a central Acme agent, a ring of ten risk tiles, inner PREVENT/DETECT/RESPOND controls, an outer TEST/EVIDENCE/OWNER loop, and a coverage grid that exposes gaps

---

## At a glance

The diagram places **ACME AGENT** at the center and wraps it in ten OWASP Agentic risk categories: **GOAL HIJACK**, **TOOL MISUSE**, **IDENTITY ABUSE**, **SUPPLY CHAIN**, **CODE EXECUTION**, **MEMORY POISONING**, **INSECURE AGENT COMMUNICATION**, **CASCADING FAILURE**, **HUMAN TRUST EXPLOITATION**, and **ROGUE AGENT**.

Each tile is connected to an inner ring of **PREVENT**, **DETECT**, and **RESPOND** controls, and to an outer ring of **TEST**, **EVIDENCE**, and **OWNER**.

The **COVERAGE GRID** at the bottom highlights which categories have real Acme scenarios, layered controls, executable red-team fixtures, and named owners, and which ones are still open.

It is a fire-safety checklist for a building: it names common hazards, but the building still needs its own exits, drills, inspections, and repairs.

---

## What the diagram teaches

### 1. The OWASP Agentic Top 10 is a catalog, not a certificate

OWASP's Agentic Top 10 for 2026 names recurring risk families, but the list itself does not make a system secure. It is a common vocabulary and a coverage lens. The real work is translating each category into one or more Acme-specific attacker or failure stories, mapping layered controls to each story, writing safe red-team fixtures, recording expected allow and deny outcomes, and assigning accountable owners.

The trace for this lesson is the recipe:

1. **Translate each category into one or more Acme-specific attacker or failure stories.**
2. **Map preventive, detective, containment, response, and recovery controls to each story.**
3. **Create safe red-team fixtures at prompt, retrieval, memory, tool, identity, agent, code, and network boundaries.**
4. **Record expected allow and deny outcomes plus evidence required to pass.**
5. **Track uncovered paths, repeated failures, control drift, and remediation owners over time.**

The outcome is to use the OWASP Agentic Top 10 as a coverage lens while keeping concrete threats, controls, and tests specific to Acme.

### 2. Goal hijack: the objective must survive untrusted input

**GOAL HIJACK** is the risk that an attacker-controlled document, prompt, retrieved page, or injected instruction redirects the agent away from the user's real objective. A malicious attachment can ask for the refund to be sent to a new account, a retrieved page can embed an alternate goal, and a hidden instruction can try to override the original request.

Prevention means keeping instruction authority separate from content. User intent, policy, and bound approval are the authoritative sources. Detect means monitoring when an agent's stated goal or planned actions diverge from the original request. Response means quarantining the input, escalating for review, and preventing the action until the goal is re-verified.

### 3. Tool misuse: every tool call is a privileged action

**TOOL MISUSE** is the abuse of a legitimate capability for an unintended purpose. The payment tool can redirect a refund, the search tool can leak across tenants, and the email tool can send sensitive data to the wrong destination. Tools are not neutral; they are authority in a callable shape.

Prevention means capability narrowing, policy evaluation, and approval binding before the tool runs. Detection means observing tool calls that do not match the approved plan, the current tenant, or the user's original intent. Response means blocking the call, revoking the capability, and writing a decision receipt that explains why the call was denied.

### 4. Identity and privilege abuse: who is acting, with whose authority

**IDENTITY ABUSE** is the risk that an agent acts with a confused or overbroad identity. A client, an agent, a workload, a tool, and a human are not interchangeable. A delegated hop must preserve the original actor and tenant, and the authority carried must be narrow and verifiable.

Prevention means strong authentication, audience-aware tokens, and least-privilege scopes at every hop. Detection means flagging identity switches, missing correlation, or tokens that do not match the requested resource. Response means rejecting the request, re-authenticating the actor, and preserving the evidence of the identity failure.

### 5. Supply chain: trust does not inherit from a card or package

**SUPPLY CHAIN** is the risk that an agent relies on discovery information, tools, models, packages, or remote agents that are not what they claim to be. An MCP server description, an A2A Agent Card, a model weight, a container image, or a Python package can be tampered with or simply mis-described.

Prevention means provenance, signing, discovery verification, version pinning, and sandboxed execution. Detection means policy checks on discovered capabilities, hash or signature verification, and alerts for unknown or changed providers. Response means quarantine, revocation of trust, and rollback to a known-good version.

### 6. Unexpected code execution: do not run attacker code in the agent loop

**CODE EXECUTION** is the risk that an agent runs code, a shell command, a browser action, or a file operation that the attacker supplied or shaped. A generated script, a downloaded package, or a sandboxed preview can break out of containment and reach the host, the network, or the secret store.

Prevention means strong sandboxing, network egress allowlists, no secret access from the execution environment, and human approval for any code that crosses a trust boundary. Detection means monitoring for unexpected outbound connections, file system writes, or process spawns. Response means terminating the sandbox, quarantining the artifact, and revoking any short-lived credentials it may have used.

### 7. Memory and context poisoning: the context window is untrusted data, not a control

**MEMORY POISONING** is the risk that retrieved text, past conversation turns, embedded system prompts, or stored facts become instructions without a trusted control. An agent's memory and context are just another data channel. An attacker who can write or retrieve into that channel can change what the agent believes is true, relevant, or authorized.

The previous lesson on attack paths shows exactly how this works. A malicious vendor file does not need to be an executable; it only needs to be parsed, remembered, and treated as authoritative.

![On dark navy, an attacker-controlled MALICIOUS VENDOR FILE enters a CONTENT PARSER and reaches a green AGENT GOAL. From the goal, four coral arrows branch toward SECRET ACCESS, PAYMENT REDIRECT, CROSS-TENANT SEARCH, and ATTACKER EGRESS. Teal controls — AUTHORITY CHECK, TENANT FILTER, APPROVAL BINDING, EGRESS DENY, and AUDIT ALERT — sit along each branch. The legitimate path ends at a green SAFE CASE while the unacceptable outcomes are marked with red blocked symbols.](../diagrams/150-attack-path-misuse-outcome-map.png)

That diagram is the close-up of memory and goal hijacking in Acme. The file's text can influence retrieved content and model context, but it has no instruction authority. The attack-path method applies to the memory-poisoning category too: choose the attacker, trace through parser, prompt, retrieval, memory, tool, approval, storage, and egress, and place preventive, detective, and response controls at each step. Without a concrete path, the category remains a vague worry.

Prevention means separating context from authority, validating memory writes, and treating external content as data until a trusted control grants it authority. Detection means flagging when an agent's plan or recalled facts reference untrusted or anomalous sources. Response means clearing the poisoned context, quarantining the source, and re-grounding the agent from a trusted baseline.

### 8. Insecure agent communication and cascading failure: one agent's lie can spread

**INSECURE AGENT COMMUNICATION** and **CASCADING FAILURE** are two sides of inter-agent risk. Insecure communication means one agent accepts a message, a plan, or a goal from another agent without authentication, authorization, or verification. Cascading failure means one agent's mistake, hallucination, or compromised state is repeated or amplified by downstream agents.

Prevention means authenticated agent-to-agent channels, audience and scope checks on delegated work, and limits on how many hops a sub-goal can travel. Detection means monitoring for loops, repeated errors, sudden changes in agent output quality, or cross-agent messages that do not match the original plan. Response means stopping the chain, isolating the affected agent, and notifying the owner of the originating task.

### 9. Human-agent trust exploitation: the interface must not bypass the policy

**HUMAN TRUST EXPLOITATION** is the risk that the agent's summary, recommendation, or urgency framing misleads a human into approving something harmful. A confident-sounding summary can hide a substituted destination, a fabricated source, or a missing approval. Urgency cues can make a human skip the safety check.

Prevention means transparent summaries that expose sources, reasoning, and policy state; requiring step-up approval for consequential actions; and designing the user interface so that approval is a deliberate act, not a single click. Detection means tracking when users approve actions that deviate from their historical patterns or from the stated policy. Response means pausing the action, offering a clear comparison between the request and the approved plan, and routing to a second approver when the gap is large.

### 10. Rogue agent: an agent operating outside its control plane

**ROGUE AGENT** is the risk that an agent or agent infrastructure operates without the intended governance. It could be a long-running agent that ignores policy updates, a forked instance with stale configuration, an external agent that claims to act on behalf of the organization, or an agent that continues to use a revoked capability.

Prevention means a control plane that issues, refreshes, and revokes capabilities; identity and provenance for every agent instance; and attestation that the agent is running an approved version. Detection means telemetry on agent versions, policy versions, capability grants, and anomalous behavior. Response means revocation of the agent's credentials, quarantine of its outputs, and review of any decisions it made while rogue.

### 11. The coverage grid turns the ring into a release decision

The **COVERAGE GRID** is the final control. It asks, for each category: what is the Acme scenario, what is the boundary, what is the prevention, what is the detection, what is the response, what is the test fixture, what is the evidence, who is the owner, what is the severity, and what is the status?

A category with no scenario, no test, no evidence, or no owner is not covered. The grid makes those gaps visible. A release review should not pass until high-severity gaps have a named owner and a remediation plan. The coverage grid is what turns the OWASP catalog from a poster into a working governance tool.

### 12. Where to start in code

**Next.js.** Create an internal coverage matrix that links each risk to threat fixtures, API test results, policy decisions, UI behavior, evidence, and remediation issues. Keep tokens, policy decisions, secrets, and privileged mutations in authenticated server code; send the browser only the minimum display state. Use typed request, decision, denial, approval, and receipt records so the React interface can explain security state without inventing it.

**Python.** Build a pytest red-team suite with tagged scenarios, deterministic adapters, expected control points, evidence assertions, and safe synthetic payloads. Use Pydantic models plus explicit middleware or service boundaries for identity, tenant, policy, data classification, and audit context. Test allow and deny paths with hostile synthetic fixtures and dependency-injected identity, policy, storage, secret, and network adapters.

---

## Case study — Acme release review, the OWASP coverage check

### Situation

Acme is preparing a release that adds attachment processing, A2A delegation, code previews, and automatic low-value refunds. Before the release, the security and governance team runs an OWASP Agentic Top 10 coverage check.

### Walkthrough

The team translates the ten categories into Acme scenarios:

1. **Goal hijack** is mapped to the malicious vendor attachment that tries to redirect a refund.
2. **Tool misuse** is mapped to the payment tool being called with a substituted account or a missing approval.
3. **Identity abuse** is mapped to an A2A agent that receives delegated work without clear actor, tenant, and audience checks.
4. **Supply chain** is mapped to unverified MCP server descriptions and A2A Agent Cards that the agent might trust.
5. **Code execution** is mapped to the code preview feature that renders or runs untrusted files.
6. **Memory poisoning** is mapped to retrieved pages and past conversation turns that can carry hidden instructions.
7. **Insecure agent communication and cascading failure** is mapped to multiple A2A agents passing plans and results without authentication or scope limits.
8. **Human trust exploitation** is mapped to misleading approval summaries and urgency cues in the operator console.
9. **Rogue agent** is mapped to stale or externally impersonated agent instances that still hold capabilities.

For each scenario, the team lists the boundary, the preventive controls, the detective controls, the response, the test fixture, the evidence location, and the owner.

### Result

The release review blocks on two high-severity gaps. The code preview feature lacks a sandbox-to-tenant egress allowlist, and the A2A delegation path has no audience check on exchanged tokens. Each gap receives a named owner, a compensating control, a test fixture, and a remediation date. The other eight categories pass with evidence attached.

### Danger

Claiming compliance because ten labels appear in a document says nothing about whether an attacker path is blocked or detected. The team could have printed the OWASP list, added a note that the agent is "aligned," and moved on. The coverage grid prevents that by demanding an Acme scenario, a control, a test, evidence, and an owner for every category.

### Takeaway

*Map the catalog to real paths, controls, tests, evidence, and owners.* A category without a test is a belief. A test without evidence is a rumor. Evidence without an owner is an orphan.

---

## Composition

The diagram is organized around a central agent, a ring of risk tiles, an inner control ring, an outer accountability ring, and a coverage grid.

- **Center:** `ACME AGENT` is the protected workload that plans, decides, and acts.
- **Ring of ten risk tiles:** `GOAL HIJACK`, `TOOL MISUSE`, `IDENTITY ABUSE`, `SUPPLY CHAIN`, `CODE EXECUTION`, `MEMORY POISONING`, `INSECURE AGENT COMMUNICATION`, `CASCADING FAILURE`, `HUMAN TRUST EXPLOITATION`, and `ROGUE AGENT`. These are the OWASP Agentic Top 10 categories.
- **Inner ring:** `PREVENT`, `DETECT`, and `RESPOND` controls sit between the category and the agent. They translate the abstract risk into layered safeguards.
- **Outer ring:** `TEST`, `EVIDENCE`, and `OWNER` labels sit outside the category tiles. They connect each risk to accountability.
- **Coverage grid:** a table or panel at the bottom that records scenario, boundary, prevention, detection, response, test, evidence, owner, severity, and status for each category.

The layout reads from the outside in: a category name, then the controls that stop it, then the agent that must remain safe. It also reads from the inside out: every category must be tested, evidenced, and owned.

---

## Element by element

- **ACME AGENT** — the central planning and acting component that is the target of the ten risk categories.
- **GOAL HIJACK** — untrusted input redirecting the agent's objective.
- **TOOL MISUSE** — abuse of a legitimate tool or capability for an unintended purpose.
- **IDENTITY ABUSE** — use of a confused, overbroad, or stolen identity across delegated hops.
- **SUPPLY CHAIN** — reliance on untrusted or unverified discovery information, models, packages, or remote agents.
- **CODE EXECUTION** — running attacker-shaped or attacker-supplied code, scripts, or commands.
- **MEMORY POISONING** — untrusted content entering the agent's context, memory, or retrieved store and being treated as authority.
- **INSECURE AGENT COMMUNICATION** — agent-to-agent messages without authentication, authorization, or scope verification.
- **CASCADING FAILURE** — one agent's error or compromise spreading to downstream agents or actions.
- **HUMAN TRUST EXPLOITATION** — misleading summaries, urgency, or presentation that causes a human to bypass policy.
- **ROGUE AGENT** — an agent operating outside its intended control plane, policy version, or capability grant.
- **PREVENT** — the set of controls that stop the risk before it reaches the agent.
- **DETECT** — the set of controls that observe and alert on attempted or partial exploitation.
- **RESPOND** — the set of controls that contain, quarantine, revoke, or recover from the event.
- **TEST** — the executable red-team or negative test that exercises the control.
- **EVIDENCE** — the durable record that proves the control worked or the failure was handled.
- **OWNER** — the named role accountable for the category, control, test, and remediation.
- **COVERAGE GRID** — the matrix that exposes which categories have scenarios, controls, tests, evidence, and owners.

---

## Colour and flow semantics

- **Cobalt platforms** represent the central agent and the protected governance boundaries around it.
- **Cyan arrows** show the mapping from a risk category to the PREVENT, DETECT, and RESPOND controls that must address it.
- **Teal arrows** show the outward accountability loop from each category to TEST, EVIDENCE, and OWNER.
- **Coral paths or highlights** mark coverage gaps, high-severity risks, and unmapped categories in the COVERAGE GRID.
- **White cards** hold the risk names, control labels, and grid cells that must each be owned and tested.

The visual flow says that every risk must be connected both inward to controls and outward to accountability. A tile with no inward control is undefended. A tile with no outward owner is ungoverned.

---

## How to present it

**Start by asking the room which of the ten categories they have actually tested.** Most teams can name a prompt-injection test. Far fewer can point to a test for identity abuse, supply chain, inter-agent communication, or rogue agents. The diagram's ring makes those gaps visible.

**Trace the ring in order.** Goal hijack, tool misuse, identity abuse, supply chain, code execution, memory poisoning, insecure agent communication, cascading failure, human trust exploitation, rogue agent. For each, ask for one concrete Acme scenario. If the room cannot produce one, that tile is red on the coverage grid.

**Point at the PREVENT / DETECT / RESPOND inner ring.** Ask whether the controls for that category are layered or whether they rely on a single front door. A single prompt saying "be careful" is not a control; a parser, an authority check, a tenant filter, an approval binding, and an egress check together are a control.

**Emphasize the outer ring.** A category without TEST, EVIDENCE, and OWNER is not covered. Ask who owns the supply-chain checks, the agent-to-agent authentication, and the rogue-agent detection. If the answer is "everyone," the answer is no one.

**Show Diagram 150 at point 7.** Explain that memory and context poisoning is not a vague worry about the model; it is a concrete attack path from untrusted content through parser, prompt, retrieval, and tool to an unacceptable outcome. The attack-path method from the previous module is exactly the drill the coverage grid needs.

**Tell the Acme release-review story.** The team mapped the ten categories, found real scenarios, blocked the release on two high-severity gaps, and assigned named owners. The alternative was a compliant-looking document with no evidence.

**Use the lab as a table exercise.** Have the room build a ten-row coverage matrix. For each row, fill in Acme scenario, boundary, prevention, detection, response, test fixture, evidence, owner, severity, and status. This usually reveals at least three red or amber cells.

**Pose the checkpoint.** *"Does passing one prompt-injection test cover all ten categories?"* The answer is no. The categories include identity, tools, supply chain, code, memory, agent communication, cascading behavior, human trust, and rogue behavior too. Passing one test proves one path, not the whole ring.

**Map the conversation to the codebase.** Ask where the coverage matrix lives, whether test fixtures are tagged by OWASP category, and whether a failing test creates a ticket with an owner. If the matrix is in a slide deck, it is not operating.

**Connect to related lessons.** `Diagram 150` is the attack-path foundation. `Diagram 166` covers execution provenance and supply-chain trust. `Diagram 169` covers the NIST AI risk management loop that keeps the coverage grid on a regular review cycle. Together they turn the ring into a governed process.

**Mention the sources in context.** The [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) provides the category definitions, and the [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) provides the broader risk-management framing that makes the coverage grid repeatable.

**Close on the standard.** *Every OWASP Agentic category has an Acme scenario, layered controls, an executable red-team test, durable evidence, and a named owner, or a documented rationale for non-applicability.*

**Timing.** Twenty-five minutes. Thirty if the room builds one row of the coverage matrix for a real release.

---

## Glossary

- **Red team** — authorized adversarial testing that tries to make the system fail in realistic ways.
- **Coverage** — the set of threats, controls, and paths that are actually exercised by tests and evidence.
- **Rogue agent** — agent behavior operating outside the intended control plane, policy version, or capability grant.

---

## Sources

- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
## Lab and checkpoint


**Lab:** Build a ten-row matrix using the exact risk names. Add Acme scenario, boundary, prevention, detection, response, test fixture, evidence, owner, severity, and status.


**Checkpoint:** Does passing one prompt-injection test cover all ten categories?


**Answer:** No. The categories include identity, tools, supply chain, code, memory, agent communication, cascading behavior, human trust, and rogue behavior too.

