# Diagram 108 — Tenant-Safe Index Design

![Two user platforms on the left of a dark navy frame — TENANT A and TENANT B, each a person at a laptop — send cyan arrows into a QUERY ROUTER cube bearing a shield. Above it, a SERVER-TRUSTED TENANT ID card sends a cyan arrow down into the router. A cyan arrow leads right to INDEX PARTITION A, a bordered panel holding TEXT INDEX with EXACT SEARCH, VECTOR INDEX with HNSW and a SPEED–RECALL gauge, and VERSION ALIAS with a checked tag. INDEX PARTITION B below is identical. Two coral dashed lines cross between the router and the partitions, meeting at a red X above a CROSS-TENANT BLOCKED tile.](../diagrams/108-tenant-safe-index-design.png)

**Module:** Chunking and representation
**Role in the course:** separate indexes, and where the tenant identity comes from
**Layout:** two tenants through one router into two mirrored partitions, with the crossing paths blocked

---

## At a glance

Two tenants, one **QUERY ROUTER**, two **mirrored index partitions**. The router carries a shield and is fed from above by a **SERVER-TRUSTED TENANT ID**.

Two coral dashed lines cross in the middle, meet at a **red X**, and terminate at **CROSS-TENANT BLOCKED**.

The card feeding the router is the diagram's subject. The tenant identity comes from the **server**, not from the request — and everything else follows from that one property.

---

## What the diagram teaches

### 1. SERVER-TRUSTED TENANT ID enters from above, not from the tenants

Follow the arrows. Tenant A and Tenant B send queries *into* the router. The tenant identity comes down into the router from a **separate card above it**.

That geometry is the security property drawn.

If the tenant identity travelled with the query, a caller could assert it. Even with authentication, a request carrying a `tenant_id` parameter is a request whose most security-critical field is under the caller's control.

Server-trusted means the router derives the tenant from the authenticated session, on the server, and the request's own content has no say in it.

### 2. The two partitions are drawn identically, and identical means separate

**INDEX PARTITION A** and **INDEX PARTITION B** have the same three components, the same layout, the same everything.

That mirroring is the isolation claim. Not one index with a tenant field — two indexes.

The alternative, filtering a shared index by tenant metadata, has a specific and well-established weakness: relevance scores, result counts and nearest-neighbour computation happen over the whole space before filtering, which leaks information about what is in the parts you cannot see.

Drawing two complete partitions rather than one filtered index is a deliberate architectural position.

### 3. Each partition holds three things, and they serve different query types

**TEXT INDEX** with the annotation **EXACT SEARCH**. Lexical matching for identifiers.

**VECTOR INDEX** with **HNSW** and a **SPEED–RECALL gauge**. Approximate nearest neighbour, with the trade-off shown as a dial.

**VERSION ALIAS** with a checked tag on a database. A pointer to which index version is live.

Three components, one partition, per tenant. The isolation applies to all three — a shared vector index with per-tenant partitions in the text index would be isolation in name only.

### 4. The SPEED–RECALL gauge is the honest part of the vector index

A dial with a needle between **SPEED** and **RECALL**, running from teal through amber to red.

HNSW and every other approximate nearest-neighbour structure trades one for the other. Faster search examines fewer candidates and misses more true matches.

Drawing it as a dial rather than a setting makes two points. It is continuous — not fast or accurate, but a position between them. And it is a **choice**, which means somebody must make it and be able to justify it.

For a knowledge system where a missed result may mean a missed policy exception, that dial should sit further toward recall than a general-purpose search would.

### 5. VERSION ALIAS is in the partition, which means versions are per-tenant

The third component, a tag with a check on a database stack.

An alias pointing at the currently-live index version. Its presence inside the partition means each tenant's index can be at a different version.

That matters operationally. Promoting a new index version for one tenant while others remain on the previous one is what makes staged rollout possible — and it is what the safe promotion diagram later in the volume depends on.

A single global version means every promotion is all-or-nothing across every tenant.

### 6. The crossing paths are drawn and then blocked

Two coral dashed lines run from the router to the *opposite* partitions, crossing in the middle at a red X, with **CROSS-TENANT BLOCKED** beneath.

Drawing the forbidden path rather than omitting it is the right choice. The route exists — a routing bug, a misconfigured partition map, a null tenant defaulting to the first partition — and showing it blocked is stronger than pretending it is inconceivable.

The X sits at the crossing point, which is where the two wrong routes intersect. That is the single place a control belongs.

### 7. The router carries a shield, and it is the only enforcement point

A shield badge on the router cube.

One place where the tenant identity is resolved and one place where the partition is selected. The partitions themselves do not check — they serve whatever reaches them.

That concentration is what makes the control auditable. There is one code path to review, one place to instrument, and one alarm to raise.

It also means a bug in the router is total. Which is why the crossing paths are drawn: the control is single and therefore must be tested directly, not assumed.

