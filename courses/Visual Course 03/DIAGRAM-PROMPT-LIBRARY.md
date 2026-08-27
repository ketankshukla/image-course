# Volume 3 Diagram Prompt Library

These prompts reproduce the visual intent of Diagrams 47-76. Generated text and layout should be checked by a person before publication.

## Shared art direction

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

## Diagram 47 - A stateless MCP request

Output filename: `diagrams/47-stateless-mcp-request.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a left-to-right request journey with exact labels CLIENT REQUEST, MCP GATEWAY, ANY SERVER, DOMAIN RESULT. Put one white request card under CLIENT REQUEST labeled VERSION, CLIENT INFO, CAPABILITIES. Behind MCP GATEWAY show three interchangeable server instances, with a round-robin arrow reaching any one of them and no session store. Use a teal result path returning to the client.

Accessibility alt text: A self-contained MCP request crosses a gateway and can reach any interchangeable server instance before a domain result returns, with no protocol session store.

## Diagram 48 - Multi Round-Trip Requests

Output filename: `diagrams/48-multi-round-trip-request.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a five-stage loop with exact labels TOOL CALL, INPUT REQUIRED, USER ANSWER, RETRY CALL, FINAL RESULT. Show TOOL CALL reaching a server, then a coral pause at INPUT REQUIRED with a question card. A person supplies USER ANSWER. RETRY CALL carries INPUT RESPONSES and REQUEST STATE back to any server. A teal path returns FINAL RESULT.

Accessibility alt text: A tool call pauses with input required, a person supplies an answer, and the original call is retried with input responses and request state before a final result returns.

## Diagram 49 - The MCP Tasks extension

Output filename: `diagrams/49-mcp-tasks-extension.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a task lifecycle with exact labels TOOL CALL, TASK HANDLE, WORKING, INPUT REQUIRED, COMPLETED, FAILED, CANCELED. Show the server deciding that long work becomes a task. Put TASKS GET, TASKS UPDATE, TASKS CANCEL on three small control cards and SUBSCRIPTIONS LISTEN on a teal update stream. Keep failure and cancellation coral.

Accessibility alt text: A long MCP tool call becomes an explicit task handle that can be checked, updated, canceled, observed, and completed with a durable result.

## Diagram 50 - Routing, caching, and gateways

Output filename: `diagrams/50-mcp-routing-and-cache.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a gateway diagram. On the left show MCP REQUEST with exact header cards MCP-METHOD and MCP-NAME. In the center show GATEWAY with ROUTE, AUTHORIZE, RATE LIMIT, TRACE. On the right show TOOL SERVER, RESOURCE SERVER, PROMPT SERVER. Along the bottom show LIST RESPONSE returning with TTL MS and CACHE SCOPE into CLIENT CACHE. Add a coral mismatch path labeled HEADER BODY MISMATCH.

Accessibility alt text: MCP method and name headers let a gateway route and protect calls, while list responses use TTL and cache scope to tell clients when cached catalogs remain safe.

## Diagram 51 - The modern MCP migration map

Output filename: `diagrams/51-mcp-migration-map.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a two-column migration bridge. Left column exact heading RETIRED OR DEPRECATED with cards INITIALIZE, SESSION ID, ROOTS, SAMPLING, LOGGING, LEGACY HTTP PLUS SSE, DCR. Right column exact heading MODERN PATH with cards SELF DESCRIBING REQUESTS, SERVER DISCOVER, MRTR, EXTENSIONS, STREAMABLE HTTP, CIMD. Use coral arrows leaving the old column and teal arrows entering the modern column. Put TEST BOTH VERSIONS at the bridge.

Accessibility alt text: A migration bridge moves an older MCP implementation away from initialize and session behavior, deprecated primitives, legacy transport, and DCR toward self-describing requests, discovery, MRTR, extensions, Streamable HTTP, and CIMD.

## Diagram 52 - Conversation state versus workflow state

Output filename: `diagrams/52-conversation-vs-workflow-state.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create two clearly separated lanes. Top lane exact heading CONVERSATION STATE with CHAT HISTORY, CURRENT QUESTION, DISPLAY TEXT and a fading clock icon. Bottom lane exact heading WORKFLOW STATE with CASE ID, ACTION STATUS, RECEIPT, OWNER and a durable database icon. Show the AGENT reading both lanes but only DOMAIN SERVICE writing business truth. Add a coral warning labeled CHAT IS NOT A DATABASE.

Accessibility alt text: Conversation state holds temporary dialogue while workflow state stores durable case identity, action status, ownership, and receipts under domain control.

