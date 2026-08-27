# Diagram 137 — Agent Roles, Skills, Contracts, and Capability Discovery

![On dark navy, a COORDINATOR robot on a blue platform sends a teal arrow labelled READING AGENT CARDS to three white cards: POLICY SPECIALIST, FINANCE SPECIALIST, CUSTOMER SPECIALIST. Each card lists SKILLS, INPUT MODES, OUTPUT MODES, SECURITY, INTERFACE, VERSION. A cyan arrow leads from the cards to a blue POLICY FILTER funnel with a check. The funnel emits a teal arrow to a single FINANCE SPECIALIST card with a green check above it. A coral dashed arrow from the funnel drops to a red box with a forbidden sign and the text DESCRIPTION ONLY IS LABELED NOT AUTHORITY. At the lower left, a legend shows cyan for command and forward-work, teal dashed for event/ack/receipt, and coral dashed for failure path.](../diagrams/137-agent-role-capability-contract.png)

**Module:** Multi-agent collaboration, delegation, and A2A
**Role in the course:** the A2A foundation — how a coordinator discovers and filters agents without trusting self-description
**Layout:** coordinator reading agent cards, a policy filter selecting one, and a rejected description-only path

---

## At a glance

A **COORDINATOR** reads three **AGENT CARDS**.

Each card lists: **SKILLS, INPUT MODES, OUTPUT MODES, SECURITY, INTERFACE, VERSION**.

A **POLICY FILTER** selects the right card. The output is **FINANCE SPECIALIST** with a green check.

And at the bottom right, a red box: **DESCRIPTION ONLY IS LABELED NOT AUTHORITY**.

A card can describe what an agent can do. It cannot grant permission to do it.

---

## What the diagram teaches

### 1. A role is why the agent exists, a skill is what it can do, and a card is the advertisement

The three cards are labelled **POLICY SPECIALIST, FINANCE SPECIALIST, CUSTOMER SPECIALIST**. Those are roles.

Each card lists skills. A role is the *why*: this agent exists to handle finance. A skill is the *what*: it can calculate a refund, it can read a ledger, it can produce a report.

The card is not the agent. It is the discoverable description. The diagram separates *description* from *authority*.

### 2. Agent Cards have six fields, and every field is a filter

**SKILLS** — the bounded capabilities.
**INPUT MODES** — how the agent can receive work. Text, structured data, file, voice.
**OUTPUT MODES** — what it returns. Text, artifact, status, structured record.
**SECURITY** — the authentication and encryption requirements.
**INTERFACE** — the protocol and version it speaks.
**VERSION** — the specific revision of the card.

The list is the same on every card because the comparison is fair. The coordinator does not ask *can you do finance?* It asks *do you accept this input, produce this output, meet this security, speak this interface, at this version?*

### 3. Discovery narrows candidates; policy selects one

The cards enter the **POLICY FILTER**. Discovery is the first step: find agents that are technically capable. Policy is the second step: decide which one may actually be used.

Policy is not part of the Agent Card. It lives in the coordinator's tenant, the allowlist, the risk engine, the data-residency rules, and the current health checks.

The filter is drawn as a funnel. Many candidates enter. One candidate exits. The rejected cards do not vanish; they are simply not authorized for this task.

### 4. Description only is labeled not authority

The red box at the bottom right is the diagram's warning. An Agent Card is a self-description. It can be wrong, out of date, or maliciously generous.

A marketing description is not a business authority. The agent may say it can issue refunds. The business policy says only the finance specialist with the Acme tenant allowlist and the current security certificate may issue refunds.

The green check above the selected FINANCE SPECIALIST card is not the card's own claim. It is the policy filter's decision.

### 5. Version is a contract, not a suggestion

The **VERSION** field is last on every card. It is there because the card is versioned. A coordinator that selected version 1.3 must not silently fall back to 1.2 because the agent prefers it.

Pinning the version is part of the delegation record. If the agent's card changes, the coordinator must decide whether the task is still valid. The version is not a recommendation; it is the contract for this delegation.

### 6. Input and output modes are the task contract

A skill without the right input and output modes is not a match. An agent may claim it can refund, but if it only accepts free text and the task has a structured refund request, it cannot do the work as specified.

The modes are the concrete interface. The skill is the abstract claim. The diagram lists them separately because both must match.

### 7. The policy filter is where security meets capability

**SECURITY** on the card says what the agent requires. The policy filter adds what the tenant requires. The result is an authorized match.

The filter is a gate. It is not a search. An agent card that is not on the allowlist, that fails health checks, or that violates data residency is rejected, regardless of its skills.

This is why the filter appears after discovery. The coordinator first narrows the search to agents that are technically capable, then applies policy. Reversing the order — applying policy before collecting candidates — makes it hard to explain why a better-qualified agent was not available. Doing policy after discovery means the decision is auditable: these were the candidates, this was the policy, this was the selected match.

The next diagram shows what the coordinator does after it has selected a card: it sends a message, creates a task, and waits for an artifact.

