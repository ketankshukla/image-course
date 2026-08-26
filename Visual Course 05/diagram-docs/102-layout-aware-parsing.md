# Diagram 102 — Layout-Aware Parsing

![An INPUT PDF page on dark navy with five coloured dashed regions labelled HEADING, PARAGRAPH, TABLE, LIST and FOOTNOTE. A blue arrow leads to LAYOUT PARSER, then to DOCUMENT TREE — a panel of five coloured node tiles, each row carrying PAGE, BOUNDING BOX, PARENT and ORDER cells. A coral arrow branches from the PDF down to FLAT TEXT, a white card whose table region has collapsed into an undifferentiated dashed row, leading to a red CONTEXT LOST warning triangle.](../diagrams/102-layout-aware-parsing.png)

**Module:** Document engineering
**Role in the course:** why extraction order and structure must survive
**Layout:** one input taking two paths — a structured tree and a flattened loss

---

## At a glance

A PDF page with five labelled regions goes two ways.

Upward through a **LAYOUT PARSER** into a **DOCUMENT TREE**, where every node keeps four properties: **PAGE, BOUNDING BOX, PARENT, ORDER**.

Downward into **FLAT TEXT**, where the table region visibly collapses into an undifferentiated row, and onward to **CONTEXT LOST**.

The comparison is the whole diagram. Same input, two extractions, and the difference is not quality — it is whether four specific properties survive.

---

## What the diagram teaches

### 1. Five region types, and each behaves differently under extraction

**HEADING** — carries hierarchy. It tells you what the content beneath it is about, and where you are in the document.

**PARAGRAPH** — the easy case. Flows as text and survives most extraction.

**TABLE** — the hard case. Its meaning lives in the relationship between cells and their headers, which is spatial, and flattening destroys it.

**LIST** — ordered or unordered, and the ordering may be semantically significant. A numbered procedure flattened into prose loses the step boundaries.

**FOOTNOTE** — attached to something specific, often on a different part of the page, and frequently containing the qualification that changes the meaning of what it annotates.

The colour-coding in the diagram — cyan, purple, green, orange, yellow — gives each type an identity that persists into the document tree.

### 2. Four properties per node, and each enables something specific

**PAGE** — which page this came from. Required for citation. An answer that cites a document without a page is not checkable in a 400-page policy.

**BOUNDING BOX** — where on the page. This is what allows a citation to be *shown* — highlighted on the original — rather than merely referenced.

**PARENT** — what this node sits under. A paragraph's parent heading is what tells you it concerns refunds rather than returns.

**ORDER** — reading sequence. Not visual position; the order a human would read it. Multi-column layouts have visual positions that do not match reading order.

Take away any one and something breaks. No page, no citation. No bounding box, no visual verification. No parent, no context. No order, and a procedure's steps can arrive scrambled.

### 3. The document tree is a tree, and the parent column is why

The right-hand panel shows nodes connected by lines to a root, with each node carrying its four properties.

A tree rather than a list. That structure is what makes **PARENT** meaningful and what makes retrieval able to expand from a chunk to its section — the parent-child pattern later in the volume depends entirely on this.

A flat list of extracted regions, even with page numbers, cannot answer "what section is this in?"

### 4. The flat text path shows the loss rather than describing it

Follow the coral arrow down. The **FLAT TEXT** card shows body lines and, in the middle, a **dashed orange rectangle divided into cells that no longer align with anything** — the table, reduced to a run of values with no headers and no column structure.

That rendering is more useful than a label. You can see that the numbers are still present and that their meaning is gone.

A table cell reading `4.2` is meaningless without knowing it sits under "Maximum" and beside "Grade B". Flattened, it becomes a number in a sentence.

### 5. CONTEXT LOST is the terminal state, and it is silent

The red warning triangle at the end of the coral path.

The critical property of this failure: **nothing errors**. Flat text extraction succeeds. It produces text. The text is indexed, retrieved, and used.

The loss only becomes visible when someone checks an answer against the original and finds that a figure was attributed to the wrong row.

That silence is what makes layout-aware parsing worth the cost. The alternative does not fail loudly; it fails in the answers.

### 6. Footnotes are the sleeper problem

Included in the five regions and easy to skim past.

A footnote is typically at the bottom of a page, far from what it annotates, and frequently contains an exception: *"except where the customer has an existing arrangement"*, *"this rate applies to new business only"*.

Under flat extraction, the footnote text arrives at the end of the page's content, disconnected from the sentence it qualifies. A chunk containing the main statement omits the exception entirely.

The **PARENT** property is what fixes this — a footnote node's parent is the element it annotates, not the page.

### 7. This is an ingestion-time decision with permanent consequences

Everything downstream inherits it. Chunking, retrieval, citation, verification.

You cannot recover bounding boxes from flat text. You cannot reconstruct parent relationships from a run of paragraphs. Re-parsing means re-ingesting the entire corpus.