## Diagram 53 - Checkpoints and resume

Output filename: `diagrams/53-checkpoint-and-resume.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a left-to-right durable workflow with exact labels START, STEP 1, CHECKPOINT A, STEP 2, CHECKPOINT B, CRASH, RESUME, COMPLETE. Show white checkpoint cards stored in a database below the main path. Use a coral arrow from STEP 2 to CRASH and a teal arrow from the latest valid checkpoint to RESUME, skipping completed work.

Accessibility alt text: A durable workflow saves checkpoints after meaningful steps so a crash can resume from the latest valid state instead of repeating all prior work.

## Diagram 54 - Retries and idempotency

Output filename: `diagrams/54-retry-and-idempotency.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a retry-safe write diagram. Exact labels USER INTENT, IDEMPOTENCY KEY, FIRST ATTEMPT, TIMEOUT, RETRY, DOMAIN GATE, ONE RECEIPT. Show FIRST ATTEMPT and RETRY carrying the same key into DOMAIN GATE. The first accepted path creates ONE RECEIPT; the duplicate path returns the same receipt in teal. Add a coral blocked symbol labeled NO SECOND WRITE.

Accessibility alt text: A first attempt and a retry carry the same idempotency key through a domain gate, producing one business write and one reusable receipt rather than a duplicate action.

## Diagram 55 - Queues, parallel work, and joins

Output filename: `diagrams/55-queues-parallel-work-and-joins.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a fan-out and join diagram. Exact labels ORCHESTRATOR, QUEUE, BANK CHECK, POLICY CHECK, TICKET CHECK, JOIN GATE, DECISION. Show ORCHESTRATOR placing three independent work cards on QUEUE. Cyan arrows fan out to the three checks. Teal result cards converge at JOIN GATE. Add coral branches labeled TIMEOUT and FAILED PART, and show DECISION only after the join rule is satisfied.

Accessibility alt text: An orchestrator fans independent checks through a queue, gathers their results at a controlled join gate, and makes a decision only when the required join rule is satisfied.

## Diagram 56 - Timeouts, cancellation, and compensation

Output filename: `diagrams/56-timeout-cancel-and-compensate.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a control-flow diagram with exact labels START WORK, DEADLINE, STILL RUNNING, CANCEL REQUEST, STOP NEW WORK, CHECK SIDE EFFECTS, COMPENSATE, FINAL STATE. Use coral for timeout and cancellation controls. Branch CHECK SIDE EFFECTS to NOTHING HAPPENED or PARTIAL CHANGE. Route PARTIAL CHANGE through COMPENSATE and end with a white receipt card.

Accessibility alt text: A deadline triggers cancellation, stops new work, checks whether side effects occurred, and compensates any partial change before recording a final state and receipt.

## Diagram 57 - The context budget

Output filename: `diagrams/57-context-budget.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a horizontal capacity meter labeled CONTEXT BUDGET. Divide it into exact labeled sections INSTRUCTIONS, USER REQUEST, HISTORY, EVIDENCE, TOOL RESULTS, RESPONSE. Above it show a funnel labeled SELECT AND COMPRESS. Add a coral overflow bin labeled IRRELEVANT OR STALE and a teal protected card labeled MUST KEEP.

Accessibility alt text: A fixed context budget is deliberately divided among instructions, the current request, history, evidence, tool results, and the response after irrelevant or stale material is removed.

## Diagram 58 - Short-term and durable memory

Output filename: `diagrams/58-short-term-and-durable-memory.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create three storage tiers around an AGENT. Exact labels WORKING MEMORY, USER PREFERENCE, BUSINESS RECORD. Under them place TEMPORARY, RECALLABLE, AUTHORITATIVE. Show a coral gate labeled CONSENT AND POLICY before writing USER PREFERENCE. Show DOMAIN SERVICE as the only writer to BUSINESS RECORD. Add delete and expiry icons to memory stores.

Accessibility alt text: An agent separates temporary working memory, consented user preferences, and authoritative business records, with different owners, retention rules, and deletion paths.

## Diagram 59 - The advanced retrieval pipeline

