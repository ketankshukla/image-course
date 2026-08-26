# Diagram 157 — Least-privilege tool and capability design

![On dark navy, a large coral key labeled ADMIN TOOL is shown on the left with a red X and a forbidden sign. To the right, four white capability cards sit on a cobalt platform: READ CASE, EXTRACT INVOICE, QUOTE REFUND, and ISSUE BOUND REFUND. Each card lists six fields: TENANT, RESOURCE, ACTION, LIMIT, EXPIRY, DESTINATION. A CAPABILITY BROKER on a cobalt platform selects one narrow card and hands it to an AGENT. POLICY and RECEIPT shields surround the high-impact ISSUE BOUND REFUND tool, while a cyan arrow shows the requested path and a teal arrow shows the allowed, receipt-producing path.](../diagrams/157-least-privilege-capability-tools.png)

**Module:** Capabilities, tools, policy, and secrets  
**Stability:** Core secure-tool pattern  
**Role in the course:** how to shape tools so safe use is the easiest use and a confused agent has little power to misuse  
**Layout:** one rejected broad administrator key, four narrow capability cards, a capability broker, an agent, and policy plus receipt guards around the high-impact tool

---

## At a glance

**ADMIN TOOL is rejected**.

**READ CASE, EXTRACT INVOICE, QUOTE REFUND, and ISSUE BOUND REFUND** are four separate, narrow capability cards.

Each card carries **TENANT, RESOURCE, ACTION, LIMIT, EXPIRY, DESTINATION**.

The **CAPABILITY BROKER** gives the **AGENT** exactly one card for the current job.

**POLICY** and **RECEIPT** surround the high-impact tool.

And the design goal is simple: **make safe use the easiest use**.

---

## What the diagram teaches

### 1. Safe use must be the easiest use

**Shape tools so safe use is the easiest use and a confused agent has little power to misuse.** A safe design makes the default path the model follows the safest one. If safety depends on a careful prompt or a long list of forbidden words, the tool is unsafe. Least-privilege capability design makes the right action obvious and the dangerous action structurally unavailable.

### 2. A tool is a typed contract, not a general API

The diagram contrasts a large **ADMIN TOOL** key with four narrow white cards. The admin tool is a general surface — a shell, SQL console, raw payment API, or unconstrained browser. The cards are typed contracts: **READ CASE** is a read, **EXTRACT INVOICE** a structured extraction, **QUOTE REFUND** a side-effect-free calculation, and **ISSUE BOUND REFUND** a high-impact payment. A tool is safer when its contract expresses one business action with narrow arguments instead of a general-purpose administrator interface.

### 3. Least privilege is architecture, not a prompt instruction

Least privilege means granting only what is needed for the current job. The **AGENT** does not receive the master key with a note to be careful; it receives exactly one card from the **CAPABILITY BROKER** that already carries the limits of the job. This is a security contract, not a promise that a model will behave. The system must verify identity and tenant, evaluate narrow authority against current context, constrain data and destinations, and preserve evidence for both allowed and denied outcomes.

### 4. Split read, propose, approve, execute, and administer

The four cards trace the lifecycle of a safe action. **READ CASE** gathers context, **EXTRACT INVOICE** pulls structured facts, **QUOTE REFUND** proposes a number with no side effect, and **ISSUE BOUND REFUND** executes only after a complete, approved, bounded request. Splitting them means a confused or compromised agent cannot jump directly to execution. It also makes each stage auditable and testable. The mistake is bundling them into one generic admin API.

### 5. Constrain arguments with enums, identifiers, bounds, schemas, and server-side lookups

The six fields on each card — **TENANT, RESOURCE, ACTION, LIMIT, EXPIRY, DESTINATION** — are enforcement, not documentation. The resource should be an explicit identifier or server-side lookup, not a free-form string. The action should be an enum, the destination from an approved list, and the expiry a real time-to-live. When arguments are constrained at the schema and policy layer, the model can only choose valid values and the server can reject anything outside that set before a real effect occurs.

### 6. Attach tenant, audience, purpose, lifetime, rate, amount, and destination limits

