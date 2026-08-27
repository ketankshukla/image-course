# FilePilot — TypeScript Counterpart

## At a glance

A TypeScript implementation can demonstrate the same architecture, but it still needs a local runtime to operate on personal files. Next.js and Vercel do not remove that requirement. Build this counterpart after the Python path works, using shared behavioral contracts rather than running two writers on one sandbox.

## What the diagram teaches

![A local coordinator separates read tools and proposals from the single operations writer. The pattern is unchanged when Python modules are replaced with TypeScript modules.](assets/architecture.svg)

The component boundaries describe responsibilities, not programming languages. In the TypeScript edition, `inventory.ts` observes files, `retrieval.ts` returns evidence, `planner.ts` proposes structured changes, and `operations.ts` owns execution. The React UI can reuse the same conceptual screens. The approval contract remains exactly as strict.

Maya's approved plan should have the same meaning in either implementation. If the Python engine rejects a changed source but the TypeScript engine moves it anyway, the two editions are not equivalent. Sharing JSON shapes alone is insufficient; share fixtures and expected outcomes too.

## Proposed separate repository

```text
filepilot-platform-ts/
  package.json
  apps/
    workspace/                  Local React/Next.js UI
    local-service/              Local API and worker lifecycle
  packages/
    contracts/                  Schemas and fixture types
    domain/                     Plans, policies, approval checks
    explorer/                   Bounded scan and metadata
    retrieval/                  Extraction and evidence search
    planner/                    Rules or model adapter
    operations/                 Journal and state machine
    filesystem-windows/         Reviewed OS-specific adapter
    mcp-adapter/                 Protocol mapping
    a2a-classifier/              Optional separate specialist
  tests/
    contract/
    recovery/
    windows/
```

Keep domain packages independent of the web framework. Importing a React component should never load a filesystem worker into a browser bundle. Server-only modules and package export boundaries should make inappropriate imports fail visibly during development.

## Map the responsibilities

| Python responsibility | TypeScript equivalent | Behavioral requirement |
|---|---|---|
| Data validation | Runtime schema validator | Reject unknown fields, not just compile-time type errors |
| Root registry | Local service module | IDs resolve only to approved roots |
| SQLite journal | Local database adapter | Durable intent and unique operation IDs |
| Filesystem adapter | Windows-specific implementation | No overwrite, identity checks, explicit unsupported cases |
| MCP adapter | Compatible SDK adapter | Same domain authorization as the CLI |
| Unit tests | TypeScript test runner | Same fixtures and denial outcomes |

TypeScript types disappear at runtime. A request from a browser or model must still be validated. Likewise, Node's path and filesystem utilities are not an authorization system. Never assume a `realpath` followed by `rename` closes all path races or provides consistent no-overwrite behavior across operating systems.

## Preserve the operations contract

Before enabling writes, build an adapter test suite on the actual supported Windows filesystem. Verify existing-target collisions, locked files, case-only names, junctions, unsupported reparse entries, and process crashes. If the selected Node API cannot provide the necessary semantics, use a reviewed native adapter or keep that operation unsupported. Do not weaken the policy to make a language comparison look complete.

A generic “copy then unlink” helper is not a drop-in replacement for same-volume movement. It introduces an interval with two copies, partial-copy failures, metadata preservation questions, and a separate source-removal decision. Cross-volume movement stays outside the first contract in both editions.

## Shared approval digest

Cross-language digest parity needs an explicit byte representation. Specify field order, string encoding, escaping, integer representation, and whether Unicode normalization is allowed. A Python serialization and JavaScript `JSON.stringify` are not automatically identical for every input. Prefer a documented canonicalization format and publish test vectors covering non-ASCII filenames and edge cases.

Within each implementation, store an immutable authoritative plan and its digest. The browser supplies a reference, not authority. If digest parity is not implemented, label approvals as local to their engine; never transfer one implementation's approval to the other.

## Deployment distinction

Ship the local service as a separately installed application with explicit OS permissions and a documented update path. Deploy only the documentation or a synthetic demo to Vercel. Do not place a background local worker inside a hosted request handler and claim it can monitor the user's machine.

## How to present it

Run the same collision and stale-source fixtures against both implementations. Show the matching refusal reasons before comparing the interfaces. The successful lesson is that the safety rules survive a change in language and framework.
