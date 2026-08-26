# Volume 9 Diagram Prompt Library

These are the exact production prompts for Diagrams 197-220. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

## Shared art direction

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

## Diagram 197 - The event-driven interface mental model

Output filename: `diagrams/197-event-driven-interface-mental-model.png`

Pattern status: AG-UI event families are current; product event vocabulary remains application-specific

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show AGENT RUN emitting typed cards RUN, TEXT, TOOL, ACTIVITY, STATE, ARTIFACT, APPROVAL, ERROR into an EVENT STREAM. A validated REDUCER updates separate CHAT, PROGRESS, TOOL, ARTIFACT, APPROVAL panels. Add a coral PARSE PROSE path to WRONG UI and a teal TYPED EVENT path to EXPLAINABLE UI.

Accessibility alt text: An agent run emits typed lifecycle, text, tool, activity, state, artifact, approval, and error events that a reducer maps into dedicated interface regions instead of parsing prose.

## Diagram 198 - State snapshots, deltas, reducers, and conflict handling

Output filename: `diagrams/198-snapshots-deltas-reducers-conflicts.png`

Pattern status: AG-UI snapshots and RFC 6902 deltas are current; conflict policy is an application responsibility

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show AUTHORITATIVE SNAPSHOT with VERSION 12 entering a REDUCER, followed by ordered DELTA 13, 14, 15 cards using ADD REPLACE REMOVE. Render a UI STATE tree. Add coral OUT OF ORDER, STALE BASE, INVALID PATH into CONFLICT, then teal REQUEST FRESH SNAPSHOT into RECOVERED STATE.

Accessibility alt text: A versioned authoritative snapshot is reduced with ordered JSON Patch deltas; out-of-order, stale-base, and invalid-path updates cause conflict and trigger a fresh snapshot.

## Diagram 199 - Reconnect, replay, deduplication, and offline recovery

Output filename: `diagrams/199-reconnect-replay-dedup-offline-recovery.png`

Pattern status: Reliable-stream design pattern built on stable identifiers and current browser capabilities

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show LIVE STREAM with CURSOR 48 entering BROWSER. A NETWORK BREAK creates OFFLINE BUFFER and RECONNECT REQUEST LAST SEEN 48. SERVER REPLAYS events 49-55 through DEDUP SET and ORDER GATE into RESTORED UI. Coral paths show DUPLICATE EFFECT, GAP, EXPIRED CURSOR; teal FRESH SNAPSHOT recovers.

Accessibility alt text: After a network break, a browser reconnects with its last seen cursor, replays ordered events through deduplication, and requests a fresh snapshot when the cursor expired or a gap remains.

## Diagram 200 - Optimistic interface state versus authoritative business state

Output filename: `diagrams/200-optimistic-versus-authoritative-state.png`

Pattern status: Stable product-state pattern; framework helpers do not change the authority boundary

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show USER ACTION entering two lanes. OPTIMISTIC UI immediately shows PENDING with LOCAL DRAFT and REVERSIBLE PREVIEW. AUTHORITATIVE SERVER checks IDENTITY POLICY VERSION EFFECT, then returns COMMITTED RECEIPT or coral REJECTED CONFLICT. A RECONCILE gate updates UI; forbid OPTIMISTIC APPROVED and OPTIMISTIC PAID.

Accessibility alt text: A user action creates reversible optimistic pending state while the authoritative server checks identity, policy, version, and effect before returning a committed receipt or rejection for reconciliation.

## Diagram 201 - Progressive disclosure and observable stage labels

Output filename: `diagrams/201-progressive-disclosure-stage-labels.png`

Pattern status: Human-centered progress pattern using current AG-UI activity and lifecycle events

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show one WORKFLOW progressing through UNDERSTAND, RESEARCH, CHECK POLICY, PREPARE, WAITING FOR YOU, COMPLETE. A SIMPLE VIEW shows current stage and next action; an EXPANDED VIEW reveals elapsed time, evidence count, tool status, and receipts. Coral INDEFINITE SPINNER and FAKE PERCENTAGE lead to LOST TRUST.

Accessibility alt text: A workflow exposes honest named stages with a simple current-state view and an expanded evidence view, contrasted with an indefinite spinner and invented percentage.

## Diagram 202 - Tool cards, evidence cards, artifacts, and receipts

Output filename: `diagrams/202-tool-evidence-artifact-receipt-cards.png`

