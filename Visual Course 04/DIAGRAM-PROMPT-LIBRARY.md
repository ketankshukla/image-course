# Volume 4 Diagram Prompt Library

These are the exact production prompts for Diagrams 77-100. The built-in image generator was used in standard generation mode. Generated labels and layouts were visually checked before publication.

## Shared art direction

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

## Diagram 77 - Normative rules versus examples

Output filename: `diagrams/77-normative-rules-map.png`

Specification status: Stable foundation

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show a three-lane specification map. Left white cards say MUST, SHOULD, MAY. The center lane says CONFORMANCE TESTS. The right lane says EXAMPLES and IMPLEMENTATION CHOICES. A coral divider labeled NOT A REQUIREMENT separates examples from tests.

Accessibility alt text: A protocol specification separates binding requirement words from examples and local implementation choices, with conformance tests derived only from actual requirements.

## Diagram 78 - Version, capability, and extension negotiation

Output filename: `diagrams/78-version-capability-extension-negotiation.png`

Specification status: Stable pattern

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show CLIENT and SERVER platforms exchanging three white cards in order: VERSION, CAPABILITIES, EXTENSIONS. Put a green COMPATIBLE PATH leading to USE SHARED FEATURES and a coral NO COMMON VERSION path leading to CLEAR ERROR. Include no session box.

Accessibility alt text: A client and server compare version, core capabilities, and optional extensions before using only the features they share.

## Diagram 79 - Requests, results, errors, metadata, and correlation

Output filename: `diagrams/79-request-result-error-correlation.png`

Specification status: Stable JSON-RPC foundation

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create an exploded JSON-RPC envelope. White cards labeled JSONRPC 2.0, ID 2048, METHOD, PARAMS travel from CLIENT to SERVER. Return paths split into RESULT or ERROR, both carrying ID 2048. A separate dotted TRACE ID crosses gateway, worker, and database.

Accessibility alt text: A JSON-RPC request and its result or error share one protocol ID, while separate correlation metadata follows the wider distributed operation.

## Diagram 80 - Build a conformance matrix

Output filename: `diagrams/80-conformance-matrix.png`

Specification status: Engineering practice

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show a large grid with columns REQUIREMENT, HAPPY PATH, NEGATIVE TEST, EVIDENCE, STATUS. Rows R-01 through R-04 have green PASS, coral FAIL, and amber NOT TESTED chips. Arrows connect SPEC to TEST SUITE to REPORT.

Accessibility alt text: A conformance matrix links every important protocol requirement to positive and negative tests, evidence, and an honest status.

## Diagram 81 - Stateless MCP routing and per-request identity

Output filename: `diagrams/81-stateless-http-routing.png`

Specification status: Stable MCP 2026-07-28 core

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show HTTP CLIENT sending one self-contained MCP REQUEST through ROUTER to three interchangeable MCP SERVER instances. The request card lists VERSION, CLIENT INFO, CAPABILITIES; headers above say MCP-METHOD and MCP-NAME. Cross out SESSION STORE and STICKY ROUTING.

Accessibility alt text: A self-contained MCP request carries the context needed for routing and capability decisions and can reach any healthy server instance.

## Diagram 82 - Server discovery, versions, and capabilities

Output filename: `diagrams/82-server-discovery-negotiation.png`

Specification status: Stable MCP 2026-07-28 core

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show CLIENT calling SERVER DISCOVER and receiving a white SERVER CARD with VERSION, CAPABILITIES, EXTENSIONS, ENDPOINT INFO. A separate DIRECT REQUEST bypasses discovery but still carries per-request metadata. Both paths meet at VALIDATION.

Accessibility alt text: MCP server discovery can describe a server before use, while every actual request still validates its own version and supported features.

## Diagram 83 - Tools, resources, prompts, and catalog scale

Output filename: `diagrams/83-mcp-primitives-catalog-scale.png`

Specification status: Stable MCP core; progressive discovery is a roadmap direction

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show MCP SERVER at center feeding three distinct platforms labeled TOOLS, RESOURCES, PROMPTS. Each has a white contract card: EXECUTE, READ CONTEXT, REUSABLE TEMPLATE. A large CATALOG passes through SEARCH, FILTER, PAGE before reaching CLIENT.

