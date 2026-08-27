# Diagram 114 — Graph Relationship Retrieval

![SOURCE TEXT documents on dark navy feed ENTITY AND RELATIONSHIP EXTRACTION, producing a graph of five nodes — CUSTOMER, ORDER, PRODUCT, POLICY, PARTNER — connected by teal edges carrying small circular markers. A coral dashed edge from CUSTOMER to the right terminates in a red X. Two teal arrows lead right to LOCAL SEARCH with a magnifier and GLOBAL THEMES with a globe. A legend beneath reads SOURCE SPAN, CONFIDENCE, and UNSOURCED EDGE REMOVED.](../diagrams/114-graphrag-relationship-retrieval.png)

**Module:** Advanced retrieval
**Role in the course:** retrieving relationships rather than passages
**Layout:** text into extraction into a graph, serving two query types, with unsourced edges removed

---

## At a glance

Text becomes a **graph of entities and relationships**, and that graph serves two query types: **LOCAL SEARCH** and **GLOBAL THEMES**.

Every edge carries two things, named in the legend: a **SOURCE SPAN** and a **CONFIDENCE**.

And one edge is coral, dashed, and terminated by a red X: **UNSOURCED EDGE REMOVED**.

The removed edge is the diagram's subject. A graph built from text will produce relationships the text does not support, and the discipline is that every edge must point back at the span that asserts it.

---

## What the diagram teaches

### 1. Edges carry source spans, and the small circles on them say so

Look closely at the teal edges. Each carries **small circular markers** along its length.

The legend identifies them: **SOURCE SPAN** and **CONFIDENCE**.

An edge is not a fact. It is an **extracted claim about a fact**, and it must carry where it was extracted from and how confident the extractor was.

That is the property that makes a graph auditable. Asked why the graph says a customer is associated with a partner, you can point at the sentence.

### 2. The unsourced edge is drawn as coral and dashed, and it is removed

One edge leaves **CUSTOMER** heading right, rendered in **coral dashed** with a small circular marker, and terminates at a **red X**.

That edge was inferred rather than extracted. It is the kind of relationship a model produces when it reasons over the text rather than reading it — plausible, unsupported, and indistinguishable from a real edge once it is in the graph.

Removing it is the discipline. An edge with no source span does not enter.

That rule costs recall. Some inferred relationships are correct. The position is that an unverifiable edge in a knowledge graph is worse than a missing one, because everything downstream treats edges as established.

### 3. Five entity types, and their relationships are the domain

**CUSTOMER, ORDER, PRODUCT, POLICY, PARTNER.**

The five are connected in a pattern that carries meaning: customer to order, order to product, product to policy, policy to partner, and several cross-links.

That web is what a graph gives you that passages do not. A passage mentions a customer and an order. A graph lets you traverse from a customer, through their orders, to the products, to the policies governing those products, to the partner who supplies them.

No single passage contains that chain.

### 4. LOCAL SEARCH and GLOBAL THEMES are two genuinely different query modes

**LOCAL SEARCH** — a magnifier. Start at a node and traverse outward. *What policies apply to this customer's orders?*

**GLOBAL THEMES** — a globe. Look at the graph as a whole. *What are the common failure patterns across all partner relationships?*

Local search is a traversal. Global themes is an aggregation over the graph's structure — clustering, community detection, summarisation of subgraphs.

They have different costs and different failure modes. Local search over a graph with a wrong edge gives one wrong answer. Global themes over a graph with systematic extraction bias gives a confidently wrong picture of the whole corpus.

### 5. Extraction is a stage with its own quality problem

**ENTITY AND RELATIONSHIP EXTRACTION** — a document with a gear.

The gear says this is machinery, and machinery has failure modes.

Entity extraction produces duplicates: the same customer as three nodes because the text names them three ways. Relationship extraction produces edges that reverse direction, edges that conflate two relationships, and edges asserted from hedged language — *"may be associated with"* becoming an unqualified edge.

The confidence field is what carries that uncertainty forward. An edge extracted from hedged text should have a lower confidence than one from a direct assertion, and consumers should be able to see the difference.

### 6. A graph is a derived artefact, and it inherits everything upstream

The graph is built from **SOURCE TEXT**. Every property of that text propagates.

If chunking split a relationship across two chunks, the extractor may not see it. If the source is stale, the graph asserts stale relationships. If a document was mis-parsed, the entities extracted from it are wrong.

That dependency is worth stating because a graph *looks* authoritative. It is a structured, queryable, confident-seeming artefact, and it is exactly as good as the text it was extracted from.

### 7. Graph and passage retrieval are complementary, not alternative

The diagram shows a graph serving two query types and does not show it replacing passage retrieval.

The division: a graph answers questions about **relationships between things**. Passages answer questions about **what a document says**.

A question like *"what does the returns policy say about promotional items"* is a passage question. A question like *"which of this customer's orders are covered by policies that changed last quarter"* is a graph question.

Building a graph and abandoning passage retrieval loses the ability to quote, which loses citation.

