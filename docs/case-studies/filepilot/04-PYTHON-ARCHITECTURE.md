# FilePilot — Python Reference Architecture

## At a glance

Use one Python application repository with modules that have clear responsibilities. Start with a CLI, SQLite, and a local single-writer worker. MCP and a browser API are adapters around those modules; they are not the place where permission rules live. A model is optional.

## What the diagram teaches

![The workspace uses the coordinator and contracts. Explorer, finder, and planner supply observations and proposals. The operations engine alone changes the sandbox and records outcomes.](assets/architecture.svg)

Maya's request enters through the workspace. The coordinator authenticates her local session and resolves the selected root grant. It calls the explorer to obtain an inventory. The finder can supply document evidence. The planner produces a proposal referencing file IDs and allowed destination IDs.

The coordinator persists the proposal so the UI can display a stable revision. Approval is recorded separately. When execution is requested, the coordinator submits the approved job to the operations engine. The engine loads the authoritative plan from storage; it never executes the browser's copy of the plan. This prevents a reviewer from approving one object while a modified request submits another.

The engine records intent, checks the source and destination through a filesystem adapter, attempts the move, and checks the result. It then invalidates the file's old search location. A successful move must not leave a citation pointing to a nonexistent path, although its stable file ID may remain unchanged if identity has been verified.

## Proposed repository structure

```text
filepilot-platform/
  pyproject.toml
  README.md
  src/filepilot/
    cli.py
    contracts.py
    policy.py
    roots.py
    inventory.py
    fingerprints.py
    extraction.py
    retrieval.py
    planner.py
    approvals.py
    operations.py
    reconciliation.py
    audit.py
    adapters/
      filesystem_windows.py
      mcp_server.py
      http_api.py
      classifier_a2a.py
    storage/
      database.py
      migrations/001_initial.sql
  tests/
    unit/
    integration/
    protocol/
    recovery/
  fixtures/                     Synthetic text and expected outcomes
  apps/workspace/               Optional local Next.js interface
  contracts/                   Language-neutral schemas
  docs/                        Implementation notes, not private traces
```

Runtime state and managed files live outside this repository. Do not make the repository itself the first managed root. Otherwise a cleanup can move the program's own database or source files while it is running.

## File responsibilities and calls

| File | Principal functions to implement | Calls |
|---|---|---|
| `roots.py` | `grant_root`, `authorize_root`, `revoke_root` | Policy and root registry |
| `inventory.py` | `scan_root`, `get_file_record` | Root checks, read-only filesystem adapter |
| `fingerprints.py` | `fingerprint`, `same_revision` | Bounded byte reads and metadata |
| `extraction.py` | `extract_text`, `split_passages` | Approved readers, resource limits |
| `retrieval.py` | `index_file`, `search_evidence` | Current grants, revision checks, index |
| `planner.py` | `propose_plan`, `validate_plan` | Allowed destinations, evidence IDs |
| `approvals.py` | `approve_revision`, `authorize_execution` | Current identity, digest, expiry |
| `operations.py` | `claim_job`, `execute_operation` | Approval checks, journal, OS adapter |
| `reconciliation.py` | `reconcile_operation`, `propose_reverse_plan` | Journal and current filesystem observations |

The read tools must not import the mutating adapter methods. Protocol adapters call application services; application services do not call protocol adapters. That dependency direction keeps a protocol upgrade from changing the core rules.

## Storage contract

Use tables for roots, files, document revisions, chunks, plans, plan operations, approvals, jobs, and operation events. A plan is immutable once presented for approval; edits create a new revision. Enforce uniqueness on an execution request's idempotency key within its principal/root scope and record the associated plan digest. Reusing a key for a different plan is an error, not a new job.

The journal records operation ID, expected source identity, target, intent time, observed result, and safe error category. Full paths may be necessary in the private local database for recovery; they should not be copied into public logs. Protect the database using local OS permissions and an appropriate encrypted-storage strategy for the intended deployment. Ordinary SQLite is not inherently an encrypted vault.

## Recovery and concurrency

Use one writer initially. A process-level ownership lock prevents two workers from manipulating the same sandbox. A crashed worker's jobs must enter reconciliation before they can be resumed. An in-process lock alone does not protect against a second process or another application changing files.

The adapter must report facts rather than optimistic booleans: source missing, destination present with expected identity, destination occupied by different content, permission denied, and unsupported operation are distinct observations. For ambiguous states, the engine requests review. A background retry should never invent a new target name.

## Acceptance gate

You can test the domain without running MCP, a browser, or a model. Protocol integration tests then prove that the same denials occur through external adapters. Recovery tests terminate the writer at known points and inspect both journal state and actual files after restart. This is an architectural target, not a statement that those tests already exist in an application repository.

## How to present it

Trace one approved operation through `approvals`, `operations`, the filesystem adapter, and `reconciliation`. Then replace the planner with a deterministic fake and show that the safety contract is unchanged.
