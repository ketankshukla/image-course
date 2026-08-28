# Your Organized Learning Workspace

## At a glance

The course website remains one Git repository. Its ten course collections live together under `courses`. All case-study documents live under `docs/case-studies`, separated into Acme, HarborCare, FilePilot, and EvidenceDesk. These are teaching collections; adding them does not install or deploy their proposed applications.

```text
image-course/
├── app/                          Course website pages and interface
├── lib/                          Website helpers and types
├── scripts/                      Content builders and maintenance tools
├── data/                         Generated navigation manifest
├── public/library/               Hashed collection JSON, search and flattened WebP
├── courses/
│   ├── Visual Course 01/
│   ├── Visual Course 02/
│   ├── Visual Course 03/
│   ├── Visual Course 04/
│   ├── Visual Course 05/
│   ├── Visual Course 06/
│   ├── Visual Course 07/
│   ├── Visual Course 08/
│   ├── Visual Course 09/
│   └── Visual Course 10/
├── docs/
│   ├── FOLDER-STRUCTURE.md        This editable guide
│   ├── FOLDER-STRUCTURE.html      Its readable edition
│   ├── assets/                   Shared document style and HTML template
│   ├── general/                  Broader planning documents
│   └── case-studies/
│       ├── acme/
│       │   ├── strategy/         Original project strategy documents
│       │   ├── manual-build/     Original step-by-step construction guides
│       │   ├── architecture-assets/
│       │   ├── companion-architecture-assets/
│       │   ├── repository-assets/
│       │   ├── beginner-assets/
│       │   └── ...               Main architecture, deployment and beginner guides
│       ├── filepilot/
│       │   ├── collection.json   Website publication allowlist
│       │   ├── 00-START-HERE.md / .html
│       │   ├── ...               Strategy, legend, safety and architecture guides
│       │   ├── manual-build/     Eight sequential workbook documents
│       │   └── assets/           Four original architecture diagrams
│       ├── evidence-desk/
│       │   ├── collection.json   Eleven-chapter publication allowlist
│       │   ├── 00-START-HERE.md / .html
│       │   ├── ...               Five layers, architecture, build and release guides
│       │   ├── lab/              Offline Python exercise with eleven tests
│       │   └── assets/           Nine original teaching diagrams
│       └── hospital/
│           ├── 00-START-HERE.md / .html
│           ├── 01-PROJECT-STRATEGY.md / .html
│           ├── 02-PLAIN-ENGLISH-AND-LEGEND.md / .html
│           ├── 03-PRIVACY-POLICY-AND-TESTS.md / .html
│           ├── 04-PYTHON-ARCHITECTURE.md / .html
│           ├── 05-HYBRID-ARCHITECTURE.md / .html
│           ├── 06-TYPESCRIPT-ARCHITECTURE.md / .html
│           ├── 07-REPOSITORIES-AND-DEPLOYMENT.md / .html
│           ├── manual-build/     Eight sequential workbook documents
│           └── assets/           Four original architecture diagrams
├── README.md                     Project entry point and commands
├── AGENTS.md                     Workspace maintenance instructions
├── package.json                  Website dependencies and commands
└── ...                           Framework, TypeScript and Git configuration
```

## 1. Start reading here

- [FilePilot safe file-automation collection](case-studies/filepilot/00-START-HERE.html)
- [EvidenceDesk — five layers of AI engineering](case-studies/evidence-desk/00-START-HERE.html)
- [FilePilot manual-build series](case-studies/filepilot/manual-build/00-START-HERE.html)
- [HarborCare hospital case-study collection](case-studies/hospital/00-START-HERE.html)
- [HarborCare manual-build series](case-studies/hospital/manual-build/00-START-HERE.html)
- [Acme project strategy](case-studies/acme/strategy/PROJECT-STRATEGY.html)
- [Acme whole-project beginner explanation](case-studies/acme/THE-WHOLE-PROJECT-IN-PLAIN-ENGLISH.html)
- [Acme manual-build series](case-studies/acme/manual-build/00-START-HERE.html)

