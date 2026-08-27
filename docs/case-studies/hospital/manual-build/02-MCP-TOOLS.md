# 2. P1: Privacy-Gated MCP Tools

## At a glance

MCP gives an agent a standard way to discover and call tools. It does not decide whether the caller may see a patient record. Your service must enforce that rule on every call, including calls made without the friendly user interface.

![Tool access and evidence retrieval sit behind the same policy boundary.](../assets/03-system-map.svg)

## 1. Create the service in layers

Add these files beneath `backend/harborcare/` in this order:

| File | Function to build | Responsibility |
|---|---|---|
| `identity.py` | `resolve_actor(credentials)` | Validate identity through the configured identity provider |
| `relationships.py` | `resolve_scope(actor, encounter_id)` | Load current hospital, patient and assignment relationships |
| `patient_repository.py` | `read_permitted_fields(scope, fields)` | Read only the permitted data projection |
| `disclosure_service.py` | `preview_disclosure(actor, request)` | Apply policy and construct a safe preview |
| `mcp_server.py` | Tool adapters | Validate protocol inputs and call the service |

For the first local tests, use explicit test identities injected by a fixture adapter. Do not accept an unrestricted production header such as `X-Role: doctor`. Keep the test identity adapter unavailable outside the test configuration.

## 2. Build the preview function before exposing a server

`preview_disclosure` receives a verified actor and a validated request. Resolve the patient and recipient relationships, evaluate the policy, fetch only authorized fields, and construct the preview. A denied request stops before the patient repository is read. A REVIEW decision permits preparation only when its allowed fields and preparation permission explicitly permit that step; it never permits transmission.

Return a preview ID, allowed field values, recipient display name and stable ID, purpose label, policy revision, expiry, and a clear “not sent” state. Keep internal rule diagnostics separate from the response shown to an untrusted caller. The reviewer may need reasons; an unauthorized requester must not learn which private facts exist.

## 3. Wrap the service with narrow tools

Start with `get_public_hospital_information`, `preview_transport_packet`, and `get_release_status`. The public tool queries only the curated public corpus. Status lookup must verify access to that particular release. A guessed release ID is not authorization.

Later add a tool that submits an approved release request to P4. Do not add a tool called `get_full_patient_chart` merely because it makes a demonstration easier. Do not allow the model to supply a delivery URL; resolve the destination from a verified recipient registry.

Use the official MCP SDK and its current authorization guidance when implementing the network adapter. Pin and record the SDK version. Keep domain tests independent of it so a protocol upgrade cannot quietly change the policy rules.

## 4. Trace one request through the files

A coordinator requests a transport preview for ENC-100. The MCP adapter validates the shape, authenticates the caller, and calls `preview_disclosure`. The service checks the caller's assignment and the recipient registry. The policy permits the pickup projection for ORG-T01. The repository returns those fields and the adapter serializes the result.

Now substitute ORG-T99. The identity may be genuine, but the organization is not assigned to this task. The service denies the request before the record read. This is the difference between authentication—knowing who someone is—and authorization—deciding what that person may do here.

## 5. Tests and failure handling

Add `tests/test_mcp_contracts.py` for malformed inputs, unknown fields, unauthorized status lookup, and attempts to supply a recipient URL. Add integration tests that call the actual protocol server, not just the Python function. Assert that tool errors contain neither the clinical canary nor other-patient identifiers.

Simulate a policy-store outage. The tool should fail closed with a retriable service error, not revert to unrestricted reads. Simulate a database timeout after authorization: no preview is invented and no release is recorded. An observability event may contain a safe error category and request ID, but not the complete tool arguments or patient record.

## 6. Acceptance gate

You can demonstrate discovery, an authorized projection, and a direct unauthorized protocol call that is denied. P1 is still not a disclosure workflow: previews cannot send packets. Keep that separation visible in both the code and the demonstration.
