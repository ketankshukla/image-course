# Diagram 180 — Slices, denominators, confidence, variance, and significance

![A high overall score is broken into meaningful slices and denominators, revealing a weak stale-policy slice, while repeated runs show variance, confidence, and a proposed decision threshold.](../diagrams/180-slices-denominators-confidence-variance.png)

**Module:** Evaluation design
**Role in the course:** Convert vague confidence into repeatable cases, assertions, calibrated judgments, meaningful slices, and honest uncertainty.
**Layout:** The diagram shows OVERALL SCORE 92 PERCENT breaking into slices LANGUAGE, CHANNEL, ISSUE TYPE, TENANT TIER, TOOL PATH, RISK; it also reveal one coral slice STALE POLICY 58 PERCENT.

---

## At a glance

**Read evaluation numbers honestly and find important failures hidden by averages or tiny denominators.**

- Report passed, failed, excluded, missing, and total eligible cases before publishing a rate.
- Predefine slices tied to user groups, workflows, risks, data age, or technical paths.
- Repeat probabilistic cases enough times to observe distribution, variance, and unacceptable tail outcomes.
- A STALE POLICY 58 PERCENT path shows the failure the design must catch before it reaches the user.

---

## What the diagram teaches

### 1. Read rates with denominators, slices, and honest uncertainty

A rate without its denominator can mislead. Ninety percent may mean nine of ten or nine thousand of ten thousand, and those results support different confidence. Always report numerator, denominator, exclusions, missing data, case version, and measurement window. Then examine slices that correspond to different user needs or failure mechanisms: language, channel, issue type, document age, tool path, tenant tier, accessibility need, risk class, region, or workflow length. Choose slices before looking for flattering results, and do not create so many tiny groups that random noise becomes a story. Generative systems can vary across repeated runs even with the same input, so record the run count, configuration, distribution, variance, and worst unacceptable outcome rather than one average. The diagram exists so the team can read evaluation numbers honestly and find important failures hidden by averages or tiny denominators.

### 2. Report passed, failed, excluded, missing, and total eligible cases before

Report passed, failed, excluded, missing, and total eligible cases before publishing a rate. Choose slices before looking for flattering results, and do not create so many tiny groups that random noise becomes a story. Always report numerator, denominator, exclusions, missing data, case version, and measurement window. In the diagram, this is represented by **PASSED ELIGIBLE**. The case study where Acme's candidate scores 92% overall, but stale-policy cases score 58% and Spanish stale-policy cases contain only four evaluations makes the risk concrete: optimizing one overall average can improve common easy cases while making rare, expensive, or vulnerable cases worse. When this step is done well, the release decision protects the known failure slice and avoids pretending that a tiny subgroup estimate is precise.

### 3. Predefine slices tied to user groups, workflows, risks, data age,

In the diagram, this is represented by **RISK**. Predefine slices tied to user groups, workflows, risks, data age, or technical paths. Choose slices before looking for flattering results, and do not create so many tiny groups that random noise becomes a story. Then examine slices that correspond to different user needs or failure mechanisms: language, channel, issue type, document age. The case study where Acme's candidate scores 92% overall, but stale-policy cases score 58% and Spanish stale-policy cases contain only four evaluations shows the value: the release decision protects the known failure slice and avoids pretending that a tiny subgroup estimate is precise. Skip it, and optimizing one overall average can improve common easy cases while making rare, expensive, or vulnerable cases worse. The takeaway is clear: every score needs a denominator, meaningful slices, repeated evidence, and an honest uncertainty rule.

### 4. Repeat probabilistic cases enough times to observe distribution, variance,

Generative systems can vary across repeated runs even with the same input, so record the run count, configuration, distribution. This is why the step is non-negotiable: repeat probabilistic cases enough times to observe distribution, variance, and unacceptable tail outcomes. Ninety percent may mean nine of ten or nine thousand of ten thousand, and those results support different confidence. In the diagram, this is represented by **DISTRIBUTION**. The case study where Acme's candidate scores 92% overall, but stale-policy cases score 58% and Spanish stale-policy cases contain only four evaluations proves it: the release decision protects the known failure slice and avoids pretending that a tiny subgroup estimate is precise. If the team omits this, optimizing one overall average can improve common easy cases while making rare, expensive, or vulnerable cases worse.

### 5. Compare practical effect and safety importance alongside uncertainty or statistical

Compare practical effect and safety importance alongside uncertainty or statistical significance. Release rules should combine minimum sample size, practical effect, safety constraints, and uncertainty handling. Confidence intervals or resampling can express uncertainty, but statistical significance does not equal business importance. The case study where Acme's candidate scores 92% overall, but stale-policy cases score 58% and Spanish stale-policy cases contain only four evaluations makes the risk concrete: optimizing one overall average can improve common easy cases while making rare, expensive, or vulnerable cases worse. When this step is done well, the release decision protects the known failure slice and avoids pretending that a tiny subgroup estimate is precise.

### 6. Require minimum denominators and route sparse or conflicting evidence

