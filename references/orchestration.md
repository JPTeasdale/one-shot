# One Shot Orchestration

## Contents

1. Root-agent responsibilities
2. Agent assignment envelope
3. Source synthesis
4. Phase 1: definition
5. Phase 2: expansion
6. Phase 3: technical design
7. Phase 4: implementation
8. Final integration and release
9. Recovery and state

## Root-agent responsibilities

Act as executive producer, orchestrator, and final integrator. Do not replace specialist roles with a single root-agent pass. Own these responsibilities:

- Establish the run root, initialize state, and protect source artifacts.
- Assign unique paths so parallel agents never edit the same file.
- Supply raw evidence rather than interpretations whenever a role can inspect the evidence directly.
- Verify that each assigned artifact exists and is substantive before accepting an agent's report.
- Relay reviewer findings to the responsible creator and enforce revision loops.
- Update `run-state.json` after artifacts and verdicts are safely written.
- Reconcile every accepted product decision into `decision-log.md` before marking a phase complete.
- Resolve deadlocks using the decision hierarchy in `SKILL.md`.
- Maintain one authoritative product direction and integrate cross-phase changes.

Use the available concurrency fully when work is independent. The three Phase 2 research tracks are designed to run simultaneously. Queue work when the environment has fewer slots.

## Agent assignment envelope

Give every subagent an assignment containing:

```text
Role: <role name>
Objective: <one bounded outcome>
Read: <source and prior-output paths>
Write only: <unique assigned path or directory>
Acceptance criteria: <observable checks>
Constraints: preserve sources; do not ask the user; cite evidence; no external production actions
Return: concise summary, files changed, unresolved risks
```

Do not tell an independent reviewer what result the creator hoped to achieve. Give the reviewer the raw sources, artifact under review, and rubric. Require this verdict block:

```text
Verdict: PASS | REVISE
Blocking findings:
Evidence:
Required changes:
Non-blocking opportunities:
```

Treat a missing verdict or an unsubstantiated `PASS` as `REVISE`.

## Source synthesis

Before Phase 1, inspect every relevant source listed in `source-manifest.json`. Create `source-digest.md` and `decision-log.md` at the run root. Capture:

- The hosts' desired outcome and intended audience
- Explicit requirements, non-goals, constraints, and taste signals
- Candidate product forms and interaction models
- Agreements, contradictions, unresolved branches, and discarded jokes/tangents
- Existing assets and what each can contribute
- Missing referenced artifacts and the assumption used instead

Reference transcript timestamps, speaker labels, page numbers, filenames, or other stable locators whenever available. Do not present invented detail as a quotation or source fact.

## Phase 1: definition

### ProjectDefinition

Assign a ProjectDefinition agent to derive the strongest coherent interpretation of the product. Have it write `phase-1/high-level-project-definition.md` using the output contract. Require all core ideas that survive the decision hierarchy, the artifact type, the primary experience, and a concrete definition of impressive completion.

### ProjectDefinitionReviewer

Assign a separate reviewer to compare the definition directly with all source evidence. Have it write `phase-1/reviews/review-NN.md` and assess:

- Vision fidelity and coverage of core features
- Resolution of contradictions
- Clarity of audience, product form, interaction, and outcome
- Whether the ambition is coherent rather than merely large
- Whether later agents could proceed without clarification

On `REVISE`, relay only the documented findings to ProjectDefinition, write the revised definition, and re-review. Continue until `PASS`. After four failed revisions, have the root agent adjudicate every blocker in `decision-log.md`, then assign a fresh final reviewer.

After `PASS`, have the root agent reconcile accepted Phase 1 choices into `decision-log.md`. Write `phase-1/final-review.md` as a compact acceptance record: name the authoritative definition and revision, link the accepted independent review, reproduce the exact verdict block, and carry forward non-blocking risks. Run the validator with `--through phase-1`; mark Phase 1 complete only when it passes.

## Phase 2: expansion

Run five required rounds and up to two additional rounds if high-impact gaps remain. In every round, launch three independent research tracks in parallel:

1. **Definition Research:** Identify known features that remain vague, hidden requirements, workflows, states, rules, and edge cases.
2. **New Capability Research:** Propose features not discussed that materially strengthen the product and fit its identity.
3. **Experience Magic Research:** Identify what would make the result feel like a demo, then propose specific moments, visuals, interactions, content, and polish that create delight and credibility.

Give each track the sources, accepted Phase 1 definition, current Phase 2 artifacts, and the current round focus. Write to distinct files under `phase-2/research/round-NN/`.

Use these round focuses:

| Round | Focus |
|---|---|
| 01 | Resolve the core product, audience journey, and feature mechanics |
| 02 | Build completeness: onboarding, states, content, operations, and edge cases |
| 03 | Create differentiation, signature moments, and visual/interaction magic |
| 04 | Remove demo smell: trust, accessibility, resilience, realism, and production depth |
| 05 | Unify the whole experience, eliminate conflicts, and maximize feasible polish |
| 06–07 | Target only high-impact gaps identified by the previous reviewer |

### ProjectExpansionGenerator

After the three research tracks finish, assign a generator to integrate only proposals that improve the coherent whole. Have it update the authoritative Phase 2 documents, feature files, traceability, inspiration index, and mockups.

Require it to:

