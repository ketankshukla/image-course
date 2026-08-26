# Diagram 240 — Runbooks, support, incident response, and operational ownership

![An operational loop moves from alert through triage, containment, communication, recovery, verification, and learning under runbooks, on-call, support, ownership, status, incident command, and evidence.](../diagrams/240-operational-ownership-loop.png)

**Module:** Delivery and production readiness
**Role in the course:** Define who notices, decides, communicates, recovers, verifies, and learns when the agent system behaves badly or becomes unavailable.
**Layout:** ON CALL begins on the left and the diagram flows toward SERVICE RESTORED; a teal **SERVICE RESTORED** path is the desired route and a coral **SILENT RETRY** path is blocked or contained.

---

## At a glance

**Runbooks, support, incident response, and operational ownership** — Define who notices, decides, communicates, recovers, verifies, and learns when the agent system behaves badly or becomes unavailable.

- The central takeaway is: Operate the complete user and business outcome: detect, contain, communicate, reconcile, verify, and learn.
- The visual begins with **ON CALL** and ends with the diagram's outcome, not a technology name.
- The safe or selected path is marked **teal**: SERVICE RESTORED then REGRESSION FIXTURE.
- The blocked or dangerous path is marked **coral**: SILENT RETRY and OWNER UNKNOWN blocked.
- The analogy is: A fire drill names who calls emergency services, who guides people, which exits are safe, where everyone gathers, and how the building is checked. A map of the alarm system alone would not coordinate the response.

---

## What the diagram teaches

### 1. Runbooks, support, incident response, and operational ownership

Asking users to paste raw prompts, tokens, or customer records into tickets is not a support strategy. Learning produces a blameless explanation of contributing conditions, control gaps, impact, detection, response, and actions. In the diagram, **INCIDENT COMMAND**, **SUPPORT** appear at the left, turning this idea into something a reviewer can point at.

### 2. Inventory Components, Service Objectives, Alerts, Owners, Support Paths, and Safe Degraded Modes.

Every service, queue, policy, data store, provider, model, protocol adapter, feature flag, and user-facing degraded mode has a named team, alert path, and decision authority. Support needs product-language receipts, correlation identifiers, known-issue guidance, privacy-safe diagnostics, and a path to engineering. The visual places **SERVICE RESTORED**, **SUPPORT** at the center; the arrows between them are the physical expression of this principle. If this is skipped, silent retries can multiply harm, while an ownerless alert can leave users in an uncertain state long after infrastructure appears healthy.

### 3. Start with Symptom-based Runbooks with Containment, Evidence, Communication, Recovery, and Escalation Steps.
![A controlled game day injects provider loss, duplicate queue delivery, stale policy, token replay, and regional failure while teams detect, contain, degrade, recover, reconcile, verify, and record evidence.](../diagrams/242-failure-game-day-recovery.png)

Diagram 242 — *Failure game day and recovery demonstration* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

Incident response separates command, technical investigation, communications, legal or privacy coordination where needed, and business decisions. The trace asks the team to write symptom-based runbooks with containment, evidence, communication, recovery, and escalation steps. Look at **EVIDENCE** on the top: the diagram uses those elements to show where this decision lives.

### 4. Exercise Incident Roles and Preserve a Factual Correlation-based Timeline.

A clear timeline records facts without exposing private model reasoning or unverified guesses. The picture shows **INCIDENT COMMAND** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: The runbook disables further retries for the affected idempotency class and places cases in an uncertain state.

### 5. Reconcile Authoritative Effects and User-visible State Before Declaring Recovery Complete.

Production ownership begins before deployment. A runbook turns an alert into safe actions: confirm scope, protect users, stop harmful effects, preserve evidence, choose degraded mode, communicate, restore, verify, and escalate. Recovery requires verification of business state, queued work, duplicate effects, artifacts, caches, indexes, audit, and user-visible status. To put this into practice, the team should reconcile authoritative effects and user-visible state before declaring recovery complete. At the bottom, **ON CALL**, **INCIDENT COMMAND**, **SERVICE RESTORED** is the element that makes this concept concrete before any code is written.

### 6. Convert Causes and Near Misses Into Owned Tests, Monitors, Runbooks, and Architecture Improvements.

Restoring one API process is not enough if Maya still sees stale or uncertain decisions. Every meaningful failure becomes a test, monitor, runbook improvement, or architecture change with an owner and due date. In the diagram, **ON CALL**, **INCIDENT COMMAND**, **SERVICE RESTORED** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, every meaningful failure becomes a test, monitor, runbook improvement, or architecture change with an owner and due date.

### 7. Operate the complete user and business outcome

It includes commands and links but also decision limits and rollback cautions. The visual places **ON CALL**, **INCIDENT COMMAND**, **SERVICE RESTORED** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

