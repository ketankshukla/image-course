# Wiki publishing and domain routing

## Architecture

The wiki is part of the existing image-course repository and Next.js application. It does not need another GitHub repository, Vercel project, or database. The production target is wiki.ketanshukla.dev; the existing library remains at course.ketanshukla.dev. The developer-profile project is separate and must not be modified when changing the wiki.

## Source and publication

`data/wiki.json` is an explicit list of published concepts. Each entry contains its stable slug, category, explanation, three-step teaching flow, example, mistake, question, answer, related slugs, and case-study IDs. Put only reviewed public teaching content in it. The server renders the full entry; the homepage's small client component receives summaries for search and category filtering, not all article bodies.

Wiki pages are under `app/wiki`. The global library sidebar links to the wiki. Wiki search is separate from the library's article search. There is no public editing, authentication, progress persistence, live agent execution, or personal data.

## Routing

`middleware.ts` checks the exact hostname. On the wiki hostname it internally rewrites `/rag` to `/wiki/rag`. The visitor keeps the short address. Requests for `/wiki` or `/wiki/*` on the production course/wiki hostnames redirect to the canonical wiki hostname. Requests for the help page on the wiki go to the course help page. Framework assets, library images and API paths are excluded from rewriting. Unknown wiki slugs return 404.

Local and preview hosts retain `/wiki` and `/wiki/rag` for testing. Plain anchor links deliberately use the internal prefix; production routing canonicalizes them before serving the page. This costs one redirect but avoids depending on client hydration for hostname detection. Canonical metadata points to the wiki subdomain.

## Release checks

Run `node scripts/verify_wiki.cjs`, `npm run build`, and `npm run verify:content`. Test search, category filters, no results, related concepts, the answer disclosure, external course links, canonical redirects, static assets and unknown slugs. Check both production hostnames after deployment. A code release updates the courses and wiki together.

Vercel's project is image-course under ketan-shuklas-projects-8feda58f. Add only wiki.ketanshukla.dev to this project; never move the apex domain or force-transfer a domain from another project. DNS is managed by Vercel. Domain assignment and HTTPS readiness must be checked independently of a successful application build.
