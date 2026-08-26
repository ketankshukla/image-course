# Volume 6 Diagram Prompt Library

These are the exact production prompts for Diagrams 125-148. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

## Shared art direction

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

## Diagram 125 - Conversation state, run state, task state, and workflow state

Output filename: `diagrams/125-state-layer-map.png`

Pattern status: Durable-system foundation

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show four separate layers labeled CONVERSATION, AGENT RUN, A2A TASK, BUSINESS WORKFLOW. Give each a different ID, OWNER, LIFETIME, and STORE. Use dashed CORRELATION ID links across layers. A coral MERGED SESSION STORE collapses all four and is labeled LOST OWNERSHIP.

Accessibility alt text: Four distinct state layers for conversation, agent run, A2A task, and business workflow are correlated without being merged, while one combined session store is rejected.

## Diagram 126 - State machines, events, commands, and invariants

Output filename: `diagrams/126-command-event-state-machine.png`

Pattern status: Mature correctness pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show USER COMMAND entering VALIDATE INVARIANTS. Valid path emits an EVENT into APPEND-ONLY HISTORY and a reducer moves STATE from OPEN to WAITING APPROVAL. Coral invalid path emits COMMAND REJECTED and leaves state unchanged. Labels: COMMAND, INVARIANT, EVENT, STATE.

Accessibility alt text: A command is checked against invariants, accepted as an event that changes state, or rejected without changing state.

## Diagram 127 - Checkpoints, snapshots, replay, and schema evolution

Output filename: `diagrams/127-snapshot-replay-schema-evolution.png`

Pattern status: Durable execution pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show APPEND-ONLY EVENTS 1 TO 900 flowing into SNAPSHOT AT 800, then REPLAY 801 TO 900 to rebuild CURRENT STATE. Above, CODE V1 and CODE V2 cross a VERSION GATE. Coral INCOMPATIBLE EVENT goes to MIGRATION TEST. Include CONTINUE AS NEW as a clean-history branch.

Accessibility alt text: A snapshot plus later events rebuilds current state while code versions and migration tests protect replay compatibility, with a continue-as-new branch for long histories.

## Diagram 128 - Durable artifacts, receipts, and business records

Output filename: `diagrams/128-artifact-receipt-business-record.png`

Pattern status: Auditability foundation

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show WORKFLOW creating three distinct outputs: A2A ARTIFACT, SIDE-EFFECT RECEIPT, BUSINESS RECORD. Each has ID, VERSION, HASH, ACTOR, TIME, and CORRELATION. A teal LINEAGE path reaches the source request. Coral CHAT ONLY is labeled NOT PROOF.

Accessibility alt text: A workflow produces a task artifact, side-effect receipt, and authoritative business record with identity and lineage, while chat text alone is rejected as proof.

## Diagram 129 - Queues, workers, leases, acknowledgements, and visibility

Output filename: `diagrams/129-queue-lease-ack-visibility.png`

Pattern status: Mature messaging pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show PRODUCER to DURABLE QUEUE to WORKER A. Delivery creates a LEASE or VISIBILITY WINDOW. Success returns ACK and removes the item. A coral WORKER CRASH lets the lease expire and WORKER B receives the same item. Include RECEIPT before ACK.

Accessibility alt text: A queue leases work to a worker; success records a receipt and acknowledges it, while a crash lets the lease expire so another worker receives the same item.

## Diagram 130 - Backpressure, rate limits, admission control, and priorities

Output filename: `diagrams/130-backpressure-admission-priority.png`

Pattern status: Reliability and fairness pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show REQUEST FLOOD entering ADMISSION GATE with CAPACITY, TENANT LIMIT, PRIORITY, and DEADLINE checks. Accepted work enters HIGH, NORMAL, BULK queues and sized WORKER POOLS. Coral OVERLOAD returns RETRY LATER. Teal CAPACITY SIGNAL flows backward.

Accessibility alt text: An admission gate uses capacity, tenant limits, priority, and deadlines to route accepted work into separate queues while overload returns a retry-later result and capacity signals flow upstream.

## Diagram 131 - Retries, idempotency keys, deduplication, and poison work

Output filename: `diagrams/131-retry-idempotency-poison-work.png`