Which is why this diagram sits second in the volume, immediately after governance and before anything about chunks or search.

The immediate consumer is the chunker, which needs structural elements rather than a character stream:

![A policy document decomposing into SECTION, PARAGRAPH, LIST and TABLE, feeding a SEMANTIC CHUNKER that produces chunks carrying HEADING PATH and PAGE SPAN, with two bracketed WHOLE IDEA outputs and one coral BAD SPLIT.](../diagrams/105-semantic-chunk-boundaries.png)

The four elements entering that chunker are nodes from this diagram's document tree. A chunker fed flat text has only length to work with.

---

## Case study — Denholm Pensions, the table that moved a decimal

Denholm administers occupational pension schemes for about 340 employers. Their assistant helps administrators answer member questions about entitlements, contribution rates, and scheme rules.

The corpus is roughly 9,000 documents, of which about 1,200 are scheme rule books — long, structured, and dense with tables.

### The extraction they started with

A general-purpose PDF text extractor. It handled the prose well and everything else badly.

They knew tables were imperfect. Their assessment at the time was that most questions were about narrative rules rather than tabular data, and the tables would be a known limitation.

### The incident

An administrator asked what the employer contribution rate was for a member in a specific scheme, at a specific grade, who had joined after a specified date.

The rate depends on all three. The scheme's rule book carries it in a table: grades down the left, joining-date bands across the top, rates in the cells.

The assistant answered **4.2%**. The correct answer was **6.8%**.

Flat extraction had produced a run of numbers with the grade labels and date-band headers separated from them. The retrieved chunk contained the right table's values and no way to associate any value with any row or column. The assistant had picked a plausible one.

The administrator relayed 4.2% to the employer, who applied it for two payroll cycles before their own finance team queried the figure.

### The remediation

Under-contribution for 61 members across two months. Denholm made up the difference, which came to about £34,000, and reported the error to the scheme trustees.

The trustees' question was the one that mattered: *how many other tables are wrong?*

### The audit

They sampled 200 documents and manually compared extracted content against the originals.

**Tables:** 89% of tables with more than three columns had lost their header association. Of those, about a third contained figures that could plausibly be misattributed — rates, thresholds, limits.

**Footnotes:** 71% of footnotes were extracted as page-terminal text with no connection to what they annotated. Denholm's rule books use footnotes heavily for exceptions, and this meant that an exception's existence was frequently invisible to the chunk containing the rule it excepted.

**Multi-column pages:** 100% of the two-column pages in older rule books were interleaved — sentences from the left column alternating with the right. About 340 documents were affected, and the extracted text was in places nonsensical.

Nobody had noticed the third category because the interleaved text was rarely retrieved. It was noise, and it had been silently degrading retrieval for two years.

### The rebuild with layout-aware parsing

**Every node keeps the four properties.** Page, bounding box, parent, order.

**Tables extract structurally.** Each table becomes a node with child nodes per row, and each cell carries its column header and row label. A cell reading `6.8` is stored with the context that makes it meaningful.

Their chunker then renders a table row as a self-contained statement: *"Scheme A, Grade 3, joined on or after 2019-04-06: employer contribution 6.8%."*

That rendering is what made the tables retrievable. It also made them citable — the row's bounding box points at the exact cell on the exact page.

**Footnotes attach to their referent.** A footnote node's parent is the element carrying the reference mark, not the page. Chunks containing a rule now carry its exceptions.

This was the change with the widest effect. Denholm estimate that roughly 8% of their rule content is qualified by footnotes, and that content had been being retrieved without its qualifications.

**Reading order is derived from the layout, not from the file.** Two-column pages now extract in reading order.

**Bounding boxes enabled visual citation.** An administrator clicking a citation sees the original page with the cited region highlighted. This was intended as a convenience and became their primary verification mechanism — administrators check the highlight rather than reading the answer's prose.

### The verification finding

Six weeks after launch, an administrator reported that a highlighted region did not match the quoted text.

Investigation found a bounding-box offset on documents produced by one particular scanning process — a consistent 4mm vertical shift that made highlights land one line low.

Nobody had spotted it in the answers, because the text was correct. It was only visible because the bounding box made the claim checkable.

They fixed the offset and added a spot check comparing extracted text against the text within its own bounding box, which has since caught two more extraction problems.

### Results

- **Tables with header association preserved:** 11% → 99%.
- **Footnotes attached to their referent:** 29% → 97%.
- **Documents with interleaved multi-column text:** 340 → 0.
- **Contribution-rate errors:** 1 known incident, 0 since.
- **Top-5 retrieval accuracy on table-dependent questions:** 34% → 91%.

That last figure is the one their product lead quotes. Table-dependent questions had been the assistant's worst category by a large margin, and the fix was not in retrieval at all.

### The line in their engineering notes

*We spent a year tuning search over text that had already lost the thing the question was about.*

---

## Composition

