# Diagram 184 — User outcome, clarity, control, and recovery quality

![A technical result is evaluated for correctness, freshness, clarity, actionability, user control, accessibility, and recovery, with explicit progress, evidence, approval, cancel, retry, edit, help, and receipt controls.](../diagrams/184-user-outcome-control-recovery-quality.png)

**Module:** Quality at every stage
**Role in the course:** Measure the component that failed instead of grading only the final sentence and guessing where the defect began.
**Layout:** The diagram shows TECHNICAL RESULT entering USER EXPERIENCE gates CORRECT, CURRENT, CLEAR, ACTIONABLE, CONTROLLED, ACCESSIBLE, RECOVERABLE; it also includes PROGRESS, EVIDENCE, APPROVAL, CANCEL, RETRY, EDIT, HUMAN HELP, RECEIPT cards.

---

## At a glance

**Judge success from the user's real outcome and ability to understand, control, and recover from the system.**

- Define the real user job, acceptable outcomes, unacceptable outcomes, and authoritative completion evidence.
- Evaluate correctness, freshness, clarity, actionability, uncertainty, and evidence presentation separately.
- Test approvals, steering, cancel, retry, edit, undo, escalation, and preserved partial work as explicit controls.
- A RETRY path shows the failure the design must catch before it reaches the user.

---

## What the diagram teaches

### 1. Judge success from the user's real outcome and control

Agent quality ends with a person or business outcome, not an HTTP status. The system may be technically healthy while the user receives stale evidence, confusing language, no clear action, a hidden partial failure, an inaccessible control, or no safe recovery. Define outcome measures from what users care about: was the problem resolved, was the evidence current and understandable, were consequential actions visible and approved, could the user correct assumptions, did progress match reality, was partial work preserved, and could failure be recovered without repeating harm? Combine system evidence with carefully designed user feedback, task completion, support escalation, correction, cancellation, and appeal records. Avoid dark metrics such as longer session time when the product goal is fast resolution. The diagram exists so the team can judge success from the user's real outcome and ability to understand, control, and recover from the system.
![A proposed action passes tool schema, policy, approval, and idempotency gates before a business effect, with receipts detecting wrong tools, invalid arguments, denied calls, and duplicate effects.](../diagrams/182-tool-policy-business-effect-quality.png)

Diagram 182 — *Tool contracts, policy decisions, and business effects* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 2. Define the real user job, acceptable outcomes, unacceptable outcomes,

Define the real user job, acceptable outcomes, unacceptable outcomes, and authoritative completion evidence. Combine system evidence with carefully designed user feedback, task completion, support escalation, correction, cancellation, and appeal records. Define outcome measures from what users care about: was the problem resolved, was the evidence current and understandable. In the diagram, this is represented by **EVIDENCE**. The case study where Acme correctly detects that Maya's answer used stale evidence, but the interface shows only 'Something went wrong' and discards the useful research already completed makes the risk concrete: a dashboard can report 99% successful requests while users face inaccessible approval controls, lost partial work, or meaningless error messages. When this step is done well, the system turns a backend failure into an understandable, recoverable user experience.

### 3. Evaluate correctness, freshness, clarity, actionability, uncertainty, and evidence presentation separately.

In the diagram, this is represented by **CORRECT** and **EVIDENCE**. Evaluate correctness, freshness, clarity, actionability, uncertainty, and evidence presentation separately. Define outcome measures from what users care about: was the problem resolved, was the evidence current and understandable. Do not expose private chain-of-thought as an explanation; provide concise decision summaries, evidence, actions, uncertainty, and receipts instead. The case study where Acme correctly detects that Maya's answer used stale evidence, but the interface shows only 'Something went wrong' and discards the useful research already completed shows the value: the system turns a backend failure into an understandable, recoverable user experience. Skip it, and a dashboard can report 99% successful requests while users face inaccessible approval controls, lost partial work, or meaningless error messages. The takeaway is clear: quality is the user's understood, controlled, recoverable outcome - not merely a green backend span.

### 4. Test approvals, steering, cancel, retry, edit, undo, escalation, and preserved

