# Volume 4 Verification

Overall status: **PASS**

Protocol baseline checked 2026-08-24: MCP 2026-07-28, A2A 1.0, and current official AG-UI documentation. Draft AG-UI interrupt behavior is labeled draft, and ACP is historical migration context only.

DOCX SHA-256: `d660fe5b35e07ac0e404858a78c0f18ccdc78aa51c710f1659edc752062a0280`

Rendered pages: `85`

## Automated checks

- PASS — docx_exists_and_nonempty: `33607625`
- PASS — pdf_exists_and_nonempty: `2792855`
- PASS — docx_zip_integrity: `OK`
- PASS — all_images_have_alt_text: `{'drawings': 25, 'blank_alt': 0}`
- PASS — substantive_word_count: `13108`
- PASS — all_24_visual_lessons_present: `[77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]`
- PASS — required_current_markers_present: `[]`
- PASS — no_placeholder_text: `[]`
- PASS — heading_hierarchy_present: `232`
- PASS — source_links_present: `['https://a2a-protocol.org/latest/specification/', 'https://blog.modelcontextprotocol.io/posts/2026-07-28/', 'https://blog.modelcontextprotocol.io/posts/mcp-roadmap/', 'https://docs.ag-ui.com/concepts/events', 'https://docs.ag-ui.com/introduction', 'https://modelcontextprotocol.io/specification/2026-07-28', 'https://www.jsonrpc.org/specification', 'https://www.rfc-editor.org/info/bcp14', 'https://www.rfc-editor.org/rfc/rfc6902']`
- PASS — tables_repeat_header_rows: `{'tables': 233, 'header_rows': 233}`
- PASS — rendered_page_count: `85`
- PASS — all_24_source_diagrams_present: `{'count': 24, 'bytes': 33823783}`
- PASS — structured_course_shape: `{'modules': 6, 'lessons': 24}`
- PASS — stability_labels_present: `['Architecture and testing pattern', 'Architecture decision', 'Capstone profile checked 2026-08-24', 'Draft AG-UI interrupt-aware lifecycle; isolate behind an adapter', 'Engineering practice', 'Historical migration; A2A is the current target', 'Mixed core and implementation choices', 'Official MCP extension', 'Official opt-in MCP extension', 'Stable A2A 1.0', 'Stable AG-UI event core', 'Stable AG-UI snapshot-delta pattern; replay policy is implementation-specific', 'Stable JSON-RPC foundation', 'Stable MCP 2026-07-28 core', 'Stable MCP core; progressive discovery is a roadmap direction', 'Stable core plus negotiated extensions', 'Stable events plus application UI policy', 'Stable foundation', 'Stable pattern']`

## Visual review

Every page was rendered to an image and inspected through 100% page renders and four-page contact sheets. Diagram labels, page boundaries, callouts, tables, images, footers, and final reference pages were checked. Two ambiguous generated visuals and one text-defective binding visual were replaced before publication.

## ZIP safety

The final packaging step creates explicit root and `diagrams/` directory entries, performs a CRC test, extracts into a new clean directory, and verifies every extracted file against the source SHA-256. This directly guards against the missing-diagrams-folder extraction problem seen in earlier bundles.