Require minimum denominators and route sparse or conflicting evidence to review instead of forcing a conclusion. A small quality change may matter greatly on a high-risk slice, while a statistically detectable change may be too small to justify cost or latency. Ninety percent may mean nine of ten or nine thousand of ten thousand, and those results support different confidence. The case study where Acme's candidate scores 92% overall, but stale-policy cases score 58% and Spanish stale-policy cases contain only four evaluations shows the value: the release decision protects the known failure slice and avoids pretending that a tiny subgroup estimate is precise. Skip it, and optimizing one overall average can improve common easy cases while making rare, expensive, or vulnerable cases worse. The takeaway is clear: every score needs a denominator, meaningful slices, repeated evidence, and an honest uncertainty rule.

### 7. Putting it together

Taken together, these steps turn the objective "read evaluation numbers honestly and find important failures hidden by averages or tiny denominators" into an operating contract. Report passed, failed, excluded, missing, and total eligible cases before publishing a rate; Predefine slices tied to user groups, workflows, risks, data age, or technical paths; Repeat probabilistic cases enough times to observe distribution, variance, and unacceptable tail outcomes. The remaining steps extend this: Compare practical effect and safety importance alongside uncertainty or statistical significance; Require minimum denominators and route sparse or conflicting evidence to review instead of forcing a conclusion. The case of Acme's candidate scores 92% overall, but stale-policy cases score 58% and Spanish stale-policy cases contain only four evaluations shows how quickly optimizing one overall average can improve common easy cases while making rare, expensive, or vulnerable cases worse. The durable lesson is every score needs a denominator, meaningful slices, repeated evidence, and an honest uncertainty rule.

### Analogy

A school average can look excellent while one classroom lacks books. You need class sizes, subject breakdowns, repeated assessments, and attention to the students most affected before declaring success.

### The Next.js surface

In the Next.js surface, the same contract appears through framework-specific patterns. Build scorecards that always display numerator, denominator, exclusions, dataset version, run count, and slice definition beside each rate. Use server-side aggregation with a controlled dimension allowlist so users cannot create unbounded metrics or expose small private groups. Provide comparison views with confidence and practical-effect notes, and label all proposed thresholds as policy choices rather than universal facts.

### The Python surface

In the Python surface, the same contract is enforced with typed models and tests. Represent each result as case ID, run ID, slice tags, score, failure class, and version manifest before aggregation. Use reproducible analysis functions for counts, rates, distributions, bootstrap intervals when appropriate, and minimum-sample warnings. Test aggregation against missing results, duplicated runs, overlapping slices, tiny groups, and Simpson's-paradox-style reversals.
![The same evidence is judged by deterministic checks, model graders, and humans, then compared through calibration, agreement measures, disagreement review, adjudication, and rubric updates while grader drift is monitored.](../diagrams/179-graders-humans-calibration-disagreement.png)

Diagram 179 — *Model graders, human rubrics, calibration, and disagreement* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

---

## Case study — Acme's 92% overall score and the stale-policy slice

Acme's candidate scores 92% overall, but stale-policy cases score 58% and Spanish stale-policy cases contain only four evaluations.

### The walkthrough

1. The dashboard reveals the exact numerators and denominators instead of showing only 92%. 
2. The stale-policy slice blocks release because it represents the known high-impact failure mechanism.
3. The Spanish subgroup is marked insufficient evidence rather than declared good or bad from four cases.
4. The team expands representative cases and repeats variable runs before making the subgroup decision.

### The result

The release decision protects the known failure slice and avoids pretending that a tiny subgroup estimate is precise.

### The danger

Optimizing one overall average can improve common easy cases while making rare, expensive, or vulnerable cases worse.

### The takeaway

Every score needs a denominator, meaningful slices, repeated evidence, and an honest uncertainty rule.

---

## Composition

At the top, an OVERALL SCORE 92 PERCENT card breaks apart into six slice cards: LANGUAGE, CHANNEL, ISSUE TYPE, TENANT TIER, TOOL PATH, and RISK. One coral slice, STALE POLICY 58 PERCENT, stands out among them. Beside every rate sits a PASSED / ELIGIBLE denominator card. Below the slices, repeated RUNS form a DISTRIBUTION with MEAN, RANGE, CONFIDENCE, and a DECISION THRESHOLD marked PROPOSED. The composition moves from one headline number at the top to honest denominators in the middle and variance at the bottom, showing that a single score is never enough.

## Element by element

