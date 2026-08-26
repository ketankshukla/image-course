# Diagram 205 — Interrupt, input request, approval, rejection, and expiry

![A workflow pauses at a decision gate and presents an approval card bound to one proposal, effect, evidence version, actor, policy, and expiry; stale cards disable and require fresh review.](../diagrams/205-interrupt-input-approval-rejection-expiry.png)

**Module:** Human control and accessible trust
**Role in the course:** Create human decision points that bind a person's choice to one understandable proposal and current evidence.
**Layout:** The diagram shows WORKFLOW reaching DECISION GATE and pausing, with a coral risk path, and a teal safe path.

---

## At a glance

**Create human decision points that bind a person's choice to one understandable proposal and current evidence.**

- The diagram centers on **WORKFLOW** and its relationship to **RECEIPT**.

- The diagram separates the tested, legitimate flow from failure paths that must fail closed.

- Maya's case: Maya leaves an approval card open overnight while a policy update changes the maximum refund exception.

---

## What the diagram teaches

### 1. 'Allow?' Is Not Informed Consent

'Allow?' is not informed consent. The diagram makes this concrete through **WORKFLOW**, **DECISION GATE**, **APPROVAL CARD**. If the team skips this, a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action. This is the lesson the case study ends with: Pause before effect, bind the decision to one versioned proposal, expire stale authority, and receipt the choice.

### 2. Approve, Reject, Request Changes, Ask A Question, And Defer

Approve, reject, request changes, ask a question, and defer are different outcomes. This is visible in the drawing as **CHOICES APPROVE REJECT EDIT ASK**. Without this step, a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action. In the walkthrough, The original card expires and its buttons become inactive before Maya returns..
![User steering changes goals, constraints, or priorities; an impact analyzer keeps valid work, rechecks dependencies, invalidates affected claims, and produces a new visible plan version with a diff.](../diagrams/206-edit-steer-reprioritize-replan-invalidate.png)

Diagram 206 — *Edit, steer, reprioritize, replan, and invalidate* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 3. Pause At A Named Decision Gate Before Any Consequential Effect

This step asks the team to pause at a named decision gate before any consequential effect, with the workflow state durably checkpointed. The diagram shows this through **DECISION GATE**, **WORKFLOW**, **EFFECT**, which make the abstract step visible and testable. An interrupt is a deliberate pause because the workflow needs human input, approval, clarification, or a decision that the system is not authorized to make alone. If the team skips this, a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action. Maya's case makes this concrete: Maya leaves an approval card open overnight while a policy update changes the maximum refund exception.

### 4. One Versioned Proposal With Purpose, Scope, Evidence, Policy, Consequences, Alternatives

Here the product must render one versioned proposal with purpose, scope, evidence, policy, consequences, alternatives, and expiry. In the drawing, **PROPOSAL**, **POLICY**, **EXPIRY** carry this responsibility. A good approval card names the exact proposal, intended effect, target, amount or scope, evidence version, policy basis, requesting actor, expiry, and what happens after each choice. If evidence, policy, amount, target, or authority changes, the old card becomes stale and its action buttons must stop working. Without this step, a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action. The result — Maya's authority applies to what she actually reviewed, not to a later changed proposal. — depends on getting this right.

### 5. Authenticate The Actor And Verify Authority, Proposal Version, Expiry

The diagram enforces this by showing the team how to authenticate the actor and verify authority, proposal version, expiry, and current preconditions on submission. The visual anchors are **PROPOSAL**, **ACTOR**, **EXPIRY**; without them the step would be invisible to the user. The choice must bind to immutable proposal identity and expected version. Rejection should not be treated as system failure, and requesting input should not silently grant authority. The case study shows the risk: a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action. This is the lesson the case study ends with: Pause before effect, bind the decision to one versioned proposal, expire stale authority, and receipt the choice.

### 6. Decision Receipt, Resume Only The Bound Transition, And Later Verify

This is the discipline that makes the product record a decision receipt, resume only the bound transition, and later verify the resulting business effect separately. This idea sits on **EFFECT** and reaches the rest of the diagram through **EFFECT**, **RECEIPT**, **DECISION GATE**. They should never claim the later business effect occurred until that effect is separately verified. Missing this is how products end up with a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action. In the walkthrough, The original card expires and its buttons become inactive before Maya returns..

### 7. Disable Stale Or Expired Cards, Preserve Safe Notes, And Require

The team must disable stale or expired cards, preserve safe notes, and require review of a refreshed proposal after material change before the interface can be trustworthy. The diagram shows this through **PROPOSAL**, **VERSION CHANGE**, **REFRESH REVIEW**, which make the abstract step visible and testable. The interface should explain why a proposal expired, preserve review notes, and offer a fresh proposal rather than simply showing an error. A system that ignores this will eventually face a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action. The danger the case warns about, Maya leaves an approval card open overnight while a policy update changes the maximum refund exception. should make this clear.

