# Diagram 158 — Policy as Code, Claims, Context, and Decision Receipts

![On dark navy, a POLICY ENFORCEMENT POINT is a blue shield platform in the center left. Eight white cards on the left feed cyan arrows into it: SUBJECT, ACTOR, TENANT, RESOURCE, ACTION, DATA CLASS, DESTINATION, RISK, and APPROVAL. A cyan arrow labelled INPUT leaves the enforcement point and enters a POLICY DECISION POINT, a blue scales platform with a VERSIONED POLICY base. From the decision point, arrows point right to four outcome cards: green ALLOW, red DENY, yellow STEP UP, teal REDACT, and purple OBLIGATIONS. Below, a DECISION RECEIPT card records INPUT HASH, POLICY VERSION, RESULT, REASONS, and TIME.](../diagrams/158-policy-context-decision-receipt.png)

**Module:** Capabilities, tools, policy, and secrets
**Role in the course:** how to move security decisions out of scattered if-statements into testable policy with explainable evidence
**Layout:** a policy enforcement point on the left collects claims and context, a policy decision point in the center applies a versioned policy, four outcomes and obligations on the right, and a decision receipt below

---

## At a glance

A **POLICY ENFORCEMENT POINT** gathers **SUBJECT, ACTOR, TENANT, RESOURCE, ACTION, DATA CLASS, DESTINATION, RISK,** and **APPROVAL**.

It sends a single **INPUT** to a **POLICY DECISION POINT** that runs a **VERSIONED POLICY**.

The decision point returns **ALLOW, DENY, STEP UP, REDACT,** plus **OBLIGATIONS**.

Every decision produces a **DECISION RECEIPT** with **INPUT HASH, POLICY VERSION, RESULT, REASONS,** and **TIME**.

A referee applies a published rulebook to the players, the score, the time, and the exact play, then records the ruling and the rule used.

---

## What the diagram teaches

### 1. Policy as code is versioned, reviewable logic

The diagram shows **VERSIONED POLICY** at the base of the decision point. That matters because policy is not a collection of ad-hoc checks hidden in route handlers. It is a separate, named, versioned artifact that can be reviewed, tested, and rolled back. When policy lives in code, the team can ask: which rule allowed this? Which version was in force? Who changed it? When?

Versioned policy is the first step toward an explainable decision. A denial from an undocumented `if` statement is a guess. A denial from a named, versioned rule is evidence.

### 2. Claims are what the system can prove

The left side of the diagram lists **SUBJECT, ACTOR, TENANT,** and **APPROVAL**. These are claims. A claim is a fact the system has verified, not a string the caller supplied. The subject claim says who originated the request. The actor claim says what software is performing it. The tenant claim says which boundary owns the data. The approval claim says a specific authorized approver bound to a specific transaction.

A policy engine fed by caller-controlled fields is not security; it is a centralization of the vulnerability. Claims must come from trusted identity and token validation, authoritative resource data, and durable approval records.

### 3. Context is the current situation

The remaining inputs — **RESOURCE, ACTION, DATA CLASS, DESTINATION,** and **RISK** — are context. The resource is the case or capability being touched. The action is the operation being attempted. The data class is the sensitivity of the data involved. The destination is where the result may go. The risk is any signal that changes the required assurance.

Context can change between planning and execution. A refund that was quoted safely may later involve a new destination or a higher amount. The policy point re-evaluates the context at the moment of decision, not when the plan was first formed.

### 4. The policy decision point is separate from the enforcement point

The **POLICY ENFORCEMENT POINT** collects the input. The **POLICY DECISION POINT** evaluates it. This split is important. The enforcement point is close to the protected resource or tool. The decision point may be in-process, a service, or an external system such as OPA.

The enforcement point does not make the call. It asks the decision point and then enforces the result. That means the same policy can be applied by many tools, and the enforcement logic is simple: obey the decision and any obligations.

### 5. The outcomes are typed and actionable