- **OVERALL SCORE 92 PERCENT** — The **OVERALL SCORE 92 PERCENT** is the headline rate that can hide weak slices and small denominators.
- **LANGUAGE** — The **LANGUAGE** is one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.
- **CHANNEL** — The **CHANNEL** is one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.
- **ISSUE TYPE** — The **ISSUE TYPE** is one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.
- **TENANT TIER** — The **TENANT TIER** is one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.
- **TOOL PATH** — The **TOOL PATH** is one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.
- **RISK** — The **RISK** is one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.
- **STALE POLICY 58 PERCENT** — The **STALE POLICY 58 PERCENT** is the coral slice that shows the known high-impact failure mechanism has a poor rate.
- **PASSED ELIGIBLE** — The **PASSED ELIGIBLE** is the denominator card that shows how many eligible cases a rate is built from.
- **RUNS** — The **RUNS** are the repeated executions of the same case set used to measure variance and build a DISTRIBUTION.
- **DISTRIBUTION** — The **DISTRIBUTION** is the chart formed by repeated RUNS, showing MEAN, RANGE, CONFIDENCE, and the DECISION THRESHOLD.
- **MEAN** — The **MEAN** is the average value of the repeated RUNS in the DISTRIBUTION.
- **RANGE** — The **RANGE** is the spread of values across the repeated RUNS in the DISTRIBUTION.
- **CONFIDENCE** — The **CONFIDENCE** is the measure of uncertainty around the observed value in the DISTRIBUTION.
- **DECISION THRESHOLD** — The **DECISION THRESHOLD** is the proposed boundary on the distribution that the team must agree to before promoting.
- **PROPOSED** — The **PROPOSED** is the marker on the DECISION THRESHOLD showing the current proposed release boundary.

---

## Colour and flow semantics

- **Cyan arrow** — a request, propagated context, telemetry signal, evaluation flow, or candidate release path. In this diagram it appears on **DECISION THRESHOLD**.
- **Coral path** — a broken trace, failed assertion, regression, overload, unsafe outcome, rollback, alert, or incident path. In this diagram it appears on **STALE POLICY 58 PERCENT**.
- **White card** — a span, event, metric, log, resource, case, score, budget, version, release, runbook, action, or regression record. In this diagram it appears on **OVERALL SCORE 92 PERCENT**, **LANGUAGE**, **CHANNEL**, **ISSUE TYPE**, **TENANT TIER**, **TOOL PATH**, **RISK**, **PASSED ELIGIBLE** and others.

The overall flow moves from the inputs on the left through the evaluation design stages and exits as either a teal healthy path or a coral failure path. White cards carry the records, cobalt platforms hold the boundaries, and the cyan arrows show propagation and requests.

---

## How to present it

- Start with the operational question the team actually needs to answer. Point at the central element and ask what a regulator, evaluator, or support operator would ask about this outcome, and which signal type would best answer it.
- Ask the room what the team would need to know before approving the next release. Point at **PASSED ELIGIBLE** and ask what would change if this step were skipped? Use the case study to make the failure concrete.
- Have the group list the operational decisions this stage informs. Highlight **RISK** and ask what real decision does this evidence support? Use the case study to make the failure concrete.
- Ask what evidence would change the route a support ticket takes. Trace with your finger **DISTRIBUTION** and ask what would a missing or corrupted value look like here? Use the case study to make the failure concrete.
- Get the room to name the owner who would need this evidence in an incident. Put a marker on the trace and ask who owns the evidence produced at this step? Use the case study to make the failure concrete.
- Ask what would need to be true for the team to skip this stage safely. Ask the room to locate the trace and ask which downstream stage would fail if this step were wrong? Use the case study to make the failure concrete.
- Use the analogy. A school average can look excellent while one classroom lacks books. Ask the room where the equivalent tracking number, queue, or ledger is in their own system, and where it would first break.
- Tell the case study — Acme's 92% overall score and the stale-policy slice. Walk through the walkthrough and stop at the moment the failure first becomes visible. Ask what signal, gate, or version field would have caught it earlier.
- Run the lab. Create a synthetic 40-case result table with six slices and two repeated runs. Calculate overall and slice rates, list denominators and exclusions, flag insufficient groups, and write one release rule based on practical harm rather than the best-looking average. Have each group label the fields that are captured, hashed, redacted, or omitted.
- Pose the checkpoint. Can a statistically significant change still be unimportant? Let the room answer before confirming with the answer. Then ask what the team would change in the next build based on the answer.
- Before moving on, ask the room to trace one healthy teal path and one coral path through the diagram, naming the evidence that flips the colour at each stage.
- Close on the contract. Every score needs a denominator, meaningful slices, repeated evidence, and an honest uncertainty rule. Make the group write one sentence that ties the lesson to their own system.

---

## Lab and checkpoint

**Lab:** Create a synthetic 40-case result table with six slices and two repeated runs. Calculate overall and slice rates, list denominators and exclusions, flag insufficient groups, and write one release rule based on practical harm rather than the best-looking average.

**Checkpoint:** Can a statistically significant change still be unimportant?

**Answer:** Yes. Significance describes evidence against chance under assumptions; it does not decide whether the effect is large, useful, safe, or worth its cost.

---

## Glossary

- **Slice** — meaningful subgroup of evaluation cases
- **Denominator** — total eligible opportunities behind a rate
- **Variance** — how spread out repeated results are

---

## Sources

- [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [Google SRE service-level objectives](https://sre.google/sre-book/service-level-objectives/)

---

## Related lessons

- Diagram 177 — The anatomy of a useful evaluation case
- Diagram 179 — Model graders, human rubrics, calibration, and disagreement
- Diagram 185 — Latency budgets, percentiles, deadlines, and the slow tail

---
