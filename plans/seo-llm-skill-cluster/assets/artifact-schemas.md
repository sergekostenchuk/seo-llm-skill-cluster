# Shared Artifact Schemas

plan_id: PLAN-SEO-LLM-SKILL-CLUSTER
task_id: T-002
artifact_contract_version: 0.1
date: 2026-06-11
status: complete

## Global Rules

All artifacts must follow these rules:

- Separate `observed` facts from `inferred` conclusions.
- Include `generated_at`, `producer_skill`, and `source_inputs`.
- Include `confidence` where claims are inferred.
- Include `evidence` for claims about live pages, rankings, crawlers, citations, search behavior, and platform rules.
- Never include secrets, API keys, cookies, private tokens, raw private analytics rows, or raw IP logs.
- Do not create hidden SEO-only facts. Metadata/schema recommendations must match visible user-facing content.
- Use UTC timestamps in ISO-8601 format.
- Use canonical absolute URLs for public pages.
- Use `unknown` when a field is not verified; do not invent.

## Common Evidence Object

```yaml
evidence:
  - type: html|http|screenshot|log|search-console|assistant-output|manual-review|source-doc|code
    source: "https://example.com/page-or/local/path"
    checked_at: "2026-06-11T00:00:00Z"
    method: "curl|browser|script|manual|official-doc"
    status: pass|fail|partial|unknown
    note: "short factual note"
```

## Common Privacy Object

```yaml
privacy:
  contains_secrets: false
  contains_private_urls: false
  contains_raw_ip_logs: false
  contains_private_analytics: false
  redaction_note: "none"
```

## Artifact: `goal_brief.md`

Purpose: Capture the target, audience, constraints, and non-goals before specialist skills run.

Producer: `site-growth-orchestrator`

Consumers: all specialist skills.

Required sections:

- target site/project
- audience and user roles
- business/search/LLM goals
- languages/locales
- canonical content model
- constraints and forbidden areas
- success metrics
- unknowns and alarms

Minimum frontmatter:

```yaml
artifact_type: goal_brief
generated_at: "2026-06-11T00:00:00Z"
producer_skill: site-growth-orchestrator
target_site: "https://example.com"
languages: [en, ru]
status: draft|approved
```

## Artifact: `semantic-core.yaml`

Purpose: Define query clusters, user intents, entities, topics, languages, and priority.

Producer: `semantic-core-architect` or core SEO architecture skill.

Consumers: information architecture, content strategy, LLM optimizer, regression validator.

Required fields:

```yaml
artifact_type: semantic_core
generated_at: "2026-06-11T00:00:00Z"
producer_skill: semantic-core-architect
site:
  canonical_host: "https://example.com"
  default_language: en
clusters:
  - id: "ai-news-for-builders"
    primary_intent: informational|navigational|commercial|transactional|support
    audience: "AI builders"
    priority: P0|P1|P2|P3
    languages: [en, ru]
    entities:
      - name: "mlllm.io"
        type: Organization|Person|SoftwareApplication|Topic|Project|Publication
        canonical_url: "https://example.com/about/"
    queries:
      - text: "AI news for builders"
        locale: en-US
        source: observed|inferred|user-provided
        evidence: []
```

Privacy: no private keyword exports unless explicitly approved and summarized.

## Artifact: `entity-topic-map.yaml`

Purpose: Map entities, topics, relationships, canonical pages, and supporting evidence.

Producer: semantic/core SEO skill.

Consumers: URL architecture, internal links, schema, LLM discovery.

Required fields:

```yaml
artifact_type: entity_topic_map
entities:
  - id: "sergey-kostenchuk"
    name: "Sergey Kostenchuk"
    type: Person
    canonical_url: "https://example.com/about/"
    same_as: []
    evidence: []
topics:
  - id: "ai-news-pipeline"
    label: "AI news pipeline"
    canonical_url: "https://example.com/topics/ai-news-pipeline/"
    related_entities: ["mlllm-io"]
relationships:
  - source: "tg-news"
    predicate: "feeds"
    target: "mlllm-io"
    evidence: []
```

## Artifact: `url-map.yaml`

Purpose: Define page roles, canonical URLs, locale alternates, indexation policy, and content ownership.

Producer: information architecture / SEO architecture skill.

Consumers: technical SEO, internal links, LLM optimizer, validator.

Required fields:

```yaml
artifact_type: url_map
pages:
  - url: "https://example.com/news/123-slug/"
    page_type: news_brief|longform_article|topic|project|blog|author|index|community
    locale: en
    canonical: "https://example.com/news/123-slug/"
    hreflang_group:
      en: "https://example.com/news/123-slug/"
      ru: "https://example.com/ru/news/123-slug/"
      x-default: "https://example.com/news/123-slug/"
    index_policy: index|noindex
    source_content_id: "123"
    paired_page:
      relation: brief|longform|translation|none
      url: "https://example.com/articles/123-slug/"
    evidence: []
```