### 8. The legend at the bottom is the course's durable vocabulary

Below the main flow, three line styles: **cyan for command and forward-work**, **teal dashed for event, acknowledgement, receipt**, **coral dashed for failure path**.

The coordinator's act of reading cards is a command — it is doing work. The cards themselves are information, like events or receipts, not authority. The rejection of a card by policy is a failure path.

This vocabulary appears in every diagram in the course. The same colours mean the same things across all diagrams. When a room sees these three colours, they should know whether a line is carrying a request, a durable fact, or a rejection.

### 9. The card is fetched from a trusted source and validated before it is compared

The `READING AGENT CARDS` arrow begins somewhere. A card from an untrusted source, or one that fails the A2A schema check, is not a candidate. It is just a document. The coordinator fetches the card from a trusted registry, validates its structure, checks the interface and protocol version, and confirms any required security extensions before it enters the six-field comparison.

This is why the fields are identical across cards: the schema is the comparison table. A card that omits a required field, or that is cached too long without re-validation, is rejected before the policy filter sees it.

### 10. Capability matching and authorization are separate systems, and the task record pins them together

The coordinator does not ask one system to do both jobs. The capability matcher answers *can the agent do this work?* by comparing the six fields to the task contract. The policy engine answers *may the agent do this work?* by checking the tenant allowlist, risk class, data-residency rules, and current health.

The selected card's identity, version, and policy decision are pinned to the delegated task record. That record is what an auditor will read, and it must show both halves of the contract.

![On dark navy, a CLIENT AGENT on a blue platform resolves an AGENT CARD, then sends a MESSAGE carrying a CONTEXT ID and REQUEST ID through an A2A INTERFACE to a REMOTE AGENT. The remote agent returns a TASK ID and WORKING status, then later STATUS UPDATE and ARTIFACT. A red coral VERSION FALLBACK arrow is blocked by a red X. Labels include A2A-VERSION 1.0.](../diagrams/138-a2a-delegation-task-creation.png)

Capability discovery from this diagram becomes a real delegation when the coordinator sends a versioned A2A message and receives a durable task ID. The Agent Card is only the advertisement; the message, task ID, and artifact are the actual contract.

---

## Case study — Montague Finance, the agent with the wrong card

Montague runs a multi-tenant accounting platform. They wanted to add a refund assistant agent that could be delegated to payment providers.

### What they had

A marketplace of agent cards. Each card described skills, input modes, output modes, security, interface, and version. The platform let users search by skill and select the first match.

There was no policy filter. The search returned any card that mentioned *refund* or *payment*. The selection was based on keyword relevance and the card's own confidence score. There was no check of the tenant allowlist, data residency, or security certificate.

### The incident

A customer searched for a *payment specialist* to handle refund calculations. The search returned two cards. Both advertised a *refund* skill. One was a third-party agent hosted in a different region, not on the tenant allowlist.

The customer selected it because it appeared first. The agent received the customer's payment data and produced a refund report. The report was correct, but the data had left the tenant's region.

The compliance team only discovered this during a quarterly review. The agent had not been authorized, but nothing in the system had stopped the delegation.

### The discovery and policy model

- **Discovery:** search the card registry for agents that match the required skill and modes.
- **Validation:** verify the card against the A2A schema, check the interface version, and confirm the security requirements.
- **Policy filter:** apply tenant allowlist, data residency, risk class, and current health status.
- **Delegation record:** pin the selected card version, the skill used, and the authorization decision to the task.

The third-party agent's card was now discoverable, but the policy filter rejected it for this tenant. The customer saw only the authorized finance specialist.

### Results

- **Unauthorized agents selected by search ranking:** 1 incident and ongoing risk → 0.
- **Data-residency violations from agent delegation:** 1 → 0.
- **Time to audit an agent delegation:** several days of cross-system search → seconds, because the task record contains the card version and policy decision.
- **Customers choosing agents by prose match:** 100% → 0, because the UI filtered by skill, modes, and policy, not keywords.

### The line in their engineering standard

*The Agent Card describes. The policy filter authorizes. No skill match is a permission match.*

---

## Composition

A coordinator reading three agent cards, with a policy filter selecting one and a rejected description-only path.

**Left:** **COORDINATOR** — a robot on a blue platform with a screen behind it, sending a teal arrow labelled **READING AGENT CARDS**.

**Centre:** three white cards on blue platforms:
- **POLICY SPECIALIST**
- **FINANCE SPECIALIST**
- **CUSTOMER SPECIALIST**

Each card lists six rows with icons: **SKILLS, INPUT MODES, OUTPUT MODES, SECURITY, INTERFACE, VERSION**.

**Right of centre:** a **POLICY FILTER** — a blue funnel with a check. A teal arrow leaves the funnel to a single **FINANCE SPECIALIST** card on a blue platform, with a green check above it.

**Lower right:** a **coral dashed arrow** from the funnel to a red box with a forbidden sign and the text **DESCRIPTION ONLY IS LABELED NOT AUTHORITY**.

