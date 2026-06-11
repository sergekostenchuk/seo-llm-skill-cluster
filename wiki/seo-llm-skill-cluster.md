# SEO/LLM Skill Cluster

status: staged MVP
updated: 2026-06-11
source_plan: `./plans/seo-llm-skill-cluster/TASK-PLAN.md`

## What This Cluster Is

The SEO/LLM skill cluster is a staged group of Codex skills for building and auditing public
websites that need to work for:

- human readers;
- search engines;
- LLM search and citation agents;
- site owners who need repeatable reports and validation.

The cluster is not an SEO-spam toolkit. It is evidence-first and keeps user-visible content
as the source of truth.

## MVP Skills

- `site-growth-orchestrator`
- `semantic-core-architect`
- `information-architecture-seo`
- `internal-link-graph-architect`
- `technical-seo-schema-engineer`
- `llm-friendly-site-architect`
- `seo-regression-validator`

## Follow-Up Skills Now Staged

- `editorial-quality-gate`
- `ux-journey-architect`
- `server-log-crawler-analyst`
- `llm-citation-monitor`
- `external-authority-placement-scout`
- `backlink-quality-validator`

The MVP also includes a cluster consistency linter and shared eval verifier in:

- `./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py`
- `./plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py`

## Central Contract

The orchestrator routes work. Specialist skills own their layers.

For the mlllm.io-style publishing model, the protected contract is:

- one short news brief;
- one expanded longform article;
- topics and homepage teasers link and summarize, but do not create duplicate article bodies.

SEO and LLM-friendly additions must strengthen that model with metadata, schema, links, and
agent-readable files. They must not multiply near-duplicate content.

## Evidence Model

Reports should separate:

- `Observed`: directly checked fact;
- `Inferred`: conclusion drawn from observed facts;
- `Open`: not verified yet.

Ranking, crawler, citation, and schema claims require a timestamped source or command.

## Current Package State

The skills are staged in:

- `./skills`

They are not installed into:

- `<codex-skills-dir>`

Installation requires explicit user approval and the runbook:

- `./plans/seo-llm-skill-cluster/install-rollback.md`

Current staging manifest:

- `./plans/seo-llm-skill-cluster/current-staging-manifest.json`

## Key Artifacts

- Architecture: `./plans/seo-llm-skill-cluster/cluster-architecture.md`
- Artifact schemas: `./plans/seo-llm-skill-cluster/assets/artifact-schemas.md`
- Trigger map: `./plans/seo-llm-skill-cluster/trigger-map.yaml`
- Freshness policy: `./plans/seo-llm-skill-cluster/freshness-policy.md`
- MVP release scope: `./plans/seo-llm-skill-cluster/mvp-release-scope.md`
- Operating handbook: `./plans/seo-llm-skill-cluster/operating-handbook.md`

## Validation Snapshot

Latest T-017 validation:

- production linter: pass for 7 staged skills;
- cluster consistency linter: 0 critical issues, 0 warnings;
- MVP eval verifier: pass for 8 MVP units and 3 end-to-end cases;
- Codex `quick_validate.py`: blocked by missing local `yaml` Python module.

Final post-plan validation:

- TASK-PLAN: 25/25 tasks done, 0 register/block mismatches;
- production linter: pass for 13 staged skills;
- eval JSON: pass for all staged skills;
- cluster consistency linter: 13 staged skills checked, 0 critical issues, 0 warnings.

## Next Work

Next meaningful work:

1. Complete `T-025`: prepare and publish a sanitized GitHub repository.
2. Decide whether to install staged skills into `<codex-skills-dir>`.
3. If installing, follow the install/rollback runbook and keep backups of any existing skill folders.
4. Add credentialed monitoring integrations only after access/privacy approval.
5. Use authority skills in dry-run mode until a specific external action is approved.

## GitHub Publication Gate

`T-025` is intentionally draft. It cannot be completed until:

- target GitHub repository/remote is explicit;
- public package scope is approved;
- local paths and sensitive data are sanitized;
- README and motivation text are reviewed;
- user explicitly approves the push.

Required publication narrative:

- mention that the work was managed with `task-plan-v2-dashboard`;
- link to `https://github.com/sergekostenchuk/task-plan-v2-dashboard`;
- explain that the dashboard gives a human operator enough task visibility to step away from constant model monitoring during long runs, even if just to make coffee.
