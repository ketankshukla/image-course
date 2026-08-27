# Diagram 168 — Tamper-Evident Audit, Redaction, and Chain of Evidence

![On a dark navy background, a horizontal sequence of eight white audit-event cards is joined by teal arrows. From left to right they read INPUT RECEIVED, IDENTITY VERIFIED, POLICY DECISION, TOOL DENIED, APPROVAL, ACTION, RECEIPT, and REVIEW. Each card carries metadata fields: TIME, ACTOR, TENANT, ACTION, RESULT, CORRELATION, and PREVIOUS HASH. A cyan arrow labelled RAW SENSITIVE PAYLOAD leaves the second card and passes through a REDACTION gate before continuing as a teal arrow into a SEALED EVIDENCE STORE. A HASH CHAIN line runs beneath all eight cards and curves down to a VERIFY step. A coral DELETE OR EDIT event tries to break the hash line and triggers a red ALERT.](../diagrams/168-tamper-evident-audit-chain.png)

**Module:** Supply chain, privacy, and audit evidence  
**Role in the course:** how to preserve useful security evidence without turning logs into a second unprotected copy of customer data and secrets  
**Layout:** a timeline of eight ordered audit events, a redaction path to a sealed evidence store, a hash chain leading to verification, and a broken-chain tamper alert

---

## At a glance

**INPUT RECEIVED → IDENTITY VERIFIED → POLICY DECISION → TOOL DENIED → APPROVAL → ACTION → RECEIPT → REVIEW**.

Every event carries **TIME, ACTOR, TENANT, ACTION, RESULT, CORRELATION,** and **PREVIOUS HASH**.

Sensitive payloads are **redacted** before they enter the general log and are held separately in a **sealed evidence store**.

A **hash chain** links the events in order and feeds a **verify** step.

A **delete or edit** anywhere along the chain **breaks verification and raises an alert**.

---

## What the diagram teaches

### 1. An audit trail is a security contract, not a confession

An audit trail proves what happened, when, for which tenant and resource, under which policy and authority, with what outcome. The diagram turns that into evidence cards stamped with the fields that make the record attributable and reviewable.

This is a **security contract**, not a model-behavior promise. The log does not stop an attack, but it makes the attack visible and disprovable afterwards.

### 2. Order matters: events form a chain, not a bag

The eight cards read left to right because an action begins with input, passes through identity and policy, may be denied or approved, and ends with a receipt and later review. Stored as an unordered collection, events can be inserted, deleted, or reordered without detection. The chain enforces the narrative.

### 3. Every event is a structured record, not a free-text line

Each card carries a common set of fields:

- **TIME** — trusted timestamp, not the client clock.
- **ACTOR** — the human, client, agent, workload, or service identity.
- **TENANT** — the boundary that keeps one customer's work separate from another's.
- **ACTION** — the specific operation or decision attempted.
- **RESULT** — allowed, denied, approved, failed, quarantined, or completed.
- **CORRELATION** — the request or workflow ID that ties scattered records together.
- **PREVIOUS HASH** — the cryptographic link to the prior event.

Structured events can be filtered, joined, verified, and alerted on. Free-text logs cannot do that reliably.

### 4. Identity and tenant travel with every decision

The **IDENTITY VERIFIED** and **POLICY DECISION** cards sit early in the chain because authority is the foundation of every later event. The diagram insists that the actor and tenant are recorded at each step, not just at the edge. A privilege error, an injection, or a cross-tenant leak may change identity or tenant mid-flow, and the audit trail must capture that shift.

A correlation ID under two different tenants, or an approval actor that does not match the action actor, is a signal. Audit makes those mismatches obvious.

### 5. Redaction keeps secrets and personal data out of general logs

A cyan arrow labelled **RAW SENSITIVE PAYLOAD** leaves the event stream and passes through a **REDACTION** gate before continuing as a safe teal arrow. Logging everything — credentials, account numbers, attachment contents, customer messages — creates a second, often less protected, copy of the data the system is supposed to guard.

