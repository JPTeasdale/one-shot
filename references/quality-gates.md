# One Shot Quality Gates

Apply these gates in addition to medium-specific tests. Review evidence, not confidence.

## Universal review verdict

Use this exact structure in accepted review files:

```text
Verdict: PASS | REVISE
Blocking findings:
Evidence:
Required changes:
Non-blocking opportunities:
```

Use `PASS` only when blocking findings and required changes are explicitly `None`.

## Phase 1 gate

- Cover every explicit core requirement or record why it was rejected.
- Resolve important contradictions instead of hiding them.
- Define audience, product form, interaction model, and successful outcome.
- Describe one coherent product another team can expand without clarification.
- Define impressive completion in observable terms.

## Phase 2 gate

- Complete five independently reviewed expansion rounds.
- Give every accepted feature behavior, states, dependencies, and acceptance criteria.
- Include original generated mockups covering the main journey and signature moments.
- Keep visual vocabulary, product names, information architecture, and feature rules consistent.
- Cite inspiration and separate it from generated work.
- Address applicable onboarding, realistic content/data, empty/loading/error/recovery states, responsiveness, accessibility, trust, privacy, and operational needs.
- Leave no high-impact feature gap or obvious “demo smell.”
- Add magic through meaningful experience, not superficial animation or feature count.

## Phase 3 gate

- Select a feasible medium, stack, or production process and explain the tradeoff.
- Use current official specifications where standards or vendor constraints can change.
- Support a complete local preview before any external production action.
- Map every accepted feature and cross-cutting quality attribute to tasks.
- Give every task inputs, dependencies, allowed outputs, binary acceptance criteria, and verification.
- Individually review every task and put productionization last.

## Phase 4 task gate

- Match the implementation to the accepted task and feature behavior.
- Actually run relevant automated checks, renders, measurements, or inspections.
- Integrate with prior work without regressing the working preview.
- Handle applicable alternate and failure states rather than only a staged happy path.
- Use final-quality content or clearly labeled, intentional sample data.
- Introduce no unapproved external action, secret, paid operation, or destructive change.

## Demo-smell audit

Fail applicable products for any of these:

- Dead controls, disconnected screens, fake navigation, or unimplemented primary paths
- Placeholder copy, arbitrary sample content, fabricated metrics, or fake external integration claims
- Only one carefully staged state when real use requires several
- Missing onboarding, empty, loading, error, recovery, responsive, accessible, or print-production behavior
- Inconsistent naming, visual language, feature rules, dimensions, or export settings
- A beautiful shell without substantive user value
- A technically complete artifact that cannot be opened, run, inspected, or understood locally

## Final experiential gate

Have a fresh reviewer begin only with `final-delivery/START-HERE.md`. Require the reviewer to:

1. Reach the primary value without hidden instructions.
2. Exercise the core journey and important alternative states.
3. Compare the experience with the Phase 1 promise and Phase 2 specification.
4. Inspect visual and interaction consistency or physical/media production quality.
5. Verify claims in the artifact inventory and production-readiness report.

Create corrective tasks for every blocking issue and run the normal implementation/review loop.

## Deterministic gate

Run:

```bash
python3 <skill-dir>/scripts/validate_run.py <RUN_ROOT> --through final --report <RUN_ROOT>/final-delivery/validation-report.json
```

Treat a nonzero exit status as incomplete. The validator checks structure and basic evidence; it never replaces expert review, actual execution, rendering, measurement, or user-path inspection.
