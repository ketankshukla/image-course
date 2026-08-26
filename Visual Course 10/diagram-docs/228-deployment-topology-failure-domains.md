# Diagram 228 — Deployment topology, failure domains, and ownership

![A deployment topology spans Vercel, Next.js, a Python API, workers, policy, database, vector index, queue, artifact storage, and providers with visible failure domains, owners, service objectives, degraded modes, and bulkheads.](../diagrams/228-deployment-topology-failure-domains.png)

**Module:** Reference architecture and contracts
**Role in the course:** Place services and data on a deployable topology that makes network paths, failure containment, scaling, recovery, and ownership visible.
**Layout:** VERCEL EDGE begins on the left and the diagram flows toward DEGRADED MODE; a teal **DEGRADED MODE** path is the desired route and a coral **CASCADE** path is blocked or contained.

---

## At a glance

**Deployment topology, failure domains, and ownership** — Place services and data on a deployable topology that makes network paths, failure containment, scaling, recovery, and ownership visible.

- The central takeaway is: Show where it runs, what fails together, who owns it, and what the user sees when it is unavailable.
- The visual begins with **VERCEL EDGE** and ends with the diagram's outcome, not a technology name.
- The safe or selected path is marked **teal**: DEGRADED MODE.
- The blocked or dangerous path is marked **coral**: CASCADE blocked by bulkheads.
- The analogy is: A ship has watertight compartments. The map shows not only which rooms exist but which doors can seal, who controls them, how alarms travel, and how the ship remains afloat when one compartment floods.

---

## What the diagram teaches

### 1. Deployment topology, failure domains, and ownership

A deployment topology says where they run, which networks they cross, how they scale, and what can fail together. In the diagram, **FAILURE DOMAINS REGION**, **FAILURE DOMAINS** appear at the left, turning this idea into something a reviewer can point at.

### 2. Place Public Edge, Web, API, Workers, Protocols, Data Stores

Stateless web or API instances can scale horizontally only if durable state and idempotency live elsewhere. Acme may preserve case notes, show cached public documentation with a freshness warning, queue a retry, or disable commits while identity or policy is unavailable. The visual places **VERCEL EDGE**, **NEXTJS WEB**, **PYTHON API** at the center; the arrows between them are the physical expression of this principle. If this is skipped, a diagram of boxes without networks, regions, scaling, failure domains, ownership, and recovery is not a deployable architecture.
![A client experience uses AG-UI with an agent service, which uses MCP for tools and context, A2A for peer agents, HTTP for business APIs, queues for durable work, and internal calls within the domain.](../diagrams/227-protocol-boundary-routing-map.png)

Diagram 227 — *MCP, A2A, AG-UI, HTTP, queue, and internal boundaries* is the next lens on this idea. The same concepts reappear there with different emphasis, so the two diagrams should be read as a pair.

### 3. Draw Authentication, Encryption, Egress, Region, Tenant, and Data-residency Paths.

Stateful dependencies need backup, restore, migration, replication, and regional decisions. The trace asks the team to draw authentication, encryption, egress, region, tenant, and data-residency paths. Look at **FAILURE DOMAINS REGION**, **DATABASE**, **TENANT** on the top: the diagram uses those elements to show where this decision lives.

### 4. Mark Process, Service, Provider, Account, Region, and Tenant Failure Domains.

The blueprint must not pretend they share memory, filesystem, deployment lifecycle, region, or transaction boundary. A failure domain is a set of components likely to become unavailable together, such as one process, service, region, account, provider, or tenant partition. The picture shows **FAILURE DOMAINS REGION**, **FAILURE DOMAINS**, **PROVIDERS** as the visual anchor for this idea, with the surrounding paths showing the flow. The project confirms the point: The topology reveals that long work was incorrectly placed inside the interactive request failure domain.

### 5. Assign Owner, Scaling Signal, Service Objective, Alert, Degraded Mode, Backup, and Recovery Target.