A graph is one of several non-document evidence sources, and they all need normalising to the same shape:

![A query plan fanning to POLICY SEARCH, SQL LEDGER and CASE API, each returning through an identical EVIDENCE ADAPTER listing VALUE, SOURCE, AS OF, AUTHORITY and CITATION, merging under a MERGE CONTRACT with verified IDs, with free-form SQL and raw API dumps blocked.](../diagrams/115-structured-federated-retrieval.png)

An edge's **source span** is its citation and its **confidence** is its authority. A graph result entering an evidence packet must carry the same five fields as a ledger row, or downstream stages need a special case for it.

---

## Case study — Ravenhill Pharmaceuticals, the interaction that was inferred

Ravenhill manufactures generic medicines. Their regulatory affairs team maintains knowledge about products, their ingredients, the markets they are licensed in, the regulations governing each, and the manufacturing partners involved.

Questions are frequently relational: *which of our products contain an ingredient affected by this regulatory change, and which partners manufacture them?*

That is not a passage question. No document contains the answer.

### What they built

A knowledge graph extracted from regulatory correspondence, product dossiers, manufacturing agreements and market authorisations.

About 40,000 entities and 190,000 relationships.

### The problem they did not see for eight months

Their extraction produced edges from inference as well as from assertion.

Given a document stating that product A contains ingredient X, and a separate document stating that ingredient X is manufactured by partner P, the extractor produced an edge asserting that **product A is manufactured by partner P**.

That inference is frequently correct and it is not what either document says. Partner P supplies the ingredient; a different partner may manufacture the finished product.

**About 14% of their manufacturing relationships were inferred rather than extracted.**

### The incident

A regulatory change affected an ingredient. The team queried the graph for products containing it and the partners involved, and issued notifications to those partners.

**Two partners were notified who had no involvement** with the affected products. Both were competitors of the actual manufacturers.

The notifications disclosed which Ravenhill products contained the ingredient and which markets were affected — commercially sensitive information, sent to companies with no need to know it, on the basis of an edge nobody had asserted.

Ravenhill disclosed the error to both partners and to the actual manufacturers. One manufacturing relationship was not renewed.

### The audit

They sampled 2,000 edges and traced each to a source span.

**73% had a direct source span** — a sentence asserting the relationship.

**14% were inferred** from two or more source spans, with no single assertion.

**9% had a source span that did not support the edge** — extraction errors where the model had read a hedged or negated statement as an assertion. *"Product A is not manufactured by partner P"* had produced an edge in three sampled cases.

**4% had no traceable source at all.**

That last category was the most alarming, because nobody could explain where those edges had come from.

### The rebuild

**Every edge requires a source span, and unsourced edges are removed.**

Their 190,000 edges reduced to about 138,000. That is a 27% recall loss and they accepted it.

**Confidence recorded per edge**, derived from the extraction: direct assertion, hedged assertion, or list membership.

Hedged edges are retained with low confidence and are excluded from queries that drive external communication.

**Negation detection added.** The 9% category was largely negation, and their extractor had no negation handling. Adding it eliminated most of that class.

**Inferred relationships kept, and marked as inferred.**

This was the decision that took longest. The 14% inferred edges were frequently useful, and discarding them lost real capability.

Their resolution: inferred edges are retained in a **separate edge type**, visibly distinguished, and excluded by default. A query can opt into them, and any result including an inferred edge is flagged.

That preserved the capability while making the distinction impossible to miss.

**Local and global queries treated differently.**

Local traversals may use inferred edges on request. **Global theme analysis may not** — because systematic inference bias produces a picture of the corpus that is confidently wrong, and there is no per-result flag that helps when the output is a summary of everything.

### The finding from confidence distribution

Once confidence was recorded, they could examine it by source type.

**Edges extracted from manufacturing agreements had high confidence.** Those documents state relationships directly.

**Edges from regulatory correspondence had much lower confidence**, because correspondence discusses relationships obliquely — *"as previously agreed with your manufacturing partner"* — without naming them.

They stopped extracting manufacturing relationships from correspondence entirely, and extraction quality improved.

Nobody had known that one source type was contributing disproportionate error, because nothing had been measuring by source.

### Results

- **Edges:** 190,000 → 138,000 sourced, plus ~26,000 marked inferred.
- **Edges with no traceable source:** ~7,600 → 0.
- **Negation-error edges:** largely eliminated by negation detection.
- **Partners notified in error:** 2 → 0.
- **Global theme analysis:** now excludes inferred edges entirely.
- **Correspondence as a manufacturing-relationship source:** removed after confidence analysis.

### The line in their knowledge engineering standard

*An edge is a claim about a sentence. If you cannot point at the sentence, it is not an edge — it is an opinion the graph is presenting as a fact.*

---

## Composition

A left-to-right pipeline from text to graph to two query modes, with a legend beneath.

**Left:** **SOURCE TEXT** — a stack of white documents on a blue platform — cyan arrow → **ENTITY AND RELATIONSHIP EXTRACTION** — a blue platform with a document-and-gear glyph.