Pattern status: Durable-evidence product pattern; protocol identifiers remain distinct

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a TOOL CALL card with PROPOSED, RUNNING, RESULT; an EVIDENCE card with SOURCE VERSION FRESHNESS AUTHORITY; an ARTIFACT card with FILE VERSION STATUS; and a RECEIPT card with ACTOR DECISION EFFECT TIME. Link all four by references. Coral CHAT CLAIM has NO RECEIPT; teal VERIFIED OUTCOME has full chain.

Accessibility alt text: Separate tool, evidence, artifact, and receipt cards link a proposed action through source versions and durable output to a verified business outcome, unlike an unsupported chat claim.

## Diagram 203 - Partial success, preserved work, and unfinished work

Output filename: `diagrams/203-partial-success-preserved-unfinished-work.png`

Pattern status: Resilient product and workflow pattern

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show a workflow split into COMPLETED RESEARCH, PRESERVED ARTIFACT, FAILED FINANCE CHECK, UNFINISHED APPROVAL, and SAFE PARTIAL RESULT. Offer CONTINUE LATER, RETRY FAILED STAGE, HUMAN HELP, CANCEL REMAINDER. Coral ALL OR NOTHING discards work; teal PRESERVE CHECKPOINT keeps value and provenance.

Accessibility alt text: A partially successful workflow preserves completed research and an artifact, names the failed and unfinished stages, and offers retry, continue-later, human-help, or cancel-remainder choices.

## Diagram 204 - Errors, recovery choices, support references, and next actions

Output filename: `diagrams/204-errors-recovery-support-next-actions.png`

Pattern status: Stable error-design principles using RFC 9457 and accessible interaction patterns

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show ERROR EVENT entering a CLASSIFIER with USER ACTIONABLE, RETRYABLE, CONFLICT, PERMISSION, UNSAFE, UNKNOWN. Each produces a plain card with WHAT HAPPENED, WHAT WAS SAVED, NEXT ACTION, SUPPORT ID. Coral RAW STACK TRACE and TRY AGAIN LOOP; teal RETRY, EDIT, RESUME, HUMAN HELP, SAFE STOP.

Accessibility alt text: An error classifier turns technical failures into plain-language cards that explain what happened, preserved work, next actions, and a support reference, while blocking raw stack traces and blind retry loops.

## Diagram 205 - Interrupt, input request, approval, rejection, and expiry

Output filename: `diagrams/205-interrupt-input-approval-rejection-expiry.png`

Pattern status: Human-control pattern; AG-UI interrupt capability is evolving and must remain versioned

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show WORKFLOW reaching DECISION GATE and pausing. An APPROVAL CARD names PROPOSAL, EFFECT, EVIDENCE VERSION, POLICY, ACTOR, EXPIRY, CHOICES APPROVE REJECT EDIT ASK. After EXPIRY or VERSION CHANGE, coral buttons disable and REFRESH REVIEW appears. Teal RECEIPT resumes the exact paused task.

Accessibility alt text: A workflow pauses at a decision gate and presents an approval card bound to one proposal, effect, evidence version, actor, policy, and expiry; stale cards disable and require fresh review.

## Diagram 206 - Edit, steer, reprioritize, replan, and invalidate

Output filename: `diagrams/206-edit-steer-reprioritize-replan-invalidate.png`

Pattern status: Human-steering product pattern; implementation and protocol events remain application-specific

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show CURRENT PLAN with GOAL, CONSTRAINTS, PRIORITIES, STEPS, ARTIFACTS. USER STEERING chooses EDIT GOAL, ADD CONSTRAINT, REPRIORITIZE, REPLAN. An IMPACT ANALYZER marks KEEP, RECHECK, INVALIDATE. Coral SILENT PLAN MUTATION; teal NEW PLAN VERSION with DIFF, CONSENT, preserved valid work.

Accessibility alt text: User steering changes goals, constraints, or priorities; an impact analyzer keeps valid work, rechecks dependencies, invalidates affected claims, and produces a new visible plan version with a diff.

## Diagram 207 - Cancel, undo, compensate, and preserve audit history

Output filename: `diagrams/207-cancel-undo-compensate-audit-history.png`

Pattern status: Established distributed-workflow and human-control pattern

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show ACTION TIMELINE with QUEUED, RUNNING, COMMITTED. CANCEL stops queued or running work. UNDO reverses a reversible local change. COMPENSATE creates a new corrective effect after COMMITTED. Every path writes AUDIT HISTORY and USER RECEIPT. Coral ERASE HISTORY and FAKE UNDO; teal RECOVERED STATE.

Accessibility alt text: A timeline distinguishes cancellation before commitment, true undo of a reversible change, and compensating action after commitment, while preserving audit history and user receipts.

## Diagram 208 - Accessibility, plain language, uncertainty, and trust cues

