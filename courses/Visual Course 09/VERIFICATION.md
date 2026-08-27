# Volume 9 Verification

Overall status: **PASS**

Knowledge baseline checked 2026-08-25 against current primary specifications and official guidance. AG-UI uses the checked 2026-07-28 repository release; MCP Apps 2026-01-26 is stable; A2UI v0.9.1 is current while v1.0 remains a candidate; WCAG 2.2, WAI-ARIA 1.2, JSON Patch RFC 6902, CSP, Permissions Policy, and NIST frameworks are labeled by status and purpose.

DOCX SHA-256: `acaff4f6ad63483a32c6fd6b2b765a8923d304b0cb60c9089b8c5a9511dd3e16`

Rendered pages: `86`

## Automated checks

- PASS — docx_exists_and_nonempty: `32883413`
- PASS — pdf_exists_and_nonempty: `2650096`
- PASS — docx_zip_integrity: `OK`
- PASS — all_images_have_alt_text: `{'drawings': 25, 'blank_alt': 0}`
- PASS — substantive_word_count: `22225`
- PASS — all_24_visual_lessons_present: `[197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220]`
- PASS — required_current_markers_present: `[]`
- PASS — no_placeholder_text: `[]`
- PASS — heading_hierarchy_present: `233`
- PASS — primary_source_links_present: `['https://a2ui.org/', 'https://a2ui.org/specification/v0.9-a2ui/', 'https://apps.extensions.modelcontextprotocol.io/', 'https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/', 'https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html', 'https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html', 'https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html', 'https://docs.ag-ui.com/', 'https://docs.ag-ui.com/concepts/architecture', 'https://docs.ag-ui.com/concepts/capabilities', 'https://docs.ag-ui.com/concepts/events', 'https://docs.ag-ui.com/concepts/messages', 'https://docs.ag-ui.com/sdk/js/client/subscriber', 'https://docs.ag-ui.com/sdk/js/core/events', 'https://fastapi.tiangolo.com/advanced/websockets/', 'https://fastapi.tiangolo.com/tutorial/background-tasks/', 'https://github.com/ag-ui-protocol/ag-ui/releases', 'https://github.com/google/A2UI', 'https://html.spec.whatwg.org/multipage/iframe-embed-object.html#attr-iframe-sandbox', 'https://html.spec.whatwg.org/multipage/web-messaging.html', 'https://json-schema.org/draft/2020-12', 'https://modelcontextprotocol.io/extensions/apps/overview', 'https://modelcontextprotocol.io/specification/2026-07-28', 'https://nextjs.org/docs/app', 'https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming', 'https://nextjs.org/docs/architecture/accessibility', 'https://notifications.spec.whatwg.org/', 'https://react.dev/reference/react/useActionState', 'https://react.dev/reference/react/useOptimistic', 'https://www.nist.gov/itl/ai-risk-management-framework', 'https://www.nist.gov/privacy-framework', 'https://www.rfc-editor.org/info/rfc6902/', 'https://www.rfc-editor.org/rfc/rfc9457', 'https://www.w3.org/TR/CSP3/', 'https://www.w3.org/TR/IndexedDB-3/', 'https://www.w3.org/TR/WCAG22/', 'https://www.w3.org/TR/appmanifest/', 'https://www.w3.org/TR/permissions-policy-1/', 'https://www.w3.org/TR/service-workers/', 'https://www.w3.org/TR/wai-aria-1.2/', 'https://www.w3.org/TR/wai-aria-1.2/#progressbar', 'https://www.w3.org/TR/wai-aria-1.2/#status', 'https://www.w3.org/WAI/ARIA/apg/', 'https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/', 'https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/']`
- PASS — tables_repeat_header_rows: `{'tables': 234, 'header_rows': 234}`
- PASS — rendered_page_count: `86`
- PASS — all_24_source_diagrams_present: `{'count': 24, 'bytes': 33065951}`
- PASS — structured_course_shape: `{'modules': 6, 'lessons': 24}`
- PASS — pattern_status_labels_present: `['A2UI v0.9.1 is the checked current release while v1.0 remains a candidate; isolate versions behind an adapter', 'AG-UI event families are current; product event vocabulary remains application-specific', 'AG-UI snapshots and RFC 6902 deltas are current; conflict policy is an application responsibility', 'Browser permission and user-activation behavior is platform-dependent; design capability detection and refusal paths', 'Design capstone using the checked 2026-08-25 baseline; pin protocol versions and revalidate before implementation', 'Durable-evidence product pattern; protocol identifiers remain distinct', 'Established distributed-workflow and human-control pattern', 'Human-centered progress pattern using current AG-UI activity and lifecycle events', 'Human-control pattern; AG-UI interrupt capability is evolving and must remain versioned', 'Human-steering product pattern; implementation and protocol events remain application-specific', 'MCP Apps extension 2026-01-26 is stable; hosts and apps still negotiate optional capabilities', 'Measurement design and experiment policy are context-specific; all course numbers are illustrative unless explicitly measured later', 'Notifications require permission and platform support; product attention policy remains application-specific', 'Privacy obligations vary by jurisdiction and context; this course teaches product architecture, not legal advice', 'Reliable-stream design pattern built on stable identifiers and current browser capabilities', 'Resilient product and workflow pattern', 'Search implementation is product-specific; source currency and prerequisite truth require ongoing editorial ownership', 'Service Worker, IndexedDB, and Web App Manifest standards are current; offline behavior still varies by browser and storage policy', 'Stable error-design principles using RFC 9457 and accessible interaction patterns', 'Stable product-state pattern; framework helpers do not change the authority boundary', 'The content model is a product contract; version it independently from the website framework', 'WCAG 2.2 and semantic web patterns are stable baselines; test actual assistive technologies and device layouts', 'WCAG 2.2 is the current W3C baseline; ARIA patterns support implementation but require testing', 'Web security standards evolve; maintain threat models, dependency updates, browser tests, and defense in depth']`
- PASS — lesson_fields_complete: `24 lessons checked`

## Visual review

All twenty-four source diagrams were reviewed for spelling, arrow logic, teaching accuracy, and visual consistency before assembly. Volume 9 follows the established course convention: only functional teaching labels appear inside each image; diagram numbers and full titles appear only in document captions. The complete document was rendered page by page and inspected through full-page PNGs and contact sheets for clipping, overflow, blank pages, table boundaries, image placement, heading hierarchy, footers, links, and final reference pages.

## ZIP safety

PASS — the final archive contains 31 entries, including explicit `Visual Course Volume 9 - Complete Learning Bundle/` and `Visual Course Volume 9 - Complete Learning Bundle/diagrams/` directory entries. CRC validation passed. A clean extraction created all required directories and 24 diagram files. All 29 source files were verified byte-identical by SHA-256 after extraction. This directly guards against the missing-diagrams-folder extraction problem seen in an earlier bundle.
