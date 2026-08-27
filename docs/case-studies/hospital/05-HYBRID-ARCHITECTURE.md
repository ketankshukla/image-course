# HarborCare — Next.js + Python Hybrid

## A reviewer-friendly screen without a second privacy policy engine

The hybrid version adds a Next.js/React interface to the Python reference. The browser presents requests, evidence, and packet previews. Python remains authoritative for policy, relationships, projection, approval, and release. All data remains synthetic.

## 1. At a glance

![The web workspace calls the Case API; policy, evidence, specialist tasks, and release remain behind explicit backend boundaries.](assets/03-system-map.svg)

Next.js is a backend-for-frontend layer: it verifies a session, loads safe display data, and forwards commands. It does not independently implement the transport field allowlist or read the chart database directly.

## 2. Proposed web structure

```text
apps/web/
├── app/
│   ├── layout.tsx
│   ├── requests/page.tsx
│   ├── requests/[requestId]/page.tsx
│   ├── requests/[requestId]/actions.ts
│   ├── api/requests/[requestId]/events/route.ts
│   └── api/public-information/route.ts
├── components/
│   ├── recipient-card.tsx
│   ├── purpose-panel.tsx
│   ├── packet-preview.tsx
│   ├── excluded-fields.tsx
│   ├── approval-panel.tsx
│   └── disclosure-timeline.tsx
└── lib/server/
    ├── session.ts
    ├── backend-client.ts
    ├── delegation.ts
    └── request-queries.ts
```

`excluded-fields` displays category names such as “diagnosis omitted,” never the hidden diagnosis value. A reviewer permitted to approve transport does not automatically get a clinician's complete chart view.

## 3. The initial page request

The server loads the verified user identity, resolves the request ID, and asks Python for a permitted read model. Python checks hospital membership, patient relationship, purpose, and reviewer role. The returned data is already scoped before it is passed to React components.

Keep backend credentials and delegation code server-only. A Server Component calls the backend adapter directly; it does not need to call its own API first. Client Components handle form interaction and event updates. Authentication and authorization still run for every subsequent read, action, and stream.

Do not share-cache patient pages. Public hospital information may use separate caching rules. Start without patient-data caches; add them only with tested identity/policy scoping and invalidation.

## 4. The request-to-release flow

The user selects a known recipient and purpose from their permitted task context. The backend validates those selections; a dropdown is not a security control. The UI shows an existing or newly created request with an idempotent intake key.

Python generates a packet preview under current policy. The reviewer sees recipient legal/display name and stable organization reference, purpose, field categories, packet version, expiry, and reason codes. Approval sends the expected revision—not a browser-edited replacement payload.

Python records approval and schedules dispatch. The page shows Queued, In flight, Delivered, Blocked, Revoked, or Outcome unknown based on persisted state. Closing the page does not stop work; a dedicated cancellation/revocation command is a separate authorized operation.

## 5. Human-readable denial design

An authorized reviewer may receive “Transport assignment expired; refresh the assignment before release.” An unrelated public visitor receives a generic response that does not reveal whether the patient exists. Error detail depends on the audience.

Avoid misleading buttons such as “Approve anyway.” An exception workflow, if ever introduced, must have its own policy, authority, and audit requirements. It is not a frontend override flag.

When a proposal changes, disable stale approval and load the current preview. Do not silently carry a prior approval onto a new recipient or field set. Before resending after a failure, check the backend's current state rather than relying on browser memory.

## 6. Upload and output protections

The first hosted demo uses curated synthetic fixtures and does not accept arbitrary patient uploads. A future upload flow must authorize the object, verify size and media type, isolate parsing, scan content, classify records, and prevent private filenames from appearing in public URLs.

Render evidence excerpts as escaped text or sanitized markup. Never insert arbitrary source HTML. Do not include restricted data in hidden DOM elements, page-source JSON, browser analytics, error reporting, or download filenames.

Progress uses authorized polling first, with optional bounded SSE later. Scope event cursors to the request and actor. A reconnect must revalidate access; the existence of an old cursor is not permission.

## 7. Hosting and tests

Host the Next.js synthetic demo on Vercel and the Python processes on a container-capable host. Keep database and private objects near backend compute. Use independent preview credentials and synthetic datasets. The host choice is not a compliance assertion; real-data deployment needs the review described in the privacy guide.

Browser tests should verify allowed field visibility, omitted clinical values in page source and network responses, wrong-patient denial, expired session, stale packet approval, and revocation before dispatch. End-to-end tests inspect the receiver's actual packet, not just a green success badge.

The hybrid implementation is complete when a reviewer understands exactly what will leave the hospital boundary, and the same restrictions hold even when someone bypasses the UI and calls the backend directly.
