# Volume 5 Website Roadmap

## Goal

Turn Volume 5 into an interactive knowledge-systems laboratory. Preserve the diagram-first lesson order, full explanation, pattern-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary sources from one structured content object.

## Recommended first release

1. Build a Next.js App Router site that reads `Volume 5 Course Content.json` at build time.
2. Create module, lesson, source-register, ingestion, retrieval-trace, temporal, evaluation, glossary, and source-register routes.
3. Put the full explanation directly beneath every diagram and show its pattern status beside the lesson title.
4. Keep authorization-sensitive demos local and synthetic; never ship real tenant documents or credentials.
5. Add keyboard-accessible previous/next navigation, local progress, adjustable text, high contrast, reduced motion, and printable lessons.
6. Deploy to Vercel only after routes, images, alt text, links, heading order, focus, responsive layouts, and synthetic security tests pass.

## Interactive visual laboratories

- Source authority mapper: assign owners and question-specific authority.
- Layout parser: label headings, tables, lists, captions, and page provenance.
- Chunking sandbox: compare semantic, fixed-token, and hierarchical boundaries.
- Hybrid retrieval funnel: inspect lexical, vector, RRF, reranking, and diversity stages.
- Permission gate: demonstrate pre-search authorization and blocked cross-tenant paths.
- Multi-hop planner: build dependencies, evidence roles, budgets, and stop rules.
- Temporal timeline: switch between valid time, recorded time, and current policy.
- Citation inspector: follow a claim to an exact source region and version.
- Conflict lab: choose answer, conflict disclosure, clarification, or abstention.
- Evaluation dashboard: compare baseline and candidate by query slice.

## Accessibility definition of done

- Every diagram has meaningful alt text and a complete adjacent explanation.
- Interactive nodes are keyboard reachable and expose the same information without hover or color.
- Status, authority, conflict, freshness, and permissions always have text labels.
- Synthetic examples explain blocked evidence without revealing forbidden content.
- Metrics state dataset size, slice, direction, and baseline; no example number is presented as a measured project result.