A fire drill names who calls emergency services, who guides people, which exits are safe, where everyone gathers, and how the building is checked. A map of the alarm system alone would not coordinate the response. Look at **ON CALL**, **INCIDENT COMMAND**, **SERVICE RESTORED** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: A provider timeout occurs after a refund request may have been accepted, and automatic retries begin creating conflicting states.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Provide honest status, preserved drafts, retry, cancel, support reference, and later-return paths for dependency and incident states.
- Expose safe correlation receipts to Maya without including secrets, internal stack traces, or other tenants' details.
- Keep emergency feature disablement and status messaging testable in preview fixtures and accessible under keyboard and screen-reader use.

Together these choices prevent the mistakes in the Acme case—A provider timeout occurs after a refund request may have been accepted, and automatic retries begin creating conflicting states.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Emit actionable alerts from service objectives and unacceptable outcomes rather than every individual provider warning.
- Build administrative containment for pausing workers, disabling effectful tools, quarantining tenants, rotating credentials, and replaying work with authorization.
- Create reconciliation jobs that compare workflow, business receipts, queue state, artifacts, and projections after uncertain effects.

These boundaries make the Acme case—A provider timeout occurs after a refund request may have been accepted, and automatic retries begin creating conflicting states.—testable and replaceable.

---

## Case study — A provider timeout occurs after a refund request may have

A provider timeout occurs after a refund request may have been accepted, and automatic retries begin creating conflicting states.

### The walkthrough

1. The runbook disables further retries for the affected idempotency class and places cases in an uncertain state.
2. Incident responders query authoritative provider receipts and Acme's idempotency records using correlation IDs.
3. Maya sees preserved work and a support reference while confirmed commits and safe retries are reconciled.
4. The post-incident action adds an uncertain-effect fixture, alert, bounded retry rule, and updated provider runbook.

### The result

Acme restores trustworthy business and interface state rather than merely restarting the service.

### The danger

Silent retries can multiply harm, while an ownerless alert can leave users in an uncertain state long after infrastructure appears healthy.

### The takeaway

Operate the complete user and business outcome: detect, contain, communicate, reconcile, verify, and learn.

---

## Composition

The picture is an operational loop. An **ALERT** card at the left enters a cycle of six white steps—**TRIAGE**, **CONTAIN**, **COMMUNICATE**, **RECOVER**, **VERIFY**, **LEARN**—arranged in a ring. Around the ring, supporting cards—**RUNBOOK**, **ON CALL**, **SUPPORT**, **OWNER**, **STATUS**, **INCIDENT COMMAND**, **EVIDENCE**—float. A teal path from **SERVICE RESTORED** leads to a **REGRESSION FIXTURE**. Two coral blocked paths—**SILENT RETRY** and **OWNER UNKNOWN**—are blocked. The composition shows operations as a closed learning loop.

## Element by element

- **ON CALL** — the ON CALL card shown in this diagram; it is one of the labeled elements the architecture uses.
- **INCIDENT COMMAND** — Incident response separates command, technical investigation, communications, legal or privacy coordination where needed, and business decisions.
- **SERVICE RESTORED** — the safe, verified, or authoritative element marked in teal; in this diagram SERVICE RESTORED then REGRESSION FIXTURE.
- **REGRESSION FIXTURE** — the safe, verified, or authoritative element marked in teal; in this diagram SERVICE RESTORED then REGRESSION FIXTURE.
- **SILENT RETRY** — the coral anti-pattern of repeating an action without observation or evidence.
- **OWNER UNKNOWN** — the coral anti-pattern of an alert or decision with no accountable person.
- **ALERT** — Every service, queue, policy, data store, provider, model, protocol adapter, feature flag, and user-facing degraded mode has a named team, alert path, and decision authority.
- **TRIAGE** — a labeled visual element in this diagram; the prompt shows it as ALERT entering TRIAGE.
- **CONTAIN** — Operate the complete user and business outcome: detect, contain, communicate, reconcile, verify, and learn.
- **COMMUNICATE** — A runbook turns an alert into safe actions: confirm scope, protect users, stop harmful effects, preserve evidence, choose degraded mode, communicate, restore, verify, and escalate.
- **RECOVER** — the RECOVER card shown in this diagram; it is one of the labeled elements the architecture uses.
- **VERIFY** — A runbook turns an alert into safe actions: confirm scope, protect users, stop harmful effects, preserve evidence, choose degraded mode, communicate, restore, verify, and escalate.
- **LEARN** — Operate the complete user and business outcome: detect, contain, communicate, reconcile, verify, and learn.
- **RUNBOOK** — A runbook turns an alert into safe actions: confirm scope, protect users, stop harmful effects, preserve evidence, choose degraded mode, communicate, restore, verify, and escalate.
- **SUPPORT** — Support needs product-language receipts, correlation identifiers, known-issue guidance, privacy-safe diagnostics, and a path to engineering.
- **OWNER** — Every meaningful failure becomes a test, monitor, runbook improvement, or architecture change with an owner and due date.
- **STATUS** — Recovery requires verification of business state, queued work, duplicate effects, artifacts, caches, indexes, audit, and user-visible status.
- **EVIDENCE** — A runbook turns an alert into safe actions: confirm scope, protect users, stop harmful effects, preserve evidence, choose degraded mode, communicate, restore, verify, and escalate.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **ON CALL**, **INCIDENT COMMAND**, **ALERT**, **TRIAGE**, **CONTAIN**, **COMMUNICATE** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **ON CALL**, **INCIDENT COMMAND**, **ALERT**, **TRIAGE** carry the forward motion of the architecture.
- **Teal arrow** — an authoritative decision, verified contract, passing gate, safe release, or recovered service. The teal elements **SERVICE RESTORED**, **REGRESSION FIXTURE** show the path the design wants to keep open.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **SILENT RETRY**, **OWNER UNKNOWN** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **ON CALL**, **INCIDENT COMMAND**, **ALERT**, **TRIAGE**, **CONTAIN**, **COMMUNICATE**, **RECOVER**, **VERIFY** are the readable records the diagram communicates.

