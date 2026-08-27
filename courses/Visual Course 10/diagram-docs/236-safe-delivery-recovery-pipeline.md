# Diagram 236 — CI/CD, environments, migrations, flags, rollback, and recovery

![Code passes lint, test, contract, security, accessibility, evaluation, build, and provenance gates before promotion across environments with migrations, flags, canaries, rollback, and restore controls.](../diagrams/236-safe-delivery-recovery-pipeline.png)

**Module:** Platform, data, and deployment
**Role in the course:** Design a release path that can prove what changed, limit exposure, reverse safely, and recover data as well as code.
**Layout:** FEATURE FLAG begins on the left and the diagram flows toward VERIFIED RELEASE; a teal **VERIFIED RELEASE** path is the desired route and a coral **DIRECT PROD** path is blocked or contained.

---

## At a glance

**CI/CD, environments, migrations, flags, rollback, and recovery** — Design a release path that can prove what changed, limit exposure, reverse safely, and recover data as well as code.

- The central takeaway is: Release a known artifact through evidence gates, and rehearse recovery for code, data, work, and users.
- The visual begins with **FEATURE FLAG** and ends with the diagram's outcome, not a technology name.
- The safe or selected path is marked **teal**: VERIFIED RELEASE.
- The blocked or dangerous path is marked **coral**: DIRECT PROD and IRREVERSIBLE MIGRATION blocked.
- The analogy is: A stage production rehearses in a workshop, then on the real stage, then before a small audience. It keeps the previous set, emergency lighting, cues, and responsible crew ready; opening night is not the first complete test.

---

## What the diagram teaches

### 1. CI/CD, environments, migrations, flags, rollback, and recovery

Old code paths and stale flags create lasting complexity and risk. Recovery proves more than redeployment. In the diagram, **ROLLBACK** appear at the left, turning this idea into something a reviewer can point at.

### 2. Build One Immutable Versioned Artifact with Dependency and Provenance Evidence.

The pipeline includes formatting, static checks, unit, contract, integration, workflow, security, accessibility, evaluation, build, dependency, provenance, and artifact-signing evidence appropriate to the risk. The visual places **BUILD**, **PROVENANCE** at the center; the arrows between them are the physical expression of this principle. If this is skipped, the pipeline includes formatting, static checks, unit, contract, integration, workflow, security, accessibility, evaluation, build, dependency, provenance, and artifact-signing evidence appropriate to the risk.
![A layered test system combines unit, property, contract, integration, workflow, security, evaluation, accessibility, and acceptance tests using shared fixtures and failure injection to produce an evidence manifest.](../diagrams/238-production-test-pyramid.png)

Diagram 238 — *Contract, integration, workflow, security, and acceptance tests* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 3. Run Code, Contract, Security, Accessibility, Evaluation, and Data-migration Gates.

Database and index migrations require forward and backward compatibility, ownership, backup, tested rollback or roll-forward, and a plan for long-running transformations. Reverting code cannot reverse an unsafe destructive data migration. The trace asks the team to run code, contract, security, accessibility, evaluation, and data-migration gates. Look at **IRREVERSIBLE MIGRATION**, **CODE**, **CONTRACT** on the top: the diagram uses those elements to show where this decision lives.

### 4. Promote Through Isolated Environments with Synthetic Fixtures and Version Manifests.

Continuous delivery promotes a known artifact through controlled environments. The picture shows **FEATURE FLAG**, **VERIFIED RELEASE**, **DIRECT PROD** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: The revised plan first expands the schema and supports both contract versions.

### 5. Release Gradually Using Flags or Canaries with Stop, Rollback, and Fallback Rules.

Feature flags, canaries, and rolling exposure reduce blast radius only when there is a kill switch, monitoring, deterministic fallback, owner, expiry, and cleanup. To put this into practice, the team should release gradually using flags or canaries with stop, rollback, and fallback rules. At the bottom, **VERIFIED RELEASE**, **ROLLBACK** is the element that makes this concept concrete before any code is written.

