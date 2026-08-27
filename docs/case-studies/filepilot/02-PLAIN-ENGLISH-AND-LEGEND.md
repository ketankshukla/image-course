# FilePilot — The Whole Flow in Plain English

## At a glance

Think of FilePilot as a careful librarian. The librarian can read the labels, look inside permitted books, and suggest a better arrangement. But rearranging the shelves requires an approved checklist. The checklist is checked again just before each book moves.

## What the diagram teaches

![A selected folder produces an inventory, then a proposed plan. Approval does not bypass execution checks. Verification and a journal support understandable results and recovery.](assets/journey.svg)

### 1. You choose the shelf

Maya chooses a sandbox folder. The application records a root identifier, such as ROOT-DEMO, and a policy saying which actions are allowed. Other components use that identifier rather than accepting a new unrestricted path every time. This is like giving someone a key to one cupboard rather than the entire building.

### 2. The explorer makes a catalog

An inventory lists the files the application is allowed to inspect. Each record has a file identifier, a location relative to the selected root, a size, and a revision fingerprint. A hash is one part of that fingerprint: changing file bytes normally changes the hash. The catalog is a dated observation, not a permanent guarantee.

### 3. Search finds evidence

Maya asks, “Which notes belong to the hospital project?” The finder searches only permitted, indexed content. It might return a paragraph mentioning discharge permissions. If the text is insufficient, it says so. It cannot make a reliable classification merely because a filename sounds medical.

### 4. The planner proposes an arrangement

The planner suggests a destination from an allowed list and explains why. It may use a model or simple rules. Either way, its output is data to validate. A model can suggest something, but cannot grant itself additional privileges.

### 5. You approve an exact checklist

The workspace shows each source, destination, explanation, and warning. Maya selects two moves and leaves a third unchanged. The server creates a new plan revision containing exactly those two operations. Her approval belongs to that revision, not to every future interpretation of “organize my files.”

### 6. The engine checks and acts

The engine verifies the approval and current filesystem conditions. If another program edited the source, it reports “File changed since preview.” If the destination exists, it reports a collision. It never silently overwrites the destination or picks a new name after approval.

### 7. The journal makes recovery possible

Imagine the move succeeds but the application loses power before updating its status. On restart, the journal says the operation was attempted. The engine checks where the file actually is and compares its identity and content. If the evidence is ambiguous, it asks for review rather than guessing. A journal is therefore an account of intent and observations, not magic protection against every disk failure.

## Technology legend

| Term | Plain-English meaning | Where it fits |
|---|---|---|
| Python | The language used for the first local engine | Explorer, rules, retrieval, journal, operations |
| MCP | A standard way for an assistant to discover and call tools | Read bounded file inventories and document previews |
| RAG | Find relevant evidence before composing an answer | Document Finder; it is not model training |
| A2A | A protocol for one agent to request work from another | Optional classifier/planner separation |
| LLM | A language model that interprets text | Optional explanations and proposed categories |
| Embedding | A numerical representation useful for similarity search | Optional local semantic retrieval |
| Chunk | A small passage cut from a document | Retrieved with its source and revision |
| Keyword search | Search using matching words | A useful first implementation without embeddings |
| SQLite | A small database stored locally | Inventory metadata, plans, approvals, journal |
| SHA-256 | A content fingerprint algorithm | Identify candidate byte-identical files and changed bytes |
| JSON Schema | A precise description of allowed data fields | Validate tool inputs and plan outputs |
| Pydantic | Python data-validation tooling | A possible implementation of typed contracts |
| FastAPI | A Python web API framework | Optional local browser-facing adapter |
| React | Components for an interactive interface | File rows, plan review, status panels |
| Next.js | A framework around React | Local workspace or separate synthetic hosted demo |
| TypeScript | JavaScript with static type checking | Interface code and an alternative local engine |
| Vercel | Hosting for the website and synthetic demonstration | Not direct access to a personal drive |
| Authentication | Establishing which caller is making a request | Local session or approved client identity |
| Authorization | Deciding what that caller may do | Root grants, read permissions, approval permissions |
| Idempotency key | A stable label for one logical request | Repeated submission returns the existing job |
| Journal | A durable record of intent and observed outcomes | Crash recovery and operation history |
| Reconciliation | Compare recorded state with reality | Determine what happened after an interruption |
| Junction / symbolic link | A filesystem entry that redirects somewhere else | A root-boundary hazard, rejected in the initial design |
| Dry run | Produce and validate a proposal without executing it | Preview stage |
| Compensation | A new action intended to reverse an earlier action | Conditional undo, not a guaranteed rewind |
| Observability | Enough safe signals to understand operation health | Counts, timings, error categories, job states |

Not every entry must be installed on day one. Start with Python, its standard library, tests, and SQLite. Add protocols and UI adapters after the rules are independently testable. Choosing a library does not replace understanding its responsibility.

## Why MCP, RAG, and A2A are different

MCP answers “What bounded tool can I call?” RAG answers “What evidence supports this answer?” A2A answers “Which specialist can perform this separate task?” None answers “Did Maya approve moving this exact file?” That is your application's authorization and workflow responsibility.

The protocol documentation describes [MCP transports and local HTTP protections](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports) and [A2A task lifecycles](https://a2a-protocol.org/dev/topics/life-of-a-task/). Pin the protocol and SDK versions when implementing; these links are references, not an instruction to adopt a development specification automatically.

## How to present it

Walk through one file, not the entire technology list. Describe what each component knows about that file, what it is allowed to do, and what evidence it passes on. Then introduce the acronym for the responsibility the audience already understands.
