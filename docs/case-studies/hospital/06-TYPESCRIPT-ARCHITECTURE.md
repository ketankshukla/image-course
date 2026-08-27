# HarborCare — Full TypeScript Counterpart

## One application language, unchanged privacy boundaries

This alternative uses TypeScript for web code, policy functions, retrieval adapters, agents, and orchestration. It is a separate implementation with separate synthetic data. It does not run alongside the Python coordinator against the same disclosure.

## 1. At a glance

![Policy and release enforcement remain separate from web presentation, retrieval, and specialist reasoning regardless of language.](assets/03-system-map.svg)

TypeScript types catch many development mistakes, but network JSON still needs runtime validation. A shared package does not give every service the same permissions. The release service remains the only component authorized to dispatch protected packets.

## 2. Proposed repository

```text
harborcare-privacy-platform-ts/
├── apps/
│   ├── web/                  Next.js requests, review UI, workflow entry points
│   ├── mcp-service/          Controlled patient views and release commands
│   ├── scheduling-agent/    Independent A2A service
│   ├── claims-agent/        Independent A2A service
│   ├── transport-agent/     Independent A2A service
│   └── receiver-simulator/  Synthetic recipient only
├── packages/
│   ├── contracts/
│   ├── policy/
│   ├── disclosure-domain/
│   ├── rag/
│   ├── identity/
│   ├── protocol-clients/
│   ├── persistence/
│   └── audit/
├── database/migrations/
├── fixtures/
└── tests/{policy,protocol,workflow,e2e}/
```

The deployment provides each service its own restricted database connection. The shared persistence package contains helpers, not an embedded administrator password.

## 3. Policy and packet functions

Write `evaluateDisclosure(context, policy)` as a deterministic decision function over verified context. Write `projectFields(record, allowedPaths)` to construct a new typed packet. `validatePacket(packet, decision)` rejects extra fields, mismatched patient/recipient, and stale policy bindings.

Use runtime schemas for every input and artifact. Define canonical JSON encoding for packet digests across Python and TypeScript: stable field selection/order, consistent null rules, Unicode handling, timestamps, and numeric bounds. A hash mismatch must cause review, not an automatic attempt to find a more permissive serialization.

Public information lives in a separate corpus. RAG scope is resolved before retrieval, and agents receive scoped task inputs. Do not rely on TypeScript's compile-time interfaces to strip unexpected fields received over the network.

## 4. Durable orchestration

Use Workflow DevKit for durable TypeScript steps and waits, instead of recreating the Python scheduler. Keep external I/O in bounded steps and preserve references rather than storing entire charts in execution history. Pin and test the selected runtime and SDK versions when implementing.

The case transaction writes request plus outbox. A bounded dispatcher starts the runtime and records its run ID. An uncertain start can create duplicate attempts; application ownership/version checks prevent both from advancing one request. Stable task and release keys protect external actions.

Approval is persisted before its notification. A hook wakes the workflow, but the workflow rereads the authoritative decision. An arbitrary hook token or an `approved: true` event does not authorize disclosure. Review completion, expiry, and revocation all require explicit state transitions.

## 5. Release transaction and external delivery

![The release gate rechecks current authority and packet binding before dispatch; acknowledgement uncertainty and revocation have distinct paths.](assets/04-release-lifecycle.svg)

The disclosure-domain transaction checks the grant, recipient, packet digest, policy/relationship revisions, and release identity. It records an in-flight attempt under a generation check. The network send is a separate operation; do not imply that a database commit proves delivery.

The receiver simulator accepts only configured synthetic recipient credentials and the expected envelope schema. It deduplicates by recipient plus release ID, compares the packet digest, and returns the original receipt for matching repeats.

When acknowledgement is missing, query status first. If a replay is permitted and still authorized, use the original packet and key. If authority is now revoked, do not retransmit contents. Escalate unresolved state rather than weakening the gate to finish the demo.

## 6. Deployment design

Each app entry point can be deployed independently from one repo. Vercel is the proposed web host and a candidate for compatible bounded TypeScript services. Test the actual MCP/A2A transport, authentication, and external state handling. If a chosen adapter requires persistent process-local state, change the adapter or use a suitable persistent host.

No patient data belongs in public environment variables. Preview URLs, service credentials, database roles, and receiver destinations are environment-specific. A preview must not call a production release service. The public demo contains only synthetic records and uses a simulator, never arbitrary recipients.

## 7. Cross-language contract tests

Run the same classification fixtures, field-projection golden files, deny reasons, packet digests, and recipient tests against both implementations. A Python client can call a TypeScript MCP service, and a TypeScript coordinator can delegate to a Python specialist, provided protocol versions and transports are compatible.

Do not compare exact model prose as the primary correctness test. Compare allowed fields, source IDs, policy revisions, decision outcomes, and release invariants. Use separate stores for ordinary side-by-side comparisons.

The TypeScript counterpart is successful when it preserves the same privacy decisions and recovery behavior—not merely when it reproduces the screen layout.
