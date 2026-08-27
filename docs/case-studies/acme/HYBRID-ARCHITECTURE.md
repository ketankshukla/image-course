# Acme Agent Platform — Hybrid Architecture

## Next.js and React on Vercel. Python behind the scenes.

**Five portfolio projects, one realistic case study, and a clear boundary between the screen and the system doing the work.**

This is a proposed implementation blueprint, not a report of applications already built. It extends the Python project strategy with a polished web experience. The existing course website remains separate: these applications belong in a new repository. The example business, customer, policy, and transactions are fictional. All credits go to a simulated ledger, never to a payment provider.

## 1. At a glance

![Hybrid command path: a React workspace calls Next.js on Vercel, which calls the Python Case API. Persisted work is picked up by the Python workflow runtime and its MCP, RAG, and A2A capabilities.](companion-architecture-assets/01-hybrid-overview.png)

The browser is the reception desk. Next.js is the receptionist's secure connection to the back office. Python is the back office: it investigates, applies rules, remembers unfinished work, and records the outcome.

**BFF means backend for frontend:** a small server-side layer shaped around what the browser needs. It can translate a login session into a trusted backend request and combine a few authorized responses into a convenient screen. It is not a second implementation of the business.

The arrow from Python API to workflow means **persist, then dispatch**. It does not mean the API holds a connection open until the whole case finishes. An outbox and leased jobs sit behind that simplified arrow. The storage band represents separately owned schemas and private objects, not universal database access.

| Question | Design decision |
|---|---|
| Where does the person work? | A React case workspace delivered by Next.js on Vercel |
| Where are rules enforced? | Python services, including the domain service behind MCP |
| Who remembers unfinished work? | The Python database-backed workflow runtime |
| Who decides whether a credit actually happened? | The domain transaction and its receipt |
| What does Vercel host? | Web rendering, authenticated browser endpoints, bounded response streaming |
| What runs elsewhere in this baseline? | Python APIs and long-lived workers on a container-capable host |
| Why choose this version first? | Preserve the Python learning investment while adding a professional interface |

## 2. What the architecture teaches

### A real-life-style case: the disputed service charge

Maya works on Acme's customer support team. A customer disputes a $120 service charge. Maya needs to know whether the charge is valid, which policy applies, whether an exception is allowed, and who approved the final action. A chatbot that simply says “I refunded you” would be dangerously incomplete.

Maya opens the case workspace and submits the dispute. The application returns case `CASE-1042` quickly. The screen says **Received**, not **Resolved**. That distinction matters: accepting work is different from completing work.

The Python workflow first obtains permitted account facts. It then asks the retrieval service for evidence relevant to the charge date and policy version. Two specialists receive bounded assignments. Policy examines eligibility; Finance checks the arithmetic. Neither specialist is allowed to issue money-like credits.

Policy finds that the applicable rule permits a partial exception. Finance calculates a $75 credit. Their outputs are versioned artifacts, not free-floating chat messages. The coordinator builds proposal revision 3, referencing the evidence pack and both specialist artifacts.

Maya now sees the proposed $75 adjustment, the reason, the source passages, and the remaining $45 charge. She can inspect these inline. She does not need to open a collection of separate dashboards to understand the recommendation.

When Maya approves, the server checks that she has the reviewer role for this tenant and case. It also checks that revision 3 is still current. Her approval is recorded against the exact action, not against an open-ended request such as “do whatever the agent recommends.”

The execution worker receives authority to request that one operation. The MCP gateway validates it again and invokes the domain transaction. The credit, its receipt, and the consumed execution grant are committed together. Only then can the screen show **Completed**.

### Why the browser does not own the process

Imagine Maya closes her laptop while Finance is still working. If the process lived in React state, it would disappear. If it lived in a long-running page request, a timeout could interrupt it. Instead, the backend has already recorded the case and its next job. Maya can return tomorrow and reconstruct the state from persistent records.

React may keep a selected tab, an expanded evidence card, and an unsent comment in local state. It must not be the only place that knows an approval exists. This separates **interface state** from **business state**.

### Why Next.js does not repeat Python's rules

The interface can warn that an amount is missing. The Python backend must still validate it. A browser is an untrusted caller, and another client could bypass the screen entirely.

However, we should not independently implement the $75 eligibility calculation in both languages. Two copies will eventually disagree. Python produces the authoritative calculation; React displays it. TypeScript may validate the shape of the response, but it does not secretly become a competing policy engine.

### Why protocols have different jobs

