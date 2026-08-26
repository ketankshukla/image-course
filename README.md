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

The site renders them in a searchable, sidebar-navigated course reader.

---

## 🏗️ Architecture

```
├── app/                  # Next.js App Router pages and components
├── lib/                  # Shared types and utilities
├── scripts/              # build_content.py: Markdown → JSON + WebP
├── data/                 # Lightweight navigation manifest
├── public/               # Generated courses, search index, and images
│   ├── courses/01.json   # Full course payload for volume 1
│   ├── images/*.webp     # Compressed diagrams
│   └── search-index.json # Full-text search index
├── Visual Course 01/     # Source Markdown, diagrams, and JSON specs
├── ...
└── Visual Course 10/
```

- **Source content** lives in `Visual Course NN/diagram-docs/` as Markdown.
- **Original diagrams** live in `Visual Course NN/diagrams/` as PNG.
- `npm run build:content` converts the PNGs to WebP and produces the JSON payloads used by the site.
- The client fetches `data/manifest.json` for navigation and lazy-loads each course's JSON when selected.

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
   - **Build Command:** `npm run build` (or `npx next build` if you want to skip content regeneration)
   - **Output Directory:** `dist` or default
   - **Install Command:** `npm install`

> **Note:** The course directories (`Visual Course NN/`) are **build inputs**, not deployable pages. Only the contents of `public/` (generated JSON + WebP images) and the Next.js app output are served by Vercel.

### About the large source assets

The original `*.docx`, `*.pdf`, and `*.zip` bundles in the course folders are **ignored by Git** and are not needed for the website build. They are kept out of the remote repo to keep it lightweight. The PNG diagrams are included because `build:content` uses them to generate the compressed WebP assets.

---

## 🔍 Features

- 📚 **10 courses, 244 lessons** with rich visual explanations
- 🖼️ **Diagram-first learning** — every lesson centers on a visual diagram
- 🔎 **Full-text search** across all courses and chapters
- 🌙 **Dark UI** designed for readability
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

The build script extracts these sections, compresses the diagrams, and writes a `public/courses/NN.json` file per course.

---

## 🧰 Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start the local dev server |
| `npm run build:content` | Parse Markdown, convert PNG → WebP, regenerate JSON |
| `npm run build` | Build content + create an optimized Next.js production build |
| `npm run start` | Serve the production build locally |

---

## 📝 License

© 2026 Ketan Shukla. All rights reserved.

The educational content and visual diagrams in this repository are the original work of the author. The Next.js application code may be used as a reference for building similar course sites.

---

## 🙌 Acknowledgments

Built with [Next.js](https://nextjs.org/), [Tailwind CSS](https://tailwindcss.com/), and a lot of diagrams.
