# MCP · ACP · A2A · RAG Visual Diagram Library

This library contains 30 reusable 16:9 explainers. The diagrams are ordered as a visual course, but each one also works as a standalone slide, lesson opener, interview aid, or architecture-review prompt.

## Design system

- Format: landscape 16:9 PNG.
- Visual language: premium 3D isometric educational infographic.
- Background: dark midnight navy.
- System stages: luminous cobalt-blue floating platforms.
- Forward work: cyan arrows.
- Results, artifacts, and receipts: teal arrows.
- Risk, rejection, retired concepts, and approval gates: coral/orange.
- Contracts and evidence: white rounded cards.
- Text: large uppercase white labels; no logo, watermark, or decorative paragraph text.

## Reusable base prompt

> Create a polished premium 16:9 educational explainer diagram in a consistent 3D isometric visual language: dark midnight navy background, luminous cobalt-blue floating platforms, cyan and teal flow arrows, white rounded panels, coral/orange for warnings and approval gates, subtle shadows and glows, clean spacious composition, crisp large uppercase white labels, friendly neutral agent icons, no logo, no watermark, and no small paragraph text. Use one unambiguous visual flow and spell every requested label exactly.

Append one of the scene prompts below to the base prompt. Diagrams 03–30 were created with the built-in image-generation mode; the original diagrams 01 and 02 were also used as style references for most of the generated series.

## Module 1 — See the whole system

### 01 — `01-agent-architecture.png`

Use: opening architecture slide.

Scene prompt: Show five connected stages—PERSON, APPLICATION AGENT, MCP CAPABILITIES, A2A SPECIALIST, DOMAIN + POLICY—with a forward work route and a returning audit/receipt route.

### 02 — `02-safe-side-effect.png`

Use: explain safe writes and retries.

Scene prompt: Show CONFIRM, AUTHORIZE, IDEMPOTENCY KEY, and CHANGE + RECEIPT + SAFE RETRY as a four-stage safety pipeline. Use coral for denied actions and teal for the committed receipt.

### 03 — `03-modern-agent-system-map.png`

Use: show how all the acronyms fit together.

Scene prompt: Arrange USER, APP AGENT, RAG KNOWLEDGE, MCP CAPABILITIES, A2A TEAM, and DOMAIN + POLICY as one coordinated agent system.

### 04 — `04-choose-the-boundary.png`

Use: protocol-selection decision tree.

Scene prompt: Start with WHAT OWNS THE WORK? and branch to LOCAL FUNCTION, RAG, MCP, and A2A, with DOMAIN + POLICY ALWAYS underneath.

### 05 — `05-request-journey.png`

Use: end-to-end request review.

Scene prompt: Show a six-stage journey labeled 1 ASK, 2 PLAN, 3 RETRIEVE, 4 ACT, 5 DELEGATE, 6 VERIFY.

### 06 — `06-protocol-comparison.png`

Use: interview-ready acronym comparison.

Scene prompt: Create four large panels labeled RAG = KNOWLEDGE, MCP = CAPABILITIES, A2A = AGENT WORK, and ACP = HISTORY.

## Module 2 — MCP capabilities

### 07 — `07-mcp-capability-discovery.png`

Use: capability discovery lesson.

Scene prompt: Show a left-to-right flow labeled 1 CLIENT, 2 SERVER / DISCOVER, 3 CAPABILITY CATALOG, 4 CALL.

### 08 — `08-mcp-primitives.png`

Use: server-catalog design.

Scene prompt: Create three equal panels labeled TOOLS = DO, RESOURCES = READ, and PROMPTS = GUIDE, each with a distinct intuitive icon.

### 09 — `09-stateless-mcp.png`

Use: replace handshake-era assumptions.

Scene prompt: Show REQUEST 1: COMPLETE and REQUEST 2: COMPLETE as independent self-contained deliveries, with a clear NO SESSION MEMORY statement beneath them.

### 10 — `10-modern-mcp-request.png`

Use: read the wire envelope.

Scene prompt: Layer VERSION HEADER with 2026-07-28, METHOD HEADER with tools/list, JSON-RPC BODY, and PER-REQUEST META as one complete modern request.

### 11 — `11-durable-mcp-task.png`

Use: long-running MCP work.

Scene prompt: Show 1 START TASK, 2 TASK ID, 3 PROGRESS, and 4 RESULT as an explicit durable-work lifecycle.

### 12 — `12-mcp-security-gates.png`

Use: production API security review.

Scene prompt: Show five gates labeled AUTHENTICATE, AUTHORIZE, VALIDATE, RATE LIMIT, and AUDIT.

## Module 3 — RAG evidence

### 13 — `13-rag-ingestion-pipeline.png`

Use: knowledge-pipeline planning.

Scene prompt: Show 1 SOURCES, 2 CLEAN, 3 CHUNK, 4 EMBED, 5 INDEX as a left-to-right ingestion pipeline.

### 14 — `14-rag-answer-pipeline.png`

Use: debug an answer path.

