# SEO/LLM Skill Cluster MVP Release Scope

date: 2026-06-11
status: approved-for-implementation
plan: `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
artifact_contract: `assets/artifact-schemas.md`
trigger_map: `trigger-map.yaml`
freshness_policy: `freshness-policy.md`

## Decision

The first release must prove the core workflow, not the whole long-term ambition.

MVP v0.1 includes the skills needed to take a site goal through semantic planning, URL structure, internal linking, technical SEO/schema, LLM-friendly architecture, and regression validation. It also includes the cluster linter, eval suite, packaging workflow, and one end-to-end dry run.

Broad editorial, UX, monitoring, citation, and authority-placement skills remain explicit follow-up/backlog work. They are not dropped.

## MVP v0.1 Included Work

| Task | Skill or Artifact | Why it is in MVP | Output |
| --- | --- | --- | --- |
| T-003 | `site-growth-orchestrator` | Central routing, sequencing, artifact handoff, and final validation gate. | Orchestrator skill and operating flow. |
| T-004 | `semantic-core-architect` | SEO/LLM structure starts from queries, entities, topics, audiences, and language priority. | `semantic-core.yaml`, `entity-topic-map.yaml`. |
| T-005 | `information-architecture-seo` | Converts semantic core into crawlable URLs, page roles, canonical rules, and hreflang groups. | `url-map.yaml`, page taxonomy. |
| T-006 | `internal-link-graph-architect` | The cluster must model one brief plus one longform, topic pages, projects, author pages, breadcrumbs, and source trails without duplicating content. | `internal-link-graph.yaml`. |
| T-007 | `technical-seo-schema-engineer` | Defines deterministic metadata, JSON-LD, OG/Twitter, sitemap, RSS, robots, and llms.txt policies. | Schema and head metadata templates/checklists. |
| T-008 | `llm-friendly-site-architect` | Converts SEO structure into machine-readable, human-visible LLM surfaces without hidden or duplicate bot content. | LLM discovery plan and refusal boundaries. |
| T-009 | `seo-regression-validator` | Prevents subjective audits by checking live/fixture HTML and generated artifacts. | `seo-regression-report.json`. |
| T-022 | `cluster-consistency-linter` | Ensures skill frontmatter, trigger map, artifact contract, placeholders, and dependency rules stay coherent. | `cluster-lint-report.json`. |
| T-016 | MVP eval suite | Tests successful and negative use cases before production install. | Forward-test prompts and expected results. |
| T-017 | Packaging/install workflow | Defines staging-to-production install, rollback, and documentation. | Install/rollback runbook. |

Already completed planning inputs remain part of the MVP baseline: T-000, T-001, T-002, T-021, T-023, and this T-024 release cut.

## Follow-Up v0.2 Work

| Task | Scope | Reason for follow-up placement |
| --- | --- | --- |
| T-010 | `editorial-quality-gate` MVP skill and content backlog | Useful, but not required to prove the SEO/LLM architecture skill chain. Needs careful boundaries so it does not rewrite source content model decisions. |
| T-011 | `ux-journey-architect` MVP skill and UX backlog | Important for conversion and user paths, but the first release must validate structural SEO/LLM competence first. |
| T-012 | Credential-free monitoring baseline | Valuable after the validator exists. MVP must not require Search Console, analytics, rank, or crawler-log credentials. |
| T-014 | White-hat authority placement policy and opportunity model | Planning can happen after core MVP, but implementation cannot proceed to external actions until safety policy is explicit. |
| T-018 | Operating handbook and wiki sync | Release-supporting documentation after install workflow exists. |
| T-019 | First end-to-end MVP use case | Runs after packaged skills exist. This is not a skill-build task, but it is required before v1 release decision. |
| T-020 | Post-eval consolidation and v1 decision | Final release decision after the first end-to-end use case. |

## Deferred or Gated Backlog

| Task | Scope | Gate |
| --- | --- | --- |
| T-013 | LLM citation monitoring workflow | Gated by A-MON-001. Credential-free references can be drafted later, but real monitoring needs confirmed surfaces and access. |
| T-015 | `external-authority-placement-scout` and `backlink-quality-validator` | Gated by A-EXT-001. No automatic posting, outreach, account use, or external placement in MVP. Dry-run-only design requires explicit user approval. |

## Alarm Classification

| Alarm | MVP Classification | Decision |
| --- | --- | --- |
| A-EXT-001 | Blocking for T-015 only | Accepted as post-MVP blocker. MVP must not include live external placement or backlink outreach. |
| A-MON-001 | Blocking for credentialed monitoring only | Accepted as post-MVP blocker. MVP may define credential-free checks but must not require Search Console, analytics, rank tracker, or LLM citation account access. |

No active alarm blocks the MVP v0.1 skill chain.

## Existing Skill Policy

Existing installed skills under `<codex-skills-dir>` are read-only during MVP implementation.

New or rewritten skills are staged under `./skills/<skill-name>/`. Production installation into `<codex-skills-dir>/<skill-name>/` is allowed only in T-017 after lint, eval, and user approval.

For T-008, prefer a new staged `llm-friendly-site-architect` skill unless review proves that upgrading an existing installed skill is safer and explicitly approved.

## Eval Scope for T-016

T-016 must cover only the MVP v0.1 skills:

- `site-growth-orchestrator`
- `semantic-core-architect`
- `information-architecture-seo`
- `internal-link-graph-architect`
- `technical-seo-schema-engineer`
- `llm-friendly-site-architect`
- `seo-regression-validator`
- `cluster-consistency-linter`

Each skill needs at least three positive prompts and three negative prompts. The orchestrator needs end-to-end prompts for mlllm.io-style news/article architecture, a non-news SaaS site, and a personal/project portfolio.

Deferred skills must not be required by MVP evals.

## Release Criteria

MVP v0.1 is complete only when:

- all included skill directories exist in `./skills/`;
- every MVP skill has a concise `SKILL.md`, trigger boundary, handoff artifacts, refusal/stop rules, and examples;
- `trigger-map.yaml` covers all MVP skills and near-miss prompts;
- linter output has no critical issues;
- eval suite covers positive and negative cases;
- packaging/rollback workflow is documented;
- no task requires secrets, private analytics, external posting, or production website changes.

## Non-MVP Explicitly Not Allowed

- creating hidden bot-only content;
- multiplying one story into extra public duplicates beyond the declared content model;
- canonicalizing one standalone brief to its longform by default;
- claiming search volume, rank, traffic, or crawler behavior without evidence;
- automatically placing links on external platforms;
- using Search Console, analytics, LLM provider dashboards, or account APIs without explicit credentials and user approval.

