# Diagram 177 — The anatomy of a useful evaluation case

![A versioned evaluation case defines input, context, expected evidence, permitted actions, forbidden outcomes, rubric, scorers, slices, and version pins before judging outputs, traces, artifacts, and tool receipts.](../diagrams/177-evaluation-case-anatomy.png)

**Module:** Evaluation design
**Role in the course:** Convert vague confidence into repeatable cases, assertions, calibrated judgments, meaningful slices, and honest uncertainty.
**Layout:** The diagram builds one EVAL CASE card with compartments INPUT, CONTEXT, EXPECTED EVIDENCE, PERMITTED ACTIONS, FORBIDDEN OUTCOMES, RUBRIC, SCORERS, SLICE TAGS, and VERSION PINS; it also send it through SYSTEM UNDER TEST to OUTPUT, TRACE, ARTIFACT, TOOL RECEIPTS, then a SCORECARD with PASS, FAIL.

---

## At a glance

**Write an evaluation case that can diagnose behavior and be rerun fairly after the system changes.**

- Name the user goal, starting state, relevant context, and unacceptable outcomes before writing an expected answer.
- Specify required evidence, permitted tools or effects, forbidden actions, artifact expectations, and recovery behavior.
- Separate deterministic assertions from rubric-scored qualities and identify which evidence each scorer may inspect.
- A FAIL path shows the failure the design must catch before it reaches the user.

---

## What the diagram teaches

### 1. Write evaluation cases that diagnose behavior fairly

An evaluation case is more than a question and a preferred sentence. It defines the input, starting context, user goal, relevant evidence, permitted actions, forbidden outcomes, expected artifacts, scoring rubric, scorer configuration, slice tags, and exact versions needed for replay. Some expectations are deterministic: a schema must validate, a forbidden tool must not run, a citation must point to the selected document version, or a transaction must remain unchanged. Other expectations allow several good answers and need a rubric for correctness, groundedness, clarity, or recovery. The case should state what evidence a scorer may inspect: final text, retrieved documents, trace stages, policy receipts, tool effects, artifacts, or user-control events. Keep the dataset versioned and reviewable. The diagram exists so the team can write an evaluation case that can diagnose behavior and be rerun fairly after the system changes.

### 2. Name the user goal, starting state, relevant context, and unacceptable

Name the user goal, starting state, relevant context, and unacceptable outcomes before writing an expected answer. The case should state what evidence a scorer may inspect: final text, retrieved documents, trace stages, policy receipts, tool effects, artifacts, or user-control events. It defines the input, starting context, user goal, relevant evidence, permitted actions, forbidden outcomes, expected artifacts. In the diagram, this is represented by **CONTEXT**. The case study where Maya asks whether a refund exception is still allowed makes the risk concrete: a case containing only prompt, reference answer, and exact-string match can punish valid answers while missing unsafe tool use, stale evidence, or wrong business effects. When this step is done well, a future candidate can be judged on evidence, authority, and user outcome rather than whether it repeats one reference paragraph.

### 3. Specify required evidence, permitted tools or effects, forbidden actions, artifact

In the diagram, this is represented by **ARTIFACT**. Specify required evidence, permitted tools or effects, forbidden actions, artifact expectations, and recovery behavior. Other expectations allow several good answers and need a rubric for correctness, groundedness, clarity, or recovery. It defines the input, starting context, user goal, relevant evidence, permitted actions, forbidden outcomes, expected artifacts. The case study where Maya asks whether a refund exception is still allowed shows the value: a future candidate can be judged on evidence, authority, and user outcome rather than whether it repeats one reference paragraph. Skip it, and a case containing only prompt, reference answer, and exact-string match can punish valid answers while missing unsafe tool use, stale evidence, or wrong business effects. The takeaway is clear: define the whole situation, allowed behavior, forbidden outcomes, evidence, rubric, and versions.

### 4. Separate deterministic assertions from rubric-scored qualities and identify which evidence
![System evidence passes deterministic schema, citation, tool, effect, policy, and artifact assertions while flexible language quality is judged in a separate rubric lane.](../diagrams/178-deterministic-contracts-behavioral-assertions.png)

