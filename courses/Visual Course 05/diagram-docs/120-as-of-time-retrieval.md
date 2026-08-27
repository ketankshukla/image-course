# Diagram 120 — Temporal Retrieval

![Two parallel timelines on dark navy. The upper, BUSINESS TIME (EFFECTIVE TIME), carries three policy cards — V6 valid 2024-01-01 to 2025-01-31, V7 valid 2025-02-01 to 2026-12-31, V8 valid 2027-01-01 to 2027-12-31. A QUERY AS OF 2026-05-10 banner drops an arrow into V7. The lower, SYSTEM TIME (RECORD TIME), carries four timestamped tiles reading dates with UTC times. A TEMPORAL EVIDENCE PACKET case shows TIME BASIS: BUSINESS TIME AS OF 2026-05-10, leading to SELECTED EVIDENCE FROM POLICY V7.](../diagrams/120-as-of-time-retrieval.png)

**Module:** Freshness and change
**Role in the course:** answering questions about the past
**Layout:** two parallel timelines, a dated query selecting one version, and an evidence packet declaring its time basis

---

## At a glance

Two timelines. **BUSINESS TIME (EFFECTIVE TIME)** carries policy versions with valid-from and valid-to dates. **SYSTEM TIME (RECORD TIME)** carries timestamps of when each was recorded.

A query dated **2026-05-10** drops into **POLICY V7**, whose validity spans that date.

And the evidence packet declares its **TIME BASIS** explicitly.

Two clocks, and a query must say which one it means.

---

## What the diagram teaches

### 1. Business time and system time are genuinely different

**BUSINESS TIME** — a calendar with a clock. When something was true in the world.

**SYSTEM TIME** — a database with a clock. When we recorded it.

They diverge routinely. Look at the diagram's own values: Policy V7 is valid from **2025-02-01** and was recorded at **2025-02-01 09:08:47 UTC** — same day. But V6 is valid from **2024-01-01** and was recorded at **2024-01-02 10:15:22 UTC** — a day later.

V8 is valid from **2027-01-01** and recorded **2027-01-01 11:42:13** — a future-dated policy already in the system.

Three relationships: recorded after it became effective, recorded on the day, and recorded in advance.

### 2. The valid-from and valid-to pairs are non-overlapping and contiguous

V6: **2024-01-01 to 2025-01-31**.
V7: **2025-02-01 to 2026-12-31**.
V8: **2027-01-01 to 2027-12-31**.

No gaps between V6's end and V7's start. No overlaps.

That contiguity is what makes as-of selection unambiguous. Any date falls in exactly one version's window, and the selection is a lookup rather than a judgement.

Real corpora frequently violate this — gaps where no version was in force, overlaps where two were. Both need resolving at ingestion, because a query landing in a gap or an overlap has no defined answer.

### 3. The query is dated, and the date does the selection

**QUERY AS OF 2026-05-10**, with a **blue arrow dropping into V7**.

The date is on the query, not on the system. The system does not have a notion of "now" that governs retrieval; each query carries its own temporal reference.

That is what allows two users to ask the same question with different dates and receive different, both-correct answers.

### 4. The evidence packet declares its TIME BASIS

The case at the bottom carries **TIME BASIS: BUSINESS TIME AS OF 2026-05-10**.

Not just the date — the **basis**. Which clock was used.

That matters because the same date means different things on the two timelines. *As of 2026-05-10 in business time* means the policy in force on that date. *As of 2026-05-10 in system time* means what our system held on that date, which may be a policy that was later corrected.

An evidence packet without a declared basis is ambiguous, and the ambiguity is invisible.

### 5. System time is what answers "what did we know then"

The lower timeline exists for a distinct class of question.

*"What did the system tell the adviser when they gave that advice in March?"*

That is not a business-time question. The business-time answer is what was in force in March. The system-time answer is what our records held in March — which may differ if a correction was made afterwards.

For dispute resolution, complaint handling and regulatory investigation, the second is frequently the one asked.

### 6. SELECTED EVIDENCE FROM POLICY V7 names the version, not just the content

The output tile names the version explicitly.

An answer that says "the rate is 4.2%" is incomplete. An answer that says "the rate is 4.2% under Policy V7, in force from 2025-02-01 to 2026-12-31" is checkable.

Naming the version is what connects temporal retrieval to citation. The citation must point at a version, not at a document, because the document has several.

### 7. Future-dated content is visible and not yet applicable

V8 is valid from **2027-01-01** and is in the system.

A query as of 2026-05-10 does not select it. But it exists, it is indexed, and a query as of 2027-06-01 would select it.

That is a real requirement. Policy changes are frequently published in advance, and a system that only holds current content cannot answer "what will the position be in January."

It also means the current-version query must be careful: the newest version is not necessarily the applicable one.

None of this is possible unless every version's derived artefacts were retained:

![Two parallel lineages, one per source version, each running through an ingest run to a version record listing CONTENT HASH, FETCHED AT, VALID FROM and PARSER VERSION, fanning out to its own parse, chunks and index, with a coral NEVER OVERWRITTEN lock.](../diagrams/117-immutable-source-versions.png)

Selecting Policy V7 for a 2026 query means retrieving from **INDEX V7**, which exists only because it was never overwritten. A system that keeps old source documents and regenerates its index in place can name the right version and cannot search it.

---

## Case study — Marlingford Mutual, the complaint about advice given two years ago

Marlingford is a life and pensions provider with about 480,000 policyholders. Their adviser support system helps staff answer questions about product terms, charges and benefit entitlements.

Product terms change. Their charging structure has been revised four times in six years, and changes apply to policies issued after the change date while existing policies remain on their original terms.

### The problem their corpus has

At any moment, five different charging structures are simultaneously in force, each applying to a different cohort of policyholders.

A question about charges has no single answer. It has an answer per cohort.

### What their first system did

Indexed the current version of each document. Answered from it.

For a policyholder on the current terms, correct. For the roughly 70% on earlier terms, wrong.

### The immediate mitigation and why it was insufficient

They added the policy issue date as a filter and indexed all versions.

That handled the cohort problem. It did not handle the second question, and the second question is what produced the complaint.

### The complaint

A policyholder complained that advice given in 2024 about their exit charges had been incorrect.

Marlingford investigated. Under the terms applicable to that policyholder's cohort, the charge stated in the 2024 advice was **wrong** — the correct figure was different.

But their records showed the adviser had used the system correctly.

The explanation: a **correction** had been made to that version of the terms document in 2025. The version had been misstated when originally ingested — a transcription error in the charge table — and had been corrected fourteen months later.

The adviser in 2024 had been given the erroneous figure, because that was what the system held at the time.

### Why they could not initially demonstrate this

Their system was business-time aware. It could answer *what were the terms for that cohort*.

It could not answer *what did our system say those terms were in March 2024*.

The correction had been applied by updating the version record. The erroneous prior state was not retained.

They knew a correction had been made because the change log recorded it. They could not reconstruct what the adviser had actually seen.

### The rebuild as bitemporal

**Both timelines retained.**

Every version record carries valid-from and valid-to (business time) **and** recorded-from and recorded-to (system time).

A correction does not update a record. It closes the erroneous record's system-time validity and opens a new one with the same business-time validity and the corrected content.

That means the erroneous state is preserved as a fact about what the system held between two dates.

**Queries declare a time basis.**

Their adviser interface defaults to business time as of today, which is the normal case.

Their complaint-handling interface defaults to **system time as of the date under investigation**, which reconstructs what the system held.

That second interface is what would have resolved the complaint in an hour rather than three weeks.

**The evidence packet declares the basis and the version.**

> Time basis: business time as of 2026-08-14 · Terms version: Series 4 (valid 2019-04-06 to 2022-03-31) · Record version: corrected 2025-06-11

Three facts, and advisers read the third when something looks unexpected.

**Gaps and overlaps resolved at ingestion.**

The bitemporal model made their existing data problems visible. Auditing validity ranges found **31 gaps** — periods with no version in force — and **eight overlaps**.

Most gaps were administrative: a version's valid-to date set to the day before the next version's valid-from, off by one, leaving a single uncovered day.

The overlaps were more serious. Two were cases where a change had been applied without closing the previous version, meaning two contradictory versions had both been valid for a period of months.

### The future-dated finding

Building the temporal model let them index announced-but-not-yet-effective changes.

Their product team had been maintaining a separate spreadsheet of upcoming changes, because the system could not hold them.

Now a change announced in October and effective the following April is indexed on announcement, invisible to as-of-today queries, and available to advisers asking what will apply from April.

That capability was not part of the plan. It eliminated a spreadsheet that had been the source of two known advice errors.

### Results

- **Complaint resolution for historical advice:** three weeks → about an hour.
- **Validity gaps found and closed:** 31.
- **Validity overlaps found:** 8, of which 2 were contradictory versions both valid for months.
- **Corrections:** now preserved as system-time states rather than overwriting.
- **Future-dated changes:** newly holdable, eliminating a manually-maintained spreadsheet.

### The line in their advice governance standard

*Two questions, two clocks. What was true, and what did we say was true. Answering the second is how you defend the first.*

---

## Composition

Two horizontal timelines with a dated query above and an evidence packet below.

**Upper timeline:** a blue arrow labelled **TIME**, carrying three white policy cards on dark headers — **POLICY V6** (valid from 2024-01-01, valid to 2025-01-31), **POLICY V7** (2025-02-01 to 2026-12-31, highlighted with a blue border), **POLICY V8** (2027-01-01 to 2027-12-31). Each field carries a calendar icon.

**Left of the upper timeline:** a bordered tag with a **calendar and clock** reading **BUSINESS TIME (EFFECTIVE TIME)**.

