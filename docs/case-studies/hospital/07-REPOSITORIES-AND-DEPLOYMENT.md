# HarborCare — Repositories and Deployment

## Keep teaching material, application code, and live state separate

This document describes future application repositories. The files created now are learning documents inside `image-course`; no HarborCare app or cloud service is being provisioned.

## 1. Proposed local layout

```text
parent-folder/
├── image-course/                       This learning repository
│   ├── courses/                        Ten course volumes and their assets
│   └── docs/case-studies/
│       ├── acme/
│       └── hospital/
├── acme-agent-platform/                Future Acme Python/hybrid app
├── harborcare-privacy-platform/        Future HarborCare Python/hybrid app
└── harborcare-privacy-platform-ts/     Optional later TS counterpart
```

Each application has one Git repository at its root. P1–P5 are modules and demonstrable projects within that repository, not five nested repositories. Do not place a new `.git` directory inside a course lesson folder.

## 2. Why not add hospital patients to Acme's database?

HarborCare has different contracts, risks, fixtures, and release semantics. A financial receipt and a disclosure receipt are not interchangeable. Reusing ideas is useful; sharing a live data store and permissions just to avoid creating another repo is not.

Start with independent application repos and small explicit contract fixtures. If a policy or protocol helper later becomes genuinely reusable, extract it as a versioned library after its consumers and compatibility rules are clear.

## 3. Deployment map

![The web, policy/release gateway, evidence service, agents, workflow, and synthetic receiver are separate runtime responsibilities backed by scoped persistent stores.](assets/03-system-map.svg)

| Runtime | Python/hybrid deployment | TypeScript deployment |
|---|---|---|
| Reviewer UI | Next.js on Vercel | Next.js on Vercel |
| Case and policy APIs | Python HTTP services | TypeScript server entry points |
| MCP gateway/release domain | Restricted Python service | Restricted TypeScript service |
| Evidence processing | Python API/ingestion worker | Server-only package and bounded jobs initially |
| Specialist agents | Independent Python A2A services | Independent TypeScript A2A services |
| Orchestration | Database-backed Python workers | Workflow DevKit plus application records |
| External destination | Local/private synthetic receiver | Local/private synthetic receiver |
| Data | Isolated PostgreSQL roles and private objects | Same ownership model, separate environment |

One repo can build multiple services. Each service gets a release identifier, health signal, credentials, and rollback strategy. A Git commit does not atomically update every running service.

## 4. Environments

Local development uses synthetic fixtures and a test receiver. Integration previews use isolated credentials and resettable synthetic datasets. The production **demo** has authenticated reviewer controls, quotas, curated fixtures, and no arbitrary patient upload or egress.

Do not describe a synthetic hosted demo as ready for real protected health information. Before that expansion, review vendor agreements, access controls, retention, audit, incident handling, model data use, regional requirements, and all applicable law with the responsible organization.

## 5. Release procedure

Run policy unit tests, protocol integration, wrong-patient tests, field-leakage canary checks, and revocation/recovery scenarios before building. Apply additive migrations with one executor. Deploy compatible provider services before consumers, then run a synthetic disclosure smoke test.

Record commit, image/deployment IDs, contract version, policy bundle version, and migration version. Paused jobs and approved packets may depend on old versions. Do not delete compatibility code while those records remain active without an explicit migration or expiry plan.

Keep source policy fixtures in Git, but do not keep live patient records, raw audit exports, packet bodies, or secrets there. Even hashes and IDs can remain sensitive in a real environment.

## 6. Deployment acceptance

Verify that every service points to the same intended environment, recipients are allowlisted by stable identity, model calls contain only authorized context, logs contain no canary secrets, and queued releases stop under revoked authority. Restore a backup into an isolated environment with outbound delivery disabled before starting workers.

The final proof is not “the website loads.” It is “the right recipient gets the exact permitted packet, the wrong recipient gets nothing, and uncertainty is handled without widening disclosure.”