- Define every feature's user value, behavior, states, edge cases, dependencies, and acceptance criteria.
- Search the web for current inspiration and save direct links, relevance notes, and licensing/use status.
- Generate original visual mockups rather than substituting mood-board prose.
- Maintain consistent names, information architecture, visual direction, and feature rules across all outputs.
- Reject attractive additions that dilute the product identity or make local realization implausible.

### ProjectExpansionReviewer

Assign an independent reviewer after each generator pass. Write `phase-2/reviews/round-NN-review-MM.md`. Review source fidelity, internal consistency, feature completeness, image/spec consistency, differentiation, feasibility, accessibility, and remaining demo smell.

On `REVISE`, send findings back to the generator and re-review the same round. On `PASS`, start the next required round. After Round 5, stop when the reviewer reports no blocking findings and no unaddressed high-impact opportunity. Otherwise run a targeted Round 6, then Round 7 if needed. After Round 7, require the root agent to adjudicate remaining tradeoffs and obtain a fresh final review.

Consolidate the accepted result into `phase-2/final-review.md` using the acceptance-record schema in `output-contract.md`. Reconcile accepted expansion decisions into `decision-log.md` and run the validator with `--through phase-2`. Do not advance merely because five rounds elapsed.

## Phase 3: technical design

Read `medium-routing.md` before assigning Phase 3. Determine whether the deliverable is software, physical, media/content, service/experience, or hybrid.

### TechnicalDesigner

Assign a specialist suited to the medium. Require current web research for unstable technical standards, APIs, prices, vendor specifications, print templates, and small-run services. Have it write:

- `phase-3/technical-design.md`
- `phase-3/architecture.md`
- `phase-3/production-plan.md`

Design local previewability first. Put deployment, ordering, printing, submission, or publishing at the end as explicit permission-gated operations.

### TechnicalDesignTaskWriter

Assign a task writer to convert the accepted product and design into a dependency-ordered task graph. Write `phase-3/tasks/task-index.md` and one file per task.

Every task must contain the schema in `output-contract.md`. Tasks must be small enough for one Implementor to complete and one reviewer to verify. Include integration and local-preview work throughout; place productionization last.

### TechnicalDesignReviewer

Independently evaluate every task. Batching tasks into one reviewer assignment is allowed, but give each task its own verdict. Check:

1. Does the task directly serve an accepted feature, quality attribute, or production requirement?
2. Is it executable from its declared inputs and dependencies?
3. Is it the right next step relative to predecessors?
4. Are completion and verification observable?
5. Does it preserve local previewability and defer permission-gated work?

Write verdicts to `phase-3/task-reviews.md`. On any `REVISE`, return findings to the task writer, revise the affected task graph, and re-review impacted tasks. Record the accepted design in `phase-3/final-review.md` using the acceptance-record schema, reconcile decisions, and run the validator with `--through phase-3`. Mark Phase 3 complete only when every task and that gate pass.

## Phase 4: implementation

Execute accepted tasks in dependency order. Parallelize only tasks that declare no overlapping files, shared mutable state, or unmet dependencies.

### Implementor

Create a fresh Implementor assignment for each task or tightly coupled task group. Choose a specialist appropriate to the medium and use relevant installed skills. Require the agent to implement, run task-level checks, and record results under `phase-4/task-runs/<task-id>/implementation.md`.

### ImplementationReviewer

Assign a separate reviewer to inspect the implementation, task contract, Phase 2 feature definition, and project vision. Require direct inspection and execution of relevant checks rather than trusting the implementation report. Write `phase-4/task-runs/<task-id>/review-NN.md`.

On `REVISE`, relay findings to the Implementor and repeat until `PASS`. Do not mark a task complete because files merely exist. After every passed task, integrate it into the working preview and run affected cross-task checks.

For permission-gated production tasks, implement all preparatory files, dry runs, checklists, and instructions. Mark the external action `READY-BUT-NOT-EXECUTED`; do not fabricate completion.

## Final integration and release

Assign a fresh FinalIntegrationReviewer to experience the product from `final-delivery/START-HERE.md` as a first-time user and compare it with the accepted Phase 1 and Phase 2 vision. Require it to inspect both happy paths and important alternate, empty, loading, error, accessibility, packaging, or physical-fit states that apply.

Write the verdict to `phase-4/final-review.md`. On `REVISE`, create corrective tasks and run them through the same Implementor/Reviewer loop.

After `PASS`:

1. Run all medium-specific tests and renders.
2. Write `phase-4/verification-report.md` with exact commands and results.
3. Write the Phase 4 acceptance record, reconcile decisions, and run the validator with `--through phase-4`.
4. Complete `final-delivery/START-HERE.md`, `artifact-inventory.md`, and `production-readiness.md`.
5. Run `scripts/validate_run.py <RUN_ROOT> --through final --report <RUN_ROOT>/final-delivery/validation-report.json`.
6. Fix every reported error and rerun until clean.

## Recovery and state

Use `run-state.json` as a checkpoint, not as proof. Artifacts and reviewer verdicts are authoritative. On resume:

1. Re-run the validator through the phase recorded as complete.
2. Downgrade any phase whose required artifacts or pass verdict are missing.
3. Inspect partial agent outputs and keep only evidence-backed work.
4. Continue from the earliest incomplete gate.

Never delete or overwrite source artifacts during recovery. Preserve rejected decisions and review history; only authoritative consolidated documents should be replaced.