Pattern status: Essential side-effect safety pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show WORK ITEM with IDEMPOTENCY KEY entering ATTEMPT 1 TIMEOUT then ATTEMPT 2. Both check DEDUP STORE. Existing RECEIPT returns SAME RESULT. Repeated deterministic failure goes to POISON or DEAD LETTER after RETRY BUDGET. No infinite loop.

Accessibility alt text: Retried attempts share an idempotency key and deduplication store so an existing receipt returns the same result, while repeated nonrecoverable failure moves to a poison-work lane.

## Diagram 132 - Deadlines, cancellation, timeout, and compensation

Output filename: `diagrams/132-deadline-cancel-timeout-compensation.png`

Pattern status: Long-running control pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show WORKFLOW with absolute DEADLINE flowing into STEP A then STEP B. USER CANCEL sends cooperative CANCELLATION. A TIMER creates TIMEOUT. Completed reversible STEP A has coral COMPENSATE A path. IRREVERSIBLE STEP B has POINT OF NO RETURN and MANUAL RECOVERY.

Accessibility alt text: A workflow carries a deadline, responds cooperatively to cancellation and timeout, compensates a completed reversible step, and treats an irreversible step as a point of no return.

## Diagram 133 - Orchestration versus choreography

Output filename: `diagrams/133-orchestration-vs-choreography.png`

Pattern status: Core distributed workflow choice

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Split canvas. Left ORCHESTRATION: one COORDINATOR sends COMMANDS to POLICY, FINANCE, NOTIFY and receives RESULTS. Right CHOREOGRAPHY: services publish FACT EVENTS through EVENT BUS and react independently. Bottom compares GLOBAL VIEW, COUPLING, RECOVERY, and OWNERSHIP.

Accessibility alt text: A side-by-side comparison shows a coordinator directing services in orchestration and services reacting to fact events through a bus in choreography, with ownership and recovery trade-offs.

## Diagram 134 - Parallel work, fan-out, fan-in, and joins

Output filename: `diagrams/134-fan-out-fan-in-join.png`

Pattern status: Parallel workflow pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show PARENT WORKFLOW fanning out to POLICY, LEDGER, FRAUD, CUSTOMER HISTORY workers. Each returns typed RESULT or ERROR to JOIN GATE. Gate has REQUIRED ALL, QUORUM, OPTIONAL, DEADLINE rules. Coral STRAGGLER and DUPLICATE paths are visible. End at AGGREGATED EVIDENCE.

Accessibility alt text: A parent workflow fans out to four workers and joins typed outcomes under required, quorum, optional, and deadline rules before creating aggregated evidence.

## Diagram 135 - Sagas, compensations, and irreversible effects

Output filename: `diagrams/135-saga-compensation-irreversible-effects.png`

Pattern status: Mature distributed transaction pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show SAGA steps RESERVE FUNDS, UPDATE CASE, SEND REFUND. Under each reversible step place a coral COMPENSATION. Mark PIVOT or POINT OF NO RETURN before irreversible SEND. Forward failures trigger reverse or business-specific compensation, then MANUAL REVIEW if compensation fails.

Accessibility alt text: A saga sequences local transactions with compensations, marks a point of no return before an irreversible refund, and escalates failed compensation to manual review.

## Diagram 136 - Scheduled, event-triggered, and externally resumed work

Output filename: `diagrams/136-schedule-event-external-resume.png`

Pattern status: Durable trigger pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show three entry paths into one WORKFLOW ID: SCHEDULE TIMER, DOMAIN EVENT, EXTERNAL CALLBACK. Each passes DEDUP AND CORRELATION GATE. Workflow may WAIT WITHOUT WORKER, then RESUME. Coral UNKNOWN CALLBACK and EXPIRED DEADLINE are rejected.

Accessibility alt text: Scheduled timers, domain events, and external callbacks pass through deduplication and correlation before resuming a waiting workflow without holding a worker.

## Diagram 137 - Agent roles, skills, contracts, and capability discovery

Output filename: `diagrams/137-agent-role-capability-contract.png`

Pattern status: Current A2A 1.0-aligned pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show COORDINATOR reading three AGENT CARDS: POLICY SPECIALIST, FINANCE SPECIALIST, CUSTOMER SPECIALIST. Each card lists SKILLS, INPUT MODES, OUTPUT MODES, SECURITY, INTERFACE, VERSION. A POLICY FILTER selects one. Coral DESCRIPTION ONLY is labeled NOT AUTHORITY.