Open the HTML edition for reading and the Markdown edition for editing. HTML documents embed their diagrams and styles, so their presentation does not depend on loading a separate image from another page. Links to other documents still require those neighboring files to remain available.

## 2. The ten folders are courses, not ten application repositories

Each course retains its own `diagrams` and `diagram-docs` folders, plus its existing source JSON, generation helpers or local bundles where present. Keeping these together preserves relative image references and makes the source of a lesson easy to find.

The 244 original course diagrams remain source assets. Website images now live under `public/library/images` as flattened WebP files, including case-study diagrams. Legacy `public/images` and `public/courses` outputs are retained locally but no longer requested by the website and are excluded from Vercel uploads. Do not delete original diagrams: they are build inputs.

Some original Word, PDF and archive files are ignored by Git. They were moved with their course or document folder and remain local; this work does not silently change their tracking policy or promise they will be uploaded by a future push.

## 3. What moved

| Previous location | Current location |
|---|---|
| Ten root-level `Visual Course NN` folders | `courses/Visual Course NN` |
| `project-architecture` | `docs/case-studies/acme` |
| Root general documents | `docs/general` |
| Acme strategy files formerly among general documents | `docs/case-studies/acme/strategy` |
| Root `regen_volume8.py` | `scripts/regen_volume8.py` |
| Root `volume8_manual_data.json` | `courses/Visual Course 08/volume8_manual_data.json` |

The main move script checked SHA-256 hashes before and after moving every file in its inventory. That checked preservation of file contents, including local ignored assets. Necessary path updates to generators and documentation were made afterward. No course was replaced with a newly generated lesson set.

Old browser tabs pointing at root-level documents will no longer resolve. Use the reading links above to reopen their new locations.

## 4. Why some folders stay in the root

`app`, `public`, framework configuration and the package files are part of the website's normal working structure. Moving everything into decorative folders would require unnecessary framework changes. `data` is also intentionally at the location used by the website.

`node_modules`, `.next`, `.git` and other tool-owned or ignored directories may exist locally. They are not teaching materials and were not moved into the document collection. Existing unrelated root files and configuration were preserved.

## 5. Rebuilding after an edit

From the repository root, run `npm run build:content` to regenerate course content, compressed diagrams, navigation and search data. Run `npm run build` for the complete production website build. The content builder now resolves configured course names inside `courses`.

Run `python scripts/build_documents.py` to rebuild the HarborCare HTML editions and this folder guide. It requires Pandoc and keeps each Markdown document beside its HTML counterpart. The existing Acme asset folders retain their own rebuild scripts, now beneath the new case-study location.

Run `python scripts/build_documents.py --collection filepilot` for FilePilot's 16 HTML editions and the workspace guides. These use the larger blue reading style. The verifier checks both supported collections and their executable foundation exercises.

Run `python scripts/verify_documents.py` to check the new document collection, embedded assets, local links and learning exercise. These checks complement—not replace—visual and browser testing of a future application.

The website now integrates these materials through explicit `collection.json` publication manifests. Case-study folders with a manifest are automatically discovered; unlisted drafts stay unpublished. The local HTML editions remain independent reading copies. See [Publishing a New Case Study](PUBLISHING-CASE-STUDIES.html) for the complete workflow. The website build is Node-only; Python and Pandoc are optional local document tools.

## 6. Where future application code belongs

Keep this repository for learning content. When implementation begins, create sibling repositories such as `harborcare-platform` for Python/hybrid and, later, `harborcare-platform-ts` for the alternative. The five projects can be modules or services within each application repository. They do not require five nested Git repositories.

Acme's future application repositories remain separate from HarborCare's. Sharing educational patterns does not mean sharing patient fixtures, credentials, deployments or release databases. None of those future repositories has been created by this documentation work.

FilePilot's future Python/hybrid code belongs in a sibling `filepilot-platform` repository. Its optional TypeScript counterpart belongs in `filepilot-platform-ts`. Managed files, local indexes, approvals and operation journals must remain outside the teaching repository and application checkouts. See [FilePilot repositories and deployment](case-studies/filepilot/07-REPOSITORIES-AND-DEPLOYMENT.html).