MCP exposes controlled capabilities such as account lookup and credit execution. A2A lets an independently running specialist accept responsibility for a task and return an artifact. RAG supplies evidence. Ordinary HTTP carries application commands and queries. A framework import inside one process is simply a function call.

Calling every interaction “agent communication” hides the distinctions that make the architecture explainable. The protocol follows the boundary; we do not add a protocol where a local function is sufficient.

## 3. How the five projects fit together

| Project | Python responsibility | New web experience | Standalone demonstration |
|---|---|---|---|
| P1 — MCP Operations Gateway | Tool discovery, authorized reads, safe domain writes | Tool catalogue, request inspector, receipt panel | Denied write, approved write, duplicate retry |
| P2 — Evidence RAG Workbench | Ingestion, source versions, retrieval, evidence packs | Upload progress, search, inline passages | Correct evidence, wrong-tenant rejection, no-evidence response |
| P3 — A2A Specialist Network | Policy and Finance tasks, status, artifacts | Delegation timeline and side-by-side findings | Independent agents communicating through A2A |
| P4 — Durable Workflow Lab | Outbox, jobs, checkpoints, approval, recovery | State timeline and controlled failure controls | Crash after commit, then recover original receipt |
| P5 — Case Resolution Platform | Intake and integrated read models | Complete workspace for Maya | Submit, investigate, approve, reconcile, complete |

One application can contain five learning areas. Five projects do not require five unrelated login systems or five copies of the same database model. Each area should have its own explanation, fixture scenario, tests, and demonstration script.

## 4. Deployment and ownership boundaries

The baseline has three hosting groups. Vercel serves the Next.js application. A container environment runs the Python services and persistent worker processes. Managed PostgreSQL and object storage hold durable data. Local development replaces these remote dependencies with local equivalents where practical.

