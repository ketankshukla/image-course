# Companion document checks

Both Markdown guides were converted to standalone HTML using Pandoc and the existing architecture stylesheet. The original documents and course website were not modified.

- Hybrid guide: 15 numbered chapters and four embedded diagrams.
- TypeScript guide: 17 numbered chapters and four embedded diagrams.
- All embedded PNG bytes match their source files.
- Internal navigation targets exist and IDs are unique.
- No external scripts, stylesheets, or image dependencies are required to render the HTML.
- Markdown fences are balanced; machine-specific paths are absent from the teaching text.
- Embedded JavaScript passes Node syntax checks.
- The two new overview diagrams and three reused diagrams were visually inspected.
- The browser preview was not exercised: the earlier local-file navigation was blocked by browser security policy. No alternate preview route was used to bypass that restriction. Layout and interaction checks here are static, not an end-to-end browser certification.

From the `docs/case-studies/acme` folder, rebuild with `companion-architecture-assets/rebuild.ps1`; rerun structural checks with `python companion-architecture-assets/verify.py`.
