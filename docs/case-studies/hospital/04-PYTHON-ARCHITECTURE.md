# HarborCare — Python Reference Architecture

## Permission checks at every boundary, one authoritative release record

This blueprint implements the synthetic hospital scenario in Python. It is a proposed application, not code already built. The local receiver replaces every real external agency. The privacy matrix is an explicit demo policy; clinical and legal determinations remain outside the model.

## 1. System map

![The privacy gateway owns policy decisions and release packets. RAG supplies permitted evidence, A2A specialists receive narrow tasks, and the workflow coordinates review and delivery.](assets/03-system-map.svg)

The Case API accepts a request and atomically records its dispatch intent. The workflow loads the patient/encounter relationship and asks the policy service for a constrained view. RAG and agents receive only that view or scoped references. A reviewer approves the resulting recipient-specific packet. The release service revalidates and dispatches to the trusted test receiver.

## 2. Ownership

| Component | Owns | Must not own |
|---|---|---|
| Case API | Intake, requester context, authorized read models | Raw unrestricted chart export |
| Policy/release domain | Policy versions, recipient bindings, projected packets, grants, release receipts | Agent reasoning or clinical decisions |
| RAG | Source versions, classified chunks, authorized evidence packs | Permission to expand scope |
| Specialists | Their own bounded task state and artifacts | Other agents' private stores or full chart credentials |
| Workflow | Jobs, checkpoints, review requests, release coordination | Authority to bypass the policy service |
| Receiver simulator | Accepted release keys and synthetic delivery receipts | Production external messaging |

Use a PostgreSQL instance with separate schemas and roles initially. Store documents and packet bodies in private object storage. The audit reader sees only the metadata its role permits; diagnostic telemetry has even less detail.

## 3. Proposed file structure

```text
harborcare-privacy-platform/
├── backend/
│   ├── pyproject.toml
│   ├── migrations/
│   ├── src/harborcare/
│   │   ├── contracts/{identity,request,decision,packet,receipt}.py
│   │   ├── security/{authenticate,relationships,authorize}.py
│   │   ├── policy/{classify,evaluate,project,versions}.py
│   │   ├── release/{repository,grants,dispatch,reconcile}.py
│   │   ├── mcp_gateway/{server,tools}.py
│   │   ├── rag/{ingest,scope,search,evidence}.py
│   │   ├── agents/{scheduling,claims,transport}/
│   │   ├── workflow/{states,jobs,outbox,review,worker}.py
│   │   ├── case_api/{app,commands,queries}.py
│   │   ├── audit/{events,redaction,queries}.py
│   │   └── lab/{receiver,scenarios,canaries}.py
│   └── tests/{unit,policy,protocol,integration,recovery}/
├── fixtures/{patients,policies,organizations,scenarios}/
├── apps/web/                 Added by the hybrid guide
├── infra/compose.yaml
└── docs/projects/
```

Braces above summarize related filenames, not literal directory names. Keep framework imports at edges. `evaluate.py` should be unit-testable without starting FastAPI or an MCP server.

## 4. Core contracts

`DisclosureRequest` includes requester reference, patient, encounter, requested recipient, requested purpose, and field categories. The authenticated actor and trusted assignment are resolved server-side, not accepted as facts from JSON.

`PolicyDecision` contains allow/deny/review, allowed field paths, decision reasons, policy and relationship revisions, expiry, and the exact context evaluated. `Packet` contains a fixed schema, patient/encounter references, recipient, purpose, projected values, source revisions, and a digest. Internal patient IDs need not be included in the external packet if the recipient can use a scoped alias.

`ReleaseGrant` binds packet digest, recipient identity, destination reference, purpose, policy/relationship revisions, and expiry. `ReleaseReceipt` records the logical release ID, receiver acknowledgement, outcome, and timestamps. Never put a bearer token or raw medical record inside a diagnostic event.

## 5. Policy and projection algorithm

Authenticate the actor. Load a current relationship for the patient/encounter and verified recipient. Validate the requested purpose against the assigned task. Evaluate applicable restrictions and policy. Intersect requested fields with the permitted schema. Deny unknown field paths and unrecognized categories.

Build a new object from permitted fields. Do not mutate a full chart in place by deleting a few known forbidden fields: a newly added clinical field could escape the blacklist. For nested objects and lists, use typed schemas and explicit paths; a shallow top-level filter is not enough.

Derived text is not trusted merely because the model produced it. Validate structured fields, citations, and data classification. Keep free-text generation out of externally released transport packets in the first release; use deterministic templates over allowed values. This makes leakage tests more meaningful.

## 6. Retrieval and specialist calls

Separate public material from patient-linked sources. RAG requires an authorized scope before querying. Filter by hospital, patient/encounter, category, source readiness, and purpose as appropriate before candidate retrieval/ranking. Scope caches by policy and relationship revisions or avoid caching patient data initially.

The coordinator submits A2A assignments with stable delegation IDs and minimal task data. The transport agent receives transport facts, not a full patient chart with a warning in its prompt. Claims and scheduling have their own contracts. Validate returned artifacts against the assignment before they can influence a packet.

Use configured recipient/service registries. Do not follow arbitrary model-proposed URLs or redirects. Public discovery metadata must not reveal patient assignments.

## 7. Release sequence and transaction boundary

![Packet preparation is followed by review and a fresh dispatch gate. Revocation blocks queued work; uncertain delivery requires receipt reconciliation rather than blind resending.](assets/04-release-lifecycle.svg)

First persist the proposed packet and review state. Approval binds its exact digest and recipient. Next create a release intent and outbox row atomically. At dispatch, lock the release and relevant authorization records, revalidate current authority, and mark the attempt in flight with a fencing generation.

The external send happens outside the local database transaction. This gap cannot be wished away. Define the authorization checkpoint precisely: revocation before the checkpoint prevents initiation; revocation after sending begins may not prevent disclosure. Recheck before a retried transmission and record the timing honestly.

The receiver simulator deduplicates a stable release ID plus packet digest. The same ID with changed content is a conflict. On lost acknowledgement, query its status using a metadata-only request. If policy is now revoked, do not use reconciliation as a reason to resend the body. Unknown outcomes can require human investigation.

## 8. Audit without creating a second chart

Audit events record actor/recipient references, patient reference as permitted, purpose, field categories, decision version, packet digest, release ID, timestamps, and reason codes. Packet contents stay in the protected packet store with separate access and retention rules.

Hashes and identifiers are not automatically anonymous. Restrict audit queries, record access, and minimize exported telemetry. Do not log full HTTP request bodies or exceptions containing source documents. The receipt store remains authoritative even when the telemetry collector is unavailable.

## 9. Verification and operations

Run the PRIV-01 through PRIV-18 catalogue against the actual database, protocol endpoints, and receiver. Instrument the fixture model adapter to capture its input so tests can prove restricted content never reached it. Capture outbound traffic to the receiver and compare exact allowed field sets.

Use role-specific database credentials, loopback-only local services, bounded workers, graceful shutdown, and migration locks. Production-demo readiness includes backup restore, release reconciliation, redacted diagnostics, environment isolation, and documented limitations. A successful HTTP response alone proves none of these.