One input branching into two paths, upper and lower.

**Left:** **INPUT PDF** — a white page with a folded corner on a blue platform, carrying five coloured dashed regions, each connected by a short line to a labelled tag: **HEADING** (cyan), **PARAGRAPH** (purple), **TABLE** (green), **LIST** (orange), **FOOTNOTE** (yellow).

**Upper path:** a **blue arrow** to **LAYOUT PARSER** — a blue rounded tile showing a layout-region glyph — then a **blue arrow** to **DOCUMENT TREE**, a dark panel containing a root node with connector lines to five coloured node tiles, each row followed by four cells reading **PAGE**, **BOUNDING BOX**, **PARENT**, **ORDER**.

**Lower path:** a **coral arrow** from the PDF to **FLAT TEXT** — a white card on a red platform, showing body lines with a **dashed orange cell region** in the middle where the table has collapsed — then a **coral arrow** to **CONTEXT LOST**, a red-outlined tile with a large warning triangle.

## Element by element

**INPUT PDF** — a white page with five colour-coded dashed regions.

**LAYOUT PARSER** — a blue tile showing a page-region layout glyph.

**DOCUMENT TREE** — a dark panel with a root node and five child nodes, colour-matched to the input regions, each carrying four property cells.

**FLAT TEXT** — a white card whose table region is a dashed row of cells with no header association.

**CONTEXT LOST** — a red-outlined tile with a white warning triangle.

## Colour and flow semantics

- **Blue arrows** carry the structured path from input through parser to tree.
- **Coral arrows** carry the flattened path to its terminal loss.
- **Region colours** — cyan, purple, green, orange, yellow — persist from the input page into the document tree nodes, showing identity survives parsing.
- The **four property cells** repeat on every tree row, asserting they are per-node rather than per-document.
- **Red** marks both the flat-text platform and the context-lost terminal.

## How to present it

**Ask what a PDF extractor produces.** Text. Then ask what it loses, and put the five region types up.

**Read the four node properties and ask what each enables.** Page for citation, bounding box for visual verification, parent for context, order for sequence. Then remove each in turn and name what breaks.

**Point at the flattened table in the FLAT TEXT card.** The numbers are still there. Their meaning is not. Ask what a cell reading `4.2` means without its row and column.

**Tell the Denholm contribution rate.** 4.2% instead of 6.8%, applied for two payroll cycles across 61 members, £34,000 to correct. Then the trustees' question: how many other tables are wrong?

**Give them the audit numbers.** 89% of wide tables lost header association. 71% of footnotes detached. 100% of two-column pages interleaved — and nobody had noticed the third because it was rarely retrieved.

**Dwell on footnotes.** They carry exceptions, they sit far from what they annotate, and flat extraction detaches them. Denholm estimated 8% of their rule content was qualified by footnotes that were being retrieved without their qualifications.

**Explain the table rendering fix.** A row becomes a self-contained sentence carrying its labels. That is what makes a table retrievable, and it is a chunking decision that depends entirely on structural extraction.

**Tell the bounding-box offset finding.** A 4mm vertical shift, invisible in the answers, visible only because the highlight made the claim checkable. Verification mechanisms find their own bugs.

**Emphasise that this is permanent.** You cannot recover bounding boxes from flat text. Re-parsing means re-ingesting everything. That is why it sits this early in the volume.

**Close on the engineering note.** *We spent a year tuning search over text that had already lost the thing the question was about.*

**Timing.** Twenty-five minutes. Thirty-five if you extract a real table both ways and compare, which is unusually persuasive.

---

## Lab and checkpoint

**Lab:** Take one PDF or document in your corpus. Extract it with a flat text extractor and with a layout-aware extractor that preserves region type, page, bounding box, parent, and reading order. Compare how a table, footnote, and two-column section are represented. Identify what context is lost in the flat version and how it would affect a retrieval query.

**Checkpoint:** Why is layout-aware parsing an ingestion-time decision with permanent consequences?

**Answer:** Because once the document is flattened, the structural information — region type, page, bounding box, parent, order — is gone. It cannot be recovered later without re-ingesting the source. The way you parse the document determines what can ever be retrieved and cited.

## Glossary

- **Bounding box** — the coordinates of a region on the page.
- **Document tree** — the hierarchical structure of regions in a document.
- **Flat text** — the lossy one-dimensional text extraction that discards layout.
- **Footnote** — a layout region that annotates or qualifies content elsewhere.
- **Header association** — the link between a table cell and its row and column labels.
- **Layout-aware parsing** — extraction that preserves the structural and spatial relationships in a document.
- **Order** — the intended reading sequence of regions.
- **Page** — the page number, used for citation and verification.
- **Parent** — the containing region that provides context.
- **Region type** — the kind of document area, such as heading, paragraph, table, or footnote.

## Sources

- PDF and document layout analysis
- Table extraction and header association
- Document parsing for RAG ingestion