Rule: brief and longform can both be self-canonical when they are genuinely separate pages with different depth and role.

## Artifact: `internal-link-graph.yaml`

Purpose: Define intentional internal links, anchor intent, and no-duplication rules.

Producer: internal link graph skill.

Consumers: UX, SEO, LLM discovery, validator.

Required fields:

```yaml
artifact_type: internal_link_graph
links:
  - source_url: "https://example.com/news/123/"
    target_url: "https://example.com/articles/123/"
    link_type: brief_to_longform|longform_to_brief|topic_to_page|page_to_topic|author_to_project|breadcrumb|source_trail|related
    anchor_intent: "Read longform"
    user_reason: "Offers deeper explanation of the same story"
    seo_reason: "Connects the two sanctioned story surfaces"
    risk: none|overlinking|duplicate-intent|thin-page
```

Rule: the link graph reinforces one short news plus one expanded article; it must not create extra duplicate story bodies.

## Artifact: `schema-report.json`

Purpose: Record structured-data recommendations and validation status.

Producer: technical SEO/schema skill.

Consumers: SEO validator, implementation agent, site-growth orchestrator.

Required fields:

```json
{
  "artifact_type": "schema_report",
  "generated_at": "2026-06-11T00:00:00Z",
  "producer_skill": "technical-seo-schema-engineer",
  "pages": [
    {
      "url": "https://example.com/news/123/",
      "schema_types": ["NewsArticle", "BreadcrumbList"],
      "required_fields_present": true,
      "visible_content_match": "pass",
      "image_policy": "media|poster|fallback-og-card",
      "issues": [],
      "evidence": []
    }
  ]
}
```

Rule: `FAQPage` is allowed only when a visible FAQ exists.

## Artifact: `llm-discovery-report.md`

Purpose: Explain how an LLM agent should discover, parse, cite, and avoid parts of the site.

Producer: LLM-friendly optimizer.

Consumers: orchestrator, SEO validator, content/editorial skills.

Required sections:

- public canonical sections
- `/llms.txt` status
- `robots.txt` AI crawler policy
- markdown alternate status
- direct-answer/TL;DR coverage
- source trail coverage
- do-not-use/private areas
- gaps and caveats

Rule: `llms.txt` links only to public canonical useful pages.

## Artifact: `ux-journey-map.md`

Purpose: Capture human and agent-readable user journeys.

Producer: UX architect.

Consumers: SEO architecture, LLM optimizer, implementation agent.

Required sections:

- audience/persona
- entry point
- intent
- first-screen comprehension
- primary action
- secondary actions
- trust/evidence needs
- accessibility/semantic requirements
- retention path
- friction and risk

## Artifact: `crawler-access-audit.json`

Purpose: Record public crawler access checks without making unsupported claims.

Producer: SEO validator or server-log crawler analyst.

Consumers: SEO architecture, security, monitoring.

Required fields:

```json
{
  "artifact_type": "crawler_access_audit",
  "generated_at": "2026-06-11T00:00:00Z",
  "checks": [
    {
      "url": "https://example.com/robots.txt",
      "user_agent": "Googlebot",
      "status_code": 200,
      "allowed_by_robots": true,
      "blocked_by_server": false,
      "method": "curl",
      "evidence": []
    }
  ],
  "limitations": ["IP ownership not verified"]
}
```

Privacy: store bot classification summaries, not raw private access logs.

## Artifact: `llm-citation-report.md`

Purpose: Record assistant/search citation observations with timestamped prompts and caveats.

Producer: LLM citation monitor.

Consumers: LLM optimizer, orchestrator, content strategy.

Required table:

| date_utc | assistant | query | locale | cited_url | rank_in_answer | snippet_summary | evidence_path | caveat |
|---|---|---|---|---|---|---|---|---|

Rule: absence of a citation is an observation for that prompt/time, not proof that the site is never cited.

## Artifact: `authority-opportunity-register.yaml`

Purpose: Track white-hat link opportunities before any external action.

Producer: authority placement scout.

Consumers: backlink validator, security/safety reviewer, user approval gate.

Required fields:

```yaml
artifact_type: authority_opportunity_register
opportunities:
  - platform: "GitHub awesome list"
    url: "https://github.com/example/list"
    topical_relevance: high|medium|low
    rule_check:
      allowed: true|false|unknown
      source: "contribution guide URL"
    proposed_target_url: "https://example.com/topics/ai-news-pipeline/"
    proposed_format: "pull request|profile link|community post|guest article"
    link_attributes_expected: follow|nofollow|sponsored|ugc|unknown
    risk: low|medium|high
    approval_status: draft|needs_user_approval|approved|rejected
    evidence: []
```

Rule: no automated posting, comments, outreach, or PRs without explicit user approval.

## Artifact: `seo-regression-report.json`

Purpose: Provide deterministic pass/fail output for live/static SEO checks.

Producer: `seo-regression-validator`.

Consumers: orchestrator, implementation agent, release gate.

Required fields:

```json
{
  "artifact_type": "seo_regression_report",
  "generated_at": "2026-06-11T00:00:00Z",
  "target": "https://example.com",
  "summary": {
    "status": "pass",
    "checked_urls": 10,
    "failures": 0,
    "warnings": 2
  },
  "checks": [
    {
      "id": "canonical-present",
      "url": "https://example.com/news/123/",
      "status": "pass",
      "observed": "https://example.com/news/123/",
      "expected": "self-canonical",
      "evidence": []
    }
  ]
}
```

## Artifact: `validation-summary.md`

Purpose: Summarize commands, results, evidence, unresolved risks, and release decision.

Producer: validator/tester/docs_sync.

Consumers: user, orchestrator, packaging gate.

Required sections:

- scope
- commands run
- artifacts checked
- pass/fail table
- unresolved risks
- rollback notes
- next tasks

## Artifact: `trigger-map.yaml`

Purpose: Prevent trigger collisions between skills.

Producer: T-021 trigger task.

Consumers: senior skill architect, cluster linter, orchestrator.

Required fields:

```yaml
artifact_type: trigger_map
skills:
  - name: site-growth-orchestrator
    trigger_contexts: []
    near_miss_prompts: []
    exclusion_rules: []
    primary_owner_for: []
    handoff_to: []
```

## Artifact: `freshness-policy.md`

Purpose: Define unstable fact categories, primary sources, browse/verify triggers, and stale-data handling.

Producer: T-023 freshness task.

Consumers: all skills.

Required sections:

- unstable facts
- primary sources
- verification cadence
- browse-required triggers
- stale-data reporting
- privacy/secret exclusions

## Artifact: `mvp-release-scope.md`

Purpose: Freeze the MVP skill list and backlog before implementation.

Producer: T-024 MVP cut task.

Consumers: implementation, eval, packaging.

Required sections:

- included MVP skills
- excluded/deferred skills
- accepted unresolved alarms
- release criteria
- install path
- rollback path

## Artifact: `cluster-lint-report.json`

Purpose: Machine-check generated skill directories for placeholders, trigger collisions, missing required files, and validation status.

Producer: T-022 linter/checklist.

Consumers: eval, packaging, release gate.

Required fields:

```json
{
  "artifact_type": "cluster_lint_report",
  "generated_at": "2026-06-11T00:00:00Z",
  "skills_checked": [],
  "errors": [],
  "warnings": [],
  "status": "pass|fail"
}
```

## Producer/Consumer Coverage Check

| Skill/domain | Input artifacts | Output artifacts |
|---|---|---|
| `site-growth-orchestrator` | user goal, `skill-inventory.md`, `cluster-architecture.md` | `goal_brief.md`, handoff prompts, `validation-summary.md` |
| `semantic-core-architect` | `goal_brief.md`, source evidence | `semantic-core.yaml`, `entity-topic-map.yaml` |
| SEO architecture | `semantic-core.yaml`, `entity-topic-map.yaml`, `goal_brief.md` | `url-map.yaml`, `schema-report.json`, `llm-discovery-report.md` |
| internal link graph | `url-map.yaml`, `entity-topic-map.yaml` | `internal-link-graph.yaml` |
| LLM optimizer | `url-map.yaml`, `semantic-core.yaml`, visible content | `llm-discovery-report.md`, `llm-citation-report.md` |
| UX architect | `goal_brief.md`, `url-map.yaml` | `ux-journey-map.md` |
| SEO regression validator | public URLs, `url-map.yaml`, `schema-report.json` | `seo-regression-report.json`, `crawler-access-audit.json` |
| Authority scout | `url-map.yaml`, `semantic-core.yaml`, safety policy | `authority-opportunity-register.yaml` |
| Cluster linter | skill directories, `trigger-map.yaml`, `mvp-release-scope.md` | `cluster-lint-report.json` |

Coverage result: every MVP domain has at least one input and one output artifact. Post-MVP authority and credentialed monitoring remain artifact-compatible but gated by safety/access tasks.
