# Manual-build series verification

## Delivered

- One start page and seven workbooks, each in Markdown and standalone HTML.
- Approximately 12,300 words across the series.
- Eight diagram placements: three new precise SVG teaching diagrams and five reused architecture images, embedded in the HTML.
- File/function build ledgers, implementation algorithms, small code exercises, test matrices, troubleshooting, and production-demo gates.

## Checks performed

- All eight HTML files exist and parse through the structural checks.
- Internal anchors and relative document links resolve.
- All embedded images match their source bytes.
- HTML requires no external image, stylesheet, or JavaScript files for rendering.
- Embedded JavaScript parses, Markdown fences are balanced, and SVG XML is valid.
- Five pure-Python exercises pass 23 explicit checks.
- The TypeScript money-formatting exercise transpiles and passes four checks using the workspace TypeScript compiler.
- All three new SVG diagrams were rasterized for visual inspection; labels and layouts were checked.

## Limits

The full application has not been scaffolded, installed, integrated, or deployed. Protocol adapters, database transactions, auth integrations, workflow runtime behavior, and cloud configuration remain implementation exercises. Small-code checks do not certify production readiness. The TypeScript sections are translation plans, not a second complete line-by-line implementation manual.

Browser interaction testing of the HTML was not performed. The earlier local-file browser security restriction was not bypassed; document validation here is structural and diagram-level.

## Repeatable checks

From the image-course workspace, run:

```powershell
& docs/case-studies/acme/manual-build/assets/rebuild.ps1
node docs/case-studies/acme/manual-build/assets/verify.cjs
python docs/case-studies/acme/manual-build/assets/verify_exercises.py
```

No application dependencies were installed or application repositories created by producing these documents. Temporary PNGs used for diagram inspection are not deliverables.
