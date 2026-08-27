# Diagram 188 — Graceful degradation, fallback, and admission control

![Admission control evaluates priority, fairness, deadline, risk, and capacity before selecting full service or bounded fallback tiers while preserving work, enforcing a quality floor, and avoiding unsafe degradation.](../diagrams/188-graceful-degradation-admission-control.png)

**Module:** Performance, capacity, and economics
**Role in the course:** Treat latency, deadlines, scenario cost, load, queues, capacity, degradation, and admission as explicit design inputs.
**Layout:** The diagram shows REQUESTS entering ADMISSION CONTROL with PRIORITY, TENANT FAIRNESS, DEADLINE, RISK, CAPACITY; it also accepted work enters FULL SERVICE then fallback tiers CACHED EVIDENCE, SMALLER MODEL, FEWER SPECIALISTS, ASYNC TASK, HUMAN HANDOFF.

---

## At a glance

**Design predictable reduced-service modes that preserve safety and useful work when dependencies or capacity fail.**

- Define the non-negotiable safety and quality floor that no degraded mode may cross.
- Create ordered service tiers with entry conditions, user-visible behavior, preserved artifacts, and exit conditions.
- Evaluate capacity, deadline, priority, risk, tenant fairness, and dependency health before admission.
- A DENY NEW WORK path shows the failure the design must catch before it reaches the user.

---

## What the diagram teaches

### 1. Design predictable fallbacks that preserve the safety floor

Graceful degradation means providing a smaller honest service instead of failing unpredictably, but a fallback is safe only if it preserves required quality and security constraints. Examples include using verified cached evidence within a freshness limit, selecting a faster model for low-risk summarization, reducing optional specialist fan-out, returning a partial artifact, moving work to an asynchronous task, or offering human help. Never degrade away tenant isolation, authorization, approval, citation, freshness, or another safety floor. Admission control decides whether new work should enter based on capacity, queue age, deadline, priority, risk, tenant fairness, and available fallback. Rejecting or delaying early can protect accepted work and make recovery faster. Define service tiers before incidents, make each user-visible, and test transitions both down and back up. The diagram exists so the team can design predictable reduced-service modes that preserve safety and useful work when dependencies or capacity fail.

### 2. Define the non-negotiable safety and quality floor that no degraded

Define the non-negotiable safety and quality floor that no degraded mode may cross. Never degrade away tenant isolation, authorization, approval, citation, freshness, or another safety floor. Graceful degradation means providing a smaller honest service instead of failing unpredictably, but a fallback is safe only if it preserves required quality and. In the diagram, this is represented by **QUALITY FLOOR**. The case study where The finance specialist is unavailable while Maya needs the current policy explanation and a refund recommendation makes the risk concrete: an ungoverned fallback can silently switch to stale data, a tool with broader authority, or a cheaper model that cannot meet the required safety task. When this step is done well, maya receives useful safe partial value and clear choices instead of a fabricated answer or total loss of work.

### 3. Create ordered service tiers with entry conditions, user-visible behavior, preserved

In the diagram, this is represented by **FULL SERVICE**. Create ordered service tiers with entry conditions, user-visible behavior, preserved artifacts, and exit conditions. Graceful degradation means providing a smaller honest service instead of failing unpredictably, but a fallback is safe only if it preserves required quality and. Define service tiers before incidents, make each user-visible, and test transitions both down and back up. The case study where The finance specialist is unavailable while Maya needs the current policy explanation and a refund recommendation shows the value: maya receives useful safe partial value and clear choices instead of a fabricated answer or total loss of work. Skip it, and an ungoverned fallback can silently switch to stale data, a tool with broader authority, or a cheaper model that cannot meet the required safety task. The takeaway is clear: degrade optional capability, never the safety floor; reject early when admission protects recovery.

### 4. Evaluate capacity, deadline, priority, risk, tenant fairness, and dependency health

