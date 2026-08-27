# Build FilePilot — Testing, Packaging, and a Production Demo

## At a glance

Finish with two clearly labelled deliverables: a restricted local sandbox application and, optionally, a public simulation using synthetic data. Neither should imply unrestricted access to real folders. A production-quality demonstration is reproducible, honest about its limits, and supported by test evidence.

## What the diagram teaches

![Public teaching and simulation are separate from the private local service and files. Optional remote inference requires a distinct transfer decision.](../assets/boundaries.svg)

The local application demonstrates actual supported operations. The public simulation demonstrates the user experience without connecting to a visitor's drive. Both are valuable, but they prove different things. Labeling them accurately builds more trust than making the hosted demo appear to control a real computer.

## 1. Build a release checklist

| Area | Required evidence |
|---|---|
| Core rules | Unit tests for approval, scope, expiry, revision, and collision |
| Filesystem boundary | Windows-specific tests for unsupported entries, locks, and identity checks |
| Protocols | Real MCP calls and, if present, A2A lifecycle tests |
| Retrieval | Excluded-root, revoked-grant, stale-source, and injection tests |
| Recovery | Process termination at every documented journal/move gap |
| UI | Keyboard review, mobile layout, repeat clicks, reconnect behavior |
| Privacy | No real paths or content in public logs, screenshots, bundles, or fixtures |
| Packaging | Fresh-machine installation, startup, update, and uninstall checks |

A skipped test remains a limitation. Report which operating system and filesystem were tested, rather than presenting one green CI badge as proof of portability.

## 2. Keep configuration explicit

Support separate development, local-demo, and hosted-simulation configurations. Local-demo mode permits only a configured disposable sandbox and has remote model calls disabled. Hosted simulation uses synthetic fixture state and contains no filesystem bridge. Fail startup if a hosted deployment accidentally enables local real-file mode.

Record dependency versions and lockfiles. Document the supported runtime versions and database schema. Never commit local session secrets, real root grants, index databases, approval records, or private logs. Inspect the built artifacts as well as the source repository for accidental data inclusion.

## 3. Make state upgrades recoverable

Version database migrations and test them on synthetic copies. Refuse to run with an unknown newer schema rather than guessing how to interpret approvals. Do not reuse old approval records after a policy change without an explicit compatibility decision; invalidating and reapproving is safer for the first implementation.

Keep backups of application state where appropriate, but explain that the journal is not a file backup. A successful database restore does not recreate a deleted document. Permanent deletion remains unsupported, and a backup strategy for real files must be independent of the assistant.

## 4. Publish measured evidence

Record scan duration for a defined fixture count and size, extraction failures, retrieval relevance on labelled queries, denied unsafe operations, recovery outcomes, and UI task-completion observations. Include hardware and environment notes where they affect performance. State targets separately from measured results.

Log operation IDs, state transitions, timings, and safe error categories. Detailed paths may exist in the protected local journal for recovery, but must not be sent to a public monitoring service by default. Avoid logging entire tool arguments, prompts, excerpts, or model responses.

## 5. Demonstrate the system in six scenes

1. Show a fresh synthetic sandbox and the explicit root grant.
2. Run a scan, inspect a duplicate group, and find one relevant document passage.
3. Review a proposal containing both a confident suggestion and an unchanged ambiguous file.
4. Approve a move, execute it, and verify its actual destination.
5. Change another file after approval and show the engine block the stale operation.
6. Inject a crash after a move, restart, and show reconciliation rather than a blind retry.

End by showing a reverse plan blocked by an occupied original location. This makes the limitations of undo concrete. No real filenames, personal screenshots, or private documents are needed to tell the story.

## 6. What must happen before real-folder use

Commission a focused review of the Windows adapter, race handling, reparse-point policy, hard links, ACLs, metadata, external references, and update mechanism. Expand parser support only with isolation and resource limits. Start any real-user pilot with backups, read-only mode, a narrow allowlist, and supervised approved writes.

Cross-volume movement, cloud synchronization, directory moves, and unattended schedules each require a new design and test matrix. They are not small toggles to enable after the demo works.

## Completion statement

When these gates pass in the future implementation, you can accurately say: “FilePilot demonstrates local, approval-bound file organization with revision checks and crash reconciliation on a documented sandbox configuration.” Do not claim general-purpose safe automation or compliance certification based on these workbooks alone.
