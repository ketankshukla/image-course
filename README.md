# 🎨 Visual Agent Course

A **Next.js 15 + TypeScript + Tailwind CSS** learning platform for the *Visual Agent Course* — a complete, diagram-first curriculum covering agentic product design, protocols, RAG, multi-agent workflows, security, and production deployment.

[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-blue?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3-38bdf8?logo=tailwindcss)](https://tailwindcss.com/)

---

## 🚀 What is this?

This repo contains the **website source** and the **course content** for 10 visual volumes:

| Volume | Theme | Lessons |
|--------|-------|---------|
| **01** | Agent Foundations | 30 |
| **02** | Build Your First Agent System | 16 |
| **03** | Durable Agent Protocols (MCP, A2A, AG-UI) | 30 |
| **04** | Production Agent Systems | 24 |
| **05** | Knowledge Systems & Advanced RAG | 24 |
| **06** | Durable Orchestration & Multi-Agent Workflows | 24 |
| **07** | Agent Identity, Security & Governance | 24 |
| **08** | Evaluation, Observability & AgentOps | 24 |
| **09** | Agentic Product Design & Human Control | 24 |
| **10** | Enterprise Architecture & Dual-Stack Project Blueprint | 24 |

Each lesson is built around a single **visual diagram** and includes:

- `At a glance` summary
- `What the diagram teaches` — narrative walkthrough
- `Composition` and `Element by element` breakdown
- `Colour and flow semantics`
- `How to present it` — facilitation guide
- `Case study`, `Lab and checkpoint`
- `Glossary`, `Sources`, and `Related lessons`

The site renders them alongside 14 Acme guides, 16 HarborCare guides, 16 FilePilot guides, 11 EvidenceDesk lessons and 20 library guides/workshops. Navigation is grouped into Courses, Case Studies and Library Guides; search spans all 321 published articles.

---

## 🏗️ Architecture

```
├── app/                  # Next.js App Router pages and components
├── lib/                  # Shared types and utilities
├── scripts/              # build_library.mjs: Node-only Markdown → JSON + WebP
├── data/                 # Lightweight navigation manifest
├── public/               # Generated courses, search index, and images
│   └── library/          # Hashed collections, flattened WebP images and search
├── courses/             # Ten source volumes, each with its own assets
│   ├── Visual Course 01/
│   └── ... Visual Course 10/
└── docs/                # Case studies, general planning, folder guide
    ├── case-studies/acme/
    ├── case-studies/hospital/
    ├── case-studies/filepilot/
    ├── case-studies/evidence-desk/
    └── general/
```

- **Source content** lives in `courses/Visual Course NN/diagram-docs/` as Markdown.
- **Original diagrams** live in `courses/Visual Course NN/diagrams/` as PNG.
- `npm run build:content` prepares PNG/SVG images as standalone flattened WebP files and renders all published Markdown. Originals are preserved.
- The page receives `data/manifest.json` at build time and lazy-loads collection JSON through content-hashed URLs.
- Case-study folders with `collection.json` are discovered automatically. Only explicitly listed documents are published.

---

## 🛠️ Local Development

```bash
# Install dependencies
npm install

# Build course content (converts PNG → WebP + JSON)
npm run build:content

# Run the dev server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the site.

### Build for production

```bash
npm run build
```

This runs `build:content` followed by `next build`.

---

## 🌐 Deployment

### Deploy to Vercel from GitHub

1. Push this repo to GitHub.
2. Import the repo in [Vercel](https://vercel.com/new).
3. Keep the default Next.js settings:
   - **Build Command:** `npm run build` (do not skip content generation)
   - **Output Directory:** Next.js default; do not set `dist`
   - **Install Command:** `npm ci`

The same Node-only build runs locally and on Vercel. No Python or Pandoc installation is required for the website. `.vercelignore` excludes standalone HTML and legacy generated assets from uploads, but retains source Markdown, manifests and original diagrams. Hashed library assets receive immutable cache headers. No live deployment is performed by running a local build.

> **Note:** The course directories (`courses/Visual Course NN/`) are **build inputs**, not deployable pages. Only the contents of `public/` (generated JSON + WebP images) and the Next.js app output are served by Vercel.

## Reading documents

- [Folder organization and document map](docs/FOLDER-STRUCTURE.md) · [HTML](docs/FOLDER-STRUCTURE.html)
- [Publishing future case studies](docs/PUBLISHING-CASE-STUDIES.md) · [HTML](docs/PUBLISHING-CASE-STUDIES.html)
- [Hospital privacy case study](docs/case-studies/hospital/00-START-HERE.html)
- [Acme manual-build series](docs/case-studies/acme/manual-build/00-START-HERE.html)
- [Acme beginner guide](docs/case-studies/acme/THE-WHOLE-PROJECT-IN-PLAIN-ENGLISH.html)

These local reading editions remain available. Their published Markdown counterparts are now integrated into the website reader through explicit collection manifests; `docs/` itself is not exposed as a static directory. Original Word/PDF/ZIP files remain local under the existing Git ignore policy.

### About the large source assets

The original `*.docx`, `*.pdf`, and `*.zip` bundles in the course folders are **ignored by Git** and are not needed for the website build. They are kept out of the remote repo to keep it lightweight. The PNG diagrams are included because `build:content` uses them to generate the compressed WebP assets.

---

## 🔍 Features

- 📚 **10 courses, 244 lessons** with rich visual explanations
- 🖼️ **Diagram-first learning** — every lesson centers on a visual diagram
- 🔎 **Full-text search** across all courses and chapters
- 🗂️ **Three library shelves** with case-study reading paths and build workbooks
- 🔍 **Diagram enlargement** and in-page contents for long guides
- 📱 **Responsive layout** for desktop and tablet
- ⚡ **Lazy-loaded course data** for fast first load

---

## 📂 Course Content Format

Each lesson is a Markdown file following this structure:

```markdown
# Diagram NNN — Title

![alt](../diagrams/NNN-slug.png)

## At a glance
## What the diagram teaches
## Composition
## Element by element
## Colour and flow semantics
## How to present it
## Case study
## Lab and checkpoint
## Glossary
## Sources
## Related lessons
```

Course files also retain their existing metadata block and separator after the first diagram. The build extracts that metadata, preserves lesson/module numbering, and writes a hashed collection file under `public/library/collections`. See existing lessons for the complete source format.

---

## 🧰 Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start the local dev server |
| `npm run build:content` | Parse Markdown, convert PNG → WebP, regenerate JSON |
| `npm run verify:content` | Check all published content, image flattening, links and search |
| `npm run lint` | Check React and TypeScript source |
| `npm run build` | Build content + create an optimized Next.js production build |
| `npm run start` | Serve the production build locally |

---

## 📝 License

© 2026 Ketan Shukla. All rights reserved.

The educational content and visual diagrams in this repository are the original work of the author. The Next.js application code may be used as a reference for building similar course sites.

---

## 🙌 Acknowledgments

Built with [Next.js](https://nextjs.org/), [Tailwind CSS](https://tailwindcss.com/), and a lot of diagrams.
