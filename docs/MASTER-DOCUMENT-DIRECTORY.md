# Master Document Directory

Your blue-and-white map of the learning workspace: what each document explains, when to use it, and where to find it.

## At a glance

357 documents: 244 individual course lessons and 113 guides, planning documents and maintenance references. Matching HTML and Markdown files count as one document.

Coverage: all Markdown documents under docs and courses; HTML reading editions paired with their Markdown sources; standalone HTML templates and Word/PDF files under docs; root README and AGENTS instructions. Course export bundles, images, code, JSON configuration and generated website files are not individual catalogue entries. This directory is local-only because it also links unpublished authoring notes. It does not publish those notes to the website.

## Choose your route

- New to the workspace: start with the folder guide and the plain-English case-study explanations.
- Ready to build: choose a case study, read its architecture, then follow its manual-build series.
- Learning one concept: browse the numbered course sections below.
- Maintaining content: use publishing instructions, templates and verification references.

Locations below are relative to the image-course repository root. Links are relative to this document, so moving the entire repository preserves navigation. Historical roadmaps and verification notes are not claims about current implementation or deployment.

## Directory sections

- [Start here — workspace guides](#orientation) — 5 documents
- [Hands-on engineering workshops](#training) — 18 documents
- [Acme — business operations](#acme) — 15 documents
- [HarborCare — privacy-first coordination](#hospital) — 16 documents
- [FilePilot — safe file automation](#filepilot) — 16 documents
- [Planning & reading-style references](#planning) — 4 documents
- [Authoring & verification references](#maintenance) — 10 documents
- [Visual Course Volume 1 — MCP, ACP, A2A and RAG](#course-01) — 30 documents
- [Visual Course Volume 2 — Build Your First Agent System](#course-02) — 16 documents
- [Visual Course Volume 3 — Production Agent Systems](#course-03) — 30 documents
- [Visual Course Volume 4 — Protocol Engineering and Interoperability](#course-04) — 24 documents
- [Visual Course Volume 5 — Knowledge Systems and Advanced RAG](#course-05) — 24 documents
- [Visual Course Volume 6 — Durable Orchestration and Multi-Agent Workflows](#course-06) — 24 documents
- [Visual Course Volume 7 — Agent Identity, Security, and Governance](#course-07) — 24 documents
- [Visual Course Volume 8 — Evaluation, Observability, and AgentOps](#course-08) — 24 documents
- [Visual Course Volume 9 — Agentic Product Design and Human Control](#course-09) — 24 documents
- [Visual Course Volume 10 — Enterprise Architecture and Dual-Stack Project Blueprint](#course-10) — 24 documents
- [Course authoring & maintenance notes](#course-support) — 29 documents

<a id="orientation"></a>

## Start here — workspace guides

Understand the repository and how documents become website articles.

### Master Document Directory

The searchable local map of reading guides, course lessons, planning files and authoring references. Markdown/HTML pairs are grouped as one document.

**Use it for:** Find the document you need, see where it lives, and choose its reading or source edition.

**Location:** `docs/MASTER-DOCUMENT-DIRECTORY.md`

**Availability:** Local directory — not published

[Read HTML](MASTER-DOCUMENT-DIRECTORY.html) · [Markdown source](MASTER-DOCUMENT-DIRECTORY.md)

### Your Organized Learning Workspace

The course website remains one Git repository. Its ten course collections live together under courses. All case-study documents live under docs/case-studies, separated into Acme, HarborCare, and FilePilot. These are teaching collections; adding them does not install or deploy their proposed applications.

**Use it for:** Locate folders and understand which files belong together.

**Location:** `docs/FOLDER-STRUCTURE.md`

**Availability:** Published in website

[Read HTML](FOLDER-STRUCTURE.html) · [Markdown source](FOLDER-STRUCTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=1)

**Inside:** 1. Start reading here · 2. The ten folders are courses, not ten application repositories · 3. What moved

### Publishing a New Case Study

The website has three shelves: Courses for the ten visual volumes, Case Studies for Acme, HarborCare and FilePilot, and Library Guides for workspace and publishing instructions. Each case study has its own reading order, reference sections and build workbooks. Search covers all published articles.

**Use it for:** Add a case study to the website safely and verify its publication.

**Location:** `docs/PUBLISHING-CASE-STUDIES.md`

**Availability:** Published in website

[Read HTML](PUBLISHING-CASE-STUDIES.html) · [Markdown source](PUBLISHING-CASE-STUDIES.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=2)

**Inside:** One source collection, two reading formats · 1. Create the case-study folder · 2. Declare what to publish

### 🎨 Visual Agent Course

A Next.js 15 + TypeScript + Tailwind CSS learning platform for the Visual Agent Course — a complete, diagram-first curriculum covering agentic product design, protocols, RAG, multi-agent workflows, security, and production deployment.

**Use it for:** Find the project overview and normal development commands.

**Location:** `README.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../README.md)

**Inside:** 🚀 What is this? · 🏗️ Architecture · 🛠️ Local Development

### Agent Notes

This is a Next.js 15 + TypeScript + Tailwind CSS learning library. Source courses live in courses/Visual Course NN. Case studies live in docs/case-studies/; each published study has a collection.json allowlist. The authoritative Node build is scripts/buildlibrary.mjs. See docs/PUBLISHING-CASE-STUDIES.md and docs/FOLDER-STRUCTURE.md.

**Use it for:** Maintain the repository while preserving its content, build and publication rules.

**Location:** `AGENTS.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../AGENTS.md)

**Inside:** Course Website · Key commands · Content structure

<a id="training"></a>

## Hands-on engineering workshops

Practice team workflows, acceptance testing, GitHub Actions, staging and controlled releases.

### Accessible and Resilient Interfaces

This workshop teaches you to design a page for people using keyboards, assistive technology, slow connections, and imperfect workflows. The supplied one-page approval simulator demonstrates clear labels, visible focus, pending state, a recoverable failure, and prevention of repeated submission within that page session. It performs no real file operation or network request.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/accessibility/ACCESSIBLE-AND-RESILIENT-INTERFACES.md`

**Availability:** Published in website

[Read HTML](training/accessibility/ACCESSIBLE-AND-RESILIENT-INTERFACES.html) · [Markdown source](training/accessibility/ACCESSIBLE-AND-RESILIENT-INTERFACES.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=15)

**Inside:** Lesson 1 — Design the state, not just the happy screenshot · Lesson 2 — Use controls with built-in meaning · Lesson 3 — Make failure recoverable

### Background Jobs and Reliable Workflows

This workshop teaches you to reason about work that outlives a single web request. You will distinguish accepting a job from completing it, simulate a crash, retry safely within a database boundary, and explain why duplicate delivery is normal. The runnable Python/SQLite model has no external side effects and uses an in-memory database.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/background-jobs/BACKGROUND-JOBS-AND-RELIABLE-WORKFLOWS.md`

**Availability:** Published in website

[Read HTML](training/background-jobs/BACKGROUND-JOBS-AND-RELIABLE-WORKFLOWS.html) · [Markdown source](training/background-jobs/BACKGROUND-JOBS-AND-RELIABLE-WORKFLOWS.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=11)

**Inside:** Lesson 1 — Separate the request from the work · Lesson 2 — Expect duplicate delivery · Lesson 3 — Read the transaction boundary

### From Solo Pushes to Confident Team Releases

This is a hands-on CI/CD course for someone who can build a project but has not recently worked with a team's release process. You will practice with a tiny Learning Library website, deliberately break a feature without breaking compilation, watch a test reject it, introduce pull-request protection, and release through staging and an approval gate. The destination is not a complicated pipeline.…

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/ci-cd/CI-CD-FROM-SOLO-TO-TEAM.md`

**Availability:** Published in website

[Read HTML](training/ci-cd/CI-CD-FROM-SOLO-TO-TEAM.html) · [Markdown source](training/ci-cd/CI-CD-FROM-SOLO-TO-TEAM.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=3)

**Inside:** Lesson 1 — Understand the journey before the commands · Two different meanings of staging · Your team, even if you are practicing alone

### Reading and Taking Over an Unfamiliar Codebase

This workshop teaches you to enter a project without trying to understand every file before making a useful contribution. You will identify an entry point, trace one feature through a service to its data, establish a passing baseline, and plan a small change with a clear regression test. A tiny Python repository provides a safe first rehearsal.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/codebase/READING-AN-UNFAMILIAR-CODEBASE.md`

**Availability:** Published in website

[Read HTML](training/codebase/READING-AN-UNFAMILIAR-CODEBASE.html) · [Markdown source](training/codebase/READING-AN-UNFAMILIAR-CODEBASE.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=17)

**Inside:** Lesson 1 — Start with the purpose and operating instructions · Lesson 2 — Find the entry point · Lesson 3 — Follow data, not just names

### Coding with Confidence: Become the Builder, Not Just the Typist

A practical course outline for returning to software development with AI beside you—not in place of your understanding.

**Use it for:** Plan a gradual return to coding through 12 core modules, 3 optional AI extensions, and a safe FilePilot Mini project.

**Location:** `docs/training/coding-confidence/CODING-WITH-CONFIDENCE.md`

**Availability:** Published in website

[Read HTML](training/coding-confidence/CODING-WITH-CONFIDENCE.html) · [Markdown source](training/coding-confidence/CODING-WITH-CONFIDENCE.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=19)

**Inside:** What the video gives us—and what we change · The new working agreement · Build understanding in layers

### Is Learning to Code Still Worth It? A Careful Look at the Video

My assessment: keep the encouragement, strengthen the evidence, and do not abandon the fundamentals. The transcript offers a useful way to approach AI-assisted development: understand an existing system, specify a change, inspect the implementation, and test the outcome. It does not establish that technical specialties, degrees, or manual coding have become obsolete.

**Use it for:** Separate the supplied coding video's useful advice from factual errors, uncertain predictions, and unsupported generalizations.

**Location:** `docs/training/coding-confidence/VIDEO-FACT-CHECK.md`

**Availability:** Published in website

[Read HTML](training/coding-confidence/VIDEO-FACT-CHECK.html) · [Markdown source](training/coding-confidence/VIDEO-FACT-CHECK.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=20)

**Inside:** What is genuinely valuable here? · Claim-by-claim assessment · 1. 0:00–0:26 — Leading AI figures say coding may disappear

### Configuration and Environments — Know What You Are Running

This workshop teaches you to separate code from deployment settings and to reject dangerous configuration before serving requests. The lab parses synthetic settings for development, staging, and production. It catches a misspelled environment, an invalid boolean, and unsafe production combinations without reading your real environment or contacting a service.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/configuration/CONFIGURATION-AND-ENVIRONMENTS.md`

**Availability:** Published in website

[Read HTML](training/configuration/CONFIGURATION-AND-ENVIRONMENTS.html) · [Markdown source](training/configuration/CONFIGURATION-AND-ENVIRONMENTS.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=10)

**Inside:** Lesson 1 — Same source does not mean same behavior · Lesson 2 — Parse strings into meaning · Lesson 3 — Validate combinations, not only fields

### Databases and Safe Schema Changes

This workshop teaches you to change stored data without assuming that a new application build can magically repair an old database. You will model lessons and progress, enforce relationships, add a compatible column, backfill existing data, observe transaction rollback, and restore a backup. The runnable exercise uses Python's built-in SQLite support and keeps every database in memory.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/databases/DATABASES-AND-SAFE-MIGRATIONS.md`

**Availability:** Published in website

[Read HTML](training/databases/DATABASES-AND-SAFE-MIGRATIONS.html) · [Markdown source](training/databases/DATABASES-AND-SAFE-MIGRATIONS.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=8)

**Inside:** Lesson 1 — Model facts, not screens · Lesson 2 — Read and run the schema · Lesson 3 — Expand before you contract

### Debugging Without Guessing

This eight-lesson workshop teaches you to investigate broken software calmly and systematically. You will run a small Learning Library app, reproduce two bugs, inspect an HTTP request, pause server execution, compare actual values with expected values, and write evidence that your fixes work. It follows naturally from the CI/CD workshop: that course taught you how to stop a bad change; this one…

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/debugging/DEBUGGING-WITHOUT-GUESSING.md`

**Availability:** Published in website

[Read HTML](training/debugging/DEBUGGING-WITHOUT-GUESSING.html) · [Markdown source](training/debugging/DEBUGGING-WITHOUT-GUESSING.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=4)

**Inside:** Lesson 1 — Think like an investigator · Keep a debugging notebook · Lesson 2 — Run the app and reproduce the failure

### Docker and Reproducible Local Environments

This workshop teaches you what an image, container, port mapping, and volume actually do. You will package a tiny Python health service, run it through an explicitly local host port, inspect its logs, and understand which changes survive container removal. The supplied service has no database or secrets.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/docker/DOCKER-AND-LOCAL-ENVIRONMENTS.md`

**Availability:** Published in website

[Read HTML](training/docker/DOCKER-AND-LOCAL-ENVIRONMENTS.html) · [Markdown source](training/docker/DOCKER-AND-LOCAL-ENVIRONMENTS.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=13)

**Inside:** Lesson 1 — Separate the recipe from the running process · Lesson 2 — Read the Dockerfile line by line · Lesson 3 — Build and run manually

### Git Collaboration and Code Review

This workshop teaches you to work on shared history without treating every disagreement as an emergency. You will create a branch, make focused commits, reproduce a real merge conflict, preserve both contributors' requirements, and undo a bad change using a new commit. A disposable local Git lab verifies the mechanics without pushing anything to GitHub or changing your real repository.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/git-team/GIT-COLLABORATION-AND-REVIEW.md`

**Availability:** Published in website

[Read HTML](training/git-team/GIT-COLLABORATION-AND-REVIEW.html) · [Markdown source](training/git-team/GIT-COLLABORATION-AND-REVIEW.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=7)

**Inside:** Lesson 1 — Understand the shared record · Lesson 2 — Rehearse a conflict safely · Lesson 3 — Resolve meaning, not just markers

### HTTP and API Development — Conversations Between Programs

This workshop teaches you to read, design, and test the conversations between a frontend and a backend. You will start a local lesson-catalogue API, make requests manually, create a record, deliberately send invalid requests, and explain why the server responds differently in each case. The aim is to understand the exchange, not memorize a list of status codes.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/http-api/HTTP-AND-API-DEVELOPMENT.md`

**Availability:** Published in website

[Read HTML](training/http-api/HTTP-AND-API-DEVELOPMENT.html) · [Markdown source](training/http-api/HTTP-AND-API-DEVELOPMENT.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=6)

**Inside:** Lesson 1 — Read the conversation · Lesson 2 — Run it and inspect a response · Lesson 3 — Create something and understand validation

### Authentication, Authorization, and Secrets

This workshop separates three ideas often blurred together: proving who a caller is, deciding what that caller may do, and protecting credentials used by software. A synthetic HarborCare scenario shows why a signed-in transport coordinator must not receive clinical notes merely because the API knows their identity.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/identity/AUTHENTICATION-AUTHORIZATION-AND-SECRETS.md`

**Availability:** Published in website

[Read HTML](training/identity/AUTHENTICATION-AUTHORIZATION-AND-SECRETS.html) · [Markdown source](training/identity/AUTHENTICATION-AUTHORIZATION-AND-SECRETS.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=9)

**Inside:** Lesson 1 — Knowing a name is not granting access · Lesson 2 — Run the permission matrix · Lesson 3 — Allowlist fields and deny by default

### Logging, Monitoring, and Incident Response

This workshop teaches you to answer “What happened?” without collecting every private detail or guessing from a generic error screen. You will connect synthetic events across a web layer and API, distinguish event logs from aggregate measurements, and rehearse an incident response that prioritizes restoring service while preserving evidence.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/observability/LOGGING-MONITORING-AND-INCIDENTS.md`

**Availability:** Published in website

[Read HTML](training/observability/LOGGING-MONITORING-AND-INCIDENTS.html) · [Markdown source](training/observability/LOGGING-MONITORING-AND-INCIDENTS.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=12)

**Inside:** Lesson 1 — Ask a question before collecting data · Lesson 2 — Follow a request without exposing its contents · Lesson 3 — Count the right thing

### Performance Investigation — Measure Before You Optimize

This workshop teaches you to turn “the app feels slow” into a measured, testable question. You will inspect a SQLite query plan, measure a controlled workload, add an index, and verify that the returned data remains the same. The script prints the timings observed on your machine; the course does not invent a speedup or require one fixed ratio.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/performance/PERFORMANCE-INVESTIGATION.md`

**Availability:** Published in website

[Read HTML](training/performance/PERFORMANCE-INVESTIGATION.html) · [Markdown source](training/performance/PERFORMANCE-INVESTIGATION.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=16)

**Inside:** Lesson 1 — Define the symptom and workload · Lesson 2 — Inspect the execution plan · Lesson 3 — Measure without pretending to eliminate noise

### Software Design and Refactoring Without Breaking Behavior

This workshop teaches you to improve code structure while preserving the behavior people already rely on. You will identify responsibilities in a small lesson-card function, capture current behavior with explicit examples, extract focused functions, and compare results before and after. The Python lab has no external dependencies or side effects.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/refactoring/SOFTWARE-DESIGN-AND-REFACTORING.md`

**Availability:** Published in website

[Read HTML](training/refactoring/SOFTWARE-DESIGN-AND-REFACTORING.html) · [Markdown source](training/refactoring/SOFTWARE-DESIGN-AND-REFACTORING.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=14)

**Inside:** Lesson 1 — Distinguish a refactor from a feature change · Lesson 2 — Capture behavior before improving structure · Lesson 3 — Extract responsibilities, not arbitrary lines

### Your Practical Software Engineering Workshops

Start with one workshop, perform its exercise, and keep a short evidence record before moving on. These are separate reading documents, not one enormous course. Each has a blue HTML edition, a Markdown source, and local practice material. Nothing is deployed automatically.

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/START-HERE.md`

**Availability:** Published in website

[Read HTML](training/START-HERE.html) · [Markdown source](training/START-HERE.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=18)

**Inside:** The learning order · How to use each workshop · Understand the verification boundary

### Testing That Catches Real Problems

This eight-lesson workshop teaches you to write tests that protect meaningful behavior rather than merely produce green badges. You will test a miniature FilePilot-style approval service, compare a weak test with stronger assertions, isolate dependencies, check failure paths, and deliberately break corrected code to see whether the suite notices. It connects debugging to CI/CD: discover a…

**Use it for:** Use this reference to understand the subject described below and its place in the collection.

**Location:** `docs/training/testing/TESTING-THAT-CATCHES-REAL-PROBLEMS.md`

**Availability:** Published in website

[Read HTML](training/testing/TESTING-THAT-CATCHES-REAL-PROBLEMS.html) · [Markdown source](training/testing/TESTING-THAT-CATCHES-REAL-PROBLEMS.md) · [Website reader](https://course.ketanshukla.dev/#course=library-guides&chapter=5)

**Inside:** Lesson 1 — Turn a promise into observable evidence · Our deliberately small contract · Lesson 2 — Run the misleading green test

<a id="acme"></a>

## Acme — business operations

A coherent customer-service case: evidence, specialist agents, approvals and controlled actions.

### Acme Agent Platform — Hybrid Architecture

The browser is the reception desk. Next.js is the receptionist's secure connection to the back office. Python is the back office: it investigates, applies rules, remembers unfinished work, and records the outcome.

**Use it for:** Understand the Next.js interface and Python backend boundary.

**Location:** `docs/case-studies/acme/HYBRID-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/HYBRID-ARCHITECTURE.html) · [Markdown source](case-studies/acme/HYBRID-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=4)

**Inside:** Next.js and React on Vercel. Python behind the scenes. · 1. At a glance · 2. What the architecture teaches

### Build It Yourself

This series teaches you how to build the five Acme projects manually. The primary route is Python services followed by a Next.js interface. Each project also explains its TypeScript implementation path. Start with one route; do not maintain two half-finished implementations at once.

**Use it for:** Choose the construction sequence and understand each workbook’s acceptance gate.

**Location:** `docs/case-studies/acme/manual-build/00-START-HERE.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/manual-build/00-START-HERE.html) · [Markdown source](case-studies/acme/manual-build/00-START-HERE.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=7)

**Inside:** Seven workbooks: from an empty folder to a production demo · 1. Your route through the series · 2. The case we will keep using

### Workbook 1 — Start with Nothing

A pure function receives values and returns a value without calling a network or writing a database. Start there because mistakes are easiest to understand when only one thing is happening. A database adapter later saves the result; a web adapter later accepts a request. Those layers should not be mixed into the first function.

**Use it for:** Begin implementation with small contracts, rules, fixtures and executable tests.

**Location:** `docs/case-studies/acme/manual-build/01-FOUNDATIONS.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/manual-build/01-FOUNDATIONS.html) · [Markdown source](case-studies/acme/manual-build/01-FOUNDATIONS.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=8)

**Inside:** Create the workshop before building the machinery · 1. At a glance · 2. Install and verify your tools

### Workbook 2 — Build the MCP Operations Gateway

MCP is the protocol wrapper around a capability. The domain function is the rule behind that capability. We write the rule first so changing the protocol SDK does not change the meaning of a credit.

**Use it for:** Build bounded tool interfaces and test authorization through the protocol adapter.

**Location:** `docs/case-studies/acme/manual-build/02-MCP-GATEWAY.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/manual-build/02-MCP-GATEWAY.html) · [Markdown source](case-studies/acme/manual-build/02-MCP-GATEWAY.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=9)

**Inside:** P1: turn business functions into controlled tools · 1. At a glance · 2. Create files in this order

### Workbook 3 — Build the Evidence RAG Workbench

RAG means retrieval-augmented generation. Retrieval finds useful material; generation explains it. A fluent answer can still be wrong when retrieval selects the wrong policy date, wrong tenant, or an irrelevant paragraph. Therefore build and test retrieval before adding answer generation.

**Use it for:** Build document ingestion, authorized retrieval and evidence-backed answers.

**Location:** `docs/case-studies/acme/manual-build/03-RAG-WORKBENCH.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/manual-build/03-RAG-WORKBENCH.html) · [Markdown source](case-studies/acme/manual-build/03-RAG-WORKBENCH.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=10)

**Inside:** P2: turn documents into traceable, authorized evidence · 1. At a glance · 2. Create the files and data models

### Workbook 4 — Build the A2A Specialist Network

The picture includes a future Risk agent; implement only Policy and Finance first. Workflow owner, coordinator, and aggregation are logical responsibilities, not three extra services you must deploy.

**Use it for:** Build specialist task coordination, artifact handling and failure behavior.

**Location:** `docs/case-studies/acme/manual-build/04-A2A-SPECIALISTS.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/manual-build/04-A2A-SPECIALISTS.html) · [Markdown source](case-studies/acme/manual-build/04-A2A-SPECIALISTS.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=11)

**Inside:** P3: delegate work without giving away business authority · 1. At a glance · 2. Create a shared task contract

### Workbook 5 — Build the Durable Workflow and Reliability Lab

Durability means a process can stop without losing accepted work. It does not mean an action runs exactly once. A durable worker may repeat a step after uncertainty, so the step's external effect must be safe to repeat.

**Use it for:** Implement approval-bound execution, durable records and crash recovery.

**Location:** `docs/case-studies/acme/manual-build/05-DURABLE-WORKFLOW.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/manual-build/05-DURABLE-WORKFLOW.html) · [Markdown source](case-studies/acme/manual-build/05-DURABLE-WORKFLOW.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=12)

**Inside:** P4: remember the work, wait safely, and recover uncertain outcomes · 1. At a glance · 2. Create files in a testable order

### Workbook 6 — Build the Case Resolution Platform

The browser owns interactions, not business truth. The Next.js server loads authorized data and forwards commands. The Python Case API records them. The workflow runs independently and exposes progress through durable read models.

**Use it for:** Build the human-facing review interface and explain authoritative job state.

**Location:** `docs/case-studies/acme/manual-build/06-CASE-PLATFORM.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/manual-build/06-CASE-PLATFORM.html) · [Markdown source](case-studies/acme/manual-build/06-CASE-PLATFORM.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=13)

**Inside:** P5: give a person a clear, safe interface to the system · 1. At a glance · 2. Build the Case API before the screen

### Workbook 7 — From Local Success to a Production Demo

Production is an operating responsibility, not a command that ends development. You must know what is running, which data it uses, how to detect failure, and how to restore service without duplicating business actions.

**Use it for:** Prepare packaging, synthetic demonstrations, operational tests and release evidence.

**Location:** `docs/case-studies/acme/manual-build/07-PRODUCTION.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/manual-build/07-PRODUCTION.html) · [Markdown source](case-studies/acme/manual-build/07-PRODUCTION.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=14)

**Inside:** Release the complete system and learn to operate it · 1. At a glance · 2. Make a release inventory

### Acme Agent Platform

The user-facing layer accepts a request and displays progress. It does not perform a long-running case investigation inside a browser request.

**Use it for:** Trace components, folders, ownership and calls before building the application.

**Location:** `docs/case-studies/acme/PROJECT-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/PROJECT-ARCHITECTURE.html) · [Markdown source](case-studies/acme/PROJECT-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=3)

**Inside:** A visual architecture and Python implementation blueprint · 1. The whole system at a glance · The five project boundaries

### Where the Projects Live

I would not build the applications inside image-course, and I would not put separate Git repositories inside its subfolders.

**Use it for:** Decide what lives in Git, what runs separately and what may be deployed.

**Location:** `docs/case-studies/acme/REPOSITORIES-AND-DEPLOYMENT.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/REPOSITORIES-AND-DEPLOYMENT.html) · [Markdown source](case-studies/acme/REPOSITORIES-AND-DEPLOYMENT.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=6)

**Inside:** A practical guide to folders, Git repositories, and deployment · 1. At a glance · 2. What the diagram teaches

### Response to project-strategy.md

This is a very strong, defensible strategy. It correctly identifies the two common failure modes (244 tiny toy projects vs. one unfinishable monolith) and proposes a portfolio suite that is both deep and modular. The five-project structure, the single Acme case-study spine, and the A/B/C demonstration taxonomy are exactly the right way to turn a 244-diagram course into credible engineering…

**Use it for:** Review commentary on the original project strategy, rather than follow a build workbook.

**Location:** `docs/case-studies/acme/strategy/project-strategy-response.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](case-studies/acme/strategy/project-strategy-response.md)

**Inside:** Bottom line · What I like most · What I would watch out for

### Python Project Strategy for the 244-Diagram Visual Agent Course

Do not build one project per diagram. That would create 244 tiny demonstrations with repeated setup, shallow implementations, and no convincing production story.

**Use it for:** Choose project scope, build order and the evidence a convincing demonstration needs.

**Location:** `docs/case-studies/acme/strategy/PROJECT-STRATEGY.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/strategy/PROJECT-STRATEGY.html) · [Markdown source](case-studies/acme/strategy/PROJECT-STRATEGY.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=1)

**Inside:** Executive recommendation · Why one project per image is the wrong model · Why one giant project is also risky

### The Whole Project in Plain English

You do not need to know how to code to read this guide. Think of the project as a small, well-organized customer-service office. Different people have different jobs, they keep written records, and nobody is allowed to move money just because they sound confident.

**Use it for:** Understand the end-to-end story and terminology before reading implementation details.

**Location:** `docs/case-studies/acme/THE-WHOLE-PROJECT-IN-PLAIN-ENGLISH.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/THE-WHOLE-PROJECT-IN-PLAIN-ENGLISH.html) · [Markdown source](case-studies/acme/THE-WHOLE-PROJECT-IN-PLAIN-ENGLISH.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=2)

**Inside:** Follow one customer request—and understand every part along the way · 1. The entire idea in one minute · 2. Meet the office staff

### Acme Agent Platform — TypeScript Architecture

Read the picture as four responsibilities. React gathers user intent. Next.js authenticates and records it. Durable dispatch ensures that accepted work reaches the workflow runtime. Workflow DevKit coordinates steps, waits, and retries.

**Use it for:** Compare the alternative TypeScript implementation and its unchanged safety responsibilities.

**Location:** `docs/case-studies/acme/TYPESCRIPT-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/acme/TYPESCRIPT-ARCHITECTURE.html) · [Markdown source](case-studies/acme/TYPESCRIPT-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=acme&chapter=5)

**Inside:** Next.js, React, and durable workflows on Vercel · 1. At a glance · 2. What the architecture teaches

<a id="hospital"></a>

## HarborCare — privacy-first coordination

A synthetic hospital discharge scenario with recipient-specific information sharing.

### HarborCare Privacy Platform

HarborCare is a fictional hospital. This document set describes a proposed privacy-engineering demonstration using entirely synthetic patients, organizations, documents, and messages. It is not a clinical decision system, a live hospital integration, or a claim of HIPAA compliance.

**Use it for:** Orient yourself to the case study and select the right next guide.

**Location:** `docs/case-studies/hospital/00-START-HERE.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/00-START-HERE.html) · [Markdown source](case-studies/hospital/00-START-HERE.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=1)

**Inside:** A complete learning case study: share the right information with the right recipient · 1. Start with the story · 2. The document collection

### HarborCare — Project Strategy

Build one long case study with five independently demonstrable projects. Each project should have its own tests and README, but they share contracts and a fictional patient story. This gives the portfolio depth without duplicating login, storage, and policy code across five repositories.

**Use it for:** Choose project scope, build order and the evidence a convincing demonstration needs.

**Location:** `docs/case-studies/hospital/01-PROJECT-STRATEGY.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/01-PROJECT-STRATEGY.html) · [Markdown source](case-studies/hospital/01-PROJECT-STRATEGY.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=2)

**Inside:** Build a privacy system you can explain, not five disconnected medical chatbots · 1. At a glance · 2. The running case

### The Hospital Case in Plain English

The most important sentence is: private information can be shared with an authorized recipient without becoming public information. A destination address is still private when the assigned driver needs it.

**Use it for:** Understand the end-to-end story and terminology before reading implementation details.

**Location:** `docs/case-studies/hospital/02-PLAIN-ENGLISH-AND-LEGEND.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/02-PLAIN-ENGLISH-AND-LEGEND.html) · [Markdown source](case-studies/hospital/02-PLAIN-ENGLISH-AND-LEGEND.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=3)

**Inside:** A hospital team needs to coordinate—not tell everybody everything · 1. At a glance · 2. Follow one patient

### Privacy Policy and Adversarial Test Catalogue

All patient and organization data is synthetic. The policy below intentionally narrows the demo. It does not assert that these exact fields or recipient categories are universally permitted or prohibited under law. Real decisions depend on jurisdiction, purpose, relationships, data type, organizational policy, and applicable authority.

**Use it for:** Define the safety boundary and adversarial tests before enabling consequential actions.

**Location:** `docs/case-studies/hospital/03-PRIVACY-POLICY-AND-TESTS.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/03-PRIVACY-POLICY-AND-TESTS.html) · [Markdown source](case-studies/hospital/03-PRIVACY-POLICY-AND-TESTS.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=4)

**Inside:** Explicit teaching rules—not a substitute for healthcare compliance review · 1. The classification model · 2. Recipient/purpose matrix

### HarborCare — Python Reference Architecture

This blueprint implements the synthetic hospital scenario in Python. It is a proposed application, not code already built. The local receiver replaces every real external agency. The privacy matrix is an explicit demo policy; clinical and legal determinations remain outside the model.

**Use it for:** Trace components, folders, ownership and calls before building the application.

**Location:** `docs/case-studies/hospital/04-PYTHON-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/04-PYTHON-ARCHITECTURE.html) · [Markdown source](case-studies/hospital/04-PYTHON-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=5)

**Inside:** Permission checks at every boundary, one authoritative release record · 1. System map · 2. Ownership

### HarborCare — Next.js + Python Hybrid

Next.js is a backend-for-frontend layer: it verifies a session, loads safe display data, and forwards commands. It does not independently implement the transport field allowlist or read the chart database directly.

**Use it for:** Understand the Next.js interface and Python backend boundary.

**Location:** `docs/case-studies/hospital/05-HYBRID-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/05-HYBRID-ARCHITECTURE.html) · [Markdown source](case-studies/hospital/05-HYBRID-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=6)

**Inside:** A reviewer-friendly screen without a second privacy policy engine · 1. At a glance · 2. Proposed web structure

### HarborCare — Full TypeScript Counterpart

TypeScript types catch many development mistakes, but network JSON still needs runtime validation. A shared package does not give every service the same permissions. The release service remains the only component authorized to dispatch protected packets.

**Use it for:** Compare the alternative TypeScript implementation and its unchanged safety responsibilities.

**Location:** `docs/case-studies/hospital/06-TYPESCRIPT-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/06-TYPESCRIPT-ARCHITECTURE.html) · [Markdown source](case-studies/hospital/06-TYPESCRIPT-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=7)

**Inside:** One application language, unchanged privacy boundaries · 1. At a glance · 2. Proposed repository

### HarborCare — Repositories and Deployment

This document describes future application repositories. The files created now are learning documents inside image-course; no HarborCare app or cloud service is being provisioned.

**Use it for:** Decide what lives in Git, what runs separately and what may be deployed.

**Location:** `docs/case-studies/hospital/07-REPOSITORIES-AND-DEPLOYMENT.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/07-REPOSITORIES-AND-DEPLOYMENT.html) · [Markdown source](case-studies/hospital/07-REPOSITORIES-AND-DEPLOYMENT.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=8)

**Inside:** Keep teaching material, application code, and live state separate · 1. Proposed local layout · 2. Why not add hospital patients to Acme's database?

### Build HarborCare by Hand

This series is a construction workbook, not a claim that the application already exists. Build the Python reference first, then add its web interface. The TypeScript architecture is an alternative implementation, not a second system that must be running alongside Python.

**Use it for:** Choose the construction sequence and understand each workbook’s acceptance gate.

**Location:** `docs/case-studies/hospital/manual-build/00-START-HERE.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/manual-build/00-START-HERE.html) · [Markdown source](case-studies/hospital/manual-build/00-START-HERE.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=9)

**Inside:** From an empty folder to a deployed synthetic demonstration · Your route through the work · What “by hand” means here

### 1. Foundations: Build the Rules Before the Agent

Your first program does not need an AI model. It needs to distinguish an assigned transport provider from an unrelated agency. The policy is the hospital's rulebook; the model is not allowed to rewrite it.

**Use it for:** Begin implementation with small contracts, rules, fixtures and executable tests.

**Location:** `docs/case-studies/hospital/manual-build/01-FOUNDATIONS.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/manual-build/01-FOUNDATIONS.html) · [Markdown source](case-studies/hospital/manual-build/01-FOUNDATIONS.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=10)

**Inside:** 1. Begin with an empty application folder · 2. Create the fixture story first · 3. Write and run one small rule

### 2. P1: Privacy-Gated MCP Tools

MCP gives an agent a standard way to discover and call tools. It does not decide whether the caller may see a patient record. Your service must enforce that rule on every call, including calls made without the friendly user interface.

**Use it for:** Build bounded tool interfaces and test authorization through the protocol adapter.

**Location:** `docs/case-studies/hospital/manual-build/02-MCP-TOOLS.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/manual-build/02-MCP-TOOLS.html) · [Markdown source](case-studies/hospital/manual-build/02-MCP-TOOLS.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=11)

**Inside:** 1. Create the service in layers · 2. Build the preview function before exposing a server · 3. Wrap the service with narrow tools

### 3. P2: Permission-Aware RAG

RAG means retrieving relevant information and using it to help answer a question. In HarborCare, relevance is not enough. A perfectly relevant paragraph about another patient must never enter the answer model's context.

**Use it for:** Build document ingestion, authorized retrieval and evidence-backed answers.

**Location:** `docs/case-studies/hospital/manual-build/03-PERMISSION-AWARE-RAG.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/manual-build/03-PERMISSION-AWARE-RAG.html) · [Markdown source](case-studies/hospital/manual-build/03-PERMISSION-AWARE-RAG.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=12)

**Inside:** 1. Create two small corpora · 2. Build the ingestion files · 3. Implement the query path in the correct order

### 4. P3: A2A Care Coordination

Agent-to-agent communication lets specialists collaborate. Think of a care coordinator asking a transport desk to arrange a pickup. The desk needs a bounded task, not a photocopy of every conversation and clinical record.

**Use it for:** Build specialist task coordination, artifact handling and failure behavior.

**Location:** `docs/case-studies/hospital/manual-build/04-A2A-COORDINATION.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/manual-build/04-A2A-COORDINATION.html) · [Markdown source](case-studies/hospital/manual-build/04-A2A-COORDINATION.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=13)

**Inside:** 1. Define task envelopes before agents · 2. Write three deterministic specialists · 3. Add the coordinator

### 5. P4: Approval, Disclosure and Recovery

This is the most important project in the case study. Preparing a packet is reversible. Sending it may not be. Build the release state machine before connecting a delivery adapter.

**Use it for:** Implement approval-bound execution, durable records and crash recovery.

**Location:** `docs/case-studies/hospital/manual-build/05-DISCLOSURE-WORKFLOW.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/manual-build/05-DISCLOSURE-WORKFLOW.html) · [Markdown source](case-studies/hospital/manual-build/05-DISCLOSURE-WORKFLOW.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=14)

**Inside:** 1. Create the state model · 2. Bind the review to the actual disclosure · 3. Add durable storage

### 6. P5: Build the Reviewer Workspace

The reviewer needs to answer four questions: which patient task is this, who will receive information, exactly which fields will they receive, and has anything actually been sent? The page should make those answers clear without exposing the entire patient chart.

**Use it for:** Build the human-facing review interface and explain authoritative job state.

**Location:** `docs/case-studies/hospital/manual-build/06-PRIVACY-WORKSPACE.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/manual-build/06-PRIVACY-WORKSPACE.html) · [Markdown source](case-studies/hospital/manual-build/06-PRIVACY-WORKSPACE.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=15)

**Inside:** 1. Create the web application last · 2. Define a browser-safe response contract · 3. Build the read path

### 7. Operate a Production-Style Synthetic Demo

Production-style means repeatable builds, controlled access, observed failures and tested recovery. It does not mean this teaching application is approved to handle real patients. Keep synthetic-only operation as a technical restriction as well as a written warning.

**Use it for:** Prepare packaging, synthetic demonstrations, operational tests and release evidence.

**Location:** `docs/case-studies/hospital/manual-build/07-PRODUCTION-DEMO.md`

**Availability:** Published in website

[Read HTML](case-studies/hospital/manual-build/07-PRODUCTION-DEMO.html) · [Markdown source](case-studies/hospital/manual-build/07-PRODUCTION-DEMO.md) · [Website reader](https://course.ketanshukla.dev/#course=hospital&chapter=16)

**Inside:** 1. Define the deployment units · 2. Separate environments before deploying · 3. Create the CI gates

<a id="filepilot"></a>

## FilePilot — safe file automation

A proposed local assistant for finding and organizing files through approved, recoverable operations.

### FilePilot — Your Personal File Operations Assistant

FilePilot is a proposed local-first application that helps you understand and organize files without handing a language model unrestricted control of your computer. It combines a file explorer, document search, an organization planner, a controlled operations engine, and a review workspace.

**Use it for:** Orient yourself to the case study and select the right next guide.

**Location:** `docs/case-studies/filepilot/00-START-HERE.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/00-START-HERE.html) · [Markdown source](case-studies/filepilot/00-START-HERE.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=1)

**Inside:** The five projects · Choose your reading route

### FilePilot — Project Strategy

Build one coherent case study with five independently demonstrable modules. Begin on Windows, with one local user, one disposable sandbox, ordinary files, and same-volume moves. Keep a single writer and make every write require approval. Add semantic search and optional specialist agents after the deterministic safety behavior works.

**Use it for:** Choose project scope, build order and the evidence a convincing demonstration needs.

**Location:** `docs/case-studies/filepilot/01-PROJECT-STRATEGY.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/01-PROJECT-STRATEGY.html) · [Markdown source](case-studies/filepilot/01-PROJECT-STRATEGY.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=2)

**Inside:** A concrete fixture collection · Build sequence and proof · Define a convincing completion target

### FilePilot — The Whole Flow in Plain English

Think of FilePilot as a careful librarian. The librarian can read the labels, look inside permitted books, and suggest a better arrangement. But rearranging the shelves requires an approved checklist. The checklist is checked again just before each book moves.

**Use it for:** Understand the end-to-end story and terminology before reading implementation details.

**Location:** `docs/case-studies/filepilot/02-PLAIN-ENGLISH-AND-LEGEND.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/02-PLAIN-ENGLISH-AND-LEGEND.html) · [Markdown source](case-studies/filepilot/02-PLAIN-ENGLISH-AND-LEGEND.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=3)

**Inside:** 1. You choose the shelf · 2. The explorer makes a catalog · 3. Search finds evidence

### FilePilot — Safety Policy and Adversarial Tests

The first supported write operation is a single ordinary-file move within one approved Windows sandbox on one volume. No directory moves, overwrites, permanent deletion, arbitrary shell execution, archive extraction, network destinations, or background cleanup. A rename is a move whose parent folder does not change.

**Use it for:** Define the safety boundary and adversarial tests before enabling consequential actions.

**Location:** `docs/case-studies/filepilot/03-SAFETY-POLICY-AND-TESTS.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/03-SAFETY-POLICY-AND-TESTS.html) · [Markdown source](case-studies/filepilot/03-SAFETY-POLICY-AND-TESTS.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=4)

**Inside:** Root and path policy · Approval contract · Test matrix

### FilePilot — Python Reference Architecture

Use one Python application repository with modules that have clear responsibilities. Start with a CLI, SQLite, and a local single-writer worker. MCP and a browser API are adapters around those modules; they are not the place where permission rules live. A model is optional.

**Use it for:** Trace components, folders, ownership and calls before building the application.

**Location:** `docs/case-studies/filepilot/04-PYTHON-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/04-PYTHON-ARCHITECTURE.html) · [Markdown source](case-studies/filepilot/04-PYTHON-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=5)

**Inside:** Proposed repository structure · File responsibilities and calls · Storage contract

### FilePilot — Next.js Workspace with a Local Python Engine

The recommended full application combines a local Next.js/React workspace with the Python reference engine. The interface makes plans understandable; Python owns root grants, inspection, approval validation, and execution. Start with both running on the same computer.

**Use it for:** Understand the Next.js interface and Python backend boundary.

**Location:** `docs/case-studies/filepilot/05-HYBRID-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/05-HYBRID-ARCHITECTURE.html) · [Markdown source](case-studies/filepilot/05-HYBRID-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=6)

**Inside:** Proposed UI structure · API contract sketch · Walk through a review

### FilePilot — TypeScript Counterpart

A TypeScript implementation can demonstrate the same architecture, but it still needs a local runtime to operate on personal files. Next.js and Vercel do not remove that requirement. Build this counterpart after the Python path works, using shared behavioral contracts rather than running two writers on one sandbox.

**Use it for:** Compare the alternative TypeScript implementation and its unchanged safety responsibilities.

**Location:** `docs/case-studies/filepilot/06-TYPESCRIPT-ARCHITECTURE.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/06-TYPESCRIPT-ARCHITECTURE.html) · [Markdown source](case-studies/filepilot/06-TYPESCRIPT-ARCHITECTURE.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=7)

**Inside:** Proposed separate repository · Map the responsibilities · Preserve the operations contract

### FilePilot — Repositories, Runtime Data, and Deployment

Keep teaching materials in the existing learning-library repository. Implement FilePilot later in its own sibling application repository. The five projects are modules within that repository, not five nested Git repositories. Personal runtime data belongs outside both repositories.

**Use it for:** Decide what lives in Git, what runs separately and what may be deployed.

**Location:** `docs/case-studies/filepilot/07-REPOSITORIES-AND-DEPLOYMENT.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/07-REPOSITORIES-AND-DEPLOYMENT.html) · [Markdown source](case-studies/filepilot/07-REPOSITORIES-AND-DEPLOYMENT.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=8)