Accessibility alt text: A coordinator compares three Agent Cards containing skills, modes, security, interfaces, and versions, then applies policy before selecting a specialist.

## Diagram 138 - A2A discovery, delegation, and task creation

Output filename: `diagrams/138-a2a-delegation-task-creation.png`

Pattern status: Current A2A 1.0 protocol contract

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show CLIENT AGENT resolving AGENT CARD then sending MESSAGE with CONTEXT ID and REQUEST ID through A2A INTERFACE. REMOTE AGENT returns TASK ID and WORKING status, later STATUS UPDATE and ARTIFACT. Coral VERSION FALLBACK is blocked. Labels include A2A-VERSION 1.0.

Accessibility alt text: A client resolves an Agent Card, sends a versioned A2A message, receives a durable task ID, follows status updates, and obtains an artifact while silent version fallback is blocked.

## Diagram 139 - Ownership, handoff, artifacts, and status propagation

Output filename: `diagrams/139-ownership-handoff-artifact-status.png`

Pattern status: Multi-agent responsibility pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show PARENT WORKFLOW owning CASE. It delegates TASK to FINANCE AGENT with INPUT ARTIFACT and ACCEPTANCE CONTRACT. Status moves SUBMITTED, WORKING, INPUT REQUIRED, COMPLETED. A HANDOFF LEDGER records FROM, TO, SCOPE, DEADLINE. Output ARTIFACT returns; ownership of CASE never moves.

Accessibility alt text: A parent workflow retains case ownership while a scoped finance task moves through statuses under a handoff ledger and returns an output artifact.

## Diagram 140 - Aggregation, disagreement, escalation, and final authority

Output filename: `diagrams/140-aggregation-disagreement-final-authority.png`

Pattern status: Decision-governance pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show POLICY AGENT, FINANCE AGENT, RISK AGENT returning RESULT CARDS with CLAIM, EVIDENCE, CONFIDENCE, LIMITS. AGGREGATOR preserves agreements and conflicts. POLICY ENGINE chooses AUTO ACCEPT, REQUEST MORE, HUMAN ESCALATE. FINAL AUTHORITY is a named role, not MAJORITY VOTE.

Accessibility alt text: Three specialist result cards enter an aggregator that preserves agreement and conflict, then policy selects acceptance, more evidence, or human escalation under a named final authority.

## Diagram 141 - Planner, executor, reviewer, and policy roles

Output filename: `diagrams/141-planner-executor-reviewer-policy.png`

Pattern status: Agent-control separation pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show USER GOAL entering PLANNER, producing a BOUNDED PLAN. POLICY GATE checks every proposed action. EXECUTOR performs allowed steps through tools. REVIEWER compares OUTPUT to acceptance tests and evidence. Coral PLAN CANNOT EXECUTE and REVIEWER CANNOT APPROVE OWN HIGH-RISK ACTION.

Accessibility alt text: A user goal becomes a bounded plan, policy checks actions, an executor performs allowed steps, and a reviewer tests the output with separation-of-duty warnings.

## Diagram 142 - Time, cost, token, tool, and retry budgets

Output filename: `diagrams/142-multi-dimensional-budget-ledger.png`

Pattern status: Bounded-agent reliability pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show PARENT BUDGET LEDGER with TIME, MONEY, TOKENS, TOOL CALLS, RETRIES, CONCURRENCY. It allocates smaller CHILD ENVELOPES to three agents. Every spend returns a RECEIPT and REMAINING amount. Coral BUDGET EXHAUSTED routes to PARTIAL RESULT, DEGRADE, or ESCALATE.

Accessibility alt text: A parent budget ledger allocates time, money, tokens, calls, retries, and concurrency to child agents, records spend, and routes exhaustion to explicit safe outcomes.

## Diagram 143 - Human interrupts, approvals, and missing input

Output filename: `diagrams/143-human-interrupt-approval-input.png`

Pattern status: Human-in-the-loop control pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show WORKFLOW reaching WAITING HUMAN with three cards: APPROVAL REQUEST, MISSING INPUT, OPERATOR INTERRUPT. Each card includes EXACT ACTION, EVIDENCE, RISK, AMOUNT, EXPIRY, APPROVER. Human sends APPROVE, DENY, EDIT, or SUPPLY INPUT. Coral STALE APPROVAL is revalidated.