Output filename: `diagrams/59-advanced-retrieval-pipeline.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create an eight-stage RAG pipeline with exact labels QUESTION, REWRITE, FILTER, HYBRID SEARCH, RERANK, ASSEMBLE EVIDENCE, ANSWER, CITE. Under HYBRID SEARCH show KEYWORD plus VECTOR. Add a coral branch from FILTER labeled NOT PERMITTED and a teal feedback loop from weak evidence to REWRITE. Keep each stage on a cobalt platform.

Accessibility alt text: A RAG question is rewritten, permission-filtered, searched with keyword and vector methods, reranked, assembled into evidence, answered, and cited with a feedback loop for weak evidence.

## Diagram 60 - Freshness and index versions

Output filename: `diagrams/60-freshness-and-index-versions.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a versioned knowledge flow. Exact labels SOURCE VERSION, INGESTION RUN, INDEX VERSION, RETRIEVAL, ANSWER RECORD. Show SOURCE V7 entering INGESTION RUN 42 and producing INDEX V42. Put a coral card SOURCE V8 AVAILABLE beside a freshness checker. The answer record must display SOURCE V7, INDEX V42, CHECKED TIME. Add a teal reindex path to INDEX V43.

Accessibility alt text: A RAG answer records the source version, ingestion run, index version, and checked time, while a freshness signal triggers reindexing when a newer source appears.

## Diagram 61 - Conflict, citation, and abstention

Output filename: `diagrams/61-conflict-citation-and-abstention.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create an evidence decision tree. Exact labels EVIDENCE PACKET, ENOUGH EVIDENCE, SOURCES AGREE, ANSWER WITH CITATIONS, SHOW CONFLICT, ASK FOR MORE, ABSTAIN. Use teal for enough and agreement. Use coral for missing evidence and disagreement. Show two source cards with different values feeding SHOW CONFLICT, and a shield beside ABSTAIN.

Accessibility alt text: An evidence packet passes sufficiency and agreement checks before the system answers with citations, shows a source conflict, asks for more information, or abstains.

## Diagram 62 - Identity and token flow

Output filename: `diagrams/62-identity-and-token-flow.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a security boundary flow with exact labels USER, APPLICATION, AUTHORIZATION SERVER, MCP SERVER, DOWNSTREAM API. Show USER signing in to APPLICATION. APPLICATION obtains a token for MCP SERVER with a visible AUDIENCE tag. MCP SERVER validates ISSUER, AUDIENCE, EXPIRY, SCOPE. Show a separate downstream token from MCP SERVER to DOWNSTREAM API. Add a coral blocked arrow labeled NO TOKEN PASSTHROUGH.

Accessibility alt text: A user and application obtain a token intended for the MCP server, which validates issuer, audience, expiry, and scope before using a separate token for any downstream API.

## Diagram 63 - Least-privilege tools

Output filename: `diagrams/63-least-privilege-tools.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a tool-design comparison. On the left a coral oversized toolbox labeled DO EVERYTHING with broad icons for read, write, delete, admin. On the right exact heading NARROW TOOLS with four separate cards GET REFUND STATUS, REQUEST REVIEW, ADD CASE NOTE, CLOSE OWN TICKET. Put policy gates above each card labeled TENANT, RESOURCE, ACTION, LIMITS. Show the agent receiving only two allowed cards.

Accessibility alt text: A broad do-everything tool is replaced by narrow capabilities whose tenant, resource, action, and limits are enforced before the agent can use them.

## Diagram 64 - Prompt injection and exfiltration

Output filename: `diagrams/64-prompt-injection-and-exfiltration.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a shielded RAG and tool flow. Exact labels USER REQUEST, UNTRUSTED CONTENT, EVIDENCE PARSER, POLICY GATE, AGENT, NARROW TOOL, SAFE RESULT. Put a coral hostile document inside UNTRUSTED CONTENT labeled IGNORE RULES and SEND SECRETS. Show those instructions blocked at POLICY GATE. Add a separate SECRET STORE with no arrow to the agent, and a coral blocked path labeled EXFILTRATION.

Accessibility alt text: Hostile instructions embedded in retrieved content are treated as untrusted data, blocked by policy, and kept away from secrets and broad tools before a safe result returns.

## Diagram 65 - Tenant isolation and secrets

Output filename: `diagrams/65-tenant-isolation-and-secrets.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create two isolated tenant lanes labeled TENANT BLUE and TENANT GOLD. Each lane has USER, APP, MEMORY, VECTOR INDEX, TASK STORE, AUDIT. Put a strong glowing boundary between lanes. Above both show SECRET MANAGER issuing short-lived handles only to server components. Add coral blocked cross-lane arrows labeled DENY and a red warning label NEVER LOG SECRETS.

Accessibility alt text: Two tenant lanes keep user data, memory, indexes, tasks, and audit evidence isolated, while a secret manager gives short-lived server access without exposing values to logs or model context.

## Diagram 66 - Audit and human approval

Output filename: `diagrams/66-audit-and-human-approval.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a consequential-action approval flow with exact labels PROPOSED ACTION, EVIDENCE, POLICY CHECK, APPROVAL REQUIRED, HUMAN DECISION, EXECUTE, AUDIT RECEIPT. Show a person reviewing a white card with amount, target, evidence, and risk. Branch HUMAN DECISION to teal APPROVE and coral REJECT. The receipt should list WHO, WHAT, WHEN, POLICY, RESULT.

