# Volume 7 Verification

Overall status: **PASS**

Knowledge baseline checked 2026-08-24 against current primary specifications and official guidance. MCP examples use protocol release 2026-07-28 and current authorization guidance; A2A examples use 1.0. NIST AI RMF 1.0, OWASP Agentic Top 10 2026, stable OAuth standards, implementation patterns, and active MCP roadmap items are labeled separately.

DOCX SHA-256: `85c24f56bf6915e709ec246a2cf603913eedbf2b04df93fcddcde86c121fc6c1`

Rendered pages: `86`

## Automated checks

- PASS — docx_exists_and_nonempty: `33547637`
- PASS — pdf_exists_and_nonempty: `2916357`
- PASS — docx_zip_integrity: `OK`
- PASS — all_images_have_alt_text: `{'drawings': 25, 'blank_alt': 0}`
- PASS — substantive_word_count: `18797`
- PASS — all_24_visual_lessons_present: `[149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172]`
- PASS — required_current_markers_present: `[]`
- PASS — no_placeholder_text: `[]`
- PASS — heading_hierarchy_present: `233`
- PASS — primary_source_links_present: `['https://a2a-protocol.org/latest/specification/', 'https://airc.nist.gov/airmf-resources/airmf/5-sec-core/', 'https://apps.extensions.modelcontextprotocol.io/api/documents/csp-and-cors.html', 'https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/', 'https://blog.modelcontextprotocol.io/posts/mcp-roadmap/', 'https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html', 'https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html', 'https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html', 'https://cheatsheetseries.owasp.org/cheatsheets/Transaction_Authorization_Cheat_Sheet.html', 'https://csrc.nist.gov/pubs/sp/800/207/final', 'https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/', 'https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices', 'https://modelcontextprotocol.io/extensions/apps/overview', 'https://modelcontextprotocol.io/extensions/auth/overview', 'https://modelcontextprotocol.io/specification/2026-07-28', 'https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization', 'https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery', 'https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration', 'https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations', 'https://modelcontextprotocol.io/specification/2026-07-28/changelog', 'https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf', 'https://slsa.dev/spec/v1.2/', 'https://spiffe.io/docs/latest/spiffe-specs/', 'https://www.nist.gov/itl/ai-risk-management-framework', 'https://www.nist.gov/privacy-framework', 'https://www.openpolicyagent.org/docs/management-decision-logs', 'https://www.rfc-editor.org/rfc/rfc7636', 'https://www.rfc-editor.org/rfc/rfc8693', 'https://www.rfc-editor.org/rfc/rfc8707', 'https://www.rfc-editor.org/rfc/rfc9207', 'https://www.rfc-editor.org/rfc/rfc9396', 'https://www.rfc-editor.org/rfc/rfc9449', 'https://www.rfc-editor.org/rfc/rfc9700', 'https://www.rfc-editor.org/rfc/rfc9728']`
- PASS — tables_repeat_header_rows: `{'tables': 234, 'header_rows': 234}`
- PASS — rendered_page_count: `86`
- PASS — all_24_source_diagrams_present: `{'count': 24, 'bytes': 33751510}`
- PASS — structured_course_shape: `{'modules': 6, 'lessons': 24}`
- PASS — pattern_status_labels_present: `['Accountability and incident-evidence pattern', 'Capstone architecture', 'Core agent-security control', 'Core containment pattern; MCP Apps profile-specific', 'Core data-and-action defense', 'Core multi-tenant security contract', 'Core outbound-control pattern', 'Core secure-tool pattern', 'Cross-layer isolation pattern', 'Current MCP 2026-07-28 · A2A 1.0', 'Current MCP authorization profile', 'High-impact action control', 'Identity foundation', 'Mature authorization pattern', 'Mature secrets-management practice', 'NIST AI RMF 1.0; revision underway', 'OWASP Agentic Top 10 for 2026', 'Organizational governance pattern', 'Privacy engineering foundation', 'Stable OAuth standard; active MCP roadmap direction', 'Stable standards plus evolving MCP agent-identity work', 'Supply-chain assurance pattern', 'Threat-model analysis pattern', 'Threat-model foundation']`
- PASS — lesson_fields_complete: `24 lessons checked`

## Visual review

All twenty-four source diagrams were reviewed for spelling, arrow logic, teaching accuracy, and visual consistency before assembly. Volume 7 follows the established course convention: only functional teaching labels appear inside each image; diagram numbers and full titles appear only in document captions. The complete document was rendered page by page and inspected through full-page PNGs and contact sheets for clipping, overflow, blank pages, table boundaries, image placement, heading hierarchy, footers, links, and final reference pages.

## ZIP safety

**PASS.** The final archive contains 31 entries: two explicit directory entries, five top-level learning artifacts, and twenty-four PNG diagrams. It passed its CRC test, extracted into a newly created clean directory, recreated the `diagrams/` folder, and produced all 29 source files byte-for-byte identically according to SHA-256. This directly guards against the missing-diagrams-folder extraction problem seen in an earlier bundle.
