# Skill Inventory And Trigger-Collision Audit

plan_id: PLAN-SEO-LLM-SKILL-CLUSTER
task_id: T-000
date: 2026-06-11
status: complete
scope: `<codex-skills-dir>`

## Purpose

This inventory prevents the SEO/LLM skill cluster from duplicating or weakening existing Codex skills. It classifies the proposed cluster skills against real installed skills, their trigger descriptions, and their current ownership boundaries.

## Evidence Commands

- `find <codex-skills-dir> -maxdepth 2 -name SKILL.md -print`
- `rg -n "seo|llm|site|ux|skill|crawler|schema|citation|analytics|link" <codex-skills-dir> -g SKILL.md`
- Direct reads of the relevant `SKILL.md` files listed below.

## Existing Skill Inventory

| Existing skill | Path | Trigger description evidence | Current ownership | Collision risk | Recommendation |
|---|---|---|---|---|---|
| `seo-llm-site-architect` | `<codex-skills-dir>/seo-llm-site-architect/SKILL.md` | "creating, editing, auditing, and monitoring SEO, AEO/GEO, LLM-readable, and AI-agent-friendly websites" | Senior site/search architecture: crawl/index, canonical routes, metadata, `robots.txt`, sitemaps, `llms.txt`, JSON-LD/schema, monitoring, bot policy. | High with `technical-seo-schema-engineer`, `information-architecture-seo`, `seo-regression-validator`, and parts of `llm-friendly-site-architect`. | Upgrade/reuse as the main SEO/LLM architecture backbone. Do not create a broad duplicate unless the new skill has a narrower artifact contract. |
| `llm-friendly-site-optimizer` | `<codex-skills-dir>/llm-friendly-site-optimizer/SKILL.md` | "Tactical LLM-friendly site optimization ... llms.txt, AI citation readiness, pillar pages, direct-answer blocks, TL;DR sections, FAQ/schema ... weekly LLM citation monitoring" | Tactical LLM citation/content layer: `llms.txt`, pillar pages, direct-answer blocks, FAQ, topic matrices, external signals, assistant citation monitoring. | High with any proposed `llm-friendly-site-architect`, `content-strategy-architect`, and `llm-citation-monitor`. | Upgrade-existing for tactical LLM layer. New skills should only split out monitoring or authority placement if they need deterministic artifacts/scripts. |
| `ui-ux-llm-product-architect` | `<codex-skills-dir>/ui-ux-llm-product-architect/SKILL.md` | "designing, editing, auditing, and validating websites, web apps ... for both human users and AI/LLM agents" | UX journeys, screen architecture, visual hierarchy, design systems, accessibility, semantic controls, rendered interaction quality. | High with `ux-journey-architect`, `onboarding-architect`, `ui-layout-validator`. | Upgrade-existing or use as the UX specialist. For MVP, do not create separate UX skills unless a smaller deterministic linter is needed. |
| `ui-ux-pro-max` | `<codex-skills-dir>/ui-ux-pro-max/SKILL.md` | "UI/UX design intelligence. 50 styles, 21 palettes ... Actions: plan, build, create, design, implement, review, fix..." | Design intelligence library: style, palettes, typography, layouts, accessibility heuristics. | Medium with UX skills, but it is more reference-heavy than architecture/governance. | Reuse as optional design-system resource; defer any new style-specific skill. |
| `web-security-architect` | `<codex-skills-dir>/web-security-architect/SKILL.md` | "websites, web apps, APIs ... auth flows, sessions, cookies, browser security headers, CSP, CORS ... AI/agent-enabled web features" | Security/privacy/appsec boundaries, auth, headers, CSP/CORS, secrets, abuse controls, safe AI/agent execution. | Medium with crawler access, bot policy, analytics/log monitoring, and external placement safety. | Reuse as safety gate. Do not duplicate security logic inside SEO/authority skills. |
| `senior-skill-architect` | `<codex-skills-dir>/senior-skill-architect/SKILL.md` | "Create, upgrade, audit, and package production-grade Codex skills ... deterministic linters, design evals ... trigger descriptions" | Production skill architecture, evals, linters, packaging, trigger optimization, freshness/safety boundaries. | High with any skill-creation meta-skill. | Reuse as the build/review authority for the whole cluster. Do not create a separate generic skill-builder. |
| `skill-creator` | `<codex-skills-dir>/skill-creator/SKILL.md` | "Create new skills, modify and improve existing skills, and measure skill performance..." | General skill creation and iterative eval workflow. | Medium with `senior-skill-architect`; senior skill is stricter for production. | Reuse for scaffolding/eval inspiration; senior-skill-architect remains the quality gate. |
| `task-plan-v2-orchestrator` | `<codex-skills-dir>/task-plan-v2-orchestrator/SKILL.md` | "Create, refactor, audit, and maintain a multi-agent TASK-PLAN v2..." | Planning artifact governance, pre-implementation gate, task registers, alarms, verification policy. | High with proposed `site-growth-orchestrator` if that skill tries to own task-plan mechanics. | Reuse for plan documents. `site-growth-orchestrator` must coordinate site-growth workflow, not replace TASK-PLAN v2. |
| `agent-browser-codex` | `<codex-skills-dir>/agent-browser-codex/SKILL.md` | "browser automation from Codex, web UI smoke tests, login flows, form filling, screenshots..." | Browser automation workflow for rendered verification and UI smoke tests. | Low to medium with live validators and UI validators. | Reuse as execution helper for browser verification. Do not create browser-control logic inside SEO validators. |
| `llm-wiki-maintainer` | `<codex-skills-dir>/llm-wiki-maintainer/SKILL.md` | "filesystem-based LLM Wiki or Obsidian vault ... ingest/query/lint workflows" | Wiki setup, maintenance, ingest/query/lint routing, vault contracts. | Medium with task-plan wiki sync and project knowledge capture. | Reuse for wiki architecture. No new wiki skill needed in MVP. |
| `wiki-update` | `<codex-skills-dir>/wiki-update/SKILL.md` | "Sync the current project's knowledge into the Obsidian wiki..." | Cross-project wiki sync and distillation. | Medium with `docs_sync` tasks. | Reuse when a task explicitly updates wiki. Keep out of MVP if only local plan artifacts are needed. |
| `wiki-capture` | `<codex-skills-dir>/wiki-capture/SKILL.md` | "Save the current conversation as a permanent, structured wiki note..." | Conversation-to-wiki distillation. | Low with skill-cluster docs. | Reuse for discussion capture, not for deterministic skill artifacts. |

