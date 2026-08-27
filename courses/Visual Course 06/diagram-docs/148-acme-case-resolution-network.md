# Diagram 148 — Capstone: The Acme Case Resolution Network

![On dark navy, seven horizontal lanes run left to right, numbered 1 to 7, with the title ACME CASE RESOLUTION NETWORK at the top. Lane 1 INTAKE AND IDENTITY: CUSTOMER, SUBMIT REFUND REQUEST, MAYA, CASE CREATED (CASE-88421), START WORKFLOW (REFUND_FLOW), with cyan COMMAND arrows. Lane 2 WORKFLOW AND EVENT HISTORY: RECEIVED, VALIDATE REQUEST, CHECK ELIGIBILITY, PROCESS REFUND, PAYMENT TIMEOUT with a FAILURE arrow to RETRY PAYMENT, then REFUND COMPLETED, with teal EVENT arrows and teal ACKNOWLEDGEMENT dashed lines. Lane 3 QUEUES AND WORKERS: VALIDATION QUEUE, VALIDATION WORKERS, ELIGIBILITY QUEUE, ELIGIBILITY WORKERS, PAYMENT QUEUE, PAYMENT WORKERS, RETRY QUEUE, PAYMENT WORKERS. Lane 4 SPECIALIST AGENTS VIA A2A 1.0: IDENTITY AGENT, POLICY AGENT, RISK AGENT, PAYMENTS AGENT, NOTIFICATIONS AGENT, LEDGER AGENT, connected by bidirectional A2A 1.0 arrows. Lane 5 HUMAN CONTROL: HUMAN REVIEW (ELIGIBILITY) and HUMAN REVIEW (PAYMENT RETRY), each with a teal APPROVE arrow. Lane 6 SIDE EFFECTS AND RECEIPTS: CASE RECEIPT, ELIGIBILITY RECEIPT, RISK ASSESSMENT RECEIPT, PAYMENT INITIATED RECEIPT, PAYMENT RETRY RECEIPT, REFUND COMPLETED RECEIPT. Lane 7 OBSERVABILITY AND RECOVERY: EVENT LOG, DISTRIBUTED TRACING, METRICS, ALERTS, CHECKPOINTS, RESUME POINTS, REPLAY EVENTS, RECOVERY ACTIONS. A legend at the bottom shows cyan for COMMAND, forward arrow for FORWARD WORK, dashed arrow for EVENT, dashed arrow for ACKNOWLEDGEMENT, receipt icon for RECEIPT, checkpoint icon for CHECKPOINT, dashed arrow for RESUME, and red arrow for FAILURE.](../diagrams/148-acme-case-resolution-network.png)

**Module:** Capstone
**Role in the course:** the complete architecture that combines every pattern into one framework-neutral case resolution network
**Layout:** seven horizontal lanes, each representing a layer, with Maya's refund journey flowing left to right

---

## At a glance

**Seven lanes:**
1. **INTAKE AND IDENTITY**
2. **WORKFLOW AND EVENT HISTORY**
3. **QUEUES AND WORKERS**
4. **SPECIALIST AGENTS VIA A2A 1.0**
5. **HUMAN CONTROL**
6. **SIDE EFFECTS AND RECEIPTS**
7. **OBSERVABILITY AND RECOVERY**

Maya submits a refund request. A case is created. A workflow starts. It fans out evidence and specialist tasks. It waits for human approval. It issues a payment. The payment times out, recovers, and completes once. Every step leaves a receipt, a checkpoint, and a trace.

This is the whole course in one diagram.

---

## What the diagram teaches

### 1. The case is the durable owner

The customer case, **CASE-88421**, is created in lane 1 and never loses ownership. Everything else — queues, agents, approvals, payments — contributes to it.

The case is the durable owner of the customer outcome. It holds the identity, the state, the budget, the deadline, the evidence plan, and the event history.

This is the same idea from the state layer, command/event/state machine, snapshot/replay, and ownership diagrams. The case is the unit of business truth.

### 2. Intake is authenticated intent

Lane 1 starts with **CUSTOMER → SUBMIT REFUND REQUEST → MAYA → CASE CREATED → START WORKFLOW**. Each step is a **COMMAND**.

The customer is authenticated. The request is a command. The case is created. The workflow starts. The command carries the identity of the requester.

Without authenticated intake, the rest of the network has no trusted owner. Every later step depends on this first command being attributable.

### 3. Workflow and event history is the durable record

Lane 2 is the event-sourced workflow: **RECEIVED → VALIDATE REQUEST → CHECK ELIGIBILITY → PROCESS REFUND → PAYMENT TIMEOUT → RETRY PAYMENT → REFUND COMPLETED**.

The workflow is not a hidden controller. It is a durable record of what happened, what is happening, and what may legally happen next.