### 6. Rehearse Code Rollback, Data Restore, Queue Reconciliation, and User Recovery Before Production Exposure.

Development, preview, staging, and production need separate identities, secrets, data, providers, queues, domains, and policy. A preview should use synthetic or properly isolated data and should never inherit production authority by convenience. The team rehearses restore, queue replay, reconciliation, artifact verification, secret rotation, provider failover, and user communication, then records real recovery evidence. In the diagram, **CODE**, **PRODUCTION**, **ROLLBACK** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, the team rehearses restore, queue replay, reconciliation, artifact verification, secret rotation, provider failover, and user communication, then records real recovery evidence.

### 7. Release a known artifact through evidence gates

Continuous integration creates repeatable evidence from source changes. A deployment is not a release until users are intentionally exposed and the required gates remain healthy. The visual places **VERIFIED RELEASE** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

A stage production rehearses in a workshop, then on the real stage, then before a small audience. It keeps the previous set, emergency lighting, cues, and responsible crew ready; opening night is not the first complete test. Look at **FEATURE FLAG**, **VERIFIED RELEASE**, **DIRECT PROD** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: Acme deploys a new proposal schema; the web app rolls back, but the database migration has already removed the field the old version requires.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Use Vercel preview deployments with isolated configuration and synthetic data, then promote only the exact reviewed build.
- Keep feature decisions server-resolved for sensitive behavior and render a deterministic accessible fallback when a flag or dependency is unavailable.
- Verify routes, bundles, environment variables, headers, images, streaming, accessibility, and API compatibility in every promotion stage.

Together these choices prevent the mistakes in the Acme case—Acme deploys a new proposal schema; the web app rolls back, but the database migration has already removed the field the old version requires.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Package the service immutably, run migrations as controlled jobs, and separate request, worker, scheduler, and maintenance processes.
- Use expand-and-contract schema changes so old and new versions can coexist during rollout, with backups and reconciliation evidence.
- Expose release, contract, model, prompt, policy, migration, and worker versions in authorized diagnostics and telemetry manifests.

These boundaries make the Acme case—Acme deploys a new proposal schema; the web app rolls back, but the database migration has already removed the field the old version requires.—testable and replaceable.

---

## Case study — Acme deploys a new proposal schema

Acme deploys a new proposal schema; the web app rolls back, but the database migration has already removed the field the old version requires.

### The walkthrough

1. The revised plan first expands the schema and supports both contract versions.
2. Web and service releases are canaried with compatibility tests while data is backfilled safely.
3. Only after the old version is retired and recovery is verified does a separate cleanup remove the legacy field.
4. The release manifest records code, contract, migration, flag, evidence, owner, and rollback state.

### The result

Acme can reverse application exposure without discovering that the data path made rollback impossible.

### The danger

A green build can still ship incompatible contracts, leaked secrets, inaccessible UI, unsafe migrations, untested restores, and unrecoverable external effects.

### The takeaway

Release a known artifact through evidence gates, and rehearse recovery for code, data, work, and users.

---

## Composition

The picture is a delivery pipeline. On the left, **CODE** enters a row of **CI** gates—**LINT**, **TEST**, **CONTRACT**, **SECURITY**, **A11Y**, **EVAL**, **BUILD**, **PROVENANCE**. Below, a promotion ladder runs **DEV** to **PREVIEW** to **STAGING** to **PRODUCTION**. In the center, **MIGRATION**, **FEATURE FLAG**, **CANARY**, **ROLLBACK**, and **RESTORE** cards sit between stages. A teal **VERIFIED RELEASE** path exits. Two coral blocked paths—**DIRECT PROD** and **IRREVERSIBLE MIGRATION**—are stopped. The composition reads left to right as a trust-but-verify release path.

## Element by element

