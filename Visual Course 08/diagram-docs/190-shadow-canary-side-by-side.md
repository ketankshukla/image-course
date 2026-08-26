# Diagram 190 — Shadow traffic, canaries, and side-by-side comparison

![Production traffic is mirrored to a no-effect shadow candidate before a small bounded canary cohort is compared with control on quality, safety, latency, cost, errors, and recovery, leading to promote, hold, or rollback.](../diagrams/190-shadow-canary-side-by-side.png)

**Module:** Release engineering
**Role in the course:** Promote changes only when reproducible offline and production evidence says the candidate is safer or better.
**Layout:** The diagram shows PRODUCTION TRAFFIC splitting into CONTROL and SHADOW CANDIDATE with EFFECTS DISABLED, then a CANARY lane with SMALL COHORT and BOUNDED EFFECTS; it also compare QUALITY, SAFETY, LATENCY, COST, ERRORS, RECOVERY by VERSION and SLICE.

---

## At a glance

**Use real workload evidence gradually while preventing duplicate or unsafe business effects.**

- Define eligible traffic, privacy basis, exclusions, cohort, duration, and representativeness before mirroring anything.
- Run the candidate in a side-effect-free isolated shadow and compare normalized outputs and stage evidence with control.
- Expose a small canary cohort with bounded effects, explicit version dimensions, and a limited error-budget risk.
- A SHARED CACHE CONTAMINATION path shows the failure the design must catch before it reaches the user.

---

## What the diagram teaches

### 1. Use real workload evidence gradually and safely

Shadowing sends a copy of eligible production input to a candidate while the control still serves the user. It reveals behavior on real workload shape without exposing candidate output, but side effects must be disabled or redirected to isolated fakes. Sensitive input, consent, retention, regional processing, and vendor terms still apply; shadow traffic is real data, not free test data. A canary serves the candidate to a small governed cohort or traffic fraction and compares it with a control. Define cohort, duration, risk budget, quality and safety checks, latency, cost, errors, user outcomes, and rollback conditions before launch. Segment metrics by version so a small bad canary is not hidden inside overall traffic. The diagram exists so the team can use real workload evidence gradually while preventing duplicate or unsafe business effects.

### 2. Define eligible traffic, privacy basis, exclusions, cohort, duration, and representativeness

Define eligible traffic, privacy basis, exclusions, cohort, duration, and representativeness before mirroring anything. A canary serves the candidate to a small governed cohort or traffic fraction and compares it with a control. Define cohort, duration, risk budget, quality and safety checks, latency, cost, errors, user outcomes, and rollback conditions before launch. In the diagram, this is represented by **PRODUCTION TRAFFIC** and **SMALL COHORT**. The case study where Acme's candidate fixes stale retrieval offline, so the team shadows real policy questions before exposing answers to Maya or calling tools makes the risk concrete: a shadow that shares caches, writes analytics, sends emails, or calls payment tools is not observational; it can change production and duplicate effects. When this step is done well, real workload evidence improves confidence without giving an unproven candidate broad business authority.
![A versioned change manifest and build artifact run against frozen cases, tools, retrieval, policy, time, and scorers before contract, quality, safety, performance, cost, and compatibility release gates produce an evidence bundle.](../diagrams/189-offline-gates-reproducible-evals.png)

Diagram 189 — *Offline gates and reproducible evaluation runs* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 3. Run the candidate in a side-effect-free isolated shadow and compare

In the diagram, this is represented by **CONTROL**. Run the candidate in a side-effect-free isolated shadow and compare normalized outputs and stage evidence with control. Shadowing sends a copy of eligible production input to a candidate while the control still serves the user. A canary serves the candidate to a small governed cohort or traffic fraction and compares it with a control. The case study where Acme's candidate fixes stale retrieval offline, so the team shadows real policy questions before exposing answers to Maya or calling tools shows the value: real workload evidence improves confidence without giving an unproven candidate broad business authority. Skip it, and a shadow that shares caches, writes analytics, sends emails, or calls payment tools is not observational; it can change production and duplicate effects. The takeaway is clear: shadow with effects isolated, canary with risk bounded, and compare by version before gradual promotion.

### 4. Expose a small canary cohort with bounded effects, explicit version