The diagram shows four outcomes: **ALLOW, DENY, STEP UP,** and **REDACT**. Each is a clear instruction. **ALLOW** means proceed with the requested action. **DENY** means stop and do not retry. **STEP UP** means the caller must provide additional authentication or approver evidence before proceeding. **REDACT** means the action can proceed only if sensitive fields are masked or removed.

Each outcome comes with **OBLIGATIONS**. An allow may carry an obligation to log a receipt. A step-up may require a specific approver within a time limit. A redact may require that the destination is an internal system. Obligations are part of the decision, not hints.

### 6. Fail-closed is the safe default

The policy decision point should be fail-closed. If the input is incomplete, if the policy version cannot be loaded, or if the decision point is unreachable, the default is deny or step-up. A fail-open policy engine that allows by default when it is confused is not a control.

The diagram enforces this by requiring a complete trusted context and a known policy version. Missing a tenant, an actor, or a resource should not produce an allow with a warning. It should produce a denial with a reason.

### 7. The receipt is as important as the decision

The **DECISION RECEIPT** at the bottom records the decision in a durable, reviewable form. It carries the **INPUT HASH**, the **POLICY VERSION**, the **RESULT**, the **REASONS**, and the **TIME**. This is the evidence that makes the decision explainable later.

The input hash is important. It lets an auditor verify that the decision was made from the same input the system claims. The policy version lets the auditor know which rule set applied. The reasons explain why. The time anchors the decision.

### 8. Trusted context plus versioned policy plus enforced obligations equals explainable security

The diagram is a formula. Start with a complete, trusted context. Send it to a versioned policy decision point. Receive an outcome and obligations. Enforce them at the protected boundary. Record a receipt.

This replaces scattered if-statements with a single, testable pipeline. It also makes security decisions visible to operators, auditors, and customers. The interface can say "This action was allowed by policy v4.2 because the subject is Maya, the actor is the refund worker, the amount is below the self-service limit, and the destination is the original payee." That is explainable. An undocumented server check cannot do that.

### 9. Policy fed by untrusted input is a confused-deputy risk

The case study in the JSON warns: *"Policy fed by caller-controlled tenant, role, or resource fields merely centralizes the vulnerability."* The diagram insists that the inputs are built from verified identity and authoritative resource data. The enforcement point must not trust the model or the client to say which tenant or which risk class applies. It must look those up from trusted sources.

This is why the inputs are split into claims and context. Claims are verified. Context is looked up. Both are assembled by the enforcement point, not by the caller.

### 10. The previous lesson shows the tool contract that this policy enforces

![On dark navy, a large coral key labeled ADMIN TOOL is shown on the left with a red X. To the right, four white capability cards sit on a cobalt platform: READ CASE, EXTRACT INVOICE, QUOTE REFUND, and ISSUE BOUND REFUND. Each card lists six fields. A CAPABILITY BROKER selects one card and hands it to an AGENT. POLICY and RECEIPT shields surround the high-impact tool.](../diagrams/157-least-privilege-capability-tools.png)

Diagram 157 defines the tool contract. Diagram 158 shows the policy decision that selects, allows, denies, or modifies the use of that contract. The capability card is the object; the policy decision point is the gate. A quote refund card is allowed for a low-risk case. An issue bound refund card may be denied without approval, step-up for a high amount, or redacted if it carries unnecessary data. The two diagrams are a pair: one designs the capability; the other decides whether it runs.

### 11. The Next.js map: centralized protected mutations and typed denial states

In Next.js, protected mutations should live in server code that calls a policy adapter. The adapter builds the input from the authenticated security context and the authoritative resource data. It returns a typed result: allow, deny, step-up, or redact. The server then enforces the decision and produces a receipt.

The React interface should render the returned state, not invent it. If the result is step-up, the UI shows exactly what approval is needed. If the result is redact, it shows which fields will be masked. Tokens, policy decisions, secrets, and privileged mutations stay in server code; the browser receives only the minimum display state.

### 12. The Python map: a PolicyDecisionPort and snapshot fixtures