Accessibility alt text: MCP tools, resources, and prompts have different jobs, and large catalogs need bounded discovery instead of dumping everything into model context.

## Diagram 84 - Cache hints, subscriptions, extensions, and deprecation

Output filename: `diagrams/84-cache-subscription-extension-policy.png`

Specification status: Stable core plus negotiated extensions

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create four lanes from MCP SERVER: CACHE RESULT with TTL and SCOPE card, SUBSCRIPTIONS LISTEN with event types, EXTENSION MAP with reverse-domain IDs, DEPRECATION RAMP with OLD to NEW and a coral removal date. All lanes pass through POLICY GATE.

Accessibility alt text: Caching, notifications, extensions, and deprecation each need explicit scope, negotiation, and lifecycle rules.

## Diagram 85 - Multi Round-Trip Requests and input-required results

Output filename: `diagrams/85-mrtr-input-required-loop.png`

Specification status: Stable MCP 2026-07-28 core

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show CLIENT calling TOOL REQUEST. SERVER returns RESULT TYPE INPUT REQUIRED with two white REQUEST cards and REQUEST STATE. A HUMAN INPUT platform supplies INPUT RESPONSES. CLIENT retries ORIGINAL CALL and receives FINAL RESULT. Use a coral timeout branch.

Accessibility alt text: An MCP call can pause with an input-required result and continue when the caller retries the original call with requested answers and request state.

## Diagram 86 - The MCP Tasks extension lifecycle

Output filename: `diagrams/86-mcp-tasks-extension-lifecycle.png`

Specification status: Official opt-in MCP extension

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show a state machine with TASK HANDLE at center. States are WORKING, INPUT REQUIRED, COMPLETED, FAILED, CANCELED. Around it place CREATE FROM CALL, TASKS GET, TASKS UPDATE, TASKS CANCEL. Use teal artifact return and coral terminal failure paths.

Accessibility alt text: The MCP Tasks extension turns selected calls into durable, addressable work that can be inspected, updated, or canceled.

## Diagram 87 - Progress, subscriptions, polling, webhooks, and channels

Output filename: `diagrams/87-delivery-mechanism-map.png`

Specification status: Mixed core and implementation choices

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a decision map from UPDATE NEEDED to four delivery boxes: SAME RESPONSE PROGRESS, SUBSCRIPTIONS LISTEN, POLLING, WEBHOOK OR CHANNEL. Decision diamonds say CONNECTION OPEN, CLIENT CAN POLL, SERVER CAN CALL BACK. All paths write DURABLE TASK STATE first.

Accessibility alt text: Progress delivery is a view of durable state, and the right mechanism depends on connection lifetime, callback reachability, reliability, and user experience.

## Diagram 88 - MCP Apps, sandboxed interfaces, consent, and audit

Output filename: `diagrams/88-mcp-apps-sandbox-consent.png`

Specification status: Official MCP extension

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show MCP TOOL returning DATA and UI TEMPLATE to HOST. HOST PREFETCH AND REVIEW leads to SANDBOXED IFRAME. A USER CONSENT GATE sits before TOOL ACTION. All UI messages return through HOST AUDIT, never directly to secrets or network.

Accessibility alt text: An MCP App renders a declared interactive interface inside a host-controlled sandbox while tool calls, consent, and audit remain under host authority.

## Diagram 89 - Agent Cards, skills, interfaces, and signatures

Output filename: `diagrams/89-a2a-agent-card-trust.png`

Specification status: Stable A2A 1.0

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show CLIENT discovering an AGENT CARD. Explode the card into PROVIDER, CAPABILITIES, SKILLS, INTERFACES, EXTENSIONS, SECURITY, SIGNATURES. A TRUST POLICY gate selects one INTERFACE before MESSAGE SEND. A coral path rejects unknown issuer or algorithm.

Accessibility alt text: An A2A Agent Card advertises who an agent is, what it can do, how to reach it, and how a client can evaluate the claim before sending work.

