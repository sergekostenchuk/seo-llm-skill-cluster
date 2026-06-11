# MVP Eval Summary

date: 2026-06-11
task: T-016
status: complete

## Scope

MVP v0.1 eval coverage includes:

- `site-growth-orchestrator`
- `semantic-core-architect`
- `information-architecture-seo`
- `internal-link-graph-architect`
- `technical-seo-schema-engineer`
- `llm-friendly-site-architect`
- `seo-regression-validator`
- `cluster-consistency-linter`

Deferred skills are excluded from MVP eval scope:

- editorial quality gate;
- UX journey architect;
- credential-free monitoring baseline;
- LLM citation monitoring;
- external authority placement;
- backlink quality validation.

## Coverage Rule

Each MVP skill must have at least:

- 3 positive forward-test prompts;
- 3 negative/refusal prompts.

The orchestrator also needs end-to-end scenario prompts. The shared suite includes three end-to-end scenarios: AI news publication architecture, B2B SaaS growth architecture, and personal/project portfolio entity architecture.

## Automation

Run:

```bash
python3 ./plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py . --report ./plans/seo-llm-skill-cluster/evals/mvp-eval-results.json
```

The verifier combines per-skill `evals.json` files with shared evals for `cluster-consistency-linter`.

## Result

`mvp-eval-results.json` passes:

- 8 MVP skill/workflow units covered.
- 3 end-to-end scenarios covered.
- Every MVP unit has at least 3 positive and 3 negative cases.
- Deferred skills remain excluded from MVP eval scope.