The Next.js application can run on Vercel while a Python API and workers run on a suitable service platform. Ownership appears on the topology: team, service objective, alert route, deployment pipeline, data classification, capacity assumption, cost center, and recovery responsibility. Degraded modes are product features. To put this into practice, the team should assign owner, scaling signal, service objective, alert, degraded mode, backup, and recovery target. At the bottom, **DEGRADED MODE**, **SERVICE**, **OWNER** is the element that makes this concept concrete before any code is written.

### 6. Walk Through Dependency Loss and Verify That Sensitive Actions Fail Safely Without Losing Preserved

Both views are needed before a full-stack build. Bulkheads, queues, limits, and fallbacks keep one failure from consuming the whole system. In the diagram, **FAILURE DOMAINS REGION**, **FAILURE DOMAINS** appear at the lower right, turning this idea into something a reviewer can point at. If this is skipped, bulkheads, queues, limits, and fallbacks keep one failure from consuming the whole system.

### 7. Show where it runs, what fails together, who owns it

A logical architecture says what components do. An unlabeled box becomes nobody's problem during an incident. The visual places **VERCEL EDGE**, **NEXTJS WEB**, **PYTHON API** at the upper left; the arrows between them are the physical expression of this principle.

### Analogy

A ship has watertight compartments. The map shows not only which rooms exist but which doors can seal, who controls them, how alarms travel, and how the ship remains afloat when one compartment floods. Look at **VERCEL EDGE**, **NEXTJS WEB**, **PYTHON API** on the left: the diagram uses those elements to show where this decision lives. The project confirms the point: The Python research service slows down, web requests pile up, and every Next.js page waits until the provider timeout finishes.

### The Next.js surface

The Next.js surface must own the human experience while keeping authority and secrets on the server side. In this diagram, that means the web boundary stops the coral anti-patterns before they reach the browser.

- Design Vercel routes and Functions as stateless compute; use explicit APIs, storage, and event paths rather than assuming local disk or process memory is durable.
- Separate public learning content, authenticated workspace, server-only integrations, and client-interactive surfaces with environment-specific configuration.
- Create visible degraded states for Python API, stream, artifact, and identity outages, including retry and support receipts.

Together these choices prevent the mistakes in the Acme case—The Python research service slows down, web requests pile up, and every Next.js page waits until the provider timeout finishes.—from becoming the architecture.

### The Python surface

The Python surface must keep business rules, protocols, and persistence in cleanly separated layers. In this diagram, that means FastAPI is one edge of a domain that does not leak into adapters or the model.

- Separate synchronous API, durable workers, schedulers, and migrations so each can scale and fail independently.
- Use health, readiness, graceful shutdown, connection limits, timeouts, and worker concurrency derived from actual workload tests.
- Keep database migrations and other one-time startup work outside replicated request processes to avoid races.

These boundaries make the Acme case—The Python research service slows down, web requests pile up, and every Next.js page waits until the provider timeout finishes.—testable and replaceable.

---

## Case study — The Python research service slows down, web requests pile up

The Python research service slows down, web requests pile up, and every Next.js page waits until the provider timeout finishes.

### The walkthrough

1. The topology reveals that long work was incorrectly placed inside the interactive request failure domain.
2. Acme returns a durable task handle, moves work to bounded workers, and applies queue and provider concurrency limits.
3. The web route shows preserved case state and an honest delayed status instead of a hanging page.
4. Service objectives and alerts distinguish web availability from delayed research completion.

### The result

A provider slowdown degrades one capability without making the entire workspace unusable.

### The danger

A diagram of boxes without networks, regions, scaling, failure domains, ownership, and recovery is not a deployable architecture.

### The takeaway

Show where it runs, what fails together, who owns it, and what the user sees when it is unavailable.

---

## Composition