## Diagram 90 - Messages, tasks, status, parts, and artifacts

Output filename: `diagrams/90-a2a-message-task-artifact-anatomy.png`

Specification status: Stable A2A 1.0

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create an anatomy diagram. USER MESSAGE contains PARTS: TEXT, FILE, DATA. It creates TASK with TASK ID, CONTEXT ID, STATUS, HISTORY. AGENT MESSAGE and ARTIFACTS return. Show status path SUBMITTED to WORKING to COMPLETED, with INPUT REQUIRED, AUTH REQUIRED, FAILED, CANCELED, REJECTED branches.

Accessibility alt text: A2A separates conversational messages from durable task state and the artifacts produced by that task.

## Diagram 91 - Streaming, push notifications, multi-turn work, and cancellation

Output filename: `diagrams/91-a2a-stream-push-cancel.png`

Specification status: Stable A2A 1.0

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show one A2A TASK feeding three update paths: OPEN STREAM with STATUS and ARTIFACT UPDATE events, PUSH WEBHOOK with signed callback, and GET TASK polling. A MULTI TURN MESSAGE returns to the same task. A coral CANCEL path races with COMPLETED and ends in one recorded terminal truth.

Accessibility alt text: A2A offers streaming, push, polling, follow-up messages, and cancellation around the same durable task contract.

## Diagram 92 - Bindings, versioning, security schemes, and interoperability

Output filename: `diagrams/92-a2a-bindings-version-security.png`

Specification status: Stable A2A 1.0

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show one CANONICAL A2A MODEL at center connected to JSON-RPC, GRPC, and HTTP PLUS JSON bindings. Each passes through FUNCTIONAL EQUIVALENCE tests. Above, headers A2A-VERSION and A2A-EXTENSIONS meet SECURITY SCHEMES: API KEY, HTTP AUTH, OAUTH2, OIDC, MTLS.

Accessibility alt text: A2A keeps one canonical meaning across multiple bindings while version, extensions, authentication, and error mappings remain explicit.

## Diagram 93 - The typed AG-UI run and event lifecycle

Output filename: `diagrams/93-agui-typed-event-lifecycle.png`

Specification status: Stable AG-UI event core

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show RUN STARTED opening a horizontal event stream. Inside are STEP STARTED and STEP FINISHED, TEXT MESSAGE START CONTENT END, TOOL CALL START ARGS END RESULT. The stream terminates at RUN FINISHED or coral RUN ERROR. IDs connect related event groups.

Accessibility alt text: AG-UI gives the frontend typed lifecycle, message, and tool-call events that can be reduced into an understandable interface.

## Diagram 94 - Snapshots, deltas, reconnects, replay, and idempotency

Output filename: `diagrams/94-agui-snapshot-delta-replay.png`

Specification status: Stable AG-UI snapshot-delta pattern; replay policy is implementation-specific

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show STATE SNAPSHOT as a full white board, followed by ordered STATE DELTA cards labeled RFC 6902. A NETWORK BREAK leads to RECONNECT, MESSAGES SNAPSHOT, REPLAY FROM SEQUENCE, DEDUPLICATE, CONSISTENT UI. A coral DIVERGENCE path requests FRESH SNAPSHOT.

Accessibility alt text: A frontend restores known state from snapshots, applies ordered deltas once, and requests a fresh snapshot when replay cannot prove consistency.

## Diagram 95 - Interrupts, resume payloads, expiry, steering, and approval

Output filename: `diagrams/95-agui-interrupt-approval-steering.png`

Specification status: Draft AG-UI interrupt-aware lifecycle; isolate behind an adapter

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show RUN FINISHED with OUTCOME INTERRUPT and two INTERRUPT cards. HUMAN REVIEW supplies RESUME PAYLOAD to NEW RUN STARTED with PARENT RUN ID. Side paths show EXPIRED, REJECTED, and STEERING MESSAGE. A bold amber DRAFT CONTRACT banner spans the visual.

Accessibility alt text: The draft AG-UI interrupt model pauses one run, gathers responses to every open interrupt, and resumes through a new related run with explicit lineage.

