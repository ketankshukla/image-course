# Volume 3 Website Roadmap

## Goal

Turn the same structured lesson source used by the document into an accessible visual study website. Keep the diagrams, explanations, case studies, labs, checkpoints, glossary, and related-lesson links synchronized from one source.

## Recommended first release

1. Build a Next.js App Router site that reads `Volume 3 Course Content.json` at build time.
2. Create module, lesson, glossary, source-register, and capstone pages.
3. Render each lesson in this order: outcome, diagram, alt text, explanation, trace, analogy, dual-stack map, Maya case study, danger, mini lab, checkpoint, glossary, related lessons.
4. Add keyboard-accessible previous and next navigation, module progress, text-size controls, high contrast, reduced motion, and printable lesson views.
5. Deploy a preview to Vercel and verify every route, image, link, heading, focus state, and mobile breakpoint.

## Second release

- Add optional diagram hotspots whose descriptions are available by keyboard and screen reader.
- Add local bookmarks and completion state before adding accounts.
- Add search across titles, glossary terms, case studies, and stack mappings.
- Add a compare view that places the Next.js and Python implementation maps side by side.
- Add a capstone checklist with evidence links rather than self-reported completion alone.

## Content model

Use `id` and `slug` as stable identities. Treat `diagram`, `alt`, `explanation`, `trace`, `caseStudy`, `lab`, `checkpoint`, `answer`, `glossary`, and `related` as required fields. Reject a build when an image or required field is missing.

## Accessibility definition of done

- Every diagram has meaningful alt text and a full text explanation directly below it.
- Decorative icons are hidden from assistive technology.
- Heading levels are sequential and every page has one clear main heading.
- All actions work without a pointer and have visible focus.
- Color is never the only signal for state, error, or direction.
- Progress and reconnection messages use appropriate live regions without excessive announcements.
