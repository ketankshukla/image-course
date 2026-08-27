# Diagram 219 — Product analytics, feedback, evaluation, and experiment ethics

![User outcomes connect to minimized product events, feedback, quality evaluation, safety review, and accessibility evidence; every metric exposes its definition and denominator, while experiments require consent, risk review, fair allocation, stop rules, guardrails, and debriefing.](../diagrams/219-analytics-feedback-evaluation-experiment-ethics.png)

**Module:** Agentic product operations
**Role in the course:** Improve an agentic product with honest evidence while protecting learners and users from manipulative measurement and unsafe experiments.
**Layout:** The diagram shows USER OUTCOME feeding PRODUCT EVENT, FEEDBACK, QUALITY EVAL, SAFETY REVIEW, ACCESSIBILITY EVIDENCE, with a coral risk path.

---

## At a glance

**Improve an agentic product with honest evidence while protecting learners and users from manipulative measurement and unsafe experiments.**

- The diagram centers on **USER OUTCOME** and its relationship to **EXAMPLE AS FACT**.

- The diagram separates the tested, legitimate flow from failure paths that must fail closed.

- Maya's case: Acme considers changing an approval button from Review and approve to Continue because a prototype shows more task completions.

---

## What the diagram teaches

### 1. They Can Inform One Another But Should Not Be Merged

They can inform one another but should not be merged into one satisfaction score. The diagram makes this concrete through **USER OUTCOME**, **PRODUCT EVENT**, **FEEDBACK**. If the team skips this, optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups. This is the lesson the case study ends with: Measure decisions, not motion; combine analytics with evaluation and human evidence; experiment only within an explicit ethical boundary.

### 2. Completion Rate Can Be Harmful If Completion Includes Accidental Approvals

Completion rate can be harmful if completion includes accidental approvals or excludes people who could not operate the interface. This is visible in the drawing as **USER OUTCOME**, **PRODUCT EVENT**, **FEEDBACK**. Without this step, optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups. In the walkthrough, The team sees that completion alone rewards speed and may hide accidental approval, so it defines informed decision quality and cancellation as guardrails..

### 3. With A Product Decision And User Outcome, Then Define

This step asks the team to start with a product decision and user outcome, then define the smallest evidence that could responsibly support it. The diagram shows this through **USER OUTCOME**, **PRODUCT EVENT**, **ACCESSIBILITY EVIDENCE**, which make the abstract step visible and testable. Collect the minimum events needed for a stated decision. Preserve the lesson, evidence, model, policy, and interface versions needed to reproduce the issue without demanding sensitive data. If the team skips this, optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups. Maya's case makes this concrete: Acme considers changing an approval button from Review and approve to Continue because a prototype shows more task completions.

### 4. Metric Semantics, Denominator, Exclusions, Slices, Retention, Access, And Known Failure

Here the product must write metric semantics, denominator, exclusions, slices, retention, access, and known failure modes before instrumentation. In the drawing, **DENOMINATOR**, **EXCLUSIONS**, **SLICE** carry this responsibility. Every metric needs an operational definition, numerator, denominator, exclusions, eligibility, time window, content and software versions, and meaningful slices. Without this step, optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups. The result — Evidence improves comprehension without manipulating Maya into a faster but less informed decision. — depends on getting this right.

### 5. Connect Privacy-minimized Product Events With Controlled Evaluations, Qualitative Feedback, Accessibility

The diagram enforces this by showing the team how to connect privacy-minimized product events with controlled evaluations, qualitative feedback, accessibility evidence, and incident records. The visual anchors are **ACCESSIBILITY EVIDENCE**, **PRODUCT EVENT**, **FEEDBACK**; without them the step would be invisible to the user. Product analytics asks what people did in the interface; evaluation asks how well the system performed on defined cases; feedback asks what people report; research explores why. Prefer semantic events such as approval reviewed or recovery completed over raw clickstreams, keystrokes, prompt contents, disability inference, or full session replay. The case study shows the risk: optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups. This is the lesson the case study ends with: Measure decisions, not motion; combine analytics with evaluation and human evidence; experiment only within an explicit ethical boundary.

### 6. Review Experiment Risk, Consent, Allocation, Guardrails, Sample Sufficiency, Stop Rules

