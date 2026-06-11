# SEO/LLM Skill Cluster Install And Rollback

date: 2026-06-11
task: T-017
status: staged package ready; production install not performed

## Package State

The MVP skills are staged under:

```text
./skills/
```

Production install target is:

```text
<codex-skills-dir>/
```

No production install was performed in T-017. Installation requires explicit user approval.

## Pre-Install Validation

Run:

```bash
python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json
```

Run production linter for each staged skill:

```bash
for d in ./skills/*; do python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py "$d" --json || exit 1; done
```

Run MVP eval coverage:

```bash
MVP_EVAL_TIMESTAMP=2026-06-11T00:00:00Z python3 ./plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py . --report ./plans/seo-llm-skill-cluster/evals/mvp-eval-results.json
```

Codex system quick validator currently fails in this local environment because the Python `yaml` module is unavailable. Treat this as a validator toolchain blocker, not as skill content failure.

## Install Procedure After Approval

1. Re-run all pre-install validation commands.
2. Create a backup of any existing target skill directories if they exist.
3. Copy each staged skill directory to the matching target path from `package-manifest.json`.
4. Restart or reload Codex session so skill discovery refreshes.
5. Verify the new skills appear in the available skill list.
6. Run one smoke prompt for `site-growth-orchestrator` and one direct prompt for `seo-regression-validator`.
7. If trigger collisions appear, roll back immediately and update `trigger-map.yaml`.

## Rollback Procedure

If installation fails or triggers behave incorrectly:

1. Remove the newly installed target skill directories.
2. Restore previous target directories from backup if any existed.
3. Restart or reload Codex session.
4. Verify the installed skill list no longer includes the staged MVP skills.
5. Keep the staging repo unchanged for debugging.
6. Record the failed install reason in the task plan before retrying.

## Not Installed In This Task

- `editorial-quality-gate`
- `ux-journey-architect`
- credential-free monitoring baseline
- `llm-citation-monitor`
- `external-authority-placement-scout`
- `backlink-quality-validator`

These remain follow-up or gated tasks.