A capability card is a portable bundle of authority. **TENANT** stops the tool from acting for the wrong customer, **RESOURCE** stops it touching arbitrary data, and **ACTION** stops a different operation. **LIMIT, EXPIRY,** and **DESTINATION** bound how much, how long, and where. These limits belong to the capability, not the prompt. If the model tries a quote for the wrong tenant or an unapproved destination, the call is denied. Capability design places resource, tenant, action, limits, destinations, lifetime, and obligations close to execution.

### 7. Data cannot authorize itself; a narrow tool still needs an authority ladder

![On dark navy, an AUTHORITY LADDER has SYSTEM POLICY at the top, then APPLICATION RULES, VERIFIED USER INTENT, APPROVED PLAN, and UNTRUSTED DATA at the bottom. A MALICIOUS FILE inside UNTRUSTED DATA says SEND SECRET and tries a coral arrow upward, but an INSTRUCTION FIREWALL blocks it. A teal path sends DATA FACTS to SAFE REASONING, POLICY CHECK, and TOOL ARGUMENTS.](../diagrams/151-instruction-authority-hierarchy.png)

Lesson 151 shows the same idea from the input side. The authority ladder keeps **SYSTEM POLICY**, **APPLICATION RULES**, **VERIFIED USER INTENT**, and **APPROVED PLANS** above **UNTRUSTED DATA**. A malicious file cannot promote its text into an instruction. Pairing that firewall with this diagram means the model can read invoice facts from an uploaded PDF, but those facts cannot rewrite the refund contract. The quote tool has no side effect. The issue tool requires a bound approval. Even if the model is confused, the exposed capability cannot export credentials or redirect arbitrary funds because the capability itself is narrower than any instruction the file could forge.

### 8. Evaluate policy again at execution, not at planning

The model may plan, but the system must decide. The **CAPABILITY BROKER** and the high-impact tool do not trust the model's plan. They re-evaluate policy at the point of execution. **POLICY** and **RECEIPT** surround **ISSUE BOUND REFUND** because the real safety check happens when the effect is about to occur. The broker checks the card, the caller, the tenant, the resource, the approval, the destination, and the expiry. If any field is wrong, the tool returns a denial and a receipt instead of a side effect. Evaluating policy again at execution prevents the model from caching an old decision, replaying a past approval, or using a capability outside its original context.

### 9. Return a typed result or denial plus a durable receipt

The diagram places **RECEIPT** next to the high-impact tool because the answer to a capability call must be evidence, not just a string. A successful call returns a typed result: the refund issued, the operation ID, the amount, the destination, and the time. A denied call returns a typed denial: the requested action, the reason, the policy version, and the decision ID. Both produce a durable receipt. That receipt is what makes the system explainable, auditable, and recoverable. Without a receipt, a denial looks like a model mood and an approval looks like an unaccountable side effect.

### 10. The capability broker is a policy gate, not a convenience router

The **CAPABILITY BROKER** is drawn as a cobalt platform because it is a protected boundary. It is not a thin API wrapper that maps a model request to a backend service. It is a gate that selects, binds, and issues one narrow capability for one context. It knows the actor, the tenant, the task, the approval, and the risk. It may issue a **QUOTE REFUND** card but not an **ISSUE BOUND REFUND** card. It may issue a read-only card to one agent and a payment card to another. Treating the broker as a policy gate changes the way the system is built: it needs an authenticated context, a policy decision point, and a delegation record, not just a route table.

### 11. The Next.js map: narrow server actions and typed records

In the Next.js stack, the pattern becomes narrow Server Actions or Route Handlers such as `quoteRefund` and `issueApprovedRefund` instead of a generic provider request endpoint. Tokens, policy decisions, secrets, and privileged mutations stay in authenticated server code; the browser receives only the minimum display state. The React interface uses typed request, decision, denial, approval, and receipt records to explain the security state without inventing it. The UI does not hold the master key. It displays the card the server selected and shows what is allowed, what is blocked, and what approval is still needed.

### 12. The Python map: typed tool functions behind a capability service