This is the discipline that makes the product review experiment risk, consent, allocation, guardrails, sample sufficiency, stop rules, rollback, and affected groups before exposure. This idea sits on **EXPERIMENT** and reaches the rest of the diagram through **EXPERIMENT**, **CONSENT**, **STOP RULE**. Experiments require risk classification. Cosmetic ordering may be low risk; approval language, disclosure, accessibility, privacy, pricing, notification urgency, or safety controls can materially affect people and deserve review, consent or exclusion, guardrails, and early stop rules. Missing this is how products end up with optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups. In the walkthrough, The team sees that completion alone rewards speed and may hide accidental approval, so it defines informed decision quality and cancellation as guardrails..
![A privacy control center explains data purposes, categories, memory scopes, retention, connected apps, export, and deletion; consent is versioned and deletion propagates through primary stores, vectors, caches, logs, and backup schedules with verification.](../diagrams/218-privacy-consent-memory-settings-deletion.png)

Diagram 218 — *Privacy controls, consent, memory settings, and deletion* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 7. Publish Results With Uncertainty, Negative Findings, Version Manifest, Practical Effect

The team must publish results with uncertainty, negative findings, version manifest, practical effect, ethics review, and follow-up actions before the interface can be trustworthy. The diagram shows this through **VERSION**, **SAFETY REVIEW**, **RISK REVIEW**, which make the abstract step visible and testable. A system that ignores this will eventually face optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups. The danger the case warns about, Acme considers changing an approval button from Review and approve to Continue because a prototype shows more task completions. should make this clear.

### 8. The standard in practice

The lesson is not a perfect prototype; it is a product contract. Improve an agentic product with honest evidence while protecting learners and users from manipulative measurement and unsafe experiments.. The diagram makes that contract visible through **USER OUTCOME**, **PRODUCT EVENT**, **FEEDBACK**, so the team can argue about the contract before choosing a framework. The contract is not framework-specific; it is the set of observable promises the product makes to the person using it. Maya's case warns that optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups. The practical standard is this: Measure decisions, not motion; combine analytics with evaluation and human evidence; experiment only within an explicit ethical boundary.

### 9. The Next.js and Python surfaces

The same contract appears in both stacks, but the boundary moves with the architecture.
**In Next.js / React:**
- Create a small typed analytics vocabulary from meaningful product transitions; redact payloads at the server boundary and disable optional analytics until the proper choice is recorded.
- Build feedback forms that attach stable lesson, content, diagram, experiment, and interface versions while making free-text details optional and warning against sensitive information.
- Resolve experiment assignment on a trusted server, expose a debug receipt to authorized staff, preserve accessibility, and include an immediate kill switch and deterministic fallback.
- Keep the most sensitive payloads and policy decisions on the server and stream only user-visible, safe view models to client components.
**In Python / FastAPI:**
- Define metric specifications in code or versioned configuration with event eligibility, numerator, denominator, exclusions, dimensions, minimum sample rules, privacy class, and owner.
- Join product events to evaluation and feedback through opaque IDs and controlled access rather than copying raw conversations into an analytics warehouse.
- Run slice, missingness, duplicate, allocation, guardrail, and rollback checks; label synthetic and illustrative datasets so they cannot be mistaken for observed performance.
- Treat every framework callback or protocol event as raw input; validate and transform it into the product's own event vocabulary before it reaches the reducer or domain model.
Both implementations must avoid the same trap: optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups.

### 10. Analogy

A teacher should not judge a lesson only by how many students reached the last page. They also examine understanding, barriers, skipped questions, different student needs, and whether the test itself was fair. The analogy keeps the lesson grounded. The diagram's **USER OUTCOME** plays the same role as the central object in the analogy: it must be visible, labeled, and trustworthy without the user having to infer meaning from a long narrative. The parallel works because both situations require separating the object from the record, the attempt from the proof, and the promise from the evidence.

---

## Case study — Maya

Acme considers changing an approval button from Review and approve to Continue because a prototype shows more task completions.

### The walkthrough

1. The team sees that completion alone rewards speed and may hide accidental approval, so it defines informed decision quality and cancellation as guardrails.
2. Risk review flags the vague Continue label as a material consent change and excludes it from an ordinary growth experiment.
3. Accessible moderated research and controlled evaluation show that the explicit label improves consequence understanding despite one extra second of review.
4. Acme keeps the understandable control, publishes the negative conversion result, and tests safer improvements to the decision summary instead.

### The result

Evidence improves comprehension without manipulating Maya into a faster but less informed decision.

### The danger

Optimizing clicks or completion can reward deceptive labels, inaccessible flows, notification pressure, privacy overcollection, and hidden harm to smaller groups.

### The takeaway

Measure decisions, not motion; combine analytics with evaluation and human evidence; experiment only within an explicit ethical boundary.

---

## Composition

