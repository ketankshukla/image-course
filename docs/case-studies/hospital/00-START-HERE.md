# HarborCare Privacy Platform

## A complete learning case study: share the right information with the right recipient

HarborCare is a fictional hospital. This document set describes a proposed privacy-engineering demonstration using **entirely synthetic patients, organizations, documents, and messages**. It is not a clinical decision system, a live hospital integration, or a claim of HIPAA compliance.

The running case is a patient's discharge. The care team needs clinical information, an insurer needs a defined claim packet, and an assigned transport provider needs a small pickup packet. An unrelated agency receives no patient information. Public visitors may read hospital service information, but not whether a named person is a patient.

## 1. Start with the story

![A hospital discharge request moves through verified identity, purpose, authorized evidence, specialist tasks, release review, and a final recipient-specific delivery gate.](assets/01-patient-journey.svg)

The question is not simply “Is this field public or private?” It is **who wants which information, about which patient, for what approved purpose, at what time?** A pickup address remains private even when the assigned transport provider is permitted to receive it.

## 2. The document collection

| Guide | What it teaches |
|---|---|
| [Project strategy](01-PROJECT-STRATEGY.html) · [Markdown](01-PROJECT-STRATEGY.md) | Five coherent projects and a practical build sequence |
| [The whole flow in plain English](02-PLAIN-ENGLISH-AND-LEGEND.html) · [Markdown](02-PLAIN-ENGLISH-AND-LEGEND.md) | Follow one patient scenario; understand the technology legend |
| [Privacy rules and test cases](03-PRIVACY-POLICY-AND-TESTS.html) · [Markdown](03-PRIVACY-POLICY-AND-TESTS.md) | Public/private distinctions, recipient matrix, adversarial tests, legal boundaries |
| [Python reference architecture](04-PYTHON-ARCHITECTURE.html) · [Markdown](04-PYTHON-ARCHITECTURE.md) | Services, contracts, ownership, and release transactions |
| [Hybrid Next.js + Python](05-HYBRID-ARCHITECTURE.html) · [Markdown](05-HYBRID-ARCHITECTURE.md) | A safe web interface over the Python system |
| [TypeScript counterpart](06-TYPESCRIPT-ARCHITECTURE.html) · [Markdown](06-TYPESCRIPT-ARCHITECTURE.md) | Same safety rules with TypeScript and durable workflow execution |
| [Repositories and deployment](07-REPOSITORIES-AND-DEPLOYMENT.html) · [Markdown](07-REPOSITORIES-AND-DEPLOYMENT.md) | Where code lives, what runs separately, and how environments stay isolated |
| [Manual-build series](manual-build/00-START-HERE.html) · [Markdown](manual-build/00-START-HERE.md) | Foundations, each of the five projects, and production-demo operations |

Each reading edition embeds its own diagrams. Supporting source diagrams stay in this case study's assets folder. You do not need to follow a link to inspect an image inside a lesson.

## 3. The five projects

| Project | Responsibility | Proof to demonstrate |
|---|---|---|
| P1 — Privacy-Gated MCP Tools | Controlled reads, packet preview, and approved release | Transport never receives diagnoses |
| P2 — Permission-Aware RAG | Retrieve authorized policy and patient evidence | Wrong-patient content never enters the model context |
| P3 — A2A Care Coordination | Scheduling, claims, and transport tasks | Each specialist receives only its bounded input |
| P4 — Disclosure Workflow and Audit | Approval, revocation, delivery, recovery | Revoked queued disclosure is blocked; unknown delivery is reconciled |
| P5 — Patient Privacy Workspace | Explain recipients, fields, reasons, and release state | A reviewer can understand exactly what will be shared |

## 4. How this differs from Acme

Acme's key invariant was “do not issue the same credit twice.” HarborCare adds a more irreversible danger: **once information reaches an unauthorized recipient, retrying correctly cannot undo the exposure.** Prevention must happen before retrieval, before delegation, and again before disclosure—not just at the last button.

We reuse the architecture patterns, not Acme's financial assumptions. Delivery to a remote organization is not one local database transaction. A recorded release intent does not prove delivery; a delivery receipt does not prove the recipient can erase what it already saw.

## 5. Scope and completion

The first release supports one hospital, two synthetic patients, an assigned care team, one insurer, one transport provider, and an unrelated lookalike organization. All external delivery goes to a local test receiver. No real patient data should be pasted into a model, prompt, fixture, trace, screenshot, or hosting preview.

Complete the Python/hybrid path first. The TypeScript documents explain a separate implementation, not a second coordinator operating on the same patient disclosure. Real-world deployment requires organization-specific legal, security, clinical, vendor, and operational review beyond these teaching policies.
