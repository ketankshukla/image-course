# Diagram 193 — Alerts, ownership, triage, and runbooks

![Operational signals become page, ticket, or record actions based on user impact, budget burn, safety, and missing evidence, then flow through ownership, triage, runbook, containment, recovery, communication, and closure.](../diagrams/193-alert-ownership-triage-runbook.png)

**Module:** Incidents and continuous learning
**Role in the course:** Make alerts actionable, rehearse failure, recover safely, and turn every serious defect into verified permanent learning.
**Layout:** The diagram shows SIGNALS entering ALERT RULE with USER IMPACT, BUDGET BURN, SAFETY VIOLATION, MISSING EVIDENCE; it also route to PAGE NOW, TICKET SOON, RECORD ONLY.

---

## At a glance

**Create alerts that lead a named person to a useful action instead of producing noise and dashboards nobody owns.**

- Define the user, business, safety, or observability condition that genuinely requires action.
- Choose page, ticket, or record behavior and name owner, severity, acknowledgement, and escalation rules.
- Include impact, scope, version, slice, denominator, time, evidence links, and recent change context.
- A OWNER path shows the failure the design must catch before it reaches the user.

---

## What the diagram teaches

### 1. Create alerts that lead to a useful action

An alert should mean a human must act now or soon. If no action is required, keep the signal for analysis rather than paging. Begin with user or safety impact, not a convenient infrastructure threshold. Useful agent alerts may cover forbidden business effects, stale-evidence rates, policy-deny bypass, missing receipts, exhausted error or cost budget, queue age, failed canary guardrails, widespread recovery failure, or telemetry loss that makes critical work unobservable. Every alert needs an owner, severity rule, acknowledgement target, escalation, runbook, evidence links, safe first actions, communication route, and closure condition. Make alert payloads privacy-safe and include version, route, slice, denominator, current impact, start time, and relevant traces or artifacts. The diagram exists so the team can create alerts that lead a named person to a useful action instead of producing noise and dashboards nobody owns.
![An incident timeline and impact analysis produce owned corrective actions with proof, permanent regression cases, control updates, and future release gates while rejecting blame and unverified closure.](../diagrams/195-postmortem-corrective-regression-loop.png)

Diagram 195 — *Postmortems, corrective actions, and regression cases* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 2. Define the user, business, safety, or observability condition that genuinely

Define the user, business, safety, or observability condition that genuinely requires action. Useful agent alerts may cover forbidden business effects, stale-evidence rates, policy-deny bypass, missing receipts, exhausted error or cost budget. Begin with user or safety impact, not a convenient infrastructure threshold. In the diagram, this is represented by **USER IMPACT** and **SAFETY VIOLATION**, near **ACTIONABLE**. The case study where After a candidate canary, stale-policy failures rise in one route while overall error rate remains normal and infrastructure dashboards stay green makes the risk concrete: paging on every model refusal or low grader score creates fatigue, while the truly dangerous deny-bypass or stale-evidence pattern is buried. When this step is done well, the team responds to user harm quickly even though CPU, HTTP errors, and average latency look healthy.

### 3. Choose page, ticket, or record behavior and name owner, severity,

In the diagram, this is represented by **PAGE** and **RECORD**, near **OWNER**. Choose page, ticket, or record behavior and name owner, severity, acknowledgement, and escalation rules. Make alert payloads privacy-safe and include version, route, slice, denominator, current impact, start time, and relevant traces or artifacts. Every alert needs an owner, severity rule, acknowledgement target, escalation, runbook, evidence links, safe first actions, communication route, and closure condition. The case study where After a candidate canary, stale-policy failures rise in one route while overall error rate remains normal and infrastructure dashboards stay green shows the value: the team responds to user harm quickly even though CPU, HTTP errors, and average latency look healthy. Skip it, and paging on every model refusal or low grader score creates fatigue, while the truly dangerous deny-bypass or stale-evidence pattern is buried. The takeaway is clear: page for actionable impact, with a named owner, useful evidence, and a tested first decision.

### 4. Include impact, scope, version, slice, denominator, time, evidence links,

