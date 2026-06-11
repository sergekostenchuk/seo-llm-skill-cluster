# SEO/LLM Skill Cluster v1 Release Decision

date: 2026-06-11
task: T-020
decision: staged v1 ready; production install remains gated

## Decision

The MVP SEO/LLM skill cluster is ready for controlled v1 use from the staging repository:

```text
./skills
```

It is not yet installed into:

```text
<codex-skills-dir>
```

Production install remains a separate approval-gated action using:

```text
./plans/seo-llm-skill-cluster/install-rollback.md
```

## Evidence

| Evidence | Result |
| --- | --- |
| Production linter for staged skills | pass, 7 skills |
| Cluster consistency linter | pass, 0 critical issues, 0 warnings |
| MVP eval verifier | pass, 8 MVP units, 3 end-to-end cases |
| mlllm.io-style E2E | pass with open follow-ups |
| Homepage regression sample | pass, 0 issues |
| EN brief regression sample | pass, 0 issues |
| EN longform regression sample | pass, 0 issues |
| Public discovery files | `robots.txt`, `llms.txt`, `sitemap.xml`, `news-sitemap.xml`, `rss.xml` reachable |

## Ready For v1

These staged skills are ready for controlled internal use:

- `site-growth-orchestrator`
- `semantic-core-architect`
- `information-architecture-seo`
- `internal-link-graph-architect`
- `technical-seo-schema-engineer`
- `llm-friendly-site-architect`
- `seo-regression-validator`

These support artifacts are part of v1:

- `trigger-map.yaml`
- `freshness-policy.md`
- `assets/artifact-schemas.md`
- `scripts/lint_skill_cluster.py`
- `scripts/verify_mvp_evals.py`
- `operating-handbook.md`
- local wiki page under `./wiki`

## Not Included In v1

The following remain draft/follow-up work:

- `editorial-quality-gate`
- UX journey/onboarding skill
- credential-free monitoring baseline
- `llm-citation-monitor`
- external authority placement scout
- backlink quality validator
- full sitemap-wide live crawl
- Lighthouse/Core Web Vitals lab report
- Search Console or analytics integration

## Active Alarms

| Alarm | Status | Handling |
| --- | --- | --- |
| `A-MON-001` | active | Use credential-free checks only; do not claim Search Console, analytics, server-log, or assistant citation evidence. |
| `A-EXT-001` | active | Keep external placement dry-run only; no posting, outreach, submissions, or account actions. |

## Release Conditions

The staged v1 can be used for planning, dry-run audits, static validation, and controlled
project-local skill development.

Before production install:

1. Re-run validation commands from `install-rollback.md`.
2. Review trigger map for collisions with existing installed skills.
3. Decide whether names should replace existing skills or remain as a separate cluster.
4. Back up any existing target skill directories.
5. Install only after explicit user approval.

## Follow-Up Backlog

P1:

- Add sitemap-wide regression mode.
- Add browser/visual smoke layer or connect to existing browser validation skill.
- Build credential-free crawler/access monitoring baseline.
- Define production install decision and rollback rehearsal.

P2:

- Build LLM citation monitor.
- Build authority placement scout only after white-hat policy is finalized.
- Add credentialed Search Console/analytics import patterns when credentials are available.

## Verdict

Release as `v1-staged`, not as production-installed skills.

This is the correct boundary: the MVP proves the cluster architecture, artifacts, and validation
workflow, while keeping monitoring, authority placement, and credentialed reality checks out of
scope until their safety and access gates are closed.
