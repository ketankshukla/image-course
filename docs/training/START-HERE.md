# Your Practical Software Engineering Workshops

## At a glance

Start with one workshop, perform its exercise, and keep a short evidence record before moving on. These are separate reading documents, not one enormous course. Each has a blue HTML edition, a Markdown source, and local practice material. Nothing is deployed automatically.

## The learning order

| Order | Workshop | What you will practice |
|---|---|---|
| 1 | [CI/CD](ci-cd/CI-CD-FROM-SOLO-TO-TEAM.md) | PR checks, staging, approval and release rejection |
| 2 | [Debugging](debugging/DEBUGGING-WITHOUT-GUESSING.md) | Reproduce, trace, inspect, fix and verify |
| 3 | [Testing](testing/TESTING-THAT-CATCHES-REAL-PROBLEMS.md) | Meaningful assertions and forbidden side effects |
| 4 | [HTTP and API Development](http-api/HTTP-AND-API-DEVELOPMENT.md) | Read requests, validate input, and test a real local API. |
| 5 | [Git Collaboration and Code Review](git-team/GIT-COLLABORATION-AND-REVIEW.md) | Resolve a real conflict and undo a change without erasing shared history. |
| 6 | [Databases and Safe Schema Changes](databases/DATABASES-AND-SAFE-MIGRATIONS.md) | Practice constraints, transactions, compatible migration, and restoration. |
| 7 | [Authentication, Authorization, and Secrets](identity/AUTHENTICATION-AUTHORIZATION-AND-SECRETS.md) | Separate identity from resource access and field disclosure. |
| 8 | [Configuration and Environments](configuration/CONFIGURATION-AND-ENVIRONMENTS.md) | Parse settings deliberately and reject unsafe combinations. |
| 9 | [Background Jobs and Reliable Workflows](background-jobs/BACKGROUND-JOBS-AND-RELIABLE-WORKFLOWS.md) | Understand retries, duplicate delivery, and transaction boundaries. |
| 10 | [Logging, Monitoring, and Incident Response](observability/LOGGING-MONITORING-AND-INCIDENTS.md) | Trace synthetic failures and write an actionable incident response. |
| 11 | [Docker and Local Environments](docker/DOCKER-AND-LOCAL-ENVIRONMENTS.md) | Build a small service image and reason about ports and storage. |
| 12 | [Software Design and Refactoring](refactoring/SOFTWARE-DESIGN-AND-REFACTORING.md) | Extract responsibilities while preserving explicit behavior. |
| 13 | [Accessible and Resilient Interfaces](accessibility/ACCESSIBLE-AND-RESILIENT-INTERFACES.md) | Practice keyboard use, status feedback, failure, and retry. |
| 14 | [Performance Investigation](performance/PERFORMANCE-INVESTIGATION.md) | Measure query behavior and verify correctness after indexing. |
| 15 | [Reading an Unfamiliar Codebase](codebase/READING-AN-UNFAMILIAR-CODEBASE.md) | Trace a feature, establish a baseline, and plan a small first change. |

## How to use each workshop

Read the scenario first. Run the smallest exercise. Predict the result before changing code. Record the observed result and explain any difference. Finish the independent challenge without immediately asking AI for the finished solution.

The JavaScript labs use Node; the newer Python labs use the standard library. Git practice also needs Git. The Docker workshop requires Docker, which was not available during authoring. The accessibility workshop contains a browser-only simulator. No exercise needs real patient data, real credentials, or access to your personal files.

## Understand the verification boundary

The runnable examples are deliberately small. Passing their checks is evidence about those examples, not production certification. Some exercises demonstrate expected failures or leave a final challenge unsolved. Docker image build/run and real independent PR approvals require your own environment and participation.

| Workshop | Important limitation |
|---|---|
| HTTP and API Development | Local in-memory API; not a production authentication or persistence system. |
| Git Collaboration and Code Review | Disposable local repository; no real PR, reviewer, remote, or push. |
| Databases and Safe Schema Changes | In-memory SQLite rehearsal; no production database migration. |
| Authentication, Authorization, and Secrets | Authorization fixture model only; login and token verification are not implemented. |
| Configuration and Environments | Synthetic settings; no cloud environment changes or network connectivity checks. |
| Background Jobs and Reliable Workflows | Sequential database-local model; not exactly-once external execution. |
| Logging, Monitoring, and Incident Response | Synthetic log model; no collector, dashboard, or live alert installed. |
| Docker and Local Environments | Docker unavailable here: image build and container run remain unverified. |
| Software Design and Refactoring | Three characterization cases; not exhaustive equivalence proof. |
| Accessible and Resilient Interfaces | Browser-only simulation; no real operation or complete accessibility audit. |
| Performance Investigation | Local synthetic query measurements; no promised production speedup. |
| Reading an Unfamiliar Codebase | Tiny teaching repository; the final whitespace enhancement is unsolved. |

## Your evidence notebook

For every workshop record: requirement, exact command or interaction, expected result, actual result, explanation, and remaining uncertainty. A useful portfolio demonstration includes this reasoning as well as screenshots or green test output.

## Where the materials live

Each workshop is a direct subfolder of `docs/training`. Its `exercises` folder contains practice code; its `assets` folder contains original diagrams. HTML files are standalone reading editions with embedded styles and diagrams. The website publishes only the Markdown entries explicitly listed in the library publication manifest. Practice code is not automatically exposed as a website download.

The master document directory also lists these workshops. Use the source repository to copy exercise folders; the reading pages explain how to run them locally.
