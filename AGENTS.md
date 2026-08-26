# Agent Notes

## Course Website

This is a Next.js 15 + TypeScript + Tailwind CSS site for the Visual Agent Course volumes. The source content lives in the `Visual Course NN` folders; the build script turns the `diagram-docs` Markdown files into per-course JSON and a small `data/manifest.json` for navigation.

### Key commands

- `npm run build:content` — parse the configured `Visual Course NN` folders, compress PNGs to `public/images/*.webp`, and regenerate `public/courses/*.json` + `data/manifest.json`.
- `npm run dev` — run the local dev server on `http://localhost:3000`.
- `npm run build` — regenerate content, then create an optimized production build.
- `npm run start` — serve the production build.

### Content structure

- Markdown course pages: `Visual Course NN/diagram-docs/`
- Original diagrams: `Visual Course NN/diagrams/`
- Compressed WebP diagrams: `public/images/`
- Per-course full data: `public/courses/NN.json`
- Lightweight navigation manifest: `data/manifest.json`
- Full-text search index: `public/search-index.json`

### Adding another course

Edit `scripts/build_content.py` and add an entry to the `COURSES` list:

```python
{
    "id": "03",
    "source_dir": "Visual Course 03",
    "title": "Visual Course Volume 3 — ...",
    "subtitle": "...",
    "icon": "🚀",
}
```

Then run `npm run build:content` (or `npm run build`). The client will automatically show the new course in the sidebar and lazy-load its data when a chapter is selected.

If the volume includes a `Volume X Course Content.json` file with `modules` and `lessons` lists, add a `content_json` key to the course entry. The build script will use that JSON for module order and titles while still rendering the detailed Markdown bodies.

### Architecture

- The page receives a small `data/manifest.json` at build time and passes it to the client.
- The client renders a nested sidebar: courses → modules → chapters.
- When a chapter is selected, the client fetches the relevant `public/courses/NN.json` on demand, so large course payloads are not loaded upfront.
- The client fetches `public/search-index.json` on first search; it ranks results by fuzzy title/course matches and exact-phrase frequency inside the article body.