Scene prompt: Show 1 QUESTION, 2 SEARCH, 3 RERANK, 4 CONTEXT, 5 ANSWER as a left-to-right grounded-generation pipeline.

### 15 — `15-rag-chunk-size.png`

Use: teach chunk-size tradeoffs.

Scene prompt: Create three panels—TOO SMALL with fragmented text, JUST RIGHT with one coherent idea and overlap, TOO LARGE with several unrelated ideas—and make the middle option clearly best.

### 16 — `16-hybrid-search.png`

Use: retrieval-quality explanation.

Scene prompt: Run KEYWORD SEARCH and VECTOR SEARCH in parallel, combine them at MERGE, then order the final candidates at RERANK.

### 17 — `17-grounded-citations.png`

Use: evidence and citation review.

Scene prompt: Show EVIDENCE flowing into ANSWER, each claim connecting to numbered CITATIONS, and a final human-readable VERIFY stage.

### 18 — `18-rag-evaluation-loop.png`

Use: evaluation and regression testing.

Scene prompt: Create a circular loop labeled RETRIEVAL, FAITHFULNESS, COVERAGE, LATENCY, and IMPROVE.

## Module 4 — A2A collaboration

### 19 — `19-agent-card-discovery.png`

Use: discovery and trust review.

Scene prompt: Show four stages—DISCOVER CARD, CHECK INTERFACE, CHECK SECURITY, TRUST DECISION—with approved and blocked allowlist routes.

### 20 — `20-a2a-task-lifecycle.png`

Use: core A2A object model.

Scene prompt: Show a five-stage flow labeled 1 MESSAGE, 2 TASK, 3 WORKING, 4 ARTIFACT, 5 COMPLETED.

### 21 — `21-a2a-delegation.png`

Use: bounded delegation design.

Scene prompt: Show CALLER AGENT creating a TASK, sending it to SPECIALIST AGENT across a protocol bridge, then receiving an ARTIFACT, with DOMAIN + POLICY remaining local to the caller.

### 22 — `22-a2a-interaction-modes.png`

Use: client-progress design.

Scene prompt: Create four panels labeled WAIT, STREAM, POLL, and PUSH. Show one final reply, ordered progress events, repeated task-status checks, and a webhook notification respectively.

### 23 — `23-a2a-security-gates.png`

Use: least-privilege delegation review.

Scene prompt: Show MINIMIZE CONTEXT, ALLOWLIST AGENT, BIND TASK, VALIDATE ARTIFACT, and LOCAL APPROVAL as a five-stage security pipeline.

### 24 — `24-incident-response-team.png`

Use: multi-agent orchestration example.

Scene prompt: Arrange TRIAGE AGENT, LOG AGENT, SECURITY AGENT, and REMEDIATION AGENT around one incident task hub. Route evidence and artifacts to HUMAN COMMANDER for final review and approval.

## Module 5 — ACP migration

### 25 — `25-acp-to-a2a-timeline.png`

Use: correct an older ACP-first course.

Scene prompt: Create a historical river/timeline labeled ACP IDEAS, MERGED INTO A2A, A2A 1.0, BUILD HERE. Use coral for the older branch and teal for the modern construction platform.

### 26 — `26-acp-a2a-concept-map.png`

Use: migration inventory.

Scene prompt: Create five old-to-current mappings: MANIFEST → AGENT CARD, RUN → TASK, INPUT → MESSAGE, OUTPUT → ARTIFACT, STATUS → TASK STATE. Label the sides OLD TERMS and CURRENT MODEL.

## Module 6 — End-to-end use cases

### 27 — `27-customer-support.png`

Use: support-agent architecture.

Scene prompt: Show CUSTOMER, RAG POLICY, MCP TICKETS, A2A SPECIALIST, SAFE RESOLUTION. Add a coral approval gate before refunds or account changes and a returning receipt arrow.

### 28 — `28-research-analyst.png`

Use: evidence-first research architecture.

Scene prompt: Show QUESTION, RAG EVIDENCE, MCP DATA, A2A REVIEWER, CITED REPORT, with source markers and a verify-and-refine return path.

### 29 — `29-software-maintenance.png`

Use: software-agent architecture.

Scene prompt: Show ISSUE, RAG CODEBASE, MCP TOOLS, A2A TEST AGENT, REVIEWED PATCH, including a failing test in coral and human-controlled merge in teal.

### 30 — `30-loan-document-review.png`

Use: high-stakes human-decision architecture.

Scene prompt: Show APPLICATION, RAG RULES, MCP SYSTEMS, A2A RISK REVIEW, HUMAN DECISION. Make it explicit that agents supply evidence and a recommendation while the human approves or declines.

## Teaching sequence

1. Start with diagrams 03, 04, and 06 until the boundary choices feel automatic.
2. Teach MCP with 07–12, then point to the same boundary in a running server.
3. Teach RAG with 13–18 and evaluate one real question set.
4. Teach A2A with 19–24, emphasizing task ownership and local trust.
5. Use 25–26 whenever older ACP material appears.
6. Finish by choosing one of 27–30 and implementing it in both technology stacks.