### 8. The standard in practice

The lesson is not a perfect prototype; it is a product contract. Create human decision points that bind a person's choice to one understandable proposal and current evidence.. The diagram makes that contract visible through **WORKFLOW**, **DECISION GATE**, **APPROVAL CARD**, so the team can argue about the contract before choosing a framework. The contract is not framework-specific; it is the set of observable promises the product makes to the person using it. Maya's case warns that a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action. The practical standard is this: Pause before effect, bind the decision to one versioned proposal, expire stale authority, and receipt the choice.

### 9. The Next.js and Python surfaces

The same contract appears in both stacks, but the boundary moves with the architecture.
**In Next.js / React:**
- Render approvals as accessible forms with visible proposal version, expiry, consequence summary, alternatives, and keyboard-operable actions.
- Submit through a server action that reauthenticates the user and revalidates proposal hash, expected state, authority, and expiry before recording the decision.
- Use distinct pending, accepted, rejected, expired, stale, and effect-confirmed states; never collapse them into one green success message.
- Keep the most sensitive payloads and policy decisions on the server and stream only user-visible, safe view models to client components.
**In Python / FastAPI:**
- Persist immutable proposal records and decision receipts with expected workflow revision, policy version, evidence references, scope, and expiry.
- Validate actor authority and current business preconditions in the same transaction that consumes the proposal decision.
- Emit a typed resume event for the exact paused transition and create a separate effect receipt after downstream confirmation.
- Treat every framework callback or protocol event as raw input; validate and transform it into the product's own event vocabulary before it reaches the reducer or domain model.
Both implementations must avoid the same trap: a reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action.

### 10. Analogy

Signing a house contract means approving one dated document with named terms. A signature cannot safely apply to an edited contract simply because the button stayed on screen. The analogy keeps the lesson grounded. The diagram's **WORKFLOW** plays the same role as the central object in the analogy: it must be visible, labeled, and trustworthy without the user having to infer meaning from a long narrative. The parallel works because both situations require separating the object from the record, the attempt from the proof, and the promise from the evidence.

---

## Case study — Maya

Maya leaves an approval card open overnight while a policy update changes the maximum refund exception.

### The walkthrough

1. The original card expires and its buttons become inactive before Maya returns.
2. Her review note is preserved, but the interface explains that the amount and policy basis changed.
3. A refreshed proposal highlights the changed fields and provides current evidence.
4. Only Maya's decision on the refreshed proposal can resume the refund transition.

### The result

Maya's authority applies to what she actually reviewed, not to a later changed proposal.

### The danger

A reusable approval button can turn an old human decision into authority for a new amount, target, policy, or action.

### The takeaway

Pause before effect, bind the decision to one versioned proposal, expire stale authority, and receipt the choice.

---

## Composition

The picture is a single-view explainer for *Interrupt, input request, approval, rejection, and expiry*. On the left, the diagram shows WORKFLOW reaching DECISION GATE and pausing. At the top, an APPROVAL CARD names PROPOSAL, EFFECT, EVIDENCE VERSION, POLICY, ACTOR, EXPIRY, CHOICES APPROVE REJECT EDIT ASK. In the center, after EXPIRY or VERSION CHANGE, coral buttons disable and REFRESH REVIEW appears. To the right, teal RECEIPT resumes the exact paused task. The eye travels from **WORKFLOW** through the central flow to **RECEIPT**, with the contrast between coral risk paths and teal recovery paths giving the reader the core message at a glance.

## Element by element

- **WORKFLOW** — the sequence of stages that the agent and product move through to complete a task.
- **DECISION GATE** — the point where the workflow pauses because human input or authority is required.
- **APPROVAL CARD** — the versioned card that asks the person to approve, reject, edit, or ask about a proposal.
- **PROPOSAL** — the immutable, versioned description of a requested decision.
- **EFFECT** — one of the cards named by **APPROVAL CARD**; this is the **EFFECT** card.
- **EVIDENCE VERSION** — one of the cards named by **APPROVAL CARD**; this is the **EVIDENCE VERSION** card.
- **POLICY** — one of the cards named by **APPROVAL CARD**; this is the **POLICY** card.
- **ACTOR** — one of the cards named by **APPROVAL CARD**; this is the **ACTOR** card.
- **EXPIRY** — one of the cards named by **APPROVAL CARD**; this is the **EXPIRY** card.
- **CHOICES APPROVE REJECT EDIT ASK** — one of the cards named by **APPROVAL CARD**; this is the **CHOICES APPROVE REJECT EDIT ASK** card.
- **VERSION CHANGE** — one of the items named by **EXPIRY**; this is the **VERSION CHANGE** item.
- **REFRESH REVIEW** — one of the items named by **EXPIRY**; this is the **REFRESH REVIEW** item.
- **RECEIPT** — durable proof of a decision, effect, or user-visible transition.

---

## Colour and flow semantics