A canary serves the candidate to a small governed cohort or traffic fraction and compares it with a control. This is why the step is non-negotiable: expose a small canary cohort with bounded effects, explicit version dimensions, and a limited error-budget risk. Define cohort, duration, risk budget, quality and safety checks, latency, cost, errors, user outcomes, and rollback conditions before launch. In the diagram, this is represented by **CANARY** and **BOUNDED EFFECTS**, near **VERSION**. The case study where Acme's candidate fixes stale retrieval offline, so the team shadows real policy questions before exposing answers to Maya or calling tools proves it: real workload evidence improves confidence without giving an unproven candidate broad business authority. If the team omits this, a shadow that shares caches, writes analytics, sends emails, or calls payment tools is not observational; it can change production and duplicate effects.

### 5. Evaluate quality, forbidden outcomes, latency, cost, errors, user recovery,

Evaluate quality, forbidden outcomes, latency, cost, errors, user recovery, and important slices against predeclared rules. For long-running tasks, the canary window must cover the work lifecycle and recovery. Define cohort, duration, risk budget, quality and safety checks, latency, cost, errors, user outcomes, and rollback conditions before launch. In the diagram, this is represented by **QUALITY** and **LATENCY**, near **COST**. The case study where Acme's candidate fixes stale retrieval offline, so the team shadows real policy questions before exposing answers to Maya or calling tools makes the risk concrete: a shadow that shares caches, writes analytics, sends emails, or calls payment tools is not observational; it can change production and duplicate effects. When this step is done well, real workload evidence improves confidence without giving an unproven candidate broad business authority.

### 6. Promote, hold, or rollback while preserving comparison evidence and checking

In the diagram, this is represented by **CONTROL** and **PROMOTE**, near **HOLD**. Promote, hold, or rollback while preserving comparison evidence and checking that control state was not contaminated. Avoid shared caches, queues, or state that allow the shadow to change control behavior or inflate cache performance. Promote in stages, hold on uncertain evidence, and rollback automatically only when that action is itself safe and tested. The case study where Acme's candidate fixes stale retrieval offline, so the team shadows real policy questions before exposing answers to Maya or calling tools shows the value: real workload evidence improves confidence without giving an unproven candidate broad business authority. Skip it, and a shadow that shares caches, writes analytics, sends emails, or calls payment tools is not observational; it can change production and duplicate effects. The takeaway is clear: shadow with effects isolated, canary with risk bounded, and compare by version before gradual promotion.

### 7. Putting it together

Taken together, these steps turn the objective "use real workload evidence gradually while preventing duplicate or unsafe business effects" into an operating contract. Define eligible traffic, privacy basis, exclusions, cohort, duration, and representativeness before mirroring anything; Run the candidate in a side-effect-free isolated shadow and compare normalized outputs and stage evidence with control; Expose a small canary cohort with bounded effects, explicit version dimensions, and a limited error-budget risk. The remaining steps extend this: Evaluate quality, forbidden outcomes, latency, cost, errors, user recovery, and important slices against predeclared rules; Promote, hold, or rollback while preserving comparison evidence and checking that control state was not contaminated. The case of Acme's candidate fixes stale retrieval offline, so the team shadows real policy questions before exposing answers to Maya or calling tools shows how quickly a shadow that shares caches, writes analytics, sends emails, or calls payment tools is not observational; it can change production and duplicate effects. The durable lesson is shadow with effects isolated, canary with risk bounded, and compare by version before gradual promotion.

### Analogy

A theater rehearses with the same script and stage before a preview audience, then opens for a few performances while the original production remains available. It does not test pyrotechnics in a packed theater without isolation.

### The Next.js surface

In the Next.js surface, the same contract appears through framework-specific patterns. Choose cohort and candidate server-side with a stable non-sensitive targeting key and record the evaluated flag variant and version on traces and receipts. Never execute shadow side effects; route candidate tools to isolated adapters and keep candidate output away from the user until the design permits it. Build a comparison view that separates control and candidate denominators, slices, missing data, and long-running completion windows.

### The Python surface

In the Python surface, the same contract is enforced with typed models and tests. Implement a shadow dispatcher that clones only approved fields, strips authority, uses isolated stores, and records candidate evidence asynchronously. Use a canary policy service to assign cohorts, cap risk, and attach version and variant to context across FastAPI and workers. Continuously compare candidate and control with predefined guardrails and emit one durable promotion, hold, or rollback decision receipt.

---

## Case study — Acme shadows real policy questions