Define outcome measures from what users care about: was the problem resolved, was the evidence current and understandable. This is why the step is non-negotiable: test approvals, steering, cancel, retry, edit, undo, escalation, and preserved partial work as explicit controls. Combine system evidence with carefully designed user feedback, task completion, support escalation, correction, cancellation, and appeal records. In the diagram, this is represented by **APPROVAL** and **CANCEL**, near **RETRY**. The case study where Acme correctly detects that Maya's answer used stale evidence, but the interface shows only 'Something went wrong' and discards the useful research already completed proves it: the system turns a backend failure into an understandable, recoverable user experience. If the team omits this, a dashboard can report 99% successful requests while users face inaccessible approval controls, lost partial work, or meaningless error messages.

### 5. Include accessibility, abandonment, correction, appeal, and unresolved cases in measurements

Include accessibility, abandonment, correction, appeal, and unresolved cases in measurements and denominators. Evaluate accessibility with keyboard, text alternatives, focus, readable status, and reduced motion. Combine system evidence with carefully designed user feedback, task completion, support escalation, correction, cancellation, and appeal records. In the diagram, this is represented by **CORRECT**. The case study where Acme correctly detects that Maya's answer used stale evidence, but the interface shows only 'Something went wrong' and discards the useful research already completed makes the risk concrete: a dashboard can report 99% successful requests while users face inaccessible approval controls, lost partial work, or meaningless error messages. When this step is done well, the system turns a backend failure into an understandable, recoverable user experience.

### 6. Connect product feedback to traces and artifacts with consent

Connect product feedback to traces and artifacts with consent and privacy controls, then turn recurring failures into cases. Evaluate accessibility with keyboard, text alternatives, focus, readable status, and reduced motion. Combine system evidence with carefully designed user feedback, task completion, support escalation, correction, cancellation, and appeal records. The case study where Acme correctly detects that Maya's answer used stale evidence, but the interface shows only 'Something went wrong' and discards the useful research already completed shows the value: the system turns a backend failure into an understandable, recoverable user experience. Skip it, and a dashboard can report 99% successful requests while users face inaccessible approval controls, lost partial work, or meaningless error messages. The takeaway is clear: quality is the user's understood, controlled, recoverable outcome - not merely a green backend span.

### 7. Putting it together

Taken together, these steps turn the objective "judge success from the user's real outcome and ability to understand, control, and recover from the system" into an operating contract. Define the real user job, acceptable outcomes, unacceptable outcomes, and authoritative completion evidence; Evaluate correctness, freshness, clarity, actionability, uncertainty, and evidence presentation separately; Test approvals, steering, cancel, retry, edit, undo, escalation, and preserved partial work as explicit controls. The remaining steps extend this: Include accessibility, abandonment, correction, appeal, and unresolved cases in measurements and denominators; Connect product feedback to traces and artifacts with consent and privacy controls, then turn recurring failures into cases. The case of Acme correctly detects that Maya's answer used stale evidence, but the interface shows only 'Something went wrong' and discards the useful research already completed shows how quickly a dashboard can report 99% successful requests while users face inaccessible approval controls, lost partial work, or meaningless error messages. The durable lesson is quality is the user's understood, controlled, recoverable outcome - not merely a green backend span.

### Analogy

A flight is not successful merely because the aircraft landed. The passenger must reach the correct destination, retrieve baggage, understand changes, receive assistance, and have a remedy when the airline makes a mistake.

### The Next.js surface

In the Next.js surface, the same contract appears through framework-specific patterns. Render authoritative stage, artifact, approval, failure, and recovery state from typed events; never infer business completion from a loading animation. Instrument user controls such as cancel, retry, edit, escalate, and correction with product events that link to receipts without capturing private text by default. Run accessibility and recovery scenario tests for keyboard, screen reader labels, focus order, reconnect, partial success, and expired approvals.

### The Python surface

In the Python surface, the same contract is enforced with typed models and tests. Model user-visible status and recovery options as typed workflow state so API responses remain consistent with durable business state. Emit outcome and recovery events with reason categories, artifact references, and trace support codes, then aggregate them with complete denominators. Create end-to-end cases that assert backend state, user-facing event sequence, accessible control availability, and final receipt together.

---

## Case study — Acme's 'Something went wrong' stale-answer screen