Diagram 178 — *Deterministic contracts, schemas, and behavioral assertions* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

It defines the input, starting context, user goal, relevant evidence, permitted actions, forbidden outcomes, expected artifacts. This is why the step is non-negotiable: separate deterministic assertions from rubric-scored qualities and identify which evidence each scorer may inspect. The case should state what evidence a scorer may inspect: final text, retrieved documents, trace stages, policy receipts, tool effects, artifacts, or user-control events. In the diagram, this is represented by **RUBRIC**. The case study where Maya asks whether a refund exception is still allowed proves it: a future candidate can be judged on evidence, authority, and user outcome rather than whether it repeats one reference paragraph. If the team omits this, a case containing only prompt, reference answer, and exact-string match can punish valid answers while missing unsafe tool use, stale evidence, or wrong business effects.

### 5. Tag meaningful slices, difficulty, risk, provenance, owner, creation reason,

Tag meaningful slices, difficulty, risk, provenance, owner, creation reason, and review date. An evaluation case is more than a question and a preferred sentence. A golden dataset means carefully maintained, not eternally true; policies, products, and acceptable behavior change, so cases need owners and review dates. In the diagram, this is represented by **REVIEW**. The case study where Maya asks whether a refund exception is still allowed makes the risk concrete: a case containing only prompt, reference answer, and exact-string match can punish valid answers while missing unsafe tool use, stale evidence, or wrong business effects. When this step is done well, a future candidate can be judged on evidence, authority, and user outcome rather than whether it repeats one reference paragraph.

### 6. Pin dataset, model, prompt, policy, retrieval corpus, index, tool, schema,

In the diagram, this is represented by **TOOL RECEIPTS**. Pin dataset, model, prompt, policy, retrieval corpus, index, tool, schema, and code versions for reproducible comparison. Some expectations are deterministic: a schema must validate, a forbidden tool must not run, a citation must point to the selected document version. It defines the input, starting context, user goal, relevant evidence, permitted actions, forbidden outcomes, expected artifacts. The case study where Maya asks whether a refund exception is still allowed shows the value: a future candidate can be judged on evidence, authority, and user outcome rather than whether it repeats one reference paragraph. Skip it, and a case containing only prompt, reference answer, and exact-string match can punish valid answers while missing unsafe tool use, stale evidence, or wrong business effects. The takeaway is clear: define the whole situation, allowed behavior, forbidden outcomes, evidence, rubric, and versions.

### 7. Putting it together

Taken together, these steps turn the objective "write an evaluation case that can diagnose behavior and be rerun fairly after the system changes" into an operating contract. Name the user goal, starting state, relevant context, and unacceptable outcomes before writing an expected answer; Specify required evidence, permitted tools or effects, forbidden actions, artifact expectations, and recovery behavior; Separate deterministic assertions from rubric-scored qualities and identify which evidence each scorer may inspect. The remaining steps extend this: Tag meaningful slices, difficulty, risk, provenance, owner, creation reason, and review date; Pin dataset, model, prompt, policy, retrieval corpus, index, tool, schema, and code versions for reproducible comparison. The case of Maya asks whether a refund exception is still allowed shows how quickly a case containing only prompt, reference answer, and exact-string match can punish valid answers while missing unsafe tool use, stale evidence, or wrong business effects. The durable lesson is define the whole situation, allowed behavior, forbidden outcomes, evidence, rubric, and versions.

### Analogy

A driving test includes the route, weather, vehicle, allowed maneuvers, automatic failures, examiner rubric, and score sheet; it is not just a destination and a preferred description of the trip.

### The Next.js surface

In the Next.js surface, the same contract appears through framework-specific patterns. Represent cases with a JSON Schema or TypeScript type and validate them on ingestion, including explicit forbidden outcomes and scorer evidence permissions. Build a review interface that shows case history, owner, slice tags, version diffs, expected evidence, and why the case entered the dataset. Keep eval execution in server-side jobs; stream progress and summarized scorecards to React without exposing private source material or hidden grader reasoning.

### The Python surface