Redaction removes or masks sensitive fields before they enter the general telemetry path. The rule is **minimize first**: record only the metadata and identifiers needed to explain the decision, not the full payload.

### 6. Sealed evidence handles the exceptions

Some investigations need the raw content: the exact attachment, or the injected prompt. The **SEALED EVIDENCE STORE** is a separate, encrypted, access-restricted repository with its own audit trail. Access is **purpose-bound**: an investigator must step up, state a reason, and have that access itself logged.

### 7. The hash chain makes tampering detectable, not impossible

A **HASH CHAIN** runs beneath the events and feeds the **VERIFY** step. Each event contains the previous hash, so changing one event requires changing every later hash. Deleting leaves a gap and inserting breaks the sequence. That is **tamper-evident**: the system detects change even if it cannot always prevent it.

A hash chain alone cannot stop an administrator from deleting the whole store. It needs append-only storage, signatures, independent checkpoints, access controls, monitoring, and backups. Verification compares the chain against those checkpoints and raises alerts when it no longer matches.

### 8. Provenance receipts explain which inputs produced the action

![Source, dependencies, build attestations, container, model, prompt, tool, policy, configuration, and discovery versions form a provenance graph leading to a run receipt while unknown or unpinned inputs are quarantined.](../diagrams/166-execution-provenance-supply-chain.png)

That diagram applies the same evidence idea to **runtime inputs**. A run receipt identifies the source commit, dependency lock, build attestation, container digest, model, prompt version, tool schema, policy, configuration, and discovery snapshot that produced one action. The audit chain explains who did what and when; the provenance diagram explains **which code, model, prompt, tool, policy, and configuration produced that behavior**. High-impact actions should carry both.

### 9. Tool denials are first-class evidence

The diagram includes a **TOOL DENIED** card, not just allowed actions. Denied requests are often more valuable than allowed ones: they reveal injection attempts, policy conflicts, misconfigured scopes, or abuse patterns. If the log only records successes, an attacker can probe the system indefinitely without leaving a trail.

A denial record should contain the same structured fields as an approval: actor, tenant, action, result, reason, and correlation. The reason matters — identity, tenant, policy, timeout, or egress — because different causes point to different controls and incident stories.

### 10. Access to evidence is itself an event

The **REVIEW** card is not an afterthought. Every investigation, replay, export, or sealed-evidence read must produce its own audit record with actor, purpose, and timestamp. Next.js consoles should require step-up and a stated purpose before displaying high-sensitivity events; Python backends should record each evidence access as a new audit event. Without access auditing, the audit system becomes a backdoor.

### 11. Retention, deletion, and export are part of the chain

Audit evidence is not kept forever. Each event or sealed artifact should carry a retention label, an owner, and a deletion route. A **DELETE OR EDIT** that is not authorized is a tampering signal; an authorized deletion with a receipt is a normal part of the lifecycle.

Deletion must reach derived copies: SIEM logs, metrics, vectors, caches, and artifacts. A deletion receipt that only updates the primary database while copies survive elsewhere is a privacy and evidence failure.

### 12. Build it as typed records and verified jobs

In Next.js, the operator timeline should be built from server-authorized redacted events and display verification state explicitly. The React interface must not invent security state.

In Python, create **AuditEvent** models, chained digests or signed batches, redaction policies, an append-only sink, and periodic verification jobs. Use explicit boundaries for identity, tenant, policy, data classification, and audit context. Test allowed and denied paths, and test the chain itself with deletion, insertion, reordering, and clock-skew attacks.

---

## Case study — Acme Refunds, the attachment that needed an audit chain

A vendor sends Maya a file that claims to contain new payment instructions. The Acme agent rejects the new payee and the security team needs to know what happened, whether any payment credential was exposed, and whether the evidence can still be trusted.

### What they had

The original telemetry system logged the full text of messages, tool responses, and model outputs, including credential-like strings, attachment contents, and the customer account number. The logs were writable by the same administrators who managed the application, so the team had bulk but not trustworthy or privacy-safe evidence.