Acme correctly detects that Maya's answer used stale evidence, but the interface shows only 'Something went wrong' and discards the useful research already completed.

### The walkthrough

1. The outcome evaluation marks diagnosis correct but clarity, preservation, and recovery as failed.
2. The redesigned flow keeps the valid research artifact and labels the stale policy stage precisely.
3. Maya can retry only retrieval, inspect current evidence, cancel, or send the case to a human.
4. The correction receipt explains what changed without revealing hidden model reasoning.

### The result

The system turns a backend failure into an understandable, recoverable user experience.

### The danger

A dashboard can report 99% successful requests while users face inaccessible approval controls, lost partial work, or meaningless error messages.

### The takeaway

Quality is the user's understood, controlled, recoverable outcome - not merely a green backend span.

---

## Composition

A TECHNICAL RESULT enters from the left into a row of USER EXPERIENCE gates: CORRECT, CURRENT, CLEAR, ACTIONABLE, CONTROLLED, ACCESSIBLE, and RECOVERABLE. Beneath these gates, a set of control cards—PROGRESS, EVIDENCE, APPROVAL, CANCEL, RETRY, EDIT, HUMAN HELP, and RECEIPT—show the affordances a user needs. One path descends as a coral TECHNICALLY GREEN / USER FAILED card, while another exits to the right as a teal UNDERSTOOD AND RECOVERED card. The composition is a usability filter: the backend result enters from the left, passes through human-centered quality gates, and either recovers or fails visibly.

## Element by element

- **TECHNICAL RESULT** — The **TECHNICAL RESULT** is the backend output before it is judged for user experience and recovery.
- **USER EXPERIENCE** — The **USER EXPERIENCE** is the stage that turns a TECHNICAL RESULT into a human-centered, understandable, and recoverable outcome.
- **CORRECT** — The **CORRECT** is the user-experience gate that checks the answer matches the user's real question and the evidence.
- **CURRENT** — The **CURRENT** is the user-experience gate that checks the evidence is not stale or outdated.
- **CLEAR** — The **CLEAR** is the user-experience gate that checks the explanation is understandable to the user.
- **ACTIONABLE** — The **ACTIONABLE** is the user-experience gate that checks the user has a useful next step.
- **CONTROLLED** — The **CONTROLLED** is the user-experience gate that checks the user has steering, approval, and recovery controls.
- **ACCESSIBLE** — The **ACCESSIBLE** is the user-experience gate that checks the interface works for users with different abilities and devices.
- **RECOVERABLE** — The **RECOVERABLE** is the user-experience gate that checks the user can recover from errors or stale answers.
- **PROGRESS** — The **PROGRESS** is the control card that shows the user where they are in the workflow.
- **EVIDENCE** — The **EVIDENCE** is the support for a claim or decision, shown to the user as concise summaries, artifacts, and citations.
- **APPROVAL** — The **APPROVAL** is the bound human authorization required for a consequential action.
- **CANCEL** — The **CANCEL** is the control that lets the user stop a workflow without harmful side effects.
- **RETRY** — The **RETRY** is the coral arrow showing work multiplied by a repeated attempt.
- **EDIT** — The **EDIT** is the control that lets the user change an input or parameter before continuing.
- **HUMAN HELP** — The **HUMAN HELP** is the control that lets the user route the case to a qualified person for support.
- **RECEIPT** — The **RECEIPT** is the durable, user-visible record of the completed business outcome.
- **TECHNICALLY GREEN USER FAILED** — The **TECHNICALLY GREEN USER FAILED** is the coral card showing that the backend succeeded while the user still failed to get a useful result.
- **UNDERSTOOD** — The **UNDERSTOOD** is the first half of the teal UNDERSTOOD AND RECOVERED outcome: the user can make sense of the result.
- **RECOVERED** — The **RECOVERED** is the second half of the teal UNDERSTOOD AND RECOVERED outcome: the user can recover from problems.

---

## Colour and flow semantics

