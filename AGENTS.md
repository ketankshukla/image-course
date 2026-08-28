# Agent Notes

## Course Website

This is a Next.js 15 + TypeScript + Tailwind CSS learning library. Source courses live in `courses/Visual Course NN`. Case studies live in `docs/case-studies/*`; each published study has a `collection.json` allowlist. The authoritative Node build is `scripts/build_library.mjs`. See `docs/PUBLISHING-CASE-STUDIES.md` and `docs/FOLDER-STRUCTURE.md`.

### Key commands

- `npm run build:content` — build courses and published documents, flatten PNG/SVG images to hashed WebP files, and regenerate the library manifest.
- `npm run verify:content` — verify links, search coverage, images and course contracts.
- `npm run dev` — run the local dev server on `http://localhost:3000`.
- `npm run build` — regenerate content, then create an optimized production build.
- `npm run start` — serve the production build.

### Content structure

- Markdown course pages: `courses/Visual Course NN/diagram-docs/`
- Original diagrams: `courses/Visual Course NN/diagrams/`
- Compressed WebP diagrams: `public/library/images/`
- Collection data: `public/library/collections/<id>.<hash>.json`
- Lightweight navigation manifest: `data/manifest.json`
- Full-text search index: `public/library/search.<hash>.json`
- Case-study publication manifests: `docs/case-studies/*/collection.json`
- Library-guide publication manifest: `docs/collection.json`

### Adding another course

Edit `data/courses.config.json` and add an entry to its array:

```json
{
    "id": "03",
    "source_dir": "Visual Course 03",
    "title": "Visual Course Volume 3 — ...",
    "subtitle": "...",
    "icon": "🚀"
}
```

Then run `npm run build:content` (or `npm run build`). The client will automatically show the new course in the sidebar and lazy-load its data when a chapter is selected.

The `source_dir` entry is relative to `courses/`, not the repository root. Move a complete course folder together with its assets to preserve relative image links. Do not move `public/`, `data/`, or application runtime files when organizing source documents.

If the volume includes a `Volume X Course Content.json` file with `modules` and `lessons` lists, add a `content_json` key to the course entry. The build script will use that JSON for module order and titles while still rendering the detailed Markdown bodies.

### Architecture

- The page receives a small `data/manifest.json` at build time and passes it to the client.
- The sidebar has Courses, Case Studies and Library Guides shelves, then collections, sections and articles.
- The client uses each manifest entry's `dataUrl` to fetch one collection on demand. Do not import full article bodies into the client bundle.
- Search uses the manifest's hashed `searchUrl`, fetched on demand.
- Keep collection/document IDs stable for bookmarks and progress; ordering is independent of IDs.
- New case studies are discovered from direct subfolders containing `collection.json`. Publish only the listed Markdown files. Keep drafts and real private data out of these manifests.
- When asked to add a case study, include its publication manifest, local reading editions where requested, a library build and content verification in the same task so it is available in the website reader too.
- Vercel runs the same Node-only `npm run build` as local builds; Python/Pandoc are only for optional legacy/local document tooling.
- Do not run legacy `scripts/build_content.py` after the library build: it writes the old manifest schema.
- The build prunes only obsolete generated files under `public/library`; never delete original sources or legacy output folders as part of content generation.

### Reading theme

- `app/theme.css` is the shared blue-and-white palette and reading typography, imported after structural `globals.css`. Tailwind colors reference its CSS variables.
- Article text defaults to 24px with 22/24/28px controls. The validated `libraryReadingSize` browser preference persists between articles and visits; storage is optional.
- Keep navigation compact, headings in the system sans-serif font, and tables/code horizontally scrollable on mobile. Theme changes do not require editing or rebuilding individual Markdown documents by hand.

### Wiki

- The wiki lives in this application, not another repository or Vercel project. Public hostname: `wiki.ketanshukla.dev`; local/preview path: `/wiki`.
- `data/wiki.json` is its publication list. Keep slugs stable, validate related slugs, and use fictional teaching examples. `app/wiki` renders entries statically; homepage search receives summaries only.
- `middleware.ts` routes the exact wiki hostname and canonicalizes production `/wiki` URLs. Preserve asset/API exclusions and do not modify the developer-profile apex domain.
- Run `node scripts/verify_wiki.cjs`, the production build, and `node scripts/smoke_wiki.mjs <origin>` after wiki/routing changes. See `docs/WIKI-OPERATIONS.md`.
