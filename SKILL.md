---
name: one-shot
description: Autonomously transform AI One Shot Podcast transcripts and accompanying artifacts into a fully researched, expanded, technically designed, implemented, independently reviewed, and locally previewable product. Use when Justin and John provide a One Shot recording folder, podcast brainstorm, transcript, or rough product artifacts and ask Codex to realize the idea end-to-end without clarification; also use to resume an existing one-shot-output run.
---

# One Shot

## Mission

Turn one podcast conversation and its supporting artifacts into the most impressive coherent product that can be completed and demonstrated locally with the available tools. Do not stop at a summary, concept, specification, mockup, or MVP when a fuller implementation is feasible.

## Honor the operating contract

- Work without asking Justin or John to resolve creative ambiguity. Inspect the evidence, make the strongest reasonable decision, and record it.
- Preserve all supplied source artifacts as read-only evidence.
- Use independent subagents for creation, research, review, technical design, and implementation. Keep the root agent as orchestrator and final integrator.
- Expand beyond the spoken idea while preserving its core identity. Prefer coherent depth over a pile of disconnected features.
- Create actual mockups and an actual local product preview, not descriptions of what could be made.
- Treat deployment, purchasing, printing, account creation, uploads, and other irreversible or external production actions as permission-gated. Prepare them but do not execute them without authority.
- Persist work after every stage so the run can survive compaction, interruption, or agent failure.

## Start or resume the run

1. Resolve `SOURCE_ROOT` from the folder named by the user; otherwise use the current working directory.
2. Default `RUN_ROOT` to `<SOURCE_ROOT>/one-shot-output`. Use another location only when the user explicitly supplies one.
3. Read [references/output-contract.md](references/output-contract.md) and [references/orchestration.md](references/orchestration.md) completely.
4. Run `scripts/initialize_run.py <SOURCE_ROOT>` before creating project artifacts. If a run already exists, preserve it and resume from the earliest incomplete quality gate.
5. Inspect `source-manifest.json`, then read every relevant transcript and artifact. Use the appropriate installed document, PDF, spreadsheet, presentation, image, audio, or code skill when available.
6. Identify references to missing artifacts, but do not pause. Record the gap and continue using the available evidence.

## Resolve ambiguity deliberately

Apply this precedence order:

1. Explicit hard constraints and clearly stated non-goals
2. Ideas repeatedly endorsed by both hosts
3. Concrete examples, sketches, and generated artifacts
4. The interpretation that creates the most coherent, distinctive, and locally demonstrable result

Do not silently average conflicting ideas. Choose one direction and record the conflict, decision, evidence, and consequence in `decision-log.md`. Treat stray brainstorming as optional unless it strengthens the chosen product.

## Execute the studio workflow

Follow [references/orchestration.md](references/orchestration.md) for agent roles, iteration mechanics, and handoffs. Satisfy [references/output-contract.md](references/output-contract.md) exactly.

1. **Define:** Derive and independently review the high-level product definition.
2. **Expand:** Run at least five focused research/generation/review rounds. Define known features, invent valuable missing capabilities, eliminate “demo smell,” curate cited inspiration, and generate visual mockups.
3. **Design:** Read [references/medium-routing.md](references/medium-routing.md), select the correct implementation/production path, research current technical or manufacturing constraints, and create an individually reviewed task graph.
4. **Implement:** Execute tasks in dependency order with an Implementor/ImplementationReviewer loop for every task. Integrate continuously and maintain a working local preview.
5. **Release locally:** Read [references/quality-gates.md](references/quality-gates.md), run final independent review and deterministic validation, then package a start-here guide, artifact inventory, and production-readiness handoff.

After each accepted phase, run the validator with that phase's scope (`--through phase-1`, `phase-2`, `phase-3`, or `phase-4`). Use `--through final` only after the final-delivery artifacts exist.

## Use subagents correctly

- Give each subagent one bounded role, the raw evidence paths it needs, an assigned output path, and explicit acceptance criteria.
- Let parallel agents write only to distinct files. Let the root agent own authoritative merges and state transitions.
- Give reviewers the source artifacts and the candidate output, not the creator's hidden rationale. Require `PASS` or `REVISE` with evidence.
- Relay review findings through files or the root orchestrator; do not assume agents can coordinate implicitly.
- Respect available concurrency. Queue roles when necessary rather than weakening role separation.
- If subagents are unavailable, perform the roles serially with fresh context boundaries and disclose the fallback in the run log.

## Apply medium-specific expertise

Use relevant installed skills and tools rather than recreating their workflows. In particular:

- Use image generation for original mockups and visual variants.
- Use web research for current products, standards, vendor specifications, and inspiration; prefer primary sources and preserve citations.
- Use dedicated skills for sites, software development, documents, PDFs, presentations, spreadsheets, and other final media when applicable.
- Use [references/medium-routing.md](references/medium-routing.md) for software, physical, media, service, and hybrid products.

## Finish only when the product is real

Run `scripts/validate_run.py <RUN_ROOT> --through final`. Do not claim completion while it reports errors.

Finish only when:

- Every phase has an independent `PASS` verdict.
- The traceability matrix connects source evidence to requirements, features, tasks, and implemented artifacts.
- The primary experience is usable locally from `final-delivery/START-HERE.md`.
- Required files contain no placeholders, fabricated citations, or unsupported completion claims.
- Production-only actions are either completed with authorization or explicitly packaged as ready-but-not-executed.

Report the local preview path and command, the finished deliverables, the validation result, and any permission-gated production step.

## Resources

- `scripts/initialize_run.py`: create or resume a safe output structure and inventory source artifacts.
- `scripts/validate_run.py`: check phase contracts, review verdicts, expansion rounds, mockups, implementation content, and final handoff.
- `references/orchestration.md`: run the multi-agent studio and its revision loops.
- `references/output-contract.md`: use the authoritative directory and document schemas.
- `references/quality-gates.md`: apply review rubrics and release criteria.
- `references/medium-routing.md`: choose implementation and production paths by product medium.