**Inside:** Proposed top-level organization · Repository and deployment matrix · Development and release environments

### Build FilePilot Manually — Start Here

This series teaches how to construct the proposed application from an empty repository. It is a sequence of implementation workbooks: each one identifies files, functions, inputs, outputs, tests, and a completion gate. The foundation lesson contains a complete executable exercise. Later chapters deliberately require implementation work; they are not a ready-made production codebase.

**Use it for:** Choose the construction sequence and understand each workbook’s acceptance gate.

**Location:** `docs/case-studies/filepilot/manual-build/00-START-HERE.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/manual-build/00-START-HERE.html) · [Markdown source](case-studies/filepilot/manual-build/00-START-HERE.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=9)

**Inside:** Reading and construction order · Your development loop · What to record as you learn

### Build FilePilot — Foundations and Your First Tests

Start with a program that cannot touch the filesystem at all. Its job is to determine whether a plan is unchanged, approved, and still eligible for execution. This exercise uses Python's standard library and synthetic identifiers. It is intentionally not a complete permission system or filesystem executor.

**Use it for:** Begin implementation with small contracts, rules, fixtures and executable tests.

**Location:** `docs/case-studies/filepilot/manual-build/01-FOUNDATIONS.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/manual-build/01-FOUNDATIONS.html) · [Markdown source](case-studies/filepilot/manual-build/01-FOUNDATIONS.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=10)

**Inside:** 1. Create the smallest learning file · 2. Understand every function · 3. Refactor only after the tests pass

### Build FilePilot — The Read-Only MCP Explorer

Create a useful explorer before creating a writer. It should inventory an approved sandbox, return bounded previews, and identify duplicate candidates without changing anything. Test the Python services directly, then expose the same behavior through MCP.

**Use it for:** Build bounded tool interfaces and test authorization through the protocol adapter.

**Location:** `docs/case-studies/filepilot/manual-build/02-MCP-EXPLORER.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/manual-build/02-MCP-EXPLORER.html) · [Markdown source](case-studies/filepilot/manual-build/02-MCP-EXPLORER.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=11)

**Inside:** 1. Create the modules in this order · 2. Define a narrow tool surface · 3. Detect duplicate candidates carefully

### Build FilePilot — Private Document Search with RAG

Start with local text and Markdown. Build keyword retrieval before embeddings, and answer from quoted evidence before adding generated summaries. Every chunk must retain the source file ID, document revision, root ID, and extraction version.

**Use it for:** Build document ingestion, authorized retrieval and evidence-backed answers.

**Location:** `docs/case-studies/filepilot/manual-build/03-DOCUMENT-RAG.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/manual-build/03-DOCUMENT-RAG.html) · [Markdown source](case-studies/filepilot/manual-build/03-DOCUMENT-RAG.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=12)

**Inside:** 1. Build the files · 2. Define the evidence object · 3. Trace an authorized query

### Build FilePilot — Organization Planning and Optional A2A

Build a deterministic planner first. It takes an inventory snapshot, allowed destinations, and optional evidence, then returns proposed operations. Later, a model or separate classifier can suggest categories. Neither gets filesystem write access or approval authority.

**Use it for:** Implement validated organization proposals and optional specialist delegation.

**Location:** `docs/case-studies/filepilot/manual-build/04-PLANNER-AND-A2A.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/manual-build/04-PLANNER-AND-A2A.html) · [Markdown source](case-studies/filepilot/manual-build/04-PLANNER-AND-A2A.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=13)

**Inside:** 1. Create the plan contract · 2. Make uncertainty a first-class result · 3. Add an A2A specialist only when it has a real boundary

### Build FilePilot — Approved Operations and Crash Recovery

Implement one ordinary-file, same-volume move before attempting any batch feature. The engine loads a persisted approved plan, checks current conditions, records intent, attempts the operation through a reviewed adapter, verifies the outcome, and records completion. A crash can happen between any two of those steps.

**Use it for:** Implement approval-bound execution, durable records and crash recovery.

**Location:** `docs/case-studies/filepilot/manual-build/05-SAFE-OPERATIONS.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/manual-build/05-SAFE-OPERATIONS.html) · [Markdown source](case-studies/filepilot/manual-build/05-SAFE-OPERATIONS.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=14)

**Inside:** 1. Create the storage and services · 2. Implement the sequence, not a giant helper · 3. Define reconciliation outcomes

### Build FilePilot — The Human Review Workspace

Build the interface around evidence and decisions, not an unrestricted chat box. The primary screens are root selection, inventory, evidence search, plan review, and operation history. Chat can help formulate a request, but the review screen remains the authority checkpoint.

**Use it for:** Build the human-facing review interface and explain authoritative job state.

**Location:** `docs/case-studies/filepilot/manual-build/06-FILE-WORKSPACE.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/manual-build/06-FILE-WORKSPACE.html) · [Markdown source](case-studies/filepilot/manual-build/06-FILE-WORKSPACE.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=15)

**Inside:** 1. Build the screens in order · 2. Treat the plan as a versioned document · 3. Handle connection loss and repeat clicks

### Build FilePilot — Testing, Packaging, and a Production Demo

Finish with two clearly labelled deliverables: a restricted local sandbox application and, optionally, a public simulation using synthetic data. Neither should imply unrestricted access to real folders. A production-quality demonstration is reproducible, honest about its limits, and supported by test evidence.

**Use it for:** Prepare packaging, synthetic demonstrations, operational tests and release evidence.

**Location:** `docs/case-studies/filepilot/manual-build/07-PRODUCTION-DEMO.md`

**Availability:** Published in website

[Read HTML](case-studies/filepilot/manual-build/07-PRODUCTION-DEMO.html) · [Markdown source](case-studies/filepilot/manual-build/07-PRODUCTION-DEMO.md) · [Website reader](https://course.ketanshukla.dev/#course=filepilot&chapter=16)

**Inside:** 1. Build a release checklist · 2. Keep configuration explicit · 3. Make state upgrades recoverable

<a id="planning"></a>

## Planning & reading-style references

Roadmaps, production plans and the blue reading-style sample. Historical plans are not current implementation status.

### The right information. The right person.

This is a typography sample, not a website update. Open the neighboring HTML file to judge the intended font sizes and blue palette; Markdown preview styling is controlled by your reader.

**Use it for:** Compare the approved blue palette, larger typography and reading treatments.

**Location:** `docs/design-samples/READING-STYLE.md`

**Availability:** Local reference — not in website allowlist

[Read HTML](design-samples/READING-STYLE.html) · [Markdown source](design-samples/READING-STYLE.md)

**Inside:** Start with a simple question · See the journey · A small, concrete example

### Video Course Production Strategy

Plans a pilot-led route from visual teaching documents to video lessons, narration scripts, storyboards and presenter options. This is a historical planning document, not proof that videos were generated.

**Use it for:** Plan a video-course pilot and distinguish production options from finished outputs.

**Location:** `docs/general/Video Course Production Strategy.docx`

**Availability:** Local reference — not in website allowlist

[Word document](general/Video%20Course%20Production%20Strategy.docx)

### Volumes 1–10 — Complete Learning Roadmap

Maps the ten-volume learning progression from foundations through protocols, retrieval, security, operations and the final project blueprint. Its original completed/planned labels predate the current ten-course library.

**Use it for:** Understand the curriculum sequence; use current course files for completion status.

**Location:** `docs/general/Visual Agent Course - Volumes 1 to 10 Roadmap.docx`

**Availability:** Local reference — not in website allowlist

[Word document](general/Visual%20Agent%20Course%20-%20Volumes%201%20to%2010%20Roadmap.docx)

### Volumes 4–10 — Future Learning Roadmap

The earlier proposal for seven continuation volumes covering protocols, knowledge, workflows, security, operations, product design and architecture.

**Use it for:** Review the original continuation plan, not current delivery status.

**Location:** `docs/general/Visual Agent Course - Volumes 4 to 10 Roadmap.docx`

**Availability:** Local reference — not in website allowlist

[Word document](general/Visual%20Agent%20Course%20-%20Volumes%204%20to%2010%20Roadmap.docx)

<a id="maintenance"></a>

## Authoring & verification references

Templates, prompt records and verification notes for maintaining the document collection.

### document.template.html

Reusable HTML layout containing placeholders and shared document structure.

**Use it for:** Maintain HTML rendering layouts; this is a template, not a finished lesson.

**Location:** `docs/assets/document.template.html`

**Availability:** Local reference — not in website allowlist

[HTML template](assets/document.template.html)

### document.template.html

Reusable HTML layout containing placeholders and shared document structure.

**Use it for:** Maintain HTML rendering layouts; this is a template, not a finished lesson.

**Location:** `docs/case-studies/acme/architecture-assets/document.template.html`

**Availability:** Local reference — not in website allowlist

[HTML template](case-studies/acme/architecture-assets/document.template.html)

### Architecture image prompts

Generated with the built-in image tool. Final images are copied into this directory; original generated files were retained. No existing course images were changed.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `docs/case-studies/acme/architecture-assets/GENERATION-PROMPTS.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](case-studies/acme/architecture-assets/GENERATION-PROMPTS.md)