Partition selection is the coarse boundary. Within a partition, a second and finer control still applies:

![An authenticated user passing through SERVER POLICY to an ALLOWED SCOPE, which excludes WRONG TENANT, RESTRICTED, EXPIRED and RETENTION HOLD while filtering a lexical index, a vector index and SQL.](../diagrams/111-authorization-before-search.png)

**WRONG TENANT** appears there as an exclusion category even though partitioning should make it impossible. That redundancy is deliberate: the partition is the structural control and the scope filter is the check that the structural control worked.

---

## Case study — Bramhope Analytics, the default that was tenant one

Bramhope provides regulatory reporting analytics to about 180 financial institutions. Each institution's data is confidential and several are direct competitors.

Their knowledge system indexes each institution's own filings, internal policy documents and correspondence with regulators.

### What they had

A shared vector index with a tenant field, filtered at query time. A shared text index, same arrangement.

It had passed a security review, because the reviewer confirmed that no document from another tenant was ever returned.

### The first finding

An external penetration test, commissioned by one of their clients rather than by Bramhope.

The tester held credentials for one institution. They could not retrieve another institution's documents and did not try.

Instead they measured **query latency and result counts** across a series of crafted queries.

Their vector index was a single HNSW graph containing all tenants' vectors. Nearest-neighbour search traverses the graph before filtering, so query time varied with the density of the neighbourhood — including neighbours belonging to other tenants.

By timing queries around specific terms, the tester established that another institution held a cluster of documents concerning a particular regulatory topic and approximate volume.

For competing institutions under the same regulator, knowing that a rival has a concentration of documents about a specific supervisory matter is meaningful information.

### The second finding, which was worse

Bramhope's own review, prompted by the first, examined their tenant filter.

A bulk import path constructed index records without a tenant value. The field defaulted to empty string.

Their filter query was `WHERE tenant = :caller_tenant`. An empty-string tenant matched nothing, so those records were invisible — which had masked the bug for eleven months.

Then a developer, fixing an unrelated issue, changed the filter to handle a null case. The change made empty-string records match a fallback branch that resolved to **the first tenant in their configuration**.

For nine days, roughly 4,000 records with no tenant were retrievable by one institution. Those records had been imported for three different institutions.

It was caught by a routine query-log review that noticed one tenant retrieving documents whose source system they had no relationship with.

### The rebuild

**Per-tenant index partitions.** Separate HNSW graphs, separate text indexes. 180 partitions.

Their vector infrastructure cost rose about 2.1×, which was the objection that had prevented this in the first place. The penetration test made it an easy conversation.

**Tenant identity derived server-side, never from the request.** The router resolves the tenant from the authenticated principal. There is no `tenant` parameter in their query API, and there is no code path that reads one.

That is the change their security lead considers most important: **it is not that the field is validated; it is that the field does not exist.**

**No default partition, ever.** A query whose tenant cannot be resolved raises rather than falling back. The empty-string case now fails loudly at index time — a record without a tenant cannot be written.

**Per-tenant version aliases.** A side benefit they had not sought. They now promote index versions per tenant, which let them run a chunking change on twelve willing institutions before rolling it wider.

**A cross-partition alarm.** Any query resolving to a partition other than the caller's raises immediately. It should be structurally impossible; it is monitored anyway.

It has fired once, during a partition rebalance, on a stale routing table entry. No query returned wrong data — the alarm fired on the routing decision, before the search ran.

### The recall dial

Separating the indexes forced a decision they had been avoiding.

Their shared HNSW graph had been configured for speed, because it served 180 tenants' traffic. Per-tenant graphs are far smaller, and the same speed is achievable at a much higher recall setting.

They moved the dial. Measured recall at their test set's top-10 went from 91% to 98.5%.

That improvement was free — a consequence of smaller graphs — and it would not have been available under the shared design.

### Results

- **Cross-tenant inference via timing:** eliminated structurally.
- **Records with no tenant:** 4,000 found, cause fixed, now impossible at write time.
- **Nine-day exposure:** 1 incident, caught by log review.
- **Vector infrastructure cost:** up ~2.1×.
- **Top-10 recall:** 91% → 98.5%, from smaller per-tenant graphs.
- **Cross-partition alarm firings:** 1, on a routing table, before any search ran.

### The line in their platform security standard

*The tenant is not a parameter. It is a property of the session, resolved on our side, and there is no request field that can influence it.*

---

## Composition

Two callers on the left, one router at centre, two mirrored partitions on the right, with blocked crossing paths.

**Left:** **TENANT A** and **TENANT B** — blue person figures at laptops with magnifiers, on blue platforms. Cyan arrows lead right.

**Above centre:** a bordered card with an ID glyph reading **SERVER-TRUSTED TENANT ID**, sending a **cyan arrow down** into the router.

**Centre:** **QUERY ROUTER** — a blue cube showing a server stack with a **blue shield** badge, on a blue platform.

**Right:** two identical bordered panels.