The picture is a deployment topology. On the left, **INTERNET** flows to a **VERCEL EDGE** and a **NEXTJS WEB** platform. In the center, a **PYTHON API** connects to a **WORKER POOL**, **POLICY**, **DATABASE**, **VECTOR**, **QUEUE**, **ARTIFACT STORE**, and **PROVIDERS**. Labeled **FAILURE DOMAINS**—**REGION**, **SERVICE**, **TENANT**, **PROVIDER**—appear as boundaries. **OWNER** and **SLO** cards sit beside components. A teal **DEGRADED MODE** path shows how service continues. A coral **CASCADE** is blocked by **BULKHEADS**. The composition makes ownership and blast radius visible.

## Element by element

- **VERCEL EDGE** — a labeled visual element in this diagram; the prompt shows it as INTERNET to VERCEL EDGE and NEXTJS WEB.
- **NEXTJS WEB** — a labeled visual element in this diagram; the prompt shows it as INTERNET to VERCEL EDGE and NEXTJS WEB.
- **PYTHON API** — The Next.js application can run on Vercel while a Python API and workers run on a suitable service platform.
- **WORKER POOL** — the WORKER POOL card shown in this diagram; it is one of the labeled elements the architecture uses.
- **ARTIFACT STORE** — the ARTIFACT STORE card shown in this diagram; it is one of the labeled elements the architecture uses.
- **FAILURE DOMAINS REGION** — Mark process, service, provider, account, region, and tenant failure domains.
- **DEGRADED MODE** — Assign owner, scaling signal, service objective, alert, degraded mode, backup, and recovery target.
- **FAILURE DOMAINS** — Mark process, service, provider, account, region, and tenant failure domains.
- **INTERNET** — a labeled visual element in this diagram; the prompt shows it as INTERNET to VERCEL EDGE and NEXTJS WEB.
- **POLICY** — Acme may preserve case notes, show cached public documentation with a freshness warning, queue a retry, or disable commits while identity or policy is unavailable.
- **DATABASE** — the DATABASE card shown in this diagram; it is one of the labeled elements the architecture uses.
- **VECTOR** — the VECTOR card shown in this diagram; it is one of the labeled elements the architecture uses.
- **QUEUE** — Acme may preserve case notes, show cached public documentation with a freshness warning, queue a retry, or disable commits while identity or policy is unavailable.
- **PROVIDERS** — Place public edge, web, API, workers, protocols, data stores, and external providers on real network boundaries.
- **SERVICE** — The Next.js application can run on Vercel while a Python API and workers run on a suitable service platform.
- **TENANT** — A failure domain is a set of components likely to become unavailable together, such as one process, service, region, account, provider, or tenant partition.
- **PROVIDER** — A failure domain is a set of components likely to become unavailable together, such as one process, service, region, account, provider, or tenant partition.
- **OWNER** — Assign owner, scaling signal, service objective, alert, degraded mode, backup, and recovery target.
- **SLO** — a labeled visual element in this diagram; the prompt shows it as OWNER and SLO cards.
- **CASCADE** — the dangerous, unacceptable, or broken element marked in coral; in this diagram CASCADE blocked by bulkheads.
- **REGION** — The blueprint must not pretend they share memory, filesystem, deployment lifecycle, region, or transaction boundary.
- **BULKHEADS** — Bulkheads, queues, limits, and fallbacks keep one failure from consuming the whole system.

---

## Colour and flow semantics

The course visual grammar uses color to separate platforms, requests, safe paths, danger, and records. In this diagram those colors are assigned as follows:
- **Cobalt platform** — a product, service, environment, or boundary. The main structural cards such as **NEXTJS WEB**, **WORKER POOL**, **ARTIFACT STORE**, **FAILURE DOMAINS REGION**, **FAILURE DOMAINS**, **SERVICE** sit on glowing cobalt platforms.
- **Cyan arrow** — a typed request, event, artifact, deployment, test, or evidence handoff. The cyan paths between **VERCEL EDGE**, **NEXTJS WEB**, **PYTHON API**, **WORKER POOL** carry the forward motion of the architecture.
- **Teal arrow** — an authoritative decision, verified contract, passing gate, safe release, or recovered service. The teal elements **DEGRADED MODE**, **BULKHEADS** show the path the design wants to keep open.
- **Coral path** — an unacceptable outcome, failed boundary, broken contract, unsafe release, or unrecovered effect. The coral elements **CASCADE** show what must be blocked or contained.
- **White card** — a requirement, schema, service, test, gate, owner, artifact, or receipt. The white cards such as **ARTIFACT STORE**, **POLICY**, **OWNER**, **SLO** are the readable records the diagram communicates.