Admission control decides whether new work should enter based on capacity, queue age, deadline, priority, risk, tenant fairness, and available fallback. This is why the step is non-negotiable: evaluate capacity, deadline, priority, risk, tenant fairness, and dependency health before admission. Define service tiers before incidents, make each user-visible, and test transitions both down and back up. In the diagram, this is represented by **PRIORITY** and **TENANT FAIRNESS**, near **DEADLINE**. The case study where The finance specialist is unavailable while Maya needs the current policy explanation and a refund recommendation proves it: maya receives useful safe partial value and clear choices instead of a fabricated answer or total loss of work. If the team omits this, an ungoverned fallback can silently switch to stale data, a tool with broader authority, or a cheaper model that cannot meet the required safety task.

### 5. Use timeouts, bounded retries, circuit breakers, bulkheads, queues, and load

Use timeouts, bounded retries, circuit breakers, bulkheads, queues, and load shedding without creating fallback loops. Graceful degradation means providing a smaller honest service instead of failing unpredictably, but a fallback is safe only if it preserves required quality and. Load shedding should be fair and governed, not silently biased toward convenient traffic. In the diagram, this is represented by **UNSAFE FALLBACK**. The case study where The finance specialist is unavailable while Maya needs the current policy explanation and a refund recommendation makes the risk concrete: an ungoverned fallback can silently switch to stale data, a tool with broader authority, or a cheaper model that cannot meet the required safety task. When this step is done well, maya receives useful safe partial value and clear choices instead of a fabricated answer or total loss of work.

### 6. Test degradation, recovery, stale-cache rejection, partial success, cancellation, and fairness

In the diagram, this is represented by **RECOVER**. Test degradation, recovery, stale-cache rejection, partial success, cancellation, and fairness under sustained load. Admission control decides whether new work should enter based on capacity, queue age, deadline, priority, risk, tenant fairness, and available fallback. Graceful degradation means providing a smaller honest service instead of failing unpredictably, but a fallback is safe only if it preserves required quality and. The case study where The finance specialist is unavailable while Maya needs the current policy explanation and a refund recommendation shows the value: maya receives useful safe partial value and clear choices instead of a fabricated answer or total loss of work. Skip it, and an ungoverned fallback can silently switch to stale data, a tool with broader authority, or a cheaper model that cannot meet the required safety task. The takeaway is clear: degrade optional capability, never the safety floor; reject early when admission protects recovery.

### 7. Putting it together

Taken together, these steps turn the objective "design predictable reduced-service modes that preserve safety and useful work when dependencies or capacity fail" into an operating contract. Define the non-negotiable safety and quality floor that no degraded mode may cross; Create ordered service tiers with entry conditions, user-visible behavior, preserved artifacts, and exit conditions; Evaluate capacity, deadline, priority, risk, tenant fairness, and dependency health before admission. The remaining steps extend this: Use timeouts, bounded retries, circuit breakers, bulkheads, queues, and load shedding without creating fallback loops; Test degradation, recovery, stale-cache rejection, partial success, cancellation, and fairness under sustained load. The case of The finance specialist is unavailable while Maya needs the current policy explanation and a refund recommendation shows how quickly an ungoverned fallback can silently switch to stale data, a tool with broader authority, or a cheaper model that cannot meet the required safety task. The durable lesson is degrade optional capability, never the safety floor; reject early when admission protects recovery.
![Request arrival passes concurrency and queue controls into workers and downstream model, retrieval, tool, and specialist limits, while gauges show load, wait, service, throughput, errors, and saturation.](../diagrams/187-load-concurrency-queues-saturation.png)

Diagram 187 — *Load, concurrency, queues, capacity, and saturation* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### Analogy

A hospital in a surge postpones routine work, triages urgent cases, opens overflow areas, and preserves safety protocols. It does not solve crowding by removing identity checks or medication safeguards.

### The Next.js surface

In the Next.js surface, the same contract appears through framework-specific patterns. Return explicit typed modes such as full, reduced, queued, partial, unavailable, or human-help with retry guidance and preserved artifact references. Use server-side feature configuration for fallbacks and keep the React interface honest about freshness, limitations, and authoritative status. Provide fair rate and admission responses with accessible recovery choices rather than infinite spinners or automatic retry storms.

### The Python surface

In the Python surface, the same contract is enforced with typed models and tests. Implement admission policies and fallback strategies as testable services with capacity inputs, safety-floor assertions, and immutable decision receipts. Use semaphores, bounded queues, circuit breakers, and deadline-aware cancellation around dependencies while preserving idempotent durable work. Run scenario tests that force each degraded tier, verify user-visible state and artifacts, and confirm controlled recovery without a surge.