In the Python surface, the same contract is enforced with typed models and tests. Define Pydantic models for Case, Expectation, Assertion, Rubric, Scorer, Slice, VersionManifest, and EvaluationResult. Load frozen fixtures for tools, retrieval, policy, and time so the same case can run deterministically when that is the evaluation goal. Store raw evidence separately from normalized scores and keep the scorer and rubric version with every judgment.

---

## Case study — Maya and the refund exception case

Maya asks whether a refund exception is still allowed. The current policy permits it only for a documented delivery failure and requires supervisor approval.

### The walkthrough

1. The case includes the customer situation, current policy document ID and version, and a synthetic delivery record.
2. It requires citation of current evidence and a supervisor-approval proposal before any refund effect.
3. It forbids use of the stale policy, invented delivery facts, direct payment execution, and disclosure of private account data.
4. Assertions inspect retrieval and tool receipts while a rubric scores the explanation and recovery choices.

### The result

A future candidate can be judged on evidence, authority, and user outcome rather than whether it repeats one reference paragraph.

### The danger

A case containing only prompt, reference answer, and exact-string match can punish valid answers while missing unsafe tool use, stale evidence, or wrong business effects.

### The takeaway

Define the whole situation, allowed behavior, forbidden outcomes, evidence, rubric, and versions.

---

## Composition

An EVAL CASE card sits at the left with internal compartments labeled INPUT, CONTEXT, EXPECTED EVIDENCE, PERMITTED ACTIONS, FORBIDDEN OUTCOMES, RUBRIC, SCORERS, SLICE TAGS, and VERSION PINS. A cyan arrow carries the case through a SYSTEM UNDER TEST toward the right, producing OUTPUT, TRACE, ARTIFACT, and TOOL RECEIPTS. These flow into a SCORECARD that shows PASS, FAIL, and REVIEW. Beside the main path, a coral UNDERSPECIFIED CASE card shows what happens when the case is missing required fields. The composition is a factory line: a complete, versioned case enters on the left, the system under test sits in the middle, and a judgment with evidence arrives on the right.

## Element by element

- **EVAL CASE** — The **EVAL CASE** is a card with compartments INPUT,.
- **INPUT** — The **INPUT** is a cyan request or propagation path that one EVAL CASE card with compartments ,.
- **CONTEXT** — The **CONTEXT** is a cyan request or propagation path.
- **EXPECTED EVIDENCE** — The **EXPECTED EVIDENCE** is a white record.
- **PERMITTED ACTIONS** — The **PERMITTED ACTIONS** is a cyan request or propagation path.
- **FORBIDDEN OUTCOMES** — The **FORBIDDEN OUTCOMES** is a white record.
- **RUBRIC** — The **RUBRIC** is an explicit criteria for a judgment.
- **SCORERS** — The **SCORERS** are the instruments that evaluate case evidence against a rubric or assertions.
- **SLICE TAGS** — The **SLICE TAGS** is a cyan request or propagation path.
- **VERSION PINS** — The **VERSION PINS** is a white record.
- **SYSTEM** — The **SYSTEM** is a TEST to OUTPUT,.
- **TEST** — The **TEST** is a TEST OUTPUT,.
- **OUTPUT** — The **OUTPUT** is a cyan request or propagation path that send it through SYSTEM UNDER TEST to ,.
- **TRACE** — The **TRACE** is a connected record of one request or workflow.
- **ARTIFACT** — The **ARTIFACT** is a ARTIFACT.
- **TOOL RECEIPTS** — The **TOOL RECEIPTS** is a white record.
- **SCORECARD** — The **SCORECARD** is the PASS, FAIL, or REVIEW judgment produced for the case.
- **PASS** — The **PASS** is a cyan request or propagation path that then a SCORECARD with ,.
- **FAIL** — The **FAIL** is the coral gate outcome where the candidate fails an offline contract check.
- **REVIEW** — The **REVIEW** is the coral gate outcome where a candidate needs more evidence before release.
- **UNDERSPECIFIED CASE** — The **UNDERSPECIFIED CASE** is a case that is missing required fields and cannot be used as a fair test.

---

## Colour and flow semantics

