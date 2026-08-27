# Build FilePilot Manually — Start Here

## At a glance

This series teaches how to construct the proposed application from an empty repository. It is a sequence of implementation workbooks: each one identifies files, functions, inputs, outputs, tests, and a completion gate. The foundation lesson contains a complete executable exercise. Later chapters deliberately require implementation work; they are not a ready-made production codebase.

## What the diagram teaches

![The build follows a selected sandbox, read-only observations, a proposed plan, explicit approval, checked execution, and verified outcomes.](../assets/journey.svg)

Start by making the rules work without an assistant. If the only way to test “an expired approval must fail” is to persuade a chatbot to generate an expired approval, your design is too entangled. A pure function can check that rule directly and reproducibly.

Next add observations. The explorer reads a synthetic folder, creates stable IDs, and reports unsupported entries. It does not move anything. Then build one tiny operation end to end: a previewed, approved move between two already existing sandbox folders. This establishes the safety loop before you add semantic retrieval or agent coordination.

The finder and planner make the system more useful, not more authoritative. The UI makes it understandable. Protocol adapters make it interoperable. None should weaken the rules established in the first exercise.

## Reading and construction order

| Workbook | Main skill | What you should have at the end |
|---|---|---|
| [Foundations](01-FOUNDATIONS.html) | Pure contracts and tests | A tested approval-bound plan |
| [MCP explorer](02-MCP-EXPLORER.html) | Bounded reads and tool contracts | Read-only inventory through a real adapter |
| [Document RAG](03-DOCUMENT-RAG.html) | Evidence and permissions | Search results with current source revisions |
| [Planner and A2A](04-PLANNER-AND-A2A.html) | Structured proposals and delegation | Validated suggestions with no write privilege |
| [Safe operations](05-SAFE-OPERATIONS.html) | Journal, execution, recovery | One approved move and tested crash reconciliation |
| [File workspace](06-FILE-WORKSPACE.html) | Human review and clear state | Understandable approval and history screens |
| [Production demo](07-PRODUCTION-DEMO.html) | Packaging, evidence, release | A reproducible restricted demonstration |

Read the series in order, but implement the smallest operations slice immediately after the explorer. Return to RAG and A2A when the non-AI workflow is reliable. This keeps the build useful even before a model is connected.

## Your development loop

For each function, write down an input example, an expected result, and a denial example. Implement the smallest behavior. Run the tests. Then call it through the adapter and verify the same result. Commit a small, understood change rather than assembling a large opaque application at once.

Use fresh temporary fixture directories for tests. Never point the tests at Downloads, the home directory, the learning-library checkout, or an existing application-data folder. Teardown should remove only the exact temporary directory created by that test, after verifying its location and marker. No broad cleanup command belongs in a beginner exercise.

## What to record as you learn

Maintain an implementation notebook with supported operations, schema versions, test commands, known limitations, and measured outcomes. Write down why an operation is unsupported. “We cannot yet guarantee no-overwrite semantics on this platform” is useful engineering information; silently falling back to a different operation is not.

Capture only synthetic screenshots. A screenshot of a real filename list can leak private information even when file contents are not shown. Keep fixture labels obviously fictional so the public demo cannot be mistaken for a personal-data integration.

## How to present your progress

After each stage, explain one function in plain English: “It receives these inputs, checks these rules, and either returns this result or this explicit refusal.” If you cannot explain the difference between a tool's result and its authority, stop and simplify the boundary before adding another framework.
