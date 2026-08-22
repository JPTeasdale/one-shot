# One Shot Output Contract

## Contents

1. Directory contract
2. Shared document rules
3. Phase 1 schema
4. Phase 2 schemas
5. Phase 3 schemas
6. Phase 4 and final-delivery schemas
7. State schema

## Directory contract

Create this structure under `RUN_ROOT`:

```text
one-shot-output/
├── source-manifest.json
├── run-state.json
├── source-digest.md
├── decision-log.md
├── phase-1/
│   ├── high-level-project-definition.md
│   ├── reviews/
│   └── final-review.md
├── phase-2/
│   ├── product-definition.md
│   ├── experience-principles.md
│   ├── feature-index.md
│   ├── traceability.md
│   ├── features/
│   ├── research/round-01/ ... round-05/
│   ├── mockups/generated/
│   ├── mockups/mockup-index.md
│   ├── inspiration/inspiration-index.md
│   ├── reviews/
│   └── final-review.md
├── phase-3/
│   ├── technical-design.md
│   ├── architecture.md
│   ├── production-plan.md
│   ├── tasks/task-index.md
│   ├── tasks/T-*.md
│   ├── task-reviews.md
│   └── final-review.md
├── phase-4/
│   ├── product/
│   ├── task-runs/<task-id>/
│   ├── local-preview.md
│   ├── verification-report.md
│   └── final-review.md
└── final-delivery/
    ├── START-HERE.md
    ├── artifact-inventory.md
    ├── production-readiness.md
    └── validation-report.json
```

Keep intermediate role output in the named phase directories. Put the actual implemented deliverable under `phase-4/product/`. Do not duplicate large deliverables into `final-delivery`; link to them with relative paths.

## Shared document rules

- Begin each document with its title, status, and last-updated date.
- Use stable IDs: requirements `R-###`, features `F-###`, tasks `T-###`, decisions `D-###`.
- Link related IDs rather than relying on similar wording.
- Cite source evidence using a filename plus timestamp, page, slide, cell range, or section when possible.
- Cite web research with a direct URL, access date, and relevance note.
- Distinguish fact, host intent, inference, and newly proposed enhancement.
- Do not use `TODO`, `TBD`, lorem ipsum, fake citations, or unlabeled placeholder content in an accepted artifact.

### Final review acceptance records

Write each phase's `final-review.md` only after an independent review passes. Name the authoritative artifact and revision, link the accepted review file, summarize prior revision history, reproduce the exact universal verdict block with `Verdict: PASS`, and list residual non-blocking risks to carry forward. Do not overwrite the underlying independent review.

## Phase 1 schema

Write `high-level-project-definition.md` with:

1. One-sentence product definition
2. Product form and final artifact types
3. Target users and jobs to be done
4. Core experience from entry to successful outcome
5. Core requirements and features discussed by the hosts
6. Chosen resolution of important contradictions
7. Experience and taste principles
8. Explicit non-goals and boundaries
9. Definition of an impressive completed result
10. Assumptions and source-evidence map

Do not prescribe a technical stack unless the source makes it a product requirement.

## Phase 2 schemas

### Product definition

Make `product-definition.md` the authoritative expanded specification. Include product promise, audiences, end-to-end journeys, information/content model, capability map, system rules, cross-feature behaviors, trust and safety, accessibility, operational needs, and success criteria.

### Experience principles

For every principle in `experience-principles.md`, state the principle, user effect, concrete manifestations, and anti-patterns. Include a visual direction described precisely enough to keep mockups consistent without locking implementation prematurely.

### Feature index and feature files

List every accepted feature in `feature-index.md` with ID, name, priority, source (`host`, `inferred`, or `expansion`), dependencies, and feature-file link.

Write one `features/F-###-slug.md` per feature containing:

1. User value and rationale
2. Related source evidence and requirements
3. User stories or scenarios
4. Detailed behavior and rules
5. Entry, happy path, alternate, empty, loading, error, and recovery states as applicable
6. Content/data needs
7. Accessibility and trust considerations
8. Dependencies and cross-feature interactions
9. Acceptance criteria
10. Mockup references

### Traceability

Use a table in `traceability.md`:

```text
Evidence locator | Requirement ID | Feature ID | Task ID | Implemented artifact | Verification
```

Allow blank Task and implementation columns during Phase 2, but complete them before final release.

### Mockup index

For each generated mockup, record filename, product surface/moment, feature IDs, state depicted, generation/reference inputs, and consistency notes. Include enough mockups to demonstrate the primary journey, signature moments, and materially different states or physical views.

### Inspiration index

For each inspiration source, record title, direct URL, access date, relevant lesson, what not to copy, and license/use status. Prefer linking over downloading. Never imply that inspiration imagery is original work.

## Phase 3 schemas

### Technical design

Specify chosen medium/stack/process, rationale, components, interfaces, data/content model, accessibility, privacy/security, performance or physical tolerances, testing/QA, local preview, packaging, and key risks.

### Architecture

Represent component ownership, dependencies, and data/material flow. Use a diagram when relationships are non-trivial. Define file/package boundaries and integration contracts.

### Production plan

Separate locally executable work from permission-gated production. For external services, include current official specification links, small-run eligibility when relevant, template/version details, export settings, cost/lead-time notes when available, and a dry-run checklist. Do not claim an order, upload, or deployment occurred unless it did.

### Task index and task files

List task ID, title, status, dependencies, feature/requirement coverage, assigned output, and review verdict in `task-index.md`.

Write each task file with:

```text
Task ID and title
Objective
Why this task exists
Requirements/features served
Dependencies and required inputs
Files or artifacts allowed to change
Implementation instructions and constraints
Acceptance criteria
Verification commands or inspection procedure
Local-preview impact
Permission/external-action classification
Completion evidence to record
```

Make acceptance criteria observable and binary. A task may not depend on an undocumented future decision.

### Task reviews

Give every task an individual `PASS` or `REVISE` verdict and findings. Record the task version or content hash reviewed so later edits invalidate stale approval.

## Phase 4 and final-delivery schemas

### Product

Place the working product, print package, media master, or hybrid deliverable under `phase-4/product/`. Include only files needed to use, build, inspect, or produce it. Preserve editable masters when the medium supports them.

### Task runs

For every task, retain implementation evidence, exact checks executed, reviewer findings, revisions, and final verdict under `task-runs/<task-id>/`.

### Local preview

Write `local-preview.md` with prerequisites, exact setup and launch/open commands, expected result, sample data or inputs, verification steps, and troubleshooting. Require a path that works without production credentials or irreversible actions.

### Verification report

Record environment, commands, render/inspection procedures, results, known limitations, and evidence paths. Say `not run` rather than inventing a result.

### START-HERE

Write for a first-time user. Explain what was built, where it is, how to experience it locally, the primary journey, and where to find deeper artifacts. Put the shortest successful preview path first.

### Artifact inventory

List each final artifact, path, purpose, format, editable-master status, validation status, and intended next use.

### Production readiness

Separate:

- Complete local deliverables
- Production-ready but unexecuted actions
- Exact authorization, credentials, payment, or external coordination required
- Final production checklist and rollback/recovery considerations

Do not describe optional future enhancements as incomplete required work.

## State schema

Use `run-state.json` to record source/run roots, initialization timestamp, current phase, per-phase status, latest accepted review paths, and last validation result. Use only `pending`, `in_progress`, `complete`, or `blocked_by_permission` as phase status values. Never mark a phase complete before its final review and deterministic gate pass.