**Inside:** 01-platform-map.png · 02-mcp-safe-write.png · 03-rag-evidence-pipeline.png

### Architecture guide verification

Diagrams: six final original PNGs, visually inspected; retrieval topology, recovery amount, and runtime grouping corrected during inspection.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `docs/case-studies/acme/architecture-assets/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](case-studies/acme/architecture-assets/VERIFICATION.md)

### document.template.html

Reusable HTML layout containing placeholders and shared document structure.

**Use it for:** Maintain HTML rendering layouts; this is a template, not a finished lesson.

**Location:** `docs/case-studies/acme/companion-architecture-assets/document.template.html`

**Availability:** Local reference — not in website allowlist

[HTML template](case-studies/acme/companion-architecture-assets/document.template.html)

### Companion architecture diagrams

E:/image-course/docs/case-studies/acme/companion-architecture-assets/01-hybrid-overview.png

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `docs/case-studies/acme/companion-architecture-assets/GENERATION-PROMPTS.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](case-studies/acme/companion-architecture-assets/GENERATION-PROMPTS.md)

**Inside:** Hybrid architecture · TypeScript architecture

### Companion document checks

Both Markdown guides were converted to standalone HTML using Pandoc and the existing architecture stylesheet. The original documents and course website were not modified.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `docs/case-studies/acme/companion-architecture-assets/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](case-studies/acme/companion-architecture-assets/VERIFICATION.md)

### template.html

Reusable HTML layout containing placeholders and shared document structure.

**Use it for:** Maintain HTML rendering layouts; this is a template, not a finished lesson.

**Location:** `docs/case-studies/acme/manual-build/assets/template.html`

**Availability:** Local reference — not in website allowlist

[HTML template](case-studies/acme/manual-build/assets/template.html)

### Manual-build series verification

Eight diagram placements: three new precise SVG teaching diagrams and five reused architecture images, embedded in the HTML.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `docs/case-studies/acme/manual-build/assets/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](case-studies/acme/manual-build/assets/VERIFICATION.md)

**Inside:** Delivered · Checks performed · Limits

### Verification scope