In the Python stack, the pattern becomes small typed tool functions registered behind a capability service. Instead of handing the model a raw payment-provider client, the service injects already-scoped repository or provider adapters. Pydantic models plus explicit middleware enforce identity, tenant, policy, data classification, and audit context. Tests use hostile synthetic fixtures with dependency-injected identity, policy, storage, secret, and network adapters. The unit test is not only the happy path; it is the denial path, the cross-tenant path, the expired-approval path, and the unknown-destination path.

---

## Case study — Acme Refunds, the attachment that wanted an admin tool

Maya has asked for a refund. The vendor PDF she uploaded says, in tiny text or in a natural-looking paragraph, that the agent should run an arbitrary payment-provider API request to complete the refund.

### What the attack needs

The PDF is untrusted content pretending to be authority. To succeed, it needs the agent to have a generic, powerful tool and a prompt that asks the model to be helpful with payment requests. The attachment does not need to hack the model perfectly; it only needs to get the model to produce text that the generic tool will interpret as a valid provider call.

### The capability design

Acme's agent does not have a generic payment-provider tool. It has four narrow capability cards.

- **READ CASE** can read the case record for the authenticated tenant. It has no side effect.
- **EXTRACT INVOICE** can pull structured fields from the uploaded PDF. It returns facts, not authority.
- **QUOTE REFUND** can read approved invoice fields and calculate a refund amount. It also has no side effect.
- **ISSUE BOUND REFUND** can issue a refund, but only with a case, a tenant, an exact bound approval, an amount ceiling, and an operation ID.

When the PDF asks for an arbitrary API request, the model finds no generic provider tool. It may produce the text of a request, but there is no tool that accepts free-form API text. If the attacker tries to route through the issue tool, the call must include the original approved payee, the approved amount ceiling, and an allowed destination. Any unknown destination or unsupported action fails schema and policy before provider access.

### The result

Even if the model's reasoning is confused, the exposed capability cannot export credentials or redirect arbitrary funds. The malicious text becomes preserved evidence of an attempted instruction, while the real refund continues through the narrow, approved path.

### The danger

A powerful generic tool plus a descriptive prompt is still a powerful generic tool when the prompt is bypassed. A prompt that says "be careful" or "do not leak secrets" does not remove the tool's ability to do those things. The only reliable defence is a tool contract that is narrower than the agent's possible mistakes.

### The line in their engineering standard

*Make the tool contract narrower than the agent's possible mistakes.*

---

## Composition

One rejected broad key, four narrow capability cards, a broker, an agent, and guards around the high-impact card.

**Left side:** a large **coral key** labelled **ADMIN TOOL**, with a red X and a forbidden sign.

**Right side:** four **white cards** on a cobalt platform:
- **READ CASE**
- **EXTRACT INVOICE**
- **QUOTE REFUND**
- **ISSUE BOUND REFUND**

Each card lists six fields: **TENANT, RESOURCE, ACTION, LIMIT, EXPIRY, DESTINATION**.

**Centre:** the **CAPABILITY BROKER** on a cobalt platform, selecting and handing one card to the **AGENT**.

**Around the high-impact tool:** a **POLICY** shield and a **RECEIPT** shield, with teal arrows showing allowed, receipt-producing paths.

**Coral path:** from the rejected **ADMIN TOOL** key to the forbidden sign, showing the broad tool is not available.

**Cyan and teal arrows:** from the broker and agent toward the selected capability, showing the request and the allowed, verified result.

## Element by element

**ADMIN TOOL** — the broad, rejected master capability.

**READ CASE** — a read-only capability that returns case context.

**EXTRACT INVOICE** — a structured extraction capability for invoice facts.

**QUOTE REFUND** — a side-effect-free calculation that returns a refund amount.

**ISSUE BOUND REFUND** — the high-impact, controlled refund execution.

**TENANT** — the tenant boundary bound to the card.

**RESOURCE** — the specific data, account, or object the action may touch.

**ACTION** — the operation the card allows, often an enum.

**LIMIT** — the bound on amount, rate, count, or scope.

**EXPIRY** — the time-to-live or validity window of the capability.