Output filename: `diagrams/208-accessibility-plain-language-uncertainty-trust.png`

Pattern status: WCAG 2.2 is the current W3C baseline; ARIA patterns support implementation but require testing

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show one interface used by KEYBOARD, SCREEN READER, ZOOM, VOICE, TOUCH, REDUCED MOTION. Cards demonstrate FOCUS ORDER, LIVE STATUS, TEXT LABELS, CONTRAST, TARGET SIZE, ERROR HELP, UNCERTAINTY. Coral COLOR ONLY, AUTO FOCUS JUMP, HIDDEN CONTROL, OVERCONFIDENT COPY; teal UNDERSTANDABLE CONTROL.

Accessibility alt text: An agent interface supports keyboard, screen reader, zoom, voice, touch, and reduced motion through focus order, status announcements, text labels, contrast, target size, error help, and honest uncertainty.

## Diagram 209 - Typed components, schemas, allowlists, and validation

Output filename: `diagrams/209-typed-components-schemas-allowlists-validation.png`

Pattern status: A2UI v0.9.1 is the checked current release while v1.0 remains a candidate; isolate versions behind an adapter

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show MODEL proposing a declarative UI TREE into JSON SCHEMA, COMPONENT ALLOWLIST, PROP VALIDATOR, ACTION POLICY. Valid cards TABLE FORM CHART NOTICE render in a SAFE COMPONENT CATALOG. Coral ARBITRARY HTML SCRIPT UNKNOWN ACTION OVERSIZED PAYLOAD go to REJECT. Teal VERSION ADAPTER leads to ACCESSIBLE UI.

Accessibility alt text: A model's declarative interface tree passes schema, component allowlist, property validation, action policy, and a version adapter before safe accessible components render; arbitrary code is rejected.

## Diagram 210 - MCP Apps, sandboxed frames, consent, and communication

Output filename: `diagrams/210-mcp-apps-sandbox-consent-communication.png`

Pattern status: MCP Apps extension 2026-01-26 is stable; hosts and apps still negotiate optional capabilities

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show MCP SERVER exposing TOOL plus UI RESOURCE with UI URI. HOST fetches resource into SANDBOXED IFRAME. APP BRIDGE exchanges JSON-RPC messages across a narrow boundary. Gates CAPABILITY NEGOTIATION, CONSENT, ORIGIN CHECK, DATA MINIMIZATION, AUDIT RECEIPT. Coral DIRECT HOST ACCESS and UNDECLARED CAPABILITY blocked.

Accessibility alt text: An MCP server declares a tool and UI resource; the host loads the app in a sandboxed iframe and permits only capability-negotiated, consented, origin-checked, minimized, audited communication through the app bridge.

## Diagram 211 - Frontend tool calls and user-device actions

Output filename: `diagrams/211-frontend-tools-user-device-actions.png`

Pattern status: Browser permission and user-activation behavior is platform-dependent; design capability detection and refusal paths

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show AGENT PROPOSAL entering USER GESTURE and HOST POLICY. Device tools CLIPBOARD, FILE PICKER, CAMERA, LOCATION, DOWNLOAD, OPEN LINK sit behind PURPOSE, PERMISSION, PREVIEW, CONFIRM. Teal EXECUTE ON DEVICE to RECEIPT. Coral SILENT ACCESS, BACKGROUND PROMPT, HIDDEN DOWNLOAD, UNSAFE URL blocked.

Accessibility alt text: An agent proposal reaches clipboard, file, camera, location, download, and link actions only after host policy, purpose, browser permission, preview, user gesture, confirmation, and a receipt.

## Diagram 212 - Interface security, data exposure, and safe rendering

Output filename: `diagrams/212-interface-security-data-exposure-safe-rendering.png`

Pattern status: Web security standards evolve; maintain threat models, dependency updates, browser tests, and defense in depth

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show UNTRUSTED INPUTS MODEL TEXT RETRIEVAL TOOL RESULT APP MESSAGE URL FILE entering ENCODE, SANITIZE WHERE NEEDED, SCHEMA, ORIGIN, CSP, PERMISSIONS POLICY, SANDBOX, AUTHZ, REDACTION. Safe outputs TEXT COMPONENT LINK DOWNLOAD. Coral XSS DATA LEAK PROMPT SPOOF CLICKJACK CONFUSED DEPUTY blocked and logged.

Accessibility alt text: Untrusted model text, retrieval, tool results, app messages, URLs, and files pass encoding, schema, origin, policy, sandbox, authorization, and redaction controls before safe components render; common web attacks are blocked.