## Proposed Cluster Decisions

| Proposed skill | Decision | Reason | MVP status |
|---|---|---|---|
| `site-growth-orchestrator` | new | No current skill owns full SEO/LLM/UX/content/monitoring/authority sequencing. It must route to specialists and prepare handoff prompts, not implement every domain itself. | MVP candidate |
| `semantic-core-architect` | new or narrow split | Existing `seo-llm-site-architect` has entity/intent mapping, but no dedicated semantic-core artifact contract with clusters, languages, priorities, and evidence. | MVP candidate if kept narrow |
| `information-architecture-seo` | merge/upgrade-existing | Existing `seo-llm-site-architect` already owns URL/canonical/hreflang/site structure. A separate skill risks duplication unless it only emits `url-map.yaml`. | Defer or merge into SEO architecture skill |
| `internal-link-graph-architect` | new narrow skill | Existing SEO/UX skills mention links, but not a deterministic internal-link graph artifact with role, anchor intent, and no-duplication rules. | Defer unless MVP requires link graph |
| `technical-seo-schema-engineer` | merge or narrow new | Existing `seo-llm-site-architect` already owns metadata/schema/sitemaps/robots. A separate skill is justified only if it packages deterministic schema/head templates and validators. | MVP candidate only as narrow implementation/checklist layer |
| `llm-friendly-site-architect` | upgrade-existing | `llm-friendly-site-optimizer` already covers `llms.txt`, pillar pages, direct-answer blocks, FAQ/schema, topic matrices, external signals, and citation monitoring. | Upgrade existing rather than create broad duplicate |
| `seo-regression-validator` | new narrow validator | Existing SEO skill has `scripts/audit_site.py`, but a separate regression validator can own repeatable live checks, report schema, and CI-style pass/fail thresholds. | MVP candidate |
| `content-strategy-architect` | defer | Useful, but overlaps with `llm-friendly-site-optimizer` topic matrices and editorial planning. Needs clearer artifact contract. | Post-MVP backlog |
| `editorial-quality-gate` | new narrow skill or defer | There is no dedicated editorial QA skill for source-backed content and anti-filler gates. It must not rewrite content invisibly or invent facts. | Post-MVP or small MVP gate |
| `translation-localization-seo` | new | No existing skill owns multilingual translation quality, localized intent, hreflang/canonical impact, and locale-specific terminology together. | Post-MVP |
| `content-decay-monitor` | defer | Monitoring/refresh logic can start inside regression validator or Search Console workflow. | Post-MVP |
| `ux-journey-architect` | upgrade-existing | `ui-ux-llm-product-architect` already owns journeys, IA, onboarding, accessibility, and agent-friendly UI. | Use existing skill |
| `conversion-retention-architect` | defer | Useful but should be a focused UX/content module after baseline UX skill is stable. | Post-MVP |
| `ui-layout-validator` | defer or script | Existing UI skill and `agent-browser-codex` can cover manual/browser checks; a deterministic script may be useful later. | Post-MVP |
| `onboarding-architect` | merge/upgrade-existing | Existing UI skill owns onboarding and first journey. | Use existing skill |
| `external-authority-placement-scout` | new with strict safety | Existing LLM optimizer mentions external signals but not platform-rule-aware outreach workflow. Must be white-hat, dry-run, permission-first. | Post-MVP after safety policy |
| `backlink-quality-validator` | new narrow validator | Not currently covered deterministically. Should validate relevance, indexability, toxic patterns, canonical target, and monitoring. | Post-MVP after scout |
| `search-console-analyst` | defer | Credentialed data source. Start with manual/credential-free monitoring until access policy is defined. | Post-MVP |
| `llm-citation-monitor` | split from optimizer later | Existing `llm-friendly-site-optimizer` already has weekly citation monitoring. Separate only if we need scripts, report schema, and repeatable prompt sets. | Post-MVP |
| `server-log-crawler-analyst` | new or security/SEO shared | Existing SEO and security skills both touch bot/log analysis. A new skill is justified if it anonymizes IPs and distinguishes crawlers/user-triggered fetchers. | Post-MVP |
| `rank-serp-monitor` | defer | Requires current SERP tools/locale controls and can easily overstate evidence. | Post-MVP |