- **Cyan arrow** — a request, propagated context, telemetry signal, evaluation flow, or candidate release path. In this diagram it appears on **INPUT**, **CONTEXT**, **PERMITTED ACTIONS**, **SLICE TAGS**, **SYSTEM**, **TEST**, **OUTPUT**, **PASS** and others.
- **Coral path** — a broken trace, failed assertion, regression, overload, unsafe outcome, rollback, alert, or incident path. In this diagram it appears on **FAIL**, **UNDERSPECIFIED CASE**.
- **White card** — a span, event, metric, log, resource, case, score, budget, version, release, runbook, action, or regression record. In this diagram it appears on **EVAL CASE**, **EXPECTED EVIDENCE**, **FORBIDDEN OUTCOMES**, **RUBRIC**, **SCORERS**, **VERSION PINS**, **TRACE**, **ARTIFACT** and others.

The overall flow moves from the inputs on the left through the evaluation design stages and exits as either a teal healthy path or a coral failure path. White cards carry the records, cobalt platforms hold the boundaries, and the cyan arrows show propagation and requests.

---

## How to present it

- Start with the operational question the team actually needs to answer. Point at the central element and ask what a regulator, evaluator, or support operator would ask about this outcome, and which signal type would best answer it.
- Ask the room what the team would need to know before approving the next release. Point at **CONTEXT** and ask what would change if this step were skipped? Use the case study to make the failure concrete.
- Have the group list the operational decisions this stage informs. Highlight **ARTIFACT** and ask what real decision does this evidence support? Use the case study to make the failure concrete.
- Ask what evidence would change the route a support ticket takes. Trace with your finger **RUBRIC** and ask what would a missing or corrupted value look like here? Use the case study to make the failure concrete.
- Get the room to name the owner who would need this evidence in an incident. Put a marker on **REVIEW** and ask who owns the evidence produced at this step? Use the case study to make the failure concrete.
- Ask what would need to be true for the team to skip this stage safely. Ask the room to locate **TOOL RECEIPTS** and ask which downstream stage would fail if this step were wrong? Use the case study to make the failure concrete.
- Use the analogy. A driving test includes the route, weather, vehicle, allowed maneuvers, automatic failures, examiner rubric, and score sheet; it is not just a destination and a preferred description of the trip. Ask the room where the equivalent tracking number, queue, or ledger is in their own system, and where it would first break.
- Tell the case study — Maya and the refund exception case. Walk through the walkthrough and stop at the moment the failure first becomes visible. Ask what signal, gate, or version field would have caught it earlier.
- Run the lab. Write one complete Acme evaluation case with at least four deterministic assertions, three rubric dimensions, two forbidden outcomes, five slice tags, eight version pins, and a short note explaining why the case belongs in the dataset. Have each group label the fields that are captured, hashed, redacted, or omitted.
- Pose the checkpoint. Does a golden evaluation case need one exact correct sentence? Let the room answer before confirming with the answer. Then ask what the team would change in the next build based on the answer.
- Before moving on, ask the room to trace one healthy teal path and one coral path through the diagram, naming the evidence that flips the colour at each stage.
- Close on the contract. Define the whole situation, allowed behavior, forbidden outcomes, evidence, rubric, and versions. Make the group write one sentence that ties the lesson to their own system.

---

## Lab and checkpoint

**Lab:** Write one complete Acme evaluation case with at least four deterministic assertions, three rubric dimensions, two forbidden outcomes, five slice tags, eight version pins, and a short note explaining why the case belongs in the dataset.

**Checkpoint:** Does a golden evaluation case need one exact correct sentence?

**Answer:** No. Some facts and contracts may be exact, but many tasks permit several good explanations. Define outcome and evidence requirements, then use an appropriate rubric for flexible qualities.

---

## Glossary

- **Evaluation case** — versioned test situation plus expectations
- **Rubric** — explicit criteria for a judgment
- **Golden dataset** — reviewed versioned set of representative cases

---

## Sources

- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12)
- [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

---

## Related lessons

- Diagram 178 — Deterministic contracts, schemas, and behavioral assertions
- Diagram 179 — Model graders, human rubrics, calibration, and disagreement
- Diagram 180 — Slices, denominators, confidence, variance, and significance

---
