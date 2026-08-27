# Diagram 58 — Short-Term and Durable Memory

![Three memory stores on dark navy beneath a central white AGENT robot. WORKING MEMORY shows teal database cylinders with a brain-marked card, tagged TEMPORARY. A coral gate labelled CONSENT AND POLICY stands between it and USER PREFERENCE, teal cylinders with a person card, tagged RECALLABLE. BUSINESS RECORD shows teal cylinders with an institution card, tagged AUTHORITATIVE, written to by a DOMAIN SERVICE above it. Each store carries DELETE and EXPIRY control badges beneath its tag.](../diagrams/58-short-term-and-durable-memory.png)

**Module:** Memory and retrieval
**Role in the course:** what an agent may remember, and for how long
**Layout:** three stores with a consent gate between the first two, each carrying delete and expiry controls

---

## At a glance

Three memory stores, each with a one-word classification: **TEMPORARY**, **RECALLABLE**, **AUTHORITATIVE**. A **coral consent-and-policy gate** stands between the first and the second. Every store carries **DELETE** and **EXPIRY** controls.

Two claims. Memory is not one thing — it is three, with different lifetimes and different rules. And **anything crossing from temporary into durable passes a gate**, because remembering something about a person is a decision that requires permission.

---

## What the diagram teaches

### 1. Three stores, three tags, three different questions

**WORKING MEMORY — TEMPORARY.** What the agent is holding right now to do the current job. The brain icon is apt: this is active reasoning state. It has no long life and is not meant to.

**USER PREFERENCE — RECALLABLE.** Things about this person that make future interactions better. How they like to be addressed, their default location, their preferred format. Durable, personal, and — critically — theirs.

**BUSINESS RECORD — AUTHORITATIVE.** What the organisation holds as fact. The system of record. Written by the domain service, not by the agent.

The three tags are the useful compression. Ask of any piece of remembered information: is it temporary scratch, is it a recallable preference, or is it authoritative truth? Each answer implies a different store, lifetime, and governance.

### 2. The consent gate is coral, and its placement is precise

The gate sits **between working memory and user preference** — not before working memory, and not before the business record.

That placement encodes the actual rule. An agent may hold things temporarily to do its job without asking permission; that is what working memory is. But **promoting something from temporary to remembered-about-you requires consent**.

The gate is drawn as a physical barrier with a shield — coral, which throughout this library marks a gate that can refuse.

The practical consequence: an agent that notices a user mentioning their new address cannot simply store it as a preference. That crossing is governed. The user has to have agreed that this kind of thing is remembered.

### 3. The business record has no consent gate, and that is not an oversight

Look carefully: the coral gate stands between store one and store two. Nothing stands between working memory and the business record.

Instead, the business record is written by the **DOMAIN SERVICE**, reached by a separate arrow from above, labelled **WRITES**.

The claim is that business truth does not enter through the memory path at all. It enters through the domain service, under that service's own rules, with its own authorisation and its own receipt. The agent does not write authoritative records; it proposes, and the domain service writes.

This is the same separation as the conversation-versus-workflow lanes:

![Two lanes — CONVERSATION STATE holding chat history and display text, and WORKFLOW STATE holding case ID, action status, receipt and owner — with an agent reading both and a domain service writing business truth, beside a coral warning reading CHAT IS NOT A DATABASE.](../diagrams/52-conversation-vs-workflow-state.png)

Consent governs what is remembered *about a person*. Authorisation governs what is written *as fact*. Two different controls for two different concerns.

### 4. Every store has delete and expiry, and both are drawn

Beneath each tag sit two teal control badges: a **bin (DELETE)** and a **clock (EXPIRY)**.

Repeating them under all three stores makes the point that these are not features of one store — they are obligations on all of them.

**Delete** — the ability to remove something on request. For user preferences this is a legal requirement in most jurisdictions. For working memory it should be trivial. For business records it is governed by retention policy, and "delete" may mean "mark void and retain per policy" rather than erase.

**Expiry** — automatic removal after a defined period. The control that prevents indefinite accumulation.

The two are different and both are needed. Delete is reactive and per-item; expiry is proactive and by policy. A store with delete but no expiry accumulates forever unless someone asks. A store with expiry but no delete cannot honour a request made before the expiry elapses.

### 5. The agent reads from all three and writes to none directly

Trace the arrows. Cyan lines rise from **working memory**, **user preference** and **business record** up into the **AGENT**. One line descends from the agent into working memory.

The agent reads everything and writes only to its own scratch space. Preferences require the consent gate; business records come from the domain service.

That asymmetry is the security property. An agent that could write directly to any store could persist anything it inferred, permanently, without anyone agreeing to it.