## Recommended MVP Cut From Inventory

The smallest useful MVP should be:

1. `site-growth-orchestrator` as a routing/handoff skill.
2. Upgrade or reuse `seo-llm-site-architect` as the core SEO/LLM architecture skill rather than creating multiple broad duplicate skills immediately.
3. `seo-regression-validator` as a narrow live/static validation skill.
4. Shared artifacts: `semantic-core.yaml`, `url-map.yaml`, `schema-report.json`, `llm-discovery-report.md`, and `seo-regression-report.json`.
5. Trigger map and freshness policy before installing new skills.

This keeps the first release useful without building a large cluster whose trigger boundaries are still untested.

## Trigger-Collision Risks

| Collision | Why it matters | Resolution |
|---|---|---|
| `seo-llm-site-architect` vs `technical-seo-schema-engineer` | Both can own metadata, schema, sitemap, robots, and canonical rules. | Keep `seo-llm-site-architect` as architecture owner; make `technical-seo-schema-engineer` template/validator-only if created. |
| `seo-llm-site-architect` vs `llm-friendly-site-optimizer` | Both mention LLM-readable sites and AI search visibility. | SEO skill owns crawl/index/metadata. LLM optimizer owns answer-shaped content, citations, pillar pages, and assistant monitoring. |
| `ui-ux-llm-product-architect` vs `information-architecture-seo` | Both can define page structure and user pathways. | SEO IA owns URL/canonical/search intent. UX owns human journey, layout, interaction, accessibility. |
| `task-plan-v2-orchestrator` vs `site-growth-orchestrator` | Both can sound like orchestration. | TASK-PLAN skill owns plan format/governance. Site-growth skill owns site-growth sequencing and specialist handoffs. |
| `senior-skill-architect` vs `skill-creator` | Both create/upgrade skills. | Senior skill is production quality gate; skill-creator is broader creation/eval workflow. |
| `llm-friendly-site-optimizer` vs `external-authority-placement-scout` | Existing optimizer covers external signals. | New scout must be platform-rule-aware opportunity workflow with dry-run, not generic citation advice. |
| `web-security-architect` vs crawler/AI-bot access tasks | Bot access can touch WAF, auth, rate limits, CSP, and privacy. | Security owns safe access boundaries; SEO owns public crawler policy and indexing intent. |
| `agent-browser-codex` vs validators | Validators may need browser checks. | Validators should call out browser verification need but reuse browser skill/tooling. |

