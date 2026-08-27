# Volume 4 Website Roadmap

## Goal

Turn the document and its structured lesson source into a visual protocol-engineering website. Keep the protocol stability label, diagram, full text explanation, Maya case study, dual-stack map, lab, checkpoint, glossary, and source links synchronized from one content object.

## Recommended first release

1. Build a Next.js App Router site that reads `Volume 4 Course Content.json` at build time.
2. Create module, lesson, protocol-status, conformance-lab, migration, glossary, and source-register pages.
3. Put the specification status beside every lesson title: stable, official extension, roadmap direction, draft, historical, or implementation pattern.
4. Render each lesson in the same order as the document and put the complete text explanation immediately below its diagram.
5. Add keyboard-accessible previous and next navigation, local progress, text-size controls, high contrast, reduced motion, and printable lesson views.
6. Deploy a preview to Vercel only after all routes, images, links, headings, focus states, and mobile layouts pass automated and human checks.

## Interactive visual ideas

- A normative-language sorter that turns MUST, SHOULD, and MAY statements into test rows.
- A capability-intersection simulator showing safe feature negotiation and downgrade failure.
- A JSON-RPC envelope lab that keeps request, business, task, and trace identities separate.
- An MCP MRTR-versus-Task decision lab.
- An A2A TaskState machine with legal and illegal transitions.
- An AG-UI event reducer replay lab with duplicate and missing events.
- An ACP-to-A2A mapping worksheet that labels gaps instead of hiding them.
- A protocol-boundary decision tree for MCP, A2A, AG-UI, ordinary HTTP, and internal functions.

## Content model

Treat `id`, `slug`, `moduleId`, `title`, `stability`, `diagram`, `alt`, `outcome`, `explanation`, `trace`, `nextjs`, `python`, `caseStudy`, `lab`, `checkpoint`, `answer`, `glossary`, `related`, and `sources` as required. Reject the build when any image, source, or required field is missing.

## Accessibility definition of done

- Every diagram has meaningful alt text and a complete adjacent explanation.
- Diagram hotspots, if added, are also reachable and understandable without a pointer.
- Heading levels are sequential and every page has one clear main heading.
- Status never depends on color alone; every badge includes text.
- Dynamic progress uses restrained live regions and provides a static reconciliation view.
- Draft, historical, roadmap, and stable material are visibly and programmatically distinguishable.