The course visual grammar applies directly to this diagram.

- **Cobalt platform** — A browser surface, state store, component catalog, product boundary, workspace, or learning-platform region. Here the cobalt surface under **WORKFLOW** and the surrounding workspace frames the product boundary; it tells the reader that this is a bounded product region, not an uncontrolled chat surface. It marks the product's responsibility to keep the user's workspace distinct from raw model output or runtime internals.

- **Cyan arrow** — A typed event, validated state update, user action, artifact reference, notification, or navigation path. Cyan arrows carry the flow of events, updates, and proposals from left to right, linking the typed cards and records to the reducer or next gate. When the reader sees cyan, they should expect a deliberate, validated transition rather than an accidental or hidden connection.

- **Teal arrow** — Authoritative state, accessible completion, informed consent, safe approval, preserved work, or verified recovery. Teal marks the authoritative and safe path, such as the committed receipt or restored state, distinguishing it from the raw request. This color tells the reader that the product has enough evidence and authority to proceed safely.

- **Coral path** — Conflict, stale UI, unsafe rendering, deceptive state, expired approval, privacy failure, lost work, or blocked action. Coral marks the conflict, stale state, or blocked action that appears when a control is missing or bypassed. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.

- **White card** — An event, component, stage, proposal, artifact, receipt, consent record, lesson, checkpoint, or recovery option. **APPROVAL CARD**, **PROPOSAL**, **RECEIPT** appear as white cards, showing that they are records, proposals, or evidence rather than raw data or system internals. The white background separates user-meaningful records from raw system logs or generated text.

The overall flow moves from the initiating actor or request, through validation and reduction, toward either the teal recovery or completion path or the coral failure path. The color of each arrow and card is a trust cue, not a decoration.

---

## How to present it

- **Start with the user moment.** Maya leaves an approval card open overnight while a policy update changes the maximum refund exception. Ask the room what they need to see to feel in control. Invite someone to describe the moment before any solution appears.

- **Point at WORKFLOW and ask what it represents.** Then trace the flow from there through the next two or three elements, naming the color and direction of each arrow. Encourage them to name the incoming trigger, the visible state, and the decision the product must make.

- **Point at DECISION GATE for step 1.** Pause At A Named Decision Gate Before Any Consequential Effect. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at PROPOSAL for step 2.** One Versioned Proposal With Purpose, Scope, Evidence, Policy, Consequences, Alternatives. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at PROPOSAL for step 3.** Authenticate The Actor And Verify Authority, Proposal Version, Expiry. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at EFFECT for step 4.** Decision Receipt, Resume Only The Bound Transition, And Later Verify. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at PROPOSAL for step 5.** Disable Stale Or Expired Cards, Preserve Safe Notes, And Require. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Use the analogy.** Signing a house contract means approving one dated document with named terms. A signature cannot safely apply to an edited contract simply because the button stayed on screen. Draw the parallel to the diagram and ask what would break if the two situations were handled the same way.

- **Tell the case study.** Maya leaves an approval card open overnight while a policy update changes the maximum refund exception Walk through the walkthrough and stop at the moment the old design would have failed. Pause at the step where the old design would have failed and ask how the new interface prevents it.

- **Run the lab.** Design an approval schema with twenty fields and draw accepted, rejected, changes-requested, deferred, expired, stale, unauthorized, and effect-failed paths. Write the exact visible explanation and durable receipt for each. Ask pairs to present one part of the diagram and explain how the other parts reference it without merging their identities.

- **Pose the checkpoint.** Does an approval receipt prove the approved business effect succeeded? Let the room answer before confirming the principle. Collect answers, then confirm the principle and note any exceptions the team should watch for.

- **Close on the contract.** Pause before effect, bind the decision to one versioned proposal, expire stale authority, and receipt the choice. Ask the team what their own product's equivalent of the contract would be.

---

## Lab and checkpoint

**Lab:** Design an approval schema with twenty fields and draw accepted, rejected, changes-requested, deferred, expired, stale, unauthorized, and effect-failed paths. Write the exact visible explanation and durable receipt for each.

**Checkpoint:** Does an approval receipt prove the approved business effect succeeded?

**Answer:** No. It proves the human decision. A separate authoritative effect receipt must prove execution and outcome.

---

## Glossary

- **Interrupt** — deliberate workflow pause for human participation
- **Proposal** — immutable versioned description of a requested decision
- **Expiry** — time or condition after which a decision card cannot grant authority

---

## Sources

- [AG-UI capabilities](https://docs.ag-ui.com/concepts/capabilities)
- [AG-UI events](https://docs.ag-ui.com/concepts/events)
- [ARIA dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)

## Related lessons

- Diagram 200 — Optimistic interface state versus authoritative business state
- Diagram 206 — Edit, steer, reprioritize, replan, and invalidate
- Diagram 207 — Cancel, undo, compensate, and preserve audit history

---