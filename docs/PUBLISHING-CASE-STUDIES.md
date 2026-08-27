# Publishing a New Case Study

## One source collection, two reading formats

The website has three shelves: Courses for the ten visual volumes, Case Studies for Acme, HarborCare and FilePilot, and Library Guides for workspace and publishing instructions. Each case study has its own reading order, reference sections and build workbooks. Search covers all published articles.

The editable Markdown remains the source of truth. Standalone HTML editions remain useful for local reading, but the website does not embed those large HTML files. Its build converts the Markdown into small collection files and prepares standalone images.

## 1. Create the case-study folder

Place the new case study under `docs/case-studies`, alongside Acme and HarborCare. Keep its Markdown, local HTML editions and original images together. Drafts can stay in this folder without appearing on the website.

```text
docs/case-studies/new-example/
  collection.json
  00-START-HERE.md
  01-ARCHITECTURE.md
  manual-build/
    01-FOUNDATIONS.md
  assets/
    architecture.svg
```

## 2. Declare what to publish

Add `collection.json`. The build automatically discovers this file in each direct case-study folder. Only the documents explicitly listed in it are published; prompts, verification reports, drafts and local bundles are not swept into the website.

```json
{
  "id": "new-example",
  "kind": "case-study",
  "title": "New Example Platform",
  "subtitle": "A short plain-English description.",
  "icon": "🧩",
  "order": 3,
  "sections": [
    {
      "title": "Start here",
      "documents": [{ "id": 1, "file": "00-START-HERE.md" }]
    },
    {
      "title": "Architecture",
      "documents": [{ "id": 2, "file": "01-ARCHITECTURE.md" }]
    },
    {
      "title": "Build it step by step",
      "documents": [{ "id": 3, "file": "manual-build/01-FOUNDATIONS.md" }]
    }
  ]
}
```

Keep collection IDs and document IDs stable. They identify bookmarks and reading progress. Reorder entries to change the reading sequence without renumbering existing documents. A document can optionally have a shorter `title` in the manifest for navigation.

## 3. Write ordinary Markdown

Use one main heading, descriptive section headings and relative local image references. Links to another published Markdown or HTML document are rewritten to the website's reader. Links to unpublished local documents fail the build, so readers do not encounter dead desktop file links. External source citations remain external links.

Keep the original diagram alongside the document. The build rasterizes SVGs, flattens transparency against white, compresses images to WebP, records their dimensions and deduplicates repeated references. It does not edit the originals. Inspect text-heavy diagrams after compression; a build passing is not a substitute for checking legibility.

The website supports an in-page contents list and enlarged diagram view. Long code examples and tables scroll within the article on small screens.

## 4. Build and verify

Run `npm run build:content` to rebuild all courses and document collections. Run `npm run build` for the complete production build. These commands use Node.js, Markdown processing and Sharp; the website build does not require Python or Pandoc on Vercel.

Run `npm run verify:content` to verify the generated library. Check the new collection through the website: navigation, internal links, search, diagrams and narrow-screen reading. Use the existing standalone document builder separately when you want a local HTML edition; website publishing does not require one.

Course configuration lives in `data/courses.config.json`. The original Python course builder is retained as a legacy helper, not the authoritative website pipeline. Do not run it after the new library build because it writes an older manifest format.

## 5. What gets deployed

The root page receives only navigation metadata. Full article bodies are fetched when a collection is opened. Search data is fetched when needed. Generated collection files, search data and images have content-hashed names, allowing long-lived caching without serving an old file under a changed filename.

The website's generated assets live in `public/library`. The build removes obsolete files only within that generator-owned folder. Existing legacy generated folders are retained locally for compatibility and excluded from Vercel uploads; the new website no longer requests them.

Vercel uses the Next.js framework preset, `npm ci` and `npm run build`. No custom output directory is necessary. Original source Markdown and diagrams must be available during the build, but the standalone HTML, Word/PDF bundles and authoring scripts do not need to be published as static assets.

## 6. Safety and release checklist

Review the publication manifest before committing: it is an explicit public-content allowlist. Never publish private patient data, secrets, real operational traces or unreviewed documents. HarborCare remains entirely synthetic.

Before a release, check the production build, content verification, browser navigation and image rendering. Commit and deploy only when requested. A successful local build does not itself mean the public Vercel site has been updated.

## Reference documentation

- [Vercel build configuration](https://vercel.com/docs/deployments/configure-a-build)
- [Next.js image component](https://nextjs.org/docs/app/api-reference/components/image)
- [Sharp image operations](https://sharp.pixelplumbing.com/api-operation/)