Acme's candidate fixes stale retrieval offline, so the team shadows real policy questions before exposing answers to Maya or calling tools.

### The walkthrough

1. The shadow uses real query shape but isolated retrieval cache, fake effects, redacted evidence, and short retention.
2. Comparison reveals higher latency only on long multilingual policies, a slice underrepresented offline.
3. After tuning, a small canary serves low-risk policy explanations while refunds still require the control path.
4. The canary meets predefined slice and budget rules before gradual promotion.

### The result

Real workload evidence improves confidence without giving an unproven candidate broad business authority.

### The danger

A shadow that shares caches, writes analytics, sends emails, or calls payment tools is not observational; it can change production and duplicate effects.

### The takeaway

Shadow with effects isolated, canary with risk bounded, and compare by version before gradual promotion.

---

## Composition

PRODUCTION TRAFFIC enters from the left and splits into two lanes: a CONTROL lane on top and a SHADOW CANDIDATE lane below it with EFFECTS DISABLED. From the shadow, a CANARY lane with a SMALL COHORT and BOUNDED EFFECTS branches to the right. Six comparison panels—QUALITY, SAFETY, LATENCY, COST, ERRORS, and RECOVERY—sit between the versions and are broken down by VERSION and SLICE. At the right, a funnel offers PROMOTE, HOLD, and ROLLBACK choices. Two safety cards appear near the bottom: a coral SHARED CACHE CONTAMINATION warning and a teal ISOLATED EVIDENCE badge. The composition is a side-by-side racetrack: control and candidate run in parallel, then a small canary is measured against predeclared rules.

## Element by element

- **PRODUCTION TRAFFIC** — The **PRODUCTION TRAFFIC** is splitting into CONTROL and SHADOW CANDIDATE with EFFECTS DISABLED,.
- **CONTROL** — The **CONTROL** is the live production version that serves real traffic and provides the baseline comparison.
- **SHADOW CANDIDATE** — The **SHADOW CANDIDATE** is the candidate version that receives real traffic but has its effects disabled.
- **EFFECTS DISABLED** — The **EFFECTS DISABLED** is a cyan request or propagation path that pRODUCTION TRAFFIC splitting into CONTROL and SHADOW CANDIDATE with ,.
- **CANARY** — The **CANARY** is the small-cohort, bounded-effects release used to compare real behavior against the control.
- **SMALL COHORT** — The **SMALL COHORT** is the limited set of real users or tasks exposed to the canary.
- **BOUNDED EFFECTS** — The **BOUNDED EFFECTS** are the limits on what the canary can change or affect in production.
- **QUALITY** — The **QUALITY** is a cobalt platform or boundary that compare ,.
- **SAFETY** — The **SAFETY** is the offline gate that checks dangerous or unacceptable outcomes.
- **LATENCY** — The **LATENCY** is a cyan request or propagation path.
- **COST** — The **COST** is a cyan request or propagation path.
- **ERRORS** — The **ERRORS** is a white record.
- **RECOVERY** — The **RECOVERY** is by VERSION and SLICE.
- **VERSION** — The **VERSION** is a SLICE .
- **SLICE** — The **SLICE** is a meaningful subgroup of evaluation cases.
- **PROMOTE** — The **PROMOTE** is a cyan request or propagation path that funnel choices ,.
- **HOLD** — The **HOLD** is a cyan request or propagation path.
- **ROLLBACK** — The **ROLLBACK** returns to a known-good compatible version set; it is not simply 'model previous' if the index or schema already changed.
- **SHARED CACHE CONTAMINATION** — The **SHARED CACHE CONTAMINATION** is the coral risk where the candidate pollutes control caches or state.
- **ISOLATED EVIDENCE** — The **ISOLATED EVIDENCE** is the teal guarantee that candidate evidence is kept separate from production.

---

## Colour and flow semantics