Each step is an **EVENT**. Dashed **ACKNOWLEDGEMENT** lines show that every event is acknowledged. **RESUME** arrows show that the workflow can continue after a timeout.

This is the same durable vocabulary from the snapshot/replay, schedule/event/resume, and steering/replan diagrams.

### 4. Queues decouple and protect slow work

Lane 3 shows **QUEUES AND WORKERS**: validation, eligibility, payment, retry. Each queue has its own workers.

Queues protect the workflow from slow operations. A payment can take seconds or minutes. The workflow does not hold a worker open. It puts the work on a queue and waits.

The queue and worker diagram from earlier explained lease, visibility, acknowledgement, and backpressure. Here the queues are part of the larger network.

### 5. Specialist agents are delegated through A2A 1.0

Lane 4 is **SPECIALIST AGENTS VIA A2A 1.0**: identity, policy, risk, payments, notifications, ledger.

Each specialist is an A2A agent with its own task identity. The case workflow delegates bounded tasks. The agents return artifacts. The workflow does not lose ownership of the case.

The A2A diagrams explained Agent Cards, task creation, ownership, and handoff. Here all of those are in parallel.

### 6. Human control is a precise approval

Lane 5 shows two **HUMAN REVIEW** points: one at eligibility, one at payment retry. Each has an **APPROVE** arrow.

The human is not just "in the loop." The human is asked a precise question with exact action, evidence, risk, amount, expiry, and approver. The approval is a durable event.

The human-in-the-loop diagram explained the approval contract and stale-approval revalidation. Here the capstone uses it twice.

### 7. Side effects and receipts prove what happened

Lane 6 is **SIDE EFFECTS AND RECEIPTS**: case receipt, eligibility result, risk assessment, payment initiated, payment retry, refund completed.

Every side effect has a receipt. The receipt is the durable evidence that the effect happened. The business record is built from these receipts.

The artifact/receipt/business record diagram is the foundation. This lane is its expression across the whole case.

### 8. Observability and recovery are the last lane, not an afterthought

Lane 7 is **OBSERVABILITY AND RECOVERY**: event log, distributed tracing, metrics, alerts, checkpoints, resume points, replay events, recovery actions.

These are not optional. They are the safety net. The event log makes the workflow auditable. Distributed tracing shows the path. Metrics and alerts detect problems. Checkpoints and resume points make recovery possible. Replay events and recovery actions are the runbook.

The recovery and chaos-test diagrams are the practice. This lane is where they live in the architecture.

### 9. Every component is replaceable if its contract remains true

The network is framework-neutral. The workflow engine, the queue, the A2A agents, the payment provider, and the observability tools can all be replaced. The only requirement is that each component honours its contract.

The contract is: commands, events, states, side effects, receipts, and identities must be durable, attributable, and inspectable. If a new component can do that, it can join the network.

### 10. The payment timeout and retry tell the whole story

The red **FAILURE** arrow from **PAYMENT TIMEOUT** to **RETRY PAYMENT**, then the green event to **REFUND COMPLETED**, is the diagram's story.

The payment provider times out. The workflow does not panic. It records the timeout, resumes, retries with the same idempotency key, and reconciles the provider receipt. The refund completes once.

This single path uses: durable workflow, queues, A2A, idempotency, receipts, checkpoints, resume, and recovery. It is the course in one line.

### 11. The capstone proof set is the graduation evidence

The diagram is not only a network map. It is the starting point for the capstone proof set: state machine, event catalog, queue topology, idempotency register, saga map, A2A handoff contracts, approval contract, budget ledger, chaos matrix, and recovery runbook.

This proof set is the graduation evidence that the design is more than a polished demo. Each artifact maps to a lane: the state machine and event catalog to lane 2, the queue topology and idempotency register to lane 3, the A2A handoffs to lane 4, the approval and budget contracts to lane 5, and the chaos matrix and recovery runbook to lane 7.

If the team can explain the proof set, it can port the network to Next.js or Python without changing the business meaning.

### 12. The contract is portable across Next.js and Python

The same case resolution network can be built with Next.js App Router server boundaries or with FastAPI, typed domain transitions, and queue workers. Both builds should share the same JSON fixtures, acceptance scenarios, and contract tests.

The browser view stays read-only against workflow truth. Mutations return stable IDs or receipts. The Python side models commands, events, states, and errors as typed records so tests replay the same fixture without network calls. The framework is interchangeable; the durable record is not.

---

## Case study — Maya's refund

Maya wants a refund. The network processes it from intake to completion.

### The journey

1. **Intake and identity.** Maya logs in and submits a refund request. The system creates **CASE-88421** and starts **REFUND_FLOW**.

2. **Workflow and event history.** The workflow receives the request, validates it, checks eligibility, and processes the refund. It records each event.