**DESTINATION** — the approved recipient, endpoint, or output boundary.

**CAPABILITY BROKER** — the protected component that selects and issues one scoped card.

**AGENT** — the caller that receives exactly one narrow capability.

**POLICY** — the guard that evaluates the current context against the card.

**RECEIPT** — the durable evidence of the call, whether allowed or denied.

## Colour and flow semantics

- **Cobalt platform** — a protected identity, policy, tenant, resource, sandbox, or governance boundary. The **CAPABILITY BROKER** and the capability cards rest on cobalt platforms.
- **Cyan arrow** — a request, delegated authority, tool call, or intended data path. The broker receives a request and the agent calls the selected tool along a cyan path.
- **Teal arrow** — a verified identity, allowed decision, safe result, receipt, evidence, or review path. The allowed card and the returned receipt follow teal.
- **Coral path** — an injection, replay, privilege error, data leak, denial, quarantine, exception, or residual risk. The **ADMIN TOOL** is coral because a generic master key is a privilege error.
- **White card** — an identity, token, claim, policy, tenant key, approval, artifact, audit event, or evidence record. Each capability card is a white card carrying a bounded authority claim.

## How to present it

**Ask the room what tools the agent can call today.** Most agents have at least one generic endpoint, SDK, or database connection. Point to the coral **ADMIN TOOL** and ask which of their tools is a master key.

**Point at the four cards and read their names.** Ask what each one does that the others do not. The split between read, extract, quote, and issue is the heart of the design.

**Pick one card and read the six fields.** Ask which of those fields are enforced by their current tool code. Often the answer is one or two. The diagram says all six must be enforced.

**Show the authority ladder from lesson 151.** Ask where untrusted data sits in the ladder. It should be at the bottom, never able to become an instruction. Then explain how the narrow tools in this diagram make the ladder stick.

**Emphasize the policy and receipt guards around ISSUE BOUND REFUND.** The real decision happens at the tool. The model only sees the quote; the broker and tool see the approval, the tenant, and the destination.

**Tell the Acme attachment story.** A PDF asks for an arbitrary provider call. There is no generic tool. The quote tool has no side effect. The issue tool requires an exact bound approval. The attack becomes evidence, not a refund.

**Ask the checkpoint question before you answer it.** "Is hiding a dangerous parameter from the model schema sufficient?" Let the room argue. The answer is no. The server-side tool implementation must also ignore or reject untrusted expansion and enforce the same boundaries itself.

**Run the lab as a redesign exercise.** Pick one generic admin API and replace it with five narrow capabilities. For each, define actor, tenant, resource, arguments, limits, destinations, expiry, approval, and receipt.

**Map the pattern to both stacks.** In Next.js, the tools become narrow Server Actions. In Python, they become typed functions behind a capability service. The visual flow is the same in both.

**Mention the sources in context.** MCP security best practices describe the model-context side of the problem, NIST Zero Trust Architecture supplies the design principle, and OWASP Agentic Top 10 2026 lists the risks that narrow tools are meant to contain.

**Pose the related lessons.** Pair this diagram with lesson 151 on instruction authority, lesson 158 on policy as code, and lesson 163 on sandboxing to show how capability, policy, and isolation layers reinforce one another.

**Close on the standard.** *Make the tool contract narrower than the agent's possible mistakes.*

**Timing.** Twenty to twenty-five minutes. Add ten minutes if the room redesigns one existing admin API into narrow capabilities.
## Lab and checkpoint


**Lab:** Replace one generic admin API with five narrow capabilities. Define actor, tenant, resource, arguments, limits, destinations, expiry, approval, and receipt for each.


**Checkpoint:** Is hiding a dangerous parameter from the model schema sufficient?


**Answer:** No. The server-side tool implementation must also ignore or reject untrusted expansion and enforce the same boundaries itself.

## Glossary

- **Least privilege** — smallest useful authority
- **Capability** — bounded power to perform an action
- **Tool contract** — typed rules for calling a tool

## Sources

- MCP security best practices
- NIST Zero Trust Architecture
- OWASP Agentic Top 10 2026

