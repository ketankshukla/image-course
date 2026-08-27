# Build HarborCare by Hand

## From an empty folder to a deployed synthetic demonstration

This series is a construction workbook, not a claim that the application already exists. Build the Python reference first, then add its web interface. The TypeScript architecture is an alternative implementation, not a second system that must be running alongside Python.

![The workspace, evidence services, specialist agents, and disclosure service have separate responsibilities.](../assets/03-system-map.svg)

## Your route through the work

| Order | Workbook | Finished checkpoint |
|---|---|---|
| 1 | [Foundations](01-FOUNDATIONS.html) · [Markdown](01-FOUNDATIONS.md) | Synthetic fixtures and a tested permission rule |
| 2 | [P1: MCP tools](02-MCP-TOOLS.html) · [Markdown](02-MCP-TOOLS.md) | A tool returns only an authorized projection |
| 3 | [P2: Permission-aware RAG](03-PERMISSION-AWARE-RAG.html) · [Markdown](03-PERMISSION-AWARE-RAG.md) | Evidence is filtered before the model sees it |
| 4 | [P3: A2A coordination](04-A2A-COORDINATION.html) · [Markdown](04-A2A-COORDINATION.md) | Specialists exchange narrowly scoped tasks |
| 5 | [P4: Disclosure workflow](05-DISCLOSURE-WORKFLOW.html) · [Markdown](05-DISCLOSURE-WORKFLOW.md) | Approval, revocation and uncertain delivery are tested |
| 6 | [P5: Privacy workspace](06-PRIVACY-WORKSPACE.html) · [Markdown](06-PRIVACY-WORKSPACE.md) | A reviewer understands and controls the exact disclosure |
| 7 | [Production-demo operations](07-PRODUCTION-DEMO.html) · [Markdown](07-PRODUCTION-DEMO.md) | Isolated environments, deployment and recovery evidence |

## What “by hand” means here

Start with small ordinary functions and tests. Only add protocol servers, model calls, storage, and deployment after those functions behave correctly. Each chapter names the files to create, the functions they own, what calls them, and the tests that must pass before moving on. The small executable exercise in the foundations chapter teaches one rule; it does not implement the whole platform.

For each file, write a one-sentence responsibility before writing code. For each function, name its inputs, output, failure result, and permitted side effects. For every successful test, write at least one corresponding denial test. This is how you learn to build the system rather than merely reproduce a folder tree.

The workbook begins with small learning modules. The architecture documents show the eventual service layout: move these tested functions into those service packages as the application grows, rather than maintaining duplicate policy implementations. Likewise, the workbook's `cases/[id]` page and the architecture's `requests/[requestId]` page are alternative route names for the same reviewer view; choose one convention when building the application.

## Keep the promises realistic

The workbooks give detailed implementation recipes, not thousands of lines of finished application code. Later SDK adapters require the current official documentation and pinned versions when you implement them. Complete each acceptance gate before calling that project implemented. A green unit test does not prove a network protocol works; a working protocol does not prove privacy is correct.

Use only synthetic information. Keep the receiver local or in an isolated test environment. There is no emergency override, real hospital connector, insurer integration, or patient upload feature in the first release. Do not convert a teaching demo into a real-data service by changing an environment variable.

## Your learning notebook

For every chapter, save the command you ran, the expected result, the actual result, and one failure you deliberately introduced. Keep screenshots free of private data and access tokens. The strongest final demonstration is not just a successful pickup packet: it is showing that the wrong agency, wrong patient, stale approval, and repeated delivery attempts are handled safely.

Return to the [case-study collection](../00-START-HERE.html) for strategy, policy and architecture explanations.