3. **Queues and workers.** Validation and eligibility checks are placed on queues with workers. The payment is placed on the payment queue.

4. **Specialist agents via A2A 1.0.** The case delegates identity, policy, risk, payment, notification, and ledger tasks to specialist agents. Each returns an artifact.

5. **Human control.** A supervisor approves the eligibility decision and later approves the payment retry after a timeout.

6. **Side effects and receipts.** The case is created, eligibility is confirmed, the payment is initiated, the retry is recorded, and the refund is completed. Each has a receipt.

7. **Observability and recovery.** Event logs, traces, metrics, and alerts record the journey. Checkpoints and resume points allow the workflow to continue after the payment timeout. The recovery runbook is ready if needed.

### The timeout

The payment provider receives the refund request but responds slowly. The worker times out before it can record the provider receipt.

The workflow records **PAYMENT TIMEOUT** as an event. It does not mark the refund as failed. It moves to **RETRY PAYMENT**.

Before retrying, the workflow reconciles with the provider using the same operation key. The provider says the refund was already accepted and returns the receipt.

The workflow records the receipt, marks **REFUND COMPLETED**, and notifies Maya once.

### Why it works

- The case is the durable owner.
- The workflow is event-sourced and resumable.
- Queues decouple slow work.
- A2A agents are delegated, not trusted with ownership.
- Human approvals are precise and stale-aware.
- Side effects are idempotent and receipted.
- Observability and recovery are built in.

### The line in the capstone standard

*The workflow owns progress; agents contribute bounded work; receipts prove effects; recovery is part of the product.*

---

## Composition

Seven horizontal lanes, each a layer of the architecture.

**Lane 1 — INTAKE AND IDENTITY:**
- **CUSTOMER** → **SUBMIT REFUND REQUEST** → **MAYA** → **CASE CREATED (CASE-88421)** → **START WORKFLOW (REFUND_FLOW)**.

**Lane 2 — WORKFLOW AND EVENT HISTORY:**
- **RECEIVED** → **VALIDATE REQUEST** → **CHECK ELIGIBILITY** → **PROCESS REFUND** → **PAYMENT TIMEOUT**.
- Red **FAILURE** arrow to **RETRY PAYMENT**.
- **RETRY PAYMENT** → **REFUND COMPLETED**.
- Teal **ACKNOWLEDGEMENT** and **RESUME** dashed lines.

**Lane 3 — QUEUES AND WORKERS:**
- **VALIDATION QUEUE → VALIDATION WORKERS**
- **ELIGIBILITY QUEUE → ELIGIBILITY WORKERS**
- **PAYMENT QUEUE → PAYMENT WORKERS**
- **RETRY QUEUE → PAYMENT WORKERS**

**Lane 4 — SPECIALIST AGENTS VIA A2A 1.0:**
- **IDENTITY AGENT**
- **POLICY AGENT**
- **RISK AGENT**
- **PAYMENTS AGENT**
- **NOTIFICATIONS AGENT**
- **LEDGER AGENT**
- Bidirectional **A2A 1.0** arrows between them.

**Lane 5 — HUMAN CONTROL:**
- **HUMAN REVIEW (ELIGIBILITY)** with **APPROVE**.
- **HUMAN REVIEW (PAYMENT RETRY)** with **APPROVE**.

**Lane 6 — SIDE EFFECTS AND RECEIPTS:**
- **CASE RECEIPT**
- **ELIGIBILITY RESULT**
- **RISK ASSESSMENT RECEIPT**
- **PAYMENT INITIATED RECEIPT**
- **PAYMENT RETRY RECEIPT**
- **REFUND COMPLETED RECEIPT**

**Lane 7 — OBSERVABILITY AND RECOVERY:**
- **EVENT LOG**
- **DISTRIBUTED TRACING**
- **METRICS**
- **ALERTS**
- **CHECKPOINTS**
- **RESUME POINTS**
- **REPLAY EVENTS**
- **RECOVERY ACTIONS**

**Bottom legend:** cyan for COMMAND, arrow for FORWARD WORK, dashed for EVENT, dashed for ACKNOWLEDGEMENT, receipt icon for RECEIPT, checkpoint icon for CHECKPOINT, dashed for RESUME, red for FAILURE.

## Element by element

**Customer / Maya** — the authenticated actor.
**Case** — the durable owner.
**Workflow** — the event-sourced process.

**Commands** — the forward actions.
**Events** — the durable history.
**Acknowledgements** — the durable handshakes.
**Resume** — continuation after failure.

**Queues / Workers** — decoupled slow work.

**A2A 1.0 agents** — delegated specialist tasks.

**Human review / Approve** — precise approvals.

**Receipts** — durable effect evidence.

**Observability / Recovery** — safety net and runbook.

## Colour and flow semantics