Accessibility alt text: A workflow waits durably for approval, missing input, or an operator interrupt using a precise request contract, then handles approve, deny, edit, or supply-input outcomes with stale approvals revalidated.

## Diagram 144 - Steering, replanning, invalidation, and resume

Output filename: `diagrams/144-steering-replan-invalidate-resume.png`

Pattern status: Controlled adaptation pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show ORIGINAL GOAL to PLAN V1 with completed and pending steps. NEW INPUT enters IMPACT ANALYSIS. Unaffected completed work stays VALID; pending branches become INVALIDATED. PLAN V2 is POLICY CHECKED, new budgets reserved, then RESUME. Coral PATCH IN PLACE is blocked.

Accessibility alt text: New input triggers impact analysis that preserves valid completed work, invalidates affected pending branches, creates a checked second plan, and resumes without patching state invisibly.

## Diagram 145 - Races, duplicates, out-of-order events, and stale state

Output filename: `diagrams/145-race-duplicate-order-stale-state.png`

Pattern status: Distributed correctness foundation

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show four hazards entering STATE STORE: RACE between two commands, DUPLICATE event, OUT OF ORDER event 12 before 11, STALE WRITE version 7 against current 9. Guards are EXPECTED VERSION, UNIQUE KEY, SEQUENCE, and MONOTONIC STATE. Rejected paths are coral and observable.

Accessibility alt text: Race, duplicate, out-of-order, and stale inputs meet version, uniqueness, sequence, and monotonic-state guards before changing authoritative state.

## Diagram 146 - Fault injection and agent workflow chaos tests

Output filename: `diagrams/146-chaos-test-matrix.png`

Pattern status: Reliability verification practice

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a CHAOS MATRIX. Rows: BEFORE COMMIT, AFTER SIDE EFFECT, DURING ACK, DURING APPROVAL, DURING HANDOFF, DURING COMPENSATION. Columns: CRASH, TIMEOUT, DUPLICATE, REORDER, PARTITION, STALE INPUT. Each cell points to EXPECTED INVARIANT, RECEIPT, METRIC, RECOVERY.

Accessibility alt text: A chaos-test matrix combines six workflow boundaries with crash, timeout, duplicate, reorder, partition, and stale-input faults, requiring expected invariants and recovery evidence.

## Diagram 147 - Recovery drills, runbooks, ownership, and receipts

Output filename: `diagrams/147-recovery-runbook-receipt-chain.png`

Pattern status: Operational readiness pattern

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show ALERT to TRIAGE to IDENTIFY WORKFLOW to FREEZE OR CONTINUE to RECONCILE EXTERNAL EFFECTS to REDRIVE OR COMPENSATE to VERIFY to CLOSE. A RUNBOOK beside it lists OWNER, ACCESS, COMMANDS, SAFETY CHECKS, ROLLBACK, EVIDENCE. Teal RECEIPT CHAIN follows every action.

Accessibility alt text: An operational recovery flow moves from alert through triage, reconciliation, controlled redrive or compensation, verification, and closure, guided by an owned runbook and receipt chain.

## Diagram 148 - Capstone: the Acme Case Resolution Network

Output filename: `diagrams/148-acme-case-resolution-network.png`

Pattern status: Framework-neutral capstone architecture

Use case: scientific-educational. Asset type: 16:9 visual-course architecture explainer. Create a polished beginner-friendly durable-workflow diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan command and forward-work arrows, teal event, acknowledgement, receipt, checkpoint, and resume paths, white task or state cards, selective coral timeout, duplicate, denial, race, and compensation paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Create a complete left-to-right architecture titled ACME CASE RESOLUTION NETWORK. Lanes: 1 INTAKE AND IDENTITY, 2 WORKFLOW AND EVENT HISTORY, 3 QUEUES AND WORKERS, 4 SPECIALIST AGENTS VIA A2A 1.0, 5 HUMAN CONTROL, 6 SIDE EFFECTS AND RECEIPTS, 7 OBSERVABILITY AND RECOVERY. Show Maya's refund surviving timeout and completing once. Keep labels crisp.

Accessibility alt text: The complete Acme network connects intake, durable workflow history, queues, specialist A2A tasks, human approval, idempotent side effects, receipts, observability, and recovery into one case journey.
