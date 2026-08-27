# 6. P5: Build the Reviewer Workspace

## At a glance

The reviewer needs to answer four questions: which patient task is this, who will receive information, exactly which fields will they receive, and has anything actually been sent? The page should make those answers clear without exposing the entire patient chart.

![The workspace receives a safe view; policy and release decisions remain on the server.](../assets/03-system-map.svg)

## 1. Create the web application last

After the Python service and release tests work, create `apps/web` in the application repository. Use the current official Next.js setup instructions and pin the generated dependencies. This is separate from the existing course website. Do not assume the course site's framework version or configuration is the correct template for a new security-sensitive application.

Create these files in sequence:

| File | Responsibility |
|---|---|
| `app/layout.tsx` | Accessible page shell and navigation |
| `lib/server/session.ts` | Verify the current session on the server |
| `lib/server/harborcare.ts` | Make authenticated server-to-server service requests |
| `app/cases/[id]/page.tsx` | Load the authorized case view |
| `components/PacketPreview.tsx` | Render only the returned allowed fields |
| `components/ReviewControls.tsx` | Collect approve/reject intent |
| `app/cases/[id]/actions.ts` | Reauthorize and submit the mutation |
| `components/ReleaseTimeline.tsx` | Explain queued, in-flight, delivered and unknown states |

## 2. Define a browser-safe response contract

Write `CaseView` before the screen. It contains an authorized display label, recipient ID and display name, purpose, allowed preview fields, review ID, revision, expiration and current release state. It does not contain a hidden full chart or a second patient's record.

Server-rendered data can still reach the browser. Passing an object to a Client Component serializes it across that boundary; a collapsed panel, CSS hiding or an omitted visual label does not protect the underlying values. Inspect the actual network response and rendered payload in tests.

Keep provider keys and service credentials in server-only modules. Do not use public environment-variable prefixes for secrets. The browser must not contact the database or receiver simulator directly.

## 3. Build the read path

The page verifies the session, resolves the requested case through the backend, and renders the safe view. Treat the URL ID as an untrusted lookup key. A reviewer changing ENC-100 to a different encounter must not gain access merely because the route exists.

Use framework-version-appropriate asynchronous request APIs. Disable shared caching for private views initially and send appropriate private/no-store response behavior. Public hospital information can use a separate public route with a separate data source.

## 4. Build the approval action

The button submits review ID, expected revision and the user's decision—not a trusted recipient object or a replacement packet. The server action verifies the session again and calls the backend's approval service. The backend rechecks the current policy and exact packet binding.

If the packet changed, show “This preview changed. Review the new version before approving.” If access was removed, show an appropriately generic denial. Do not convert a timeout into “Approved” for a smoother-looking interface. Disable repeated clicks for usability, but rely on server idempotency for correctness.

Server Actions and route handlers are server endpoints: both need authorization. Hiding the button is not an access check. Apply the framework's request-origin protections and the application's own permission rules.

## 5. Explain state without overstating it

Use explicit labels: “Prepared, not sent,” “Approved, awaiting dispatch,” “Delivery in progress,” “Receiver confirmed,” and “Delivery status unknown.” A green approval badge must not look like a delivery receipt. Provide text labels as well as colors for accessibility.

Show the recipient's stable organization identity alongside its display name. ORG-T99 might deliberately have a name similar to ORG-T01; a reviewer must not be asked to identify the right agency by a friendly name alone.

## 6. Acceptance gate

Test direct API calls without the UI, changed case IDs, stale review submissions, session expiry, simultaneous reviewers and repeated clicks. Search HTML, serialized page data, API responses, error text and browser logs for the clinical and wrong-patient canaries.

Run keyboard and narrow-screen checks. Ensure long field names and recipient names remain readable. The visual acceptance test is not only “looks attractive”: a beginner must correctly explain who gets what and whether the packet has actually left the system.
