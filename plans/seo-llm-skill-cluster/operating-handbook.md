# SEO/LLM Skill Cluster Operating Handbook

date: 2026-06-11
status: staged MVP handbook
scope: `.`

## Purpose

This cluster turns site-growth work into a controlled sequence of specialist skills:
semantic planning, information architecture, internal links, schema, LLM-readable surfaces,
and live regression validation.

The default operating rule is simple:

1. Plan the site model before implementation.
2. Keep one canonical user-facing content model.
3. Add SEO and LLM-readable metadata around visible content.
4. Validate live output before claiming results.
5. Record evidence, gaps, and unresolved risks.

## Current MVP Skills

| Skill | Role | Use When | Main Artifact |
| --- | --- | --- | --- |
| `site-growth-orchestrator` | central router | user asks for SEO/LLM/UX/site-growth plan or multi-skill workflow | execution plan, handoff sequence, evidence requirements |
| `semantic-core-architect` | semantic planner | building keyword/entity/topic model | semantic core, entity map, intent map |
| `information-architecture-seo` | URL and section architect | designing site structure and crawl paths | URL map, section model, hreflang/canonical notes |
| `internal-link-graph-architect` | link graph designer | connecting briefs, longforms, topics, projects, author pages | link graph, anchor rules, orphan-risk report |
| `technical-seo-schema-engineer` | metadata/schema specialist | adding or auditing title/meta/canonical/hreflang/JSON-LD | schema plan, metadata matrix, validation checklist |
| `llm-friendly-site-architect` | agent/RAG surface specialist | improving llms.txt, markdown alternates, answer blocks, source trails | LLM access plan, citation-oriented page model |
| `seo-regression-validator` | evidence checker | validating local or live HTML after changes | SEO/LLM regression report |

## Operating Sequence

For a new or heavily reworked public site:

1. `site-growth-orchestrator`
2. `semantic-core-architect`
3. `information-architecture-seo`
4. `internal-link-graph-architect`
5. `technical-seo-schema-engineer`
6. `llm-friendly-site-architect`
7. `seo-regression-validator`

For an existing site with known issues:

1. `site-growth-orchestrator`
2. `seo-regression-validator`
3. The specific specialist skill that owns the failing layer.
4. `seo-regression-validator` again after fixes.

For a content-model dispute:

1. `site-growth-orchestrator`
2. `information-architecture-seo`
3. `internal-link-graph-architect`
4. `technical-seo-schema-engineer`

Do not let a specialist silently change the content model. The orchestrator must preserve
the explicit story contract and route changes through architecture review.

## Artifact Lifecycle

Every material site-growth workflow should produce or update these artifacts:

| Artifact | Owner Skill | Validation |
| --- | --- | --- |
| Goal brief | orchestrator | scope, exclusions, success criteria |
| Semantic core | semantic core architect | intents, entities, language coverage, source evidence |
| URL map | IA SEO | canonical pages, language alternates, index/noindex rules |
| Link graph | internal link graph | no orphan critical pages, clear brief/longform/topic paths |
| Metadata matrix | technical SEO/schema | title, description, OG, canonical, hreflang, article meta |
| Schema graph | technical SEO/schema | JSON validity and visible-content match |
| LLM access plan | LLM-friendly architect | robots, llms.txt, source trails, markdown/noindex rules |
| Regression report | SEO regression validator | pass/fail with URL, timestamp, command/tool |

## Evidence Rules

Use these labels in all reports:

- `Observed`: directly checked in file, command output, browser, validator, or fetched URL.
- `Inferred`: reasonable conclusion from observed evidence.
- `Open`: not checked, credential-gated, time-dependent, or requiring user approval.

Never claim:

- a search ranking without live search evidence and timestamp;
- bot access without HTTP/log evidence;
- valid schema without parsing or validator evidence;
- assistant citation visibility without a recorded prompt set and run timestamp;
- external placement value without source quality and policy checks.

## Safety Boundaries

Allowed:

- public-site SEO and LLM-readability architecture;
- structured data matching visible content;
- white-hat internal linking;
- public crawler access audits;
- dry-run authority opportunity analysis.

Forbidden:

- hidden bot-only content;
- doorway pages;
- fake reviews or fake authority signals;
- automated comment/forum spam;
- external posting without explicit account authorization;
- storing secrets, tokens, raw private analytics rows, or private IP logs in generated docs.

## Common Workflows

### Workflow A: Build SEO/LLM Architecture For A Site

Run:

1. `site-growth-orchestrator`
2. `semantic-core-architect`
3. `information-architecture-seo`
4. `internal-link-graph-architect`
5. `technical-seo-schema-engineer`
6. `llm-friendly-site-architect`
7. `seo-regression-validator`

Expected outputs:

- semantic core;
- URL map;
- internal link graph;
- schema and metadata matrix;
- llms.txt/robots/RSS/sitemap notes;
- regression report.

### Workflow B: Fix A Metadata Or Schema Audit Finding

Run:

1. `seo-regression-validator` to confirm the live or local issue.
2. `technical-seo-schema-engineer` to design the fix.
3. Implement in the target project.
4. `seo-regression-validator` to prove the fix.

Expected outputs:

- before/after report;
- exact pages checked;
- validator command or fetch evidence.

### Workflow C: Protect A One Brief Plus One Longform Model

Run:

1. `site-growth-orchestrator`
2. `information-architecture-seo`
3. `internal-link-graph-architect`
4. `technical-seo-schema-engineer`

Rules:

- the brief page remains self-canonical;
- the longform page remains self-canonical;
- both pages link to each other with clear labels;
- topics and homepage teasers summarize and route, they do not create a third article body;
- schema can connect the pair, but must not collapse them into one page if both are intentional user surfaces.

## Validation Commands

Cluster consistency:

```bash
python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json
```

MVP eval coverage:

```bash
MVP_EVAL_TIMESTAMP=2026-06-11T00:00:00Z python3 ./plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py . --report ./plans/seo-llm-skill-cluster/evals/mvp-eval-results.json
```

Production skill lint:

```bash
for d in ./skills/*; do python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py "$d" --json || exit 1; done
```

Secret scan for this handbook:

```bash
rg -n "secret|password|api key|token" ./plans/seo-llm-skill-cluster/operating-handbook.md ./wiki/seo-llm-skill-cluster.md
```

The secret scan may match the warning text in this handbook. That is acceptable if no actual credential value is present.

## Install State

The MVP skills are staged under `./skills`.
They are not installed into `<codex-skills-dir>`.

Use `./plans/seo-llm-skill-cluster/install-rollback.md`
before any production install.

## Troubleshooting

If two skills give conflicting guidance:

1. Preserve the declared content model.
2. Check `trigger-map.yaml` for ownership.
3. Prefer the specialist owner for the specific layer.
4. Record the conflict in the task plan.
5. Add or update an eval case if the conflict can recur.

If a live audit conflicts with local files:

1. Treat live output as the user-visible state.
2. Record the deploy/build gap.
3. Do not mark the task complete until the checked target matches the claimed target.

If a validator fails because of missing local dependencies:

1. Record the exact command and error.
2. Run independent deterministic checks where available.
3. Do not hide the blocker.