The picture is a single-view explainer for *Product analytics, feedback, evaluation, and experiment ethics*. On the left, the diagram shows USER OUTCOME feeding PRODUCT EVENT, FEEDBACK, QUALITY EVAL, SAFETY REVIEW, ACCESSIBILITY EVIDENCE. At the top, mETRIC CARD includes DEFINITION, NUMERATOR, DENOMINATOR, EXCLUSIONS, SLICE, WINDOW, VERSION. In the center, eXPERIMENT gate CONSENT, RISK REVIEW, FAIR ALLOCATION, STOP RULE, GUARDRAIL, DEBRIEF. To the right, coral DARK PATTERN, VANITY METRIC, HIDDEN HARM, EXAMPLE AS FACT. The eye travels from **USER OUTCOME** through the central flow to **EXAMPLE AS FACT**, with the contrast between coral risk paths and teal recovery paths giving the reader the core message at a glance.

## Element by element

- **USER OUTCOME** — the user outcome feeding PRODUCT EVENT, FEEDBACK, QUALITY EVAL, SAFETY REVIEW, ACCESSIBILITY EVIDENCE..
- **PRODUCT EVENT** — a privacy-minimized record of a meaningful product transition.
- **FEEDBACK** — the learner or user report that captures confusion, barrier, or incident.
- **QUALITY EVAL** — a controlled assessment of how well the system performed on defined cases.
- **SAFETY REVIEW** — the review of outputs and interactions for harm, risk, or policy violation.
- **ACCESSIBILITY EVIDENCE** — the record that the interface works across input methods and assistive technologies.
- **METRIC CARD** — the exposed definition of a measure, including numerator, denominator, exclusions, slice, window, and version.
- **DEFINITION** — one of the cards named by **METRIC CARD**; this is the **DEFINITION** card.
- **NUMERATOR** — one of the cards named by **METRIC CARD**; this is the **NUMERATOR** card.
- **DENOMINATOR** — one of the cards named by **METRIC CARD**; this is the **DENOMINATOR** card.
- **EXCLUSIONS** — one of the cards named by **METRIC CARD**; this is the **EXCLUSIONS** card.
- **SLICE** — one of the cards named by **METRIC CARD**; this is the **SLICE** card.
- **WINDOW** — one of the cards named by **METRIC CARD**; this is the **WINDOW** card.
- **VERSION** — one of the cards named by **METRIC CARD**; this is the **VERSION** card.
- **EXPERIMENT** — a controlled change that requires risk review, consent, guardrails, and debrief.
- **CONSENT** — the informed, specific, and revocable user choice before data or authority is granted.
- **RISK REVIEW** — one of the items named by **EXPERIMENT**; this is the **RISK REVIEW** item.
- **FAIR ALLOCATION** — one of the items named by **EXPERIMENT**; this is the **FAIR ALLOCATION** item.
- **STOP RULE** — one of the items named by **EXPERIMENT**; this is the **STOP RULE** item.
- **GUARDRAIL** — one of the items named by **EXPERIMENT**; this is the **GUARDRAIL** item.
- **DEBRIEF** — one of the items named by **EXPERIMENT**; this is the **DEBRIEF** item.
- **DARK PATTERN** — the dark pattern VANITY METRIC, HIDDEN HARM, EXAMPLE AS FACT..
- **VANITY METRIC** — the vanity metric DARK PATTERN, VANITY METRIC, HIDDEN HARM, EXAMPLE AS FACT..
- **HIDDEN HARM** — the hidden harm DARK PATTERN, VANITY METRIC, HIDDEN HARM, EXAMPLE AS FACT..
- **EXAMPLE AS FACT** — the example as fact DARK PATTERN, VANITY METRIC, HIDDEN HARM, EXAMPLE AS FACT..

---

## Colour and flow semantics

The course visual grammar applies directly to this diagram.

- **Cobalt platform** — A browser surface, state store, component catalog, product boundary, workspace, or learning-platform region. Here the cobalt surface under **USER OUTCOME** and the surrounding workspace frames the product boundary; it tells the reader that this is a bounded product region, not an uncontrolled chat surface. It marks the product's responsibility to keep the user's workspace distinct from raw model output or runtime internals.

- **Cyan arrow** — A typed event, validated state update, user action, artifact reference, notification, or navigation path. Cyan arrows carry the flow of events, updates, and proposals from left to right, linking the typed cards and records to the reducer or next gate. When the reader sees cyan, they should expect a deliberate, validated transition rather than an accidental or hidden connection.