Make alert payloads privacy-safe and include version, route, slice, denominator, current impact, start time, and relevant traces or artifacts. This is why the step is non-negotiable: include impact, scope, version, slice, denominator, time, evidence links, and recent change context. Every alert needs an owner, severity rule, acknowledgement target, escalation, runbook, evidence links, safe first actions, communication route, and closure condition. In the diagram, this is represented by **USER IMPACT** and **MISSING EVIDENCE**. The case study where After a candidate canary, stale-policy failures rise in one route while overall error rate remains normal and infrastructure dashboards stay green proves it: the team responds to user harm quickly even though CPU, HTTP errors, and average latency look healthy. If the team omits this, paging on every model refusal or low grader score creates fatigue, while the truly dangerous deny-bypass or stale-evidence pattern is buried.

### 5. Write safe triage, containment, recovery, communication, and verification steps

Write safe triage, containment, recovery, communication, and verification steps with decision branches. Triage establishes whether the event is real, its impact and scope, what changed, and whether containment is safer than continued diagnosis. Every alert needs an owner, severity rule, acknowledgement target, escalation, runbook, evidence links, safe first actions, communication route, and closure condition. In the diagram, this is represented by **TRIAGE** and **CONTAIN**, near **RECOVER**. The case study where After a candidate canary, stale-policy failures rise in one route while overall error rate remains normal and infrastructure dashboards stay green makes the risk concrete: paging on every model refusal or low grader score creates fatigue, while the truly dangerous deny-bypass or stale-evidence pattern is buried. When this step is done well, the team responds to user harm quickly even though CPU, HTTP errors, and average latency look healthy.

### 6. Exercise the alert, measure noise and missed incidents, verify routing,

In the diagram, this is represented by **ALERT RULE**. Exercise the alert, measure noise and missed incidents, verify routing, and update or retire the rule. Make alert payloads privacy-safe and include version, route, slice, denominator, current impact, start time, and relevant traces or artifacts. Every alert needs an owner, severity rule, acknowledgement target, escalation, runbook, evidence links, safe first actions, communication route, and closure condition. The case study where After a candidate canary, stale-policy failures rise in one route while overall error rate remains normal and infrastructure dashboards stay green shows the value: the team responds to user harm quickly even though CPU, HTTP errors, and average latency look healthy. Skip it, and paging on every model refusal or low grader score creates fatigue, while the truly dangerous deny-bypass or stale-evidence pattern is buried. The takeaway is clear: page for actionable impact, with a named owner, useful evidence, and a tested first decision.

### 7. Putting it together

Taken together, these steps turn the objective "create alerts that lead a named person to a useful action instead of producing noise and dashboards nobody owns" into an operating contract. Define the user, business, safety, or observability condition that genuinely requires action; Choose page, ticket, or record behavior and name owner, severity, acknowledgement, and escalation rules; Include impact, scope, version, slice, denominator, time, evidence links, and recent change context. The remaining steps extend this: Write safe triage, containment, recovery, communication, and verification steps with decision branches; Exercise the alert, measure noise and missed incidents, verify routing, and update or retire the rule. The case of After a candidate canary, stale-policy failures rise in one route while overall error rate remains normal and infrastructure dashboards stay green shows how quickly paging on every model refusal or low grader score creates fatigue, while the truly dangerous deny-bypass or stale-evidence pattern is buried. The durable lesson is page for actionable impact, with a named owner, useful evidence, and a tested first decision.

### Analogy

A smoke alarm should wake someone for a probable fire, not beep for every piece of toast and certainly not ring in an empty building with nobody responsible for responding.

### The Next.js surface

In the Next.js surface, the same contract appears through framework-specific patterns. Build an operator incident view that resolves alert references to authorized traces, artifacts, release versions, budgets, and runbook steps without embedding sensitive payloads in notifications. Expose kill switch, rollback, and communication actions only to authorized roles and require reason, scope, confirmation, and decision receipts. Keep customer-facing status tied to verified incident state and approved communication, not speculative internal alerts.

### The Python surface

In the Python surface, the same contract is enforced with typed models and tests. Evaluate alert rules over normalized metrics and durable safety events, then deduplicate and group by incident candidate rather than paging per trace. Create typed Alert, Incident, Owner, RunbookStep, Action, Communication, and ClosureEvidence records with immutable histories. Test synthetic rule firing, routing, acknowledgement, escalation, stale ownership, missing telemetry, and closure verification in scheduled exercises.

