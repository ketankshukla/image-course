# Five Layers of AI Engineering — Build EvidenceDesk

## At a glance

This is a hands-on course about **prompt, context, harness, loop, and graph engineering**. You will learn what each layer does, why it fails, how to implement it, and how to demonstrate that it works. Our single capstone is EvidenceDesk: a Next.js/React interface with a Python backend that turns a small evidence collection into a reviewable decision brief.

> **Key idea:** You do not need five different projects. Build one understandable system, then give it five increasingly capable layers.

This package contains teaching chapters, architecture, a manual construction workbook, production and evaluation guidance, a transcript assessment, and a small executable Python exercise. It does **not** claim that the complete production application already exists. The web application described here is your build project; the Python exercise is a deliberately limited local demonstration.

## What the diagram teaches

![Five engineering responsibilities, from instructions to coordinated work](assets/five-layers.svg)

Imagine asking a research assistant: “Which document-search product should our small support team trial?” A clever assistant can still fail if the assignment is vague, the pricing sheet is obsolete, their account can read another team's confidential files, a retry repeats an action, or the final report arrives before the cost analysis finishes.

The five layers address these different problems. Prompt engineering defines the assignment. Context engineering supplies the right evidence. Harness engineering provides controlled tools and records. Loop engineering decides whether work should continue. Graph engineering arranges dependencies between pieces of work. None makes the others obsolete.

The diagram is a responsibility map, not a historical timeline or a requirement to buy five products. One Python program can implement all five. Some tasks only need a prompt and a deterministic validator. We add complexity only when a test exposes a need.

## The real-life-style case study

Our fictional company, Northstar Support, has twelve support specialists. Its manager wants to choose between two fictional knowledge-search services, Cedar and Birch. The evidence packet includes product descriptions, a current price sheet, an older price sheet, an internal requirements note, and a deliberately restricted document belonging to another team.

The manager asks: “For twelve people, compare annual cost, SSO support and export capability. Stay within our stated requirements. Show evidence for each conclusion. Do not purchase anything.”

The word “fictional” matters: the prices and capabilities are learning fixtures, not market research. The project must say when evidence is missing. “No document proves this” is different from “the product does not support this.”

A successful brief includes a comparison, source excerpts, explicit unknowns, and a reasoned recommendation that a human can approve. A rejected brief is also a successful demonstration if the system correctly notices unsupported claims and prevents publication.

## Your learning route

| Chapter | Question you will answer | Artifact you produce |
|---|---|---|
| [Prompt engineering](01-PROMPT-ENGINEERING.md) | What exactly should the model do? | Versioned assignment and output contract |
| [Context engineering](02-CONTEXT-ENGINEERING.md) | What information should it see? | Authorized evidence packet |
| [Harness engineering](03-HARNESS-ENGINEERING.md) | What may it do, and what is recorded? | Tool gateway and run ledger |
| [Loop engineering](04-LOOP-ENGINEERING.md) | When should it retry, pause or stop? | Bounded state machine |
| [Graph engineering](05-GRAPH-ENGINEERING.md) | What depends on what? | Research, merge and review graph |
| [Architecture](06-PROJECT-ARCHITECTURE.md) | How do the frontend and backend connect? | Repository, contracts and deployment map |
| [Manual build](07-MANUAL-BUILD.md) | What do I write first? | Incremental construction workbook |
| [Evaluation and production](08-EVALUATION-AND-PRODUCTION.md) | What evidence permits release? | Failure tests and release gates |
| [Transcript assessment](09-TRANSCRIPT-ASSESSMENT.md) | Which claims need qualification? | A grounded mental model |
| [Practice lab](10-PRACTICE-LAB.md) | Can I trace the rules without an AI account? | Executable Python experiment |

Read the five concepts in order, then build. Alternatively, read the architecture after chapter one if seeing the whole system helps you learn. Every chapter contains an exercise and an explanation you can compare with your own answer.

## What you need before starting

You should be able to read a Python function, a JavaScript object and a basic React component. If these feel unfamiliar, begin by changing one variable and predicting the output in the practice lab. You do not need to understand distributed systems or vector databases before the first lesson.

For the full build, use Git, Node.js, a supported Python release, an editor and two local terminals. The early stages need no paid AI API. Start with fixtures and a fake model so mistakes are understandable and repeatable. Introduce a real model only after your contracts work.

A useful rhythm is one concept session followed by one build session. Stop when you can explain your code rather than when you have copied the whole page. No lesson requires a completion counter or score.

## A small legend before the big words

A **model** predicts an output from supplied input. An **agent** is an application that lets a model help choose actions. A **workflow** is a sequence whose rules you define. **State** is what the application currently knows about a run. A **contract** is the agreed shape and meaning of information crossing a boundary.

**RAG** means retrieving evidence before generating an answer. **MCP** is an optional protocol for exposing tools to model-connected applications. **A2A** is an optional protocol for cooperation between independently operated agents. You do not need MCP or A2A merely because your application contains multiple Python functions. See the architecture for where optional adapters belong.

## What a convincing demonstration looks like

First run a normal comparison. Then remove the current price sheet and show an honest unknown. Try an unauthorized document and show that retrieval excludes it before model input. Simulate a timeout and show a bounded retry. Finally restart a worker and show that an approved result is not published twice.

These demonstrations reveal your engineering judgment. “It generated a nice paragraph” demonstrates much less.

## How to present this course

Say: “I built a system that knows what to ask, what evidence to use, which actions are permitted, when to stop, and which tasks must finish before others start.” Then show one failure and its protective behavior. Explain the code boundary responsible for that behavior. That is a stronger story than listing frameworks.