**Lower left:** a legend with three entries:
- **Cyan arrow** — COMMAND AND FORWARD-WORK.
- **Teal dashed arrow** — EVENT, ACKNOWLEDGEMENT, RECEIPT.
- **Coral dashed arrow** — FAILURE PATH.

## Element by element

**COORDINATOR** — the entity discovering and selecting an agent.

**AGENT CARD** — the discoverable description.

**SKILLS / INPUT MODES / OUTPUT MODES / SECURITY / INTERFACE / VERSION** — the six fields.

**POLICY FILTER** — the authorization gate.

**FINANCE SPECIALIST** — the selected, authorized agent.

**DESCRIPTION ONLY IS LABELED NOT AUTHORITY** — the warning that self-description is not permission.

## Colour and flow semantics

- **Cyan arrow** from the coordinator to the cards marks command and forward-work — the active search.
- **Teal dashed** from the cards to the filter marks the event/ack/receipt lane — the card information is a reference, not a transfer of authority.
- **Coral dashed** from the filter to the red box is the failure path — description without authority is rejected.
- **Green check** above the selected card is the policy decision.
- The **identical card fields** make the comparison explicit and fair.

## How to present it

**Start with the business-card analogy.** A business card tells you someone's services and phone number; it does not give them permission to sign your company's checks.

**Point at the six fields and ask which ones the room checks.** Most check skills, few check version, fewer check security or interface.

**Show the policy filter and ask where it lives.** In the agent? In the registry? In the coordinator? The correct answer is in the coordinator's policy, not the agent's card.

**Emphasise the red box.** DESCRIPTION ONLY IS LABELED NOT AUTHORITY. An agent can claim anything. The policy filter decides whether the claim is authorized for this task.

**Trace the next diagram.** From card to message to task to artifact. The card is only the first step. The real delegation is a versioned A2A message with a durable task ID.

**Tell the Montague story.** A third-party payment agent discovered by keyword, selected by search ranking, processed customer data outside the tenant's region. The fix: validation, policy filter, allowlist, version pinning, delegation record.

**Make the version point.** Pin the card version to the task. Do not silently fall back. A changed card is a new decision.

**Ask what the task record would show if an auditor reviewed it.** A complete record includes the workflow ID, the discovery query, the candidate cards considered, the policy filter result, the selected card version, and the delegated task ID. Without that, an unauthorized delegation is not a simple mistake; it is an undetectable one.

**Close on the standard.** *The Agent Card describes. The policy filter authorizes. No skill match is a permission match.*

**Run the lab as a card inspection.** Hand the room the Agent Card checklist (identity, skills, modes, interface, version, security, extensions, cache validation, and trust source) and ask them to score a sample card. The gaps they find become the most memorable part of the session.

**Pose the checkpoint question before you answer it.** "Does a matching skill prove an agent may access Maya's case?" Let the room argue, then give the rule: a matching skill proves declared capability only; authorization, tenant policy, and least privilege decide access.

**Map the pattern to both stacks.** In Next.js, keep the card catalog operator-only and resolve policy status on the server; in Python, validate the A2A schema and persist the selected card identity and version beside every delegated task. The visual flow is the same in both stacks.

**Point to the sources.** The A2A Protocol 1.0 specification, the A2A agent discovery topic, and the A2A protocol definitions give the fields and validation rules the diagram represents.

**Use the glossary terms as checks.** Before the close, have the room define *Agent Card*, *Skill*, and *Capability discovery* in their own words, then compare them to the official definitions.

**Timing.** Twenty minutes. Thirty if the room inspects one existing agent selection and checks whether policy is applied after the card is returned.

---

## Lab and checkpoint

**Lab:** Inspect one agent card your system uses. Score it against the checklist: identity, skills, modes, interface, version, security, extensions, cache validation, and trust source. Then write the policy filter that authorizes the card for a specific task, and the task record that pins discovery, policy, and delegation together.

**Checkpoint:** Why does a matching skill not prove an agent may access a user's case?

**Answer:** Because the agent card describes capability, not authorisation. A matching skill only proves the agent declares it can do the work. Authorisation, tenant policy, and least privilege decide whether it may access the case.

## Glossary

- **Agent card** — the advertised description of an agent's role, skills, and interfaces.
- **Capability** — what the agent can do at the protocol level.
- **Capability discovery** — the process of finding agents that match a need.
- **Card version** — the pinned, validated version used for a task.
- **Delegation record** — the durable record of selecting and assigning a task to an agent.
- **Description** — a claim in the card, not authority.
- **Policy filter** — the coordinator's check that authorizes the selected card.
- **Role** — why the agent exists.
- **Security** — the security properties declared in the card.
- **Skill** — what the agent can do.
- **Version pinning** — using the exact card version chosen at delegation time.

## Sources

- A2A Agent Card specification
- A2A discovery and capability matching
- Agent selection and authorization policies