The repository/deployment guide is an architectural proposal, not a scaffold or deployment.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `docs/case-studies/acme/repository-assets/verify.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](case-studies/acme/repository-assets/verify.md)

<a id="course-01"></a>

## Visual Course Volume 1 — MCP, ACP, A2A and RAG

A visual course on modern agent architecture, capabilities, collaboration, and retrieval.

### Diagram 01 — Agent Architecture

Five stages in a straight line: a person, the agent they talk to, the capabilities that agent can call, the specialist agents it can hand work to, and the policy layer that everything eventually touches. A second, quieter route runs back underneath, from the policy layer all the way to the person.

**Use it for:** Study Agent Architecture through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/01-agent-architecture.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/01-agent-architecture.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=1)

**Inside:** 1. Five stages means four boundaries · 2. A capability is a tool; a specialist is an actor · 3. Policy is the far wall, not a step

### Diagram 02 — Safe Side Effect

This is the diagram for the moment an agent stops reading and starts changing something. It breaks a single write into four required steps and then shows what happens when that same write is attempted a second time.

**Use it for:** Study Safe Side Effect through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/02-safe-side-effect.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/02-safe-side-effect.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=2)

**Inside:** 1. The colour flips at the point of no return · 2. Confirmation is a human physically touching the trigger · 3. Authorization is per-item, not a boolean

### Diagram 03 — Modern Agent System Map

Three lanes, one router, one gate. The agent branches into knowledge, capabilities, and other agents — and all three reconverge on a single policy platform before anything reaches the system of record.

**Use it for:** Study Modern Agent System Map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/03-modern-agent-system-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/03-modern-agent-system-map.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=3)

**Inside:** 1. Three lanes answer three different questions · 2. The agent is the only thing that fans out · 3. Convergence on policy is the structural claim

### Diagram 04 — Choose the Boundary

One question, four answers, one floor. WHAT OWNS THE WORK? branches into the four places a piece of work can live, and every branch is then routed back down into a policy check that no branch can avoid.

**Use it for:** Study Choose the Boundary through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/04-choose-the-boundary.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/04-choose-the-boundary.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=4)

**Inside:** 1. The question is about ownership, and the wording is doing work · 2. Local function is listed first, and that is an argument · 3. The four branches are exclusive per unit of work

### Diagram 05 — Request Journey

The same architecture as diagram 01, re-told as six verbs. Where the architecture diagram names components, this one names actions — and in doing so it adds two stages that the component view has no box for: planning at the front, and verification at the end.

**Use it for:** Study Request Journey through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/05-request-journey.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/05-request-journey.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=5)

**Inside:** 1. Two of the six stages have no component · 2. Retrieve comes before act, and the ordering is a commitment · 3. Delegate sits after act, not instead of it

### Diagram 06 — Protocol Comparison

Four acronyms, four one-word definitions. RAG = KNOWLEDGE. MCP = CAPABILITIES. A2A = AGENT WORK. ACP = HISTORY.

**Use it for:** Study Protocol Comparison through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/06-protocol-comparison.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/06-protocol-comparison.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=6)

**Inside:** 1. One word each, and the words are chosen carefully · 2. Three of these are complementary; the fourth is on a different axis · 3. Each panel's icon defines the term better than its label

### Diagram 07 — MCP Capability Discovery

Four stages: a client, a server that announces what it has, a catalogue of capabilities, and a call. Underneath, a bright cyan line carries the catalogue itself back from the far end to the client.

**Use it for:** Study MCP Capability Discovery through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/07-mcp-capability-discovery.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/07-mcp-capability-discovery.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=7)

**Inside:** 1. Discovery is a step, and it produces an object · 2. The server announces; the client does not guess · 3. Every row in the catalogue carries a check

### Diagram 08 — MCP Primitives

This is the diagram you use when designing what a capability server actually exposes. The three-way split looks obvious once stated and is routinely collapsed in practice — most first-draft servers are all tools, with resources implemented as tools that read things and prompts not implemented at all. That collapse costs you specific, predictable things.

**Use it for:** Study MCP Primitives through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/08-mcp-primitives.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/08-mcp-primitives.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=8)

**Inside:** 1. Three primitives exist because three different things are being asked for · 2. The uri:// badge is the whole definition of a resource · 3. The conveyor belt is the tool's tell

### Diagram 09 — Stateless MCP

Two requests. Each one carries its own version, its own identity, its own tools, and its own payload. Both arrive at the same server. Underneath, a key crossed out in coral and the words NO SESSION MEMORY.

**Use it for:** Study Stateless MCP through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/09-stateless-mcp.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/09-stateless-mcp.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=9)

**Inside:** 1. "Complete" is the word doing the work · 2. The duplication is deliberate and it is the diagram's whole method · 3. Four things every request carries

### Diagram 10 — Modern MCP Request

One request, pulled apart into its four layers. A version, a method, a body, and metadata — stacked, labelled, and then delivered as a single thing to a server.

**Use it for:** Study Modern MCP Request through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/10-modern-mcp-request.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/10-modern-mcp-request.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=10)

**Inside:** 1. Four layers, and each answers a different question · 2. Version travels with the request, not with the connection · 3. The method sits outside the body for operational reasons

### Diagram 11 — Durable MCP Task

Four stages: start the work, receive an identifier, check on it, collect the result. Underneath, a dashed timeline with glowing nodes, and from the node under the progress stage a route back up to the identifier.

**Use it for:** Study Durable MCP Task through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/11-durable-mcp-task.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/11-durable-mcp-task.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=11)

**Inside:** 1. The ticket in panel 2 is the entire pattern · 2. Task identity is not session state · 3. The progress gauge is showing you something you must design

### Diagram 12 — MCP Security Gates

The content is not the list — most engineers can produce that list. The content is the ordering, and the fact that each gate is drawn as a raised, upright barrier that a request must pass through rather than a checkbox on a review form. Get the order wrong and you have built five controls that do less than five controls' worth of work.

**Use it for:** Study MCP Security Gates through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/12-mcp-security-gates.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/12-mcp-security-gates.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=12)

**Inside:** 1. The order is the lesson · 2. Audit is not the same as logging, and it is a gate · 3. Refusals are the most important thing audit captures

### Diagram 13 — RAG Ingestion Pipeline

Five stages that turn a pile of documents into something searchable: SOURCES → CLEAN → CHUNK → EMBED → INDEX.

**Use it for:** Study RAG Ingestion Pipeline through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/13-rag-ingestion-pipeline.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/13-rag-ingestion-pipeline.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=13)

**Inside:** 1. Sources are heterogeneous, and the picture insists on it · 2. Clean is the stage everyone skips and the one that decides quality · 3. Chunk is where you decide what a retrievable unit is

### Diagram 14 — RAG Answer Pipeline

Five stages that turn a question into a grounded answer: QUESTION → SEARCH → RERANK → CONTEXT → ANSWER.

**Use it for:** Study RAG Answer Pipeline through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/14-rag-answer-pipeline.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/14-rag-answer-pipeline.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=14)

**Inside:** 1. Search casts a wide net and returns a mess · 2. The scored list is the most instructive object in the diagram · 3. Context assembly is a stage, and it is where the budget lives

### Diagram 15 — RAG Chunk Size

Three panels, three verdicts: TOO SMALL with a coral ✗, JUST RIGHT with a teal ✓, TOO LARGE with an amber !.

**Use it for:** Study RAG Chunk Size through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/15-rag-chunk-size.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/15-rag-chunk-size.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=15)

**Inside:** 1. Too small destroys meaning, and the bin says so · 2. Too large dilutes, and the amber says something different · 3. The middle panel shows two properties, not one

### Diagram 16 — Hybrid Search

Two retrieval methods run in parallel, their results are combined, and then the combined set is put in order. Keyword and vector search are not alternatives to choose between — they are complementary, and the diagram's geometry says so by giving them equal panels feeding a single merge.

**Use it for:** Study Hybrid Search through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/16-hybrid-search.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/16-hybrid-search.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=16)

**Inside:** 1. The two lanes fail in opposite directions · 2. Parallel, not sequential — and that is a design commitment · 3. The merge is not a union, and the interleaving shows it

### Diagram 17 — Grounded Citations

Four stages — EVIDENCE → ANSWER → CITATIONS → VERIFY — with a colour assigned to each source and carried unbroken through every stage.

**Use it for:** Study Grounded Citations through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/17-grounded-citations.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/17-grounded-citations.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=17)

**Inside:** 1. Grounding is per-claim, not per-answer · 2. The four source types are deliberately different · 3. Citations are objects, not decorations

### Diagram 18 — RAG Evaluation Loop

Four measurements and one action, arranged as a circle that never terminates: RETRIEVAL → FAITHFULNESS → COVERAGE → LATENCY → IMPROVE → back to the start.

**Use it for:** Study RAG Evaluation Loop through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/18-rag-evaluation-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/18-rag-evaluation-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=18)

**Inside:** 1. Four metrics, because one number cannot see all four failures · 2. Latency is a quality metric, not an infrastructure metric · 3. Green, red and amber mean different things

### Diagram 19 — Agent Card Discovery

Four stages: find the card, check what it can do, check who it is, decide whether to trust it. The fourth stage is a gate labelled ALLOWLIST that splits into two visibly different outcomes — a teal route to an approved agent, and a coral route to a barricade marked BLOCKED.

**Use it for:** Study Agent Card Discovery through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/19-agent-card-discovery.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/19-agent-card-discovery.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=19)

**Inside:** 1. The card is published by the agent, which makes it a claim · 2. Interface and security are separate checks, and both are necessary · 3. The allowlist is the decision, and it is a human one

### Diagram 20 — A2A Task Lifecycle

Five stages: a message arrives, becomes a task, the task works, produces an artifact, and completes. Beneath them, a bright cyan rail with arrows pointing up into every single stage.

**Use it for:** Study A2A Task Lifecycle through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/20-a2a-task-lifecycle.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/20-a2a-task-lifecycle.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=20)

**Inside:** 1. A message is not a task · 2. The task ID is drawn as literal text, and that is deliberate · 3. Working is a state, not a gap

### Diagram 21 — A2A Delegation

A caller creates a task, sends it across a bridge to a specialist, and receives an artifact back. Meanwhile, on a separate platform in the bottom-left corner, DOMAIN + POLICY connects upward into the caller only — and never crosses the bridge.

**Use it for:** Study A2A Delegation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/21-a2a-delegation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/21-a2a-delegation.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=21)

**Inside:** 1. The bridge is drawn as architecture because it is a boundary · 2. The task card shows incomplete work, and that is the whole design · 3. Bounded means the boundaries are in the task

### Diagram 22 — A2A Interaction Modes

Four ways for a client to find out that delegated work has progressed: WAIT, STREAM, POLL, PUSH.

**Use it for:** Study A2A Interaction Modes through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/22-a2a-interaction-modes.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/22-a2a-interaction-modes.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=22)

**Inside:** 1. All four consume the same underlying thing · 2. WAIT is not wrong, it is bounded · 3. STREAM gives the user something to watch

### Diagram 23 — A2A Security Gates

Five gates that a delegation passes through: MINIMIZE CONTEXT → ALLOWLIST AGENT → BIND TASK → VALIDATE ARTIFACT → LOCAL APPROVAL.

**Use it for:** Study A2A Security Gates through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/23-a2a-security-gates.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/23-a2a-security-gates.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=23)

**Inside:** 1. Context minimisation comes first, and the funnel says why · 2. Allowlisting is one gate of five, not the whole story · 3. Binding is what stops a task becoming general authority

### Diagram 24 — Incident Response Team

Four specialist agents arranged around a shared INCIDENT TASK HUB, all working the same incident in parallel, with everything they produce converging on a single HUMAN COMMANDER below.

**Use it for:** Study Incident Response Team through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/24-incident-response-team.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/24-incident-response-team.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=24)

**Inside:** 1. The hub is a shared object, not a message bus · 2. Four agents, four domains, no overlap · 3. Parallelism is the reason to do this at all

### Diagram 25 — ACP to A2A Timeline

A river that starts coral, merges into blue, passes a version marker, and arrives at a teal construction site labelled BUILD HERE.

**Use it for:** Study ACP to A2A Timeline through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/25-acp-to-a2a-timeline.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/25-acp-to-a2a-timeline.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=25)

**Inside:** 1. The river merges — it does not dead-end · 2. The first panel is ideas, not infrastructure · 3. The middle panel is where the actual claim lives

### Diagram 26 — ACP to A2A Concept Map

Five old terms on the left in coral, five current terms on the right in teal, one arrow each. MANIFEST → AGENT CARD. RUN → TASK. INPUT → MESSAGE. OUTPUT → ARTIFACT. STATUS → TASK STATE.

**Use it for:** Study ACP to A2A Concept Map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/26-acp-a2a-concept-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/26-acp-a2a-concept-map.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=26)

**Inside:** 1. The one-to-one mapping is the reassurance · 2. Each rename fixes an imprecision · 3. Output to artifact is the one that changes code

### Diagram 27 — Customer Support

A complete support architecture: CUSTOMER → RAG POLICY → MCP TICKETS → A2A SPECIALIST → [APPROVAL GATE] → SAFE RESOLUTION, with a dashed return path to the customer.

**Use it for:** Study Customer Support through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/27-customer-support.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/27-customer-support.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=27)

**Inside:** 1. All three lanes appear, in the order the work needs them · 2. The knowledge index is drawn as a sub-platform, and that is a claim about scope · 3. The MCP stage is plaqued as a gateway, and the word is deliberate

### Diagram 28 — Research Analyst

A research pipeline: QUESTION → RAG EVIDENCE → MCP DATA → A2A REVIEWER → CITED REPORT, with a VERIFY & REFINE loop running back to the start.

**Use it for:** Study Research Analyst through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/28-research-analyst.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/28-research-analyst.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=28)

**Inside:** 1. Retrieved documents and live data are different things, and the diagram separates them · 2. The three data tiles are named, and naming them changes the design · 3. The reviewer is permitted to flag gaps, and the coral makes it explicit

### Diagram 29 — Software Maintenance

A maintenance pipeline: ISSUE → RAG CODEBASE → MCP TOOLS → A2A TEST AGENT → REVIEWED PATCH, with a dashed return to the issue.

**Use it for:** Study Software Maintenance through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/29-software-maintenance.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/29-software-maintenance.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=29)

**Inside:** 1. The toolbox changes, and the change is the point · 2. The codebase is a RAG lane, and it holds two kinds of thing · 3. Bounded task and test results are the same shape, and that is deliberate

### Diagram 30 — Loan Document Review

A lending pipeline: APPLICATION → RAG RULES → MCP SYSTEMS → A2A RISK REVIEW → HUMAN DECISION, with a banner across the bottom spelling the architecture's thesis in words: AGENT SUPPLIES EVIDENCE & RECOMMENDATION → HUMAN DECIDES.

**Use it for:** Study Loan Document Review through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 01/diagram-docs/30-loan-document-review.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2001/diagram-docs/30-loan-document-review.md) · [Website reader](https://course.ketanshukla.dev/#course=01&chapter=30)

**Inside:** 1. The banner is the diagram, and everything above it is supporting detail · 2. Both outcomes are drawn, and both are buttons · 3. Rules and systems are separated, and in lending the distinction is regulatory

<a id="course-02"></a>

## Visual Course Volume 2 — Build Your First Agent System

The implementation bridge from web basics to MCP, RAG, A2A, reliability, and deployment.

### Diagram 31 — Browser Request Journey

Six stages between typing an address and seeing a page: PERSON → BROWSER → DNS → HTTPS → WEB SERVER → PAGE + DATA.

**Use it for:** Study Browser Request Journey through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/31-browser-request-journey.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/31-browser-request-journey.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=31)

**Inside:** 1. Six stages, and three of them are invisible · 2. DNS is a lookup, and the diagram shows the actual translation · 3. HTTPS is a stage, not a setting

### Diagram 32 — HTTP Conversation

The composition is symmetrical on purpose: URL, METHOD, HEADERS, BODY on the left travelling in; STATUS, HEADERS, BODY on the right travelling out. Once you can name those seven things, you can read almost any web interaction, debug most integration problems, and understand what a tool call actually is when you meet one later in the course.

**Use it for:** Study HTTP Conversation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/32-http-conversation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/32-http-conversation.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=32)

**Inside:** 1. Four parts going out, and each answers a different question · 2. The response adds status, and status is the part beginners skip · 3. Headers appear on both sides, and that symmetry is informative

### Diagram 33 — JSON Object Anatomy

One real JSON object at the centre, with its five structural concepts arranged around it: KEY, VALUE, ARRAY, NESTED OBJECT, DATA TYPES.

**Use it for:** Study JSON Object Anatomy through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/33-json-object-anatomy.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/33-json-object-anatomy.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=33)

**Inside:** 1. The centre object is a complete specimen · 2. Keys are strings; values can be anything · 3. The four data types are shown as literal values

### Diagram 34 — JSON Schema Validation

Data arrives, a schema describes what it should look like, a gate checks it against four criteria, and it comes out either ACCEPTED or REJECTED — with the rejection telling you specifically which of the four failed.

**Use it for:** Study JSON Schema Validation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/34-json-schema-validation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/34-json-schema-validation.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=34)

**Inside:** 1. A schema is a description, not code · 2. Four checks, and they are the four ways data goes wrong · 3. Both outcomes are drawn, and rejection gets more detail than acceptance

### Diagram 35 — Frontend / Backend Boundary

Five stages, and a glowing vertical line between the first and the second. One stage on the left labelled FRONTEND. Four on the right labelled BACKEND.

**Use it for:** Study Frontend / Backend Boundary through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/35-frontend-backend-boundary.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/35-frontend-backend-boundary.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=35)

**Inside:** 1. The line means "who can see this" · 2. Stage 1 is the only frontend stage, and that proportion is the point · 3. The API route is a door, and the metaphor is exact

### Diagram 36 — Server Request Pipeline

Six stages inside your backend: ROUTE → VALIDATE → AUTHENTICATE → AUTHORIZE → EXECUTE → RESPOND, with three coral STOP exits hanging beneath stages 2, 3 and 4.

**Use it for:** Study Server Request Pipeline through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/36-server-request-pipeline.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/36-server-request-pipeline.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=36)

**Inside:** 1. Three stages can stop, and they are consecutive · 2. Validate before authenticate is the ordering that surprises people · 3. Authenticate and authorize are different questions

### Diagram 37 — Storage Map

Four stores around one application, and each carries a one-word tag saying what it owns: FACTS, MEANING, PROGRESS, EVIDENCE.

**Use it for:** Study Storage Map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/37-storage-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/37-storage-map.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=37)

**Inside:** 1. Four stores because four different questions · 2. The tags prevent four specific mistakes · 3. Every arrow is bidirectional, and the audit log is the interesting exception

### Diagram 38 — Identity Boundary

Five stages: SIGN IN → TOKEN → AUTHENTICATE → AUTHORIZE → LEAST PRIVILEGE, with a glowing shield outline enclosing the final three and a coral branch dropping from authorization to DENIED.

**Use it for:** Study Identity Boundary through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/38-identity-boundary.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/38-identity-boundary.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=38)

**Inside:** 1. Sign-in happens once; the three inside the shield happen every request · 2. The token is a claim, not an identity · 3. Authenticate and authorize are consecutive and different

### Diagram 39 — Agent Decision Loop

Five stages in a ring — OBSERVE → PLAN → CHOOSE → ACT → CHECK — and then three different things can happen from CHECK: loop back to plan, stop, or ask a human.

**Use it for:** Study Agent Decision Loop through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/39-agent-decision-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/39-agent-decision-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=39)

**Inside:** 1. Five stages, and choose is separate from plan · 2. Act is a hand holding a tool, and that is the only stage that touches the world · 3. Check has three exits, and that is the diagram's content

### Diagram 40 — Tool Call Lifecycle

Five stages: MODEL PROPOSES → CLIENT VALIDATES → SERVER AUTHORIZES → DOMAIN EXECUTES → RESULT + RECEIPT, with two STOP signs hanging beneath stages 2 and 3.

**Use it for:** Study Tool Call Lifecycle through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/40-tool-call-lifecycle.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/40-tool-call-lifecycle.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=40)

**Inside:** 1. "Proposes" is the most carefully chosen word in the volume · 2. Two checks, in two different places, run by two different parties · 3. The two STOP signs are drawn as road signs, and there is no third

### Diagram 41 — RAG Reliability Loop

Six stages — QUESTION → RETRIEVE → RELEVANT? → ANSWER → CITE → VERIFY — with a decision diamond in the middle that can send the process back around.

**Use it for:** Study RAG Reliability Loop through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/41-rag-reliability-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/41-rag-reliability-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=41)

**Inside:** 1. The diamond is the only decision shape in the volume · 2. "No" is a normal outcome, and it has somewhere to go · 3. Answer, cite and verify are three stages, not one

### Diagram 42 — A2A Task State Machine

That repetition is the diagram's method. It is not showing five different things; it is showing one thing at five moments. The task has an identity that persists across every state change, which is precisely what makes work that takes time possible to manage.

**Use it for:** Study A2A Task State Machine through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/42-a2a-task-state-machine.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/42-a2a-task-state-machine.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=42)

**Inside:** 1. The card is the same card, and that is the whole idea · 2. Five states, and two of them are failures · 3. Failed and cancelled are different, and conflating them loses information

### Diagram 43 — Error Recovery Map

One hub labelled ERROR, four kinds of failure across the top, and four responses across the bottom — each response sitting directly beneath the failure it belongs to.

**Use it for:** Study Error Recovery Map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/43-error-recovery-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/43-error-recovery-map.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=43)

**Inside:** 1. Four categories, and they are distinguished by what you should do · 2. Retrying is correct for one of four, and wrong for the others · 3. Not authorized is the only coral arrow, and it is the only one that stops

### Diagram 44 — Observability Trace

A request gets an identifier, and that identifier travels with it through every component it touches. The journey is drawn as one continuous line with node dots at each hop, divided into four labelled spans, and it ends by branching into three different destinations: METRICS, LOGS, and AUDIT.

**Use it for:** Study Observability Trace through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/44-observability-trace.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/44-observability-trace.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=44)

**Inside:** 1. The trace ID is issued once, at the front · 2. One line, not four logs · 3. Spans divide the line into measurable segments

### Diagram 45 — Local to Vercel

Six stages from your laptop to the internet: LOCAL CODE → TESTS → GIT → VERCEL BUILD → PREVIEW → PRODUCTION.

**Use it for:** Study Local to Vercel through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/45-local-to-vercel.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/45-local-to-vercel.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=45)

**Inside:** 1. Failure loops back, and the two loops go to different places · 2. Tests come before git, and that ordering is a discipline · 3. Build happens somewhere else, in a clean environment

### Diagram 46 — Capstone Build Roadmap

Seven steps rising left to right, a person walking up them, and a flag at the top reading WORKING SYSTEM.

**Use it for:** Study Capstone Build Roadmap through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 02/diagram-docs/46-capstone-build-roadmap.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2002/diagram-docs/46-capstone-build-roadmap.md) · [Website reader](https://course.ketanshukla.dev/#course=02&chapter=46)

**Inside:** 1. The ascent means each step stands on the one below it · 2. Data comes first, and that is the least intuitive part · 3. Domain function before MCP tool, and this is the step most often skipped

<a id="course-03"></a>

## Visual Course Volume 3 — Production Agent Systems

Turn a working agent demo into a durable, secure, measurable system.

### Diagram 47 — A Stateless MCP Request

One request, drawn as an open envelope containing four cards — METHOD, NAME, REQUEST ID, AUTH SCOPE — travelling through a server, a policy gate, and a tool, with a result returning underneath.

**Use it for:** Study A Stateless MCP Request through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/47-stateless-mcp-request.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/47-stateless-mcp-request.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=47)

**Inside:** 1. Four cards, and each removes a dependency on the past · 2. The envelope is open, and that is deliberate · 3. Policy sits between the server and the tool, not before the server

### Diagram 48 — Multi Round-Trip Requests

A tool call pauses, asks a question, gets an answer from a person, and is retried carrying both the answer and the original request state — after which it completes.

**Use it for:** Study Multi Round-Trip Requests through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/48-multi-round-trip-request.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/48-multi-round-trip-request.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=48)

**Inside:** 1. Input required is a first-class outcome, not an error · 2. The question is an artefact, not a message · 3. The retry carries two things, and both are named on the card

### Diagram 49 — The MCP Tasks Extension

A tool call that will take too long becomes a task. The caller receives a handle instead of a result, and from then on interacts with the work through three control operations — TASKS GET, TASKS UPDATE, TASKS CANCEL — plus a subscription that streams updates.

**Use it for:** Study The MCP Tasks Extension through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/49-mcp-tasks-extension.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/49-mcp-tasks-extension.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=49)

**Inside:** 1. The server decides, and that is a considered design choice · 2. The task handle is what you hold instead of a result · 3. Three control operations, and they map onto three different needs

### Diagram 50 — Routing, Caching, and Gateways

Two headers — MCP-METHOD and MCP-NAME — let a gateway do four things before anything is parsed: ROUTE, AUTHORIZE, RATE LIMIT, TRACE. The request then reaches one of three server types. Along the bottom, list responses travel back carrying CACHE SCOPE and TTL MS into a client cache.

**Use it for:** Study Routing, Caching, and Gateways through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/50-mcp-routing-and-cache.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/50-mcp-routing-and-cache.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=50)

**Inside:** 1. Two headers, and they are outside the body on purpose · 2. Four gateway functions, and their order matters · 3. Header body mismatch is a security control, not a validation nicety

### Diagram 51 — The Modern MCP Migration Map

Seven retired or deprecated mechanisms on the left, six modern replacements on the right, and a bridge between them carrying one instruction: TEST BOTH VERSIONS.

**Use it for:** Study The Modern MCP Migration Map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/51-mcp-migration-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/51-mcp-migration-map.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=51)

**Inside:** 1. The left column is not a random list — it is one idea repeated · 2. The right column is fewer items, and it is not a one-to-one map · 3. Self-describing requests is the keystone

### Diagram 52 — Conversation State vs Workflow State

Two lanes. The top one holds what was said. The bottom one holds what is true. An agent reads both; a domain service writes only to the bottom one. And on the right, in coral, the diagram states its thesis in words: CHAT IS NOT A DATABASE.

**Use it for:** Study Conversation State vs Workflow State through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/52-conversation-vs-workflow-state.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/52-conversation-vs-workflow-state.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=52)

**Inside:** 1. The two lanes hold different kinds of thing, and the icons say so · 2. The four workflow items are the minimum, and each is load-bearing · 3. The agent reads both lanes, and reads is the operative word

### Diagram 53 — Checkpoint and Resume

A workflow with checkpoints between the steps, a crash partway through, and a resume that reads the last checkpoint from a durable store and carries on.

**Use it for:** Study Checkpoint and Resume through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/53-checkpoint-and-resume.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/53-checkpoint-and-resume.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=53)

**Inside:** 1. Checkpoints are stages, not side effects · 2. A checkpoint records state, not progress · 3. The store is drawn separately and below, and that is the whole point

### Diagram 54 — Retry and Idempotency

One user intent produces one key. Two attempts carry the same key. One gate lets the first through and refuses the second. One receipt exists at the end, and both attempts get it back.

**Use it for:** Study Retry and Idempotency through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/54-retry-and-idempotency.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/54-retry-and-idempotency.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=54)

**Inside:** 1. The key is derived from the intent, before any attempt · 2. Both attempt cards carry the same value, and they are numbered · 3. The timeout is on the path, not at the end

### Diagram 55 — Queues, Parallel Work, and Joins

Work is queued, fanned out to three independent checks running in parallel, and then reassembled at a JOIN GATE before a decision is made.

**Use it for:** Study Queues, Parallel Work, and Joins through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/55-queues-parallel-work-and-joins.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/55-queues-parallel-work-and-joins.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=55)

**Inside:** 1. The queue is a stage, and it decouples the orchestrator from the work · 2. Three checks, and their independence is the reason to parallelise · 3. The join gate waits for all three, and produces one result

### Diagram 56 — Timeout, Cancel, and Compensate

Work runs past its deadline. A cancel request goes out, new work stops — and then the diagram does the thing most cancellation designs omit: it checks what already happened.

**Use it for:** Study Timeout, Cancel, and Compensate through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/56-timeout-cancel-and-compensate.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/56-timeout-cancel-and-compensate.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=56)

**Inside:** 1. Cancel stops new work; it does not undo old work · 2. The deadline is a stage, and it is what triggers everything · 3. STILL RUNNING is the branch point, and it goes two ways

### Diagram 57 — Context Budget

Everything available goes into a funnel labelled SELECT AND COMPRESS. Two things leave it sideways — IRRELEVANT OR STALE into a bin, and MUST KEEP to a protected card — and what remains drops into a CONTEXT BUDGET divided into six named segments with a fill gauge at the end.

**Use it for:** Study Context Budget through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/57-context-budget.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/57-context-budget.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=57)

**Inside:** 1. The budget has six segments, and they compete · 2. Select and compress are two operations, not one · 3. The two side exits are the interesting part

### Diagram 58 — Short-Term and Durable Memory

Three memory stores, each with a one-word classification: TEMPORARY, RECALLABLE, AUTHORITATIVE. A coral consent-and-policy gate stands between the first and the second. Every store carries DELETE and EXPIRY controls.

**Use it for:** Study Short-Term and Durable Memory through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/58-short-term-and-durable-memory.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/58-short-term-and-durable-memory.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=58)

**Inside:** 1. Three stores, three tags, three different questions · 2. The consent gate is coral, and its placement is precise · 3. The business record has no consent gate, and that is not an oversight

### Diagram 59 — Advanced Retrieval Pipeline

Eight stages: QUESTION → REWRITE → FILTER → HYBRID SEARCH → RERANK → ASSEMBLE EVIDENCE → ANSWER → CITE.

**Use it for:** Study Advanced Retrieval Pipeline through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/59-advanced-retrieval-pipeline.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/59-advanced-retrieval-pipeline.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=59)

**Inside:** 1. Rewrite comes before anything touches the index · 2. Filter before search, and this is the diagram's most important ordering claim · 3. NOT PERMITTED is drawn as a shield, not a bin

### Diagram 60 — Freshness and Index Versions

Everything in this diagram carries a version. The source is V7. The ingestion run is 42. The index is V42. And the answer record at the end states all of it: SOURCE V7, INDEX V42, CHECKED 2026-08-24.

**Use it for:** Study Freshness and Index Versions through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/60-freshness-and-index-versions.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/60-freshness-and-index-versions.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=60)

**Inside:** 1. Three version numbers, and they are deliberately different · 2. The answer record is the diagram's payload · 3. The freshness checker sits outside the main flow, and that is correct

### Diagram 61 — Conflict, Citation, and Abstention

Two gates before an answer is allowed: ENOUGH EVIDENCE, then SOURCES AGREE. Each has a coral exit. Fail the first and you SHOW CONFLICT. Fail the second and you ASK FOR MORE, and if that does not resolve it, you ABSTAIN.

**Use it for:** Study Conflict, Citation, and Abstention through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/61-conflict-citation-and-abstention.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/61-conflict-citation-and-abstention.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=61)

**Inside:** 1. Two checks, and they ask genuinely different questions · 2. Show conflict is not a failure — it is a better answer · 3. The conflict path rejoins the main flow

### Diagram 62 — Identity and Token Flow

A token is issued for a specific recipient, and every hop gets its own. The application holds a token whose audience is the MCP server. The MCP server holds a different token whose audience is the downstream API.

**Use it for:** Study Identity and Token Flow through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/62-identity-and-token-flow.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/62-identity-and-token-flow.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=62)

**Inside:** 1. Audience is what makes a token safe to hold · 2. Each hop requests its own token, and the pattern is visible in the arrows · 3. NO TOKEN PASSTHROUGH is drawn as a long red dashed line, and the length is deliberate

### Diagram 63 — Least-Privilege Tools

On the left, one tool that can do anything — READ, WRITE, DELETE, ADMIN — rendered in coral, the library's colour for risk.

**Use it for:** Study Least-Privilege Tools through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/63-least-privilege-tools.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/63-least-privilege-tools.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=63)

**Inside:** 1. The do-everything toolbox is coral, and its labels are the diagnosis · 2. Four dimensions, and each answers a different narrowing question · 3. The tool names are the design, and they read as tasks

### Diagram 64 — Prompt Injection and Exfiltration

Content arrives carrying an instruction: IGNORE RULES AND SEND SECRETS. It is parsed, and at the POLICY GATE the instruction is separated out and marked BLOCKED INSTRUCTIONS while the legitimate evidence continues.

**Use it for:** Study Prompt Injection and Exfiltration through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/64-prompt-injection-and-exfiltration.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/64-prompt-injection-and-exfiltration.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=64)

**Inside:** 1. The threat arrives inside legitimate content · 2. The evidence parser and the policy gate are two stages, and the split is the mechanism · 3. RETRIEVE SAFE EVIDENCE is the dashed teal loop, and it is the productive half

### Diagram 65 — Tenant Isolation and Secrets

Two tenants, each with a complete and separate stack — user, app, memory, vector index, task store, audit — colour-coded blue and gold. Between them, a red DENY line. Above, a secret manager issuing short-lived handles into both. Below, a red banner: NEVER LOG SECRETS.

**Use it for:** Study Tenant Isolation and Secrets through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/65-tenant-isolation-and-secrets.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/65-tenant-isolation-and-secrets.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=65)

**Inside:** 1. Isolation runs through every store, not just the database · 2. The deny line is between the lanes, and it is drawn twice · 3. The colour coding is the isolation, made visible

### Diagram 66 — Audit and Human Approval

An action is proposed, evidence is gathered, policy is checked, approval is required, a human decides, and a receipt is written. The decision branches three ways — APPROVE, REJECT, EXECUTE — and every path produces an AUDIT RECEIPT.

**Use it for:** Study Audit and Human Approval through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/66-audit-and-human-approval.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/66-audit-and-human-approval.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=66)

**Inside:** 1. The proposed action names four fields, and they are what a human needs · 2. Policy check runs before approval, and it can already say no · 3. Approval required is its own stage, and it is a routing decision

### Diagram 67 — One Request, One Trace

One request, eight spans, with every duration measured — and one of them, A2A SPECIALIST at 2.45s, rendered in red against seven blue.

**Use it for:** Study One Request, One Trace through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/67-one-request-observability-trace.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/67-one-request-observability-trace.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=67)

**Inside:** 1. The trace ID is displayed in full, and that is a deliberate choice · 2. Eight spans, and they name the actual architecture · 3. One red bar among seven blue is the entire diagnostic

### Diagram 68 — Golden Datasets and the Eval Harness

Seven stages, closed into a loop: real cases are redacted and curated into a golden dataset, the system is run against it, outputs are scored on five dimensions, failures are reviewed, and regression cases are added — which feed back into the dataset.

**Use it for:** Study Golden Datasets and the Eval Harness through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/68-golden-datasets-and-eval-harness.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/68-golden-datasets-and-eval-harness.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=68)

**Inside:** 1. Cases come from reality, not from imagination · 2. The four case types are the diagram's most important content · 3. Redact and curate is two operations, and both are obligations

### Diagram 69 — Stage-by-Stage Quality Metrics

Beneath those, six coral lines drop to red ✗ badges and converge on a single banner: FINAL FAILURE.

**Use it for:** Study Stage-by-Stage Quality Metrics through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/69-stage-by-stage-quality-metrics.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/69-stage-by-stage-quality-metrics.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=69)

**Inside:** 1. Six stages, six different metrics, and they are not interchangeable · 2. The failure lines are the diagram's real content · 3. The six numbers are deliberately similar, and that is the trap

### Diagram 70 — Latency and Cost Budgets

Ten seconds, allocated. Six stages with named time budgets that sum to exactly the total. Cost, allocated — four categories summing to 100%. Two paths through the system, FAST and DEEP. And a gate asking VALUE JUSTIFIES COST? with alerts on the failure side.

**Use it for:** Study Latency and Cost Budgets through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/70-latency-and-cost-budgets.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/70-latency-and-cost-budgets.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=70)

**Inside:** 1. The time budget sums exactly, and that forces the trade · 2. Tools have the largest allocation, and that reflects where time actually goes · 3. The cost budget is proportional, not absolute, and that is the right shape

### Diagram 71 — Red Team and Incident Learning Loop

A closed loop of nine stages that turns both attacks you run yourself and incidents that happen to you into verified controls.

**Use it for:** Study Red Team and Incident Learning Loop through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/71-red-team-and-incident-learning-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/71-red-team-and-incident-learning-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=71)

**Inside:** 1. The loop starts at threat model, not at attack · 2. Detect and contain sit between attacking and investigating, and their presence is a claim · 3. The five threat cards are a named catalogue, and each maps to a diagram in this volume

### Diagram 72 — MCP, A2A, and AG-UI Together

The lanes are parallel and separate. None feeds into another. That geometry is the argument: these are three different concerns operating at three different levels, and a production system runs all three simultaneously rather than choosing between them.

**Use it for:** Study MCP, A2A, and AG-UI Together through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/72-mcp-a2a-and-agui-together.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/72-mcp-a2a-and-agui-together.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=72)

**Inside:** 1. Three lanes, three questions, three audiences · 2. The lane order is top to bottom by proximity to the human · 3. Each lane has its own return path, and they are separate

### Diagram 73 — Typed Agent Event Stream

Eight typed events, a reducer that turns them into UI state, and five surfaces that render it. Underneath, an EVENT ID and a RUN ID, and a RECONNECT path that resumes AFTER LAST EVENT.

**Use it for:** Study Typed Agent Event Stream through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/73-typed-agent-event-stream.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/73-typed-agent-event-stream.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=73)

**Inside:** 1. Eight event types, and each one enables a different piece of interface · 2. Text delta and state snapshot are two different transmission models · 3. The reducer is a single named component, and that is an architectural claim

### Diagram 74 — Progress, Artifacts, and Recovery UX

Three columns. LIVE PROGRESS shows what is happening. ARTIFACTS shows what has been produced so far. RECOVERY shows what the user can do when something breaks.

**Use it for:** Study Progress, Artifacts, and Recovery UX through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/74-progress-artifacts-and-recovery-ux.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/74-progress-artifacts-and-recovery-ux.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=74)

**Inside:** 1. Progress steps are named, not numbered · 2. Artifacts are surfaced as they are produced, not at the end · 3. Partial failure is a distinct state, and it gets its own tile

### Diagram 75 — Interrupts, Approval, and Steering

Work plans, policy is checked, and then it pauses — presenting an approval card with a proposed action, evidence, a graded risk bar, an expiry, and three buttons.

**Use it for:** Study Interrupts, Approval, and Steering through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/75-interrupts-approval-and-steering.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/75-interrupts-approval-and-steering.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=75)

**Inside:** 1. The approval card carries four things, and the risk bar is graded · 2. The expiry is on the card, and it is the operational detail teams forget · 3. Three buttons, and EDIT is the interesting one

### Diagram 76 — Production Capstone Architecture

A user, a React experience, an orchestrator, a policy gate, a durable workflow, memory and RAG, an A2A specialist, MCP servers, evals, observability, and six shared stores — with a legend distinguishing request, results, denial and human control paths.

**Use it for:** Study Production Capstone Architecture through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 03/diagram-docs/76-production-capstone-architecture.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2003/diagram-docs/76-production-capstone-architecture.md) · [Website reader](https://course.ketanshukla.dev/#course=03&chapter=76)

**Inside:** 1. The orchestrator is the only component that touches everything · 2. Three components sit between the orchestrator and everything else · 3. The two capability lanes are on the right, and they are shaped differently

<a id="course-04"></a>

## Visual Course Volume 4 — Protocol Engineering and Interoperability

Read, test, connect, and safely evolve MCP, A2A, and AG-UI systems.

### Diagram 100 — Protocol Interoperability Lab

The whole volume, assembled. A named user — Maya — in a React interface, an orchestrator, an MCP server, an A2A agent, and four shared services hanging off a correlation spine.

**Use it for:** Study Protocol Interoperability Lab through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/100-protocol-interoperability-lab.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/100-protocol-interoperability-lab.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=100)

**Inside:** 1. Three protocols, three relationships, one orchestrator · 2. Each protocol destination carries a card naming what it uses · 3. Maya is named, and that is a deliberate choice

### Diagram 77 — Normative Rules Versus Examples

Three lanes. SPECIFICATION on the left, CONFORMANCE TESTS in the middle, EXAMPLES AND IMPLEMENTATION CHOICES on the right — and a vertical coral dashed divider between the right and the centre, labelled NOT A REQUIREMENT.

**Use it for:** Study Normative Rules Versus Examples through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/77-normative-rules-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/77-normative-rules-map.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=77)

**Inside:** 1. Three requirement words, three different obligations · 2. All three generate tests, and that is not obvious · 3. The divider is coral, and it points the right way

### Diagram 78 — Version, Capability, and Extension Negotiation

Three cards travel in both directions between a client and a server, in order: VERSION, CAPABILITIES, EXTENSIONS. The exchange resolves either to USE SHARED FEATURES along a green compatible path, or to CLEAR ERROR along a red one.

**Use it for:** Study Version, Capability, and Extension Negotiation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/78-version-capability-extension-negotiation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/78-version-capability-extension-negotiation.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=78)

**Inside:** 1. Three layers, in a required order · 2. The arrows run both ways, and that makes it negotiation rather than declaration · 3. The outcome is the intersection, and the label says so

### Diagram 79 — Requests, Results, Errors, and Correlation

A JSON-RPC request pulled apart into four cards — JSONRPC 2.0, ID 2048, METHOD, PARAMS — travelling from a client toward a server. It returns as either a RESULT or an ERROR, and both carry ID 2048.

**Use it for:** Study Requests, Results, Errors, and Correlation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/79-request-result-error-correlation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/79-request-result-error-correlation.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=79)

**Inside:** 1. The four request cards are the complete JSON-RPC envelope · 2. ID 2048 appears three times, and the repetition is the mechanism · 3. Error and result are alternatives, and both are responses

### Diagram 80 — Build a Conformance Matrix

A table. One row per requirement, five columns: REQUIREMENT → HAPPY PATH → NEGATIVE TEST → EVIDENCE → STATUS.

**Use it for:** Study Build a Conformance Matrix through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/80-conformance-matrix.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/80-conformance-matrix.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=80)

**Inside:** 1. Every requirement gets a row, and the identifier is the spine · 2. Happy path and negative test are separate columns, and both are required · 3. The teal return arrow connects negative back to happy, and that is a sequencing claim

### Diagram 81 — Stateless HTTP Routing

A request carrying VERSION, CLIENT INFO, CAPABILITIES in its body and MCP-METHOD, MCP-NAME in its headers reaches a router, which sends it to any of three interchangeable servers.

**Use it for:** Study Stateless HTTP Routing through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/81-stateless-http-routing.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/81-stateless-http-routing.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=81)

**Inside:** 1. Three things in the body make the request self-describing · 2. Two things in the headers make the request routable · 3. Three servers, and their interchangeability is the whole point

### Diagram 82 — Server Discovery and Negotiation

Two routes from the same client. The upper one discovers a server card describing what the server offers. The lower one sends a direct request carrying per-request metadata.

**Use it for:** Study Server Discovery and Negotiation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/82-server-discovery-negotiation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/82-server-discovery-negotiation.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=82)

**Inside:** 1. The server card carries four things, and they are not interchangeable · 2. Discovery is episodic; the direct request is per-call · 3. Both paths reach the same validation, and that is the structural claim

### Diagram 83 — MCP Primitives at Catalogue Scale

The top half restates the three primitives with their verbs: TOOLS → EXECUTE, RESOURCES → READ CONTEXT, PROMPTS → REUSABLE TEMPLATE.

**Use it for:** Study MCP Primitives at Catalogue Scale through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/83-mcp-primitives-catalog-scale.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/83-mcp-primitives-catalog-scale.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=83)

**Inside:** 1. Three primitives, three verbs, and the verbs are the definitions · 2. All three return to the server, and the teal arrows say the server owns them · 3. The catalogue pipeline exists because listing everything stops working

### Diagram 84 — Cache, Subscription, Extension, and Deprecation Policy

Four things a server must have a stated policy about: caching, subscriptions, extensions, and deprecation. All four pass through one POLICY GATE and produce four corresponding outcomes.

**Use it for:** Study Cache, Subscription, Extension, and Deprecation Policy through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/84-cache-subscription-extension-policy.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/84-cache-subscription-extension-policy.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=84)

**Inside:** 1. Cache policy is two values, and both are required · 2. Subscription policy means declaring event types, not just offering a stream · 3. Extension IDs use reverse-domain names, and the examples are shown

### Diagram 85 — Multi Round-Trip Requests and Input Required

A tool request returns RESULT TYPE INPUT REQUIRED rather than a result. Questions go to a human. The human's answers, plus the REQUEST STATE the server had accumulated, are carried by the ORIGINAL CALL (RETRY) — which produces the final result.

**Use it for:** Study Multi Round-Trip Requests and Input Required through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/85-mrtr-input-required-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/85-mrtr-input-required-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=85)

**Inside:** 1. INPUT REQUIRED is a result type, not an error · 2. The questions are numbered and plural · 3. REQUEST STATE is what the server had established before it paused

### Diagram 86 — The MCP Tasks Extension Lifecycle

A TASK HANDLE at the centre — drawn as a padlock over a gear — with five states around it and three control operations entering from the edges: TASKS GET, TASKS UPDATE, TASKS CANCEL.

**Use it for:** Study The MCP Tasks Extension Lifecycle through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/86-mcp-tasks-extension-lifecycle.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/86-mcp-tasks-extension-lifecycle.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=86)

**Inside:** 1. The handle is a lock and a gear, and both halves are meaningful · 2. CREATE FROM CALL is how tasks come into existence · 3. Three control operations enter from outside the ring

### Diagram 87 — Delivery Mechanism Map

DURABLE TASK STATE on the left. Four delivery mechanisms in the middle. FINAL GET TASK on the right — and every one of the four converges on it.

**Use it for:** Study Delivery Mechanism Map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/87-delivery-mechanism-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/87-delivery-mechanism-map.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=87)

**Inside:** 1. Durable task state is the source, and all four are derived · 2. Each mechanism carries a qualifying phrase, and the phrases are the design content · 3. The four paired cards show what each mechanism actually delivers

### Diagram 88 — MCP Apps, Sandbox, and Consent

A host prefetches and reviews something, runs it in a sandboxed iframe, gates its actions behind user consent, and lets it perform a tool action — while two coral dashed arrows run from that action toward SECRETS and NETWORK.

**Use it for:** Study MCP Apps, Sandbox, and Consent through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/88-mcp-apps-sandbox-consent.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/88-mcp-apps-sandbox-consent.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=88)

**Inside:** 1. Prefetch and review happens before anything runs · 2. The sandbox is drawn as a dashed boundary inside a browser window · 3. User consent is a gate between the sandbox and any action

### Diagram 89 — A2A Agent Card and Trust

An agent card explodes into seven sections, of which exactly one — INTERFACES, highlighted with a blue outline — feeds the TRUST POLICY.

**Use it for:** Study A2A Agent Card and Trust through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/89-a2a-agent-card-trust.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/89-a2a-agent-card-trust.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=89)

**Inside:** 1. Seven sections, and they serve different consumers · 2. Skills and capabilities are separate, and conflating them is a real error · 3. Only INTERFACES feeds the trust policy, and the highlight says so

### Diagram 90 — Message, Task, and Artifact Anatomy

PARTS — text, file, data — compose into a TASK carrying three fields: TASK ID, CONTEXT ID, STATUS.

**Use it for:** Study Message, Task, and Artifact Anatomy through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/90-a2a-message-task-artifact-anatomy.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/90-a2a-message-task-artifact-anatomy.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=90)

**Inside:** 1. Parts are typed, and the three types are not interchangeable · 2. TASK ID and CONTEXT ID are two identifiers with two scopes · 3. Status is a field on the task, not a separate object

### Diagram 91 — Stream, Push, Poll, and Cancel

Three update paths from one task. Two terminal outcomes. And between those two outcomes, a coral RACE label with a double-headed arrow.

**Use it for:** Study Stream, Push, Poll, and Cancel through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/91-a2a-stream-push-cancel.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/91-a2a-stream-push-cancel.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=91)

**Inside:** 1. Three update paths, and they can run concurrently · 2. Each path carries a different payload shape · 3. CANCEL is coral and it bypasses the update paths entirely

### Diagram 92 — Bindings, Version, and Security Schemes

One CANONICAL A2A MODEL at the centre, fed by two headers, expressed through three bindings — JSON-RPC, gRPC, HTTP+JSON — all verified by one FUNCTIONAL EQUIVALENCE TESTS banner.

**Use it for:** Study Bindings, Version, and Security Schemes through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/92-a2a-bindings-version-security.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/92-a2a-bindings-version-security.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=92)

**Inside:** 1. The canonical model is at the centre, and everything else is derived · 2. Version and extensions are headers on the model, not on the bindings · 3. Three bindings, and their differences are real

### Diagram 93 — Typed Event Lifecycle

A stream from RUN STARTED to RUN FINISHED, with three grouped bands in between — a step, a text message, a tool call — each band's events tied together by a shared identifier: S1, M1, T1.

**Use it for:** Study Typed Event Lifecycle through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/93-agui-typed-event-lifecycle.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/93-agui-typed-event-lifecycle.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=93)

**Inside:** 1. Events come in start-and-end pairs, and the pairing is explicit · 2. The identifiers are what make concurrency survivable · 3. The three group types have different internal shapes

### Diagram 94 — Snapshot, Delta, and Replay

A STATE SNAPSHOT carrying "version": 42, followed by RFC 6902 patches that transform it. A NETWORK BREAK. Then RECONNECT → MESSAGES SNAPSHOT → REPLAY FROM SEQUENCE → DEDUPLICATE → CONSISTENT UI.

**Use it for:** Study Snapshot, Delta, and Replay through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/94-agui-snapshot-delta-replay.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/94-agui-snapshot-delta-replay.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=94)

**Inside:** 1. The snapshot is complete and versioned, and both properties are load-bearing · 2. The deltas are RFC 6902, and naming the standard matters · 3. The fourth patch updates the version, and that is the whole protocol

### Diagram 95 — Interrupt, Approval, and Steering

A run finishes. Its outcome is an INTERRUPT. That interrupt produces interrupt cards which become a DRAFT CONTRACT, reviewed by a human, and resumed as a NEW RUN carrying a PARENT RUN ID.

**Use it for:** Study Interrupt, Approval, and Steering through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/95-agui-interrupt-approval-steering.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/95-agui-interrupt-approval-steering.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=95)

**Inside:** 1. RUN FINISHED comes before OUTCOME INTERRUPT, and the ordering is the design · 2. PARENT RUN ID appears twice, and it is the thread · 3. The DRAFT CONTRACT is amber, is the widest object in the frame, and is the heart of the diagram

### Diagram 96 — Tool, Artifact, and Recovery Surfaces

The four cards are the surfaces. The equation is the rule that governs the fourth one's buttons, and it is stated as an equation because it admits no exceptions.

**Use it for:** Study Tool, Artifact, and Recovery Surfaces through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/96-agui-tool-artifact-recovery.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/96-agui-tool-artifact-recovery.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=96)

**Inside:** 1. One reducer, four surfaces — state derived once · 2. The first two cards look the same and mean different things · 3. ARTIFACT READY has a different button, and the difference is the point

### Diagram 97 — Protocol Boundary Decision Tree

One question — WHO OWNS THE OTHER SIDE — with four answers, each producing a different protocol. And beneath all four, a coral banner: DO NOT STACK PROTOCOLS WITHOUT A REAL BOUNDARY.

**Use it for:** Study Protocol Boundary Decision Tree through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/97-protocol-boundary-decision-tree.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/97-protocol-boundary-decision-tree.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=97)

**Inside:** 1. The question is about ownership, and it is the only question · 2. Four answers, and the first one is the most important · 3. APP TO CAPABILITY SERVER → MCP

### Diagram 98 — Adapters, Correlation, and Contract Maps

An orchestrator drives two adapters — one for MCP, one for A2A — each translating through a CONTRACT MAP into a different protocol.

**Use it for:** Study Adapters, Correlation, and Contract Maps through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/98-adapter-correlation-contract.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/98-adapter-correlation-contract.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=98)

**Inside:** 1. The orchestrator is a segmented cube, and the segmentation is apt · 2. Five identifiers, five scopes, and they are not interchangeable · 3. The spine feeds both adapters, and that is the whole point of drawing it

### Diagram 99 — ACP to A2A Migration

Five old terms on the left under HISTORY ACP (HISTORICAL). Five current terms on the right under CURRENT TARGET A2A 1.0.

**Use it for:** Study ACP to A2A Migration through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 04/diagram-docs/99-acp-to-a2a-migration.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2004/diagram-docs/99-acp-to-a2a-migration.md) · [Website reader](https://course.ketanshukla.dev/#course=04&chapter=99)

**Inside:** 1. Five mappings, and two of them are more than renames · 2. HISTORICAL in coral is a status, not a judgement · 3. The strangler bridge is a pattern with a name, and the name is the point

<a id="course-05"></a>

## Visual Course Volume 5 — Knowledge Systems and Advanced RAG

Build permission-aware, fresh, explainable, and measurable evidence systems.

### Diagram 101 — Source Inventory, Authority, Ownership, and Purpose

Four different kinds of source feed a SOURCE REGISTER. Every one carries the same five fields: OWNER, AUTHORITY, PURPOSE, REFRESH, SENSITIVITY.

**Use it for:** Study Source Inventory, Authority, Ownership, and Purpose through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/101-source-authority-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/101-source-authority-map.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=101)

**Inside:** 1. Five fields, and each answers a question that has consequences later · 2. The same five fields appear on every source and on the register · 3. The four source types are chosen to be maximally different

### Diagram 102 — Layout-Aware Parsing

Upward through a LAYOUT PARSER into a DOCUMENT TREE, where every node keeps four properties: PAGE, BOUNDING BOX, PARENT, ORDER.

**Use it for:** Study Layout-Aware Parsing through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/102-layout-aware-parsing.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/102-layout-aware-parsing.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=102)

**Inside:** 1. Five region types, and each behaves differently under extraction · 2. Four properties per node, and each enables something specific · 3. The document tree is a tree, and the parent column is why

### Diagram 103 — OCR, Images, Attachments, and Multimodal Evidence

Three visual input types feed two different processing paths — one that reads text out of images, one that embeds the image itself — and both converge on a MULTIMODAL EVIDENCE record carrying five fields.

**Use it for:** Study OCR, Images, Attachments, and Multimodal Evidence through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/103-multimodal-evidence-intake.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/103-multimodal-evidence-intake.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=103)

**Inside:** 1. Two processing paths, and they are complementary rather than alternative · 2. Charts are the case that justifies visual embedding · 3. Five fields, and the first four are the citation chain

### Diagram 104 — Provenance, Permission, and Retention

Original, parse, chunk — and then a seven-field evidence record that everything downstream depends on: SOURCE ID, VERSION ID, TENANT, ACL, VALID FROM, RETAIN UNTIL, HASH.

**Use it for:** Study Provenance, Permission, and Retention through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/104-provenance-permission-retention.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/104-provenance-permission-retention.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=104)

**Inside:** 1. Seven fields, and they answer three different kinds of question · 2. The record sits after CHUNK and before the gate, and that ordering is load-bearing · 3. HASH is the field that makes the others trustworthy

### Diagram 105 — Semantic Chunk Boundaries

A policy document, decomposed into its structural elements, fed to a SEMANTIC CHUNKER, producing chunks that each carry a HEADING PATH and a PAGE SPAN.

**Use it for:** Study Semantic Chunk Boundaries through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/105-semantic-chunk-boundaries.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/105-semantic-chunk-boundaries.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=105)

**Inside:** 1. Chunking operates on structure, not on characters · 2. HEADING PATH is carried on every chunk, and it is what makes a chunk interpretable alone · 3. PAGE SPAN is a range, and ranges rather than points is the honest representation

### Diagram 106 — Parent-Child Retrieval

Three levels of granularity — DOCUMENT, SECTION, CHILD CHUNKS — with one child highlighted and a teal arrow labelled EXPAND TO PARENT running up to its section.

**Use it for:** Study Parent-Child Retrieval through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/106-parent-child-retrieval.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/106-parent-child-retrieval.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=106)

**Inside:** 1. Three levels, and each is good at something different · 2. The highlighted child and the highlighted section are the mechanism · 3. The search line enters at the section level, and that is worth reading carefully

### Diagram 107 — Complementary Representations

Each has a labelled match type — EXACT MATCH, SEMANTIC MATCH, LATE INTERACTION — and each is annotated with what it is good at: ERROR CODE, REFUND MEANING, TERM ALIGNMENT.

**Use it for:** Study Complementary Representations through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/107-complementary-representations.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/107-complementary-representations.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=107)

**Inside:** 1. Three representations of the same chunk, not three different chunks · 2. The visual encoding of each representation tells you its shape · 3. ERROR CODE is what lexical search wins

### Diagram 108 — Tenant-Safe Index Design

Two tenants, one QUERY ROUTER, two mirrored index partitions. The router carries a shield and is fed from above by a SERVER-TRUSTED TENANT ID.

**Use it for:** Study Tenant-Safe Index Design through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/108-tenant-safe-index-design.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/108-tenant-safe-index-design.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=108)

**Inside:** 1. SERVER-TRUSTED TENANT ID enters from above, not from the tenants · 2. The two partitions are drawn identically, and identical means separate · 3. Each partition holds three things, and they serve different query types

### Diagram 109 — Query Understanding and Plan

A question is decomposed into five things — INTENT, ENTITIES, FILTERS, TIME, AMBIGUITY — and those five determine which of four actions to take: DIRECT QUERY, REWRITE, DECOMPOSE, CLARIFY.

**Use it for:** Study Query Understanding and Plan through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/109-query-understanding-plan.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/109-query-understanding-plan.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=109)

**Inside:** 1. Five extractions, and each one changes what you search for · 2. TIME is a first-class extraction, and its presence here is unusual · 3. Four actions, and they are responses to different findings

### Diagram 110 — Hybrid Candidate Funnel

Three search channels — LEXICAL, DENSE, OPTIONAL SPECIALIST — each producing a ranked list, fused by RRF, deduplicated, and reduced to a CANDIDATE POOL 60.

**Use it for:** Study Hybrid Candidate Funnel through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/110-hybrid-candidate-funnel.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/110-hybrid-candidate-funnel.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=110)

**Inside:** 1. The third channel is labelled OPTIONAL, and that word is doing work · 2. Each channel produces the same shape, which is what makes fusion possible · 3. RRF is named, and naming it rules out the alternative

### Diagram 111 — Authorization Before Search

From that scope, two things happen simultaneously. Four coral arrows carry exclusions: WRONG TENANT, RESTRICTED, EXPIRED, RETENTION HOLD. And three teal arrows descend to three filtered indexes.

**Use it for:** Study Authorization Before Search through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/111-authorization-before-search.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/111-authorization-before-search.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=111)

**Inside:** 1. ALLOWED SCOPE is computed once and applied everywhere · 2. All three indexes are labelled FILTERED, and the repetition is the point · 3. FILTERED SQL is included, and structured data is where filtering is most often forgotten

### Diagram 112 — Rerank, Diversity, and the Evidence Packet

Sixty candidates through five stages — RERANKER, DEDUPLICATE, DIVERSIFY, AUTHORITY CHECK, TOKEN BUDGET — producing an EVIDENCE PACKET with four labelled types.

**Use it for:** Study Rerank, Diversity, and the Evidence Packet through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/112-rerank-diversity-evidence-pack.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/112-rerank-diversity-evidence-pack.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=112)

**Inside:** 1. Five stages, and each removes candidates for a different reason · 2. DEDUPLICATE and DIVERSIFY are different operations · 3. AUTHORITY CHECK is a teal shield, and it is where the source register pays off

### Diagram 113 — Bounded Multi-Hop Retrieval

Three hops, each with a name describing what it is looking for, each producing two things: EVIDENCE and a NEXT QUERY.

**Use it for:** Study Bounded Multi-Hop Retrieval through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/113-bounded-multihop-retrieval.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/113-bounded-multihop-retrieval.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=113)

**Inside:** 1. Each hop has a purpose, not a number · 2. Each hop produces two outputs, and the second is what makes it multi-hop · 3. Four stop conditions, and they catch four different failures

### Diagram 114 — Graph Relationship Retrieval

Text becomes a graph of entities and relationships, and that graph serves two query types: LOCAL SEARCH and GLOBAL THEMES.

**Use it for:** Study Graph Relationship Retrieval through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/114-graphrag-relationship-retrieval.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/114-graphrag-relationship-retrieval.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=114)

**Inside:** 1. Edges carry source spans, and the small circles on them say so · 2. The unsourced edge is drawn as coral and dashed, and it is removed · 3. Five entity types, and their relationships are the domain

### Diagram 115 — Structured and Federated Retrieval

A query plan reaches three completely different sources — a document search, a SQL database, an HTTP API — and each returns through an identical EVIDENCE ADAPTER carrying five fields: VALUE, SOURCE, AS OF, AUTHORITY, CITATION.

**Use it for:** Study Structured and Federated Retrieval through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/115-structured-federated-retrieval.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/115-structured-federated-retrieval.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=115)

**Inside:** 1. The three sources are deliberately heterogeneous · 2. The adapters are drawn identically, and that is the normalisation claim · 3. Five fields, and they map onto the governance work from the start of the volume

### Diagram 116 — Agentic Retrieval and the Budget Loop

Four stages in a loop — PLAN, SEARCH, INSPECT EVIDENCE, DECIDE — with a teal shield at the centre connected to all four.

**Use it for:** Study Agentic Retrieval and the Budget Loop through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/116-agentic-retrieval-budget-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/116-agentic-retrieval-budget-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=116)

**Inside:** 1. The shield at the centre governs every stage · 2. PLAN carries a chess knight, and the glyph is apt · 3. Five budget dimensions, and they exhaust independently

### Diagram 117 — Immutable Source Versions

Two rows, structurally identical. V7 ingests to a version record and fans out to its own parse, chunks and index. V8 does the same, separately.

**Use it for:** Study Immutable Source Versions through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/117-immutable-source-versions.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/117-immutable-source-versions.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=117)

**Inside:** 1. Four fields on the version record, and each answers a different question · 2. FETCHED AT and VALID FROM are different clocks, and the record carries both · 3. Each version fans out to its own parse, chunks and index

### Diagram 118 — Incremental Ingestion and Reconciliation

Above: source changes — create, update, delete — captured, queued, and applied as four operations.

**Use it for:** Study Incremental Ingestion and Reconciliation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/118-incremental-change-capture.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/118-incremental-change-capture.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=118)

**Inside:** 1. Three change types, and DELETE is drawn in red · 2. The work queue is IDEMPOTENT and RETRY-SAFE, and both words are on the diagram · 3. Four operations, and their separation is what makes incremental work incremental

### Diagram 119 — Safe Index Promotion

INDEX BLUE V7 is live. INDEX GREEN V8 is being built. Between them, a RELEASE GATE with six checks, and an ATOMIC PROMOTE arrow.

**Use it for:** Study Safe Index Promotion through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/119-safe-index-promotion.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/119-safe-index-promotion.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=119)

**Inside:** 1. The alias is what is live, not the index · 2. Blue and green are peers, not old and new · 3. Six checks, and they cover four different concerns

### Diagram 120 — Temporal Retrieval

Two timelines. BUSINESS TIME (EFFECTIVE TIME) carries policy versions with valid-from and valid-to dates. SYSTEM TIME (RECORD TIME) carries timestamps of when each was recorded.

**Use it for:** Study Temporal Retrieval through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/120-as-of-time-retrieval.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/120-as-of-time-retrieval.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=120)

**Inside:** 1. Business time and system time are genuinely different · 2. The valid-from and valid-to pairs are non-overlapping and contiguous · 3. The query is dated, and the date does the selection

### Diagram 121 — Claim-to-Source Citation Lineage

Three claims, each traced across five columns: EVIDENCE SPANS → CHUNK → SOURCE VERSION → ORIGINAL PAGE → OWNER.

**Use it for:** Study Claim-to-Source Citation Lineage through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/121-claim-citation-lineage.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/121-claim-citation-lineage.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=121)

**Inside:** 1. Five columns, and each removes a different kind of doubt · 2. Claims 2 and 3 share a chunk, and the diagram shows it · 3. The version hash appears alongside the version number

### Diagram 122 — Evidence Conflict and Abstention

Two pieces of evidence that disagree: Policy V8 recommends allow; Case Note V7 recommends deny. Both scoped to internal tools.

**Use it for:** Study Evidence Conflict and Abstention through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/122-conflict-uncertainty-abstention.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/122-conflict-uncertainty-abstention.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=122)

**Inside:** 1. The conflicting evidence is scoped identically, which is what makes it a real conflict · 2. The version numbers differ, and that is the first resolution to try · 3. CONFLICT DETECTED says the disagreement REMAINS EXPOSED

### Diagram 123 — Layered RAG Evaluation

A GOLDEN QUERY SET with six named categories feeds two separate dashboards — RETRIEVAL and GENERATION — whose metrics are compared BASELINE against CANDIDATE, producing PASS or HOLD.

**Use it for:** Study Layered RAG Evaluation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/123-rag-evaluation-dashboard.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/123-rag-evaluation-dashboard.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=123)

**Inside:** 1. Six query categories, and each exercises a different capability · 2. PERMISSION as a query category is the unusual one · 3. Two dashboards, and their metrics do not overlap

### Diagram 124 — Acme Knowledge Fabric Capstone

Six numbered columns, twenty-eight stages, and a red hexagonal cross hanging off nearly every one of them.

**Use it for:** Study Acme Knowledge Fabric Capstone through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 05/diagram-docs/124-acme-knowledge-fabric.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2005/diagram-docs/124-acme-knowledge-fabric.md) · [Website reader](https://course.ketanshukla.dev/#course=05&chapter=124)

**Inside:** 1. Six columns, and they are the volume's structure · 2. Nearly every stage has a red cross, and that is the honest picture · 3. AUTHORIZE is highlighted, and it is the only stage drawn that way

<a id="course-06"></a>

## Visual Course Volume 6 — Durable Orchestration and Multi-Agent Workflows

Design queues, sagas, A2A delegation, and recovery so agent work survives failure.

### Diagram 125 — State Layer Map

Four lanes, each with its own ID, OWNER, LIFETIME and STORE. Each running the same seven-stage sequence. Each with its own failure path.

**Use it for:** Study State Layer Map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/125-state-layer-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/125-state-layer-map.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=125)

**Inside:** 1. Four state layers, and they answer four different questions · 2. The four fields on every lane are what make them distinct · 3. The seven stages repeat identically in every lane, and that is deliberate

### Diagram 126 — Commands, Events, Invariants, and State

A command is validated against invariants. Valid, it becomes an event, is appended to history, and is reduced into state. Invalid, it is rejected — and a red X cuts the path to the state, labelled STATE UNCHANGED (OPEN REMAINS).

**Use it for:** Study Commands, Events, Invariants, and State through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/126-command-event-state-machine.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/126-command-event-state-machine.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=126)

**Inside:** 1. Four object types, and confusing any two is a design error · 2. Validation happens before the event exists, and that ordering is everything · 3. APPEND-ONLY is the property that makes history a fact

### Diagram 127 — Snapshot, Replay, and Schema Evolution

Above it, CODE V1 and CODE V2 both feeding a VERSION GATE — because the events being replayed were written by one version of the code and are being read by another.

**Use it for:** Study Snapshot, Replay, and Schema Evolution through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/127-snapshot-replay-schema-evolution.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/127-snapshot-replay-schema-evolution.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=127)

**Inside:** 1. Snapshot plus replay is the answer to replay cost · 2. The snapshot carries a green check, and the check is a claim · 3. Both code versions feed the version gate, and that is the real problem

### Diagram 128 — Durable Artifacts, Receipts, and Business Records

Three different glyphs — a document, a receipt, a database — and beside each, the same six fields: ID, VERSION, HASH, ACTOR, TIME, CORRELATION.

**Use it for:** Study Durable Artifacts, Receipts, and Business Records through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/128-artifact-receipt-business-record.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/128-artifact-receipt-business-record.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=128)

**Inside:** 1. Three outputs, and each one proves a different kind of thing · 2. Six identical fields, and their identity is the contract · 3. HASH is the field that makes the other five worth having

### Diagram 129 — Queues, Workers, Leases, Acknowledgements, and Visibility

The arrow from the queue to the worker is dashed: the delivery creates a LEASE / VISIBILITY WINDOW.

**Use it for:** Study Queues, Workers, Leases, Acknowledgements, and Visibility through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/129-queue-lease-ack-visibility.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/129-queue-lease-ack-visibility.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=129)

**Inside:** 1. Four stages, and the order is the contract · 2. The queue is durable, the worker is not, and the lease is what bridges them · 3. A lease is a visibility window, and the dashed arrow is what it looks like

### Diagram 130 — Backpressure, Rate Limits, Admission Control, and Priorities

A REQUEST FLOOD of white cubes meets a tall blue ADMISSION GATE. Inside the gate, four checks: CAPACITY, TENANT LIMIT, PRIORITY, DEADLINE.

**Use it for:** Study Backpressure, Rate Limits, Admission Control, and Priorities through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/130-backpressure-admission-priority.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/130-backpressure-admission-priority.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=130)

**Inside:** 1. There are four reasons to reject work, and they live in one gate · 2. The gate is an honest promise, and that is why it comes first · 3. Three lanes, and the worker pools are different sizes on purpose

### Diagram 131 — Retries, Idempotency Keys, Deduplication, and Poison Work

If NO RECEIPT FOUND, the work is processed. In ATTEMPT 1, the work times out and loops back. In ATTEMPT 2, the work fails permanently, hits the RETRY BUDGET, and when the budget is exhausted, goes to POISON / DEAD LETTER.

**Use it for:** Study Retries, Idempotency Keys, Deduplication, and Poison Work through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/131-retry-idempotency-poison-work.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/131-retry-idempotency-poison-work.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=131)

**Inside:** 1. A retry is a second attempt, not a second intention · 2. The idempotency key must be generated before the first side effect · 3. CHECK DEDUP STORE is the first step of every attempt

### Diagram 132 — Deadlines, Cancellation, Timeout, and Compensation

From the left, two inputs: USER CANCEL and TIMER → TIMEOUT. Both send dashed arrows into the steps.

**Use it for:** Study Deadlines, Cancellation, Timeout, and Compensation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/132-deadline-cancel-timeout-compensation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/132-deadline-cancel-timeout-compensation.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=132)

**Inside:** 1. Four different concepts, and conflating them is the most expensive mistake · 2. The deadline travels with the work, and the point of no return is derived from it · 3. Cancellation is a request, and a request can be refused

### Diagram 133 — Orchestration versus Choreography

Orchestration: one COORDINATOR sends COMMANDS to POLICY, FINANCE, NOTIFY, and receives RESULTS.

**Use it for:** Study Orchestration versus Choreography through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/133-orchestration-vs-choreography.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/133-orchestration-vs-choreography.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=133)

**Inside:** 1. Commands and events are different messages with different owners · 2. Orchestration gives a global view at the cost of coupling · 3. Choreography gives loose coupling at the cost of a partial view

### Diagram 134 — Parallel Work, Fan-Out, Fan-In, and Joins

The diagram is not about starting work in parallel. It is about knowing when to stop waiting and continue.

**Use it for:** Study Parallel Work, Fan-Out, Fan-In, and Joins through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/134-fan-out-fan-in-join.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/134-fan-out-fan-in-join.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=134)

**Inside:** 1. Four branches, but one parent owns the join · 2. The join gate is the contract, and it has four dimensions · 3. REQUIRED ALL is the default, and it is dangerous when misused

### Diagram 135 — Sagas, Compensations, and Irreversible Effects

The first two steps are compensable. Under each, a coral dashed arrow drops to a compensation: RELEASE FUNDS, RESTORE CASE.

**Use it for:** Study Sagas, Compensations, and Irreversible Effects through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/135-saga-compensation-irreversible-effects.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/135-saga-compensation-irreversible-effects.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=135)

**Inside:** 1. A saga is not a distributed transaction · 2. Compensable steps record their own counteractions · 3. The pivot is the boundary between reversible and irreversible

### Diagram 136 — Scheduled, Event-Triggered, and Externally Resumed Work

SCHEDULE TIMER — a calendar with a clock. DOMAIN EVENT — an antenna. EXTERNAL CALLBACK — a globe.

**Use it for:** Study Scheduled, Event-Triggered, and Externally Resumed Work through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/136-schedule-event-external-resume.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/136-schedule-event-external-resume.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=136)

**Inside:** 1. There are three legitimate triggers, and they are not interchangeable · 2. Every trigger must pass the DEDUP + CORRELATION GATE · 3. Wait without worker is the point of the pattern

### Diagram 137 — Agent Roles, Skills, Contracts, and Capability Discovery

A POLICY FILTER selects the right card. The output is FINANCE SPECIALIST with a green check.

**Use it for:** Study Agent Roles, Skills, Contracts, and Capability Discovery through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/137-agent-role-capability-contract.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/137-agent-role-capability-contract.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=137)

**Inside:** 1. A role is why the agent exists, a skill is what it can do, and a card is the advertisement · 2. Agent Cards have six fields, and every field is a filter · 3. Discovery narrows candidates; policy selects one

### Diagram 138 — A2A Discovery, Delegation, and Task Creation

CLIENT AGENT resolves an AGENT CARD, then sends a MESSAGE with CONTEXT ID and REQUEST ID through the A2A INTERFACE to a REMOTE AGENT.

**Use it for:** Study A2A Discovery, Delegation, and Task Creation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/138-a2a-delegation-task-creation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/138-a2a-delegation-task-creation.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=138)

**Inside:** 1. Resolve the card first · 2. A message is the request, not the work · 3. Task ID is the durable identity of the remote work

### Diagram 139 — Ownership, Handoff, Artifacts, and Status Propagation

It DELEGATES A SCOPED TASK TO a FINANCE AGENT, with an INPUT ARTIFACT and an ACCEPTANCE CONTRACT.

**Use it for:** Study Ownership, Handoff, Artifacts, and Status Propagation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/139-ownership-handoff-artifact-status.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/139-ownership-handoff-artifact-status.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=139)

**Inside:** 1. Ownership and responsibility are not the same thing · 2. The case stays with the parent, and the shield is the point · 3. The handoff ledger is the delegation contract

### Diagram 140 — Aggregation, Disagreement, Escalation, and Final Authority

Three agents — POLICY, FINANCE, RISK — each produce a RESULT CARD: CLAIM, EVIDENCE, CONFIDENCE, LIMITS.

**Use it for:** Study Aggregation, Disagreement, Escalation, and Final Authority through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/140-aggregation-disagreement-final-authority.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/140-aggregation-disagreement-final-authority.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=140)

**Inside:** 1. Each result card has four fields, and they are not the same · 2. Aggregation is not synthesis · 3. Agreement and conflict must both be visible

### Diagram 141 — Planner, Executor, Reviewer, and Policy Roles

The planner proposes. The policy gate allows or denies. The executor acts. The reviewer checks.

**Use it for:** Study Planner, Executor, Reviewer, and Policy Roles through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/141-planner-executor-reviewer-policy.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/141-planner-executor-reviewer-policy.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=141)

**Inside:** 1. The user goal is not the plan · 2. The planner proposes, the policy gate permits · 3. The bounded plan is the contract for this execution

### Diagram 142 — Time, Cost, Token, Tool, and Retry Budgets

A PARENT BUDGET LEDGER has six columns: TIME, MONEY, TOKENS, TOOL CALLS, RETRIES, CONCURRENCY.

**Use it for:** Study Time, Cost, Token, Tool, and Retry Budgets through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/142-multi-dimensional-budget-ledger.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/142-multi-dimensional-budget-ledger.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=142)

**Inside:** 1. Six dimensions, not one · 2. Allocate means reserve, not share · 3. Every spend returns a receipt

### Diagram 143 — Human Interrupts, Approvals, and Missing Input

APPROVAL REQUEST — the workflow has a proposed action that needs human authorization. MISSING INPUT — the workflow needs a fact from a person. OPERATOR INTERRUPT — a person needs to stop or steer the workflow because of an incident.

**Use it for:** Study Human Interrupts, Approvals, and Missing Input through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/143-human-interrupt-approval-input.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/143-human-interrupt-approval-input.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=143)

**Inside:** 1. There are three reasons to wait for a human · 2. An approval request is a contract, not a blank cheque · 3. Missing input is a durable wait with a responsible responder

### Diagram 144 — Steering, Replanning, Invalidation, and Resume

The result is PLAN V2, which is POLICY CHECKED, then gets NEW BUDGET RESERVED, then RESUME.

**Use it for:** Study Steering, Replanning, Invalidation, and Resume through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/144-steering-replan-invalidate-resume.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/144-steering-replan-invalidate-resume.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=144)

**Inside:** 1. New input is an event, not a mutation · 2. Impact analysis separates valid from invalidated work · 3. Completed work stays valid only when its inputs and acceptance remain valid

### Diagram 145 — Races, Duplicates, Out-of-Order Events, and Stale State

RACE — two commands try to change the same state at the same time. DUPLICATE EVENT — the same event or command arrives twice. OUT OF ORDER — a later sequence arrives before an earlier one. STALE WRITE — a command is based on an old version of the state.

**Use it for:** Study Races, Duplicates, Out-of-Order Events, and Stale State through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/145-race-duplicate-order-stale-state.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/145-race-duplicate-order-stale-state.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=145)

**Inside:** 1. The four hazards are different · 2. Expected version catches stale writes and races · 3. Unique key catches duplicates

### Diagram 146 — Fault Injection and Agent Workflow Chaos Tests

Each cell is a hypothesis: if a crash happens before a commit, what is the expected invariant? Is it durable? Is there a receipt? Is there a metric? Is there a recovery path?

**Use it for:** Study Fault Injection and Agent Workflow Chaos Tests through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/146-chaos-test-matrix.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/146-chaos-test-matrix.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=146)

**Inside:** 1. Chaos testing needs a hypothesis, not random destruction · 2. The rows are the dangerous business boundaries · 3. The columns are the common failure modes

### Diagram 147 — Recovery Drills, Runbooks, Ownership, and Receipts

ALERT → TRIAGE → IDENTIFY WORKFLOW → FREEZE OR CONTINUE → RECONCILE EXTERNAL EFFECTS → REDRIVE OR COMPENSATE → VERIFY → CLOSE.

**Use it for:** Study Recovery Drills, Runbooks, Ownership, and Receipts through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/147-recovery-runbook-receipt-chain.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/147-recovery-runbook-receipt-chain.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=147)

**Inside:** 1. The runbook is an executable decision guide · 2. The owner is a named role, not a hero · 3. Access is scoped to the recovery role

### Diagram 148 — Capstone: The Acme Case Resolution Network

Maya submits a refund request. A case is created. A workflow starts. It fans out evidence and specialist tasks. It waits for human approval. It issues a payment. The payment times out, recovers, and completes once. Every step leaves a receipt, a checkpoint, and a trace.

**Use it for:** Study Capstone: The Acme Case Resolution Network through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 06/diagram-docs/148-acme-case-resolution-network.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2006/diagram-docs/148-acme-case-resolution-network.md) · [Website reader](https://course.ketanshukla.dev/#course=06&chapter=148)

**Inside:** 1. The case is the durable owner · 2. Intake is authenticated intent · 3. Workflow and event history is the durable record

<a id="course-07"></a>

## Visual Course Volume 7 — Agent Identity, Security, and Governance

Protect every identity, capability, data path, tenant, and consequential action.

### Diagram 149 — Assets, Identities, Trust Boundaries, Data Flows, and Owners

MAYA → ACME AGENT → IDENTITY GATE → POLICY GATE → CASE DATA / PAYMENT TOOL / SECRET VAULT / AUDIT EVIDENCE.

**Use it for:** Study Assets, Identities, Trust Boundaries, Data Flows, and Owners through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/149-asset-identity-trust-boundary-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/149-asset-identity-trust-boundary-map.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=149)

**Inside:** 1. A threat model is a picture, not a product list · 2. Assets are more than the language model and the database · 3. Identities exist at every hop, not just at login

### Diagram 150 — Attack paths, misuse cases, and unacceptable outcomes

A MALICIOUS VENDOR FILE is the attacker's starting point. It enters the CONTENT PARSER and tries to ride the agent toward its goal. From there the diagram shows four coral branches: SECRET ACCESS, PAYMENT REDIRECT, CROSS-TENANT SEARCH, and ATTACKER EGRESS.

**Use it for:** Study Attack paths, misuse cases, and unacceptable outcomes through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/150-attack-path-misuse-outcome-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/150-attack-path-misuse-outcome-map.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=150)

**Inside:** 1. An attack path is a story, not a vulnerability count · 2. A misuse case is a legitimate feature used badly · 3. The unacceptable outcome is the design target

### Diagram 151 — Prompt Injection and Instruction-Authority Hierarchy

A vertical AUTHORITY LADDER ranks SYSTEM POLICY above APPLICATION RULES, VERIFIED USER INTENT, APPROVED PLAN, and UNTRUSTED DATA. A MALICIOUS FILE tries to promote a secret, but the INSTRUCTION FIREWALL blocks it. A teal DATA FACTS path reaches tool arguments through safe reasoning and a policy check.

**Use it for:** Study Prompt Injection and Instruction-Authority Hierarchy through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/151-instruction-authority-hierarchy.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/151-instruction-authority-hierarchy.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=151)

**Inside:** 1. The authority ladder is a design problem, not a prompt-engineering trick · 2. Every input must carry an origin label · 3. System policy is the highest authority and it never comes from an uploaded file

### Diagram 152 — Data Exfiltration and Unsafe Side Effects

The dangerous path is the EXFILTRATION lane: MODEL OUTPUT, URL QUERY, TOOL ARGUMENT, LOG, and ARTIFACT all try to carry protected data toward an ATTACKER DESTINATION.

**Use it for:** Study Data Exfiltration and Unsafe Side Effects through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/152-exfiltration-side-effect-control.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/152-exfiltration-side-effect-control.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=152)

**Inside:** 1. Exfiltration and side effects are two different problems · 2. Every output channel is a trust boundary · 3. Classify data before it moves anywhere

### Diagram 153 — Authentication, Authorization, Delegation, and Impersonation

Maya, the Acme client, the Acme agent, the payment workload, and the payment resource are five different identity cards.

**Use it for:** Study Authentication, Authorization, Delegation, and Impersonation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/153-authentication-authorization-delegation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/153-authentication-authorization-delegation.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=153)

**Inside:** 1. Authentication is only the first gate · 2. Resolve every identity before deciding authority · 3. Authorization is a decision made in this exact context

### Diagram 154 — OAuth, OpenID Connect, Resource Metadata, and Audiences

The client first calls the MCP RESOURCE without a token. The resource answers with 401 UNAUTHORIZED and PROTECTED RESOURCE METADATA.

**Use it for:** Study OAuth, OpenID Connect, Resource Metadata, and Audiences through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/154-oauth-resource-audience-flow.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/154-oauth-resource-audience-flow.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=154)

**Inside:** 1. The resource, not the client, drives the authorization contract · 2. OpenID Connect and access tokens are different · 3. Discovery is the second step and must be SSRF-safe

### Diagram 155 — DPoP, Sender-Constrained Tokens, and Replay Resistance

CLIENT KEY → DPoP PROOF → AUTHORIZATION SERVER → KEY-BOUND TOKEN → MCP RESOURCE → ALLOWED REQUEST.

**Use it for:** Study DPoP, Sender-Constrained Tokens, and Replay Resistance through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/155-dpop-sender-token-replay.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/155-dpop-sender-token-replay.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=155)

**Inside:** 1. DPoP changes the bearer-token assumption · 2. The DPoP proof is a fresh, signed envelope over the request · 3. The authorization server binds the issued token to the public key

### Diagram 156 — Workload Identity, Token Exchange, and Agent Delegation

MAYA TOKEN → ACME POLICY → ACME AGENT. WORKLOAD IDENTITY + TRUST DOMAIN → ACME AGENT. SUBJECT AUTHORITY + ACTOR ID + TARGET AUDIENCE + NARROW SCOPE → TOKEN EXCHANGE → DELEGATED TOKEN → PAYMENT RESOURCE. DELEGATION RECEIPT. FULL USER TOKEN COPY BLOCKED.

**Use it for:** Study Workload Identity, Token Exchange, and Agent Delegation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/156-workload-identity-token-exchange.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/156-workload-identity-token-exchange.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=156)

**Inside:** 1. A user's token is a boundary credential, not a downstream API key · 2. The agent is a workload with its own identity · 3. Token exchange is a transformation, not a relay

### Diagram 157 — Least-privilege tool and capability design

READ CASE, EXTRACT INVOICE, QUOTE REFUND, and ISSUE BOUND REFUND are four separate, narrow capability cards.

**Use it for:** Study Least-privilege tool and capability design through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/157-least-privilege-capability-tools.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/157-least-privilege-capability-tools.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=157)

**Inside:** 1. Safe use must be the easiest use · 2. A tool is a typed contract, not a general API · 3. Least privilege is architecture, not a prompt instruction

### Diagram 158 — Policy as Code, Claims, Context, and Decision Receipts

A POLICY ENFORCEMENT POINT gathers SUBJECT, ACTOR, TENANT, RESOURCE, ACTION, DATA CLASS, DESTINATION, RISK, and APPROVAL.

**Use it for:** Study Policy as Code, Claims, Context, and Decision Receipts through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/158-policy-context-decision-receipt.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/158-policy-context-decision-receipt.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=158)

**Inside:** 1. Policy as code is versioned, reviewable logic · 2. Claims are what the system can prove · 3. Context is the current situation

### Diagram 159 — Step-up Authorization, Approval, and Transaction Binding

A PROPOSED REFUND card lists the fields that make the consequence real: TENANT, CASE, PAYEE, AMOUNT, CURRENCY, DESTINATION, and DATA.

**Use it for:** Study Step-up Authorization, Approval, and Transaction Binding through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/159-step-up-approval-transaction-binding.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/159-step-up-approval-transaction-binding.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=159)

**Inside:** 1. Step-up is a response to risk, not a constant burden · 2. Transaction binding turns approval into a specific promise · 3. The canonical transaction is built from authoritative data

### Diagram 160 — Secret Managers, Short-Lived Credentials, and Rotation

A WORKLOAD IDENTITY asks the CREDENTIAL BROKER for a credential, providing TARGET, PURPOSE, POLICY, and TTL.

**Use it for:** Study Secret Managers, Short-Lived Credentials, and Rotation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/160-secret-manager-short-lived-credentials.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/160-secret-manager-short-lived-credentials.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=160)

**Inside:** 1. The model usually needs the result, not the credential · 2. A credential broker makes the credential purpose-bound and short-lived · 3. Direct handoff from broker to adapter keeps the secret out of general code

### Diagram 161 — Tenant Isolation Through Every Data and Workflow Layer

TENANT A (blue lane) and TENANT B (violet lane) both move through the same stack: IDENTITY GATE → API → POLICY → DATABASE ROWS → VECTOR INDEX → WORKFLOW → TOOL → ARTIFACT → AUDIT.

**Use it for:** Study Tenant Isolation Through Every Data and Workflow Layer through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/161-tenant-isolation-data-workflow.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/161-tenant-isolation-data-workflow.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=161)

**Inside:** 1. A tenant is an owner identity, not just a customer label · 2. The tenant key must come from trusted identity, not from the request · 3. Isolation has to hold at every layer, not just the API

### Diagram 162 — Cache, Index, Queue, Artifact, and Telemetry Isolation

TRUSTED TENANT CONTEXT → CACHE KEY → VECTOR NAMESPACE → QUEUE ENVELOPE → ARTIFACT PATH → TRACE → METRIC → LOG VIEW.

**Use it for:** Study Cache, Index, Queue, Artifact, and Telemetry Isolation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/162-cache-index-queue-artifact-telemetry-isolation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/162-cache-index-queue-artifact-telemetry-isolation.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=162)

**Inside:** 1. Tenant isolation fails in the places you forget to check · 2. A cache key is a trust boundary · 3. Vector namespaces need tenant filters

### Diagram 163 — Sandboxed Code, Browser, File, and MCP App Execution

Four sandboxes run side by side: CODE VM, BROWSER SESSION, FILE WORKSPACE, and MCP APP IFRAME.

**Use it for:** Study Sandboxed Code, Browser, File, and MCP App Execution through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/163-sandbox-code-browser-file-mcp-app.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/163-sandbox-code-browser-file-mcp-app.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=163)

**Inside:** 1. A sandbox is a restricted execution environment, not just a container · 2. Input must be scanned and classified before execution · 3. Each sandbox carries the same seven limits

### Diagram 164 — Network Egress, Destination Allowlists, and DLP

AGENT TOOL REQUEST → EGRESS GATE → [DNS & IP, DESTINATION ALLOWLIST, METHOD, PATH TEMPLATE, TENANT, PURPOSE, DATA CLASS, PAYLOAD DLP, RATE] → ACME API or APPROVED PAYMENT API.

**Use it for:** Study Network Egress, Destination Allowlists, and DLP through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/164-network-egress-allowlist-dlp.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/164-network-egress-allowlist-dlp.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=164)

**Inside:** 1. Egress is a trust boundary, not an open door · 2. No raw URL from a model or document is fetched directly · 3. Logical connector names beat absolute URLs

### Diagram 165 — MCP server discovery, A2A Agent Cards, signatures, and trust decisions

MCP CLIENT → server/discover → MCP SERVER returns VERSION, CAPABILITIES, INSTRUCTIONS, and RESOURCES.

**Use it for:** Study MCP server discovery, A2A Agent Cards, signatures, and trust decisions through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/165-mcp-discovery-a2a-card-trust.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/165-mcp-discovery-a2a-card-trust.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=165)

**Inside:** 1. Discovery is a claim, not trust or authorization · 2. MCP server/discover is the new stateless handshake · 3. A2A Agent Cards are well-known metadata with optional signatures

### Diagram 166 — Dependency, Model, Prompt, Tool, and Configuration Provenance

A provenance graph lists the versioned, integrity-checked inputs that feed one Agent Execution.

**Use it for:** Study Dependency, Model, Prompt, Tool, and Configuration Provenance through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/166-execution-provenance-supply-chain.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/166-execution-provenance-supply-chain.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=166)

**Inside:** 1. Provenance is a graph, not a source commit · 2. Every high-impact action is attributable to an approved, versioned, integrity-checked set · 3. Pin the source and dependency lock

### Diagram 167 — Data Minimization, Retention, Consent, and Deletion

PERSONAL DATA → PURPOSE GATE → MINIMIZE → USE → STORE → SHARE → RETAIN → DELETE → VERIFY DELETION.

**Use it for:** Study Data Minimization, Retention, Consent, and Deletion through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/167-privacy-data-lifecycle.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/167-privacy-data-lifecycle.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=167)

**Inside:** 1. Privacy is a lifecycle, not a collection notice · 2. The purpose gate decides whether the data is allowed to enter · 3. Minimization removes fields before they reach the model, tool, or log

### Diagram 168 — Tamper-Evident Audit, Redaction, and Chain of Evidence

INPUT RECEIVED → IDENTITY VERIFIED → POLICY DECISION → TOOL DENIED → APPROVAL → ACTION → RECEIPT → REVIEW.

**Use it for:** Study Tamper-Evident Audit, Redaction, and Chain of Evidence through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/168-tamper-evident-audit-chain.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/168-tamper-evident-audit-chain.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=168)

**Inside:** 1. An audit trail is a security contract, not a confession · 2. Order matters: events form a chain, not a bag · 3. Every event is a structured record, not a free-text line

### Diagram 169 — The NIST AI Risk Loop in Plain English

The NIST AI Risk Management Framework becomes a living management cycle. GOVERN names owners, policies, and risk culture. MAP understands the use case, affected people, assets, and threats. MEASURE evaluates risk and controls with tests, metrics, red-team exercises, and an honest account of uncertainty. MANAGE prioritizes, treats, responds, and monitors. An EVIDENCE REPOSITORY and a REVIEW DATE…

**Use it for:** Study The NIST AI Risk Loop in Plain English through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/169-nist-ai-risk-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/169-nist-ai-risk-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=169)

**Inside:** 1. Govern is the starting posture, not the finish line · 2. Map turns vague worry into named context and impact · 3. Measure replaces opinion with evidence and uncertainty

### Diagram 170 — OWASP Agentic Top 10 Mapping and Red-Team Coverage

The diagram places ACME AGENT at the center and wraps it in ten OWASP Agentic risk categories: GOAL HIJACK, TOOL MISUSE, IDENTITY ABUSE, SUPPLY CHAIN, CODE EXECUTION, MEMORY POISONING, INSECURE AGENT COMMUNICATION, CASCADING FAILURE, HUMAN TRUST EXPLOITATION, and ROGUE AGENT.

**Use it for:** Study OWASP Agentic Top 10 Mapping and Red-Team Coverage through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/170-owasp-agentic-red-team-coverage.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/170-owasp-agentic-red-team-coverage.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=170)

**Inside:** 1. The OWASP Agentic Top 10 is a catalog, not a certificate · 2. Goal hijack: the objective must survive untrusted input · 3. Tool misuse: every tool call is a privileged action

### Diagram 171 — Roles, Exceptions, Escalation, Accountability, and Review

A GOVERNANCE TABLE maps every risk, control, evidence bundle, incident, exception, and deployment to the people who own, operate, review, approve, and answer for it.

**Use it for:** Study Roles, Exceptions, Escalation, Accountability, and Review through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/171-roles-exceptions-accountability-review.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/171-roles-exceptions-accountability-review.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=171)

**Inside:** 1. Accountability is a named role, not a vague job · 2. Every control needs at least five named roles · 3. The governance table is an operating model, not an org chart

### Diagram 172 — Capstone: Acme Secure Agent Gateway and Policy Center

MAYA + ACME OPERATORS → IDENTITY AND TENANT GATE → SECURE AGENT GATEWAY → INSTRUCTION AUTHORITY / POLICY DECISION / CAPABILITY BROKER / APPROVAL BINDING / SECRET BROKER / TENANT DATA PLANE / SANDBOX / EGRESS GATE / DISCOVERY TRUST / PROVENANCE / AUDIT EVIDENCE → SAFE REFUND + RECEIPT.

**Use it for:** Study Capstone: Acme Secure Agent Gateway and Policy Center through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 07/diagram-docs/172-acme-secure-agent-gateway-policy-center.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2007/diagram-docs/172-acme-secure-agent-gateway-policy-center.md) · [Website reader](https://course.ketanshukla.dev/#course=07&chapter=172)

**Inside:** 1. The gateway is a logical set of enforcement points, not one giant service · 2. Identity and tenant are the first gates · 3. Instruction authority lives in trusted channels

<a id="course-08"></a>

## Visual Course Volume 8 — Evaluation, Observability, and AgentOps

Prove quality, safety, latency, cost, and recovery before and after release.

### Diagram 173 — Traces, spans, logs, metrics, events, and resources

Observability means being able to ask useful questions about a running system from the evidence it produces. A trace follows one request or workflow across components. A span is one timed operation inside that trace, such as retrieval, policy evaluation, an MCP tool call, an A2A delegation, or model generation. A log is a timestamped record that explains a local event in detail. A metric combines…

**Use it for:** Study Traces, spans, logs, metrics, events, and resources through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/173-traces-spans-logs-metrics-events-resources.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/173-traces-spans-logs-metrics-events-resources.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=173)

**Inside:** 1. Choose the right telemetry signal for each question · 2. Start with one named user outcome and create or continue · 3. Create spans only for operations whose timing, status, or evidence

### Diagram 174 — Context propagation across MCP, A2A, AG-UI, HTTP, and queues

Preserve one explainable evidence chain across protocol and asynchronous boundaries without confusing trace identity with business identity.

**Use it for:** Study Context propagation across MCP, A2A, AG-UI, HTTP, and queues through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/174-context-propagation-protocols-queues.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/174-context-propagation-protocols-queues.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=174)

**Inside:** 1. Preserve one evidence chain across protocols and time · 2. Create one trace at the trusted entry point or validate · 3. Extract before work begins, create a correctly parented span,

### Diagram 175 — Privacy-safe telemetry and content capture policy

Design telemetry that answers operational questions without creating an uncontrolled copy of private application content.

**Use it for:** Study Privacy-safe telemetry and content capture policy through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/175-privacy-safe-telemetry-capture-policy.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/175-privacy-safe-telemetry-capture-policy.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=175)

**Inside:** 1. Design telemetry that answers questions without leaking content · 2. Inventory every · 3. Classify the field, choose allow, hash, redact, tokenize, aggregate, sample,

### Diagram 176 — Business outcomes, artifacts, receipts, and trace references

Connect technical telemetry to durable user and business evidence without treating a trace as the system of record.

**Use it for:** Study Business outcomes, artifacts, receipts, and trace references through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/176-business-outcomes-artifacts-receipts-traces.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/176-business-outcomes-artifacts-receipts-traces.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=176)

**Inside:** 1. Connect durable business records to execution traces · 2. Define the user goal, business state transitions, unacceptable outcomes, · 3. Create durable request, decision, effect, artifact, and user-receipt records

### Diagram 177 — The anatomy of a useful evaluation case

Write an evaluation case that can diagnose behavior and be rerun fairly after the system changes.

**Use it for:** Study The anatomy of a useful evaluation case through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/177-evaluation-case-anatomy.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/177-evaluation-case-anatomy.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=177)

**Inside:** 1. Write evaluation cases that diagnose behavior fairly · 2. Name the user goal, starting state, relevant context, and unacceptable · 3. Specify required evidence, permitted tools or effects, forbidden actions, artifact

### Diagram 178 — Deterministic contracts, schemas, and behavioral assertions

Use exact assertions for exact contracts and reserve probabilistic graders for qualities that truly require judgment.

**Use it for:** Study Deterministic contracts, schemas, and behavioral assertions through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/178-deterministic-contracts-behavioral-assertions.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/178-deterministic-contracts-behavioral-assertions.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=178)

**Inside:** 1. Use exact assertions and reserve graders for judgment · 2. List every requirement and ask whether an authoritative machine-readable fact · 3. Validate shapes and types with schemas before judging meaning

### Diagram 179 — Model graders, human rubrics, calibration, and disagreement

Treat graders as measuring instruments that need calibration, disagreement handling, and their own evaluation.

**Use it for:** Study Model graders, human rubrics, calibration, and disagreement through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/179-graders-humans-calibration-disagreement.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/179-graders-humans-calibration-disagreement.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=179)

**Inside:** 1. Treat graders as measuring instruments that need calibration · 2. Define one rubric dimension at a time with clear anchors, · 3. Create a human-reviewed calibration set containing representative, difficult, unsafe,

### Diagram 180 — Slices, denominators, confidence, variance, and significance

Read evaluation numbers honestly and find important failures hidden by averages or tiny denominators.

**Use it for:** Study Slices, denominators, confidence, variance, and significance through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/180-slices-denominators-confidence-variance.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/180-slices-denominators-confidence-variance.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=180)

**Inside:** 1. Read rates with denominators, slices, and honest uncertainty · 2. Report passed, failed, excluded, missing, and total eligible cases before · 3. Predefine slices tied to user groups, workflows, risks, data age,

### Diagram 181 — Intent, routing, and retrieval quality

Locate whether a bad answer began with misunderstanding, wrong routing, or weak evidence retrieval.

**Use it for:** Study Intent, routing, and retrieval quality through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/181-intent-routing-retrieval-quality.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/181-intent-routing-retrieval-quality.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=181)

**Inside:** 1. Measure intent, routing, and retrieval as separate stages · 2. Label the user intent, entities, constraints, ambiguity, and required clarification · 3. Record the expected route and compare it with the chosen

### Diagram 182 — Tool contracts, policy decisions, and business effects

Evaluate what the agent actually attempted and changed, not merely what it said it would do.

**Use it for:** Study Tool contracts, policy decisions, and business effects through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/182-tool-policy-business-effect-quality.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/182-tool-policy-business-effect-quality.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=182)

**Inside:** 1. Evaluate what the agent actually attempted and changed · 2. Compare expected and selected tool, declared capability, schema version, · 3. Assert policy decision, authority, tenant, approval, and transaction binding before

### Diagram 183 — Planning, delegation, synthesis, and groundedness

Measure whether multi-step agent work stays bounded, delegates appropriately, preserves constraints, and synthesizes grounded evidence.

**Use it for:** Study Planning, delegation, synthesis, and groundedness through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/183-planning-delegation-synthesis-groundedness.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/183-planning-delegation-synthesis-groundedness.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=183)

**Inside:** 1. Keep multi-step work bounded, delegated, and grounded · 2. Compare the plan with required steps, dependencies, constraints, budgets, approvals, · 3. Check specialist capability, authority, task scope, supplied context, deadline,

### Diagram 184 — User outcome, clarity, control, and recovery quality

Judge success from the user's real outcome and ability to understand, control, and recover from the system.

**Use it for:** Study User outcome, clarity, control, and recovery quality through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/184-user-outcome-control-recovery-quality.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/184-user-outcome-control-recovery-quality.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=184)

**Inside:** 1. Judge success from the user's real outcome and control · 2. Define the real user job, acceptable outcomes, unacceptable outcomes, · 3. Evaluate correctness, freshness, clarity, actionability, uncertainty, and evidence presentation separately.

### Diagram 185 — Latency budgets, percentiles, deadlines, and the slow tail

Design and measure end-to-end response time as a budget shared by stages rather than one unexplained average.

**Use it for:** Study Latency budgets, percentiles, deadlines, and the slow tail through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/185-latency-budget-percentiles-deadlines.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/185-latency-budget-percentiles-deadlines.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=185)

**Inside:** 1. Design latency as a budget shared across stages · 2. Define the user-visible deadline and separate first update, first evidence, · 3. Allocate a scenario budget to each stage plus network

### Diagram 186 — Token, retrieval, tool, specialist, storage, and cache costs

Explain where scenario cost comes from and compare cost with quality, latency, and user outcome instead of chasing one cheap request.

**Use it for:** Study Token, retrieval, tool, specialist, storage, and cache costs through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/186-agent-cost-ledger.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/186-agent-cost-ledger.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=186)

**Inside:** 1. Count the whole scenario cost per valuable outcome · 2. Inventory every billable or capacity-consuming stage and record usage quantity · 3. Attach route, feature, version, outcome, and environment using bounded dimensions

### Diagram 187 — Load, concurrency, queues, capacity, and saturation

Recognize when an agent system is out of capacity and prevent queues, fan-out, and retries from turning delay into an outage.

**Use it for:** Study Load, concurrency, queues, capacity, and saturation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/187-load-concurrency-queues-saturation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/187-load-concurrency-queues-saturation.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=187)

**Inside:** 1. Recognize saturation and prevent load from becoming an outage · 2. Describe realistic workload classes, route mix, request size, fan-out, think · 3. Measure arrival, concurrency, queue depth and age, service time, throughput,

### Diagram 188 — Graceful degradation, fallback, and admission control

Design predictable reduced-service modes that preserve safety and useful work when dependencies or capacity fail.

**Use it for:** Study Graceful degradation, fallback, and admission control through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/188-graceful-degradation-admission-control.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/188-graceful-degradation-admission-control.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=188)

**Inside:** 1. Design predictable fallbacks that preserve the safety floor · 2. Define the non-negotiable safety and quality floor that no degraded · 3. Create ordered service tiers with entry conditions, user-visible behavior, preserved

### Diagram 189 — Offline gates and reproducible evaluation runs

Make candidate comparisons repeatable enough that a release decision can be explained and rerun.

**Use it for:** Study Offline gates and reproducible evaluation runs through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/189-offline-gates-reproducible-evals.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/189-offline-gates-reproducible-evals.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=189)

**Inside:** 1. Make candidate comparisons repeatable before production · 2. Create a complete candidate manifest and verify every version · 3. Select a versioned eligible case set and controlled fixtures

### Diagram 190 — Shadow traffic, canaries, and side-by-side comparison

Use real workload evidence gradually while preventing duplicate or unsafe business effects.

**Use it for:** Study Shadow traffic, canaries, and side-by-side comparison through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/190-shadow-canary-side-by-side.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/190-shadow-canary-side-by-side.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=190)

**Inside:** 1. Use real workload evidence gradually and safely · 2. Define eligible traffic, privacy basis, exclusions, cohort, duration, and representativeness · 3. Run the candidate in a side-effect-free isolated shadow and compare

### Diagram 191 — Feature flags, version pinning, rollback, and kill switches

Control independent agent-system changes without creating an untraceable mixture of versions or an untested emergency switch.

**Use it for:** Study Feature flags, version pinning, rollback, and kill switches through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/191-feature-flags-version-pins-rollback.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/191-feature-flags-version-pins-rollback.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=191)

**Inside:** 1. Control version bundles without creating untraceable mixtures · 2. Resolve every behavior-changing component into one recorded version manifest · 3. Evaluate flags from governed non-sensitive context and record variant, reason,

### Diagram 192 — Protocol conformance, compatibility, and migration gates

Release protocol and schema changes only when supported combinations, expected rejection, and migration behavior are proved.

**Use it for:** Study Protocol conformance, compatibility, and migration gates through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/192-protocol-conformance-compatibility-migration.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/192-protocol-conformance-compatibility-migration.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=192)

**Inside:** 1. Release protocol and schema changes with proven compatibility · 2. Inventory supported client, server, protocol, binding, schema, card, extension, · 3. Create positive, negative, unknown-field, unsupported-capability, malformed, authorization, cancellation, and error

### Diagram 193 — Alerts, ownership, triage, and runbooks

Create alerts that lead a named person to a useful action instead of producing noise and dashboards nobody owns.

**Use it for:** Study Alerts, ownership, triage, and runbooks through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/193-alert-ownership-triage-runbook.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/193-alert-ownership-triage-runbook.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=193)

**Inside:** 1. Create alerts that lead to a useful action · 2. Define the user, business, safety, or observability condition that genuinely · 3. Choose page, ticket, or record behavior and name owner, severity,

### Diagram 194 — Red-team, chaos, abuse, and recovery exercises

Rehearse dangerous and disruptive conditions safely enough to prove controls and recovery before a real incident.

**Use it for:** Study Red-team, chaos, abuse, and recovery exercises through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/194-red-team-chaos-abuse-recovery.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/194-red-team-chaos-abuse-recovery.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=194)

**Inside:** 1. Rehearse dangerous conditions safely to prove recovery · 2. State the hypothesis, protected outcome, expected detection, containment, degradation, recovery, · 3. Authorize scope, environment, synthetic data, blast radius, affected identities, tools,

### Diagram 195 — Postmortems, corrective actions, and regression cases

Turn a serious failure into verified system improvement instead of a document that is filed and forgotten.

**Use it for:** Study Postmortems, corrective actions, and regression cases through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/195-postmortem-corrective-regression-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/195-postmortem-corrective-regression-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=195)

**Inside:** 1. Turn serious failures into verified permanent learning · 2. Build a factual timeline from business records, traces, alerts, changes, · 3. Describe impact and contributing technical, process, ownership, and decision conditions

### Diagram 196 — Capstone: the Acme Agent Quality Lab

Assemble a framework-neutral operating contract that can guide both future full-stack implementations.

**Use it for:** Study Capstone: the Acme Agent Quality Lab through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 08/diagram-docs/196-acme-agent-quality-lab.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2008/diagram-docs/196-acme-agent-quality-lab.md) · [Website reader](https://course.ketanshukla.dev/#course=08&chapter=196)

**Inside:** 1. Assemble a framework-neutral operating contract for agent quality · 2. Define user outcomes, unacceptable outcomes, owners, quality and safety rules · 3. Instrument the whole path with W3C context, OpenTelemetry signals, business

<a id="course-09"></a>

## Visual Course Volume 9 — Agentic Product Design and Human Control

Turn complex agent work into an understandable, accessible, and recoverable human experience.

### Diagram 197 — The event-driven interface mental model

Explain why an agent interface should render typed events and explicit state rather than guess meaning from chat text.

**Use it for:** Study The event-driven interface mental model through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/197-event-driven-interface-mental-model.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/197-event-driven-interface-mental-model.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=197)

**Inside:** 1. Agent Interface Is Not Merely A Chat Box With Animated · 2. Interface Must Not Inspect A Sentence For Phrases · 3. User-visible Outcome And The Interface Regions That Help The Person

### Diagram 198 — State snapshots, deltas, reducers, and conflict handling

Use snapshots and deltas without allowing missing or conflicting updates to silently corrupt the interface.

**Use it for:** Study State snapshots, deltas, reducers, and conflict handling through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/198-snapshots-deltas-reducers-conflicts.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/198-snapshots-deltas-reducers-conflicts.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=198)

**Inside:** 1. Snapshot Says, 'replace Your Current View Of This State · 2. Conflict Handling Must Be Explicit: Reject The Patch, Mark · 3. Validated Snapshot With Schema Version, State Revision, And Product Ownership

### Diagram 199 — Reconnect, replay, deduplication, and offline recovery

Design reconnect behavior that restores visible state without duplicating messages, actions, or business effects.

**Use it for:** Study Reconnect, replay, deduplication, and offline recovery through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/199-reconnect-replay-dedup-offline-recovery.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/199-reconnect-replay-dedup-offline-recovery.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=199)

**Inside:** 1. Streaming Interfaces Must Assume Disconnection · 2. Offline Input Should Be Classified · 3. Assign Each Stream Event A Stable ID And Monotonic Cursor

### Diagram 200 — Optimistic interface state versus authoritative business state

Use optimistic UI for responsiveness without pretending that a consequential business action already succeeded.

**Use it for:** Study Optimistic interface state versus authoritative business state through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/200-optimistic-versus-authoritative-state.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/200-optimistic-versus-authoritative-state.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=200)

**Inside:** 1. Optimistic State Is A Temporary Interface Prediction: The Screen Responds · 2. Successful Response Returns A Receipt Or New Authoritative Snapshot · 3. Classify The Proposed Interaction By Reversibility, Consequence, External Effect

### Diagram 201 — Progressive disclosure and observable stage labels

Design progress that answers what is happening, what is complete, what is waiting, and what the person can do next.

**Use it for:** Study Progressive disclosure and observable stage labels through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/201-progressive-disclosure-stage-labels.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/201-progressive-disclosure-stage-labels.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=201)

**Inside:** 1. Progress Is A Promise About State, Not Decoration · 2. Do Not Invent Percentages For Work Whose Size Is Unknown · 3. Small Stage Vocabulary From Observable Product Events And Durable Transitions

### Diagram 202 — Tool cards, evidence cards, artifacts, and receipts

Choose the right card for transient execution, supporting evidence, durable output, and proof of a decision or effect.

**Use it for:** Study Tool cards, evidence cards, artifacts, and receipts through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/202-tool-evidence-artifact-receipt-cards.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/202-tool-evidence-artifact-receipt-cards.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=202)

**Inside:** 1. It Is Not A Dump Of Telemetry · 2. Tool Card From Typed Lifecycle And Result Events While Keeping · 3. Attach Versioned Evidence Cards With Freshness, Authority, Scope, And Selection

### Diagram 203 — Partial success, preserved work, and unfinished work

Represent partial success without discarding useful work or pretending the whole task completed.

**Use it for:** Study Partial success, preserved work, and unfinished work through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/203-partial-success-preserved-unfinished-work.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/203-partial-success-preserved-unfinished-work.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=203)

**Inside:** 1. Long Agent Workflows Rarely Fail As One Indivisible Block · 2. HTTP Success And Final Prose Do Not Describe That Shape · 3. Completion, Evidence, Artifact, And Dependency State At Explicit Workflow Checkpoints

### Diagram 204 — Errors, recovery choices, support references, and next actions

Design error messages that preserve dignity, evidence, and control instead of blaming the user or offering a useless retry button.

**Use it for:** Study Errors, recovery choices, support references, and next actions through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/204-errors-recovery-support-next-actions.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/204-errors-recovery-support-next-actions.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=204)

**Inside:** 1. Never Expose Stack Traces, Internal URLs, Tokens, Or Provider Payloads · 2. Normalize Technical Failures Into Bounded Product Categories With Consequence, Retryability · 3. State What Happened, What Was Preserved, What May Have Changed

### Diagram 205 — Interrupt, input request, approval, rejection, and expiry

Create human decision points that bind a person's choice to one understandable proposal and current evidence.

**Use it for:** Study Interrupt, input request, approval, rejection, and expiry through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/205-interrupt-input-approval-rejection-expiry.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/205-interrupt-input-approval-rejection-expiry.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=205)

**Inside:** 1. 'Allow?' Is Not Informed Consent · 2. Approve, Reject, Request Changes, Ask A Question, And Defer · 3. Pause At A Named Decision Gate Before Any Consequential Effect

### Diagram 206 — Edit, steer, reprioritize, replan, and invalidate

Let a person change direction without silently discarding valid work or pretending old evidence still supports a new plan.

**Use it for:** Study Edit, steer, reprioritize, replan, and invalidate through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/206-edit-steer-reprioritize-replan-invalidate.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/206-edit-steer-reprioritize-replan-invalidate.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=206)

**Inside:** 1. It Is Not The Same As Sending Another Chat Message · 2. Some Changes Require Fresh Approval Or Cannot Be Accepted After · 3. Current Goal, Constraints, Priorities, Plan Version, Preserved Artifacts, And Committed

### Diagram 207 — Cancel, undo, compensate, and preserve audit history

Maya's case: Maya cancels a refund workflow after Acme has already sent the refund request but before the provider acknowledgement arrives.

**Use it for:** Study Cancel, undo, compensate, and preserve audit history through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/207-cancel-undo-compensate-audit-history.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/207-cancel-undo-compensate-audit-history.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=207)

**Inside:** 1. Cancellation Is Cooperative · 2. It Works For A Draft Edit Or Local Ordering Change · 3. Mark Each Stage And Effect As Cancellable, Reversible, Compensatable, Irreversible

### Diagram 208 — Accessibility, plain language, uncertainty, and trust cues

Treat accessibility and understandable trust as core product behavior rather than a final visual checklist.

**Use it for:** Study Accessibility, plain language, uncertainty, and trust cues through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/208-accessibility-plain-language-uncertainty-trust.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/208-accessibility-plain-language-uncertainty-trust.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=208)

**Inside:** 1. Static Homepage Audit Is Not Enough · 2. WCAG 2.2 Provides Testable Success Criteria, While WAI-ARIA Supplies Semantics · 3. Workflow State And Control To Semantic HTML, Accessible Name, Description

### Diagram 209 — Typed components, schemas, allowlists, and validation

Let an agent choose from safe interface building blocks without allowing it to execute arbitrary frontend code.

**Use it for:** Study Typed components, schemas, allowlists, and validation through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/209-typed-components-schemas-allowlists-validation.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/209-typed-components-schemas-allowlists-validation.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=209)

**Inside:** 1. A2UI Follows This Server-driven Idea · 2. Dynamic Composition Does Not Remove Human Control · 3. Bounded Declarative Payload With Protocol Version, Surface ID, Component Tree

### Diagram 210 — MCP Apps, sandboxed frames, consent, and communication

Explain how an MCP App can provide a rich embedded experience while the host keeps a visible security and consent boundary.

**Use it for:** Study MCP Apps, sandboxed frames, consent, and communication through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/210-mcp-apps-sandbox-consent-communication.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/210-mcp-apps-sandbox-consent-communication.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=210)

**Inside:** 1. Unsupported Behavior Needs A Safe Fallback · 2. Discover The MCP Tool And Its Declared UI Resource Metadata · 3. Fetch And Validate The Resource Under Host Policy, Then Load

### Diagram 211 — Frontend tool calls and user-device actions

Design browser and device actions as visible, scoped user choices instead of invisible agent powers.

**Use it for:** Study Frontend tool calls and user-device actions through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/211-frontend-tools-user-device-actions.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/211-frontend-tools-user-device-actions.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=211)

**Inside:** 1. Links And Downloads Are Side Effects Too · 2. Validate Schemes And Destinations, Prevent Opener Abuse, Label File Type · 3. Convert The Agent Suggestion Into A Typed Frontend Proposal

### Diagram 212 — Interface security, data exposure, and safe rendering

Apply ordinary web security and agent-specific trust boundaries to every dynamic interface input and action.

**Use it for:** Study Interface security, data exposure, and safe rendering through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/212-interface-security-data-exposure-safe-rendering.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/212-interface-security-data-exposure-safe-rendering.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=212)

**Inside:** 1. Sanitization Is Needed Only When The Product Intentionally Supports · 2. Avoid Raw HTML Whenever Structured Components Can Express The Same · 3. Inventory Every Interface Input, Renderer, Frame, Bridge, Browser Capability, Action

### Diagram 213 — A reusable visual lesson content model

Design one durable lesson source that can power documents, a website, search, accessibility, and future learning experiences.

**Use it for:** Study A reusable visual lesson content model through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/213-reusable-visual-lesson-content-model.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/213-reusable-visual-lesson-content-model.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=213)

**Inside:** 1. Website Should Not Begin By Copying Paragraphs Out Of Word · 2. Migration Should Preserve Author Intent, Report Information Loss, And Leave · 3. Stable Course, Module, Lesson, Source, Term, Checkpoint, And Asset Identities

### Diagram 214 — Responsive diagrams, zoom, annotations, and reading order

Make complex diagrams usable at every screen size and through visual, keyboard, zoom, and screen-reader paths.

**Use it for:** Study Responsive diagrams, zoom, annotations, and reading order through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/214-responsive-diagrams-zoom-annotations-reading-order.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/214-responsive-diagrams-zoom-annotations-reading-order.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=214)

**Inside:** 1. Annotations Should Connect A Hotspot To A Stable Concept, Not · 2. Focus Must Remain Visible And The Viewport Must Not Trap · 3. With The Learning Outcome And Define The Smallest Set

### Diagram 215 — Glossary, citations, search, prerequisites, and cross-links

Turn many visual lessons into a navigable body of knowledge rather than a long folder of isolated pages.

**Use it for:** Study Glossary, citations, search, prerequisites, and cross-links through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/215-glossary-citations-search-prerequisites-crosslinks.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/215-glossary-citations-search-prerequisites-crosslinks.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=215)

**Inside:** 1. Course Becomes Easier To Learn When Relationships Are Explicit · 2. These Labels Should Not Be Collapsed Into One Vague More · 3. Stable Records For Lessons, Terms, Sources, Topics, Technologies, And Relation

### Diagram 216 — Progress, checkpoints, quizzes, accessibility, and offline use

Design a learning experience that preserves progress, supports practice, remains accessible, and behaves honestly offline.

**Use it for:** Study Progress, checkpoints, quizzes, accessibility, and offline use through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/216-progress-checkpoints-quizzes-accessibility-offline.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/216-progress-checkpoints-quizzes-accessibility-offline.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=216)

**Inside:** 1. Checkpoints Give Immediate Retrieval Practice; Quizzes Measure A Broader Set · 2. Explanations Should Teach After An Answer And Allow Retry Without · 3. Learner-owned Progress Model Using Stable Lesson, Activity, Question, And Content-version

### Diagram 217 — Asynchronous return, notifications, and attention management

Let long-running agent work release the user's attention and call it back only when the timing and reason are genuinely useful.

**Use it for:** Study Asynchronous return, notifications, and attention management through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/217-async-return-notifications-attention-management.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/217-async-return-notifications-attention-management.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=217)

**Inside:** 1. Product Stores A Durable Run, Explains What Can Continue · 2. Notifications Are An Attention Budget, Not Proof That The System · 3. Classify Task Transitions As Silent, Inbox, Digest, Interruptive, Or Prohibited

### Diagram 218 — Privacy controls, consent, memory settings, and deletion

Give people understandable control over what an agent collects, remembers, shares, exports, and deletes across the complete data lifecycle.

**Use it for:** Study Privacy controls, consent, memory settings, and deletion through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/218-privacy-consent-memory-settings-deletion.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/218-privacy-consent-memory-settings-deletion.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=218)

**Inside:** 1. Decline And Delete Should Be As Understandable As Accept · 2. Inventory Every Collected Field, Derived Value, Memory Item, Embedding, Artifact · 3. Separate Necessary Processing From Optional Purposes And Capture Versioned, Revocable

### Diagram 219 — Product analytics, feedback, evaluation, and experiment ethics

Improve an agentic product with honest evidence while protecting learners and users from manipulative measurement and unsafe experiments.

**Use it for:** Study Product analytics, feedback, evaluation, and experiment ethics through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/219-analytics-feedback-evaluation-experiment-ethics.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/219-analytics-feedback-evaluation-experiment-ethics.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=219)

**Inside:** 1. They Can Inform One Another But Should Not Be Merged · 2. Completion Rate Can Be Harmful If Completion Includes Accidental Approvals · 3. With A Product Decision And User Outcome, Then Define

### Diagram 220 — Capstone: Acme Agent Workspace and Learning Platform

Combine the full visual course into an implementation-ready product specification without prematurely writing the Next.js or Python project.

**Use it for:** Study Capstone: Acme Agent Workspace and Learning Platform through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 09/diagram-docs/220-acme-agent-workspace-learning-platform.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2009/diagram-docs/220-acme-agent-workspace-learning-platform.md) · [Website reader](https://course.ketanshukla.dev/#course=09&chapter=220)

**Inside:** 1. Capstone Is One Coherent Product With Two Experiences · 2. A2A Coordinates Task-oriented Peer Agents · 3. Maya Opens A Customer Case And Requests A Refund-policy Review

<a id="course-10"></a>

## Visual Course Volume 10 — Enterprise Architecture and Dual-Stack Project Blueprint

Assemble the architecture, contracts, delivery, and operational handoff for a real agent platform.

### Diagram 221 — Problem, workflow, assistant, agent, and automation boundaries

Problem, workflow, assistant, agent, and automation boundaries — Choose whether a problem needs information, a fixed workflow, an assistant, an agent, or deterministic automation before selecting protocols or frameworks.

**Use it for:** Study Problem, workflow, assistant, agent, and automation boundaries through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/221-automation-boundary-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/221-automation-boundary-map.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=221)

**Inside:** 1. Problem, workflow, assistant, agent, and automation boundaries · 2. Start with the User Outcome and Current Pain Without Naming a Technology. · 3. Separate Known Repeatable Steps from Uncertain Judgment or Research.

### Diagram 222 — Use-case selection, value, frequency, uncertainty, and reversibility

Use-case selection, value, frequency, uncertainty, and reversibility — Rank candidate agent use cases using user value and risk-shaped evidence instead of novelty or an impressive demo.

**Use it for:** Study Use-case selection, value, frequency, uncertainty, and reversibility through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/222-use-case-selection-scorecard.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/222-use-case-selection-scorecard.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=222)

**Inside:** 1. Use-case selection, value, frequency, uncertainty, and reversibility · 2. Name Candidate Outcomes in User Language and Remove Duplicate Technology Ideas. · 3. Define Value, Frequency, Uncertainty, Reversibility, Data, and Evidence Scales.

### Diagram 223 — Risk classification, human authority, and unacceptable outcomes

Risk classification, human authority, and unacceptable outcomes — Turn broad safety concerns into a usable classification, an explicit human-authority model, and hard unacceptable-outcome rules.

**Use it for:** Study Risk classification, human authority, and unacceptable outcomes through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/223-risk-authority-unacceptable-outcomes.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/223-risk-authority-unacceptable-outcomes.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=223)

**Inside:** 1. Risk classification, human authority, and unacceptable outcomes · 2. Describe Credible Harms and the People, Data, and Services Exposed. · 3. Classify Impact, Likelihood, Exposure, Reversibility, and Detectability with Evidence.

### Diagram 224 — Success criteria, exit criteria, and evidence requirements

Success criteria, exit criteria, and evidence requirements — Define success and stopping rules with named evidence before the team starts building or collecting convenient metrics.

**Use it for:** Study Success criteria, exit criteria, and evidence requirements through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/224-success-exit-evidence-contract.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/224-success-exit-evidence-contract.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=224)

**Inside:** 1. Success criteria, exit criteria, and evidence requirements · 2. Start with One User Outcome and the Unacceptable Outcomes That Constrain It. · 3. Define Quality, Safety, Latency, Cost, Accessibility, and Recovery Measures with Denominators.

### Diagram 225 — Capability, context, model, tool, and authority boundaries

Capability, context, model, tool, and authority boundaries — Draw a complete trust-boundary view that separates what a component knows, can request, may execute, and is authoritative to commit.

**Use it for:** Study Capability, context, model, tool, and authority boundaries through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/225-enterprise-boundary-stack.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/225-enterprise-boundary-stack.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=225)

**Inside:** 1. Capability, context, model, tool, and authority boundaries · 2. Name Components and Assign One Owned Job to Each. · 3. Draw Every Network, Process, Tenant, Provider, and Privilege Boundary.

### Diagram 226 — State, data, memory, evidence, artifact, and audit architecture

State, data, memory, evidence, artifact, and audit architecture — Give each kind of data a clear purpose, owner, lifetime, authority, and deletion path instead of treating every record as agent memory.

**Use it for:** Study State, data, memory, evidence, artifact, and audit architecture through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/226-state-data-evidence-audit-architecture.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/226-state-data-evidence-audit-architecture.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=226)

**Inside:** 1. State, data, memory, evidence, artifact, and audit architecture · 2. Classify Every Data Object as State, Source, Memory, Evidence, Artifact, Audit · 3. Assign Owner, Authority, Tenant, Privacy Class, Retention, Indexing, and Deletion Behavior.

### Diagram 227 — MCP, A2A, AG-UI, HTTP, queue, and internal boundaries

MCP, A2A, AG-UI, HTTP, queue, and internal boundaries — Select a protocol or transport from the relationship and failure needs at each boundary instead of forcing one protocol across the whole system.

**Use it for:** Study MCP, A2A, AG-UI, HTTP, queue, and internal boundaries through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/227-protocol-boundary-routing-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/227-protocol-boundary-routing-map.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=227)

**Inside:** 1. MCP, A2A, AG-UI, HTTP, queue, and internal boundaries · 2. Name the Relationship: Frontend Interaction, Tool Access, Peer Delegation, Business Command, Durable Work · 3. Name Duration, Streaming, Retry, Ordering, Discovery, Identity, and Failure Requirements.

### Diagram 228 — Deployment topology, failure domains, and ownership

Deployment topology, failure domains, and ownership — Place services and data on a deployable topology that makes network paths, failure containment, scaling, recovery, and ownership visible.

**Use it for:** Study Deployment topology, failure domains, and ownership through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/228-deployment-topology-failure-domains.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/228-deployment-topology-failure-domains.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=228)

**Inside:** 1. Deployment topology, failure domains, and ownership · 2. Place Public Edge, Web, API, Workers, Protocols, Data Stores · 3. Draw Authentication, Encryption, Egress, Region, Tenant, and Data-residency Paths.

### Diagram 229 — Shared schemas, contracts, fixtures, and conformance cases

Shared schemas, contracts, fixtures, and conformance cases — Create one framework-neutral behavior contract that both future stacks can implement and test without sharing application code.

**Use it for:** Study Shared schemas, contracts, fixtures, and conformance cases through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/229-shared-contract-conformance-kit.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/229-shared-contract-conformance-kit.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=229)

**Inside:** 1. Shared schemas, contracts, fixtures, and conformance cases · 2. Inventory Commands, Queries, Events, Artifacts, Proposals, Decisions, Errors, and Receipts Shared by Both Stacks. · 3. Start with Canonical Schemas Plus Semantic Rules for Identity, Authority, Ordering, Idempotency, Privacy

### Diagram 230 — Next.js and React responsibility map

Next.js and React responsibility map — Assign the future Next.js and React project a clear web responsibility without turning the browser into the agent backend or source of truth.

**Use it for:** Study Next.js and React responsibility map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/230-nextjs-react-responsibility-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/230-nextjs-react-responsibility-map.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=230)

**Inside:** 1. Next.js and React responsibility map · 2. Map Each User Journey to Routes, Layouts, Initial Server Data, and Interactive Client Islands. · 3. Define Web-to-service Commands, Queries, Streams, Artifacts, Errors, and Identity Propagation.

### Diagram 231 — Python and FastAPI responsibility map

Python and FastAPI responsibility map — Assign the future Python and FastAPI project clear domain, orchestration, policy, persistence, and protocol responsibilities.

**Use it for:** Study Python and FastAPI responsibility map through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/231-python-fastapi-responsibility-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/231-python-fastapi-responsibility-map.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=231)

**Inside:** 1. Python and FastAPI responsibility map · 2. Organize Routers Around Product Capabilities Rather Than Provider or Protocol Names. · 3. Define Application Use Cases and Domain Invariants Independently from Transport and Persistence.

### Diagram 232 — Cross-stack integration, adapters, and end-to-end tests

Cross-stack integration, adapters, and end-to-end tests — Join the two future projects through owned adapters and a layered test strategy that proves the whole user story, not only isolated endpoints.

**Use it for:** Study Cross-stack integration, adapters, and end-to-end tests through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/232-cross-stack-adapter-test-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/232-cross-stack-adapter-test-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=232)

**Inside:** 1. Cross-stack integration, adapters, and end-to-end tests · 2. Choose a Vertical User Journey and Assign One Correlation Identity Across Every Service · 3. Define Adapter Inputs, Outputs, Timeouts, Retries, Versions, and Safe Error Mappings.

### Diagram 233 — Authentication, secrets, tenants, policy, and audit services

Authentication, secrets, tenants, policy, and audit services — Design identity and policy as explicit services that constrain every protocol, tenant, tool, and authoritative action.

**Use it for:** Study Authentication, secrets, tenants, policy, and audit services through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/233-identity-policy-audit-services.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/233-identity-policy-audit-services.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=233)

**Inside:** 1. Authentication, secrets, tenants, policy, and audit services · 2. Inventory Human, Service, Agent, Provider, and Administrative Identities and Their Credential Flows. · 3. Bind Every Token to Intended Issuer, Audience, Resource, Scope, Tenant, and Expiry.

### Diagram 234 — Database, vector index, queue, cache, and artifact storage

Database, vector index, queue, cache, and artifact storage — Select storage by the job data must perform and define consistency, tenancy, retention, backup, and recovery for each store.

**Use it for:** Study Database, vector index, queue, cache, and artifact storage through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/234-polyglot-storage-decision-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/234-polyglot-storage-decision-map.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=234)

**Inside:** 1. Database, vector index, queue, cache, and artifact storage · 2. Name Data Objects and the Query, Transaction, Search, Delivery, or File Behavior Each Needs. · 3. Assign One Authoritative Store and Treat Other Copies as Derived Projections.

### Diagram 235 — Telemetry, evaluation, analytics, and cost control

Telemetry, evaluation, analytics, and cost control — Design an evidence control plane that explains system behavior, product value, safety, and cost without turning telemetry into a second uncontrolled data lake.

**Use it for:** Study Telemetry, evaluation, analytics, and cost control through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/235-telemetry-evaluation-cost-control-plane.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/235-telemetry-evaluation-cost-control-plane.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=235)

**Inside:** 1. Telemetry, evaluation, analytics, and cost control · 2. Define the Decisions Telemetry Must Support Before Choosing Fields or Dashboards. · 3. Create a Versioned Event and Attribute Vocabulary with Privacy Classification and Ownership.

### Diagram 236 — CI/CD, environments, migrations, flags, rollback, and recovery

CI/CD, environments, migrations, flags, rollback, and recovery — Design a release path that can prove what changed, limit exposure, reverse safely, and recover data as well as code.

**Use it for:** Study CI/CD, environments, migrations, flags, rollback, and recovery through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/236-safe-delivery-recovery-pipeline.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/236-safe-delivery-recovery-pipeline.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=236)

**Inside:** 1. CI/CD, environments, migrations, flags, rollback, and recovery · 2. Build One Immutable Versioned Artifact with Dependency and Provenance Evidence. · 3. Run Code, Contract, Security, Accessibility, Evaluation, and Data-migration Gates.

### Diagram 237 — Milestones, vertical slices, backlog, dependencies, and owners

Milestones, vertical slices, backlog, dependencies, and owners — Turn the architecture into small end-to-end milestones that create demonstrable evidence and reduce the most important uncertainty early.

**Use it for:** Study Milestones, vertical slices, backlog, dependencies, and owners through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/237-vertical-slice-delivery-roadmap.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/237-vertical-slice-delivery-roadmap.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=237)

**Inside:** 1. Milestones, vertical slices, backlog, dependencies, and owners · 2. Start with the Final User Journey and the Riskiest Unknowns the Project Must Retire. · 3. Define Thin Slices That Cross the System and End in Observable User Value

### Diagram 238 — Contract, integration, workflow, security, and acceptance tests

Contract, integration, workflow, security, and acceptance tests — Build a layered test system that proves domain rules, cross-stack contracts, real integrations, human journeys, adversarial behavior, and recovery.

**Use it for:** Study Contract, integration, workflow, security, and acceptance tests through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/238-production-test-pyramid.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/238-production-test-pyramid.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=238)

**Inside:** 1. Contract, integration, workflow, security, and acceptance tests · 2. Map Every Requirement and Unacceptable Outcome to One or More Test Layers. · 3. Create Reusable Synthetic Fixtures and Deterministic Clocks, Identities, Tenants, and Provider Doubles.

### Diagram 239 — Threat, evaluation, accessibility, privacy, and readiness gates

Threat, evaluation, accessibility, privacy, and readiness gates — Combine cross-functional proof into a transparent go, conditional-go, or no-go decision without letting one team self-certify the whole system.

**Use it for:** Study Threat, evaluation, accessibility, privacy, and readiness gates through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/239-readiness-gate-system.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/239-readiness-gate-system.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=239)

**Inside:** 1. Threat, evaluation, accessibility, privacy, and readiness gates · 2. Define Required Evidence and Independent Reviewers for Each Readiness Domain. · 3. Run Threat, Evaluation, Accessibility, Privacy, and Operational Tests on the Exact Release Candidate.

### Diagram 240 — Runbooks, support, incident response, and operational ownership

Runbooks, support, incident response, and operational ownership — Define who notices, decides, communicates, recovers, verifies, and learns when the agent system behaves badly or becomes unavailable.

**Use it for:** Study Runbooks, support, incident response, and operational ownership through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/240-operational-ownership-loop.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/240-operational-ownership-loop.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=240)

**Inside:** 1. Runbooks, support, incident response, and operational ownership · 2. Inventory Components, Service Objectives, Alerts, Owners, Support Paths, and Safe Degraded Modes. · 3. Start with Symptom-based Runbooks with Containment, Evidence, Communication, Recovery, and Escalation Steps.

### Diagram 241 — Architecture review and trade-off defense

Architecture review and trade-off defense — Present and defend the blueprint as a set of evidence-based trade-offs rather than a collection of boxes or fashionable technologies.

**Use it for:** Study Architecture review and trade-off defense through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/241-architecture-review-tradeoff-defense.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/241-architecture-review-tradeoff-defense.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=241)

**Inside:** 1. Architecture review and trade-off defense · 2. Start with the User Problem, Requirements, Unacceptable Outcomes, and Quality Priorities. · 3. Walk the End-to-end Journey Across Authority, Data, Protocol, Deployment, Failure, and Recovery Boundaries.

### Diagram 242 — Failure game day and recovery demonstration

Failure game day and recovery demonstration — Demonstrate that the designed system and team can recognize, contain, recover, reconcile, and learn from realistic failures.

**Use it for:** Study Failure game day and recovery demonstration through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/242-failure-game-day-recovery.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/242-failure-game-day-recovery.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=242)

**Inside:** 1. Failure game day and recovery demonstration · 2. Choose One Architecture Assumption and Write the Failure Hypothesis and Success Evidence. · 3. Authorize Scope, Synthetic Data, Observers, Communications, Stop Conditions, and Rollback.

### Diagram 243 — Portfolio evidence, README, case study, and demonstration plan

Portfolio evidence, README, case study, and demonstration plan — Explain the project as a credible engineering story whose claims can be traced to artifacts, tests, deployments, and honestly measured results.

**Use it for:** Study Portfolio evidence, README, case study, and demonstration plan through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/243-portfolio-evidence-story-map.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/243-portfolio-evidence-story-map.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=243)

**Inside:** 1. Portfolio evidence, README, case study, and demonstration plan · 2. Start with the One-sentence User Problem, Constraints, Unacceptable Outcomes · 3. Link Requirements to Diagrams, Contracts, Code Locations, Tests, Deployment, and Evidence Manifests.

### Diagram 244 — Graduation map and handoff to the two separate coding projects

Graduation map and handoff to the two separate coding projects — Package the entire course into a clean implementation handoff so the two later full-stack projects can begin independently and reunite through one tested product contract.

**Use it for:** Study Graduation map and handoff to the two separate coding projects through the diagram, its explanation and a worked teaching scenario.

**Location:** `courses/Visual Course 10/diagram-docs/244-dual-project-graduation-handoff.md`

**Availability:** Published course lesson

[Markdown source](../courses/Visual%20Course%2010/diagram-docs/244-dual-project-graduation-handoff.md) · [Website reader](https://course.ketanshukla.dev/#course=10&chapter=244)

**Inside:** 1. Graduation map and handoff to the two separate coding projects · 2. Freeze the Blueprint Version and Inventory Every Handoff Artifact, Open Question, Assumption, Owner · 3. Create Separate Next.js and Python Backlogs Mapped to the Same Vertical Slices, Contracts

<a id="course-support"></a>

## Course authoring & maintenance notes

Prompt libraries, roadmap notes and historical verification records accompanying the visual courses.

### MCP · ACP · A2A · RAG Visual Diagram Library

This library contains 30 reusable 16:9 explainers. The diagrams are ordered as a visual course, but each one also works as a standalone slide, lesson opener, interview aid, or architecture-review prompt.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 01/Diagram Library Guide and Prompts.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2001/Diagram%20Library%20Guide%20and%20Prompts.md)

**Inside:** Design system · Reusable base prompt · Module 1 — See the whole system

### Verification Report

Layout result: no blank pages, clipped diagrams, orphaned checkpoints, or unintended page breaks.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 01/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2001/VERIFICATION.md)

**Inside:** Final artifacts · Word course checks · Diagram-library checks

### Volume 2 Diagram Prompt Library

Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make…

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 02/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2002/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Repeated visual grammar · Diagram prompts

### Volume 2 Verification Report

Page structure: cover and orientation, 4 module dividers, 3 pages per lesson, capstone, website companion, and source/reference pages.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 02/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2002/VERIFICATION.md)

**Inside:** Deliverable scope · Word document QA · Course-data QA

### Visual Agent Academy — Website Roadmap

Volume 1 built the big mental model: RAG supplies evidence, MCP supplies capabilities, A2A delegates separately owned work, and domain policy controls consequences. The correct next step for a beginner is the implementation bridge: learn the ordinary web and application machinery underneath those protocols, then follow one request through an agent runtime, failure handling, observability, and…

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 02/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2002/WEBSITE-ROADMAP.md)

**Inside:** The next logical step · The website promise · Recommended information architecture

### Volume 3 Diagram Prompt Library

These prompts reproduce the visual intent of Diagrams 47-76. Generated text and layout should be checked by a person before publication.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 03/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2003/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Diagram 47 - A stateless MCP request · Diagram 48 - Multi Round-Trip Requests

### Volume 3 Verification Report

Page structure: cover, three orientation pages, six module dividers, three pages per lesson, capstone, website companion, and source/reference pages.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 03/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2003/VERIFICATION.md)

**Inside:** Deliverable scope · Word document QA · Course-data QA

### Volume 3 Website Roadmap

Turn the same structured lesson source used by the document into an accessible visual study website. Keep the diagrams, explanations, case studies, labs, checkpoints, glossary, and related-lesson links synchronized from one source.

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 03/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2003/WEBSITE-ROADMAP.md)

**Inside:** Goal · Recommended first release · Second release

### Volume 4 Diagram Prompt Library

These are the exact production prompts for Diagrams 77-100. The built-in image generator was used in standard generation mode. Generated labels and layouts were visually checked before publication.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 04/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2004/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Diagram 77 - Normative rules versus examples · Diagram 78 - Version, capability, and extension negotiation

### Volume 4 Verification

Protocol baseline checked 2026-08-24: MCP 2026-07-28, A2A 1.0, and current official AG-UI documentation. Draft AG-UI interrupt behavior is labeled draft, and ACP is historical migration context only.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 04/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2004/VERIFICATION.md)

**Inside:** Automated checks · Visual review · ZIP safety

### Volume 4 Website Roadmap

Turn the document and its structured lesson source into a visual protocol-engineering website. Keep the protocol stability label, diagram, full text explanation, Maya case study, dual-stack map, lab, checkpoint, glossary, and source links synchronized from one content object.

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 04/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2004/WEBSITE-ROADMAP.md)

**Inside:** Goal · Recommended first release · Interactive visual ideas

### Volume 5 Diagram Prompt Library

These are the exact production prompts for Diagrams 101-124. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 05/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2005/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Diagram 101 - Source inventory, authority, ownership, and purpose · Diagram 102 - Layout-aware parsing for pages, headings, tables, and lists

### Volume 5 Verification

Knowledge baseline checked 2026-08-24 against primary research and official documentation. Methods are labeled as foundations, established patterns, optional advanced techniques, or measured choices so no single retrieval architecture is presented as universally best.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 05/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2005/VERIFICATION.md)

**Inside:** Automated checks · Visual review · ZIP safety

### Volume 5 Website Roadmap

Turn Volume 5 into an interactive knowledge-systems laboratory. Preserve the diagram-first lesson order, full explanation, pattern-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary sources from one structured content object.

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 05/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2005/WEBSITE-ROADMAP.md)

**Inside:** Goal · Recommended first release · Interactive visual laboratories

### Volume 6 Diagram Prompt Library

These are the exact production prompts for Diagrams 125-148. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 06/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2006/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Diagram 125 - Conversation state, run state, task state, and workflow state · Diagram 126 - State machines, events, commands, and invariants

### Volume 6 Verification

Knowledge baseline checked 2026-08-24 against current primary specifications and official documentation. A2A examples use the 1.0 contract. Workflow engines, queues, and SDKs remain replaceable implementations of the durable responsibilities taught in the course.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 06/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2006/VERIFICATION.md)

**Inside:** Automated checks · Visual review · ZIP safety

### Volume 6 Website Roadmap

Turn Volume 6 into an interactive durable-workflow laboratory. Preserve the diagram-first teaching order, complete explanation, pattern-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 06/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2006/WEBSITE-ROADMAP.md)

**Inside:** Goal · Recommended first release · Interactive visual laboratories

### Volume 7 Diagram Prompt Library

These are the exact production prompts for Diagrams 149-172. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 07/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2007/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Diagram 149 - Assets, identities, trust boundaries, data flows, and owners · Diagram 150 - Attack paths, misuse cases, and unacceptable outcomes

### Volume 7 Verification

Knowledge baseline checked 2026-08-24 against current primary specifications and official guidance. MCP examples use protocol release 2026-07-28 and current authorization guidance; A2A examples use 1.0. NIST AI RMF 1.0, OWASP Agentic Top 10 2026, stable OAuth standards, implementation patterns, and active MCP roadmap items are labeled separately.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 07/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2007/VERIFICATION.md)

**Inside:** Automated checks · Visual review · ZIP safety

### Volume 7 Website Roadmap

Turn Volume 7 into an interactive agent-security laboratory. Preserve the diagram-first teaching order, complete explanation, standards-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 07/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2007/WEBSITE-ROADMAP.md)

**Inside:** Goal · Recommended first release · Interactive visual laboratories

### Volume 8 Diagram Prompt Library

These are the exact production prompts for Diagrams 173-196. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 08/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2008/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Diagram 173 - Traces, spans, logs, metrics, events, and resources · Diagram 174 - Context propagation across MCP, A2A, AG-UI, HTTP, and queues

### Volume 8 Verification

Knowledge baseline checked 2026-08-25 against current primary specifications and official guidance. MCP examples use protocol release 2026-07-28; A2A examples use 1.0; W3C Trace Context is the stable propagation baseline; OpenTelemetry Semantic Conventions 1.44.0 are current while the dedicated GenAI conventions remain versioned and evolving. NIST, OpenFeature, SRE practices, standards, and…

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 08/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2008/VERIFICATION.md)

**Inside:** Automated checks · Visual review · ZIP safety

### Volume 8 Website Roadmap

Turn Volume 8 into an interactive Agent Quality Lab. Preserve the diagram-first teaching order, complete explanation, standards-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 08/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2008/WEBSITE-ROADMAP.md)

**Inside:** Goal · Recommended first release · Interactive visual laboratories

### Volume 9 Diagram Prompt Library

These are the exact production prompts for Diagrams 197-220. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 09/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2009/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Diagram 197 - The event-driven interface mental model · Diagram 198 - State snapshots, deltas, reducers, and conflict handling

### Volume 9 Verification

Knowledge baseline checked 2026-08-25 against current primary specifications and official guidance. AG-UI uses the checked 2026-07-28 repository release; MCP Apps 2026-01-26 is stable; A2UI v0.9.1 is current while v1.0 remains a candidate; WCAG 2.2, WAI-ARIA 1.2, JSON Patch RFC 6902, CSP, Permissions Policy, and NIST frameworks are labeled by status and purpose.

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 09/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2009/VERIFICATION.md)

**Inside:** Automated checks · Visual review · ZIP safety

### Volume 9 Website Roadmap

Turn Volume 9 into an accessible Agent Workspace and Visual Learning Platform. Preserve the diagram-first teaching order, complete explanation, standards-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 09/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2009/WEBSITE-ROADMAP.md)

**Inside:** Goal · Recommended first release · Interactive visual laboratories

### Volume 10 Diagram Prompt Library

These are the exact production prompts for Diagrams 221-244. The built-in image generator was used in standard generation mode. Every selected diagram was visually checked for logic, labels, legibility, and consistency before publication.

**Use it for:** Maintain or reproduce diagram authoring; not the recommended learner starting point.

**Location:** `courses/Visual Course 10/DIAGRAM-PROMPT-LIBRARY.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2010/DIAGRAM-PROMPT-LIBRARY.md)

