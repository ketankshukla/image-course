# Volume 6 Website Roadmap

## Goal

Turn Volume 6 into an interactive durable-workflow laboratory. Preserve the diagram-first teaching order, complete explanation, pattern-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

## Recommended first release

1. Build a Next.js App Router site that reads `Volume 6 Course Content.json` at build time.
2. Create module, lesson, workflow, task, queue, approval, artifact, recovery, glossary, and source routes.
3. Put the full explanation directly below each diagram and expose all states with text, not color alone.
4. Keep every interactive failure demonstration synthetic and local; never ship real customer records, queue credentials, repair commands, or provider secrets.
5. Add keyboard navigation, local progress, adjustable text, high contrast, reduced motion, downloadable diagrams, and printable lessons.
6. Deploy to Vercel only after routes, images, alt text, links, heading order, focus behavior, responsive layouts, and synthetic failure scenarios pass.

## Interactive visual laboratories

- State-layer mapper: assign IDs, owners, stores, and lifetimes to conversation, run, task, and workflow records.
- State-machine builder: accept or reject commands under explicit invariants.
- Replay laboratory: rebuild state from events, snapshots, and code versions.
- Queue simulator: change visibility, crash a worker, redeliver, and acknowledge after a receipt.
- Backpressure dashboard: adjust capacity, priorities, fairness, and overload response.
- Idempotency sandbox: retry before and after side effects and inspect one stable result.
- Join designer: choose all, quorum, required-plus-optional, or deadline-aware fan-in.
- Saga mapper: classify compensable, pivot, retryable, irreversible, and manual steps.
- A2A delegation lab: resolve a 1.0 Agent Card, create a task, follow status, and accept an artifact.
- Approval contract lab: change an amount after approval and observe invalidation.
- Budget ledger: reserve and spend time, money, token, tool, retry, and concurrency envelopes.
- Chaos matrix: inject crash, timeout, duplicate, reorder, partition, and stale input at named boundaries.
- Recovery runbook: reconcile external truth, choose repair, and produce a closure receipt.

## Accessibility definition of done

- Every diagram has meaningful alt text and a complete adjacent explanation.
- Every interactive control is keyboard reachable and exposes the same state without hover or animation.
- Status, ownership, priority, permission, timeout, duplicate, compensation, and recovery always have text labels.
- Simulations provide pause, step, reset, and a reduced-motion mode.
- Example performance, cost, and reliability values are clearly labeled as scenarios, never measured project results.