---

## How to present it

- Point to **VERCEL EDGE** and ask the room to state the human problem or outcome before naming any technology, protocol, or model.
- Point to **NEXTJS WEB** and ask what would have to change for the team to place public edge, web, API, workers, protocols, data stores, and external providers on real network boundaries, and who would own that change.
- Point to **FAILURE DOMAINS REGION** and ask what evidence would show the team has already draw authentication, encryption, egress, region, tenant, and data-residency paths, and what test would fail first if it is missing.
- Point to **FAILURE DOMAINS** and ask who else in the room must agree before the team can mark process, service, provider, account, region, and tenant failure domains, and what would change their mind.
- Point to **DEGRADED MODE** and ask what the smallest version of assign owner, scaling signal, service objective, alert, degraded mode, backup, and recovery target looks like, and what would be left out of that version.
- Point to **WORKER POOL** and ask what would have to change for the team to walk through dependency loss and verify that sensitive actions fail safely without losing preserved work, and who would own that change.
- Trace the **teal** path (DEGRADED MODE) and ask what evidence would prove the real system follows it, who collects that evidence, and how often it is refreshed.
- Show the **coral** path (CASCADE blocked by bulkheads) and ask what control, owner, or test would catch it before a user is harmed, and what the safe state would be if it is triggered.
- Point to **FAILURE DOMAINS REGION** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Point to **FAILURE DOMAINS** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Point to **POLICY** and ask who owns it, what evidence it needs, what happens when that evidence is missing, and which test proves the gate cannot be bypassed.
- Use the analogy: A ship has watertight compartments. The map shows not only which rooms exist but which doors can seal, who controls them, how alarms travel, and how the ship remains afloat when one compartment floods. Ask how the same failure would appear in the team's current code or process.
- Return to the whole diagram and ask the room to name one thing they will stop, one thing they will start, and one thing they will own differently before the next build.
- Run the lab: Create the Acme deployment topology for Vercel plus a Python platform. Include networks, regions, environments, stores, providers, identity, egress, secrets, owners, scaling signals, service objectives, failure domains, degraded modes, backup, restore, and six outage walkthroughs.

---

## Lab and checkpoint

**Lab:** Create the Acme deployment topology for Vercel plus a Python platform. Include networks, regions, environments, stores, providers, identity, egress, secrets, owners, scaling signals, service objectives, failure domains, degraded modes, backup, restore, and six outage walkthroughs.

**Checkpoint:** Can two services deployed together be assumed to share durable local files?

**Answer:** No. Treat service filesystems and process memory as ephemeral unless the chosen platform explicitly guarantees otherwise; use an owned durable store.

---

## Glossary

- **Failure domain** — components likely to fail together
- **Bulkhead** — limit that contains failure within one area
- **Degraded mode** — reduced but honest and safe service state

---

## Sources

- Next.js deploying
- Vercel Functions
- FastAPI deployment concepts
- FastAPI containers

---

## Related lessons

- **Lesson 227** — MCP, A2A, AG-UI, HTTP, queue, and internal boundaries (`protocol-boundary-routing-map`)
- **Lesson 234** — Database, vector index, queue, cache, and artifact storage (`polyglot-storage-decision-map`)
- **Lesson 236** — CI/CD, environments, migrations, flags, rollback, and recovery (`safe-delivery-recovery-pipeline`)