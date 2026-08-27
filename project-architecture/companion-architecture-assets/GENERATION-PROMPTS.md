# Companion architecture diagrams

Generated with the built-in image-generation tool. Original PNG bytes are preserved.

Saved outputs:

- `E:/image-course/project-architecture/companion-architecture-assets/01-hybrid-overview.png`
- `E:/image-course/project-architecture/companion-architecture-assets/02-typescript-overview.png`

The guides also embed the existing MCP, RAG, and A2A diagrams unchanged. Their detailed prose identifies the optional Risk agent and distinguishes logical coordinator roles from deployed services.

## Hybrid architecture

Use case: infographic-diagram. Create a polished wide 16:9 educational architecture illustration, dark navy background, blue isometric servers and glass panels, cyan arrows, teal accents, crisp large white typography, generous spacing. No tiny text. Title "HYBRID ARCHITECTURE". Four large numbered panels left to right with single right-pointing arrows between adjacent panels. Panel 1 "BROWSER" subtitle "React workspace", laptop icon. Panel 2 "VERCEL" subtitle "Next.js UI + BFF", blue cloud icon. Panel 3 "PYTHON API" subtitle "Validate + persist", server icon. Panel 4 "PYTHON WORKFLOW" subtitle "Durable coordination", gears icon. Below panel 4 a bracket containing three compact tiles labeled "MCP", "RAG", "A2A"; bracket caption "Backend capabilities". Bottom full-width foundation band labeled "PostgreSQL + object storage" with subtitle "Owned data • durable events • receipts". Small footer "The browser displays progress. The backend owns the work." This is a simplified command path, no return arrows, no direct browser database connection. Exact labels only.

## TypeScript architecture

Use case: infographic-diagram. Create a polished wide 16:9 educational architecture illustration, dark navy background, blue isometric servers and glass panels, cyan arrows, teal accents, crisp large white typography, generous spacing. No tiny text. Title "TYPESCRIPT ARCHITECTURE". Four large numbered panels left to right with single right-pointing arrows between adjacent panels. Panel 1 "REACT WORKSPACE" subtitle "Submit • inspect • approve", laptop icon. Panel 2 "NEXT.JS API" subtitle "Authorize + persist", blue server icon. Panel 3 "DURABLE DISPATCH" subtitle "Outbox + reconciliation", inbox icon. Panel 4 "WORKFLOW DEVKIT" subtitle "Steps • waits • retries", gears icon. Below panel 4 a bracket containing three compact tiles labeled "MCP", "RAG", "A2A"; bracket caption "TypeScript capabilities". Bottom full-width foundation band labeled "PostgreSQL + object storage" with subtitle "Business state is separate from workflow history". Small footer "One language. Explicit service boundaries. Durable business rules." No direct browser database arrow. Exact labels only.
