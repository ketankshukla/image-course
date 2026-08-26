# Volume 2 Diagram Prompt Library

## Shared art direction

Use this paragraph at the start of every new prompt:

> Create a polished 16:9 educational architecture diagram for a beginner visual course. Use a dark midnight-navy gradient background, glowing cobalt-blue isometric platforms, cyan forward arrows, teal return paths, white data or contract cards, occasional coral warning accents, rounded 3D icons, crisp uppercase sans-serif labels, generous spacing, and a professional high-contrast composition. Make the logic readable at a glance. Use only the exact labels specified. Do not add a logo, watermark, branding, unrelated title, or tiny decorative prose.

For strongest continuity, provide Diagram 01 or 27 from Volume 1 and one approved Volume 2 diagram as visual references.

## Repeated visual grammar

- Cobalt platform: a component, stage, or ownership boundary.
- Cyan arrow: request, command, task, evidence, or forward work.
- Teal arrow: result, artifact, recovery, confirmation, or receipt.
- Coral path: rejection, risk, failure, approval, or human-control path.
- White card: visible data or a contract.

## Diagram prompts

### 31 — Browser request journey

Create six numbered stages from left to right: `PERSON`, `BROWSER`, `DNS`, `HTTPS`, `WEB SERVER`, `PAGE + DATA`. Use person at laptop, browser, domain/IP lookup, secure lock, server, and web page plus JSON icons. Cyan arrows move forward and a teal dashed line shows the result returning.

### 32 — HTTP conversation

Show `HTTP REQUEST` on the left with four labeled layers: `URL`, `METHOD`, `HEADERS`, `BODY`. Send them into a central server. Show `HTTP RESPONSE` on the right with `STATUS`, `HEADERS`, `BODY`. Use cyan request and teal response arrows.

### 33 — JSON object anatomy

Place `JSON OBJECT` in the center. Connect it to `KEY`, `VALUE`, `ARRAY`, `NESTED OBJECT`, and `DATA TYPES`. Under data types show `STRING`, `NUMBER`, `BOOLEAN`, and `NULL`. Use a simple correct JSON example.

### 34 — JSON Schema validation

Create a left-to-right flow: `INPUT DATA` → `JSON SCHEMA` → `VALIDATE`. Inside the validation gate show `REQUIRED`, `TYPE`, `FORMAT`, `LIMITS`. Branch to teal `ACCEPTED` and coral `REJECTED`; beside rejected show `REQUIRED MISSING`, `TYPE MISMATCH`, `FORMAT INVALID`, `LIMITS EXCEEDED`.

### 35 — Frontend/backend boundary

Create five numbered stages: `REACT UI`, `API ROUTE`, `DOMAIN SERVICE`, `DATA STORE`, `RECEIPT`. Separate stage 1 from stages 2–5 with a glowing vertical boundary labeled `FRONTEND` and `BACKEND`. Cyan arrows move right; a teal result path returns to the UI.

### 36 — Server request pipeline

Create six numbered gates: `ROUTE`, `VALIDATE`, `AUTHENTICATE`, `AUTHORIZE`, `EXECUTE`, `RESPOND`. Cyan arrows connect the allowed path. Add coral exits from validation, authentication, and authorization to `STOP`. Add a teal response path returning to the caller.

### 37 — Storage map

Place `APPLICATION` in the center. Connect it both ways to `RELATIONAL DB`, `VECTOR INDEX`, `TASK STORE`, and `AUDIT LOG`. Add the ownership labels `FACTS`, `MEANING`, `PROGRESS`, and `EVIDENCE` beneath the matching stores.

### 38 — Identity boundary

Create a five-stage security journey: `SIGN IN`, `TOKEN`, `AUTHENTICATE`, `AUTHORIZE`, `LEAST PRIVILEGE`. Enclose stages 3–5 in a shield-shaped boundary. Add a coral branch from authorization to `DENIED`.

### 39 — Agent decision loop

Create a circular loop with `OBSERVE`, `PLAN`, `CHOOSE`, `ACT`, `CHECK`, and `STOP`. Cyan arrows move clockwise. From check, add a coral branch to `ASK HUMAN`, then a teal return to the loop.

### 40 — Tool call lifecycle

Create five numbered stages: `MODEL PROPOSES`, `CLIENT VALIDATES`, `SERVER AUTHORIZES`, `DOMAIN EXECUTES`, `RESULT + RECEIPT`. Add coral `STOP` exits beneath client validation and server authorization. Add a teal dashed result line returning to the model/client side.

### 41 — RAG reliability loop

Create the main path `QUESTION` → `RETRIEVE` → `RELEVANT?` → `ANSWER` → `CITE` → `VERIFY`. Label the happy branch `YES`. Add a coral `NO` branch from relevance to `IMPROVE QUERY`, then a teal loop back to retrieval.

### 42 — A2A task state machine

Create a task lifecycle with `SUBMITTED` → `WORKING` → `COMPLETED`. From working, branch to `INPUT REQUIRED` with a return path to working. Add coral terminal branches to `FAILED` and `CANCELED`. Move one visible task card with a stable ID through the states.

### 43 — Error recovery map

Place `ERROR` in the center. Create four paired paths: `BAD INPUT` → `FIX REQUEST`; `NOT AUTHORIZED` → `STOP`; `TEMPORARY FAILURE` → `RETRY`; `UNKNOWN SIDE EFFECT` → `CHECK RECEIPT`. Use coral for the stop/risk route and teal for recovery routes.

### 44 — Observability trace

Show `USER REQUEST` receiving a `TRACE ID`, then crossing `APP`, `RAG`, `MCP`, and `A2A`. Draw one continuous trace line with `SPAN 1`, `SPAN 2`, `SPAN 3`, and `SPAN 4`. Route safe copies to `METRICS`, `LOGS`, and `AUDIT`.

### 45 — Local to Vercel

Create six numbered stages: `LOCAL CODE`, `TESTS`, `GIT`, `VERCEL BUILD`, `PREVIEW`, `PRODUCTION`. Cyan arrows move forward. Coral failure arrows return from tests and build to an earlier stage. A teal dashed `PROMOTE` arrow goes from preview to production.

### 46 — Capstone build roadmap

Create seven ascending isometric steps: `LOCAL DATA`, `DOMAIN FUNCTION`, `MCP TOOL`, `RAG SEARCH`, `A2A TASK`, `WEB UI`, `DEPLOY`. Add a beginner walking upward and a final flag labeled `WORKING SYSTEM`.

## Quality check before accepting a visual

- Every required label is present and spelled correctly.
- The arrows express the intended direction and return path.
- Failure paths are coral and do not look like the happy path.
- The visual remains readable when reduced to half-page size.
- No icon implies that the model itself owns authentication, authorization, or business truth.
- Any explanatory prose in the image is short; the full explanation belongs beneath the visual in the course.
- The PNG is preserved at its generated resolution without resizing, recompression, or editing.

