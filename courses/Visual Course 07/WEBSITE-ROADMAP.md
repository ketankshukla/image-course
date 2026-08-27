# Volume 7 Website Roadmap

## Goal

Turn Volume 7 into an interactive agent-security laboratory. Preserve the diagram-first teaching order, complete explanation, standards-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

## Recommended first release

1. Build a Next.js App Router site that reads `Volume 7 Course Content.json` at build time.
2. Create module, lesson, threat, identity, policy, tenant, audit, governance, glossary, and source routes.
3. Put the full explanation directly below each diagram and expose all states with text, not color alone.
4. Keep every attack demonstration synthetic and local; never ship real customer records, tokens, secrets, exploit payloads, or usable attack instructions.
5. Add keyboard navigation, local progress, adjustable text, high contrast, reduced motion, downloadable diagrams, and printable lessons.
6. Deploy to Vercel only after routes, images, alt text, links, heading order, focus behavior, responsive layouts, and synthetic failure scenarios pass.

## Interactive visual laboratories

- Threat-model canvas: place assets, identities, trust boundaries, attackers, and unacceptable outcomes.
- Instruction-authority sorter: classify system policy, developer rules, user intent, retrieved data, and hostile content.
- OAuth laboratory: inspect protected-resource metadata, authorization-server metadata, audience binding, PKCE, issuer validation, and scopes.
- Delegation chain viewer: follow Maya, the Acme agent, token exchange, workload identity, and one bounded tool authority.
- Policy decision playground: vary identity, tenant, tool, destination, amount, risk, and approval claims, then inspect the decision receipt.
- Transaction-binding lab: change the payee or amount after approval and observe invalidation.
- Tenant-isolation explorer: follow one tenant key through database, vector index, cache, queue, artifacts, logs, and deletion.
- Sandbox and egress simulator: choose file, browser, code, MCP App, destination, and data class, then observe allow, deny, redact, or quarantine.
- Card trust inspector: compare unsigned, signed, stale, extended, and unexpectedly changed discovery cards.
- Provenance graph: trace code, dependency, model, prompt, tool, policy, and configuration versions into one execution receipt.
- Privacy lifecycle designer: minimize collection, set purpose and retention, record consent, delete data, and prove downstream completion.
- Governance board: map NIST functions and OWASP Agentic risks to owners, controls, evidence, exceptions, and review dates.

## Accessibility definition of done

- Every diagram has meaningful alt text and a complete adjacent explanation.
- Every interactive control is keyboard reachable and exposes the same state without hover or animation.
- Status, identity, tenant, authority, permission, risk, denial, quarantine, and evidence always have text labels.
- Simulations provide pause, step, reset, and a reduced-motion mode.
- Example performance, cost, and reliability values are clearly labeled as scenarios, never measured project results.