- **FEATURE FLAG** — the FEATURE FLAG card shown in this diagram; it is one of the labeled elements the architecture uses.
- **VERIFIED RELEASE** — the safe, verified, or authoritative element marked in teal; in this diagram VERIFIED RELEASE.
- **DIRECT PROD** — the coral anti-pattern of promoting code straight to production without gates.
- **IRREVERSIBLE MIGRATION** — the coral anti-pattern of deploying a data change that cannot be undone.
- **CODE** — Reverting code cannot reverse an unsafe destructive data migration.
- **CI** — a labeled visual element in this diagram; the prompt shows it as CODE to CI gates LINT.
- **LINT** — a labeled visual element in this diagram; the prompt shows it as CODE to CI gates LINT.
- **TEST** — the TEST card shown in this diagram; it is one of the labeled elements the architecture uses.
- **CONTRACT** — The pipeline includes formatting, static checks, unit, contract, integration, workflow, security, accessibility, evaluation, build, dependency, provenance, and artifact-signing evidence appropriate to the risk.
- **SECURITY** — The pipeline includes formatting, static checks, unit, contract, integration, workflow, security, accessibility, evaluation, build, dependency, provenance, and artifact-signing evidence appropriate to the risk.
- **EVAL** — the EVAL card shown in this diagram; it is one of the labeled elements the architecture uses.
- **BUILD** — The pipeline includes formatting, static checks, unit, contract, integration, workflow, security, accessibility, evaluation, build, dependency, provenance, and artifact-signing evidence appropriate to the risk.
- **PROVENANCE** — The pipeline includes formatting, static checks, unit, contract, integration, workflow, security, accessibility, evaluation, build, dependency, provenance, and artifact-signing evidence appropriate to the risk.
- **DEV** — a labeled visual element in this diagram; the prompt shows it as Promote DEV to PREVIEW to STAGING to PRODUCTION.
- **PREVIEW** — Development, preview, staging, and production need separate identities, secrets, data, providers, queues, domains, and policy.
- **STAGING** — Development, preview, staging, and production need separate identities, secrets, data, providers, queues, domains, and policy.
- **PRODUCTION** — Development, preview, staging, and production need separate identities, secrets, data, providers, queues, domains, and policy.
- **MIGRATION** — Reverting code cannot reverse an unsafe destructive data migration.
- **CANARY** — limited exposure used to detect problems.
- **ROLLBACK** — Database and index migrations require forward and backward compatibility, ownership, backup, tested rollback or roll-forward, and a plan for long-running transformations.
- **RESTORE** — The team rehearses restore, queue replay, reconciliation, artifact verification, secret rotation, provider failover, and user communication, then records real recovery evidence.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **FEATURE FLAG**, **CODE**, **CI**, **LINT**, **TEST**, **CONTRACT** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **FEATURE FLAG**, **CODE**, **CI**, **LINT** carry the forward motion of the architecture.
- **Teal arrow** — an authoritative decision, verified contract, passing gate, safe release, or recovered service. The teal elements **VERIFIED RELEASE** show the path the design wants to keep open.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **DIRECT PROD**, **IRREVERSIBLE MIGRATION** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **FEATURE FLAG**, **CODE**, **CI**, **LINT**, **TEST**, **CONTRACT**, **SECURITY**, **EVAL** are the readable records the diagram communicates.

---

## How to present it

