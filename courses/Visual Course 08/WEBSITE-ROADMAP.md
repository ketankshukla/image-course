# Volume 8 Website Roadmap

## Goal

Turn Volume 8 into an interactive Agent Quality Lab. Preserve the diagram-first teaching order, complete explanation, standards-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

## Recommended first release

1. Build a Next.js App Router site that reads `Volume 8 Course Content.json` at build time.
2. Create module, lesson, trace, evaluation, quality, performance, release, incident, glossary, and source routes.
3. Put the full explanation directly below each diagram and expose all states with text, not color alone.
4. Keep every dataset, trace, prompt, incident, and attack demonstration synthetic and local; never ship real customer records, private prompts, tokens, secrets, or production telemetry.
5. Add keyboard navigation, local progress, adjustable text, high contrast, reduced motion, downloadable diagrams, and printable lessons.
6. Deploy to Vercel only after routes, images, alt text, links, heading order, focus behavior, responsive layouts, and synthetic failure scenarios pass.

## Interactive visual laboratories

- Trace explorer: follow one support request through browser, Next.js, FastAPI, MCP, A2A, RAG, tools, queues, and artifacts.
- Context propagation lab: inject, extract, link, restart, and intentionally break W3C trace context across HTTP and queue boundaries.
- Telemetry privacy designer: classify fields, choose capture modes, redact content, sample safely, set retention, and verify deletion.
- Evaluation case builder: define input, context, expected evidence, allowed actions, forbidden outcomes, rubric, scorer, and version pins.
- Grader calibration lab: compare deterministic assertions, model grades, and human judgments while inspecting disagreements.
- Quality slice explorer: reveal failures hidden by an overall average across language, channel, issue type, tenant tier, and tool path.
- Stage-metric tree: connect final answer failure to routing, retrieval, policy, tools, delegation, synthesis, and user recovery.
- Budget calculator: allocate latency and scenario cost across model, retrieval, tools, agents, storage, queues, and cache.
- Load and saturation simulator: vary concurrency, queue depth, worker capacity, deadlines, and admission control.
- Release funnel: move a version through offline gates, shadow traffic, canary, promotion, rollback, and kill switch.
- Compatibility matrix: compare protocol version, capability, schema, fixture, and migration evidence across services.
- Incident learning loop: move an alert through ownership, triage, containment, recovery, postmortem, corrective action, and permanent regression test.

## Accessibility definition of done

- Every diagram has meaningful alt text and a complete adjacent explanation.
- Every interactive control is keyboard reachable and exposes the same state without hover or animation.
- Status, trace, score, budget, failure, alert, rollback, recovery, and evidence always have text labels.
- Simulations provide pause, step, reset, and a reduced-motion mode.
- Example performance, cost, and reliability values are clearly labeled as scenarios, never measured project results.
