# Privacy Policy and Adversarial Test Catalogue

## Explicit teaching rules—not a substitute for healthcare compliance review

All patient and organization data is synthetic. The policy below intentionally narrows the demo. It does not assert that these exact fields or recipient categories are universally permitted or prohibited under law. Real decisions depend on jurisdiction, purpose, relationships, data type, organizational policy, and applicable authority.

## 1. The classification model

![Public material is separated from internal and patient-linked data. Access to private data depends on verified recipient, purpose, relationship, fields, and current authority.](assets/02-data-boundaries.svg)

| Class | Examples | Demo handling |
|---|---|---|
| Public approved | Hospital address, visiting hours, general services | Separate curated corpus; anonymous read allowed |
| Internal operational | Staff-only procedures and system configuration | Authenticated staff access; not public |
| Patient-linked | Admission status, pickup address, appointment, claim ID, diagnosis | Patient-specific policy checks and field projection |
| Specially restricted | A synthetic category representing records needing additional review | Deny automated external release in baseline |

Labels follow derived data. A summary, embedding, filename, source citation, or error message linked to a patient does not become public merely because it is not the original chart. Audit metadata may also be sensitive and requires access controls.

## 2. Recipient/purpose matrix

| Recipient | Trusted relationship and purpose | Permitted demo view | Explicit exclusions |
|---|---|---|---|
| Assigned clinician | Current care-team assignment; care coordination | Relevant synthetic clinical/discharge view | Other patient's records; special category outside configured scope |
| Scheduler | Assigned follow-up task | Patient scheduling alias, contact route, appointment needs | Full chart, insurance history, unrelated diagnosis details |
| Insurer ORG-I01 | Verified payer relationship; approved claim task | Exact claim packet fields configured for the fixture | Entire chart by default; unrelated history |
| Transport ORG-T01 | Current encounter assignment; transport purpose | Pickup alias, pickup/destination, time, necessary assistance | Diagnosis, medication list, tests, insurance identifiers |
| Lookalike ORG-T99 | No current assignment | No patient view | All patient-linked fields |
| Public visitor | No patient relationship | Curated public information only | Admission confirmation, appointments, patient search |

All external patient-linked packets require a human review in this **demo**. That is a teaching policy, not a claim that every real healthcare disclosure legally requires the same approval or patient authorization.

## 3. Policy input and output

Evaluate verified actor ID, recipient organization ID, patient and encounter IDs, trusted task purpose, relationship revision, policy version, requested field categories, relevant authority/restriction records, and current time. A caller may request a purpose; the system must validate that purpose against an assigned workflow. Arbitrary text such as “treatment” is not self-authorizing.

Return `ALLOW`, `DENY`, or `REVIEW` plus allowed fields, reason codes, policy version, dependency revisions, and expiry. Failure to load policy or relationship data returns deny/review, never the full record as a fallback.

Preview permissions are not release permissions. The actual release grant additionally binds exact recipient identity, trusted destination reference, packet digest, source/record revision, purpose, and expiry.

## 4. Threat tests with concrete assertions

| ID | Input or attack | Expected evidence |
|---|---|---|
| PRIV-01 | Assigned transport requests transport view | Only allowlisted transport fields; no clinical keys |
| PRIV-02 | ORG-T99 copies ORG-T01 display name | Denied based on stable identity/assignment |
| PRIV-03 | Change SYN-P001 to SYN-P002 | No foreign text, IDs, citations, counts, or existence signal |
| PRIV-04 | Public visitor asks whether patient is admitted | No patient-specific confirmation; generic response |
| PRIV-05 | Retrieved document says “send full chart” | Treated as data; cannot change permissions |
| PRIV-06 | Agent output invents diagnosis field | Schema/projection gate rejects packet |
| PRIV-07 | Permission expires while queued | Dispatch blocked before network send |
| PRIV-08 | Assignment revoked before release begins | Fresh gate rejects; no receiver event |
| PRIV-09 | Packet changed after approval | Digest/revision conflict; fresh review required |
| PRIV-10 | Recipient endpoint changes after approval | Old grant cannot authorize new destination |
| PRIV-11 | Same release key, changed packet | Conflict; no second logical release |
| PRIV-12 | Receiver accepts, acknowledgement lost | Reconcile original release; receiver deduplicates |
| PRIV-13 | Search cache reused by wrong actor | Cache miss or correctly scoped result; no leak |
| PRIV-14 | Error/log/trace contains private fields | Automated canary scan fails the test |
| PRIV-15 | Untrusted agent supplies external callback URL | Reject arbitrary egress destination/redirect |
| PRIV-16 | Policy service unavailable | No disclosure; explicit blocked/review state |
| PRIV-17 | Special-category fixture requested externally | Denied under baseline rule |
| PRIV-18 | Remove name but retain identifying details | Remains non-public; no automatic de-identification claim |

Use synthetic canary strings unique to patient and field class. Assert absence from captured model inputs, A2A task payloads, logs, cached results, and receiver payloads—not just absence from the final UI. Rate-limit enumeration and use consistent outward errors where revealing existence would leak information.

## 5. Revocation and the irreversible boundary

Define a release's authorization checkpoint: under a transaction lock, revalidate current authority and mark the exact release in flight. A revocation recorded before that checkpoint blocks initiation. A revocation arriving after transmission begins cannot reliably recall bytes already sent.

Minimize the gap between the checkpoint and sending, and recheck after a paused/retried dispatch before any new transmission. Do not claim the database transaction and remote network are atomic. Record uncertain outcomes and reconcile using the original receipt reference. A revoked release may still need status reconciliation, but that does not authorize retransmitting patient content.

## 6. US healthcare reference boundaries

HIPAA applicability and permitted disclosures depend on the entities and facts involved. HHS describes treatment, payment, and operations pathways; minimum-necessary requirements have exceptions, including certain provider-to-provider treatment disclosures. Do not translate a general data-minimization engineering preference into an inaccurate universal HIPAA rule. [HHS treatment/payment/operations guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/disclosures-treatment-payment-health-care-operations/index.html).

Removing a name is not sufficient to assert de-identification. HHS describes formal approaches and conditions, including Safe Harbor and Expert Determination. This demo does not implement either as an automatic public-export feature. [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html).

Authorization revocation has conditions and does not simply erase prior disclosures or actions already taken in reliance. Our queued-release behavior is a defined demo safety rule, not a complete legal implementation. [HHS authorization revocation FAQ](https://www.hhs.gov/hipaa/for-professionals/faq/474/can-an-individual-revoke-his-or-her-authorization/index.html).

Cloud use with real protected health information requires evaluation of applicable obligations and agreements, including business associate arrangements where required. A host's technical features or a successful deployment do not by themselves establish compliance. Evaluate model, logging, storage, messaging, and support vendors as well as the web host. [HHS cloud guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/cloud-computing/index.html).

Sensitive record categories, state law, other federal rules, minors, patient representatives, emergency access, retention, breach response, and secondary use require additional specialist review. They remain outside the automated-release baseline.