Accessibility alt text: A consequential action gathers evidence, passes policy, pauses for a human decision, executes only after approval, and produces an audit receipt naming who, what, when, policy, and result.

## Diagram 67 - Follow one request end to end

Output filename: `diagrams/67-one-request-observability-trace.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create one horizontal distributed trace labeled TRACE RF-2048. Show spans USER REQUEST, NEXT.JS API, AGENT PLAN, MCP TOOL, A2A SPECIALIST, VECTOR SEARCH, PAYMENT API, RESPONSE. Give each span a small duration bar and shared TRACE ID. Under the trace show correlated LOGS, METRICS, COST, ERROR. Use coral on one slow span and teal on the final response.

Accessibility alt text: One shared trace follows refund request RF-2048 across the Next.js API, agent, MCP tool, A2A specialist, retrieval, payment service, and response while linking logs, metrics, cost, and errors.

## Diagram 68 - Golden datasets and an evaluation harness

Output filename: `diagrams/68-golden-datasets-and-eval-harness.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a loop with exact labels REAL CASES, REDACT AND CURATE, GOLDEN DATASET, RUN SYSTEM, SCORE OUTPUT, REVIEW FAILURES, ADD REGRESSION CASES. Show sample cards NORMAL, EDGE, ADVERSARIAL, ABSTAIN. Add a white scorecard labeled CORRECT, GROUNDED, SAFE, COMPLETE, USEFUL and a teal arrow returning improved cases to the dataset.

Accessibility alt text: Real support cases become a redacted golden dataset containing normal, edge, adversarial, and abstention examples; an evaluation loop runs the system, scores five qualities, reviews failures, and adds regression cases.

## Diagram 69 - Measure quality at every stage

Output filename: `diagrams/69-stage-by-stage-quality-metrics.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a six-stage pipeline labeled UNDERSTAND, RETRIEVE, PLAN, TOOL, SYNTHESIZE, DELIVER. Put a small scorecard beneath each: ROUTE ACCURACY, RECALL AND PRECISION, PLAN VALIDITY, TOOL SUCCESS, GROUNDEDNESS, USER OUTCOME. Add an END-TO-END SCORE above the pipeline and coral failure markers showing that one final failure can originate at different stages.

Accessibility alt text: A six-stage agent pipeline has a local quality measure at every step plus one end-to-end outcome, revealing whether a failure began in routing, retrieval, planning, a tool, synthesis, or delivery.

## Diagram 70 - Latency and cost budgets

Output filename: `diagrams/70-latency-and-cost-budgets.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a horizontal 10 SECOND REQUEST BUDGET split into ROUTING 0.3S, RETRIEVAL 1.2S, MODEL 2.5S, TOOLS 3.0S, SPECIALIST 2.0S, UI 1.0S. Below it show a COST BUDGET with MODEL TOKENS, SEARCH, TOOL CALLS, STORAGE. Add coral budget alerts, a teal FAST PATH, a blue DEEP PATH, and a small decision gate labeled VALUE JUSTIFIES COST?

Accessibility alt text: A ten-second request budget and a separate cost budget allocate limits to routing, retrieval, models, tools, specialist work, and the interface, with fast and deep paths chosen by expected value.

## Diagram 71 - Red-team and incident learning loop

Output filename: `diagrams/71-red-team-and-incident-learning-loop.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a circular reliability loop labeled THREAT MODEL, ATTACK TESTS, DETECT, CONTAIN, INVESTIGATE, FIX, REGRESSION TEST, RELEASE SAFELY. Feed REAL INCIDENT and NEAR MISS cards into INVESTIGATE. Show coral attack paths for INJECTION, EXCESSIVE ACTION, DATA LEAK, CROSS-TENANT, RETRY DUPLICATE and teal verified controls returning to RELEASE SAFELY.

Accessibility alt text: Threat modeling, attack tests, detection, containment, investigation, fixes, and regression tests form a learning loop fed by incidents and near misses before a safer release.

## Diagram 72 - MCP, A2A, and AG-UI together

Output filename: `diagrams/72-mcp-a2a-and-agui-together.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create three connected ownership lanes. Top lane AG-UI labeled USER EXPERIENCE with USER, REACT APP, EVENTS, SHARED STATE, INTERRUPTS. Middle lane A2A labeled AGENT COLLABORATION with ORCHESTRATOR AGENT, SPECIALIST AGENT, TASK, ARTIFACT. Bottom lane MCP labeled TOOLS AND CONTEXT with MCP CLIENT, MCP SERVER, TOOL, RESOURCE. Use cyan arrows downward for requests and teal arrows upward for results. Add three white cards: USER SEES PROGRESS, AGENTS SHARE WORK, TOOLS DO BOUNDED ACTIONS.

