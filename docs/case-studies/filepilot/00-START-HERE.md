# FilePilot — Your Personal File Operations Assistant

## At a glance

FilePilot is a proposed local-first application that helps you understand and organize files without handing a language model unrestricted control of your computer. It combines a file explorer, document search, an organization planner, a controlled operations engine, and a review workspace.

This collection is a design and manual-build curriculum, not an installed file-management application. Its examples use fictional documents in a disposable sandbox. No real folder has been scanned, reorganized, or connected to an external model by creating these guides.

## What the diagram teaches

![FilePilot moves from a selected sandbox through inventory and evidence, a proposed plan, human approval, checked execution, and verification. A separate local journal supports recovery.](assets/journey.svg)

Suppose Maya is studying agent engineering. Her practice folder contains downloaded notes, invoice examples, screenshots, and several versions of a project proposal. She asks, “Put the project material together and show me which files are duplicates.”

A weak implementation turns that sentence directly into file operations. FilePilot first asks a much more concrete question: which folder did Maya authorize, and which kinds of actions are permitted? An instruction to organize one folder is not authorization to inspect her entire drive.

The inventory is a snapshot of what exists. It is not a promise that those files will remain unchanged. Document search supplies evidence about content. The planner turns that evidence into suggestions, but neither search nor planning can move a file. This makes it possible to inspect the reasoning without risking the originals.

Maya then sees a precise proposal: move two notes into “Agent Study,” leave an uncertain screenshot alone, and move an extra byte-identical example into “Review Duplicates.” That review folder is not a recycle bin. Nothing is permanently deleted. A duplicate can still matter because a project refers to its current location.

Approval binds to this exact plan revision. If someone edits a source file or creates a destination with the same name afterward, the engine stops the affected operation. It does not reinterpret Maya's original request as permission to improvise.

Finally, the engine checks the result and records it. If the program crashes after moving a file but before recording completion, restarting means reconciling the actual filesystem with the journal—not blindly trying the same move again. The diagram therefore ends with evidence, not with an optimistic success message.

> **Key idea:** A clever proposal and permission to execute it are two different things. Keeping them separate makes the assistant useful without making it the security boundary.

## The five projects

| Project | What you demonstrate | What it cannot do |
|---|---|---|
| P1 File Explorer | Inspect a selected root and discover bounded MCP tools | Browse arbitrary drives |
| P2 Document Finder | Answer questions from permitted document passages | Treat retrieved text as instructions |
| P3 Organization Planner | Produce an explainable, validated proposal | Approve or execute its own proposal |
| P4 Safe Operations Engine | Execute approved same-volume moves and reconcile failures | Overwrite or permanently delete files |
| P5 File Workspace | Review changes and understand outcomes | Grant permissions merely by hiding UI buttons |

## Choose your reading route

Begin with [the project strategy](01-PROJECT-STRATEGY.html) and [the plain-English flow and technology legend](02-PLAIN-ENGLISH-AND-LEGEND.html). Read [safety rules](03-SAFETY-POLICY-AND-TESTS.html) before implementing writes.

The [Python architecture](04-PYTHON-ARCHITECTURE.html) is the reference design. The [hybrid architecture](05-HYBRID-ARCHITECTURE.html) adds a local Next.js interface. The [TypeScript counterpart](06-TYPESCRIPT-ARCHITECTURE.html) is an alternative implementation, not another writer sharing the same state. [Repository and deployment guidance](07-REPOSITORIES-AND-DEPLOYMENT.html) explains what stays local.

Start constructing the application with the [manual-build series](manual-build/00-START-HERE.html). Each workbook identifies the files, functions, data contracts, tests, and acceptance gate for its stage. Only the explicitly labelled foundation exercise is a complete runnable example; later stages are implementation workbooks, not a claim that a production application already exists.

## How to present it

Show a small before-and-after folder tree beside the approval screen. First demonstrate a successful move, then demonstrate the more important case: change a file after approval and show the engine refuse to proceed. Finish with recovery after an injected crash. Explain the distinction between “proposed,” “approved,” “attempted,” and “verified.” Those four words tell a stronger engineering story than “AI cleaned my Downloads.”