### The incident

The file reached the agent as an untrusted attachment. The agent attempted a tool call with a redirected payee; the policy engine denied it and the egress filter blocked an attempt to send credentials outside. Each step should have left evidence, but the logs mixed metadata with raw payloads and had no hash chain, so an investigator could not prove a log line had not been altered.

### The new design

The new audit chain records these events:

1. **INPUT RECEIVED** — attachment intake, actor is the authenticated customer, tenant is Maya, correlation is the refund case.
2. **IDENTITY VERIFIED** — the customer identity and the agent workload identity are both recorded.
3. **POLICY DECISION** — the redirection rule flags the new payee; the result is deny.
4. **TOOL DENIED** — the payment tool is not called; the reason is payee-policy violation.
5. **APPROVAL INVALIDATION** — any previously bound approval is automatically invalidated because the input changed.
6. **ACTION** — the safe refund to the original payee is completed.
7. **RECEIPT** — the final refund produces a receipt with the policy outcome.
8. **REVIEW** — a security investigator opens the sealed attachment under a recorded purpose and verifies the chain.

The general logs show event hashes, actor, tenant, action, result, and reason. The attachment itself and any credential-like strings live in the sealed evidence store, encrypted and access-controlled.

### Results

- **Investigation time to reconstruct the incident:** from hours of grepping mixed logs to minutes of following a verified chain.
- **Risk of leaking customer data through logs:** reduced because raw payloads are redacted and sealed.
- **Ability to prove the log was not altered after the incident:** enabled by the hash chain and independent checkpoints.
- **Investigator access:** logged as a new audit event with purpose, identity, and time.

### The line in their operations standard

*High-impact allows, denials, approvals, changes, and actions remain attributable and verifiable, while audit access and payload content follow least privilege and privacy rules.*

---

## Composition

A horizontal timeline of eight white audit-event cards, a redaction path, a sealed evidence store, a hash chain, a verification step, and a tamper alert.

**Top row (eight white cards):**

- **INPUT RECEIVED** — document or message entering the system.
- **IDENTITY VERIFIED** — actor and tenant confirmed.
- **POLICY DECISION** — authority evaluated against context.
- **TOOL DENIED** — an attempted tool call rejected.
- **APPROVAL** — explicit authorization for a consequential action.
- **ACTION** — the operation that changes state.
- **RECEIPT** — proof that the action completed with a known outcome.
- **REVIEW** — later inspection or investigation.

**Each card** contains fields: **TIME, ACTOR, TENANT, ACTION, RESULT, CORRELATION, PREVIOUS HASH**.

**Below the cards**, a **HASH CHAIN** line links each event to the next and leads to the **VERIFY** step.

**A cyan arrow** from the event stream points to a **REDACTION** gate, then becomes a teal arrow into the **SEALED EVIDENCE STORE**.

**A coral path** labelled **DELETE OR EDIT** tries to cut the hash chain and triggers a red **ALERT**.

## Element by element

**INPUT RECEIVED** — the start of the trace; could be a message, attachment, API call, or scheduled job.

**IDENTITY VERIFIED** — the point where the system records the verified actor and tenant.

**POLICY DECISION** — the recorded result of evaluating authority, purpose, and context.

**TOOL DENIED** — a rejected tool call, often the most important signal in an attack.

**APPROVAL** — explicit consent or authorization for an action that crosses a trust boundary.

**ACTION** — the state-changing operation, such as a payment, update, deletion, or egress.

**RECEIPT** — an artifact that proves the action and its outcome, often with a correlation ID.

**REVIEW** — later investigation, replay, or audit of the chain.

**TIME, ACTOR, TENANT, ACTION, RESULT, CORRELATION, PREVIOUS HASH** — the minimum structured fields that make an event attributable and linkable.

**REDACTION** — removal or masking of secrets and unnecessary personal data before general logging.

**SEALED EVIDENCE STORE** — encrypted, access-restricted storage for exceptional raw artifacts.

