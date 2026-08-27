# The Hospital Case in Plain English

## A hospital team needs to coordinate—not tell everybody everything

Imagine a hospital organizing a patient's journey home. A doctor needs clinical information. A transport company needs to know where and when to collect the patient. An insurer may need a specific set of claim facts. These are different jobs, so they should not all receive the same envelope.

Our application prepares the right envelope for the right organization. It checks the request, selects only permitted information, asks for review where our demonstration policy requires it, and records what happened. Every person and record in this case is fictional.

## 1. At a glance

![A discharge request passes identity and purpose checks, then restricted evidence and specialist tasks, before a recipient-specific packet is reviewed and released.](assets/01-patient-journey.svg)

The most important sentence is: **private information can be shared with an authorized recipient without becoming public information.** A destination address is still private when the assigned driver needs it.

## 2. Follow one patient

The care coordinator opens the synthetic discharge case. The system confirms that the coordinator belongs to the hospital and is assigned to this patient. Merely working at a hospital does not mean a person may inspect every record.

The coordinator chooses the transport task. The system identifies the actual assigned transport organization using a stable organization ID and verified credentials—not a similar-looking company name typed into a box.

The policy service checks the permitted purpose, the current assignment, and any required authorization under our demo rules. It decides which fields may be used. The retrieval component receives that restricted scope before looking for evidence.

The transport agent receives a bounded task: plan a pickup using the allowed scheduling information. It does not receive the diagnosis and then promise not to mention it. The safer design keeps unnecessary information out of its context in the first place.

The system builds a packet preview. The reviewer sees the exact recipient, pickup information, and the categories withheld. They approve that particular version. Just before dispatch, the system checks that the assignment and permission are still valid.

The packet is sent only to our synthetic test receiver. The receiver returns a receipt, and the case records delivery. If the reply is lost, the system checks the same release reference rather than sending a newly expanded packet.

## 3. What counts as public?

Public information is deliberately approved general material: hospital address, visiting hours, services offered, and general educational content. A public statement that the hospital offers oncology is different from a statement that a particular patient is receiving oncology treatment.

Names, appointment times, pickup destinations, insurance IDs, diagnoses, and even confirmation that a named person is admitted can be patient-linked information. Removing the diagnosis does not automatically make the rest public. Replacing a name with an ID does not automatically make the record anonymous.

The demo uses a separate, curated public collection. It does not ask a model to turn private records into public pages on its own.

## 4. The three familiar technologies

**MCP is the controlled tool counter.** It exposes specific operations: retrieve a permitted patient view, preview a packet, release an approved packet, or check a receipt. Our application enforces permission; MCP does not decide healthcare law for us.

**RAG is the careful librarian.** It finds relevant policy passages and authorized patient facts. It must search within permission boundaries before returning text to a model. Filtering the answer afterward is too late if private text already reached an unauthorized agent.

**A2A is the assignment system.** Scheduling, transport, and claims specialists exchange bounded tasks and results. Each task carries only the information needed under the demo policy. The agents cannot enlarge their own permissions.

**The workflow is the checklist keeper.** It remembers the request, decision, review, dispatch, and receipt. It can wait for a person without depending on an open browser window.

## 5. Technology and concept legend

| Name | Simple explanation | Where it fits |
|---|---|---|
| Python | Language for writing the main backend | Rules, services, retrieval, workers |
| TypeScript | JavaScript with development-time type checks | Web app and alternative backend |
| React / Next.js | Tools for building the web workspace and server-side page behavior | Reviewer screen and browser-facing API |
| FastAPI | Python framework for HTTP endpoints | Case and internal APIs |
| Pydantic / runtime schemas | Check actual input and output shapes | Reject malformed requests; not a substitute for permission |
| PostgreSQL | Durable organized records | Assignments, cases, decisions, packets, receipts |
| pgvector / full-text search | Search by meaning and words | Retrieve evidence inside authorized scope |
| Private object storage | Store whole documents and encrypted packet objects | Source files and bounded artifacts |
| Identity provider | Verifies users and service identities | Sign-in and machine authentication; vendor not selected |
| Authentication | “Who are you?” | Verify requester and recipient |
| Authorization | “May you do this?” | Check patient, purpose, fields, and time |
| Role and attributes | Job category plus context such as care assignment | A clinician role alone is not enough |
| Policy engine | Ordinary code evaluating explicit sharing rules | Produces allow, deny, or review decisions |
| Field allowlist | Exact list of fields permitted in this packet | Select information before processing and delivery |
| Projection | A smaller view made from only allowed fields | Transport view instead of a full chart |
| Data classification | Labels describing information sensitivity | Public, internal, patient-linked, specially restricted |
| Consent/authorization record | Evidence of a permission or restriction where applicable | One input to policy; not the only possible legal basis |
| Execution/release grant | Permission slip bound to one packet and recipient | Final disclosure gate |
| Hash | A compact fingerprint of exact bytes or structured content | Detect changed packet; does not make it anonymous |
| Encryption | Scramble data so only holders of the right key can read it | Protect storage and transport; does not authorize recipients |
| Audit trail | Protected record of decisions and outcomes | Explain who received what categories and why |
| Outbox / job queue | Saved work waiting to be delivered or processed | Survive process failures |
| Idempotency | Repeating the same request does not create another logical action | Avoid duplicate release records and duplicate receiver processing |
| Reconciliation | Check what really happened after a missing reply | Query the existing delivery receipt |
| Revocation | Withdrawal or invalidation of authority for future action | Stop a queued release when applicable |
| Workflow DevKit | Durable TypeScript execution framework | Alternative to the Python scheduler |
| Git / GitHub | Source history and hosted collaboration | Code, fixtures, tests—not live patient records |
| Docker / container host | Package and run services | Python backend and local development |
| Vercel | Proposed host for the web app and compatible TS services | Synthetic demo only until real deployment review |
| Tests / CI | Automated checks before release | Prove wrong recipients and wrong patients are blocked |
| Logs / traces / metrics | Diagnostic records and measurements | Observe failures without copying clinical content |
| FHIR | A healthcare data-exchange standard | Possible future adapter, not required or implemented here |

The stack contains alternatives, not a requirement to install everything twice. The Python workflow and the TypeScript workflow do not jointly control one disclosure.

## 6. Why “just redact the answer” is insufficient

If an unauthorized agent has already read the full record, hiding a diagnosis in its final answer does not undo that access. The information might also appear in a trace, cache, source citation, retry payload, or intermediate summary.

We therefore check permission at entry, at retrieval, at task creation, at packet creation, and at release. Each boundary checks the current context rather than trusting a model's statement that the request is harmless.

## 7. Explain it in one paragraph

“We are building a hospital coordination demo where each organization receives a different approved view of a synthetic patient's information. The system checks identity, relationship, purpose, and permitted fields before retrieving or sending data. Agents help coordinate tasks, but ordinary policy code controls disclosure. The reviewer sees the exact packet, and the system records delivery or denial without treating private information as public.”