Accessibility alt text: Three stacked lanes give AG-UI responsibility for the live user experience, A2A responsibility for agent collaboration and task artifacts, and MCP responsibility for bounded tools and context.

## Diagram 73 - The typed agent event stream

Output filename: `diagrams/73-typed-agent-event-stream.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a left-to-right event timeline labeled RUN STARTED, STEP STARTED, TEXT DELTA, TOOL CALL STARTED, TOOL CALL RESULT, STATE SNAPSHOT, ARTIFACT READY, RUN FINISHED. Under it show a REACT REDUCER turning events into CHAT, PROGRESS, TOOL CARD, STATE PANEL, ARTIFACT CARD. Add EVENT ID and RUN ID tags and a coral RECONNECT arrow resuming AFTER LAST EVENT.

Accessibility alt text: A typed event timeline with run and event IDs drives React views for chat, progress, tools, shared state, and artifacts, while reconnection resumes after the last applied event.

## Diagram 74 - Progress, artifacts, and recovery UX

Output filename: `diagrams/74-progress-artifacts-and-recovery-ux.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a three-column agent interface blueprint. Column one LIVE PROGRESS has steps UNDERSTANDING, CHECKING POLICY, VERIFYING PAYMENT, PREPARING RESULT. Column two ARTIFACTS has EVIDENCE PACK, DECISION SUMMARY, AUDIT RECEIPT. Column three RECOVERY has RETRY SAFE STEP, CONTINUE TASK, CHANGE INPUT, CONTACT HUMAN. Add a coral PARTIAL FAILURE between progress and recovery, plus a teal COMPLETED EARLIER badge on preserved artifacts.

Accessibility alt text: A user interface separates live progress, durable artifacts, and recovery choices so a partial failure preserves completed work and offers a safe next step.

## Diagram 75 - Interrupts, approval, and human steering

Output filename: `diagrams/75-interrupts-approval-and-steering.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create an active run flowing from PLAN to CHECK POLICY to PAUSE. At PAUSE show a large APPROVAL CARD with PROPOSED ACTION, EVIDENCE, RISK, EXPIRES, APPROVE, REJECT, EDIT. Add separate steering controls ADD CONTEXT, CHANGE PRIORITY, CANCEL. Then show REVALIDATE leading to RESUME or coral INVALIDATE AND REPLAN. Include a white card labeled NEW INPUT NEVER SILENTLY REWRITES COMPLETED ACTIONS.

Accessibility alt text: An active run pauses on an approval card, accepts explicit approval or steering, revalidates changed state, and either resumes or creates a new plan without silently rewriting completed actions.

## Diagram 76 - Production capstone: Acme Agent Desk

Output filename: `diagrams/76-production-capstone-architecture.png`

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a polished complete architecture map titled only ACME AGENT DESK. Left: USER and NEXT.JS REACT EXPERIENCE with AG-UI EVENTS, AUTH, APPROVALS, ARTIFACTS. Center: ORCHESTRATOR, DURABLE WORKFLOW, POLICY GATE, MEMORY AND RAG, EVALS, OBSERVABILITY. Right: A2A PAYMENT SPECIALIST with TASKS AND ARTIFACTS, plus MCP SERVERS POLICY, CASES, BANKING with narrow TOOLS. Bottom: POSTGRES, VECTOR INDEX, QUEUE, ARTIFACT STORE, SECRET MANAGER, AUDIT STORE. Use cyan request paths, teal results, coral denials and human control. Add PYTHON FASTAPI CORE and VERCEL DEPLOYMENT labels without any other branding.

Accessibility alt text: The complete Acme Agent Desk joins a Next.js and React experience, AG-UI events, a Python and FastAPI core, durable workflows, policy and RAG, A2A specialist tasks, narrow MCP servers, governed storage, evaluations, and observability.