In Python, the pattern becomes a `PolicyDecisionPort` with an in-process test implementation and an external adapter such as OPA. The port accepts a typed decision input and returns a typed decision. Decision fixtures are snapshotted by policy version, so tests can detect when a policy change alters an expected outcome.

Pydantic models for identity, tenant, policy, data classification, and audit context keep the boundaries explicit. Tests cover allow and deny paths with hostile synthetic fixtures. The test suite should include the ten cases from the lab: correct tenant, cross-tenant, low amount, high amount, changed payee, expired approval, new destination, risky device, missing evidence, and emergency exception.

---

## Case study — Maya's refund with a changed destination

Maya asks for a refund. The refund is valid, but the vendor attachment tries to change the payee, and the amount is above her self-service threshold.

### The decision input

The policy enforcement point builds the input:

- **SUBJECT** — Maya, the customer.
- **ACTOR** — the Acme refund worker.
- **TENANT** — Maya's organization.
- **RESOURCE** — the refund case.
- **ACTION** — issue refund.
- **DATA CLASS** — payment and personal data.
- **DESTINATION** — the new payee from the attachment.
- **RISK** — amount above self-service threshold and destination changed from the original.
- **APPROVAL** — no supervisor approval yet.

### The policy decision

The policy decision point runs the versioned refund policy:

- The new destination is not on the approved payee list: **DENY** for that path.
- The amount is above the self-service threshold: **STEP UP**, requiring a supervisor approval.
- If the destination were the original payee and the amount were lower, the result would be **ALLOW**.
- The sensitive payment token is not needed in the interface, so any response must **REDACT** it.

The tool receives no executable authority until the obligations are satisfied.

### The result

The interface tells Maya that the proposed destination is not allowed and that a supervisor must approve the amount. It does not leak the payment token or the full case file. The receipt records the input hash, the policy version, the step-up result, and the reasons.

### The danger

If the policy engine trusted the caller to supply the tenant, the risk class, or the approved destination, the attacker could simply say the new payee is low risk. The policy would then be a rubber stamp on a forged context.

### The takeaway

Trusted context plus versioned policy plus enforced obligations equals an explainable decision.

---

## Composition

The diagram has a left-to-right flow with a receipt below.

**Left side — input cards:**
- **SUBJECT** — the human originator.
- **ACTOR** — the software performing the action.
- **TENANT** — the organizational boundary.
- **RESOURCE** — the protected object.
- **ACTION** — the operation being attempted.
- **DATA CLASS** — the sensitivity label.
- **DESTINATION** — where the result may go.
- **RISK** — any risk signal.
- **APPROVAL** — the bound approval record.

**Center — two platforms:**
- **POLICY ENFORCEMENT POINT** — collects input and enforces the decision.
- **POLICY DECISION POINT** — evaluates the input against the versioned policy.

**Right side — outcomes:**
- **ALLOW** — green, proceed.
- **DENY** — red, stop.
- **STEP UP** — yellow, require more proof.
- **REDACT** — teal, remove or mask data.
- **OBLIGATIONS** — purple, conditions the enforcement point must satisfy.

**Bottom — DECISION RECEIPT:**
- **INPUT HASH** — fingerprint of the evaluated input.
- **POLICY VERSION** — the rule set in force.
- **RESULT** — the outcome.
- **REASONS** — why the decision was made.
- **TIME** — when the decision was made.

## Element by element

**SUBJECT** — the human on whose behalf the action is taken.

**ACTOR** — the software identity performing the action.

**TENANT** — the boundary that owns the data and the transaction.

**RESOURCE** — the protected object or capability being accessed.

**ACTION** — the operation being attempted.

**DATA CLASS** — the classification of the data involved.

**DESTINATION** — the intended recipient or location of the result.

**RISK** — any signal that changes the required assurance.

**APPROVAL** — the durable authorization for a specific transaction.

**POLICY ENFORCEMENT POINT** — the boundary that assembles input and enforces the decision.

**POLICY DECISION POINT** — the component that evaluates the input against policy.

**VERSIONED POLICY** — the named, versioned rule set.

