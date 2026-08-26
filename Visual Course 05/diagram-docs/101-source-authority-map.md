# Diagram 101 — Source Inventory, Authority, Ownership, and Purpose

![Four source platforms on dark navy — POLICY with a shield, CASE RECORD with a folder, PAYMENT LEDGER with a ledger book, CUSTOMER UPLOAD with a cloud — each carrying a card listing OWNER, AUTHORITY, PURPOSE, REFRESH and SENSITIVITY. Cyan lines converge on a SOURCE REGISTER book platform carrying the same five fields. From it, a teal path leads through a shield and a checked document to a green APPROVED INTAKE CONTRACT with a rosette, while a coral dashed path with a red cross stops before a red UNKNOWN OWNER card.](../diagrams/101-source-authority-map.png)

**Module:** Governance foundation
**Role in the course:** the first diagram — nothing enters a knowledge system unowned
**Layout:** four sources into a register, splitting into an approved contract and a blocked unknown

---

## At a glance

Four different kinds of source feed a **SOURCE REGISTER**. Every one carries the same five fields: **OWNER, AUTHORITY, PURPOSE, REFRESH, SENSITIVITY**.

Two things leave the register. A **teal path** through a shield and a verification step to an **APPROVED INTAKE CONTRACT**. And a **coral dashed path**, stopped by a red cross, leading to **UNKNOWN OWNER**.

The red card is the point. It has all five field labels and no values. A source nobody owns does not enter the system, and the diagram shows it being refused rather than quietly absorbed.

---

## What the diagram teaches

### 1. Five fields, and each answers a question that has consequences later

**OWNER** — who is accountable for this source. Not who built the integration; who is answerable when the content is wrong.

**AUTHORITY** — how much weight this source carries. A published policy outranks a case note. When two sources disagree, this is the field that resolves it.

**PURPOSE** — what this source may be used for. A source ingested for one purpose being used for another is a governance failure, and often a legal one.

**REFRESH** — how often it changes and how often you re-read it. This is what determines whether retrieval will serve stale content.

**SENSITIVITY** — what protections apply. It drives access control, retention, and whether the content may appear in an answer at all.

The five are not administrative metadata. Every one of them is consumed by a later stage of the system, and a source missing any of them creates a specific downstream failure.

### 2. The same five fields appear on every source and on the register

Look at the cards. Policy, case record, payment ledger, customer upload — four very different things, and all four carry an identical field set.

That uniformity is deliberate. A register where different source types carry different metadata cannot be queried consistently, and the questions you need to ask — *what do we hold that is highly sensitive and refreshed monthly?* — become impossible.

The register itself carries the same five, which says it is not a different schema. It is the same contract, enforced centrally.

### 3. The four source types are chosen to be maximally different

**POLICY** — a shield. Authoritative, published, slow-changing, low sensitivity.

**CASE RECORD** — a folder with a person. Operational, frequently updated, personal data.

**PAYMENT LEDGER** — a ledger with a currency symbol. Structured, financial, high sensitivity, and probably not a document at all.

**CUSTOMER UPLOAD** — a cloud with an upload arrow. Unknown content, unknown quality, arriving from outside your organisation.

That last one is the hard case and it is included on purpose. A customer upload has no owner in your organisation by default, no established authority, and unknown sensitivity. It is exactly the source type that tempts teams to skip the register.

### 4. UNKNOWN OWNER is refused, and the refusal is drawn as a hard stop

The coral dashed line carries a **large red cross** partway along, before the red card is reached.

The path is drawn and then interrupted. That rendering says the attempt happens — a source arrives, someone tries to ingest it — and the register refuses.

Note that the red card still has all five field rows. It is not malformed; it is incomplete. Owner is the field that is missing, and its absence blocks everything.

Why owner specifically: without it, nobody can answer the questions the other four fields raise. Who decides the authority? Who confirms the purpose? Who is told when the refresh fails? Who classifies the sensitivity?

An unowned source is not a source with four fields. It is a source with none, because there is nobody to maintain them.

### 5. The approval path has three stages, not one

Between the register and the contract: a **teal shield**, then a **checked document with a magnifier**, then the contract with a **rosette**.

Three steps. A policy check, a verification, and an award.

That is more ceremony than "the fields are filled in." The shield checks the values against policy — is this sensitivity level permitted for this purpose? The magnifier verifies them — is the stated owner real and does the stated refresh actually happen? The rosette marks the outcome as a certified artefact.

### 6. The output is a contract, and that word is load-bearing

Not "approved source" or "registered source" — an **INTAKE CONTRACT**.

A contract has two parties and obligations on both sides.

The source owner commits to maintaining the content, honouring the stated refresh, and notifying on material change. The knowledge system commits to using the content only for the stated purpose, applying the stated sensitivity protections, and honouring retention.

Framing it as a contract makes those obligations explicit and makes it possible to identify a breach on either side.

The five fields do not stop at the register. They propagate onto every chunk derived from the source:

![An ingestion chain from ORIGINAL through PARSE and CHUNK to a seven-field EVIDENCE RECORD listing SOURCE ID, VERSION ID, TENANT, ACL, VALID FROM, RETAIN UNTIL and HASH, gated before SEARCH with coral drops to EXPIRED, REVOKED and WRONG TENANT.](../diagrams/104-provenance-permission-retention.png)

**SENSITIVITY** becomes tenant and ACL. **REFRESH** becomes valid-from and retain-until. The register is where the contract is agreed; that record is where it is enforced, per chunk, on every query.

---

## Case study — Halstead Regional Health, the corpus nobody owned

Halstead operates fourteen community health services. They built a knowledge system to help clinical and administrative staff find guidance — clinical protocols, operational procedures, HR policy, and commissioning documentation.

The corpus reached about 47,000 documents over two years. Then their information governance function asked a question that stopped the project for four months.

### The question

*For each document in the index, who is accountable for its accuracy?*

Nobody could answer. The corpus had been assembled by pointing ingestion at a set of network shares and document management systems, and the ingestion had been indiscriminate by design — the team's view had been that more content meant better retrieval.

### The audit

Four months of work, and it produced numbers that changed how the organisation thought about the system.

**47,000 documents ingested. 12,000 had an identifiable owner.**

Of the remaining 35,000:

**19,000 were superseded versions** sitting alongside current ones in the same shares. Nothing distinguished them, and retrieval had been returning both.

**8,000 were personal working documents** — drafts, notes, meeting minutes — that individuals had saved to shared locations. Several contained patient-identifiable information in free text.

**4,000 were from services that had been decommissioned** or transferred to other providers. Their content was no longer Halstead's to hold, let alone to surface.

**3,000 were genuinely orphaned** — content whose originating team had dissolved, whose subject matter was still relevant, and for which no current person would claim responsibility.

**1,000 could not be classified at all.**

### The incident they found in the process

The audit found that a clinical assistant had, four months earlier, surfaced a protocol for a procedure that Halstead had stopped offering after a service transfer.

A clinician had read it, found it plausible, and queried it with a colleague before acting. It was caught by that conversation and not by the system.

The document had no owner, no valid-to date, and no indication that the service had transferred. It ranked well because it was well-written and specific.

### The rebuild around the register

**Every source requires an owner before ingestion.** Not a team name — a named individual with a role, who receives an annual re-attestation request.

That single requirement eliminated the 8,000 personal working documents and the 4,000 transferred-service documents immediately, because nobody would claim them.

**Authority became a four-level scale.** *Published policy* (highest), *approved procedure*, *operational guidance*, *reference material* (lowest). Retrieval weights by it and conflict resolution uses it.

The 19,000 superseded versions were resolved by requiring a valid-from and valid-to on every policy source, which is what the version work later in the volume builds on.

**Purpose was constrained per source.** A source ingested for clinical guidance cannot be surfaced in an HR query. This was an information governance requirement and it turned out to improve retrieval quality independently, because it removed a category of plausible-but-irrelevant results.

**Sensitivity drove three protections.** Access control, retention, and — the one they had not considered — whether content may be quoted in an answer at all. Some sources may inform a response without being reproduced in it.

**Refresh became a monitored commitment.** A source whose owner declared a monthly refresh and has not changed in four months raises a flag. This has found seven sources whose upstream feed had silently broken.

### The 3,000 genuinely orphaned documents

The hardest category, and the one that took the longest.

The content was relevant. The subject matter was live. There was simply no current owner.

Halstead's resolution: each was reviewed by the service that would be affected if it were wrong. Roughly 1,100 were adopted by a current team. About 1,400 were found to be superseded by newer material and were removed. Around 500 were genuinely orphaned and genuinely needed, and were assigned to a knowledge management function created for the purpose.

That last group is the argument for the register. Without it, 500 documents that mattered had no maintenance path, and nobody knew.

### Results

- **Documents in the index:** 47,000 → 15,600, all owned.
- **Superseded content in retrieval:** eliminated by valid-from/valid-to.
- **Personal working documents with patient data:** 8,000 removed.
- **Documents from transferred services:** 4,000 removed.
- **Silently broken source feeds found by refresh monitoring:** 7 in the first year.
- **Retrieval quality:** their top-5 accuracy improved from 61% to 84% on a fixed question set, purely from removing unowned content.

That last figure surprised them. The governance exercise, undertaken for compliance reasons, produced the largest single quality improvement in the system's history — because a third of the corpus had been noise.

### The line in their information governance policy

*If nobody will put their name to it, we do not index it. A source with no owner is not a source; it is a file.*

---

## Composition

Four source platforms on the left, converging on a central register, splitting into two outcomes on the right.