- Point to **FEATURE FLAG** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **BUILD** and ask what would have to change for the team to build one immutable versioned artifact with dependency and provenance evidence, and who would own that change.
- Point to **IRREVERSIBLE MIGRATION** and ask what evidence would show the team has already run code, contract, security, accessibility, evaluation, and data-migration gates, and what test would fail first if it is missing.
- Point to **VERIFIED RELEASE** and ask who else in the room must agree before the team can promote through isolated environments with synthetic fixtures and version manifests, and what would change their mind.
- Point to **ROLLBACK** and ask what the smallest version of release gradually using flags or canaries with stop, rollback, and fallback rules looks like, and what would be left out of that version.
- Point to **CODE** and ask what would have to change for the team to rehearse code rollback, data restore, queue reconciliation, and user recovery before production exposure, and who would own that change.
- Trace the **teal** path (VERIFIED RELEASE) and ask what evidence would prove the real system follows it, who collects that evidence, and how often it is refreshed.
- Show the **coral** path (DIRECT PROD and IRREVERSIBLE MIGRATION blocked) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Use the analogy: A stage production rehearses in a workshop, then on the real stage, then before a small audience. It keeps the previous set, emergency lighting, cues, and responsible crew ready; opening night is not the first complete test. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Design the dual-stack delivery pipeline. Include environment isolation, artifact provenance, all test gates, preview data, migrations, flags, canary, kill switch, rollback, restore, queue replay, secret rotation, incident communication, owners, and release manifest.
- Pose the checkpoint: *Does rolling back application code automatically restore the previous data model?*

---

## Lab and checkpoint

**Lab:** Design the dual-stack delivery pipeline. Include environment isolation, artifact provenance, all test gates, preview data, migrations, flags, canary, kill switch, rollback, restore, queue replay, secret rotation, incident communication, owners, and release manifest.

**Checkpoint:** Does rolling back application code automatically restore the previous data model?

**Answer:** No. Data changes need their own compatibility, backup, rollback or roll-forward, and reconciliation strategy.

---

## Glossary

- **Promotion** — moving the same reviewed artifact to a later environment
- **Canary** — limited exposure used to detect problems
- **Provenance** — evidence describing how an artifact was produced

---

## Sources

- GitHub Actions documentation
- Vercel deployments
- Vercel rolling releases
- SLSA specification
- OpenSSF Scorecard

---

## Related lessons

- **Lesson 228** — Deployment topology, failure domains, and ownership (`deployment-topology-failure-domains`)
- **Lesson 238** — Contract, integration, workflow, security, and acceptance tests (`production-test-pyramid`)
- **Lesson 240** — Runbooks, support, incident response, and operational ownership (`operational-ownership-loop`)
---

### Why this diagram must precede the build

The team should not begin with code, prompts, or models for CI/CD, environments, migrations, flags, rollback, and recovery until the diagram is legible to every reviewer. Design a release path that can prove what changed, limit exposure, reverse safely, and recover data as well as code. The trace moves through 5 decisions: Build one immutable versioned artifact with dependency and provenance evidence.; Run code, contract, security, accessibility, evaluation, and data-migration gates.; Promote through isolated environments with synthetic fixtures and version manifests.; Release gradually using flags or canaries with stop, rollback, and fallback rules.; Rehearse code rollback, data restore, queue reconciliation, and user recovery before production exposure.. Each decision maps to a labeled element in the picture, and each label must have an owner, a contract, and an acceptance test before the corresponding code is written.

The case study—Acme deploys a new proposal schema; the web app rolls back, but the database migration has already removed the field the old version requires.—shows that Release a known artifact through evidence gates, and rehearse recovery for code, data, work, and users. If the team skips this, A green build can still ship incompatible contracts, leaked secrets, inaccessible UI, unsafe migrations, untested restores, and unrecoverable external effects. The diagram is the contract the two projects share. Until the team can trace the problem through the labels, assign owners to each card, and write the corresponding test, the build will drift from the architecture.

Before writing the first route, prompt, or adapter, the team should be able to answer: what is the user outcome this diagram protects, which card owns each decision, what evidence moves across each arrow, where the coral anti-patterns first appear, what test or gate proves the real system matches the picture, and which fixture will catch the next regression. When those answers are visible and reviewable, the build becomes a direct translation of the architecture rather than a guess about it. The diagram is the earliest acceptance test the project can write. Keeping it current is cheaper than debugging the drift it prevents. A reviewer who cannot read the diagram will not be able to read the build. Start every build review by pointing at the diagram, not the code.