**ALLOW** — the outcome that permits the action.

**DENY** — the outcome that refuses the action.

**STEP UP** — the outcome that requires additional authentication or approval.

**REDACT** — the outcome that requires sensitive data to be masked or removed.

**OBLIGATIONS** — conditions the enforcement point must satisfy.

**DECISION RECEIPT** — the durable record of the decision.

## Colour and flow semantics

- **Cobalt platform** — a protected boundary. The POLICY ENFORCEMENT POINT and POLICY DECISION POINT are cobalt.
- **Cyan arrow** — a request or input. The arrows from the left cards into the enforcement point and from the enforcement point to the decision point are cyan.
- **Teal arrow/path** — a verified, allowed, or safe path. The redact outcome and the decision receipt are teal.
- **Red card** — a denial. The DENY outcome is red.
- **Green card** — an allowed outcome. The ALLOW card is green.
- **Yellow card** — a step-up or exception. The STEP UP card is yellow.
- **Purple card** — obligations that accompany the decision.
- **White card** — a claim, record, or evidence. The input cards and the receipt are white.

The flow moves from left to right, from claims and context through the decision point to an outcome. The receipt below anchors the entire transaction.

## How to present it

**Ask where the policy decisions live today.** Most systems scatter them in controllers, middleware, and model prompts. The diagram shows a single pipeline. Ask the room to find one business rule that is currently duplicated or hidden.

**Trace the input cards one by one.** For a real action in their system, can they name the subject, actor, tenant, resource, action, data class, destination, risk, and approval? If any are missing, the policy is incomplete.

**Emphasize that claims are not caller-controlled.** The subject and tenant must come from trusted identity and token validation. The resource and data class must come from authoritative data. The approval must come from a durable approval record. If the caller can set the tenant, the policy is cosmetic.

**Explain the four outcomes.** Allow, deny, step-up, and redact are not just return codes. They are instructions with obligations. A step-up must name the required approver. A redact must name the fields to remove.

**Show the receipt as evidence.** The decision receipt is what makes the decision reviewable. Ask what their current system records when a payment is denied. Does it include the policy version and the reasons?

**Pair with Diagram 157.** The capability card is the object. The policy decision is the gate. A quote refund card and an issue refund card can be evaluated by the same policy point with different context.

**Map to Next.js.** Centralize protected mutations in server code. Use a policy adapter that returns typed states. Render those states in the UI. Do not let the UI invent security messages.

**Map to Python.** Use a `PolicyDecisionPort`. Snapshot decision fixtures by policy version. Test the lab's ten cases. Make the policy version an explicit dependency of the deployment.

**Run the lab as a table exercise.** Have the room fill out the decision input and expected outcome for the ten cases. This usually reveals that many "obvious" rules are not written down.

**Ask the checkpoint.** "Should the policy engine itself perform the refund?" The answer is usually no. It decides and returns obligations. A separate enforcement point performs or denies the action and records the result.

**Close on the standard.** Every protected action uses a complete trusted context, a known policy version, fail-closed enforcement, and a redacted decision receipt.

**Timing.** Twenty-five minutes. Thirty if the room writes the decision schema for one real action.

---

## Lab and checkpoint

**Lab:** Create a decision-input schema and ten table-driven cases: correct tenant, cross-tenant, low amount, high amount, changed payee, expired approval, new destination, risky device, missing evidence, and emergency exception.

**Checkpoint:** Should the policy engine itself perform the refund?

**Answer:** Usually no. It decides and returns obligations; a separate enforcement point performs or denies the action and records the result.

---

## Glossary

- **Claim** — an asserted identity or token fact that has been verified.
- **Policy decision point** — the component that evaluates rules against an input.
- **Obligation** — a condition the enforcement point must satisfy as part of a policy decision.
- **Decision receipt** — a durable record of the policy input, version, result, reasons, and time.
- **Fail-closed** — a default of deny or step-up when the decision cannot be made with confidence.

---

## Sources

- Open Policy Agent decision logs
- NIST Zero Trust Architecture