**Centre:** a cyan arrow into a large blue platform holding five blue node tiles — **CUSTOMER** (person), **ORDER** (trolley), **PRODUCT** (cube), **POLICY** (shield), **PARTNER** (handshake) — connected by **teal edges** carrying small circular markers.

A **coral dashed edge** leaves **CUSTOMER** to the upper right, carrying a circular marker, and terminates at a **red X**.

**Right:** two teal arrows lead to **LOCAL SEARCH** (blue magnifier) and **GLOBAL THEMES** (blue wireframe globe).

**Beneath:** three legend cards — a teal line with a circle reading **SOURCE SPAN**; a teal circle reading **CONFIDENCE**; a coral dashed line with a red X reading **UNSOURCED EDGE REMOVED**.

## Element by element

**SOURCE TEXT** — a stack of documents. Everything is derived from this.

**ENTITY AND RELATIONSHIP EXTRACTION** — a document with a gear. Machinery with failure modes.

**The five nodes** — CUSTOMER, ORDER, PRODUCT, POLICY, PARTNER.

**Teal edges with circular markers** — each carrying a source span and a confidence.

**The coral dashed edge** — inferred, unsourced, terminated by a red X.

**LOCAL SEARCH** — a magnifier. Traversal from a node.
**GLOBAL THEMES** — a globe. Aggregation over the graph.

## Colour and flow semantics

- **Cyan arrows** carry the extraction pipeline from text to graph.
- **Teal edges** connect the nodes and carry the source-span and confidence markers.
- **Teal arrows** carry the graph into both query modes.
- **Coral dashed** marks the single unsourced edge, terminated by a red X.
- The **legend is the only place the edge properties are named**, which makes reading it necessary rather than optional.

## How to present it

**Ask what a graph gives you that passages do not.** Relationships that no single passage contains. Then trace the chain: customer → order → product → policy → partner.

**Point at the circular markers on the edges and go to the legend.** Source span and confidence. An edge is an extracted claim, not a fact.

**Ask what an unsourced edge is.** Inference rather than extraction. Plausible, unsupported, and indistinguishable from a real edge once it is in the graph.

**Tell the Ravenhill notification.** Two partners notified about products they had no involvement with, on an edge nobody had asserted, disclosing commercially sensitive information to competitors of the actual manufacturers.

**Give them the audit breakdown.** 73% directly sourced, 14% inferred, 9% extraction errors including negation, 4% with no traceable source at all. Ask which category worries them most — the 4% usually does.

**Tell the negation finding.** *"Product A is not manufactured by partner P"* producing an edge. Their extractor had no negation handling.

**Present the inferred-edge decision as a genuine trade.** Discarding them lost real capability. Ravenhill kept them as a separate edge type, excluded by default, opt-in, and flagged. Ask the room which they would choose.

**Draw the local/global distinction on inferred edges.** Local traversal can flag an inferred edge in a result. A global theme summary cannot — systematic inference bias produces a confidently wrong picture with nowhere to put a flag.

**Tell the source-type confidence finding.** Manufacturing agreements state relationships; correspondence discusses them obliquely. Measuring confidence by source revealed one source type contributing disproportionate error, and they stopped extracting that relationship type from it.

**Note the dependency.** A graph looks authoritative and is exactly as good as the text it came from. Bad chunking, stale sources and parse errors all propagate.

**Close on the standard.** *An edge is a claim about a sentence.*

**Timing.** Twenty-five minutes. Thirty-five if you sample the room's own edges for traceable sources, which is usually uncomfortable.

---

## Lab and checkpoint

**Lab:** Take a small graph in your corpus and audit 20 edges. For each, find the source span, the extraction confidence, and the source type. Classify each edge as directly sourced, inferred, extraction error, or untraceable. Decide how your system should treat inferred edges and write the policy for exposing them.

**Checkpoint:** Why is an unsourced edge dangerous?

**Answer:** Because an unsourced edge is an inference or extraction error that looks like a fact once it is in the graph. It can be traversed and used to answer questions, and its lack of source makes it impossible to verify or correct.

## Glossary

- **Edge** — a relationship between entities in a graph.
- **Entity** — a node in the graph, such as a customer, product, or policy.
- **Extraction error** — a relationship incorrectly extracted from text.
- **Global themes** — high-level summaries derived from the graph.
- **GraphRAG** — retrieval that uses a knowledge graph alongside passages.
- **Inferred edge** — a relationship derived by reasoning rather than directly extracted.
- **Local search** — a query answered by traversing the graph around a specific entity.
- **Negation** — a sentence stating that a relationship does not hold, which an extractor can miss.
- **Source span** — the exact text in the source that supports an edge.
- **Traceable** — having a source span that can be checked.
- **Unsourced edge** — an edge with no supporting source.

## Sources

- GraphRAG and graph-based retrieval
- Entity and relationship extraction
- Source provenance and inferred-edge policies