- **Cobalt platform** — a service, stage, dataset, quality gate, budget, release lane, or incident-control boundary. In this diagram it appears on **CONTROL**, **CANARY**, **QUALITY**.
- **Cyan arrow** — a request, propagated context, telemetry signal, evaluation flow, or candidate release path. In this diagram it appears on **PRODUCTION TRAFFIC**, **EFFECTS DISABLED**, **SMALL COHORT**, **BOUNDED EFFECTS**, **LATENCY**, **COST**, **SLICE**, **PROMOTE** and others.
- **Teal arrow** — a healthy result, matched evidence, safe promotion, controlled degradation, recovery, or verified learning path. In this diagram it appears on **SAFETY**, **RECOVERY**, **ISOLATED EVIDENCE**.
- **Coral path** — a broken trace, failed assertion, regression, overload, unsafe outcome, rollback, alert, or incident path. In this diagram it appears on **SHARED CACHE CONTAMINATION**.
- **White card** — a span, event, metric, log, resource, case, score, budget, version, release, runbook, action, or regression record. In this diagram it appears on **SHADOW CANDIDATE**, **ERRORS**, **VERSION**.

The overall flow moves from the inputs on the left through the release engineering stages and exits as either a teal healthy path or a coral failure path. White cards carry the records, cobalt platforms hold the boundaries, and the cyan arrows show propagation and requests.

---

## How to present it

- Start with the operational question the team actually needs to answer. Point at the central element and ask what a regulator, evaluator, or support operator would ask about this outcome, and which signal type would best answer it.
- Ask the room what the team would need to know before approving the next release. Point at **PRODUCTION TRAFFIC** and **SMALL COHORT** and ask what would change if this step were skipped? Use the case study to make the failure concrete.
- Have the group list the operational decisions this stage informs. Highlight **CONTROL** and ask what real decision does this evidence support? Use the case study to make the failure concrete.
- Ask what evidence would change the route a support ticket takes. Trace with your finger **CANARY** and **BOUNDED EFFECTS** and ask what would a missing or corrupted value look like here? Use the case study to make the failure concrete.
- Get the room to name the owner who would need this evidence in an incident. Put a marker on **QUALITY** and **LATENCY** and ask who owns the evidence produced at this step? Use the case study to make the failure concrete.
- Ask what would need to be true for the team to skip this stage safely. Ask the room to locate **CONTROL** and **PROMOTE** and ask which downstream stage would fail if this step were wrong? Use the case study to make the failure concrete.
- Use the analogy. A theater rehearses with the same script and stage before a preview audience, then opens for a few performances while the original production remains available. Ask the room where the equivalent tracking number, queue, or ledger is in their own system, and where it would first break.
- Tell the case study — Acme shadows real policy questions. Walk through the walkthrough and stop at the moment the failure first becomes visible. Ask what signal, gate, or version field would have caught it earlier.
- Run the lab. Design a three-stage release for Acme: shadow, 2% low-risk canary, and 20% expanded canary. Define eligibility, isolation, duration, six comparison measures, two critical slices, error-budget exposure, hold rules, and rollback evidence. Mark percentages as proposed. Have each group label the fields that are captured, hashed, redacted, or omitted.
- Pose the checkpoint. Is shadow traffic automatically risk-free because users do not see the candidate output? Let the room answer before confirming with the answer. Then ask what the team would change in the next build based on the answer.
- Before moving on, ask the room to trace one healthy teal path and one coral path through the diagram, naming the evidence that flips the colour at each stage.
- Close on the contract. Shadow with effects isolated, canary with risk bounded, and compare by version before gradual promotion. Make the group write one sentence that ties the lesson to their own system.

---

## Lab and checkpoint

**Lab:** Design a three-stage release for Acme: shadow, 2% low-risk canary, and 20% expanded canary. Define eligibility, isolation, duration, six comparison measures, two critical slices, error-budget exposure, hold rules, and rollback evidence. Mark percentages as proposed.

**Checkpoint:** Is shadow traffic automatically risk-free because users do not see the candidate output?

**Answer:** No. It processes real data and can affect shared caches, stores, quotas, vendors, or tools unless intentionally isolated and governed.

---

## Glossary

- **Shadow traffic** — copied input evaluated without serving candidate output
- **Canary** — small governed production exposure
- **Control** — current version used as comparison baseline

---

## Sources

- [Google SRE canarying releases](https://sre.google/workbook/canarying-releases/)
- [OpenFeature specification](https://openfeature.dev/specification/)
- [OpenFeature observability appendix](https://openfeature.dev/specification/appendix-d/)

---

## Related lessons

- Diagram 189 — Offline gates and reproducible evaluation runs
- Diagram 191 — Feature flags, version pinning, rollback, and kill switches
- Diagram 194 — Red-team, chaos, abuse, and recovery exercises

---
