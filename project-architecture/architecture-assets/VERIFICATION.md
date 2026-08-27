# Architecture guide verification

- Markdown: 19 numbered chapters, covering all five portfolio projects.
- Diagrams: six final original PNGs, visually inspected; retrieval topology, recovery amount, and runtime grouping corrected during inspection.
- HTML: all six PNGs embedded byte-for-byte; no external CSS, JavaScript, fonts, or image dependencies.
- Markdown image targets: all exist.
- HTML internal anchors: all resolve; no duplicate IDs.
- Markdown code fences: balanced.
- Inline JavaScript: syntax checked with Node's parser; not browser-executed.
- Browser visual/interaction verification: not performed. Browser security policy blocked the local-file URL. No workaround attempted.
- Scope: architecture documentation only; no application services implemented, launched, or represented as tested.

From the `project-architecture` folder, rebuild with `architecture-assets/rebuild.ps1`; verify with `python architecture-assets/verify_document.py`.
