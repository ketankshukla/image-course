# Volume 9 Website Roadmap

## Goal

Turn Volume 9 into an accessible Agent Workspace and Visual Learning Platform. Preserve the diagram-first teaching order, complete explanation, standards-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

## Recommended first release

1. Build a Next.js App Router site that reads `Volume 9 Course Content.json` at build time.
2. Create module, lesson, trace, case-study, lab, glossary, source, search, progress, privacy, and settings routes.
3. Put the full explanation directly below each diagram and expose all states with text, not color alone.
4. Keep every customer case, event stream, proposal, app message, permission, and security demonstration synthetic and local; never ship real customer records, private prompts, tokens, secrets, or production telemetry.
5. Add keyboard navigation, local progress, adjustable text, high contrast, reduced motion, downloadable diagrams, and printable lessons.
6. Deploy to Vercel only after routes, images, alt text, links, heading order, focus behavior, responsive layouts, and synthetic failure scenarios pass.

## Interactive visual laboratories

- Event replay lab: apply lifecycle, activity, tool, state, approval, artifact, and recovery events to an empty interface.
- Snapshot conflict lab: reorder, duplicate, and corrupt deltas, then recover through a fresh authoritative snapshot.
- Approval designer: compare, edit, steer, reject, expire, cancel, undo, compensate, and preserve receipts.
- Generated component catalog: validate A2UI-style payloads against schema, nesting, data, action, and accessibility rules.
- MCP App host: negotiate capabilities, sandbox an iframe, inspect bridge messages, grant consent, revoke access, and audit a receipt.
- Device-action studio: simulate file, clipboard, camera, location, download, and open-link proposals with refusal alternatives.
- Safe-rendering range: inject hostile text, markup, URLs, component trees, app messages, and cross-tenant identifiers.
- Diagram accessibility viewer: test zoom, annotations, reading order, keyboard behavior, reflow, and complete text equivalents.
- Knowledge navigator: search by beginner language, inspect match reasons, follow prerequisites, and audit source freshness.
- Offline learning lab: install a course pack, answer checkpoints offline, create conflicts, reconnect, merge, export, and delete.
- Attention policy simulator: apply urgency, channels, quiet hours, privacy, grouping, rate limits, and deep links.
- Privacy lineage lab: follow collection, memory, embeddings, caches, providers, export, deletion, and verification.

## Accessibility definition of done

- Every diagram has meaningful alt text and a complete adjacent explanation.
- Every interactive control is keyboard reachable and exposes the same state without hover or animation.
- Status, stage, proposal, approval, error, uncertainty, privacy, recovery, and evidence always have text labels.
- Simulations provide pause, step, reset, and a reduced-motion mode.
- Example product, learning, and experiment values are clearly labeled as scenarios, never measured project results.