## Near-Miss Prompt Examples For T-021

| Prompt | Primary owner | Not owner | Routing note |
|---|---|---|---|
| "Проверь schema.org и canonical на сайте" | `seo-llm-site-architect` or narrow technical SEO validator | `llm-friendly-site-optimizer` | Technical metadata/schema first; LLM layer only if answer blocks/citations are also requested. |
| "Сделай TL;DR сверху статьи для LLM" | `llm-friendly-site-optimizer` | `technical-seo-schema-engineer` | Visible answer-shaped content, not schema-only work. |
| "Сделай красивую и понятную главную страницу" | `ui-ux-llm-product-architect` | `seo-llm-site-architect` | SEO can review metadata after UX/content structure is set. |
| "Почему Gemini не может зайти на сайт?" | `seo-llm-site-architect` with possible `web-security-architect` handoff | `llm-friendly-site-optimizer` | First determine HTTP/robots/WAF/bot policy evidence. |
| "Размести ссылки на сайт на площадках" | future `external-authority-placement-scout` | `seo-regression-validator` | Must be dry-run and permission-aware; no spam automation. |
| "Проверь, не опасны ли IP в логах" | `web-security-architect` | `seo-llm-site-architect` | Security owns abuse/threat analysis; SEO can classify crawlers. |
| "Собери семантическое ядро для сайта" | future `semantic-core-architect` | `llm-friendly-site-optimizer` | Semantic artifact first; LLM pillar matrix can consume it. |
| "Нарисуй путь нового читателя" | `ui-ux-llm-product-architect` | `seo-llm-site-architect` | UX journey first; SEO reviews entry pages and internal links. |
| "Создай новый production-grade skill" | `senior-skill-architect` | `site-growth-orchestrator` | Site-growth orchestrator may route, but skill architecture belongs to senior skill architect. |
| "Обнови Obsidian wiki по проекту" | `wiki-update` or `llm-wiki-maintainer` | `task-plan-v2-orchestrator` | Task plan can require wiki sync, but wiki skill owns vault contract. |
| "Проверь сайт в Chrome на desktop/mobile" | `agent-browser-codex` plus UX/SEO owner depending on purpose | `seo-regression-validator` alone | Browser skill handles mechanics; validator decides assertions. |
| "Проверь, цитирует ли Perplexity сайт" | `llm-friendly-site-optimizer` monitoring mode | `seo-llm-site-architect` | LLM citation monitoring requires assistant/query evidence and timestamps. |

## Open Decisions For T-001/T-024

- Final install path: production under `<codex-skills-dir>/*` or staging under `./skills/*`.
- Whether to upgrade existing `seo-llm-site-architect` and `llm-friendly-site-optimizer` directly or wrap them with a new orchestrator first.
- Whether `semantic-core-architect` and `technical-seo-schema-engineer` are separate MVP skills or references/scripts inside the SEO architecture skill.
- Which wiki target should receive final cluster knowledge.
- Which monitoring surfaces are credential-free in MVP and which remain manual.

## T-000 Review Result

- Existing skill directories were read but not modified.
- Broad duplication risk is high if all concept skills are created immediately.
- Recommended first build is a small MVP: orchestrator + reused/upgraded SEO architecture + narrow regression validator + trigger/freshness/contracts.
- External authority placement and credentialed monitoring must remain post-MVP until safety and access policies are explicit.