**HASH CHAIN** — ordered cryptographic links that make later tampering detectable.

**VERIFY** — the routine check that the chain is intact and matches checkpoints.

**DELETE OR EDIT** — unauthorized modification, shown in coral as a break in the chain.

**ALERT** — the signal produced when verification fails or the chain is broken.

## Colour and flow semantics

- **White cards** represent audit events and evidence records, the same way white cards represent identity, claim, policy, and approval records elsewhere in the course.
- **Cyan arrows** carry the flow of live action and raw data through the system.
- **Teal arrows and lines** represent verified, safe, or evidence paths: the hash chain, the redacted payload after the gate, and the sealed evidence path.
- **Coral** marks the delete-or-edit tamper path, the broken chain, and the resulting alert.
- The **hash chain** runs beneath the events because it is the hidden structural link that makes the whole timeline trustworthy.
- The **sealed evidence store** sits below the main row because it is a side path, available only under restricted conditions.

## How to present it

**Ask how the room would investigate an attacker who tried to redirect a payment.** Most teams will describe grepping logs. Ask them whether those logs contain the raw credential, whether they can prove the log was not edited, and whether every investigator access is recorded.

**Point at the eight event cards and read the common fields.** Time, actor, tenant, action, result, correlation, previous hash. Ask which of those fields their current logs reliably include for every high-impact action.

**Trace the redaction path.** A sensitive payload does not go straight into the log. It goes through a redaction gate, and only the safe metadata enters general telemetry. Ask what secrets or personal data currently sit in application logs.

**Show the sealed evidence store and ask who can open it.** It should require step-up authentication, a stated purpose, and its own audit record. If the answer is "anyone with log access," the store is not sealed.

**Explain the hash chain and the verify step.** Each event contains the previous hash. Changing, deleting, or inserting an event breaks the chain. Emphasize that a hash chain detects tampering; independent retention and protected administration are still required to survive a malicious deletion of the whole store.

**Use the checkpoint question.** *Does a hash chain prevent an administrator from deleting the entire log store?* The answer is no. It reveals alteration when checkpoints survive, but access controls, monitoring, and backups still matter.

**Tell the Acme attachment story.** The old logs mixed raw payloads with metadata. The new chain separates redacted events from sealed evidence and proves the sequence was not silently edited.

**Show the provenance diagram.** An audit chain explains who did what. A run receipt explains which code, model, prompt, tool, policy, and configuration produced the behavior. High-stakes actions need both.

**Make the room design one audit event.** Have them list actor, subject, tenant, resource, action, result, reason, policy, correlation, previous hash, retention, access, and sealed evidence reference. This is the lab prompt in a single sentence.

**Talk about the related lessons.** Lesson 158 covers the policy-context-decision-receipt flow, lesson 166 covers execution provenance, and lesson 171 covers governance roles and exceptions.

**Mention the sources in context.** OWASP logging guidance describes what to log and what to avoid, Open Policy Agent decision logs show how to record policy outcomes, and the NIST AI Risk Management Framework ties technical evidence to accountable risk decisions.

**Close on the standard.** *High-impact allows, denials, approvals, changes, and actions remain attributable and verifiable, while audit access and payload content follow least privilege and privacy rules.*

**Timing.** Twenty-five minutes. Thirty if the room writes a sample audit event and redaction table for one real workflow.
## Lab and checkpoint


**Lab:** Design twelve audit events and a redaction table. Add actor, tenant, resource, action, result, reason, policy, correlation, previous hash, retention, access, and sealed evidence reference.


**Checkpoint:** Does a hash chain prevent an administrator from deleting the entire log store?


**Answer:** Not by itself. It can reveal alteration when checkpoints survive; independent retention, access controls, monitoring, and backups still matter.

## Glossary

- **Tamper-evident** — changes can be detected
- **Chain of evidence** — record of evidence handling
- **Redaction** — removal or masking of sensitive content

## Sources

- OWASP Logging
- Open Policy Agent decision logs
- NIST AI Risk Management Framework

