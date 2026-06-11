# FEATURE-PREPARATION

feature_id: F-SEO-LLM-SKILL-CLUSTER
feature_title: SEO, LLM-friendly, UX, monitoring, and authority skill cluster
status: partial
owner_role: planner
last_updated: 2026-06-11

## 1. Problem and goal

- [x] Фича названа одним ясным предложением.
- [x] Понятно, какую проблему она решает.
- [x] Определен основной пользователь: Sergey as site owner/operator and Codex/agent workflows that build, audit, and grow public sites.
- [x] Определена ценность фичи: reusable skill system for architecture, execution, validation, and feedback loops instead of ad hoc SEO/LLM prompts.
- [x] Понятно, что не входит в фичу: black-hat SEO, link spam, fake crawler evidence, hidden SEO-only content, automated posting without platform permission.

## 2. User intents

- [x] Собраны типовые пользовательские команды.
- [x] Описаны основные user flows.
- [x] Описаны неоднозначные запросы.
- [x] Описаны ошибки и edge cases.
- [x] Определено, когда AI должен уточнять запрос.

### Core Intents

- "Построй SEO/LLM-friendly структуру сайта для проекта X."
- "Собери семантическое ядро и URL map."
- "Проверь сайт live: schema, canonical, hreflang, robots, llms.txt, sitemap, RSS."
- "Проверь, видят ли сайт Google/LLM crawlers."
- "Сделай план внутренней перелинковки."
- "Проверь UX пути и onboarding для нового читателя."
- "Найди площадки, где white-hat ссылка на сайт будет уместна."
- "Проверь, цитируют ли сайт ChatGPT/Perplexity/Claude/Gemini."
- "Собери task-plan и evidence по результатам аудита."

### Clarification Triggers

- Target site/domain is missing.
- The user asks to "place links everywhere" without ownership, permission, or platform rules.
- Required analytics access is unavailable.
- The user wants hidden content, doorway pages, fake reviews, PBNs, or automated spam.
- The target site has no confirmed canonical content model.

## 3. UI/UX

- [x] Определено, где пользователь вызывает фичу: Codex chat / skill-triggered local workflow.
- [x] Определен основной UI-паттерн: conversational orchestration with Markdown task-plan artifacts.
- [x] Понятно, как выглядит preview результата: `TASK-PLAN.md`, optional checklist, reports, skill drafts.
- [x] Понятно, как подтвердить применение: explicit user approval before creating or installing production skills.
- [x] Понятно, как сделать undo/rollback: git revert or delete generated skill directory before install.
- [x] Описаны состояния UI: draft, ready, in_progress, needs_review, done.
- [x] Описано поведение при ошибке или низкой уверенности: stop with `INVALID_INPUT` or active alarm.

## 4. Technical design

- [x] Определены затрагиваемые подсистемы.
- [x] Определена точка входа AI layer: central `site-growth-orchestrator` skill.
- [x] Описан путь intent -> internal action.
- [x] Понятно, какие API/events/contracts нужны.
- [x] Определены ограничения и forbidden areas.
- [x] Решено, нужен ли preview/dry-run mode: yes, default all external placement and audits to dry-run unless explicitly authorized.
- [x] Если предлагаются mock/stub/placeholder элементы, на них заведены alarms с условиями замены.

## 5. Verification

- [x] Для фичи есть acceptance criteria.
- [x] Для каждого ключевого сценария есть способ проверки.
- [x] Определены unit/integration/e2e/manual тесты на уровне плана.
- [x] Подготовлены sample data sources: mlllm.io task-plan, static builder, live SEO audit, concept file.
- [x] Определен oracle успеха: deterministic artifacts, validated skill structure, forward-test prompts, no hidden placeholders.
- [x] Определены negative tests.
- [x] Определены regression risks.
- [x] Понятно, чего именно не хватает, чтобы заменить каждый временный mock/placeholder.

## 6. Delivery and rollout

- [x] Определен MVP-срез: existing skill inventory, trigger map, freshness policy, MVP cut, one orchestrator skill, core SEO/LLM architecture skill, live validator, and MVP eval suite.
- [x] Определено, что отложено на потом: automated external placement, credentialed Search Console integrations, broad rank tracking, paid APIs, and full monitoring/UX/editorial companion skills beyond the MVP.
- [x] Решено, нужен ли feature flag: not applicable for local skills; install/enable step acts as activation gate.
- [x] Определен rollback/fallback: remove generated skill directories or revert git commits.
- [x] Определено, что писать в wiki: skill architecture, artifact schemas, safety constraints, eval outcomes.
- [x] Определено, какие артефакты должен вернуть Codex: plan, skill dependency graph, creation prompts, validation checklist.

## Decisions

problem_statement: SEO, LLM-friendly, UX, content, monitoring, and authority work is currently spread across conversation-specific reasoning and project task-plans; it needs to become a reusable coordinated skill cluster with evidence-first validation.
primary_user: Sergey Kostenchuk and local Codex agents working on public websites and AI-native content systems.
value: Repeatable site growth architecture with clear role separation, shared artifacts, safety boundaries, and real-world validation.
mvp_slice: Create the task-plan, inventory existing skills, approve trigger boundaries and freshness policy, cut the MVP scope, then build `site-growth-orchestrator`, `seo-llm-static-site-architect`, `seo-llm-regression-auditor`, and an MVP eval suite first.
deferred_scope: Automated placement on external platforms, Search Console API ingestion, LLM citation automation, broad rank tracking, and non-MVP companion skills until access, compliance, and trigger boundaries are confirmed.
feature_flag: local skill install/enable gate.
rollback: remove generated skill directories or revert commits before Codex reload.
required_artifacts: `FEATURE-PREPARATION.md`, `TASK-PLAN.md`, skill dependency graph, skill inventory, trigger map, freshness policy, MVP release scope, shared artifact schemas, eval prompts, validation reports.
wiki_updates: update local wiki after each implemented skill with final skill path, trigger description, validation commands, unresolved risks, and eval outcomes.