---

## Case study — Maya's refund recommendation when the finance specialist is down

The finance specialist is unavailable while Maya needs the current policy explanation and a refund recommendation.

### The walkthrough

1. The system preserves current policy research but marks the financial recommendation incomplete.
2. It refuses to use stale cached finance rules because that would cross the freshness floor.
3. Maya can queue the specialist task, continue with the explanation, or request human review.
4. When finance recovers, a controlled probe succeeds and queued work resumes without duplicate effects.

### The result

Maya receives useful safe partial value and clear choices instead of a fabricated answer or total loss of work.

### The danger

An ungoverned fallback can silently switch to stale data, a tool with broader authority, or a cheaper model that cannot meet the required safety task.

### The takeaway

Degrade optional capability, never the safety floor; reject early when admission protects recovery.

---

## Composition

REQUESTS enter from the top into an ADMISSION CONTROL stage with five inputs: PRIORITY, TENANT FAIRNESS, DEADLINE, RISK, and CAPACITY. Accepted work flows downward into FULL SERVICE, then through fallback tiers: CACHED EVIDENCE, SMALLER MODEL, FEWER SPECIALISTS, ASYNC TASK, and HUMAN HANDOFF. Two coral lanes on the left show DENY NEW WORK and UNSAFE FALLBACK; two teal lanes on the right show PRESERVE WORK and RECOVER. A QUALITY FLOOR card runs across the bottom, showing the safety boundary that no fallback may cross. The composition is a triage funnel: requests are evaluated at the top, service tiers run down the middle, and a floor under everything keeps the system safe.

## Element by element

- **REQUESTS** — The **REQUESTS** are the incoming operation shown as a cyan path that starts the telemetry chain.
- **ADMISSION CONTROL** — The **ADMISSION CONTROL** is a deciding whether work may enter now.
- **PRIORITY** — The **PRIORITY** is the urgency of a corrective action relative to other work.
- **TENANT FAIRNESS** — The **TENANT FAIRNESS** is a cyan request or propagation path.
- **DEADLINE** — The **DEADLINE** is a latest useful completion time.
- **RISK** — The **RISK** is one of the population slices used to break down the OVERALL SCORE into a meaningful subgroup.
- **CAPACITY** — The **CAPACITY** is a cobalt platform or boundary.
- **FULL SERVICE** — The **FULL SERVICE** is a cyan request or propagation path that accepted work enters then fallback tiers CACHED EVIDENCE,.
- **CACHED EVIDENCE** — The **CACHED EVIDENCE** is a white record that accepted work enters FULL SERVICE then fallback tiers ,.
- **SMALLER MODEL** — The **SMALLER MODEL** is a MODEL.
- **FEWER SPECIALISTS** — The **FEWER SPECIALISTS** is a cyan request or propagation path.
- **ASYNC TASK** — The **ASYNC TASK** is a cyan request or propagation path.
- **HUMAN HANDOFF** — The **HUMAN HANDOFF** is a cyan request or propagation path.
- **DENY NEW WORK** — The **DENY NEW WORK** is a coral failure, risk, or incident path that coral lanes and UNSAFE FALLBACK;.
- **UNSAFE FALLBACK** — The **UNSAFE FALLBACK** is a coral failure, risk, or incident path that coral lanes DENY NEW WORK and ;.
- **PRESERVE WORK** — The **PRESERVE WORK** is a teal healthy or verified result path that teal lanes and RECOVER.
- **RECOVER** — The **RECOVER** is a teal healthy or verified result path that teal lanes PRESERVE WORK and .
- **QUALITY FLOOR** — The **QUALITY FLOOR** is the safety and quality boundary that no fallback may cross.

---

## Colour and flow semantics