This is a workload choice, not a claim that Vercel cannot run Python. Vercel supports bounded Python functions too. The existing educational Python runtime deliberately includes workers that lease jobs and run continuously; that makes a container environment a straightforward fit. Function execution remains time-limited and plan-dependent. Verify current limits when implementing rather than designing around a remembered number. [Vercel Functions limits](https://vercel.com/docs/functions/limitations), [Node.js and Python duration update](https://vercel.com/changelog/vercel-functions-can-now-run-up-to-30-minutes).

| Component | Process or deployment | Database permissions |
|---|---|---|
| Next.js web/BFF | Vercel application | No direct access to Python-owned business schemas |
| Python Case API | HTTP service | Case intake and authorized read models |
| Workflow worker and relay | Background processes | Workflow, approval, jobs, inbox/outbox |
| MCP gateway with domain module | HTTP service | Operational domain, ledger, grants, receipts |
| RAG API and ingestion worker | API plus worker | Sources, versions, chunks, evidence packs |
| Policy and Finance agents | Separate A2A services/workers | Their own task and artifact records |

Keep the database near the backend services to avoid adding a long network round trip to every query. Start in one region. A globally reachable frontend does not make a region-bound transaction globally local.

## 5. Proposed repository and file structure

The tree below is a design for a new repository. It is not a list of files this document has created.

```text
acme-agent-platform-hybrid/
├── apps/
│   └── web/
│       ├── app/
│       │   ├── layout.tsx
│       │   ├── page.tsx
│       │   ├── cases/page.tsx
│       │   ├── cases/[caseId]/page.tsx
│       │   ├── cases/[caseId]/actions.ts
│       │   ├── api/cases/route.ts
│       │   ├── api/cases/[caseId]/events/route.ts
│       │   ├── api/uploads/prepare/route.ts
│       │   ├── loading.tsx
│       │   └── error.tsx
│       ├── components/
│       │   ├── case-workspace.tsx
│       │   ├── evidence-panel.tsx
│       │   ├── approval-panel.tsx
│       │   ├── task-timeline.tsx
│       │   └── receipt-card.tsx
│       ├── lib/server/
│       │   ├── session.ts
│       │   ├── backend-client.ts
│       │   ├── delegation.ts
│       │   └── case-queries.ts
│       ├── lib/client/event-cursor.ts
│       ├── next.config.ts
│       └── package.json
├── backend/
│   ├── pyproject.toml
│   ├── src/acme/
│   │   ├── contracts/
│   │   ├── security/
│   │   ├── domain/
│   │   ├── case_api/
│   │   ├── mcp_gateway/
│   │   ├── rag/
│   │   ├── agents/policy/
│   │   ├── agents/finance/
│   │   ├── workflow/
│   │   │   ├── coordinator.py
│   │   │   ├── worker.py
│   │   │   ├── relay.py
│   │   │   ├── approvals.py
│   │   │   └── reconciliation.py
│   │   ├── model/
│   │   ├── observability/
│   │   └── lab/
│   ├── migrations/
│   └── tests/
├── packages/api-contracts/
│   ├── openapi.json
│   ├── schemas/
│   ├── generated/types.ts
│   └── fixtures/
├── tests/contract/
├── tests/e2e/
├── infra/compose.yaml
├── scripts/
├── docs/projects/
├── .env.example
└── README.md
```

### Read the folders in this order

Start with `contracts`: it defines the messages crossing boundaries. Read `domain` next: it contains the rules that must remain true regardless of the UI or model. Then inspect `case_api` and `workflow` to see how a request becomes durable work. Finally, inspect the web app to see how that work is presented.

`backend-client.ts` is the only general gateway from Next.js into Python. It attaches trusted credentials, forwards stable request identifiers, applies deadlines, and translates expected errors. It must not automatically retry every POST with a newly generated operation key.

`case-queries.ts` prepares authorized screen data. `actions.ts` accepts user intent and invokes the backend adapter. `approval-panel.tsx` displays the proposal and collects confirmation. None of those files writes a ledger row.

Generate TypeScript API types from the backend's published schema and verify the generated files in continuous integration. Keep runtime validation at network boundaries: a TypeScript type annotation does not inspect bytes received over HTTP.

## 6. React and Next.js: which code runs where?

Use Server Components for the initial case view and Client Components for controls that need interaction. Keep credentials and backend adapters server-only. Only send the browser fields it is authorized to display. These boundaries follow the Next.js model, but the business ownership rules are this project's design. [Next.js Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components).

| File or feature | Runs where? | What it does |
|---|---|---|
| Case page | Next.js server | Loads authorized initial case snapshot |
| Evidence panel | Server-rendered content, optional client controls | Shows passages and allows expansion |
| Approval panel | Browser interaction | Shows the exact proposal and submits confirmation |
| Approval action | Next.js server | Rechecks session and forwards command |
| Backend adapter | Next.js server only | Calls Python with scoped identity |
| Event subscription | Browser plus bounded server endpoint | Updates the timeline from durable events |

The Server Component calls the backend adapter directly; it need not make an HTTP request to its own Next.js API first. Browser requests use the public application boundary. Server Actions remain remotely invocable mutation endpoints and need authentication, authorization, input validation, and the framework's origin protections; a hidden button is not protection.

Default private case responses to explicit non-shared caching. Do not place tenant case content in a public CDN cache. Any later cache design must include tenant and authorization context and invalidate correctly after approvals or access changes. Public course diagrams may be cached differently from customer case data.

## 7. Exact call flow: submission to receipt

| Step | Caller → receiver | Information crossing the boundary | Durable outcome |
|---|---|---|---|
| 1 | React → Next.js | Dispute form and intake idempotency key | None yet |
| 2 | Next.js → Python Case API | Validated form, trusted user delegation, same key | Case and intake outbox committed together |
| 3 | Relay → workflow inbox | Case-created event ID | Deduplicated workflow job |
| 4 | Coordinator → MCP | Authorized account lookup | Referenced account snapshot |
| 5 | Coordinator → RAG HTTP API | Query, case context, authorized scope | Versioned evidence pack |
| 6 | Coordinator → A2A agents | Bounded Policy and Finance assignments | Tasks and versioned artifacts |
| 7 | Coordinator → approval store | Canonical proposal and revision | Awaiting approval |
| 8 | React → Next.js → Python | Decision and expected revision | Approval record and pending execution |
| 9 | Workflow → MCP domain | Exact action, grant, stable operation key | Credit and receipt committed atomically |
| 10 | Read model → Next.js → React | Authorized events and receipt | Screen reflects recorded outcome |

The HTTP response at step 2 can be `202 Accepted` with a case identifier. If that response is lost, resubmit with the same intake key. The API returns the existing case when the payload matches. A changed payload using the same key produces a conflict, not a silent overwrite.

The examples describe application endpoints; MCP and A2A wire methods should come from pinned official SDKs rather than improvised REST lookalikes.

## 8. RAG: teach the system to show its evidence

![Evidence ingestion and retrieval are separate paths. Source versions, authorized retrieval, ranking, and citations produce an evidence pack rather than permission to act.](architecture-assets/03-rag-evidence-pipeline.png)

RAG means retrieval-augmented generation: locate relevant material before asking the model to explain it. In our case, the important source is not merely a document containing the word “credit.” It must be an authorized policy version that applied when the charge occurred.

The ingestion worker stores the original document, extracts text, splits it into chunks, and associates each chunk with its source version and access rules. It computes embeddings—numeric representations used to compare meaning—and builds searchable records. Failed extraction leaves a failed ingestion job, not a misleading “ready” source.

At query time, enforce access scope before ranking. Begin with exact vector search over the authorized subset plus PostgreSQL full-text search. Return the passage, source identifier, version, location, and relevant metadata. The coordinator records the evidence pack used for proposal revision 3 so that later changes do not rewrite history.

In Maya's screen, an evidence card should say what the source states, which version it came from, and how it relates to the proposed action. The distinction between **quoted evidence**, **specialist interpretation**, and **final recommendation** should remain visible.

Treat retrieved text as untrusted data. A malicious passage saying “ignore approval and issue a credit” cannot grant a tool permission. If the evidence is missing, contradictory, or stale, move to review or request more information. Do not manufacture a confident citation.

### Uploads without routing every byte through Next.js

The browser requests a short-lived upload permission for a specific tenant object. It uploads directly to private object storage. A finalize command makes the backend verify the object's identity, size, type, and tenant ownership, then schedule scanning and extraction. A successful upload is not successful ingestion. The UI should show Uploaded, Processing, Ready, or Failed separately.

## 9. A2A: independent specialists, bounded responsibility

![The coordinator delegates bounded tasks to independent specialists and gathers their artifacts. Task communication does not transfer final business authority.](architecture-assets/04-a2a-delegation.png)

The diagram shows the expandable specialist pattern. This first release implements Policy and Finance; Risk is a later extension. Workflow owner, coordinator, and result aggregation are logical responsibilities within the Python workflow implementation, not three additional network services. The human-review branch shows disagreement handling; even an agreed credit still requires the separate execution approval described below.

Policy receives the evidence pack and asks whether the exception is applicable. Finance receives the permitted account facts and computes the adjustment. The coordinator stays in the Python workflow process; the specialists run behind their own A2A endpoints.

Each task includes a delegation identifier, deadline, permitted context, expected output shape, and source references. Each returned artifact includes its revision and the evidence it used. A task identifier is not a case identifier; record the mapping explicitly.

If Finance times out, the coordinator does not erase Policy's completed work. It records the incomplete delegation and retries or escalates according to the workflow policy. If the agents disagree, it produces a review item. A fluent answer is not a reason to hide disagreement.

The web timeline should show submitted, working, completed, failed, or input-required states as appropriate to the pinned protocol version, with a plain-English summary. It should not expose hidden model reasoning or internal credentials. Show evidence, tool results, and concise decision explanations instead.

## 10. Human approval and safe MCP execution

![Sensitive MCP writes pass through identity, authorization, exact approval binding, idempotency, and a domain transaction before producing a receipt.](architecture-assets/02-mcp-safe-write.png)

Approval is a record with meaning. It binds tenant, case, account, action, amount, currency, proposal revision, relevant evidence revisions, reviewer, and expiry. Use a canonical payload digest to detect substitution. The server recomputes that binding; it does not trust a browser-supplied hash alone.

For the running case, the approved business action includes:

```json
{
  "case_id": "CASE-1042",
  "proposal_revision": 3,
  "action": "issue_credit",
  "amount_minor": 7500,
  "currency": "USD",
  "operation_key": "CASE-1042-credit-proposal-3"
}
```

The execution grant additionally binds the account, tenant, authorization scope, expiry, and proposal digest. The abbreviated example is not a complete security token.

Only the execution identity may invoke the write. Finance can recommend 7500 minor units; it cannot convert its recommendation into permission. The domain service locks and validates the relevant records, checks business uniqueness, consumes the grant, inserts the credit and receipt, and writes its outgoing event in one local database transaction.

For a matching completed operation key, the service returns the original receipt after authenticating and authorizing the caller; it does not demand that the already-consumed grant become unused again. For the same key with a different action payload, it returns a conflict. A separate business uniqueness rule prevents a caller from using a fresh key to repeat the same approved adjustment.

If a reviewer opens revision 3 but revision 4 is created before they click, reject the stale approval and display the new proposal. Never silently apply a stale confirmation to a changed amount.

## 11. Failure recovery and live progress

Suppose the ledger commits, but the worker loses the response. “No response” does not mean “no credit.” The workflow enters a reconciling state and queries the operation or retries the same command with the same key. It receives the existing receipt. Only then does it update the case outcome.

A leased job uses an expiry and a fencing/version check so a worker that resumes after losing its lease cannot overwrite a newer worker's state. Inbox deduplication handles repeated events. Outbox retry handles failed delivery. These mechanisms provide recoverable processing; they do not create universal exactly-once network delivery.

The screen reads durable events using a cursor. With server-sent events, reconnect after a bounded connection closes and resume after the last acknowledged event ID. If the cursor is too old, fetch a fresh snapshot. Authorize the case on every connection. Polling is a valid first implementation and can be easier to test.

Disconnecting a stream must not cancel the workflow. An explicit Cancel command is separate, and cancellation after a possible business effect must reconcile that effect. The UI should distinguish **Disconnected**, **Retrying**, **Needs review**, and **Failed** rather than treating them as the same red badge.

## 12. Identity, secrets, and trust

Next.js verifies the user's session. It then calls Python using a short-lived, audience-restricted delegation mechanism that the backend verifies. Include the actor and tenant, but derive tenant membership from trusted identity data, not a text field in the form. Authenticate the service as well as the user whose request it forwards.

Never trust arbitrary inbound headers such as `X-User-Id`. Strip spoofable headers at the public boundary. Backend authorization must verify that the delegated actor may access the specific case. Internal service credentials should have least privilege and be separately rotatable.

Keep model keys, database credentials, and delegation signing material out of browser bundles and public environment variables. Redact logs. Do not dump full customer documents into traces. Even this fictional-data demonstration should establish good habits.

Preview deployments must use isolated synthetic data and separate credentials. A preview URL must not accidentally point at a production write-capable backend. Failure-injection controls belong only in the authenticated demonstration environment and must be absent or disabled in production builds.

## 13. Testing the architecture, not just the buttons

| Test layer | Example assertion | What it proves |
|---|---|---|
| Python unit | Unsupported policy cannot produce an executable proposal | Rules are independent of UI |
| Contract | Python responses validate against published schemas and TS consumers | Language boundary agrees |
| Protocol | Discover and call MCP; submit and retrieve A2A tasks over HTTP | Real protocol integration |
| Database | Concurrent same-key requests create one credit and one receipt | Local transactional safety |
| Security | Tenant B cannot fetch Tenant A's evidence or event cursor | Scoped access |
| End-to-end | Submit, inspect evidence, approve, see receipt | Complete user journey |
| Recovery | Crash after commit, then resume | Unknown outcome is reconciled |
| UI | Keyboard approval, readable source cards, reconnect notice | Usable and accessible experience |

Fixture mode uses deterministic model responses and synthetic documents but keeps real HTTP, database transactions, MCP, and A2A boundaries. Live mode swaps the model adapter, not the entire application. This lets a reviewer run the architecture without paying for unpredictable model calls.

Measure elapsed time, retry counts, retrieval accuracy on labeled fixtures, and duplicate-credit counts. Report measured results only after running the tests. Do not turn suggested acceptance criteria into claimed achievements.

## 14. Build order and demonstration script

Build one vertical slice first: submit a case, persist it, and display it after a browser refresh. Then add evidence retrieval, specialist tasks, approval, safe execution, and failure recovery in that order. Each stage must leave the app runnable.

| Milestone | Deliverable | Exit condition |
|---|---|---|
| 1 | Contracts, fixtures, local data stores | Invalid payloads and wrong tenants rejected |
| 2 | Next.js case workspace plus Python intake | Refresh does not lose accepted cases |
| 3 | Evidence workbench | Inline versioned citations match fixtures |
| 4 | A2A specialists | Independent task records and artifacts visible |
| 5 | Approval and MCP write | Unauthorized and stale writes rejected |
| 6 | Recovery lab | Lost response returns the original receipt |
| 7 | Isolated deployment | Secrets, health checks, budgets, and rollback tested |

For a presentation, open with the customer problem, not the technology list. Submit the dispute and explain why acceptance is immediate. Expand the policy passage. Show the two specialist findings. Attempt a stale approval to make revision binding tangible. Approve the current proposal, simulate a lost response, then show that the recovered receipt identifies the same single credit.

Finish with one sentence: **“React makes the work understandable; Python makes the work durable and enforceable.”**

## 15. When this is the right choice

Choose the hybrid architecture when Python is a core learning objective, when you want to preserve the reference backend, or when your retrieval and document-processing tools are strongest in Python. Its cost is maintaining two language toolchains and a real network contract between them.

Do not add a second TypeScript workflow engine just because the frontend is on Vercel. In this version, Python owns case orchestration. If you later replace a component, migrate one boundary at a time and keep one authoritative business writer for each case.

The result is not a thin chatbot wrapper. It is an explainable operations application whose interface, protocols, evidence, approvals, and recovery behavior can each be demonstrated independently.