## Diagram 213 - A reusable visual lesson content model

Output filename: `diagrams/213-reusable-visual-lesson-content-model.png`

Pattern status: The content model is a product contract; version it independently from the website framework

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show AUTHORING SOURCE feeding VALIDATED LESSON MODEL with OUTCOME, STATUS, DIAGRAM, ALT, EXPLANATION, TRACE, ANALOGY, NEXTJS, PYTHON, CASE STUDY, LAB, CHECKPOINT, GLOSSARY, SOURCES, LINKS. Outputs DOCX WEBSITE SEARCH OFFLINE QUIZ. Add SCHEMA VERSION MIGRATION and coral COPY PASTE DRIFT.

Accessibility alt text: One validated, versioned lesson model containing the complete visual teaching structure produces the document, website, search, offline package, and quizzes while preventing copy-and-paste drift.

## Diagram 214 - Responsive diagrams, zoom, annotations, and reading order

Output filename: `diagrams/214-responsive-diagrams-zoom-annotations-reading-order.png`

Pattern status: WCAG 2.2 and semantic web patterns are stable baselines; test actual assistive technologies and device layouts

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show one VISUAL LESSON adapting to DESKTOP TABLET MOBILE ZOOM 400%. Layers OVERVIEW, NUMBERLESS FUNCTIONAL LABELS, HOTSPOTS, ANNOTATIONS, PAN ZOOM RESET, KEYBOARD, READING ORDER, ALT TEXT, DETAILED EXPLANATION. Coral TINY TEXT, HORIZONTAL TRAP, COLOR ONLY, IMAGE OF TEXT. Teal EQUIVALENT PATH.

Accessibility alt text: One visual lesson adapts across desktop, tablet, mobile, and 400 percent zoom with keyboard zoom and pan, annotations, clear reading order, alt text, and a detailed equivalent explanation; tiny text and color-only meaning are rejected.

## Diagram 215 - Glossary, citations, search, prerequisites, and cross-links

Output filename: `diagrams/215-glossary-citations-search-prerequisites-crosslinks.png`

Pattern status: Search implementation is product-specific; source currency and prerequisite truth require ongoing editorial ownership

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show COURSE KNOWLEDGE GRAPH with LESSON nodes linked by PREREQUISITE, RELATED, BUILDS ON, CASE STUDY, TERM, SOURCE. SEARCH box applies QUERY, FILTER VOLUME MODULE TOPIC STACK STATUS, returns SNIPPETS with WHY MATCHED. SOURCE cards show OFFICIAL, CHECKED DATE, VERSION, SUPPORTS CLAIM. Coral BROKEN LINK STALE SOURCE CIRCULAR PREREQUISITE.

Accessibility alt text: A course knowledge graph connects lessons, terms, sources, prerequisites, related concepts, and case studies; transparent search filters results and source cards expose version and freshness while stale or broken relationships are flagged.

## Diagram 216 - Progress, checkpoints, quizzes, accessibility, and offline use

Output filename: `diagrams/216-progress-checkpoints-quizzes-accessibility-offline.png`

Pattern status: Service Worker, IndexedDB, and Web App Manifest standards are current; offline behavior still varies by browser and storage policy

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show LEARNER choosing START LESSON, CHECKPOINT, QUIZ, LAB, BOOKMARK, NOTE. LOCAL PROGRESS and OPTIONAL SYNC merge through CONSENT and CONFLICT RULES. SERVICE WORKER caches APP SHELL CONTENT VERSION DIAGRAMS. OFFLINE badge leads to QUEUED ACTIONS then RECONNECT. Accessibility gates KEYBOARD SCREEN READER REFLOW REDUCED MOTION. Coral LOST PROGRESS STALE ANSWER SILENT SYNC.

Accessibility alt text: Learner progress, checkpoints, quizzes, bookmarks, notes, optional consented sync, and accessible controls work through an offline cache and reconnect queue with conflict rules, avoiding lost progress, stale answers, or silent synchronization.

## Diagram 217 - Asynchronous return, notifications, and attention management

Output filename: `diagrams/217-async-return-notifications-attention-management.png`

Pattern status: Notifications require permission and platform support; product attention policy remains application-specific

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show USER STARTS LONG TASK then LEAVES. DURABLE RUN continues through STAGES. RETURN OPTIONS IN APP BADGE, EMAIL DIGEST, PUSH NOTIFICATION behind USER CHOICE, URGENCY, QUIET HOURS, RATE LIMIT, PRIVACY, DEEP LINK. States READY NEEDS INPUT FAILED EXPIRED. Coral NOTIFICATION STORM, SECRET IN PREVIEW, FALSE URGENCY. Teal RESUME CONTEXT.