- **Cobalt platform** — a service, stage, dataset, quality gate, budget, release lane, or incident-control boundary. In this diagram it appears on **ADMISSION CONTROL**, **CAPACITY**, **QUALITY FLOOR**.
- **Cyan arrow** — a request, propagated context, telemetry signal, evaluation flow, or candidate release path. In this diagram it appears on **REQUESTS**, **PRIORITY**, **TENANT FAIRNESS**, **DEADLINE**, **FULL SERVICE**, **SMALLER MODEL**, **FEWER SPECIALISTS**, **ASYNC TASK** and others.
- **Teal arrow** — a healthy result, matched evidence, safe promotion, controlled degradation, recovery, or verified learning path. In this diagram it appears on **PRESERVE WORK**, **RECOVER**.
- **Coral path** — a broken trace, failed assertion, regression, overload, unsafe outcome, rollback, alert, or incident path. In this diagram it appears on **DENY NEW WORK**, **UNSAFE FALLBACK**.
- **White card** — a span, event, metric, log, resource, case, score, budget, version, release, runbook, action, or regression record. In this diagram it appears on **RISK**, **CACHED EVIDENCE**.

The overall flow moves from the inputs on the left through the performance, capacity, and economics stages and exits as either a teal healthy path or a coral failure path. White cards carry the records, cobalt platforms hold the boundaries, and the cyan arrows show propagation and requests.

---

## How to present it

- Start with the operational question the team actually needs to answer. Point at the central element and ask what a regulator, evaluator, or support operator would ask about this outcome, and which signal type would best answer it.
- Ask the room what the team would need to know before approving the next release. Point at **QUALITY FLOOR** and ask what would change if this step were skipped? Use the case study to make the failure concrete.
- Have the group list the operational decisions this stage informs. Highlight **FULL SERVICE** and ask what real decision does this evidence support? Use the case study to make the failure concrete.
- Ask what evidence would change the route a support ticket takes. Trace with your finger **PRIORITY** and **TENANT FAIRNESS** and ask what would a missing or corrupted value look like here? Use the case study to make the failure concrete.
- Get the room to name the owner who would need this evidence in an incident. Put a marker on **UNSAFE FALLBACK** and ask who owns the evidence produced at this step? Use the case study to make the failure concrete.
- Ask what would need to be true for the team to skip this stage safely. Ask the room to locate **RECOVER** and ask which downstream stage would fail if this step were wrong? Use the case study to make the failure concrete.
- Use the analogy. A hospital in a surge postpones routine work, triages urgent cases, opens overflow areas, and preserves safety protocols. Ask the room where the equivalent tracking number, queue, or ledger is in their own system, and where it would first break.
- Tell the case study — Maya's refund recommendation when the finance specialist is down. Walk through the walkthrough and stop at the moment the failure first becomes visible. Ask what signal, gate, or version field would have caught it earlier.
- Run the lab. Create four service tiers for Acme. For each, define capacity trigger, quality floor, allowed features, forbidden shortcuts, visible status, artifact preservation, recovery choices, and exit test. Add one fairness rule and one stale-cache rejection. Have each group label the fields that are captured, hashed, redacted, or omitted.
- Pose the checkpoint. Is returning any answer better than rejecting a request during overload? Let the room answer before confirming with the answer. Then ask what the team would change in the next build based on the answer.
- Before moving on, ask the room to trace one healthy teal path and one coral path through the diagram, naming the evidence that flips the colour at each stage.
- Close on the contract. Degrade optional capability, never the safety floor; reject early when admission protects recovery. Make the group write one sentence that ties the lesson to their own system.

---

## Lab and checkpoint

**Lab:** Create four service tiers for Acme. For each, define capacity trigger, quality floor, allowed features, forbidden shortcuts, visible status, artifact preservation, recovery choices, and exit test. Add one fairness rule and one stale-cache rejection.

**Checkpoint:** Is returning any answer better than rejecting a request during overload?

**Answer:** No. An unsafe or misleading answer may cause more harm. A clear rejection, queued task, partial artifact, or human handoff can be the correct degraded outcome.

---

## Glossary

- **Admission control** — deciding whether work may enter now
- **Quality floor** — minimum behavior no fallback may violate
- **Circuit breaker** — control that pauses calls to a failing dependency

---

## Sources

- [Google SRE monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Google SRE service-level objectives](https://sre.google/sre-book/service-level-objectives/)

---

## Related lessons

- Diagram 183 — Planning, delegation, synthesis, and groundedness
- Diagram 185 — Latency budgets, percentiles, deadlines, and the slow tail
- Diagram 187 — Load, concurrency, queues, capacity, and saturation

---