**INDEX PARTITION A** — three sub-panels: **TEXT INDEX** (white document) above a tag reading **EXACT SEARCH**; **VECTOR INDEX** (blue node graph) beside a **SPEED–RECALL gauge**, above a tag reading **HNSW**; **VERSION ALIAS** (teal database stack with a checked tag).

**INDEX PARTITION B** — identical.

**Cyan arrows** run from the router to each partition's correct destination.

**Two coral dashed lines** run from the router to the opposite partitions, crossing at a **red X**, with a coral-bordered **CROSS-TENANT BLOCKED** tile bearing a padlock beneath.

## Element by element

**TENANT A / TENANT B** — person figures at laptops. Two callers.

**SERVER-TRUSTED TENANT ID** — a bordered card with an ID glyph, entering the router from above.

**QUERY ROUTER** — a blue cube with a server stack and a shield. The single enforcement point.

**TEXT INDEX / EXACT SEARCH** — lexical matching.
**VECTOR INDEX / HNSW / SPEED–RECALL** — approximate nearest neighbour with its trade-off dial.
**VERSION ALIAS** — a checked tag on a database. Per-tenant versioning.

**CROSS-TENANT BLOCKED** — a coral tile with a padlock, beneath a red X at the crossing point.

## Colour and flow semantics

- **Cyan arrows** carry queries in and route them to the correct partition.
- The **tenant identity arrow enters from above**, separate from the query path — the diagram's central security claim.
- **Coral dashed lines** draw the forbidden crossing routes, blocked at their intersection.
- **The two partitions are rendered identically**, asserting separation rather than filtering.
- The **speed–recall gauge** runs teal → amber → red, presenting the trade-off as continuous.

## How to present it

**Ask where the tenant identity comes from in their system.** If it is a request field, that is the finding. Then point at the card entering from above.

**Give them the distinction.** It is not that the field is validated; it is that the field does not exist. A validated field is still a field a caller controls.

**Ask why two partitions rather than one filtered index.** Then tell the Bramhope timing attack: query latency varying with neighbourhood density in a shared HNSW graph, revealing that a competitor held a cluster of documents on a specific supervisory topic.

**Tell the empty-string default.** Records imported without a tenant, invisible for eleven months because empty matched nothing, then a null-handling fix that made them resolve to the first configured tenant. Nine days, 4,000 records, three institutions.

**Ask what their fallback behaviour is.** A query whose tenant cannot be resolved should raise, not default. Ask whether theirs has a default partition.

**Point at the speed–recall dial.** Continuous, and a choice somebody must justify. For a knowledge system where a missed result may be a missed exception, it should sit toward recall.

**Give them the free improvement.** Per-tenant graphs are smaller, so the same latency buys much higher recall. Bramhope went from 91% to 98.5% top-10 recall as a side effect of separation.

**Point at the version alias inside the partition.** Per-tenant versioning enables staged promotion. A single global version makes every promotion all-or-nothing.

**Ask about the impossible-condition alarm.** Bramhope monitor cross-partition routing even though it should be structurally impossible. It fired once, on a stale routing table, before any search ran.

**Handle the cost objection directly.** 2.1× vector infrastructure. Their conversation became easy after the penetration test, which is a poor way to fund it.

**Timing.** Twenty-five minutes. Thirty-five if you trace where the room's own tenant identity originates, which occasionally finds a request parameter.

---

## Lab and checkpoint

**Lab:** Trace the tenant identity in your search path. Is it set by a trusted server-side component, or does it come from a request field? If shared, locate the index partition logic and write the test that proves tenant A cannot query tenant B. Then tune the speed-recall dial for one tenant and version alias for promotion.

**Checkpoint:** Why should the tenant ID be server-trusted and not a request field, even if the field is validated?

**Answer:** Because a request field is controlled by the caller. Validation can be bypassed or misconfigured. A server-trusted tenant ID means the infrastructure sets the scope independently, so tenants cannot alter or guess it. Filtering on a caller-provided field is not the same as isolation.

## Glossary

- **HNSW** — a graph-based approximate nearest-neighbour index.
- **Impossible-condition alarm** — an alert for cross-tenant routing that should be structurally impossible.
- **Partition** — a separate index segment for one tenant.
- **Per-tenant version alias** — the pointer that lets a tenant promote an index version independently.
- **Recall** — the proportion of relevant results the index returns.
- **Router** — the shielded component that enforces tenant routing.
- **Server-trusted tenant ID** — the tenant identity set by the server, not the client.
- **Shared index** — a single index with metadata filtering, which is less isolated than partitions.
- **Speed-recall dial** — the trade-off between query latency and retrieval completeness.
- **Tenant** — the isolated customer or organisation boundary.
- **Version alias** — the pointer to the current index version for a tenant.

## Sources

- Multi-tenant vector index design
- Tenant isolation in HNSW and vector search
- Per-tenant versioning and staged promotion