---

## Case study — Stale-policy failures rise in one canary route

After a candidate canary, stale-policy failures rise in one route while overall error rate remains normal and infrastructure dashboards stay green.

### The walkthrough

1. A user-outcome alert detects the critical slice crossing its proposed guardrail with a sufficient denominator.
2. The page identifies the candidate version, route, start time, affected artifacts, and comparison with control.
3. The runbook pauses the canary, verifies the current policy source, preserves evidence, and communicates to support.
4. The owner closes the incident only after rollback traffic and fresh-answer cases verify recovery.

### The result

The team responds to user harm quickly even though CPU, HTTP errors, and average latency look healthy.

### The danger

Paging on every model refusal or low grader score creates fatigue, while the truly dangerous deny-bypass or stale-evidence pattern is buried.

### The takeaway

Page for actionable impact, with a named owner, useful evidence, and a tested first decision.

---

## Composition

SIGNALS enter from the left into an ALERT RULE that evaluates four inputs: USER IMPACT, BUDGET BURN, SAFETY VIOLATION, and MISSING EVIDENCE. From the rule, work routes to one of three lanes: PAGE NOW, TICKET SOON, or RECORD ONLY. PAGE NOW flows right into OWNER, SEVERITY, TRIAGE, RUNBOOK, CONTAIN, RECOVER, and COMMUNICATE, with an ACK CLOCK and an escalation ladder above it. A coral loop on the bottom left shows a NO OWNER alert cycling without action; a teal loop on the bottom right shows an ACTIONABLE alert closing with a RECEIPT. The layout is an incident-response flowchart: noisy signals are filtered, urgent ones get a named owner and runbook, and loops show what happens when ownership is missing or present.

## Element by element

- **SIGNALS** — The **SIGNALS** is entering ALERT RULE with USER IMPACT,.
- **ALERT RULE** — The **ALERT RULE** is the logic that decides whether a signal requires a response.
- **USER IMPACT** — The **USER IMPACT** is a cyan request or propagation path that sIGNALS entering ALERT RULE with ,.
- **BUDGET BURN** — The **BUDGET BURN** is a white record.
- **SAFETY VIOLATION** — The **SAFETY VIOLATION** is a teal healthy or verified result path.
- **MISSING EVIDENCE** — The **MISSING EVIDENCE** is a white record.
- **PAGE** — The **PAGE** is a cyan request or propagation path that route to NOW,.
- **TICKET SOON** — The **TICKET SOON** is the routing that creates a ticket for investigation without immediate paging.
- **RECORD** — The **RECORD** is oNLY.
- **OWNER** — The **OWNER** is a coral failure, risk, or incident path that pAGE NOW enters ,.
- **SEVERITY** — The **SEVERITY** is a cyan request or propagation path.
- **TRIAGE** — The **TRIAGE** is a rapid assessment of reality, impact, scope, and next action.
- **RUNBOOK** — The **RUNBOOK** is a tested decision guide for an operational situation.
- **CONTAIN** — The **CONTAIN** is a cyan request or propagation path.
- **RECOVER** — The **RECOVER** is a teal healthy or verified result path.
- **COMMUNICATE** — The **COMMUNICATE** is a cyan request or propagation path.
- **ACK CLOCK** — The **ACK CLOCK** is the timer that measures how long an alert waits for acknowledgement before escalating.
- **ACTIONABLE** — The **ACTIONABLE** is the user-experience gate that checks the user has a useful next step.
- **RECEIPT** — The **RECEIPT** is the durable, user-visible record of the completed business outcome.

---

## Colour and flow semantics