## Diagram 96 - Tool rendering, artifacts, errors, and recovery choices

Output filename: `diagrams/96-agui-tool-artifact-recovery.png`

Specification status: Stable events plus application UI policy

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show AG-UI EVENT REDUCER producing four UI cards: TOOL IN PROGRESS, TOOL RESULT, ARTIFACT READY, RUN ERROR. Each card has permitted actions: VIEW DETAILS, RETRY SAFE STEP, DOWNLOAD, EDIT INPUT, CONTACT SUPPORT. A coral branch blocks BLIND RETRY for effectful calls.

Accessibility alt text: A good agent interface turns typed events into honest status, durable artifacts, and recovery actions matched to the failure and side-effect risk.

## Diagram 97 - Choose MCP, A2A, AG-UI, or an internal function

Output filename: `diagrams/97-protocol-boundary-decision-tree.png`

Specification status: Architecture decision

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a decision tree starting WHO OWNS THE OTHER SIDE. Branch SAME PROCESS to INTERNAL FUNCTION, APP TO CAPABILITY SERVER to MCP, AGENT TO INDEPENDENT AGENT to A2A, AGENT TO USER INTERFACE to AG-UI. A coral warning says DO NOT STACK PROTOCOLS WITHOUT A REAL BOUNDARY.

Accessibility alt text: Choose a protocol from the ownership boundary and interaction contract, not because more protocols sound more advanced.

## Diagram 98 - Gateways, adapters, correlation IDs, and contract translation

Output filename: `diagrams/98-adapter-correlation-contract.png`

Specification status: Architecture and testing pattern

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Show AG-UI EVENT entering ORCHESTRATOR, then MCP ADAPTER to POLICY SERVER and A2A ADAPTER to PAYMENT AGENT. A vertical CORRELATION SPINE carries TRACE ID, CASE ID, TASK ID, TOOL CALL ID, IDEMPOTENCY KEY. White CONTRACT MAP cards sit at each adapter; coral arrows reject lossy mappings.

Accessibility alt text: Adapters translate shapes while preserving meaning, identity, authorization, errors, and evidence across protocol boundaries.

## Diagram 99 - ACP-to-A2A historical migration

Output filename: `diagrams/99-acp-to-a2a-migration.png`

Specification status: Historical migration; A2A is the current target

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a two-column migration map. Left HISTORY ACP has AGENT MANIFEST, RUN, MESSAGE, OUTPUT, CUSTOM STREAM. Right CURRENT TARGET A2A 1.0 has AGENT CARD, TASK, MESSAGE PARTS, ARTIFACT, STATUS AND ARTIFACT EVENTS. An ADAPTER STRANGLER bridge supports DUAL READ, SHADOW TEST, CUTOVER, RETIRE. Do not portray ACP as current.

Accessibility alt text: A safe ACP migration inventories old semantics, maps them to current A2A contracts, tests gaps, and retires the old boundary gradually.

## Diagram 100 - Capstone: the Acme Protocol Interoperability Lab

Output filename: `diagrams/100-protocol-interoperability-lab.png`

Specification status: Capstone profile checked 2026-08-24

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a solid opaque dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested labels. Do not add a logo, watermark, unrelated title, tiny decorative prose, transparency, paint splashes, or rough masks.

Create a large integrated architecture. MAYA in REACT UI connects by AG-UI to ORCHESTRATOR. It calls POLICY MCP SERVER and PAYMENT A2A AGENT. Show MCP DISCOVERY, TOOL AND RESOURCE, MRTR OR TASK; A2A AGENT CARD, TASK, STATUS, ARTIFACT; AG-UI RUN, TOOL, STATE, ERROR. Add TRUST GATEWAY, CORRELATION SPINE, DURABLE STORE, CONFORMANCE SUITE, TRACE AND AUDIT. Mark draft interrupt adapter separately.

Accessibility alt text: The Acme lab composes MCP, A2A, and AG-UI at distinct boundaries and proves the result with conformance, correlation, recovery, and security evidence.