- **Cyan arrows** are commands, the forward work of the case.
- **Teal arrows** are events and acknowledgements, the durable history.
- **Red arrow** is failure, the payment timeout.
- **Dashed arrows** are acknowledgements and resume, the durable recovery paths.
- **Receipt icons** in lane 6 mark every side effect.
- **Seven lanes** show that the architecture is layered but connected by a single journey.
- The **payment timeout → retry → complete** path is the central story.

## How to present it

**Start at the title.** The Acme Case Resolution Network. This is the whole course in one architecture. Ask the room which lane they have implemented and which is missing.

**Trace lane by lane.** Intake, workflow, queues, agents, human control, receipts, observability. Show that each lane is a pattern from earlier in the course.

**Point at the case.** CASE-88421. The case is the durable owner. Everything else contributes to it.

**Trace the payment timeout.** The red failure arrow. It is the most important path. Ask how the room would handle a payment timeout today. Would it retry blindly? Reconcile first? Lose the receipt?

**Show that the retry queue is the same work.** The payment worker retries with the same operation key. The workflow resumes from the checkpoint. The provider idempotency prevents duplicates.

**Point at lane 7.** Observability and recovery are not afterthoughts. They are part of the architecture. Ask where their metrics, alerts, checkpoints, and runbooks live.

**Emphasize framework neutrality.** Each component can be replaced if it honours the contract. The workflow engine, the queue, the A2A agents, and the payment provider are all interchangeable.

**Tell Maya's story.** A refund that survives a timeout and completes once. That is the goal of the whole network.

**Close on the capstone standard.** *The workflow owns progress; agents contribute bounded work; receipts prove effects; recovery is part of the product.*

**Ask the room to name the capstone's most important component.** Wait for "LLM," "queue," or "agent." Then answer: the durable business contract. Without ownership, invariants, side effects, evidence, and recovery, the rest is decoration.

**Map the proof set to the lanes.** The state machine is lane 2, the queue topology is lane 3, A2A handoffs are lane 4, the approval and budget contracts are lane 5, and the chaos matrix and recovery runbook are lane 7.

**Contrast Next.js and Python as two implementations of one contract.** Ask which contract tests already travel between frontend and backend. Both stacks should pass the same JSON fixtures and acceptance scenarios.

**Probe the missing durable contract.** Ask what would fail first if the durable record did not exist: duplicate payment, lost receipt, unrecoverable timeout, or approval without context.

**Timing.** Thirty minutes. Forty if the room maps their own architecture against the seven lanes.

---

## Lab and checkpoint

**Lab:** Map your own architecture against the seven lanes of the case resolution network: authenticated intake, durable workflow, queues, specialist agents, human control, side effects/receipts, and observability/recovery. Identify which lane is missing, where a payment timeout would be lost, and how the case remains the durable owner.

**Checkpoint:** What is the most important component of the network?

**Answer:** The durable business contract. Without ownership, invariants, side effects, evidence, and recovery, the components are not enough. The case must own the outcome; the workflow must own progress; agents must do bounded work; receipts must prove effects; and recovery must be part of the product.

## Glossary

- **A2A** — the protocol for delegating work to specialist agents.
- **Case** — the durable owner of the customer outcome.
- **Checkpoint** — the saved state that lets a workflow resume after a failure.
- **Human control** — precise approval and steering, not a generic pause.
- **Intake** — the authenticated receipt of customer intent.
- **Observable** — the lane that makes the system diagnosable and recoverable.
- **Payment timeout** — the failure path that tests the whole network.
- **Queue** — the decoupling and protection mechanism for slow work.
- **Receipt** — the proof that a side effect occurred.
- **Recovery** — the runbook and process that returns the system to a correct state.
- **Retry** — the continuation of the same work with the same operation key.
- **Side effect** — an external change that must be proved by a receipt.
- **Workflow** — the durable progress of the case through its stages.

## Sources

- Capstone case-resolution network
- Durable workflow, queue, and A2A orchestration
- Chaos testing, recovery runbooks, and observability

## The patterns beneath the network

![On dark navy, a four-band state layer map. Cyan PROPOSAL has REQUEST and PLAN. Green DECISION has APPROVAL and POLICY. Red EFFECT has SIDE EFFECT and COMPENSATION. Teal RECORD has ARTIFACT and BUSINESS RECORD. Teal lines show ARTIFACT flowing into BUSINESS RECORD. A red IRREVERSIBLE arrow from SIDE EFFECT is blocked. A legend shows cyan for proposal, green for decision, red for effect, and teal for record.](../diagrams/125-state-layer-map.png)

That earlier diagram is the conceptual spine. The capstone network is its implementation. The case is the business record. Commands, events, and approvals are the decision layers. The payment is the side effect. The receipts in lane 6 are the artifacts. The recovery in lane 7 is the compensation path. Every lane in the capstone maps to one of the four bands.