- **Teal arrow** — Authoritative state, accessible completion, informed consent, safe approval, preserved work, or verified recovery. Teal marks the authoritative and safe path, such as the committed receipt or restored state, distinguishing it from the raw request. This color tells the reader that the product has enough evidence and authority to proceed safely.

- **Coral path** — Conflict, stale UI, unsafe rendering, deceptive state, expired approval, privacy failure, lost work, or blocked action. Coral marks the conflict, stale state, or blocked action that appears when a control is missing or bypassed. It signals that the product should pause, surface the conflict, and offer a recovery path rather than proceed silently.

- **White card** — An event, component, stage, proposal, artifact, receipt, consent record, lesson, checkpoint, or recovery option. **PRODUCT EVENT**, **METRIC CARD** appear as white cards, showing that they are records, proposals, or evidence rather than raw data or system internals. The white background separates user-meaningful records from raw system logs or generated text.

The overall flow moves from the initiating actor or request, through validation and reduction, toward either the teal recovery or completion path or the coral failure path. The color of each arrow and card is a trust cue, not a decoration.

---

## How to present it

- **Start with the user moment.** Acme considers changing an approval button from Review and approve to Continue because a prototype shows more task completions. Ask the room what they need to see to feel in control. Invite someone to describe the moment before any solution appears.

- **Point at USER OUTCOME and ask what it represents.** Then trace the flow from there through the next two or three elements, naming the color and direction of each arrow. Encourage them to name the incoming trigger, the visible state, and the decision the product must make.

- **Point at USER OUTCOME for step 1.** With A Product Decision And User Outcome, Then Define. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at DENOMINATOR for step 2.** Metric Semantics, Denominator, Exclusions, Slices, Retention, Access, And Known Failure. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at ACCESSIBILITY EVIDENCE for step 3.** Connect Privacy-minimized Product Events With Controlled Evaluations, Qualitative Feedback, Accessibility. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at EXPERIMENT for step 4.** Review Experiment Risk, Consent, Allocation, Guardrails, Sample Sufficiency, Stop Rules. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Point at VERSION for step 5.** Publish Results With Uncertainty, Negative Findings, Version Manifest, Practical Effect. Ask what observable evidence the product would produce if this step worked correctly. Have the room identify the color of the path leaving this element and what it tells a user about trust.

- **Use the analogy.** A teacher should not judge a lesson only by how many students reached the last page. They also examine understanding, barriers, skipped questions, different student needs, and whether the test itself was fair. Draw the parallel to the diagram and ask what would break if the two situations were handled the same way.

- **Tell the case study.** Acme considers changing an approval button from Review and approve to Continue because a prototype shows more task completions Walk through the walkthrough and stop at the moment the old design would have failed. Pause at the step where the old design would have failed and ask how the new interface prevents it.

- **Run the lab.** Write a measurement plan for the visual course website with six outcomes, twelve minimized events, metric definitions and denominators, consent and retention, accessibility slices, feedback taxonomy, evaluation joins, three experiment risk classes, guardrails, stop rules, rollback, and a statement marking every sample number as illustrative. Ask pairs to present one part of the diagram and explain how the other parts reference it without merging their identities.

- **Pose the checkpoint.** If an experiment increases task completion, is it automatically a product improvement? Let the room answer before confirming the principle. Collect answers, then confirm the principle and note any exceptions the team should watch for.

- **Close on the contract.** Measure decisions, not motion; combine analytics with evaluation and human evidence; experiment only within an explicit ethical boundary. Ask the team what their own product's equivalent of the contract would be.

---

## Lab and checkpoint

**Lab:** Write a measurement plan for the visual course website with six outcomes, twelve minimized events, metric definitions and denominators, consent and retention, accessibility slices, feedback taxonomy, evaluation joins, three experiment risk classes, guardrails, stop rules, rollback, and a statement marking every sample number as illustrative.

**Checkpoint:** If an experiment increases task completion, is it automatically a product improvement?

**Answer:** No. Completion may rise through confusion, coercion, accidental approval, inaccessible exclusion, or privacy pressure. Examine understanding, safety, accessibility, recovery, user control, and practical effect with clear denominators.

---

## Glossary

- **Operational definition** — exact rule turning observations into a metric
- **Guardrail** — measure that must remain acceptable during change
- **Dark pattern** — interface designed to manipulate a choice against the person's interests

---

## Sources

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## Related lessons

- Diagram 208 — Accessibility, plain language, uncertainty, and trust cues
- Diagram 215 — Glossary, citations, search, prerequisites, and cross-links
- Diagram 218 — Privacy controls, consent, memory settings, and deletion

---