Accessibility alt text: A durable task continues after the user leaves and returns through consented in-app, digest, or push notifications filtered by urgency, quiet hours, rate limits, and privacy, with a deep link restoring context.

## Diagram 218 - Privacy controls, consent, memory settings, and deletion

Output filename: `diagrams/218-privacy-consent-memory-settings-deletion.png`

Pattern status: Privacy obligations vary by jurisdiction and context; this course teaches product architecture, not legal advice

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show DATA LIFECYCLE COLLECT USE STORE SHARE REMEMBER EXPORT DELETE. USER CONTROL CENTER has PURPOSE, DATA CATEGORIES, MEMORY OFF SESSION PROJECT LONG TERM, RETENTION, CONNECTED APPS, DOWNLOAD, DELETE. CONSENT RECEIPT versions policy. DELETION FAN OUT to PRIMARY, VECTOR, CACHE, LOG, BACKUP SCHEDULE with VERIFICATION. Coral DARK PATTERN, BUNDLED CONSENT, GHOST MEMORY.

Accessibility alt text: A privacy control center explains data purposes, categories, memory scopes, retention, connected apps, export, and deletion; consent is versioned and deletion propagates through primary stores, vectors, caches, logs, and backup schedules with verification.

## Diagram 219 - Product analytics, feedback, evaluation, and experiment ethics

Output filename: `diagrams/219-analytics-feedback-evaluation-experiment-ethics.png`

Pattern status: Measurement design and experiment policy are context-specific; all course numbers are illustrative unless explicitly measured later

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show USER OUTCOME feeding PRODUCT EVENT, FEEDBACK, QUALITY EVAL, SAFETY REVIEW, ACCESSIBILITY EVIDENCE. METRIC CARD includes DEFINITION, NUMERATOR, DENOMINATOR, EXCLUSIONS, SLICE, WINDOW, VERSION. EXPERIMENT gate CONSENT, RISK REVIEW, FAIR ALLOCATION, STOP RULE, GUARDRAIL, DEBRIEF. Coral DARK PATTERN, VANITY METRIC, HIDDEN HARM, EXAMPLE AS FACT.

Accessibility alt text: User outcomes connect to minimized product events, feedback, quality evaluation, safety review, and accessibility evidence; every metric exposes its definition and denominator, while experiments require consent, risk review, fair allocation, stop rules, guardrails, and debriefing.

## Diagram 220 - Capstone: Acme Agent Workspace and Learning Platform

Output filename: `diagrams/220-acme-agent-workspace-learning-platform.png`

Pattern status: Design capstone using the checked 2026-08-25 baseline; pin protocol versions and revalidate before implementation

Use case: scientific-educational. Asset type: 16:9 visual-course human-control explainer. Create a polished beginner-friendly agentic product diagram on a solid opaque dark midnight-navy gradient background. Use glowing cobalt-blue isometric platforms, cyan event, navigation, and proposal arrows, teal authoritative, accessible, consented, preserved-work, and recovery paths, white event, state, component, evidence, artifact, approval, lesson, or receipt cards, selective coral conflict, stale state, unsafe rendering, expired approval, data exposure, lost work, and blocked-action paths, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the requested functional teaching labels and render them verbatim. Do not place a diagram number, lesson number, full diagram title, headline, caption, or title banner inside the image; the course document supplies those outside the image. No logo, watermark, tiny prose, transparency, paint texture, decorative clutter, or extra text.

Show two connected product zones AGENT WORKSPACE and VISUAL LEARNING PLATFORM. Inputs NEXTJS REACT FASTAPI MCP A2A AG-UI MCP APPS A2UI RAG TOOLS. Center HUMAN CONTROL LOOP REQUEST, PLAN, PROGRESS, EVIDENCE, PROPOSAL, APPROVAL, ACTION, RECEIPT, RECOVERY. Learning loop VISUAL, EXPLANATION, CASE, LAB, CHECKPOINT, PROGRESS. Cross-cutting ACCESSIBILITY SECURITY PRIVACY OBSERVABILITY EVALUATION OFFLINE. Coral STALE POLICY UNSAFE UI EXPIRED APPROVAL DATA LEAK blocked.

Accessibility alt text: The Acme capstone connects an agent workspace and visual learning platform through human-control and learning loops, using Next.js, React, FastAPI, MCP, A2A, AG-UI, MCP Apps, A2UI, RAG, and tools under shared accessibility, security, privacy, observability, evaluation, and offline controls.