- **Cobalt platform** — a service, stage, dataset, quality gate, budget, release lane, or incident-control boundary. In this diagram it appears on **CONTROLLED**.
- **Cyan arrow** — a request, propagated context, telemetry signal, evaluation flow, or candidate release path. In this diagram it appears on **TECHNICAL RESULT**, **USER EXPERIENCE**, **CORRECT**, **CLEAR**, **ACCESSIBLE**, **PROGRESS**, **APPROVAL**, **CANCEL** and others.
- **Teal arrow** — a healthy result, matched evidence, safe promotion, controlled degradation, recovery, or verified learning path. In this diagram it appears on **CURRENT**, **ACTIONABLE**, **RECOVERABLE**, **UNDERSTOOD**, **RECOVERED**, **UNDERSTOOD AND RECOVERED**.
- **Coral path** — a broken trace, failed assertion, regression, overload, unsafe outcome, rollback, alert, or incident path. In this diagram it appears on **RETRY**, **TECHNICALLY GREEN USER FAILED**, **TECHNICALLY GREEN / USER FAILED**.
- **White card** — a span, event, metric, log, resource, case, score, budget, version, release, runbook, action, or regression record. In this diagram it appears on **EVIDENCE**, **RECEIPT**.

The overall flow moves from the inputs on the left through the quality at every stage stages and exits as either a teal healthy path or a coral failure path. White cards carry the records, cobalt platforms hold the boundaries, and the cyan arrows show propagation and requests.

---

## How to present it

- Start with the operational question the team actually needs to answer. Point at the central element and ask what a regulator, evaluator, or support operator would ask about this outcome, and which signal type would best answer it.
- Ask the room what the team would need to know before approving the next release. Point at **EVIDENCE** and ask what would change if this step were skipped? Use the case study to make the failure concrete.
- Have the group list the operational decisions this stage informs. Highlight **CORRECT** and **EVIDENCE** and ask what real decision does this evidence support? Use the case study to make the failure concrete.
- Ask what evidence would change the route a support ticket takes. Trace with your finger **APPROVAL** and **CANCEL** and ask what would a missing or corrupted value look like here? Use the case study to make the failure concrete.
- Get the room to name the owner who would need this evidence in an incident. Put a marker on **CORRECT** and ask who owns the evidence produced at this step? Use the case study to make the failure concrete.
- Ask what would need to be true for the team to skip this stage safely. Ask the room to locate the trace and ask which downstream stage would fail if this step were wrong? Use the case study to make the failure concrete.
- Use the analogy. A flight is not successful merely because the aircraft landed. Ask the room where the equivalent tracking number, queue, or ledger is in their own system, and where it would first break.
- Tell the case study — Acme's 'Something went wrong' stale-answer screen. Walk through the walkthrough and stop at the moment the failure first becomes visible. Ask what signal, gate, or version field would have caught it earlier.
- Run the lab. Write one end-to-end evaluation for a stale answer. Include backend evidence, visible stage sequence, accessible error text, preserved artifact, four recovery controls, human handoff, correction receipt, and denominators for abandoned and unresolved cases. Have each group label the fields that are captured, hashed, redacted, or omitted.
- Pose the checkpoint. Should user outcome quality be measured only with a satisfaction survey? Let the room answer before confirming with the answer. Then ask what the team would change in the next build based on the answer.
- Before moving on, ask the room to trace one healthy teal path and one coral path through the diagram, naming the evidence that flips the colour at each stage.
- Close on the contract. Quality is the user's understood, controlled, recoverable outcome - not merely a green backend span. Make the group write one sentence that ties the lesson to their own system.

---

## Lab and checkpoint

**Lab:** Write one end-to-end evaluation for a stale answer. Include backend evidence, visible stage sequence, accessible error text, preserved artifact, four recovery controls, human handoff, correction receipt, and denominators for abandoned and unresolved cases.

**Checkpoint:** Should user outcome quality be measured only with a satisfaction survey?

**Answer:** No. Surveys can help, but combine them with task resolution, corrections, recovery, abandonment, escalation, accessibility, durable receipts, and system evidence.

---

## Glossary

- **Outcome quality** — whether the user's real job was completed well
- **Recovery affordance** — visible safe action after failure
- **Abandonment** — user leaves before successful resolution

---

## Sources

- [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457)

---

## Related lessons

- Diagram 176 — Business outcomes, artifacts, receipts, and trace references
- Diagram 182 — Tool contracts, policy decisions, and business effects
- Diagram 193 — Alerts, ownership, triage, and runbooks

---