**Inside:** Shared art direction · Diagram 221 - Problem, workflow, assistant, agent, and automation boundaries · Diagram 222 - Use-case selection, value, frequency, uncertainty, and reversibility

### Volume 10 Verification

Knowledge baseline checked 2026-08-25 against current primary specifications and official guidance. MCP 2026-07-28, A2A 1.0, current AG-UI architecture, OpenTelemetry semantic conventions 1.44.0, OpenAPI 3.1.1, JSON Schema 2020-12, AsyncAPI 3.0.0, OAuth RFCs 9700, 9449 and 9728, WCAG 2.2, current NIST AI RMF status, OWASP Agentic Applications 2026, Next.js, Vercel, and FastAPI guidance are…

**Use it for:** Review the checks and limitations recorded at authoring time; rerun current checks before release.

**Location:** `courses/Visual Course 10/VERIFICATION.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2010/VERIFICATION.md)

**Inside:** Automated checks · Visual review · ZIP safety

### Volume 10 Dual-Project Handoff Roadmap

Turn Volume 10 into the implementation handoff for two separate full-stack projects. Preserve the diagram-first teaching order, complete explanation, standards-status label, Maya case study, dual-stack map, lab, checkpoint, glossary, and primary-source register from one structured lesson source.

**Use it for:** Review a course-specific website plan; verify it against the current application before implementing.

**Location:** `courses/Visual Course 10/WEBSITE-ROADMAP.md`

**Availability:** Local reference — not in website allowlist

[Markdown source](../courses/Visual%20Course%2010/WEBSITE-ROADMAP.md)

**Inside:** Goal · Recommended first release · Blueprint laboratories

## Keep this directory current

Run `node scripts/build_document_directory.mjs` from the repository root after adding or moving documents. Run it with `--check` to verify coverage, links and that both editions match the current inventory. The directory reads source introductions and headings; it does not certify the correctness of every document. Its generated Markdown and HTML should be updated through the builder rather than edited separately.
