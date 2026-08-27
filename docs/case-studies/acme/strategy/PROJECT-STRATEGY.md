# Python Project Strategy for the 244-Diagram Visual Agent Course

## Executive recommendation

Do **not** build one project per diagram. That would create 244 tiny demonstrations with repeated setup, shallow implementations, and no convincing production story.

Also, do **not** begin with one enormous application that tries to implement all ten courses at once. That creates a monolith which takes months before anything useful can be demonstrated.

The strongest approach is a **portfolio suite**:

1. Use one consistent real-world case study across the entire series.
2. Build four independently runnable Python projects around that case study.
3. Combine those four projects into one production-style capstone.
4. Treat every diagram as a requirement, test, failure experiment, architectural decision, or presentation aid within those projects.

The recommended case study is an **AI-assisted customer case-resolution platform**. A customer submits a complicated case—for example an insurance claim, loan-document query, billing dispute, or support escalation. The system retrieves evidence, calls operational tools, delegates specialist work, pauses for human approval, and produces an auditable resolution.

For the examples below, I will call it **Acme Case Resolution Platform**. The name can change later without changing the architecture.

---

## Why one project per image is the wrong model

A diagram normally explains one idea, not one complete application. For example:

- Stateless MCP requests are one transport behavior.
- Idempotency is one safety property.
- Hybrid retrieval is one RAG stage.
- A2A task states are one collaboration contract.
- Human approval is one workflow checkpoint.
- Trace correlation is one observability requirement.

If each becomes a separate repository, every repository needs its own installation instructions, configuration, fake data, API, tests, logging, and explanation. Most of the work will be repeated plumbing. A reviewer will see many toy programs but little evidence that the pieces can work together.

It also produces an awkward demonstration. You would have to say:

> “Here is my idempotency demo. Now open another repository for my queue demo. Now open another repository for my approval demo.”

That is much weaker than saying:

> “Here is one customer case. Watch it move through retrieval, policy, delegation, approval, execution, recovery, and audit. Now I will deliberately break one stage and show the system recover.”

The second version demonstrates engineering judgment, not just isolated code.

---

## Why one giant project is also risky

A single application spanning all 244 diagrams sounds coherent, but it creates three problems.

First, there is no early finish line. You can work for weeks on infrastructure before producing a useful demonstration.

Second, unrelated lessons become tightly coupled. A change to the RAG index should not make it difficult to demonstrate MCP discovery. A UI experiment should not require rebuilding the durable workflow engine.

Third, a reviewer may not know where to look. A huge repository can conceal good work because the boundaries are unclear.

The answer is therefore one **shared case study**, implemented as several **small but real systems** with explicit contracts between them.

---

## The recommended portfolio suite

### Project 1 — MCP Operations Gateway

This is the controlled capability layer. It exposes business operations as MCP tools and business information as MCP resources.

Example capabilities:

- `get_case`
- `list_case_documents`
- `calculate_refund`
- `draft_resolution`
- `issue_credit`
- `request_human_approval`
- `get_policy_resource`
- `get_audit_receipt`

The project should demonstrate:

- tool, resource, and prompt discovery;
- JSON Schema input validation;
- stateless HTTP handling;
- authentication and authorization;
- least-privilege tool access;
- idempotency keys for side effects;
- task handles for long-running operations;
- structured results and receipts;
- protocol-version and capability negotiation;
- conformance tests and error correlation.

This project mainly turns the MCP diagrams from Volumes 1–4 into executable behavior.

**Best live demonstration:** call `issue_credit` twice with the same idempotency key. Show that only one credit is issued and that both calls resolve to the same business receipt.

### Project 2 — Evidence RAG Workbench

This is the governed knowledge system. It ingests policies, case documents, tables, scanned forms, notes, and structured records, then produces evidence packs rather than unsupported answers.

The project should demonstrate:

- source ownership and authority;
- layout-aware parsing;
- OCR and multimodal evidence intake;
- provenance and retention metadata;
- semantic chunking;
- parent-child retrieval;
- lexical, vector, and structured retrieval;
- authorization before search;
- reranking and diversity;
- bounded multi-hop retrieval;
- immutable versions and as-of-time retrieval;
- claim-level citation lineage;
- conflict detection, uncertainty, and abstention;
- retrieval and answer-quality evaluation.

This project is the executable expression of Volume 5 and the RAG sections of Volumes 1–3.

**Best live demonstration:** ask a question whose answer changed between two policy versions. Show the current answer, then run the same query “as of” an earlier date and display the older evidence and citation chain.

### Project 3 — A2A Specialist Network

This is the multi-agent collaboration layer. A coordinator delegates bounded work to independently owned specialist agents.

Suggested specialist agents:

- **Triage Agent** — classifies the case and identifies missing information.
- **Policy Agent** — constructs a cited evidence pack.
- **Finance Agent** — calculates refunds or adjustments.
- **Risk Agent** — checks policy and risk constraints.
- **Reviewer Agent** — challenges unsupported claims and identifies disagreement.

The project should demonstrate:

- agent-card discovery;
- trust and allowlisting;
- message, task, artifact, and task-state separation;
- streaming, polling, and push delivery;
- cancellation;
- bounded delegation;
- ownership handoff;
- artifact aggregation;
- disagreement handling;
- final-authority rules;
- protocol adapters and correlation IDs.

Use the official A2A Python SDK behind a thin adapter owned by your code. The SDK is evolving, so protocol-specific types should not leak through the entire business layer. Pin the exact version used by the project and test the adapter contract. The official SDK is published as `a2a-sdk` and maintained in the [A2A Python repository](https://github.com/a2aproject/a2a-python).

**Best live demonstration:** let the Policy Agent and Risk Agent disagree. Show that the coordinator does not average their answers or allow the loudest agent to win; it routes the conflict to the named final authority.

### Project 4 — Durable Workflow and Reliability Lab

This is the execution and evaluation environment. It owns long-running case state and gives you a controlled place to demonstrate failures.

The project should demonstrate:

- separate conversation, run, task, and workflow state;
- explicit state machines;
- snapshots, replay, and schema evolution;
- queues, leases, acknowledgement, and visibility timeouts;
- backpressure and priority;
- retries, idempotency, and poison work;
- deadlines, cancellation, and compensation;
- fan-out/fan-in and join policies;
- schedules and external resume events;
- human interruption and approval;
- steering, replanning, and invalidation;
- race conditions and stale-state protection;
- traces, metrics, logs, receipts, and cost ledgers;
- golden datasets, graders, quality slices, and regression gates;
- chaos tests and recovery runbooks.

This project covers Volumes 3, 6, 7, and 8 particularly well.

You can implement the first version with explicit Python state-machine code and PostgreSQL. Once the behavior is understood, add a durable orchestration framework if it improves the demonstration. LangGraph, for example, officially focuses on durable execution, streaming, persistence, and human-in-the-loop workflows. Keep the business state model independent of the framework so the project demonstrates your architecture rather than only your knowledge of a library.

**Best live demonstration:** terminate the worker midway through a case, restart it, and show that it resumes from the last durable checkpoint without repeating an already committed payment.

### Project 5 — Acme Case Resolution Platform

This is the integration capstone, not a fifth implementation from scratch. It composes Projects 1–4 behind a simple interface.

A complete case journey is:

1. A person submits a case and supporting documents.
2. The RAG Workbench builds an authorized evidence pack.
3. The coordinator creates A2A tasks for relevant specialists.
4. Specialists return artifacts, not informal chat snippets.
5. The workflow engine aggregates their work and records disagreement.
6. The MCP Gateway exposes any approved operational action.
7. A human approves or rejects high-impact changes.
8. The domain service commits the change using an idempotency key.
9. The system returns a receipt and preserves the complete trace.

The capstone should have a thin web interface, but the substantial engineering should remain in Python. A practical split is:

- Python/FastAPI for APIs and domain services;
- Pydantic models for boundary validation;
- PostgreSQL for durable business and workflow state;
- a vector index appropriate to the chosen scale;
- Redis or a real message broker only when the queue demonstration requires it;
- OpenTelemetry-compatible traces and metrics;
- pytest for unit, contract, integration, conformance, and failure tests;
- a small React/Next.js interface or a lightweight Python UI for demonstrations.

The official MCP Python SDK supports clients, servers, tools, resources, prompts, structured output, authentication, and Streamable HTTP. Use the stable supported line, pin it, and isolate it behind your own adapter because SDK majors and experimental features can change. See the [official MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).

---

## How the ten volumes should map to the projects

| Course | Main engineering outcome | Primary project |
|---|---|---|
| Volume 1 | Understand the complete agent system and its boundaries | Capstone skeleton |
| Volume 2 | Build the HTTP, JSON, validation, identity, and storage foundation | Shared Python platform |
| Volume 3 | Add production MCP, durable state, memory, security, evaluation, and agent UI events | MCP Gateway + Reliability Lab |
| Volume 4 | Implement protocol negotiation, correlation, conformance, A2A, and adapters | MCP Gateway + A2A Network |
| Volume 5 | Build governed ingestion, retrieval, freshness, citations, and evaluation | Evidence RAG Workbench |
| Volume 6 | Build durable orchestration, queues, compensation, delegation, and recovery | Reliability Lab + A2A Network |
| Volume 7 | Add identity, policy, tenant isolation, sandboxing, privacy, and audit | Shared security layer across all projects |
| Volume 8 | Add traces, evaluations, cost controls, rollout gates, and incident learning | Reliability Lab |
| Volume 9 | Build the event-driven user experience, recovery UI, consent, and accessibility | Capstone interface |
| Volume 10 | Integrate, deploy, test, operate, defend, and present the architecture | Final capstone |

The courses therefore become an engineering sequence. They do not need ten unrelated capstones.

---

## What each of the 244 diagrams becomes

Every diagram should be assigned one of five implementation roles.

### 1. Executable feature

The diagram becomes working behavior in the system.

Examples:

- MCP discovery lists real tools.
- A2A task lifecycle changes real persisted task states.
- Hybrid search merges real lexical and vector candidates.
- Human approval actually pauses and resumes a workflow.

### 2. Automated test

The diagram becomes a correctness property.

Examples:

- A repeated idempotency key cannot create a second side effect.
- An unauthorized tenant's documents never enter candidate generation.
- A stale workflow version cannot overwrite current state.
- Every result is correlated with the correct request.

### 3. Failure-injection scenario

The diagram becomes a demonstration of what happens when something breaks.

Examples:

- Kill a worker after a side effect but before acknowledgement.
- Delay one branch of a fan-out beyond the join deadline.
- replay a duplicate A2A event;
- expire a human approval;
- make the vector index unavailable;
- inject an untrusted instruction into a retrieved document.

### 4. Architectural decision record

Some diagrams explain a choice rather than runtime behavior.

Examples:

- Orchestration versus choreography.
- Local function versus MCP versus A2A.
- Relational database versus task store versus vector index.
- Current A2A vocabulary versus historical ACP vocabulary.

These should become short ADRs containing the decision, alternatives, trade-offs, and evidence.

### 5. Presentation scene

Some diagrams are best used to explain a completed feature during a demonstration. Embed the diagram directly beside the live scenario, then show the relevant trace, state, artifact, or test result underneath it.

This gives every image a practical purpose without pretending every image deserves a separate application.

---

## The demonstration-unit pattern

Create one small “scenario” for each important diagram or closely related group of diagrams. A scenario is much smaller than a project.

Each scenario should contain:

```text
scenario.yaml
README.md
seed.py
run.py
expected.json
tests/
```

`scenario.yaml` records:

- the diagrams demonstrated;
- the services required;
- the starting state;
- the action to perform;
- the expected state transition;
- the evidence that proves success;
- the optional fault to inject.

For example, the idempotency scenario could say:

```yaml
name: duplicate-credit-request
diagrams: [2, 54, 131]
start:
  case_id: CASE-1042
  credit_status: not_issued
action:
  calls: 2
  idempotency_key: CASE-1042-CREDIT-1
expect:
  credits_created: 1
  receipts_returned: 2
  receipt_business_id_count: 1
fault:
  disconnect_after_commit: true
```

This one scenario demonstrates three diagrams across three volumes and produces measurable evidence.

---

## Recommended repository shape

Start with one monorepo so that shared contracts, fixtures, and local startup remain manageable:

```text
acme-agent-platform/
├── apps/
│   ├── case_api/                 # FastAPI business API
│   ├── demo_ui/                  # Small demonstration interface
│   └── scenario_runner/          # Runs diagram scenarios
├── services/
│   ├── mcp_gateway/
│   ├── rag_workbench/
│   ├── coordinator_agent/
│   ├── policy_agent/
│   ├── finance_agent/
│   ├── risk_agent/
│   └── workflow_worker/
├── packages/
│   ├── contracts/                # Pydantic message and artifact models
│   ├── domain/                   # Business rules with no protocol dependency
│   ├── authz/                    # Identity and policy decisions
│   ├── audit/                    # Receipts and provenance
│   ├── telemetry/                # Trace and metric helpers
│   └── testkit/                  # Fakes, fixtures, chaos controls
├── scenarios/
│   ├── mcp/
│   ├── rag/
│   ├── a2a/
│   ├── workflow/
│   ├── security/
│   └── reliability/
├── tests/
│   ├── unit/
│   ├── contract/
│   ├── integration/
│   ├── conformance/
│   ├── evaluation/
│   └── chaos/
├── docs/
│   ├── architecture/
│   ├── decisions/
│   ├── demonstrations/
│   └── diagram-map.md
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

Each service must be runnable independently. The monorepo is for convenience, not permission to blur ownership.

If one component later becomes impressive enough to deserve its own public repository, extract it then. Do not pay that coordination cost on day one.

---

## Build order

### Phase 1 — One thin vertical slice

Build one complete but simple path:

```text
Question → Retrieve policy → Draft answer → Human approves → Record receipt
```

Use one policy document, one MCP tool, one agent, one database table, and one trace. No multi-agent network yet.

This proves that the repository starts, the boundaries communicate, and the user receives a result.

### Phase 2 — Make the MCP boundary real

Move business capabilities behind the MCP Gateway. Add discovery, validation, authentication, authorization, structured results, idempotency, and receipts.

At the end of this phase, Project 1 is independently demonstrable.

### Phase 3 — Build the evidence pipeline

Add governed ingestion, chunking, hybrid retrieval, reranking, citations, versioning, authorization-before-search, and evaluation.

At the end of this phase, Project 2 is independently demonstrable.

### Phase 4 — Add specialist delegation

Introduce two specialist agents first, not five. Give them agent cards, bounded task contracts, task states, artifacts, cancellation, and explicit final authority.

At the end of this phase, Project 3 is independently demonstrable.

### Phase 5 — Make it durable

Persist workflow state, add checkpoints, queues, retries, deadlines, compensation, approval interrupts, replay protection, and recovery tests.

At the end of this phase, Project 4 is independently demonstrable.

### Phase 6 — Add production controls

Add tenant isolation, least privilege, prompt-injection defenses, secrets, audit chains, traces, golden datasets, cost budgets, canary releases, chaos tests, and runbooks.

### Phase 7 — Build the capstone experience

Add the web interface, scenario selector, trace view, evidence viewer, task timeline, approval controls, artifact cards, and recovery actions.

The interface should make the invisible architecture visible. A reviewer should be able to see:

- which agent owns the current task;
- which evidence supports each claim;
- which tool was proposed;
- which policy allowed or denied it;
- whether a human decision is required;
- what was committed;
- which receipt proves it;
- how long and how much the run cost;
- what happened after an injected failure.

---

## How many demonstrations should you actually build?

Do not attempt 244 equally detailed demonstrations.

Use three levels:

### Level A — Portfolio demonstrations: about 12

These are polished, narrated, end-to-end scenarios that a recruiter or engineer can run.

Recommended set:

1. MCP discovery and structured tool call.
2. Safe side effect with retry and idempotency.
3. Long-running task with progress and recovery.
4. Authorized hybrid RAG with claim-level citations.
5. As-of-time retrieval across policy versions.
6. Conflict detection and abstention.
7. A2A delegation with task and artifact lifecycle.
8. Multi-agent disagreement with final authority.
9. Human approval interrupt and resume.
10. Worker crash, replay, and exactly-once business effect.
11. Prompt-injection/exfiltration attempt blocked by policy.
12. Full case resolution with trace, evaluation, cost, and audit receipt.

### Level B — Engineering scenarios: roughly 35–50

These are runnable tests or fault-injection cases. They may have a short README and command-line output rather than a polished UI.

### Level C — Coverage mappings: all remaining diagrams

These become tests, ADRs, assertions, or documentation references. They still map to code, but they do not need a separate live performance.

This gives you complete conceptual coverage without producing hundreds of shallow programs.

---

## What makes the projects convincing

A good portfolio project is not proved by screenshots or a large dependency list. It is proved by observable behavior.

For every major feature, capture:

- the input contract;
- the resulting state transition;
- the trace or correlation ID;
- the retrieved evidence and citation lineage;
- the policy decision;
- the produced artifact;
- the business receipt;
- the test that prevents regression;
- the behavior under one realistic failure.

Avoid claims such as “production-ready,” “exactly once,” “secure,” or “99% accurate” unless a test or measurement shown in the repository supports the claim.

The strongest README sentence is not:

> “This project uses MCP, A2A, RAG, LangGraph, FastAPI, and PostgreSQL.”

It is:

> “This case was interrupted after the refund committed but before the worker acknowledged it. On recovery, the workflow resumed, the idempotency key prevented a duplicate refund, and the original receipt was returned.”

That sentence describes engineering evidence.

---

## Final answer

Use **one long case-study domain**, but do not use one inseparable application.

Build:

1. an MCP Operations Gateway;
2. an Evidence RAG Workbench;
3. an A2A Specialist Network;
4. a Durable Workflow and Reliability Lab;
5. an integration capstone that composes all four.

Organize them initially in one Python monorepo. Turn the 244 diagrams into a mixture of executable features, automated tests, failure scenarios, architectural decisions, and presentation scenes. Polish approximately twelve demonstrations; make another 35–50 runnable engineering scenarios; map the remainder to code and tests without forcing each one to become a toy project.

This structure gives you both things a strong portfolio needs:

- **depth**, because one realistic case travels through the complete system; and
- **range**, because each subsystem can be started, tested, explained, and demonstrated independently.