**Left:** four blue platforms, each with an icon and a dark card listing five rows with blue icons — **POLICY** (shield with lines), **CASE RECORD** (folder with a person), **PAYMENT LEDGER** (ledger with `$`), **CUSTOMER UPLOAD** (cloud with an up-arrow). Each card lists **OWNER** (person), **AUTHORITY** (institution), **PURPOSE** (target), **REFRESH** (cycle arrows), **SENSITIVITY** (padlock).

**Cyan lines** converge into a single arrow entering **SOURCE REGISTER** — a blue book with a person glyph on a wide platform, carrying the same five fields on a larger card.

**Right, upper:** a **teal line** leads to a **red X** blocking a **coral-bordered UNKNOWN OWNER card** with the same five rows in red.

**Right, lower:** a **teal line** leads through a **teal shield with a check**, then a **stack of white documents with a green check and magnifier**, then to **APPROVED INTAKE CONTRACT** — a teal-bordered card with the five fields and a **teal rosette**.

## Element by element

**POLICY** — a blue shield containing document lines. Authoritative, published.
**CASE RECORD** — a blue folder with a person. Operational, personal.
**PAYMENT LEDGER** — a blue ledger with a currency symbol. Structured, financial.
**CUSTOMER UPLOAD** — a blue cloud with an upload arrow. External, unknown.

**SOURCE REGISTER** — a blue book with a person glyph, carrying the five-field contract.

**UNKNOWN OWNER** — a coral-bordered card with five red field rows and no values, blocked by a red cross.

**APPROVED INTAKE CONTRACT** — a teal-bordered card with five fields and a rosette badge.

## Colour and flow semantics

- **Cyan lines** carry sources into the register — intake.
- **Teal lines** carry the governed outcomes, both approval and refusal.
- **Coral and red** mark the blocked path and the incomplete card.
- **Teal** on the approval path marks verification and certification, consistent with teal meaning provenance and validation throughout the volume.
- The **identical five-field card** on every source and on the register is the composition's central device.

## How to present it

**Ask who owns the documents in their corpus.** Not who built the pipeline — who is accountable for accuracy. Most rooms cannot answer for most of their content.

**Read the five fields and ask what each is consumed by later.** Owner drives accountability. Authority drives conflict resolution. Purpose drives access. Refresh drives staleness detection. Sensitivity drives protection. None is administrative.

**Point at CUSTOMER UPLOAD.** The hard case, included deliberately. No owner by default, no established authority, unknown sensitivity. Ask how their system handles external content.

**Ask why the red card still has five rows.** It is not malformed; it is incomplete. Then ask why owner specifically blocks everything — because without it nobody maintains the other four.

**Tell the Halstead audit.** 47,000 documents, 12,000 owned. Then the breakdown: 19,000 superseded, 8,000 personal working documents with patient data, 4,000 from transferred services, 3,000 genuinely orphaned.

**Tell the transferred-service protocol incident.** A clinician read a protocol for a procedure Halstead no longer offered, caught by a conversation with a colleague rather than by the system.

**Give them the number that lands hardest.** Top-5 retrieval accuracy went from 61% to 84% purely from removing unowned content. A compliance exercise produced their largest quality improvement, because a third of the corpus was noise.

**Ask about the 3,000 orphans.** Relevant content, no owner. Halstead found 500 that genuinely mattered and had no maintenance path. Ask what their equivalent would be.

**Close on the word contract.** Two parties, obligations both ways. The owner commits to maintenance and notification; the system commits to purpose and protection. Ask which half their current arrangement has.

**Timing.** Twenty-five minutes. Thirty-five if you audit a sample of the room's own corpus for ownership, which reliably finds a category nobody claims.

---

## Lab and checkpoint

**Lab:** Audit a sample of your own corpus and assign the five fields to each source: owner, authority, purpose, refresh policy, and sensitivity. Identify any source with unknown owner and decide whether it is a customer upload, a transferred service, a personal working document, superseded, or genuinely orphaned. Then write the contract between owner and system for the retained sources.

**Checkpoint:** Why is an unknown owner a hard refusal rather than a warning?

**Answer:** Because without an owner there is nobody accountable for the accuracy, maintenance, and other four fields. The system cannot rely on the source, and warning would let it be used. Refusing forces the source to be claimed and documented.

## Glossary

- **Approval path** — the stages a source passes through before entering the register.
- **Authority** — the source or person that resolves conflicts about accuracy.
- **Contract** — the mutual obligations between the owner and the system.
- **Corpus** — the entire collection of sources available to the system.
- **Customer upload** — content supplied by a user, with no owner by default.
- **Orphaned** — content that is relevant but has no owner.
- **Owner** — the accountable party for a source.
- **Purpose** — the allowed use of the source.
- **Refresh policy** — the rule for how often the source is checked for updates.
- **Register** — the authoritative list of approved sources.
- **Sensitivity** — the protection level required for the source.
- **Unknown owner** — a source that cannot be used because no owner is recorded.

## Sources

- Information governance and source ownership
- Corpus quality and authority management
- Data provenance and sensitivity classification
