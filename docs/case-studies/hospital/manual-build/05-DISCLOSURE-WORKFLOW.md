# 5. P4: Approval, Disclosure and Recovery

## At a glance

This is the most important project in the case study. Preparing a packet is reversible. Sending it may not be. Build the release state machine before connecting a delivery adapter.

![A preview becomes an approved queued release, then a checked dispatch attempt, followed by a receipt or explicit uncertainty.](../assets/04-release-lifecycle.svg)

## 1. Create the state model

In `release/contracts.py`, define PREVIEW, AWAITING_REVIEW, APPROVED, QUEUED, IN_FLIGHT, DELIVERED, DENIED, REVOKED, EXPIRED and DELIVERY_UNKNOWN. Define allowed transitions explicitly. An arbitrary request must not be able to set `state=DELIVERED`.

In `release/packet.py`, implement `canonicalize_packet` and `calculate_digest`. Use a documented canonical representation so equivalent objects hash consistently. A digest binds the review to exact bytes or a precisely defined canonical payload; it does not make the contents anonymous. Treat it as protected metadata.

## 2. Bind the review to the actual disclosure

In `release/review.py`, implement `create_review` and `approve_review`. Store patient, encounter, recipient stable ID, registered destination revision, purpose, exact field set, packet digest, policy and relationship revisions, expiration, reviewer identity and decision time.

On approval, re-read current policy. Check that the reviewer is authorized for this review and that the packet has not changed. In this demo every external patient packet requires human review; this is a deliberately conservative teaching policy, not a statement that all real-world disclosures legally require patient authorization.

Changing the destination, fields or patient requires a new review. Do not let an approved screen remain valid after an invisible background edit.

## 3. Add durable storage

Create release, review, outbox and audit tables with explicit foreign keys and uniqueness rules. In `release/repository.py`, implement `queue_approved_release` as one local transaction: insert the release intent and corresponding outbox job together. If either write fails, neither should remain committed.

The outbox is a durable list of work to send. It solves the local “saved the approval but lost the job” problem. It does not make a remote network delivery atomic with your database.

## 4. Implement the worker's authorization checkpoint

In `release/worker.py`, write `claim_job`, `authorize_dispatch`, `send_attempt` and `reconcile_delivery`. `authorize_dispatch` locks the relevant current state, checks revocation and expiry, verifies the approved digest and recipient, records an attempt generation, and transitions to IN_FLIGHT. Use transaction and concurrency tests, not just sequential examples.

Make the network call after the local transaction. Document the boundary honestly: revocation that wins before authorization blocks initiation. Revocation after bytes have left cannot recall them. Minimize the gap, check immediately before each new transmission, and record the timing needed to investigate races.

## 5. Build a local recipient simulator

Create `receiver_simulator.py` with `accept_packet` and `lookup_receipt`. Key acceptance by recipient identity and release ID, and bind it to the exact digest. Repeating the same accepted release returns the same receipt; the same key with different content is a conflict, not an overwrite.

Add modes for reject-before-accept, accept-then-drop-acknowledgment, slow response and unavailable status. Keep this simulator isolated; it must not forward to an email address or real agency.

## 6. Handle the uncertain case explicitly

If the receiver accepted the packet but the acknowledgment was lost, mark DELIVERY_UNKNOWN. Query receipt status using protected metadata first. Do not blindly resend the payload. If authorization has since been revoked, do not start a new payload transmission. If status cannot be determined, preserve the uncertainty and request operator review.

Do not promise exactly-once network delivery without a receiver contract that supports the necessary guarantees. Even with idempotency, a timeout is evidence of uncertainty, not proof of non-delivery.

## 7. Acceptance gate

Test process termination after approval, after outbox commit, after authorization and after receiver acceptance. Test two workers racing, revocation before dispatch, expired review, changed packet digest, and a receiver conflict. Assert the exact number of receiver acceptances, not just the number of successful HTTP responses.

Audit identifiers, decisions and state changes without logging the full packet. Protect the audit store itself. Your final explanation should distinguish “approved,” “attempted,” “received,” and “unknown” in ordinary language.