**Above:** a bordered **QUERY AS OF 2026-05-10** banner with a blue arrow dropping down into **POLICY V7**.

**Lower timeline:** a **teal dashed arrow** labelled **RECORDED AT**, carrying four teal-bordered tiles with clock icons: **2024-01-02 10:15:22 UTC**, **2025-02-01 09:08:47 UTC**, and **2027-01-01 11:42:13 UTC**.

**Left of the lower timeline:** a bordered tag with a **teal database and clock** reading **SYSTEM TIME (RECORD TIME)**.

**Centre-bottom:** a blue arrow from V7 down into **TEMPORAL EVIDENCE PACKET** — a white case with a blue header, carrying **TIME BASIS** and a highlighted tile reading **BUSINESS TIME AS OF 2026-05-10**.

**Right:** a blue arrow to a bordered tile with documents and a teal shield reading **SELECTED EVIDENCE FROM POLICY V7**.

## Element by element

**BUSINESS TIME** — a calendar with a clock. When it was true.
**SYSTEM TIME** — a database with a clock. When we recorded it.

**POLICY V6 / V7 / V8** — three versions with contiguous, non-overlapping validity ranges.

**QUERY AS OF** — a dated query, selecting by business time.

**TEMPORAL EVIDENCE PACKET** — declaring its time basis explicitly.

**SELECTED EVIDENCE FROM POLICY V7** — naming the version, not just the content.

## Colour and flow semantics

- **Blue** marks the business-time timeline, the query, and the selection path.
- **Teal** marks the system-time timeline and its timestamps — dashed, because it is a parallel record rather than the primary axis.
- **POLICY V7 is highlighted** with a blue border, marking it as selected.
- The **two timelines run parallel and never intersect**, which is the diagram's structural claim.
- The **TIME BASIS tile** is highlighted within the packet, marking it as the declaration rather than a detail.

## How to present it

**Read the two timeline labels.** Effective time and record time. Then ask which one their system has. Most have neither explicitly; they have "the current version."

**Point at the three recorded-at timestamps and compare them to the valid-from dates.** One recorded a day late, one on the day, one in advance. Three different relationships between the clocks.

**Ask what question each clock answers.** Business time: what was true. System time: what did we say was true.

**Tell the Marlingford complaint.** Advice given in 2024 with a figure that was wrong under the applicable terms, and an adviser who had used the system correctly — because the version had been misstated at ingestion and corrected fourteen months later.

**Make the distinction sharp.** They were business-time aware and could say what the terms were. They could not say what their system had said the terms were, which is what the complaint was about.

**Explain how a correction works bitemporally.** It does not update the record. It closes the erroneous record's system-time validity and opens a new one with the same business-time validity and corrected content. The erroneous state is preserved as a fact.

**Point at the contiguous validity ranges.** No gaps, no overlaps, so any date falls in exactly one window. Then note that real corpora violate this — Marlingford found 31 gaps and 8 overlaps, two of which were contradictory versions valid simultaneously for months.

**Read the TIME BASIS declaration.** An evidence packet without one is ambiguous, and the ambiguity is invisible.

**Point at V8 being future-dated.** Indexed, invisible to as-of-today queries, available to a query about next year. Then give the spreadsheet finding: a manually-maintained list of upcoming changes that had been the source of two advice errors.

**Warn about the current-version trap.** The newest version is not necessarily the applicable one, once future-dated content is held.

**Close on the standard.** *Two questions, two clocks. Answering the second is how you defend the first.*

**Timing.** Twenty-five minutes. Thirty-five if you audit the room's validity ranges for gaps and overlaps, which almost always finds some.

---

## Lab and checkpoint

**Lab:** Pick one corpus that changes over time. Add `valid_from` and `valid_to` to every version and ensure the ranges are contiguous and non-overlapping. Add `recorded_at` for system time. Run a dated query and make the evidence packet declare its time basis. Audit for gaps, overlaps, and future-dated content.

**Checkpoint:** Why is the newest version not always the applicable one?

**Answer:** Because a version can be future-dated. It may be indexed but not yet applicable. Querying for today must not return the future-dated version. Without explicit validity dates, the system will always return the newest record, which may be wrong for the question's time.

## Glossary

- **As-of-time retrieval** — answering a question using evidence valid at a specific date.
- **Bitemporal** — keeping both business time and system time.
- **Business time** — the time the content was authoritative in the real world.
- **Effective time** — the same as business time.
- **Future-dated** — a version that is stored but not yet applicable.
- **Record time** — the time the system recorded the content.
- **Selected evidence** — the evidence chosen for the answer.
- **System time** — the time the system knew or stated the content.
- **Time basis** — the declared date for which an evidence packet is valid.
- **Valid from / valid to** — the business-time range of a version.

## Sources

- Bitemporal databases and as-of-time queries
- Version validity and future-dated content
- Evidence packet time-basis declaration