### 6. Expiry lengths should differ per store, and the diagram does not say what they are

An honest gap worth filling when teaching.

**Working memory** — measured in the lifetime of a task. Minutes to hours. It should not survive the work it exists for.

**User preference** — measured in the relationship. Months to years, with re-confirmation. A preference stated once eighteen months ago and never used since is questionable to keep.

**Business record** — measured by regulation and business need. Years, and not the agent's decision.

Applying one retention policy across all three is the common mistake, and it fails in both directions: business records deleted too early, and working memory retained far past any justification.

---

## Case study — Bellweather Health Insurance, the preference nobody consented to

Bellweather provides private medical insurance to about 400,000 members. They built a servicing assistant handling claims questions, policy queries, and pre-authorisation requests.

To make it feel helpful, the first version remembered things. If a member mentioned during a call that they had a new employer, or that they preferred email over phone, or that they were managing a long-term condition, the assistant stored it and used it next time.

Members liked it. Their data protection officer did not.

### What the review found

The assistant had accumulated, across 400,000 members, a store of inferred facts that nobody had consented to and that members did not know existed.

Three categories, in ascending order of seriousness.

**Innocuous preferences.** Contact preference, preferred name, time of day they usually call. Roughly 180,000 members had at least one. Not sensitive, and still stored without consent.

**Circumstantial facts.** Employer, family situation, whether they were travelling. About 60,000 members. Some of it was out of date — an employer noted fourteen months earlier that was no longer current, being used to shape responses.

**Health inferences.** This was the finding that stopped the system. The assistant had, in about 9,000 cases, recorded inferences about members' health conditions derived from what they had asked about — not from their claims data, but from the content of their questions.

A member who asked twice about physiotherapy coverage had "possible musculoskeletal condition" against their record. Nobody had entered that. The assistant had inferred it and stored it as a preference to make future conversations more relevant.

Under their regulatory obligations, health information is special category data requiring explicit consent and specific handling. Bellweather had created a health data store by accident.

### The rebuild

**Three stores, explicitly separated.**

*Working memory* — everything the assistant holds during a conversation. Cleared when the conversation ends, hard expiry at 4 hours for interrupted sessions. Never promoted automatically.

*User preference* — only what the member has explicitly agreed to have remembered, from a defined list. Contact preference, preferred name, communication format, accessibility requirements. Four categories, and nothing else can enter.

*Business record* — claims, policy details, authorisations. Written only by their policy administration service, never by the assistant.

**A real consent gate.** Promoting anything from working memory to preference requires an explicit member action. The assistant asks: *"Would you like me to remember that you prefer email?"* and stores it only on a yes.

The gate is enforced in code, not in prompting. There is no path by which the assistant can write a preference without a recorded consent event.

**An allowlist, not a blocklist.** Their first attempt blocked health-related inferences specifically. Their DPO rejected it: a blocklist requires you to anticipate every category you should not store, and the health inferences had not been anticipated the first time either.

The allowlist inverts it. Four permitted preference types. Anything not on the list cannot be stored, whether or not anyone thought of it.

**Delete and expiry per store.** Working memory: 4 hours. Preferences: 24 months, with re-confirmation prompted at 18. Business records: per their regulatory retention schedule, which is 7 years after policy end and is not the assistant's concern.

Members can view and delete their preferences from their account. This surfaced something useful: about 12% of members who looked at their stored preferences deleted at least one, mostly stale contact preferences.

**The existing store was deleted.** All 9,000 health inferences, all 60,000 circumstantial facts, and the 180,000 unconsented preferences. Members were notified. It was the right call and it was not a comfortable meeting.

### What it cost and what it returned

The rebuild took nine weeks. Deleting the accumulated store made the assistant measurably less personalised for a period, and satisfaction scores dipped about four points before recovering as consented preferences accumulated.

Eighteen months later, roughly 140,000 members have at least one consented preference — fewer than the 180,000 that had been stored without asking, but every one of them is defensible.

### The reasoning their DPO uses

*The question is never "is this useful to remember." It is "did they agree that we would."*

---

## Composition

A central agent above three stores, with a consent gate between the first two and a domain service above the third.

**AGENT** sits at top centre — a white robot on a blue platform. A cyan line descends left into **WORKING MEMORY**; cyan lines rise from **USER PREFERENCE** and **BUSINESS RECORD** back up into it.

Left to right along the base: **WORKING MEMORY** → **[coral consent gate]** → **USER PREFERENCE** → **BUSINESS RECORD**, with cyan arrows between the first three.

**DOMAIN SERVICE** sits at upper right, sending a teal line labelled **WRITES** down into the business record.

