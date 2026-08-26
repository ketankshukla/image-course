# Verification Report

## Final artifacts

- `Visual Course - MCP ACP A2A and RAG - 2026 Edition.docx`
- `Visual Diagram Library - MCP ACP A2A RAG.zip`
- `Diagram Library Guide and Prompts.md`

## Word course checks

- Final Microsoft Word render: 43 pages, US Letter.
- Visual inspection: all 43 pages inspected from the final v5 render.
- Layout result: no blank pages, clipped diagrams, orphaned checkpoints, or unintended page breaks.
- DOCX ZIP integrity: passed (`testzip = None`).
- Embedded media files: 30.
- Drawing instances: 31 (30 lesson diagrams plus the cover reuse).
- Drawing instances with non-empty alt text: 31 of 31.
- Heading paragraphs: 76.
- Tables/callout structures: 137.
- Accessibility audit: 0 high, 0 medium, and 0 low findings.

## Diagram-library checks

- PNG diagrams: 30.
- Dimensions: 1671×941 or 1672×941 pixels; both are approximately 16:9.
- ZIP entries: 31 (30 diagrams plus the guide/prompt file).
- ZIP integrity: passed (`testzip = None`).

## Protocol baseline represented in the course

- MCP: specification revision 2026-07-28.
- A2A: 1.0 target model.
- ACP: historical lineage and migration vocabulary, not a new implementation target.
- RAG: retrieval architecture pattern, evaluated through retrieval, faithfulness, coverage, and latency.

## SHA-256

```text
A96436D9A69196656CBBE77F293F9E57441755AA1A949A1F9C1DEBFB25A6B71D  Visual Course - MCP ACP A2A and RAG - 2026 Edition.docx
5B35D6D5ABE66DAEB3A615944074BDEB0387D88517A3773AAF8415059614E18B  Visual Diagram Library - MCP ACP A2A RAG.zip
6FD1CEA24815867C5D9D68224422352DAA5BB09ACAB3E00164164E2E19914B4D  Diagram Library Guide and Prompts.md
```

