# FilePilot — Next.js Workspace with a Local Python Engine

## At a glance

The recommended full application combines a local Next.js/React workspace with the Python reference engine. The interface makes plans understandable; Python owns root grants, inspection, approval validation, and execution. Start with both running on the same computer.

## What the diagram teaches

![Local browser requests reach a local service and selected sandbox. The public website contains only teaching documents and a possible synthetic demonstration, with no personal filesystem bridge.](assets/boundaries.svg)

It is tempting to put the React interface on Vercel and assume it can call the computer's filesystem. That is not how the proposed architecture works. Code running in a hosted server has access to its own environment, not Maya's E: drive. A local browser page also does not receive unrestricted file permissions just because it contains a “Scan” button.

For the first version, launch the interface locally and use a same-origin route for its API calls. The local UI server forwards approved API routes to a loopback-only Python service. The Python service validates its own session and caller authorization rather than trusting “the request came from the interface.” Keep credentials out of client bundles and query strings.

A malicious website can attempt to contact local services. Binding to loopback is necessary but insufficient. Validate Host and Origin, require an authenticated local session, protect state-changing requests against CSRF, and reject unknown origins. CORS is not a substitute for authorization. The [MCP transport security guidance](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports) also highlights protections for local HTTP servers; ordinary application endpoints need their own equivalent review.

## Proposed UI structure

```text
apps/workspace/
  app/
    page.tsx                    Root selection and current inventory
    plans/[id]/page.tsx          Exact plan revision review
    jobs/[id]/page.tsx           Execution and recovery timeline
    api/local/[...route]/route.ts  Narrow allowlisted local proxy
  components/
    RootGrantPanel.tsx
    FileTable.tsx
    EvidencePanel.tsx
    PlanReview.tsx
    ApprovalSummary.tsx
    OperationTimeline.tsx
  lib/
    api-client.ts
    contracts.ts
```

The proxy must forward only explicitly supported API paths and methods to one configured local backend. It must not become a generic URL fetcher or a way to reach arbitrary local ports. The catch-all filename is a routing convenience, not permission to proxy every path.

## API contract sketch

| Request | Purpose | Important constraint |
|---|---|---|
| `POST /scans` | Start inventory for a granted root ID | Cannot introduce a new root implicitly |
| `GET /scans/{id}` | Return bounded status and file summaries | Caller owns or may inspect this scan |
| `POST /queries` | Search permitted evidence | No content sent remotely by default |
| `POST /plans` | Propose a plan from a scan revision | Allowlisted operations and destination IDs |
| `POST /plans/{id}/approvals` | Record explicit reviewer approval | Current revision, expiry, authenticated principal |
| `POST /jobs` | Request execution of an approved plan | Idempotency key; engine reloads authoritative plan |
| `GET /jobs/{id}` | Return verified progress and errors | No fabricated progress after disconnect |
| `POST /jobs/{id}/reverse-plans` | Propose supported undo operations | A new plan requiring review, never immediate reversal |

These are application routes, not standard MCP or A2A method names. Give the implementation an OpenAPI contract or equivalent tests and ensure TypeScript types agree with actual serialized responses.

## Walk through a review

Maya selects two rows from a five-operation draft. The interface sends those operation IDs, not a rewritten plan. The server validates the selection, creates a new revision, and returns its digest and summary. Maya reviews that revision and approves it. The UI displays the approved count, destinations, and expiry.

Clicking Execute sends the plan reference, approval reference, and idempotency key. The server owns the job state. A second click returns the same job. If the browser closes, the engine's durable state remains authoritative. On reopening, the UI loads the job and displays completed, blocked, and unknown operations separately.

## Hosted demonstration versus personal tool

A hosted demo can display synthetic inventories and simulate state transitions. Label it prominently as a simulation. Do not present an animated folder tree as evidence that real files moved. Keep real-file mode in a separately installed local application.

A future cloud-to-local bridge is a separate security project: authenticated device pairing, scoped commands, expiring grants, local confirmation, revocation, origin restrictions, and safe updates. It is not included in the first release. Do not expose the local Python port to the Internet to make the demonstration easier.

## How to present it

Show the local and hosted versions side by side. Explain which one can act on a sandbox and which merely demonstrates the interface. Then disconnect the local UI during a job and show that reconnecting displays the engine's actual state.