Each store carries a dark tag panel beneath it — **TEMPORARY**, **RECALLABLE**, **AUTHORITATIVE** — and below that two teal circular badges: a **bin** labelled **DELETE** and a **clock** labelled **EXPIRY**.

## Element by element

**AGENT**
A white rounded robot with teal eyes, on a blue platform with a dark **AGENT** nameplate.

**WORKING MEMORY**
Three **teal database cylinders** beside a white card carrying a **teal brain icon**. Tagged **TEMPORARY**.

**The consent gate**
A **coral archway** with vertical bars, carrying a **coral shield with a white check**, on a plinth reading **CONSENT AND POLICY**. The only coral element in the diagram.

**USER PREFERENCE**
Three **teal database cylinders** beside a white card carrying a **teal person icon**. Tagged **RECALLABLE**.

**BUSINESS RECORD**
Three **teal database cylinders** beside a white card carrying a **teal institution icon**. Tagged **AUTHORITATIVE**.

**DOMAIN SERVICE**
A dark outlined panel at upper right, connected downward by a teal line labelled **WRITES** in cyan.

**The control badges**
Beneath each tag, two teal circular badges: a **waste bin** labelled **DELETE** and a **clock face** labelled **EXPIRY**.

## Colour and flow semantics

- **Cyan** carries the agent's reads and its single write to working memory.
- **Coral** appears once, on the consent gate — the only thing in the diagram that can refuse.
- **Teal** marks all three stores, all six control badges, and the domain service's write.
- The **repetition of DELETE and EXPIRY under every store** asserts them as universal obligations rather than per-store features.
- The **domain service's separate arrow** keeps business truth off the memory path entirely.

## How to present it

**Ask what an agent should remember.** Rooms usually answer in terms of usefulness. Then introduce the three tags and re-ask: is this temporary scratch, a recallable preference, or authoritative truth? Three different answers, three different sets of rules.

**Point at where the coral gate sits.** Between temporary and recallable — not before working memory, and not before the business record. Ask why. An agent may hold things to do its job; promoting them to remembered-about-you is a decision requiring permission.

**Ask why the business record has no consent gate.** Because it is not on the memory path. It is written by the domain service under authorisation, with a receipt. Consent governs what is remembered about a person; authorisation governs what is written as fact.

**Tell the Bellweather health-inference story.** Nine thousand members with inferred conditions derived from the questions they asked. Nobody entered it; the assistant created a special-category data store by being helpful.

**Make the allowlist argument.** Their first fix blocked health inferences. Their DPO rejected it because a blocklist requires anticipating every bad category — and the health inferences had not been anticipated the first time. Ask the room whether their own memory design is allow or block shaped.

**Ask about expiry lengths per store.** Working memory in task lifetimes, preferences in relationship lifetimes with re-confirmation, business records by regulation. Then ask what single retention policy they currently apply, and how it fails in both directions.

**Separate delete from expiry.** Delete is reactive and per-item; expiry is proactive and by policy. A store with only delete accumulates forever unless asked. Both badges appear under every store for a reason.

**Note the visible-preferences finding.** 12% of Bellweather members who looked at their stored preferences deleted one. Showing people what you remember is both a compliance measure and a data-quality one.

**Timing.** Twenty-five minutes. Thirty-five if you classify the room's own remembered data into the three tags, which reliably finds something in the wrong store.

---

## Lab and checkpoint

**Lab:** Classify one piece of data your agent currently remembers into one of the three stores: working memory, user preference, or business record. For each, write whether it is tagged as temporary, recallable, or authoritative, and who may write it. Then write the delete and expiry rules and the consent or authorisation that applies.

**Checkpoint:** Why does the business record have no consent gate?

**Answer:** Because the business record is not on the memory path. It is written by a domain service under authorisation, with a receipt. Consent governs what is remembered about a person; authorisation and receipt govern what is written as fact.

## Glossary

- **Allowlist** — a list of categories that may be remembered, with everything else blocked.
- **Authoritative** — the tag for business records, written by domain services under authorisation.
- **Business record** — durable truth about the world, not memory about a person.
- **Consent and policy** — the gate that decides what can move from working memory to a recallable user preference.
- **Delete** — reactive, per-item removal of data.
- **Expiry** — proactive, policy-driven data removal.
- **Recallable** — the tag for user preferences that may be remembered.
- **Temporary** — the tag for working memory in a single task.
- **User preference** — a stored preference about how the user wants the agent to behave.
- **Working memory** — short-term context for the current task.

## Sources

- Agent memory, preference, and record separation
- Data-protection consent and purpose-limitation
- Retention, deletion, and expiry policy design