---

## How to present it

- Point to **ON CALL** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **SERVICE RESTORED** and ask what would have to change for the team to inventory components, service objectives, alerts, owners, support paths, and safe degraded modes, and who would own that change.
- Point to **EVIDENCE** and ask what evidence would show the team has already write symptom-based runbooks with containment, evidence, communication, recovery, and escalation steps, and what test would fail first if it is missing.
- Point to **INCIDENT COMMAND** and ask who else in the room must agree before the team can exercise incident roles and preserve a factual correlation-based timeline, and what would change their mind.
- Point to **REGRESSION FIXTURE** and ask what the smallest version of reconcile authoritative effects and user-visible state before declaring recovery complete looks like, and what would be left out of that version.
- Point to **SILENT RETRY** and ask what would have to change for the team to convert causes and near misses into owned tests, monitors, runbooks, and architecture improvements, and who would own that change.
- Trace the **teal** path (SERVICE RESTORED then REGRESSION FIXTURE) and ask what evidence would prove the real system follows it, who collects that evidence, and how often it is refreshed.
- Show the **coral** path (SILENT RETRY and OWNER UNKNOWN blocked) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Point to **OWNER UNKNOWN** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Point to **OWNER** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Use the analogy: A fire drill names who calls emergency services, who guides people, which exits are safe, where everyone gathers, and how the building is checked. A map of the alarm system alone would not coordinate the response. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Write two runbooks and one incident exercise for provider uncertain effects, cross-tenant evidence exposure, or queue backlog. Include triggers, owners, authority, containment, evidence, communications, privacy, degraded UX, reconciliation, verification, and follow-up tests.
- Pose the checkpoint: *Is service recovery complete when health checks return green?*

---

## Lab and checkpoint

**Lab:** Write two runbooks and one incident exercise for provider uncertain effects, cross-tenant evidence exposure, or queue backlog. Include triggers, owners, authority, containment, evidence, communications, privacy, degraded UX, reconciliation, verification, and follow-up tests.

**Checkpoint:** Is service recovery complete when health checks return green?

**Answer:** No. Verify authoritative effects, queued work, artifacts, projections, user-visible state, notifications, and any privacy or security consequences.

---

## Glossary

- **Runbook** — tested guide for diagnosing and responding
- **Reconciliation** — comparing records to restore a trustworthy shared state
- **Incident command** — clear coordination and decision roles during disruption

---

## Sources

- OpenTelemetry semantic conventions 1.44.0
- NIST AI Risk Management Framework
- FastAPI deployment concepts
- Vercel deployments

---

## Related lessons

- **Lesson 228** — Deployment topology, failure domains, and ownership (`deployment-topology-failure-domains`)
- **Lesson 235** — Telemetry, evaluation, analytics, and cost control (`telemetry-evaluation-cost-control-plane`)
- **Lesson 242** — Failure game day and recovery demonstration (`failure-game-day-recovery`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for Runbooks, support, incident response, and operational ownership until the diagram is legible to every reviewer. Define who notices, decides, communicates, recovers, verifies, and learns when the agent system behaves badly or becomes unavailable. The trace moves through 5 decisions: Inventory components, service objectives, alerts, owners, support paths, and safe degraded modes.; Write symptom-based runbooks with containment, evidence, communication, recovery, and escalation steps.; Exercise incident roles and preserve a factual correlation-based timeline.; Reconcile authoritative effects and user-visible state before declaring recovery complete.; Convert causes and near misses into owned tests, monitors, runbooks, and architecture improvements.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—A provider timeout occurs after a refund request may have been accepted, and automatic retries begin creating conflicting states.—shows that Operate the complete user and business outcome: detect, contain, communicate, reconcile, verify, and learn. If the team skips this, Silent retries can multiply harm, while an ownerless alert can leave users in an uncertain state long after infrastructure appears healthy. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.