- **Cobalt platform** — a service, stage, dataset, quality gate, budget, release lane, or incident-control boundary. In this diagram it appears on **ALERT RULE**, **RUNBOOK**.
- **Cyan arrow** — a request, propagated context, telemetry signal, evaluation flow, or candidate release path. In this diagram it appears on **SIGNALS**, **USER IMPACT**, **PAGE**, **TICKET SOON**, **SEVERITY**, **TRIAGE**, **CONTAIN**, **COMMUNICATE** and others.
- **Teal arrow** — a healthy result, matched evidence, safe promotion, controlled degradation, recovery, or verified learning path. In this diagram it appears on **SAFETY VIOLATION**, **RECOVER**, **ACTIONABLE**.
- **Coral path** — a broken trace, failed assertion, regression, overload, unsafe outcome, rollback, alert, or incident path. In this diagram it appears on **OWNER**.
- **White card** — a span, event, metric, log, resource, case, score, budget, version, release, runbook, action, or regression record. In this diagram it appears on **BUDGET BURN**, **MISSING EVIDENCE**, **RECORD**, **RECEIPT**.

The overall flow moves from the inputs on the left through the incidents and continuous learning stages and exits as either a teal healthy path or a coral failure path. White cards carry the records, cobalt platforms hold the boundaries, and the cyan arrows show propagation and requests.

---

## How to present it

- Start with the operational question the team actually needs to answer. Point at the central element and ask what a regulator, evaluator, or support operator would ask about this outcome, and which signal type would best answer it.
- Ask the room what the team would need to know before approving the next release. Point at **USER IMPACT** and **SAFETY VIOLATION** and ask what would change if this step were skipped? Use the case study to make the failure concrete.
- Have the group list the operational decisions this stage informs. Highlight **PAGE** and **RECORD** and ask what real decision does this evidence support? Use the case study to make the failure concrete.
- Ask what evidence would change the route a support ticket takes. Trace with your finger **USER IMPACT** and **MISSING EVIDENCE** and ask what would a missing or corrupted value look like here? Use the case study to make the failure concrete.
- Get the room to name the owner who would need this evidence in an incident. Put a marker on **TRIAGE** and **CONTAIN** and ask who owns the evidence produced at this step? Use the case study to make the failure concrete.
- Ask what would need to be true for the team to skip this stage safely. Ask the room to locate **ALERT RULE** and ask which downstream stage would fail if this step were wrong? Use the case study to make the failure concrete.
- Use the analogy. A smoke alarm should wake someone for a probable fire, not beep for every piece of toast and certainly not ring in an empty building with nobody responsible for responding. Ask the room where the equivalent tracking number, queue, or ledger is in their own system, and where it would first break.
- Tell the case study — Stale-policy failures rise in one canary route. Walk through the walkthrough and stop at the moment the failure first becomes visible. Ask what signal, gate, or version field would have caught it earlier.
- Run the lab. Write three Acme alerts: forbidden effect, stale-evidence slice, and queue saturation. For each, define denominator, proposed threshold, severity, owner, page or ticket, acknowledgement, escalation, evidence payload, runbook first action, communication, and closure proof. Have each group label the fields that are captured, hashed, redacted, or omitted.
- Pose the checkpoint. Should every failed evaluation case generate a production page? Let the room answer before confirming with the answer. Then ask what the team would change in the next build based on the answer.
- Before moving on, ask the room to trace one healthy teal path and one coral path through the diagram, naming the evidence that flips the colour at each stage.
- Close on the contract. Page for actionable impact, with a named owner, useful evidence, and a tested first decision. Make the group write one sentence that ties the lesson to their own system.

---

## Lab and checkpoint

**Lab:** Write three Acme alerts: forbidden effect, stale-evidence slice, and queue saturation. For each, define denominator, proposed threshold, severity, owner, page or ticket, acknowledgement, escalation, evidence payload, runbook first action, communication, and closure proof.

**Checkpoint:** Should every failed evaluation case generate a production page?

**Answer:** No. Individual failures usually belong in evaluation results or tickets. Page when a severe singular event or actionable pattern requires immediate human response.

---

## Glossary

- **Triage** — rapid assessment of reality, impact, scope, and next action
- **Runbook** — tested decision guide for an operational situation
- **Alert fatigue** — reduced attention caused by excessive noisy alerts

---

## Sources

- [Google SRE monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Google SRE incident response](https://sre.google/workbook/incident-response/)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

---

## Related lessons

- Diagram 175 — Privacy-safe telemetry and content capture policy
- Diagram 187 — Load, concurrency, queues, capacity, and saturation
- Diagram 195 — Postmortems, corrective actions, and regression cases

---
