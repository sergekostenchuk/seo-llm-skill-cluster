# TASK-PLAN v2

template_note:
- This plan converts `./CONCEPT-SCHEMA-SEO-LLM-SKILLS.MD` into a sequenced skill-cluster build plan.
- Markdown is the source of truth.
- Implementation tasks stay `draft` until shared contracts, target skill paths, and safety boundaries are approved.
- No task may invent live SEO results, crawler access, backlink opportunities, platform permissions, or assistant citations.

project: seo-llm-skill-cluster
plan_id: PLAN-SEO-LLM-SKILL-CLUSTER
plan_version: 0.3
canonical_source: ./plans/seo-llm-skill-cluster/TASK-PLAN.md
dashboard_target: none
status: draft
owner_role: planner
created_at: 2026-06-11
updated_at: 2026-06-11

## Feature Layer

feature_id: F-SEO-LLM-SKILL-CLUSTER
feature_title: SEO, LLM-friendly, UX, monitoring, and authority skill cluster
rationale: Build a reusable group of Codex skills that can architect, implement, validate, and continuously improve public websites for search engines, LLM agents, human UX, authority signals, and real-world performance without hidden SEO tricks or ad hoc prompts.
priority: P0
status: draft
goal: Create a coordinated skill system with a central orchestrator, expert subskills, validation/test skills, shared artifact contracts, white-hat authority workflows, and feedback loops from live search/LLM/crawler/analytics evidence.
scope_in:
- Existing skill inventory, trigger-collision audit, and upgrade-vs-new decisions before implementation.
- Central orchestrator skill for task sequencing and handoff.
- SEO/LLM architecture skills: semantic core, site structure, internal link graph, technical schema, LLM-friendly discovery.
- Content/editorial skills: content strategy, quality gates, localization, content decay monitoring.
- UX/UI skills: journey architecture, onboarding, retention, layout/accessibility validation.
- Monitoring/validation skills: live SEO regression audit, crawler access audit, LLM citation monitoring, Search Console/rank/log analysis.
- White-hat authority placement skills: opportunity scout and backlink quality validator.
- Shared artifacts: semantic core, URL map, entity map, internal link graph, schema report, UX journey map, crawler audit, LLM citation report, authority opportunity register.
- Eval prompts and deterministic linters/checklists for each skill.
- Freshness and primary-source policy for SEO, LLM crawler rules, platform rules, schema.org, Google documentation, and ranking/citation claims.
- MVP release cut that keeps v1 small before the full cluster is built.
scope_out:
- Black-hat SEO, PBNs, link farms, automated comment/forum spam, fake reviews, doorway pages, cloaking, hidden SEO-only content.
- Automated external posting without account ownership, explicit permission, or platform rules.
- Claims about rankings, citations, or crawl access without live evidence.
- Building or changing a target website as part of this planning task.
- Storing secrets, API keys, assistant account tokens, or private analytics rows in generated public skill artifacts.
changed_subsystems:
- `./plans/seo-llm-skill-cluster`
- `./skills`
- gated production install target `<codex-skills-dir>`
- future SEO/LLM/content/UX/authority/monitoring staging skill directories
- optional local wiki pages for skill architecture and eval results
constraints:
- Every skill must have a narrow trigger description and clear scope boundaries.
- The central orchestrator coordinates, routes, and prepares handoff prompts; it does not programmatically invoke other skills and must not silently replace specialist skills.
- Evidence-first: live SEO, crawler, LLM, analytics, and ranking claims require source URL, timestamp, command/tool, and report artifact.
- Schema must match visible user-facing content.
- LLM-friendly additions must not create duplicate story bodies, hidden bot-only content, or low-value doorway pages.
- External link placement must be white-hat, permission-aware, and platform-rule-aware.
- Skills must support dry-run/preview mode before external publication or outreach.
- Near-miss prompts and trigger-collision checks are required before a new skill is considered production-ready.
assumptions:
- Codex local skills are the first target runtime.
- Existing mlllm.io SEO/LLM work provides reusable patterns and test cases.
- Skill implementation will use production skill structure: `SKILL.md`, `agents/openai.yaml`, `references/`, `scripts/`, `assets/`.
- The initial cluster can be useful without direct Search Console or paid rank-tracking API credentials.
open_questions:
- Which existing skills receive production upgrades after staging validation.
- Which external platforms/accounts are authorized for link placement and outreach.
- Which search/LLM monitoring surfaces can be automated without credentials or terms-of-service risk.
- Whether the future dashboard should be Markdown-only, Obsidian wiki, HTML dashboard, or all three.
risks:
- Overlapping skills may give conflicting advice unless shared artifacts and ownership boundaries are explicit.
- Link-placement automation can drift into spam if not strictly constrained.
- LLM citation monitoring can produce misleading conclusions if prompt sets, locale, personalization, or time are not recorded.
- UX, SEO, and LLM goals can conflict unless the orchestrator enforces visible-human-content-first rules.
- Skills may become large prompt dumps if references/scripts/evals are not separated.
regression_risks:
- Existing working skills may be weakened if upgraded without preserving current trigger descriptions and domain boundaries.
- Future site work may be over-optimized for crawlers and hurt user experience.
- Authority placement mistakes can harm domain reputation.
- Monitoring outputs can be mistaken for facts if they are not timestamped and scoped.
security_privacy_notes:
- Do not store secrets or private analytics rows in skill files, public wiki pages, or generated examples.
- Any crawler/IP/user-agent analysis must keep raw IP data private unless explicitly anonymized.
- External placement skills must not scrape, submit, or post to third-party services without explicit user authorization.
- Search Console, analytics, and assistant-monitoring credentials must stay in environment variables or approved secret stores.
non_functional_requirements:
- Skill instructions must be compact and progressively load references.
- Repeated checks should be deterministic scripts where possible.
- Each skill must include validation commands and at least three forward-test prompts.
- Orchestrator outputs must be auditable and resume-friendly.
- Reports must distinguish observed facts, inferred conclusions, and open questions.
milestones:
- M0 Existing skill inventory, trigger collision audit, and MVP release cut.
- M1 Shared skill-cluster architecture, artifact contracts, and freshness policy.
- M2 MVP skills: orchestrator, SEO/LLM architecture core, live regression validator, and MVP eval suite.
- M3 Content/editorial and UX/UI companion skills after MVP.
- M4 Monitoring and reality-layer skills after MVP.
- M5 White-hat authority placement skills after safety policy.
- M6 Packaging, wiki sync, operating handbook, and end-to-end validation.
timebox: planning phase 2026-06-11; implementation timebox to be set after T-024.
wiki_pages_to_read_before:
- `<mlllm-site-local-worktree>/wiki/projects/mlllm-site/mlllm-site.md`
- `<mlllm-site-local-worktree>/wiki/projects/mlllm-site/concepts/story-surface-seo-model.md`
- `<mlllm-site-local-worktree>/wiki/projects/mlllm-site/concepts/rich-results-schema-and-trust-gaps.md`
wiki_pages_to_update_after:
- local skill-cluster architecture page; exact wiki target is chosen in T-018
wiki_facts_to_capture:
- final skill names and install paths
- shared artifact schemas
- safety boundaries for external placement
- eval results and unresolved risks
wiki_do_not_store:
- secrets
- account credentials
- private analytics rows
- raw IP logs
- third-party platform private messages

## Pre-Implementation Gate

feature_preparation_path: ./plans/seo-llm-skill-cluster/FEATURE-PREPARATION.md
preimplementation_status: partial
entry_rule: Implementation tasks remain `draft` until T-000 inventories existing skills, T-001 approves the cluster contract, T-002 approves shared artifacts, T-021 approves trigger boundaries, T-023 approves freshness/primary-source policy, T-024 approves the MVP release cut, and active blocking alarms are either resolved or scoped to later tasks.

## Active Alarms

feature_active_alarms:
- A-EXT-001
- A-MON-001
feature_resolved_alarms:
- A-PATH-001
- A-PUB-001

### ALARM A-PATH-001

alarm_id: A-PATH-001
alarm_type: placeholder
severity: warning
status: resolved
scope: feature
applies_to: F-SEO-LLM-SKILL-CLUSTER
location: target skill install paths
summary: Final staging path for generated skills is confirmed.
current_value: staging under `./skills/*`; production install target gated at `<codex-skills-dir>/*`
why_present: Resolved in T-001 to avoid modifying installed production skills during MVP implementation.
missing_to_replace: none
replacement_target: New and upgraded skills are built in staging first, then installed only during T-017 after validation and user approval.
replacement_plan: Keep production install gated; use staging paths for implementation tasks.
owner_role: planner
blocks:
- none
must_propagate: true

### ALARM A-EXT-001

alarm_id: A-EXT-001
alarm_type: placeholder
severity: blocking
status: active
scope: task
applies_to: T-014, T-015
location: external authority placement automation
summary: External posting/link placement cannot be automated until authorized accounts, platforms, and rules are confirmed.
current_value: platform/account authorization unknown
why_present: The concept includes future placement of links on external platforms, but no approved platforms or credentials are specified.
missing_to_replace: List of authorized platforms/accounts, posting permissions, allowed formats, and compliance constraints.
replacement_target: White-hat placement workflow with dry-run, user approval, and platform-specific rule checks.
replacement_plan: Resolve during T-014; keep T-015 draft until a safe platform list and approval flow exist.
owner_role: planner
blocks:
- ready for T-015
- in_progress for T-015
- done for T-015
must_propagate: true

### ALARM A-MON-001

alarm_id: A-MON-001
alarm_type: placeholder
severity: warning
status: active
scope: task
applies_to: T-012, T-013
location: Search Console, rank tracking, and LLM citation monitoring inputs
summary: Some monitoring surfaces may require credentials or manual evidence capture.
current_value: access availability unknown
why_present: The concept requires real search/LLM picture, but credentials and approved monitoring surfaces are not listed.
missing_to_replace: Confirmed data sources, credentials policy, allowed APIs/tools, and manual fallback method.
replacement_target: Monitoring skills that distinguish automated evidence from manual evidence and never invent observed rankings/citations.
replacement_plan: T-012 defines source tiers; T-013 implements only credential-free checks first unless credentials are provided.
owner_role: planner
blocks:
- ready for credentialed monitoring subtasks
must_propagate: true

### ALARM A-PUB-001

alarm_id: A-PUB-001
alarm_type: placeholder
severity: blocking
status: resolved
scope: task
applies_to: T-025
location: GitHub publication target and public package approval
summary: GitHub publication target, public scope, sanitation review, and push approval were resolved during T-025.
current_value: Published public repository `https://github.com/sergekostenchuk/seo-llm-skill-cluster` from a fresh sanitized export.
why_present: The cluster contains local development paths, validation artifacts, and private-workstation context that must be sanitized before public release.
missing_to_replace: none
replacement_target: Public GitHub release package with sanitized paths, README, motivation text, task plan, skills, and validation artifacts.
replacement_plan: Completed in T-025 by creating a fresh sanitized export, running publication checks, committing the export, and pushing to the public GitHub repository.
owner_role: docs_sync
blocks:
- none
must_propagate: true

## Execution Policy

orchestration_mode: sequential_multi_agent
default_agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
status_legend:
- draft
- ready
- in_progress
- blocked
- needs_review
- approved
- done
- dropped

## Execution Governance

mode: CODE-FIRST, NO-FICTION, ONE-TASK-ONLY
no_fiction_policy:
- if required input is missing, return `INVALID_INPUT` instead of guessing
- do not invent skill files, commits, test results, approvals, platform permissions, crawl outcomes, ranking data, or LLM citations
- critical unknowns block ready, in_progress, approved, and done
mock_policy:
- mocks, stubs, fake integrations, dummy outputs, and pretend backends are forbidden by default
- temporary mocks require active alarms with missing_to_replace, replacement_target, replacement_plan, and blocked transitions
placeholder_policy:
- placeholders are allowed only while tasks are draft
- ready or in_progress is forbidden if critical fields are placeholders without an active alarm
- placeholder evidence, placeholder tests, and placeholder artifact paths are forbidden
alarm_propagation_policy:
- every active alarm must be copied into task prompts, runtime projections, and handoff summaries until resolved
prompt_policy:
- one task equals one prompt
- prompts must include RESUME_FROM, scope_in, scope_out, forbidden_areas, verification_strategy, and relevant active alarms
code_first_policy:
- implementation tasks require real file changes before docs-sync closure
- docs-only closure is allowed for planning/governance tasks T-001 and T-002
done_policy:
- dependencies are done or explicitly accepted as external pending
- required approvals passed
- verification_strategy executed
- commands_run and artifacts recorded
- rollback_plan exists
- Task Register and Task Block are synchronized
- no forbidden_areas touched
commit_policy:
- implementation tasks require commit hashes or explicit "not a git repo" note with artifact paths
- docs sync is separate from implementation evidence
sync_audit_policy:
- Task Register status must match Task Block status
- dependencies and unblocks must be bidirectional
boundary_audit_policy:
- external placement, credentialed monitoring, and existing skill upgrades require explicit reviewer approval
rollback_policy:
- failed required checks cannot go to done
- choose REVERT or FORWARD_FIX
timeout_escalation_policy:
- in_progress over timebox requires escalation
- max_review_loops exceeded requires escalation

## Verification Policy

verification_planning_rule:
- planner defines verification_strategy before implementer starts
- reviewer validates verification_strategy before implementation approval
- tester executes planned checks and records commands_run plus test_artifacts
critical_verification_fields:
- tests_required
- test_levels
- test_targets
- test_data_origin
- oracle
- stop_on_failure
- commands_planned
test_level_enum:
- unit
- integration
- e2e
- smoke
- manual-check-needed
planned_vs_executed_rule:
- commands_planned is filled before implementation
- commands_run is filled only after actual execution
failure_rule:
- if stop_on_failure is true, the task cannot pass to docs_sync after a required red test

## Shared Artifact Contract

artifact_contract_version: 0.2
required_shared_artifacts:
- `skill-inventory.md`: existing skills, trigger descriptions, overlap risks, upgrade/new recommendation.
- `cluster-architecture.md`: ownership matrix, staging/install path decision, handoff order, safety boundaries.
- `assets/artifact-schemas.md`: required fields, producers, consumers, evidence policy, privacy policy for shared artifacts.
- `goal_brief.md`: target site, audience, business goal, languages, constraints, non-goals.
- `semantic-core.yaml`: query clusters, intents, entities, language targets, priority, evidence.
- `entity-topic-map.yaml`: entities, topics, relationships, canonical pages, evidence URLs.
- `url-map.yaml`: planned URL, page type, locale, canonical, hreflang group, status.
- `internal-link-graph.yaml`: source URL, target URL, anchor intent, link type, reason.
- `schema-report.json`: URL, schema types, required fields, visible-content match status.
- `llm-discovery-report.md`: llms.txt, robots, sitemap, RSS, markdown alternates, answer blocks, source trails.
- `ux-journey-map.md`: personas, entry points, first actions, retention paths, friction.
- `crawler-access-audit.json`: URL, user agent, status, headers, timestamp, conclusion.
- `llm-citation-report.md`: assistant/search surface, query, timestamp, cited URLs, snippets, caveats.
- `authority-opportunity-register.yaml`: platform, URL, relevance, rule check, risk, proposed target page, approval status.
- `seo-regression-report.json`: deterministic live/static SEO validation checks and pass/fail evidence.
- `validation-summary.md`: checks run, pass/fail, artifacts, unresolved risks, next actions.
- `trigger-map.yaml`: skill name, trigger contexts, near-miss prompts, exclusion rules, owner skill.
- `freshness-policy.md`: unstable facts, primary sources, verification cadence, stale-data handling.
- `mvp-release-scope.md`: v1 skill list, excluded backlog skills, release criteria, active alarms accepted/deferred.
- `cluster-lint-report.json`: skill folder checks, placeholder checks, trigger collision findings, validation status.

## Skill Dependency Graph

central_orchestrator:
- `site-growth-orchestrator`
seo_llm_cluster:
- `semantic-core-architect`
- `information-architecture-seo`
- `internal-link-graph-architect`
- `technical-seo-schema-engineer`
- `llm-friendly-site-architect`
- `seo-regression-validator`
content_editorial_cluster:
- `content-strategy-architect`
- `editorial-quality-gate`
- `translation-localization-seo`
- `content-decay-monitor`
ux_ui_cluster:
- `ux-journey-architect`
- `conversion-retention-architect`
- `ui-layout-validator`
- `onboarding-architect`
authority_cluster:
- `external-authority-placement-scout`
- `backlink-quality-validator`
monitoring_cluster:
- `search-console-analyst`
- `llm-citation-monitor`
- `server-log-crawler-analyst`
- `rank-serp-monitor`
validation_cluster:
- `skill-cluster-implementation-validator`
- `skill-eval-runner`
- `trigger-collision-auditor`
- `cluster-consistency-linter`

## Task Register

| task_id | title | status | priority | owner_role | depends_on | required_approvals |
| --- | --- | --- | --- | --- | --- | --- |
| T-000 | Existing skill inventory and trigger-collision audit | done | P0 | planner | [] | [skill-review, architecture-review] |
| T-001 | Finalize cluster architecture and skill ownership boundaries | done | P0 | planner | [T-000] | [architecture-review, safety-review] |
| T-002 | Define shared artifact schemas and handoff contracts | done | P0 | planner | [T-001] | [architecture-review, validator-review] |
| T-003 | Build site-growth-orchestrator skill | done | P0 | implementer | [T-001, T-002, T-021, T-023, T-024] | [architecture-review, skill-review, eval-review] |
| T-004 | Build semantic-core-architect skill | done | P0 | implementer | [T-002, T-003, T-023, T-024] | [SEO-review, skill-review, eval-review] |
| T-005 | Build information-architecture-seo skill | done | P0 | implementer | [T-002, T-004, T-024] | [SEO-review, LLM-review, skill-review] |
| T-006 | Build internal-link-graph-architect skill | done | P0 | implementer | [T-002, T-005, T-024] | [SEO-review, UX-review, skill-review] |
| T-007 | Build technical-seo-schema-engineer skill | done | P0 | implementer | [T-002, T-005, T-023, T-024] | [SEO-review, code-review, eval-review] |
| T-008 | Build llm-friendly-site-architect skill or upgrade existing one | done | P0 | implementer | [T-002, T-005, T-006, T-007, T-021, T-023, T-024] | [LLM-review, SEO-review, skill-review] |
| T-009 | Build seo-regression-validator skill | done | P0 | implementer | [T-002, T-007, T-023, T-024] | [validator-review, code-review, eval-review] |
| T-010 | Build editorial-quality-gate MVP skill and content backlog | done | P1 | implementer | [T-002, T-003, T-024] | [editorial-review, SEO-review, skill-review] |
| T-011 | Build UX-journey-architect MVP skill and UX backlog | done | P1 | implementer | [T-002, T-003, T-024] | [UX-review, accessibility-review, skill-review] |
| T-012 | Build credential-free monitoring baseline and monitoring backlog | done | P1 | implementer | [T-002, T-009, T-023, T-024] | [analytics-review, privacy-review, eval-review] |
| T-013 | Build LLM citation monitoring workflow | done | P1 | implementer | [T-008, T-012] | [LLM-review, privacy-review, eval-review] |
| T-014 | Design white-hat authority placement policy and opportunity model | done | P1 | planner | [T-001, T-002] | [safety-review, SEO-review, legal/compliance-review] |
| T-015 | Build external-authority-placement-scout and backlink-quality-validator | done | P2 | implementer | [T-014] | [safety-review, SEO-review, user-approval] |
| T-016 | Build MVP skill-cluster eval suite and forward-test prompts | done | P0 | tester | [T-003, T-004, T-005, T-006, T-007, T-008, T-009, T-021, T-022, T-023, T-024] | [eval-review, skill-review] |
| T-017 | Package, validate, and document install/rollback workflow | done | P0 | docs_sync | [T-016, T-022] | [skill-review, docs-review] |
| T-018 | Create operating handbook and wiki sync | done | P1 | docs_sync | [T-017] | [docs-review, architecture-review] |
| T-019 | Run first end-to-end MVP use case on mlllm.io-style target | done | P1 | tester | [T-017, T-018, T-024] | [e2e-review, SEO-review, LLM-review, UX-review] |
| T-020 | Post-eval consolidation and cluster v1 release decision | done | P1 | planner | [T-019] | [architecture-review, user-approval] |
| T-021 | Trigger descriptions and near-miss prompt map | done | P0 | planner | [T-000, T-001] | [trigger-review, skill-review] |
| T-022 | Cluster consistency linter and placeholder audit | done | P0 | implementer | [T-002, T-021] | [validator-review, skill-review] |
| T-023 | Freshness and primary-source policy | done | P0 | planner | [T-001, T-002] | [freshness-review, safety-review] |
| T-024 | MVP release cut and backlog split | done | P0 | planner | [T-000, T-001, T-002, T-021, T-023] | [architecture-review, user-approval] |
| T-025 | Prepare and publish sanitized GitHub repository | done | P1 | docs_sync | [T-017, T-018, T-020, T-023] | [privacy-review, publication-review, user-approval] |

## Tasks

### TASK T-000

task_id: T-000
title: Existing skill inventory and trigger-collision audit
rationale: The cluster must not duplicate, weaken, or over-trigger existing SEO, LLM, UX, and skill-architecture skills. A production skill cluster starts by inventorying what already exists and identifying upgrade-vs-new decisions from evidence.
priority: P0
status: done
owner_role: planner
dependencies: []
blocked_by:
- none
unblocks:
- T-001
- T-021
- T-024
task_size: M
goal: Produce `skill-inventory.md` with existing skill names, paths, trigger descriptions, overlap risks, reuse candidates, and upgrade-vs-new recommendations.
scope_in:
- Inspect relevant existing skills under `<codex-skills-dir>`.
- Identify overlap with `seo-llm-site-architect`, `llm-friendly-site-optimizer`, `ui-ux-*`, `senior-skill-architect`, and `ta<api-key-redacted>`.
- Mark each concept skill as `new`, `upgrade-existing`, `merge`, `defer`, or `drop`.
- Identify likely trigger collisions and near-miss prompts.
scope_out:
- Editing existing skills.
- Creating new skills.
- Changing Codex installation state.
changed_subsystems:
- planning documents only
candidate_files:
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
- `./plans/seo-llm-skill-cluster/skill-inventory.md`
forbidden_areas:
- existing skill directories
- external websites/accounts
constraints:
- Inventory must cite actual skill paths and trigger descriptions.
- Do not infer an existing skill's behavior from its name alone; read enough of `SKILL.md` to classify overlap.
assumptions:
- Existing skills are available under `<codex-skills-dir>`.
open_questions:
- none
risks:
- missing an existing skill and creating a redundant new skill
- changing trigger strategy without reading current descriptions
regression_risks:
- future over-triggering if collision risks are not captured
security_privacy_notes:
- Do not copy secrets or unrelated private notes from skill directories.
non_functional_requirements:
- Inventory must be concise enough to use as an implementation input.
acceptance_criteria:
- `skill-inventory.md` or equivalent section lists relevant existing skills, paths, trigger descriptions, overlap risks, and recommended action.
- Every proposed MVP skill has a reuse/new/defer decision.
- At least 10 near-miss trigger examples are captured for T-021.
acceptance_checks:
- Cross-check proposed skill list against existing skill names and descriptions.
- Confirm no existing skill was modified.
exit_criteria:
- skill-review and architecture-review self-check complete against actual skill trigger descriptions.
rollback_plan:
- Revert planning artifact additions.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- reviewer
- docs_sync
required_approvals:
- skill-review
- architecture-review
max_review_loops: 2
escalation_rule: If inventory shows high overlap, stop implementation and revise MVP release cut in T-024.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- skill inventory and collision notes
test_data_origin: existing skill directories and concept file
oracle: Existing skills are classified with cited paths and no proposed skill lacks an upgrade/new/defer decision.
negative_tests:
- classify a skill without reading its trigger description
- recommend a new skill that duplicates an existing skill without justification
determinism_notes: Inventory is filesystem-based and should be repeatable for the same skill set.
flakiness_risk: installed skill list can change between sessions
stop_on_failure: true
commands_planned:
- `find <codex-skills-dir> -maxdepth 2 -name SKILL.md -print`
- `rg -n "seo|llm|site|ux|skill|crawler|schema|citation|analytics|link" <codex-skills-dir> -g SKILL.md`
commands_run:
- `find <codex-skills-dir> -maxdepth 2 -name SKILL.md -print`
- `rg -n "seo|llm|site|ux|skill|crawler|schema|citation|analytics|link" <codex-skills-dir> -g SKILL.md`
- `sed -n '1,220p' <codex-skills-dir>/seo-llm-site-architect/SKILL.md`
- `sed -n '1,220p' <codex-skills-dir>/llm-friendly-site-optimizer/SKILL.md`
- `sed -n '1,220p' <codex-skills-dir>/ui-ux-llm-product-architect/SKILL.md`
- `sed -n '1,180p' <codex-skills-dir>/web-security-architect/SKILL.md`
- `sed -n '1,180p' <codex-skills-dir>/agent-browser-codex/SKILL.md`
- `sed -n '1,160p' <codex-skills-dir>/llm-wiki-maintainer/SKILL.md`
expected_artifacts:
- skill inventory
- collision notes
artifact_locations:
- `./plans/seo-llm-skill-cluster/skill-inventory.md`
summary_format: Inventory path, reuse/new/defer decisions, collision risks, next task.

completion_notes:
- Created the inventory artifact with existing skill paths, trigger descriptions, overlap risks, proposed cluster decisions, and 12 near-miss prompt examples.
- Existing skill directories were read only and not modified.
- Main finding: creating every proposed skill immediately would duplicate existing SEO, LLM, and UX skills; the MVP should stay small and use upgrades/reuse where possible.

### TASK T-001

task_id: T-001
title: Finalize cluster architecture and skill ownership boundaries
rationale: The concept names many skills; before implementation, the cluster needs explicit boundaries so the orchestrator coordinates specialists instead of duplicating or contradicting them.
priority: P0
status: done
owner_role: planner
dependencies:
- T-000
blocked_by:
- none
unblocks:
- T-002
- T-021
- T-023
- T-024
- T-014
task_size: M
goal: Produce an approved skill ownership matrix, dependency graph, target path decision, and upgrade-vs-new decision for existing skills.
scope_in:
- Confirm final skill names.
- Decide which existing skills to upgrade versus which new skills to create.
- Define orchestrator authority boundaries.
- State explicitly that the orchestrator routes and prepares handoffs; it does not programmatically call other skills.
- Define cluster-to-cluster handoff order.
scope_out:
- Creating skill files.
- Running external audits.
- External placement.
changed_subsystems:
- planning documents only
candidate_files:
- `./CONCEPT-SCHEMA-SEO-LLM-SKILLS.MD`
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
- `./plans/seo-llm-skill-cluster/cluster-architecture.md`
forbidden_areas:
- existing skill directories
- external websites/accounts
constraints:
- Build new or changed skills in staging under `./skills` first.
- Do not install or modify production skills under `<codex-skills-dir>` until T-017.
assumptions:
- Current concept is the baseline architecture.
- T-000 inventory exists or this task remains draft.
open_questions:
- none
risks:
- over-fragmenting skills into too many small tools
- making orchestrator too broad
acceptance_criteria:
- Skill ownership matrix exists.
- Orchestrator responsibilities and non-responsibilities are explicit.
- Target install/staging path is confirmed and A-PATH-001 is resolved.
acceptance_checks:
- Review task register for no unowned cluster.
- Review dependency graph for cycles.
exit_criteria:
- architecture-review and safety-review self-check complete.
rollback_plan:
- Revert planning edits.
active_alarm_ids:
- none
resolved_alarm_ids:
- A-PATH-001
agent_sequence:
- planner
- reviewer
- docs_sync
required_approvals:
- architecture-review
- safety-review
max_review_loops: 2
escalation_rule: If ownership cannot be resolved after two loops, keep implementation tasks draft and ask user to choose minimal MVP skill set.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- skill dependency graph
- ownership matrix
test_data_origin: concept file and existing skill list
oracle: No cluster is unowned; no skill has overlapping authority without explicit handoff.
negative_tests:
- orchestrator tries to implement detailed schema checks itself
- link placement skill lacks safety owner
determinism_notes: Planning artifact review only.
flakiness_risk: none
stop_on_failure: true
commands_planned:
- `rg -n "site-growth-orchestrator|seo|llm|authority|monitoring" ./plans/seo-llm-skill-cluster/TASK-PLAN.md`
commands_run:
- `rg -n "site-growth-orchestrator|seo|llm|authority|monitoring" ./plans/seo-llm-skill-cluster/TASK-PLAN.md`
expected_artifacts:
- updated TASK-PLAN.md
- ownership matrix
artifact_locations:
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
- `./plans/seo-llm-skill-cluster/cluster-architecture.md`
summary_format: Architecture decisions, unresolved alarms, next task.

completion_notes:
- Created `cluster-architecture.md` with ownership matrix, dependency graph, handoff order, orchestrator authority boundary, and safety decisions.
- Resolved A-PATH-001 by choosing `./skills` as staging and keeping `<codex-skills-dir>` as the gated production install target for T-017.
- Existing installed skills remain read-only during MVP implementation.

### TASK T-002

task_id: T-002
title: Define shared artifact schemas and handoff contracts
rationale: Skills need a common data language for semantic cores, URL maps, link graphs, schema reports, UX journeys, crawler audits, LLM citation reports, and authority opportunities.
priority: P0
status: done
owner_role: planner
dependencies:
- T-001
blocked_by:
- none
unblocks:
- T-003
- T-004
- T-005
- T-006
- T-007
- T-008
- T-009
- T-010
- T-011
- T-012
- T-014
- T-021
- T-022
- T-023
- T-024
task_size: L
goal: Create stable artifact schemas and handoff contracts used by every skill.
scope_in:
- YAML/JSON/Markdown artifact schemas.
- Required fields and provenance rules.
- Evidence and timestamp conventions.
- Human-visible-content-first rule.
scope_out:
- Building skills.
- Running live audits.
changed_subsystems:
- plan assets or future `assets/` folder
candidate_files:
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
- `./plans/seo-llm-skill-cluster/assets/artifact-schemas.md`
forbidden_areas:
- external accounts
- production sites
constraints:
- No schema may require secrets or raw private analytics.
- Every artifact must separate observed facts from inferred conclusions.
assumptions:
- Markdown/YAML/JSON are sufficient for v1.
open_questions:
- none
risks:
- over-complex schemas may make skills hard to use
acceptance_criteria:
- Shared Artifact Contract is complete enough for all MVP skills.
- Every artifact has purpose, required fields, and producer/consumer skills.
acceptance_checks:
- Cross-check every skill in dependency graph has at least one input and output artifact.
exit_criteria:
- validator-review self-check complete.
rollback_plan:
- Revert artifact schema additions.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- reviewer
- docs_sync
required_approvals:
- architecture-review
- validator-review
max_review_loops: 2
escalation_rule: If schemas become too broad, reduce MVP to goal brief, semantic core, URL map, schema report, validation summary.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- shared artifact contract
test_data_origin: concept file and mlllm.io SEO/LLM artifacts
oracle: Every artifact has producer, consumers, required fields, evidence policy, and privacy policy.
negative_tests:
- artifact includes raw secrets
- artifact allows unproven claims without evidence
determinism_notes: Review-only.
flakiness_risk: none
stop_on_failure: true
commands_planned:
- `rg -n "required_shared_artifacts|semantic-core|url-map|schema-report|authority-opportunity" ./plans/seo-llm-skill-cluster/TASK-PLAN.md`
commands_run:
- `rg -n "required_shared_artifacts|semantic-core|url-map|schema-report|authority-opportunity" ./plans/seo-llm-skill-cluster/TASK-PLAN.md ./plans/seo-llm-skill-cluster/assets/artifact-schemas.md`
expected_artifacts:
- approved shared artifact contract
artifact_locations:
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
- `./plans/seo-llm-skill-cluster/assets/artifact-schemas.md`
summary_format: Added/changed schemas, producer/consumer map, unresolved fields.

completion_notes:
- Created `assets/artifact-schemas.md` with global evidence/privacy rules and schemas for goal brief, semantic core, entity-topic map, URL map, internal link graph, schema report, LLM discovery, UX journey, crawler audit, LLM citation, authority opportunities, SEO regression, trigger map, freshness policy, MVP release scope, and cluster lint.
- Added producer/consumer coverage so every MVP domain has at least one input and one output artifact.
- Confirmed artifacts forbid secrets, raw private analytics, raw IP logs, hidden SEO-only content, and unsupported claims.

### TASK T-003

task_id: T-003
title: Build site-growth-orchestrator skill
rationale: The cluster needs one central skill that classifies user intent, routes work to the right specialist sequence, prepares handoff prompts, collects evidence, maintains task-plan state, and prevents unsafe shortcuts.
priority: P0
status: done
owner_role: implementer
dependencies:
- T-001
- T-002
- T-021
- T-023
- T-024
blocked_by:
- none
unblocks:
- T-004
- T-005
- T-010
- T-011
- T-012
task_size: L
goal: Create a production-grade orchestrator skill that routes SEO/LLM/UX/content/monitoring/authority tasks and enforces evidence-first governance.
scope_in:
- `SKILL.md`
- `agents/openai.yaml`
- references for workflow and routing
- eval prompts for full orchestration
scope_out:
- Implementing specialist checks inside the orchestrator.
- External posting.
changed_subsystems:
- future orchestrator skill directory
candidate_files:
- future `site-growth-orchestrator/SKILL.md`
- future `site-growth-orchestrator/agents/openai.yaml`
- future `site-growth-orchestrator/references/workflow.md`
- future `site-growth-orchestrator/evals.json`
forbidden_areas:
- live websites
- existing skills unless upgrade is approved in T-001
constraints:
- Orchestrator must delegate specialist tasks.
- Orchestrator must not claim to programmatically invoke other skills; it prepares explicit handoff instructions and next-step prompts.
- Orchestrator must propagate active alarms.
assumptions:
- Target install path resolved by T-001.
open_questions:
- none
risks:
- overly broad orchestrator becomes a prompt dump
acceptance_criteria:
- Skill routes at least 10 user intents to correct specialist sequence.
- Skill refuses/flags black-hat or unevidenced requests.
- Skill outputs required artifacts and next-task plan.
acceptance_checks:
- Run production skill lint.
- Run forward-test prompts.
exit_criteria:
- skill-review and eval-review approved.
rollback_plan:
- Remove skill directory or revert commit.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- architecture-review
- skill-review
- eval-review
max_review_loops: 3
escalation_rule: If skill is too broad after review, split routing references and reduce SKILL.md to trigger/dispatch rules.
tests_required: yes
test_levels:
- unit
- smoke
- manual-check-needed
test_targets:
- skill structure
- trigger description
- routing behavior
- safety refusals
test_data_origin: generated eval prompts and mlllm.io use cases
oracle: Linter passes; forward tests produce correct specialist sequence and no invented evidence.
negative_tests:
- request hidden SEO content
- request bulk link spam
- ask for ranking claim without data
determinism_notes: Lint deterministic; forward tests reviewed manually.
flakiness_risk: LLM phrasing variability in forward tests.
stop_on_failure: true
commands_planned:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py "$ORCHESTRATOR_SKILL_PATH"`
- `python3 <codex-system-skill-creator>/scripts/quick_validate.py "$ORCHESTRATOR_SKILL_PATH"`
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/site-growth-orchestrator --json`
- `python3 <codex-system-skill-creator>/scripts/quick_validate.py ./skills/site-growth-orchestrator`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `python3 -m json.tool ./skills/site-growth-orchestrator/evals.json`
expected_artifacts:
- orchestrator skill directory
- validation report
- eval notes
artifact_locations:
- `./skills/site-growth-orchestrator/SKILL.md`
- `./skills/site-growth-orchestrator/agents/openai.yaml`
- `./skills/site-growth-orchestrator/references/workflow.md`
- `./skills/site-growth-orchestrator/assets/handoff-packet.template.md`
- `./skills/site-growth-orchestrator/evals.json`
- `./skills/site-growth-orchestrator/validation-report.md`
summary_format: Skill path, files changed, validation commands, eval result, risks.

completion_notes:
- Created staged `site-growth-orchestrator` skill under `./skills/site-growth-orchestrator`.
- Kept orchestrator scoped to routing, sequencing, handoff quality, evidence, alarms, and validation gates; specialist SEO/LLM/UX/security/authority work remains delegated.
- Added workflow reference, handoff packet template, OpenAI metadata, 6 positive eval cases, 6 negative eval cases, and validation report.
- Production skill linter passed with 0 errors and 0 warnings.
- Cluster linter passed with 0 critical issues and 0 warnings after the staged skill was added.
- System `quick_validate.py` could not run because the local validator environment lacks Python module `yaml`; recorded as toolchain limitation, not skill failure.

### TASK T-004

task_id: T-004
title: Build semantic-core-architect skill
rationale: SEO and LLM architecture starts from queries, intents, entities, topics, languages, and priority; this must be reusable before URL and link graph design.
priority: P0
status: done
owner_role: implementer
dependencies:
- T-002
- T-003
- T-023
- T-024
blocked_by:
- none
unblocks:
- T-005
task_size: M
goal: Create a skill that turns a site goal into `semantic-core.yaml` and `entity-topic-map.yaml`.
scope_in:
- query clusters
- intent classification
- entity/topic mapping
- language/locale priority
- competitor/source evidence capture
scope_out:
- generating pages
- link placement
changed_subsystems:
- future semantic-core skill directory
candidate_files:
- future `semantic-core-architect/SKILL.md`
- future `semantic-core-architect/references/semantic-core-rubric.md`
- future `semantic-core-architect/assets/semantic-core.template.yaml`
forbidden_areas:
- live site changes
constraints:
- Search volume or ranking claims require source/freshness.
acceptance_criteria:
- Produces semantic core with intents, entities, clusters, priority, evidence, and gaps.
- Marks unknown volume/competition as unknown instead of invented.
acceptance_checks:
- Forward-test on AI news site, SaaS site, and personal portfolio.
exit_criteria:
- SEO-review and eval-review approved.
rollback_plan:
- Remove skill directory or revert commit.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- SEO-review
- skill-review
- eval-review
max_review_loops: 2
escalation_rule: If source freshness cannot be established, keep volume fields optional and evidence-labeled.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- generated semantic core artifacts
test_data_origin: sample site briefs
oracle: Artifact includes no unsupported volume/rank claims and has actionable clusters.
negative_tests:
- ambiguous target audience
- no keyword data access
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/semantic-core-architect --json`
- `python3 -m json.tool ./skills/semantic-core-architect/evals.json`
- `ruby -e 'require "yaml"; YAML.load_file(ARGV[0]); YAML.load_file(ARGV[1]); puts "yaml-ok"' ./skills/semantic-core-architect/assets/semantic-core.template.yaml ./skills/semantic-core-architect/assets/entity-topic-map.template.yaml`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- semantic-core skill
- templates
- eval notes
artifact_locations:
- `./skills/semantic-core-architect/SKILL.md`
- `./skills/semantic-core-architect/agents/openai.yaml`
- `./skills/semantic-core-architect/references/semantic-core-rubric.md`
- `./skills/semantic-core-architect/assets/semantic-core.template.yaml`
- `./skills/semantic-core-architect/assets/entity-topic-map.template.yaml`
- `./skills/semantic-core-architect/evals.json`
- `./skills/semantic-core-architect/validation-report.md`
summary_format: Skill path, artifacts, eval outcomes.

completion_notes:
- Created staged `semantic-core-architect` skill with rubric, OpenAI metadata, semantic core template, entity-topic map template, evals, and validation report.
- The skill owns query clusters, intents, entities, topics, language priorities, evidence labels, and unknown metric handling.
- The skill explicitly does not own final URL/canonical policy, internal link graph, schema implementation, or rank guarantees.
- Production skill linter passed with 0 errors and 0 warnings.
- Template YAML and eval JSON validated.
- Cluster linter passed with 0 critical issues and 0 warnings across staged skills.

### TASK T-005

task_id: T-005
title: Build information-architecture-seo skill
rationale: Semantic core must become a crawlable URL structure with canonical rules, hreflang strategy, pillar/topic pages, and page roles.
priority: P0
status: done
owner_role: implementer
dependencies:
- T-002
- T-004
- T-024
blocked_by:
- none
unblocks:
- T-006
- T-007
- T-008
task_size: M
goal: Create a skill that produces `url-map.yaml`, page taxonomy, canonical model, hreflang groups, and pillar/topic/page-role rules.
scope_in:
- URL strategy
- canonical/hreflang
- information architecture
- pillar/topic/news/article/blog/project role separation
scope_out:
- writing final content
- UI visuals
changed_subsystems:
- future IA SEO skill directory
candidate_files:
- future `information-architecture-seo/SKILL.md`
- future `information-architecture-seo/references/url-architecture.md`
- future `information-architecture-seo/assets/url-map.template.yaml`
forbidden_areas:
- production website files
constraints:
- Must prevent duplicate public content bodies.
- Must align page role with user/search/LLM intent.
acceptance_criteria:
- URL map includes canonical, locale, page type, status, dependencies, and rationale.
- Skill explicitly handles one-brief-one-longform and other site-specific content models.
acceptance_checks:
- Forward-test on mlllm-style news/article model and non-news site.
exit_criteria:
- SEO-review and LLM-review approved.
rollback_plan:
- Remove skill directory or revert commit.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- SEO-review
- LLM-review
- skill-review
max_review_loops: 2
escalation_rule: If content model is unclear, skill must ask for clarification rather than inventing canonical strategy.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- URL map outputs
test_data_origin: sample semantic core artifacts
oracle: No duplicate role/canonical conflicts; hreflang groups are coherent.
negative_tests:
- canonicalize brief to longform when brief is standalone
- make topic page duplicate article body
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/information-architecture-seo --json`
- `python3 -m json.tool ./skills/information-architecture-seo/evals.json`
- `ruby -e 'require "yaml"; YAML.load_file(ARGV[0]); puts "yaml-ok"' ./skills/information-architecture-seo/assets/url-map.template.yaml`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- information architecture skill
artifact_locations:
- `./skills/information-architecture-seo/SKILL.md`
- `./skills/information-architecture-seo/agents/openai.yaml`
- `./skills/information-architecture-seo/references/url-architecture.md`
- `./skills/information-architecture-seo/assets/url-map.template.yaml`
- `./skills/information-architecture-seo/evals.json`
- `./skills/information-architecture-seo/validation-report.md`
summary_format: Skill path, URL strategy tests, risks.

completion_notes:
- Created staged `information-architecture-seo` skill with URL architecture reference, OpenAI metadata, URL map template, evals, and validation report.
- The skill converts semantic core outputs into URL strategy, page taxonomy, canonical rules, hreflang groups, status, index policy, and duplicate-content boundaries.
- It explicitly preserves one short brief plus one longform article as separate self-canonical surfaces when page roles differ.
- It rejects topic/article body duplication and unreviewed mass language publication.
- Production skill linter passed with 0 errors and 0 warnings.
- URL map YAML and eval JSON validated.
- Cluster linter passed with 0 critical issues and 0 warnings across staged skills.

### TASK T-006

task_id: T-006
title: Build internal-link-graph-architect skill
rationale: Search and LLM understanding depend on deliberate links between briefs, longforms, topics, projects, author pages, breadcrumbs, and source trails.
priority: P0
status: done
owner_role: implementer
dependencies:
- T-002
- T-005
- T-024
blocked_by:
- none
unblocks:
- T-008
- T-019
task_size: M
goal: Create a skill that produces `internal-link-graph.yaml` and validates link purpose, anchor intent, page role, and no-duplication rules.
scope_in:
- internal link graph
- breadcrumbs
- brief-longform links
- topic/project/author/source links
- orphan and overlink checks
scope_out:
- external backlink outreach
changed_subsystems:
- future link graph skill directory
candidate_files:
- future `internal-link-graph-architect/SKILL.md`
- future `internal-link-graph-architect/assets/internal-link-graph.template.yaml`
forbidden_areas:
- live website files
constraints:
- Link graph must reinforce canonical model, not create new duplicate story bodies.
acceptance_criteria:
- Produces link graph with source, target, anchor intent, link type, reason, and risk.
- Flags orphan pages and circular/irrelevant linking.
acceptance_checks:
- Test with one short news plus one longform plus topic/project/author pages.
exit_criteria:
- SEO-review and UX-review approved.
rollback_plan:
- Remove skill directory or revert commit.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- SEO-review
- UX-review
- skill-review
max_review_loops: 2
escalation_rule: If link intent is ambiguous, require page-role clarification.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- internal-link-graph outputs
test_data_origin: sample URL maps
oracle: Every link has a role and no page is linked as a duplicate replacement for itself.
negative_tests:
- hidden link recommendations
- irrelevant exact-match anchor stuffing
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/internal-link-graph-architect --json`
- `python3 -m json.tool ./skills/internal-link-graph-architect/evals.json`
- `ruby -e 'require "yaml"; YAML.load_file(ARGV[0]); puts "yaml-ok"' ./skills/internal-link-graph-architect/assets/internal-link-graph.template.yaml`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- link graph skill
artifact_locations:
- `./skills/internal-link-graph-architect/SKILL.md`
- `./skills/internal-link-graph-architect/agents/openai.yaml`
- `./skills/internal-link-graph-architect/references/link-graph-rules.md`
- `./skills/internal-link-graph-architect/assets/internal-link-graph.template.yaml`
- `./skills/internal-link-graph-architect/evals.json`
- `./skills/internal-link-graph-architect/validation-report.md`
summary_format: Skill path, graph checks, risks.

completion_notes:
- Created staged `internal-link-graph-architect` skill with link graph rules, OpenAI metadata, internal-link graph template, evals, and validation report.
- The skill produces link records with source, target, link type, anchor intent, user reason, SEO reason, LLM reason, placement, required flag, and risk.
- It preserves the one brief plus one longform model and rejects hidden links, exact-match stuffing, and duplicate story pages.
- Production skill linter passed with 0 errors and 0 warnings.
- Internal link graph YAML and eval JSON validated.
- Cluster linter passed with 0 critical issues and 0 warnings across staged skills.

### TASK T-007

task_id: T-007
title: Build technical-seo-schema-engineer skill
rationale: Public pages need deterministic head metadata, schema.org, sitemaps, RSS, robots, llms.txt, and social metadata that match visible content.
priority: P0
status: done
owner_role: implementer
dependencies:
- T-002
- T-005
- T-023
- T-024
blocked_by:
- none
unblocks:
- T-008
- T-009
task_size: L
goal: Create a skill for technical SEO/schema design and implementation guidance with deterministic checklists and templates.
scope_in:
- title/meta rules
- canonical/hreflang
- JSON-LD schema
- OpenGraph/Twitter
- sitemap/news-sitemap/RSS
- robots/llms.txt
- publisher/logo/ImageObject policy
scope_out:
- running live audits; that is T-009
changed_subsystems:
- future technical SEO skill directory
candidate_files:
- future `technical-seo-schema-engineer/SKILL.md`
- future `technical-seo-schema-engineer/references/schema-patterns.md`
- future `technical-seo-schema-engineer/assets/jsonld-templates.md`
forbidden_areas:
- hidden schema-only content
constraints:
- Schema must match visible content.
- Prefer deterministic validators over vibes.
acceptance_criteria:
- Skill can design schema/head metadata for news, article, topic, author, project, homepage, blog, index pages.
- Skill rejects hidden FAQ/schema claims.
acceptance_checks:
- Forward-test with mlllm-style page set.
exit_criteria:
- SEO-review and code-review approved.
rollback_plan:
- Remove skill directory or revert commit.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- SEO-review
- code-review
- eval-review
max_review_loops: 3
escalation_rule: If schema guidance conflicts with visible content, visible content wins and schema is reduced.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- schema/head templates
test_data_origin: mlllm.io examples and synthetic fixtures
oracle: Templates have required fields, visible-content match rule, and clear no-hidden-content policy.
negative_tests:
- FAQPage schema without visible FAQ
- NewsArticle.image missing
- duplicate canonical
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/technical-seo-schema-engineer --json`
- `python3 -m json.tool ./skills/technical-seo-schema-engineer/evals.json`
- `rg -n "NewsArticle|TechArticle|BreadcrumbList|WebSite|Organization|Person|canonical|hreflang|article:published_time" ./skills/technical-seo-schema-engineer/assets ./skills/technical-seo-schema-engineer/references/schema-patterns.md`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- technical SEO schema skill
artifact_locations:
- `./skills/technical-seo-schema-engineer/SKILL.md`
- `./skills/technical-seo-schema-engineer/agents/openai.yaml`
- `./skills/technical-seo-schema-engineer/references/schema-patterns.md`
- `./skills/technical-seo-schema-engineer/assets/jsonld-templates.md`
- `./skills/technical-seo-schema-engineer/assets/head-metadata.template.html`
- `./skills/technical-seo-schema-engineer/evals.json`
- `./skills/technical-seo-schema-engineer/validation-report.md`
summary_format: Skill path, schema coverage, validation.

completion_notes:
- Created staged `technical-seo-schema-engineer` skill with schema patterns, OpenAI metadata, JSON-LD templates, head metadata template, evals, and validation report.
- The skill covers NewsArticle, TechArticle/Article, BreadcrumbList, WebSite, Organization, Person, page-level metadata, canonical, hreflang, OG/Twitter, RSS, sitemap, robots, llms.txt, and ImageObject fallback policy.
- The skill rejects hidden FAQ/schema claims and requires schema to match visible content.
- Production skill linter passed with 0 errors and 0 warnings.
- Eval JSON validated and schema/head pattern coverage checked.
- Cluster linter passed with 0 critical issues and 0 warnings across staged skills.

### TASK T-008

task_id: T-008
title: Build llm-friendly-site-architect skill or upgrade existing one
rationale: LLM-friendly architecture needs llms.txt, answer blocks, source trails, entity pages, markdown alternates, and crawler-readable HTML without creating duplicate or hidden content.
priority: P0
status: done
owner_role: implementer
dependencies:
- T-002
- T-005
- T-006
- T-007
- T-021
- T-023
- T-024
blocked_by:
- none
unblocks:
- T-013
- T-019
task_size: L
goal: Create or upgrade a skill that designs LLM-friendly public site layers while preserving human-first content and canonical strategy.
scope_in:
- llms.txt
- answer blocks
- source trails
- entity pages
- markdown alternates
- AI crawler policy
- no duplicate story bodies
scope_out:
- LLM citation monitoring execution
changed_subsystems:
- future or existing LLM-friendly skill directory
candidate_files:
- existing `<codex-skills-dir>/llm-friendly-site-optimizer`
- existing `<codex-skills-dir>/seo-llm-site-architect`
- future `llm-friendly-site-architect`
forbidden_areas:
- existing skills unless T-001 approves upgrade
constraints:
- Human-visible content first.
- No hidden bot-only facts.
acceptance_criteria:
- Skill produces LLM discovery plan with llms.txt, source trail, entity, and answer-block policy.
- Skill refuses doorway pages and duplicate content expansion.
acceptance_checks:
- Forward-test against news site, docs site, project portfolio.
exit_criteria:
- LLM-review and SEO-review approved.
rollback_plan:
- Revert upgrade or remove new skill.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- LLM-review
- SEO-review
- skill-review
max_review_loops: 3
escalation_rule: If existing skill upgrade is risky, create a new skill and leave existing skill unchanged.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- LLM-friendly recommendations and refusal boundaries
test_data_origin: mlllm.io cases and synthetic site briefs
oracle: Recommendations improve machine readability without duplicate/hidden content.
negative_tests:
- add TL;DR to every short news page by default
- generate hidden FAQ schema
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/llm-friendly-site-architect --json`
- `python3 -m json.tool ./skills/llm-friendly-site-architect/evals.json`
- `rg -n "llms.txt|source trail|markdown|crawler|hidden|duplicate|brief|longform" ./skills/llm-friendly-site-architect`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- new or upgraded LLM-friendly skill
artifact_locations:
- `./skills/llm-friendly-site-architect/SKILL.md`
- `./skills/llm-friendly-site-architect/agents/openai.yaml`
- `./skills/llm-friendly-site-architect/references/llm-readable-architecture.md`
- `./skills/llm-friendly-site-architect/assets/llm-discovery-report.template.md`
- `./skills/llm-friendly-site-architect/assets/llms-txt.template.md`
- `./skills/llm-friendly-site-architect/evals.json`
- `./skills/llm-friendly-site-architect/validation-report.md`
summary_format: Skill path, upgrade/new decision, eval results.

completion_notes:
- Created new staged `llm-friendly-site-architect` skill and left installed `llm-friendly-site-optimizer` unchanged.
- The skill designs `llms.txt`, visible answer blocks, source trails, entity pages, markdown alternates, AI crawler policy handoff, and no-duplicate-content guardrails.
- It explicitly preserves the one short brief plus one longform model and rejects hidden bot-only facts, doorway pages, hidden FAQ schema, and duplicate story variants.
- Production skill linter passed with 0 errors and 0 warnings.
- Eval JSON validated and LLM-readable architecture rule coverage checked.
- Cluster linter passed with 0 critical issues and 0 warnings across staged skills.

### TASK T-009

task_id: T-009
title: Build seo-regression-validator skill
rationale: SEO/LLM claims must be checked against live HTML and artifacts instead of external-audit disagreement or subjective review.
priority: P0
status: done
owner_role: implementer
dependencies:
- T-002
- T-007
- T-023
- T-024
blocked_by:
- none
unblocks:
- T-012
- T-016
- T-019
task_size: L
goal: Create a validator skill that runs or guides live checks for schema, canonical, hreflang, OG/Twitter, robots, llms.txt, sitemap, RSS, crawler access, and performance evidence.
scope_in:
- live HTML audit
- fixture-based regression checks
- report templates
- Lighthouse/PageSpeed baseline guidance
- critical/warning severity model
scope_out:
- Search Console credentialed data
- external placement
changed_subsystems:
- future SEO regression validator skill directory
candidate_files:
- future `seo-regression-validator/SKILL.md`
- future `seo-regression-validator/scripts/`
- possible reuse of `<mlllm-site-local-worktree>/scripts/live_seo_audit.py`
forbidden_areas:
- mutating target sites during validation
constraints:
- Validation must record URLs, timestamps, user agents, status codes, and artifacts.
acceptance_criteria:
- Skill can audit a live site and produce `validation-summary.md`.
- Skill flags missing JSON-LD, duplicate canonical, missing image, missing hreflang, blocked public pages.
acceptance_checks:
- Run against local fixture or known public sample when authorized.
exit_criteria:
- validator-review and eval-review approved.
rollback_plan:
- Remove skill directory or revert commit.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- validator-review
- code-review
- eval-review
max_review_loops: 3
escalation_rule: If automated check is too target-specific, split generic validator and target adapters.
tests_required: yes
test_levels:
- unit
- smoke
- manual-check-needed
test_targets:
- parser/check scripts
- skill guidance
- report generation
test_data_origin: fixtures and mlllm.io audit script patterns
oracle: Known-bad fixtures fail; known-good fixtures pass; live checks record evidence without mutation.
negative_tests:
- fake passing report without fetching URL
- missing JSON-LD not detected
stop_on_failure: true
commands_planned:
- production skill linter
- script unit tests if scripts are added
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/seo-regression-validator --json`
- `SEO_REGRESSION_TIMESTAMP=2026-06-11T00:00:00Z python3 ./skills/seo-regression-validator/scripts/audit_static_seo.py ./skills/seo-regression-validator/fixtures/good-news.html --report ./skills/seo-regression-validator/fixtures/good-news.report.json`
- `SEO_REGRESSION_TIMESTAMP=2026-06-11T00:00:00Z python3 ./skills/seo-regression-validator/scripts/audit_static_seo.py ./skills/seo-regression-validator/fixtures/bad-news.html --report ./skills/seo-regression-validator/fixtures/bad-news.report.json; test $? -eq 1`
- `python3 -m json.tool ./skills/seo-regression-validator/evals.json`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- validator skill
- scripts and tests if applicable
artifact_locations:
- `./skills/seo-regression-validator/SKILL.md`
- `./skills/seo-regression-validator/agents/openai.yaml`
- `./skills/seo-regression-validator/references/regression-checklist.md`
- `./skills/seo-regression-validator/scripts/audit_static_seo.py`
- `./skills/seo-regression-validator/fixtures/good-news.html`
- `./skills/seo-regression-validator/fixtures/bad-news.html`
- `./skills/seo-regression-validator/fixtures/good-news.report.json`
- `./skills/seo-regression-validator/fixtures/bad-news.report.json`
- `./skills/seo-regression-validator/evals.json`
- `./skills/seo-regression-validator/validation-report.md`
summary_format: Skill path, checks covered, test results.

completion_notes:
- Created staged `seo-regression-validator` skill with checklist, OpenAI metadata, deterministic HTML audit script, good/bad fixtures, golden reports, evals, and validation report.
- The script checks title, meta description, canonical count, hreflang, JSON-LD parseability/types, NewsArticle.image, OpenGraph, Twitter card, viewport, RSS autodiscovery, and article meta tags.
- Good fixture passes; bad fixture fails as expected and detects missing meta description, duplicate canonical, and missing NewsArticle.image.
- Added deterministic `SEO_REGRESSION_TIMESTAMP` support so fixture reports can be stable.
- Production skill linter passed with 0 errors and 0 warnings.
- Cluster linter passed with 0 critical issues and 0 warnings across staged skills.

### TASK T-010

task_id: T-010
title: Build editorial-quality-gate MVP skill and content backlog
rationale: SEO and LLM-friendly work can fail if source quality, unsupported claims, prompt residue, translation drift, and content decay are not governed. For MVP, this must start with one focused editorial quality gate instead of four broad content skills at once.
priority: P1
status: done
owner_role: implementer
dependencies:
- T-002
- T-003
- T-024
blocked_by:
- none
unblocks:
- T-019
task_size: L
goal: Create the `editorial-quality-gate` MVP skill and document a backlog for `content-strategy-architect`, `translation-localization-seo`, and `content-decay-monitor`.
scope_in:
- `editorial-quality-gate`
- backlog decisions for `content-strategy-architect`, `translation-localization-seo`, and `content-decay-monitor`
- source-backed quality checklist
- no SEO-filler and no hidden-content checks
scope_out:
- live publishing pipelines
- model provider credentials
- implementing localization or decay-monitoring skills in this MVP task
changed_subsystems:
- future content/editorial skill directories
candidate_files:
- future content skill directories
forbidden_areas:
- target site content unless explicitly requested later
constraints:
- No SEO filler.
- Translations must be localized and quality-gated.
acceptance_criteria:
- `editorial-quality-gate` produces a quality checklist for news, longform, blog, project, and topic pages.
- Backlog entries exist for content strategy, localization, and decay monitoring with dependencies and acceptance criteria.
- Skill rejects unsupported claims, prompt residue, repeated blocks, hidden filler, and source-less SEO claims.
acceptance_checks:
- Forward-test content review for news, longform, blog, project page.
exit_criteria:
- editorial-review and SEO-review approved.
rollback_plan:
- Remove generated skills or revert commit.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- editorial-review
- SEO-review
- skill-review
max_review_loops: 2
escalation_rule: If too broad, split into editorial-quality-gate first and defer the rest.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- content recommendations and quality gates
test_data_origin: sample articles and site briefs
oracle: Recommendations are source-backed, non-duplicative, and human-useful.
negative_tests:
- prompt residue
- weak unsupported claims
- literal low-quality translation
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/editorial-quality-gate --json`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `python3 -m json.tool ./skills/editorial-quality-gate/evals.json ><tmp-dir>/editorial-quality-gate-evals.pretty.json`
expected_artifacts:
- editorial-quality-gate skill
- content/editorial backlog
artifact_locations:
- `./skills/editorial-quality-gate/SKILL.md`
- `./skills/editorial-quality-gate/references/editorial-quality-checklist.md`
- `./skills/editorial-quality-gate/references/content-backlog.md`
- `./skills/editorial-quality-gate/assets/quality-gate-report.template.md`
- `./skills/editorial-quality-gate/evals.json`
- `./skills/editorial-quality-gate/validation-report.md`
summary_format: Skills created, quality gates, eval results.
completion_notes:
- Created staged `editorial-quality-gate` skill with page-type gates for news, longform, blog, project, topic, and translation content.
- Added explicit checks for prompt residue, repeated generated blocks, unsupported claims, translation drift, hidden SEO filler, and duplicate public story bodies.
- Documented deferred content skills: `content-strategy-architect`, `translation-localization-seo`, and `content-decay-monitor`.
- Added trigger-map entry for `editorial-quality-gate`.
- Production skill linter passed with 0 errors and 0 warnings.
- Cluster linter passed with 0 critical issues and 0 warnings across 8 staged skills.

### TASK T-011

task_id: T-011
title: Build UX-journey-architect MVP skill and UX backlog
rationale: Search and LLM-friendly architecture must work for humans. For MVP, the first reusable skill should map user journeys and onboarding paths; layout validation, retention, and conversion skills can follow once the core flow is proven.
priority: P1
status: done
owner_role: implementer
dependencies:
- T-002
- T-003
- T-024
blocked_by:
- none
unblocks:
- T-019
task_size: L
goal: Create the `ux-journey-architect` MVP skill and document backlog tasks for conversion/retention, UI layout validation, and onboarding architecture.
scope_in:
- `ux-journey-architect`
- backlog decisions for `conversion-retention-architect`, `ui-layout-validator`, and `onboarding-architect`
- journey maps for new readers, returning users, agents, project reviewers, and conversion paths
scope_out:
- redesigning a specific site
- implementing UI layout validator in this MVP task
changed_subsystems:
- future UX/UI skill directories
candidate_files:
- future UX/UI skill directories
forbidden_areas:
- target site code
constraints:
- UX recommendations must not be generic landing-page filler.
- Accessibility and mobile layout must be explicit.
acceptance_criteria:
- `ux-journey-architect` produces journey map, entry points, first actions, trust points, and handoff to SEO/LLM artifacts.
- Backlog entries exist for conversion/retention, layout validation, and onboarding skills.
- Skill integrates with SEO/LLM structure instead of conflicting with it.
acceptance_checks:
- Forward-test for news/media site and SaaS/product site.
exit_criteria:
- UX-review and accessibility-review approved.
rollback_plan:
- Remove generated skills or revert commit.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- UX-review
- accessibility-review
- skill-review
max_review_loops: 2
escalation_rule: If too broad, implement `ux-journey-architect` first and defer layout validator.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- UX journey outputs
- layout validation checklist
test_data_origin: sample pages and screenshots
oracle: UX recommendations are actionable, domain-appropriate, and do not weaken SEO content model.
negative_tests:
- decorative redesign that hides content
- CTA hierarchy without user intent
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/ux-journey-architect --json`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `python3 -m json.tool ./skills/ux-journey-architect/evals.json ><tmp-dir>/ux-journey-architect-evals.pretty.json`
expected_artifacts:
- UX journey MVP skill
- UX/UI backlog
artifact_locations:
- `./skills/ux-journey-architect/SKILL.md`
- `./skills/ux-journey-architect/references/journey-workflow.md`
- `./skills/ux-journey-architect/references/ux-backlog.md`
- `./skills/ux-journey-architect/assets/journey-map.template.md`
- `./skills/ux-journey-architect/evals.json`
- `./skills/ux-journey-architect/validation-report.md`
summary_format: Skills created, UX outputs, eval results.
completion_notes:
- Created staged `ux-journey-architect` skill for user journeys, onboarding paths, entry points, first actions, trust points, accessibility/mobile risks, and SEO/LLM handoff notes.
- Documented deferred UX skills: `conversion-retention-architect`, `ui-layout-validator`, and `onboarding-architect`.
- Added trigger-map entry for `ux-journey-architect`.
- Production skill linter passed with 0 errors and 0 warnings.
- Cluster linter passed with 0 critical issues and 0 warnings across 9 staged skills.

### TASK T-012

task_id: T-012
title: Build credential-free monitoring baseline and monitoring backlog
rationale: Real search and LLM performance must be measured rather than assumed, but credentialed Search Console, rank tracking, and LLM citation automation should not block a useful MVP. The first monitoring layer should be credential-free and evidence-labeled.
priority: P1
status: done
owner_role: implementer
dependencies:
- T-002
- T-009
- T-023
- T-024
blocked_by:
- none
unblocks:
- T-013
- T-019
task_size: L
goal: Create a credential-free monitoring baseline skill or workflow and document backlog tasks for Search Console, rank/SERP, and richer crawler/LLM monitoring.
scope_in:
- credential-free `server-log-crawler-analyst` or monitoring baseline
- backlog decisions for `search-console-analyst`, `rank-serp-monitor`, and richer credentialed monitoring
- data-source tiering
- privacy rules
scope_out:
- storing credentials
- scraping search engines against terms
- implementing credentialed Search Console/rank APIs in this MVP task
changed_subsystems:
- future monitoring skill directories
candidate_files:
- future monitoring skill directories
forbidden_areas:
- private analytics exports unless user provides them for a task
constraints:
- Raw IP and query data are private.
- Ranking/citation claims require timestamp and method.
acceptance_criteria:
- MVP monitoring skill distinguishes live observed facts from unknowns and supports manual evidence.
- Backlog entries exist for Search Console, rank/SERP, and credentialed monitoring.
- Raw IP/privacy rules are explicit.
acceptance_checks:
- Forward-test with sample server log snippet and Search Console export description.
exit_criteria:
- analytics-review and privacy-review approved.
rollback_plan:
- Remove generated skills or revert commit.
active_alarm_ids:
- A-MON-001
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- analytics-review
- privacy-review
- eval-review
max_review_loops: 2
escalation_rule: If credentialed data access is unavailable, keep automated API portions deferred and ship manual-evidence workflows only.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- monitoring report outputs
test_data_origin: synthetic logs and sample exported metrics
oracle: Reports label source, timestamp, method, limitations, and privacy handling.
negative_tests:
- invent rankings
- expose raw IP in public output
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/server-log-crawler-analyst --json`
- `python3 ./skills/server-log-crawler-analyst/scripts/analyze_access_log.py ./skills/server-log-crawler-analyst/fixtures/sample-access.log --report <tmp-dir>/server-log-crawler-report.json`
- `python3 -m json.tool <tmp-dir>/server-log-crawler-report.json ><tmp-dir>/server-log-crawler-report.pretty.json`
- `python3 -m json.tool ./skills/server-log-crawler-analyst/evals.json ><tmp-dir>/server-log-crawler-evals.pretty.json`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `rg -n "203\.0\.113|raw_ips_in_report|iphash" <tmp-dir>/server-log-crawler-report.json`
expected_artifacts:
- credential-free monitoring baseline skill/workflow
- monitoring backlog
artifact_locations:
- `./skills/server-log-crawler-analyst/SKILL.md`
- `./skills/server-log-crawler-analyst/scripts/analyze_access_log.py`
- `./skills/server-log-crawler-analyst/references/data-source-tiers.md`
- `./skills/server-log-crawler-analyst/references/monitoring-backlog.md`
- `./skills/server-log-crawler-analyst/assets/crawler-monitor-report.template.md`
- `./skills/server-log-crawler-analyst/evals.json`
- `./skills/server-log-crawler-analyst/validation-report.md`
summary_format: Skills created, data tiers, risks.
completion_notes:
- Created staged `server-log-crawler-analyst` skill for credential-free crawler/public endpoint monitoring.
- Added privacy-preserving access-log analyzer that emits redacted IP hashes and refuses ranking/indexing/citation conclusions from logs alone.
- Documented data-source tiers and deferred monitoring skills: `search-console-analyst`, `rank-serp-monitor`, and `credentialed-crawler-monitor`.
- Added trigger-map entry for `server-log-crawler-analyst`.
- Production skill linter passed with 0 errors and 0 warnings.
- Cluster linter passed with 0 critical issues and 0 warnings across 10 staged skills.
- `A-MON-001` remains active for credentialed Search Console, rank, analytics, and assistant citation monitoring.

### TASK T-013

task_id: T-013
title: Build LLM citation monitoring workflow
rationale: LLM-friendly work should be judged by whether assistants can find and cite the target site for intended questions, but observations must be timestamped, repeatable, and caveated.
priority: P1
status: done
owner_role: implementer
dependencies:
- T-008
- T-012
blocked_by:
- none
unblocks:
- T-019
task_size: M
goal: Create a skill/workflow that tests target questions across approved LLM/search surfaces and records citation evidence without inventing results.
scope_in:
- target question matrix
- manual and automated observation modes
- citation report template
- competitor citation capture
scope_out:
- bypassing bot protections
- storing assistant account credentials
changed_subsystems:
- future `llm-citation-monitor` skill directory
candidate_files:
- future `llm-citation-monitor/SKILL.md`
- future `llm-citation-monitor/assets/citation-report.template.md`
forbidden_areas:
- assistant credentials in skill files
constraints:
- Must record assistant/search surface, date/time, query, locale, mode, cited URLs, snippets, and caveats.
acceptance_criteria:
- Skill can generate monitoring plan and report format.
- Skill refuses to claim citation without evidence.
acceptance_checks:
- Forward-test with target query list and mock-free manual observation transcript.
exit_criteria:
- LLM-review and privacy-review approved.
rollback_plan:
- Remove skill directory or revert commit.
active_alarm_ids:
- A-MON-001
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- LLM-review
- privacy-review
- eval-review
max_review_loops: 2
escalation_rule: If automation is not safe, ship manual evidence workflow only.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- citation report workflow
test_data_origin: sample target questions
oracle: Every reported citation has evidence and caveats; no unsupported claims.
negative_tests:
- "ChatGPT cites us" without screenshot/log/source
- personalized answer treated as universal ranking
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/llm-citation-monitor --json`
- `python3 -m json.tool ./skills/llm-citation-monitor/evals.json ><tmp-dir>/llm-citation-monitor-evals.pretty.json`
- `rg -n "sk-[A-Za-z0-9]{20,}|cookie|token|api key" ./skills/llm-citation-monitor || true`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- LLM citation monitoring skill/workflow
artifact_locations:
- `./skills/llm-citation-monitor/SKILL.md`
- `./skills/llm-citation-monitor/references/citation-evidence-policy.md`
- `./skills/llm-citation-monitor/assets/query-matrix.template.md`
- `./skills/llm-citation-monitor/assets/citation-report.template.md`
- `./skills/llm-citation-monitor/evals.json`
- `./skills/llm-citation-monitor/validation-report.md`
summary_format: Skill path, monitoring surfaces, evidence policy.
completion_notes:
- Created staged `llm-citation-monitor` skill as a manual/evidence-first workflow with query matrix and citation report templates.
- Skill requires timestamp, surface, query, locale, mode/account state, cited URLs, snippets, and caveats for every observed citation.
- Skill refuses unsupported "ChatGPT/Perplexity cites us" claims and rejects universal conclusions from one personalized answer.
- No assistant credentials, cookies, API keys, screenshots, or private transcripts were stored.
- Production skill linter passed with 0 errors and 0 warnings.
- Cluster linter passed with 0 critical issues and 0 warnings across 11 staged skills.
- `A-MON-001` remains active for credentialed/automated monitoring, but no longer blocks this manual workflow artifact.

### TASK T-014

task_id: T-014
title: Design white-hat authority placement policy and opportunity model
rationale: External link acquisition can help site authority, but it must be relevance-first, permission-aware, platform-rule-aware, and explicitly non-spam.
priority: P1
status: done
owner_role: planner
dependencies:
- T-001
- T-002
blocked_by:
- none
unblocks:
- T-015
task_size: M
goal: Define safe policy, approval workflow, and `authority-opportunity-register.yaml` fields before any placement skill is built.
scope_in:
- white-hat placement policy
- platform rule checklist
- opportunity scoring
- approval gates
- UTM/monitoring policy
scope_out:
- actual outreach/posting
- scraping external platforms
changed_subsystems:
- planning docs and future authority assets
candidate_files:
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
- future authority policy reference
forbidden_areas:
- external platforms/accounts
constraints:
- No automated placement without user approval.
- No link farms, PBNs, fake reviews, comment spam, or irrelevant directories.
acceptance_criteria:
- Policy defines allowed/forbidden placement types.
- Opportunity register includes relevance, indexability, rule check, risk, target page, and approval.
acceptance_checks:
- Review policy against black-hat/grey-hat cases.
exit_criteria:
- safety-review and legal/compliance-review approved.
rollback_plan:
- Revert policy additions.
active_alarm_ids:
- A-EXT-001
resolved_alarm_ids:
- none
agent_sequence:
- planner
- reviewer
- docs_sync
required_approvals:
- safety-review
- SEO-review
- legal/compliance-review
max_review_loops: 2
escalation_rule: If external permissions remain unknown, keep T-015 draft and ship scout as dry-run only later.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- authority placement policy
test_data_origin: concept file and known white-hat SEO rules
oracle: Policy blocks spam patterns and requires platform compliance and user approval.
negative_tests:
- automated forum posting
- irrelevant directory submission
- PBN/link farm recommendation
stop_on_failure: true
commands_planned:
- policy review checklist
commands_run:
- `rg -n "automated forum|Irrelevant directory|PBN|link farm|No external action|must not post|without explicit user approval|A-EXT-001|dry-run" ./plans/seo-llm-skill-cluster/authority`
- `rg -n "platform_rules_checked|user_approval_status|external_action_status|risk_score|target_url|proposed_anchor" ./plans/seo-llm-skill-cluster/authority/opportunity-register.schema.yaml`
expected_artifacts:
- authority placement policy
- opportunity register schema
artifact_locations:
- `./plans/seo-llm-skill-cluster/authority/white-hat-authority-policy.md`
- `./plans/seo-llm-skill-cluster/authority/opportunity-register.schema.yaml`
- `./plans/seo-llm-skill-cluster/authority/policy-review.md`
summary_format: Policy decisions, blocked actions, allowed actions.
completion_notes:
- Created white-hat authority placement policy with allowed/forbidden opportunity types, platform-rule checklist, scoring model, approval gates, and UTM/monitoring policy.
- Created opportunity register schema with relevance, indexability/link attribute, platform rule check, risk, target page, proposed anchor, and approval/action status fields.
- Reviewed black-hat/grey-hat negative cases: automated forum posting, irrelevant directory submission, PBN/link farm, fake reviews, paid undisclosed links, and mass profile creation are blocked.
- No external platform, account, outreach, posting, submission, PR, DM, email, or account edit was performed.
- `A-EXT-001` remains active for real external actions; T-015 may only create dry-run-first skills unless separately approved.

### TASK T-015

task_id: T-015
title: Build external-authority-placement-scout and backlink-quality-validator
rationale: After safe policy exists, the cluster needs skills that find legitimate link opportunities and validate placement quality without becoming spam automation.
priority: P2
status: done
owner_role: implementer
dependencies:
- T-014
blocked_by:
- none
unblocks:
- T-019
task_size: L
goal: Create dry-run-first authority scout and backlink validator skills.
scope_in:
- opportunity discovery
- platform rule checks
- relevance scoring
- indexability/nofollow/sponsored checks
- outreach draft preparation
- backlink validation
scope_out:
- automatic posting without approval
- paid link buying
- black-hat tactics
changed_subsystems:
- future authority skill directories
candidate_files:
- future `external-authority-placement-scout/SKILL.md`
- future `backlink-quality-validator/SKILL.md`
forbidden_areas:
- external accounts unless explicitly authorized
constraints:
- Dry-run by default.
- User approval required before any external action.
acceptance_criteria:
- Skill produces opportunity register, not silent external posts.
- Validator rejects toxic/irrelevant/spam placements.
acceptance_checks:
- Forward-test with GitHub README, awesome-list PR, Product Hunt, Dev.to, Reddit/HN scenarios.
exit_criteria:
- safety-review and user-approval passed.
rollback_plan:
- Remove skills or disable external-action instructions.
active_alarm_ids:
- A-EXT-001
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- safety-review
- SEO-review
- user-approval
max_review_loops: 3
escalation_rule: If safe external action cannot be guaranteed, ship only opportunity scout and validator, no placement execution.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- authority opportunity recommendations
- spam refusal behavior
test_data_origin: synthetic platform scenarios
oracle: Skill never posts automatically; every opportunity has relevance, rule status, risk, and approval field.
negative_tests:
- "post my link everywhere"
- link farm opportunity
- fake review request
stop_on_failure: true
commands_planned:
- production skill linter
- forward-test prompt set
commands_run:
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/external-authority-placement-scout --json`
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py ./skills/backlink-quality-validator --json`
- `python3 -m json.tool ./skills/external-authority-placement-scout/evals.json ><tmp-dir>/external-authority-placement-scout-evals.pretty.json`
- `python3 -m json.tool ./skills/backlink-quality-validator/evals.json ><tmp-dir>/backlink-quality-validator-evals.pretty.json`
- `rg -n "Do not post|Dry-run|without separate explicit approval|rejects|PBN|fake review|link farm" ./skills/external-authority-placement-scout ./skills/backlink-quality-validator`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- authority scout skill
- backlink validator skill
artifact_locations:
- `./skills/external-authority-placement-scout/SKILL.md`
- `./skills/external-authority-placement-scout/references/scouting-workflow.md`
- `./skills/external-authority-placement-scout/evals.json`
- `./skills/external-authority-placement-scout/validation-report.md`
- `./skills/backlink-quality-validator/SKILL.md`
- `./skills/backlink-quality-validator/references/validation-rubric.md`
- `./skills/backlink-quality-validator/evals.json`
- `./skills/backlink-quality-validator/validation-report.md`
summary_format: Skills created, dry-run behavior, refusal tests.
completion_notes:
- Created dry-run `external-authority-placement-scout` skill that produces opportunity registers and drafts only, with no posting/outreach/submission/account action.
- Created `backlink-quality-validator` skill that rejects toxic, irrelevant, spam, PBN, fake-review, paid-undisclosed, hidden, or low-quality placements.
- Added trigger-map entry for `backlink-quality-validator`; `external-authority-placement-scout` already had a policy-gated entry.
- Production skill linter passed with 0 errors and 0 warnings for both skills.
- Cluster linter passed with 0 critical issues and 0 warnings across 13 staged skills.
- `A-EXT-001` remains active for real external actions; these skills are dry-run-first and do not authorize placement.

### TASK T-016

task_id: T-016
title: Build MVP skill-cluster eval suite and forward-test prompts
rationale: The MVP cluster must be tested on successful use cases and negative cases before broader content, UX, monitoring, and authority skills are implemented.
priority: P0
status: done
owner_role: tester
dependencies:
- T-003
- T-004
- T-005
- T-006
- T-007
- T-008
- T-009
- T-021
- T-022
- T-023
- T-024
blocked_by:
- none
unblocks:
- T-017
task_size: L
goal: Create eval prompts, expected behavior rubrics, and benchmark records for the approved MVP skill set from T-024.
scope_in:
- successful use cases from mlllm.io-style workflows
- negative tests for black-hat SEO, hidden content, fake evidence, duplicate content
- skill trigger tests
- artifact contract tests
- MVP-only evals for the skills approved by T-024
scope_out:
- grading model automation unless tooling is available
- full-cluster eval coverage for deferred skills; that becomes a follow-up after those skills exist
changed_subsystems:
- future eval files under each skill or shared eval folder
candidate_files:
- future `evals.template.json`
- future per-skill eval prompt files
forbidden_areas:
- live external posting
constraints:
- Evals must not assume credentials or external access.
acceptance_criteria:
- Each MVP skill has at least 3 positive and 3 negative forward-test prompts.
- Orchestrator has end-to-end scenario prompts.
- Deferred skills are explicitly excluded from MVP eval scope unless T-024 includes them.
acceptance_checks:
- Run linter/eval review.
exit_criteria:
- eval-review approved.
rollback_plan:
- Revert eval files.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- tester
- reviewer
- docs_sync
required_approvals:
- eval-review
- skill-review
max_review_loops: 2
escalation_rule: If automated eval harness is unavailable, keep manual eval table and record limitation.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- skill outputs against eval prompts
test_data_origin: mlllm.io task-plan, concept file, synthetic sites
oracle: Skills route correctly, refuse unsafe tasks, and produce expected artifacts without invented evidence.
negative_tests:
- hidden FAQ schema
- fake Search Console claim
- automated link spam
- duplicate doorway pages
stop_on_failure: true
commands_planned:
- production skill linter for each skill
- manual forward-test prompt run
commands_run:
- `MVP_EVAL_TIMESTAMP=2026-06-11T00:00:00Z python3 ./plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py . --report ./plans/seo-llm-skill-cluster/evals/mvp-eval-results.json`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `for d in ./skills/*; do python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py "$d" --json ><tmp-dir>/skill-lint-$(basename "$d").json || exit 1; done; echo production-lint-ok`
expected_artifacts:
- eval suite
- eval results summary
artifact_locations:
- `./plans/seo-llm-skill-cluster/evals/mvp-skill-cluster-evals.json`
- `./plans/seo-llm-skill-cluster/evals/mvp-eval-results.json`
- `./plans/seo-llm-skill-cluster/evals/mvp-eval-summary.md`
- `./plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py`
summary_format: Evals added, pass/fail, uncovered risks.

completion_notes:
- Created shared MVP eval suite with 3 end-to-end cases and shared eval coverage for `cluster-consistency-linter`.
- Added `verify_mvp_evals.py` to combine per-skill evals with shared cluster-linter evals and produce `mvp-eval-results.json`.
- Eval verification passed for 8 MVP units: orchestrator, semantic core, IA SEO, internal link graph, technical SEO/schema, LLM-friendly architecture, SEO regression validator, and cluster consistency linter.
- Every MVP unit has at least 3 positive and 3 negative cases; orchestrator has 6 and 6.
- Deferred P1/P2 skills remain excluded from MVP eval scope.
- Production linter passed for every staged skill; cluster linter passed with 0 critical issues and 0 warnings.

### TASK T-017

task_id: T-017
title: Package, validate, and document install/rollback workflow
rationale: A multi-skill cluster needs predictable install, validation, reload, and rollback instructions so it can be safely reused.
priority: P0
status: done
owner_role: docs_sync
dependencies:
- T-016
- T-022
blocked_by:
- none
unblocks:
- T-018
- T-019
task_size: M
goal: Validate skill package structure and produce install/rollback notes.
scope_in:
- skill validation commands
- package checklist
- Codex reload note
- rollback path
scope_out:
- changing target sites
changed_subsystems:
- generated skill directories
- docs
candidate_files:
- future cluster README
- future validation reports
forbidden_areas:
- secrets
constraints:
- Every skill must pass available validators or record toolchain blocker.
acceptance_criteria:
- Install/rollback workflow is clear.
- Validation results are recorded.
acceptance_checks:
- Run quick validators where available.
exit_criteria:
- skill-review and docs-review approved.
rollback_plan:
- Remove installed skills or revert commits.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- tester
- docs_sync
- reviewer
required_approvals:
- skill-review
- docs-review
max_review_loops: 2
escalation_rule: If validator toolchain fails, record exact error and rely on production linter plus manual review.
tests_required: yes
test_levels:
- smoke
- manual-check-needed
test_targets:
- all generated skill directories
test_data_origin: generated skill files
oracle: Validation passes or failures are explicit and actionable.
negative_tests:
- missing SKILL.md
- missing frontmatter description
- unresolved placeholder in production skill
stop_on_failure: true
commands_planned:
- production skill linter
- Codex quick_validate
commands_run:
- `python3 -m json.tool ./plans/seo-llm-skill-cluster/package-manifest.json ><tmp-dir>/package-manifest.pretty.json`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `MVP_EVAL_TIMESTAMP=2026-06-11T00:00:00Z python3 ./plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py . --report ./plans/seo-llm-skill-cluster/evals/mvp-eval-results.json`
- `for d in ./skills/*; do python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py "$d" --json ><tmp-dir>/skill-lint-$(basename "$d").json || exit 1; done; echo production-lint-ok`
- `python3 <codex-system-skill-creator>/scripts/quick_validate.py /path/to/skill`
expected_artifacts:
- install guide
- rollback guide
- validation reports
artifact_locations:
- `./plans/seo-llm-skill-cluster/package-manifest.json`
- `./plans/seo-llm-skill-cluster/install-rollback.md`
- `./plans/seo-llm-skill-cluster/validation-matrix.md`
- `./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `./plans/seo-llm-skill-cluster/evals/mvp-eval-results.json`
summary_format: Validation matrix, install steps, rollback steps.
completion_notes:
- Created a package manifest for 7 staged skills under `./skills`.
- Created explicit install and rollback instructions; no production install into `<codex-skills-dir>` was performed.
- Recorded validation matrix with production-linter, cluster-linter, MVP-eval, and quick_validate results.
- Production linter passed for all 7 staged skills.
- Cluster consistency linter passed with 0 critical issues and 0 warnings.
- MVP eval verifier passed for 8 MVP units and 3 end-to-end cases.
- Codex `quick_validate.py` is blocked in this environment by `ModuleNotFoundError: No module named 'yaml'`; this is recorded as a toolchain blocker rather than a staged-skill content failure.

### TASK T-018

task_id: T-018
title: Create operating handbook and wiki sync
rationale: The cluster needs a human-readable handbook explaining sequence, artifacts, evidence rules, safety constraints, and when to call each skill.
priority: P1
status: done
owner_role: docs_sync
dependencies:
- T-017
blocked_by:
- none
unblocks:
- T-019
task_size: M
goal: Create an operating handbook and sync stable decisions to wiki.
scope_in:
- cluster overview
- invocation sequence
- artifact lifecycle
- evidence standards
- safety constraints
- troubleshooting
scope_out:
- implementation code changes
changed_subsystems:
- docs/wiki
candidate_files:
- future cluster README
- future wiki page
forbidden_areas:
- secrets
- private analytics rows
constraints:
- Handbook must not include credentials or platform-private data.
acceptance_criteria:
- User can understand what to run first, what each skill returns, and how to validate.
acceptance_checks:
- Dry-read handbook against 3 example workflows.
exit_criteria:
- docs-review approved.
rollback_plan:
- Revert docs/wiki changes.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- docs_sync
- reviewer
required_approvals:
- docs-review
- architecture-review
max_review_loops: 2
escalation_rule: If wiki target is unknown, keep handbook local and record wiki sync as pending.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- handbook clarity
test_data_origin: generated skills and plan
oracle: Handbook maps every common intent to a skill sequence and artifact set.
negative_tests:
- ambiguous "do SEO" workflow with no validation
stop_on_failure: true
commands_planned:
- `rg -n "secret|password|api key|token" "$HANDBOOK_PATH"`
commands_run:
- `rg -n "secret|password|api key|token" ./plans/seo-llm-skill-cluster/operating-handbook.md ./wiki/seo-llm-skill-cluster.md || true`
- `rg -n "Workflow A|Workflow B|Workflow C|one short news brief|one expanded longform article|not installed" ./plans/seo-llm-skill-cluster/operating-handbook.md ./wiki/seo-llm-skill-cluster.md`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
expected_artifacts:
- operating handbook
- wiki sync note
artifact_locations:
- `./plans/seo-llm-skill-cluster/operating-handbook.md`
- `./wiki/seo-llm-skill-cluster.md`
summary_format: Docs created, wiki synced, unresolved docs gaps.
completion_notes:
- Created a local operating handbook with routing rules, artifact lifecycle, evidence standards, safety boundaries, validation commands, and troubleshooting guidance.
- Created a local wiki page under `./wiki`; external Obsidian vault was not modified.
- Dry-read coverage is represented by three explicit handbook workflows: new site architecture, metadata/schema fix, and one-brief-plus-one-longform protection.
- Secret scan found only handbook warning text and the scan command itself; no credential values were added.
- Cluster consistency linter still passes with 0 critical issues and 0 warnings.

### TASK T-019

task_id: T-019
title: Run first end-to-end MVP use case on mlllm.io-style target
rationale: The approved MVP cluster should be validated on a real successful use case pattern before deferred content, UX, monitoring, and authority skills are treated as production.
priority: P1
status: done
owner_role: tester
dependencies:
- T-017
- T-018
- T-024
blocked_by:
- none
unblocks:
- T-020
task_size: L
goal: Run a complete MVP dry-run workflow against a permitted target and record outputs, gaps, and skill improvements.
scope_in:
- goal brief
- semantic core
- URL map
- schema/LLM audit
- live SEO regression validation where allowed
- trigger routing and handoff checks
- MVP artifact consistency checks
scope_out:
- production deploy
- external posting
- full authority opportunity workflow unless T-024 explicitly includes it
- credentialed monitoring unless access is provided and T-024 includes it
changed_subsystems:
- reports only
candidate_files:
- future `.local/evals/seo-llm-skill-cluster/`
forbidden_areas:
- live site changes unless separately requested
- external posting
constraints:
- Use dry-run and evidence labels.
acceptance_criteria:
- End-to-end report exists with artifacts and improvement backlog.
- No unsafe external actions were taken.
- Workflow scope matches T-024 MVP release cut.
acceptance_checks:
- Review all generated artifacts for consistency and no invented evidence.
exit_criteria:
- e2e-review approved.
rollback_plan:
- Delete dry-run report artifacts if incorrect; no production changes expected.
active_alarm_ids:
- A-MON-001
- A-EXT-001
resolved_alarm_ids:
- none
agent_sequence:
- planner
- tester
- reviewer
- docs_sync
required_approvals:
- e2e-review
- SEO-review
- LLM-review
- UX-review
max_review_loops: 2
escalation_rule: If target access is insufficient, use mlllm.io public pages for read-only dry-run and record limitations.
tests_required: yes
test_levels:
- e2e
- manual-check-needed
test_targets:
- full cluster workflow
test_data_origin: permitted target site and generated artifacts
oracle: Artifacts are internally consistent, evidence-backed, and produce actionable next tasks.
negative_tests:
- external placement performed without approval
- live ranking claim without measurement
stop_on_failure: true
commands_planned:
- run orchestrator dry-run prompt
- run validator checks allowed by target access
commands_run:
- `SEO_REGRESSION_TIMESTAMP=2026-06-11T00:00:00Z python3 ./skills/seo-regression-validator/scripts/audit_static_seo.py https://mlllm.io/ --report ./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/homepage-seo-report.json`
- `SEO_REGRESSION_TIMESTAMP=2026-06-11T00:00:00Z python3 ./skills/seo-regression-validator/scripts/audit_static_seo.py https://mlllm.io/news/948-langchain-introduces-self-checking-module-for-ai-agents/ --report ./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/en-news-seo-report.json`
- `SEO_REGRESSION_TIMESTAMP=2026-06-11T00:00:00Z python3 ./skills/seo-regression-validator/scripts/audit_static_seo.py https://mlllm.io/articles/948-langchain-introduces-rubricmiddleware-module-for-ai-agent-self-correction/ --report ./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/en-article-seo-report.json`
- `python3` read-only fetch of `robots.txt`, `llms.txt`, `sitemap.xml`, `news-sitemap.xml`, and `rss.xml`
- `python3 -m json.tool ./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/site-access-snapshot.json ><tmp-dir>/e2e-site-access.pretty.json`
- `for f in ./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/*seo-report.json; do python3 -m json.tool "$f" ><tmp-dir>/$(basename "$f").pretty.json || exit 1; done`
- `rg -n "\b(secret|password|api key|token)\b|sk-[A-Za-z0-9]{20,}" ./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style || true`
expected_artifacts:
- end-to-end report
- improvement backlog
artifact_locations:
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/e2e-report.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/goal-brief.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/routing-and-handoffs.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/semantic-core.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/url-map.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/internal-link-graph.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/technical-seo-schema-audit.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/llm-friendly-audit.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/improvement-backlog.md`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/site-access-snapshot.json`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/homepage-seo-report.json`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/en-news-seo-report.json`
- `./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style/en-article-seo-report.json`
summary_format: Workflow result, artifacts, blockers, improvements.
completion_notes:
- Ran a read-only dry-run against public `mlllm.io` URLs; no production website, TG-NEWS, Telegram, or external placement action was performed.
- Representative homepage, EN brief, and EN longform pages passed the staged SEO regression validator with 0 issues.
- Public discovery surfaces were reachable: `robots.txt`, `llms.txt`, `sitemap.xml`, `news-sitemap.xml`, and `rss.xml`.
- Created goal brief, routing/handoff notes, semantic core, URL map, internal link graph, technical SEO/schema audit, LLM-friendly audit, and improvement backlog.
- Remaining gaps are explicit: no full sitemap crawl, no Lighthouse/Core Web Vitals, no Search Console, no server logs, no LLM citation monitoring, and no browser visual smoke in this E2E.

### TASK T-020

task_id: T-020
title: Post-eval consolidation and cluster v1 release decision
rationale: After the first end-to-end run, the cluster should be consolidated into v1 or held for fixes based on evidence.
priority: P1
status: done
owner_role: planner
dependencies:
- T-019
blocked_by:
- none
unblocks: []
task_size: S
goal: Decide whether the skill cluster is ready for v1 use, needs fixes, or should remain experimental.
scope_in:
- evaluate T-019 results
- classify defects
- update task-plan statuses
- decide release/readiness
scope_out:
- creating new skills beyond approved backlog
changed_subsystems:
- plan and docs
candidate_files:
- TASK-PLAN.md
- release notes
forbidden_areas:
- production sites
- external accounts
constraints:
- Release decision must cite eval evidence.
acceptance_criteria:
- v1 decision is recorded with evidence.
- Backlog of fixes or next skills is explicit.
acceptance_checks:
- Review eval artifacts and unresolved alarms.
exit_criteria:
- architecture-review and user-approval passed.
rollback_plan:
- Mark cluster experimental and keep skills installed only as draft/internal if needed.
active_alarm_ids:
- A-MON-001
- A-EXT-001
resolved_alarm_ids:
- none
agent_sequence:
- planner
- reviewer
- docs_sync
required_approvals:
- architecture-review
- user-approval
max_review_loops: 2
escalation_rule: If evidence is mixed, release only the passing MVP skills and keep risky clusters draft.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- release readiness
test_data_origin: T-019 reports
oracle: Decision cites evidence, unresolved alarms, and exact scope of v1.
negative_tests:
- release all skills despite failed evals
- ignore active safety alarms
stop_on_failure: true
commands_planned:
- review T-019 artifacts
- update task statuses
commands_run:
- `rg -n "status: pass|pass, 0 issues|No P0|Open Items|Cluster Verdict|No production" ./plans/seo-llm-skill-cluster/evals/e2e-mlllm-style ./plans/seo-llm-skill-cluster/validation-matrix.md`
expected_artifacts:
- v1 release decision
- backlog
artifact_locations:
- `./plans/seo-llm-skill-cluster/release-decision-v1.md`
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
summary_format: Decision, ready skills, deferred skills, next actions.
completion_notes:
- Recorded the release decision as `v1-staged`, not production-installed.
- Ready staged skills: orchestrator, semantic core, IA SEO, internal link graph, technical SEO/schema, LLM-friendly architecture, and SEO regression validator.
- Cited T-017 validation and T-019 E2E evidence.
- Kept monitoring and external-placement alarms active.
- Deferred editorial quality gate, UX journey skill, monitoring baseline, LLM citation monitor, authority placement skills, full sitemap crawl, Lighthouse/Core Web Vitals, and credentialed Search Console/analytics work.

### TASK T-021

task_id: T-021
title: Trigger descriptions and near-miss prompt map
rationale: A multi-skill cluster can fail even when each skill is good if trigger descriptions overlap and near-miss prompts route to the wrong skill. Trigger boundaries must be designed before production implementation.
priority: P0
status: done
owner_role: planner
dependencies:
- T-000
- T-001
blocked_by:
- none
unblocks:
- T-003
- T-008
- T-016
- T-024
task_size: M
goal: Produce `trigger-map.yaml` with intended trigger contexts, near-miss prompts, exclusion rules, and owner skill for each MVP and deferred skill.
scope_in:
- Trigger descriptions for MVP skills.
- Near-miss prompts for SEO vs LLM vs UX vs validator vs authority requests.
- Collision rules for existing skills and new skills.
- Explicit "do not trigger when..." cases.
scope_out:
- Editing skill files.
- Running evals.
- External site work.
changed_subsystems:
- planning artifacts
candidate_files:
- `./plans/seo-llm-skill-cluster/trigger-map.yaml`
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
forbidden_areas:
- existing skill directories
constraints:
- Trigger map must use evidence from T-000 inventory.
- Existing skill behavior must not be inferred from names only.
assumptions:
- T-000 identifies relevant existing trigger descriptions.
open_questions:
- none
risks:
- over-triggering the orchestrator on requests that should go to specialist skills
- splitting skills so narrowly that users cannot predict which one applies
regression_risks:
- existing useful skills could become harder to trigger if future descriptions overlap
security_privacy_notes:
- No private user data needed.
non_functional_requirements:
- Trigger map must be concise enough to use in `SKILL.md` frontmatter work.
acceptance_criteria:
- Every MVP skill has trigger contexts, near-miss prompts, exclusion rules, and owner role.
- At least 10 near-miss prompts are captured.
- Trigger conflicts with existing skills are explicitly resolved or recorded as active follow-up risks.
acceptance_checks:
- Compare trigger map against T-000 inventory.
- Review near-miss prompts for ambiguous routing.
exit_criteria:
- trigger-review and skill-review self-check complete.
rollback_plan:
- Revert trigger-map additions.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- reviewer
- docs_sync
required_approvals:
- trigger-review
- skill-review
max_review_loops: 2
escalation_rule: If trigger ownership remains ambiguous, MVP release cut must exclude the ambiguous skill until resolved.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- trigger map and near-miss prompts
test_data_origin: T-000 skill inventory and concept file
oracle: Each near-miss prompt has exactly one primary owner skill and clear fallback/handoff behavior.
negative_tests:
- "audit SEO" routes to three skills without owner
- "make site pretty" triggers SEO skill instead of UX skill
- "place links everywhere" bypasses authority safety policy
determinism_notes: Trigger map is a static artifact.
flakiness_risk: future skill list changes require rerun
stop_on_failure: true
commands_planned:
- `rg -n "description:|name:" <codex-skills-dir> -g SKILL.md`
- `rg -n "trigger|near-miss|owner" ./plans/seo-llm-skill-cluster/TASK-PLAN.md`
commands_run:
- `rg -n "description:|name:" <codex-skills-dir> -g SKILL.md`
- `rg -n "trigger|near-miss|owner" ./plans/seo-llm-skill-cluster/TASK-PLAN.md ./plans/seo-llm-skill-cluster/trigger-map.yaml`
- `python3 - <<'PY' ...` attempted YAML parse; PyYAML unavailable in system Python.
- `ruby -e 'require "yaml"; data = YAML.load_file(ARGV[0]); puts "yaml-ok"; puts "skills=#{data["skills"].length}"; puts "near_miss_registry=#{data["near_miss_registry"].length}"' ./plans/seo-llm-skill-cluster/trigger-map.yaml`
expected_artifacts:
- trigger-map artifact
- updated plan notes
artifact_locations:
- `./plans/seo-llm-skill-cluster/trigger-map.yaml`
summary_format: Trigger map path, conflicts resolved, conflicts deferred.

completion_notes:
- Created `trigger-map.yaml` with 12 skill entries, global routing rules, exclusion rules, handoff targets, and near-miss ownership.
- Captured 12 registry-level near-miss prompts; per-skill prompt examples bring total prompt ownership entries to 38.
- Deferred external authority and credentialed monitoring triggers remain post-MVP and gated by A-EXT-001/A-MON-001.

### TASK T-022

task_id: T-022
title: Cluster consistency linter and placeholder audit
rationale: A production skill cluster needs deterministic checks for folder structure, frontmatter, missing resources, unresolved placeholders, trigger collisions, and artifact contract coverage.
priority: P0
status: done
owner_role: implementer
dependencies:
- T-002
- T-021
blocked_by:
- none
unblocks:
- T-016
- T-017
task_size: M
goal: Create a lightweight cluster consistency linter or checklist that validates generated skill directories and emits `cluster-lint-report.json`.
scope_in:
- Check for `SKILL.md`, valid frontmatter, `agents/openai.yaml`, references/assets/scripts as required.
- Check unresolved placeholders and fake evidence strings.
- Check trigger-map coverage for each MVP skill.
- Check each MVP skill has eval prompts and validation commands.
scope_out:
- Replacing Codex `quick_validate.py`.
- Validating external SEO facts.
changed_subsystems:
- future cluster linter/checklist artifacts
candidate_files:
- future `./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py`
- future `./plans/seo-llm-skill-cluster/cluster-lint-report.json`
forbidden_areas:
- external websites/accounts
constraints:
- If no script is created, a deterministic checklist must exist and the limitation must be recorded.
- The linter must not claim production readiness from structural checks alone.
assumptions:
- Skill paths are resolved by T-001/T-024 before execution.
open_questions:
- none
risks:
- overfitting linter to one local folder layout
regression_risks:
- missing placeholder detection could allow draft text into production skills
security_privacy_notes:
- Linter must not print secrets if scanning files.
non_functional_requirements:
- Linter/checklist should run quickly on local skill folders.
acceptance_criteria:
- Linter/checklist covers structure, frontmatter, placeholders, trigger map, evals, and validation commands.
- A report artifact is produced or a manual report template exists.
- Unresolved path marker strings fail after MVP skill paths are resolved.
acceptance_checks:
- Run against at least one known existing skill and one synthetic bad fixture or documented bad-case checklist.
exit_criteria:
- validator-review and skill-review approved.
rollback_plan:
- Remove linter/checklist artifacts.
active_alarm_ids:
- none
resolved_alarm_ids:
- none
agent_sequence:
- planner
- implementer
- reviewer
- tester
- docs_sync
required_approvals:
- validator-review
- skill-review
max_review_loops: 2
escalation_rule: If script scope is too broad, ship a checklist first and create a script follow-up.
tests_required: yes
test_levels:
- unit
- smoke
- manual-check-needed
test_targets:
- cluster linter/checklist
- placeholder detection
- trigger-map coverage
test_data_origin: generated skills, existing skills, synthetic bad fixture if script exists
oracle: Known-bad missing `SKILL.md`/placeholder/trigger gaps are detected; known-good existing skill is not falsely failed for irrelevant optional resources.
negative_tests:
- missing `SKILL.md`
- unresolved skill-path marker after path resolution
- no eval prompts for MVP skill
- missing trigger-map entry
determinism_notes: Script checks must be path-based and stable.
flakiness_risk: optional resources differ by skill type
stop_on_failure: true
commands_planned:
- `python3 "$CLUSTER_LINTER_PATH" "$SKILL_CLUSTER_PATH"`
- `python3 <codex-skills-dir>/senior-skill-architect/scripts/lint_production_skill.py "$SKILL_PATH"`
commands_run:
- `ruby -e 'require "yaml"; data = YAML.load_file(ARGV[0]); puts "yaml-ok"; puts "skills=#{data["skills"].length}"; puts "near_miss_registry=#{data["near_miss_registry"].length}"' ./plans/seo-llm-skill-cluster/trigger-map.yaml`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --skills-root <codex-skills-dir> --only senior-skill-architect --no-mvp-required`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --skills-root ./plans/seo-llm-skill-cluster/fixtures --only bad-placeholder-skill --no-mvp-required`
expected_artifacts:
- cluster linter or checklist
- cluster lint report
artifact_locations:
- `./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py`
- `./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `./plans/seo-llm-skill-cluster/fixtures/bad-placeholder-skill/SKILL.md`
summary_format: Linter/checklist path, checks covered, known limitations.

completion_notes:
- Created `scripts/lint_skill_cluster.py` with structural checks for `SKILL.md`, frontmatter, trigger-map coverage, placeholders, possible secrets, eval signals, and validation signals.
- Added `cluster-lint-report.json`; current cluster report passes with 0 critical issues and 1 expected warning because `./skills` does not exist until T-003 begins skill creation.
- Updated `trigger-map.yaml` from 12 to 17 skill entries so all MVP skills from `mvp-release-scope.md` have explicit trigger ownership.
- Verified known-good `senior-skill-architect` does not fail critically; warnings are from intentional placeholder-test strings in script/assets.
- Added and tested bad fixture `bad-placeholder-skill`; linter exits nonzero and catches missing frontmatter plus unresolved TODO.

### TASK T-023

task_id: T-023
title: Freshness and primary-source policy
rationale: SEO, schema.org, crawler rules, LLM bot names, platform policies, Search Console behavior, and ranking/citation surfaces change. Skills need explicit freshness rules so they browse or verify unstable facts instead of relying on stale memory.
priority: P0
status: done
owner_role: planner
dependencies:
- T-001
- T-002
blocked_by:
- none
unblocks:
- T-003
- T-004
- T-007
- T-008
- T-009
- T-012
- T-016
- T-024
task_size: M
goal: Produce `freshness-policy.md` defining unstable fact categories, primary sources, verification cadence, and stale-data handling for all MVP and deferred skills.
scope_in:
- Google/Search Central and schema.org freshness rules.
- AI crawler/bot policy verification rules.
- Platform policy verification for external placement.
- Search/LLM/rank monitoring evidence freshness.
- "Browse/verify required" triggers.
scope_out:
- Running live audits.
- Building monitoring integrations.
changed_subsystems:
- planning artifacts
candidate_files:
- `./plans/seo-llm-skill-cluster/freshness-policy.md`
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
forbidden_areas:
- external posting
- credentials
constraints:
- Primary sources must be preferred for technical SEO, schema, crawler rules, and platform policies.
- Recommendations must label observed, inferred, and unknown facts.
assumptions:
- Web access may be available during future live checks, but skills need a fallback for no-network contexts.
open_questions:
- Credentialed Search Console, rank, and assistant monitoring access remains unknown; tracked by A-MON-001.
risks:
- stale bot/platform guidance can cause incorrect access or link-placement recommendations
regression_risks:
- future skills may claim "current" rules from old references
security_privacy_notes:
- Do not store credentials or private analytics in freshness artifacts.
non_functional_requirements:
- Policy must be short enough to be loaded by multiple skills.
acceptance_criteria:
- Freshness policy lists unstable fact categories and primary sources.
- It defines when browsing/verification is mandatory.
- It defines how to report uncertainty when verification is unavailable.
acceptance_checks:
- Review policy against SEO/schema, crawler, LLM citation, and external placement cases.
exit_criteria:
- freshness-review and safety-review self-check complete.
rollback_plan:
- Revert freshness policy artifact.
active_alarm_ids:
- A-MON-001
resolved_alarm_ids:
- none
agent_sequence:
- planner
- reviewer
- docs_sync
required_approvals:
- freshness-review
- safety-review
max_review_loops: 2
escalation_rule: If primary source list cannot be confirmed, keep source list minimal and require live verification by task.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- freshness policy
test_data_origin: senior-skill-architect freshness rules and project audit cases
oracle: Policy prevents unsupported current-fact claims and gives a clear verification path.
negative_tests:
- recommend outdated crawler rule without verification
- cite platform placement rule without source/date
- claim live ranking without timestamp/tool
determinism_notes: Policy review only.
flakiness_risk: external source availability changes
stop_on_failure: true
commands_planned:
- `rg -n "freshness|primary source|verify|browse|current" ./plans/seo-llm-skill-cluster/TASK-PLAN.md`
commands_run:
- `rg -n "freshness|primary source|verify|browse|current" ./plans/seo-llm-skill-cluster/TASK-PLAN.md ./plans/seo-llm-skill-cluster/freshness-policy.md`
- `rg -n "Google|OpenAI|Anthropic|Perplexity|schema.org|Browse/Verify|unknown_current_status|A-MON-001" ./plans/seo-llm-skill-cluster/freshness-policy.md`
expected_artifacts:
- freshness policy
artifact_locations:
- `./plans/seo-llm-skill-cluster/freshness-policy.md`
summary_format: Policy path, mandatory verification triggers, unresolved access gaps.

completion_notes:
- Created `freshness-policy.md` with source tiers, primary-source URLs, unstable fact categories, mandatory browse/verify triggers, no-network fallback, evidence labels, and skill-specific requirements.
- Current-fact claims now require source URL, timestamp, method, implementation impact, and caveat.
- A-MON-001 remains active because credentialed monitoring surfaces are not confirmed.

### TASK T-024

task_id: T-024
title: MVP release cut and backlog split
rationale: The concept describes a large long-term cluster. Production execution needs a small v1 release cut so implementation starts with the highest leverage skills and defers broad clusters until the core is proven.
priority: P0
status: done
owner_role: planner
dependencies:
- T-000
- T-001
- T-002
- T-021
- T-023
blocked_by:
- none
unblocks:
- T-003
- T-004
- T-005
- T-006
- T-007
- T-008
- T-009
- T-010
- T-011
- T-012
- T-016
- T-019
task_size: M
goal: Produce `mvp-release-scope.md` defining v1 skills, deferred skills, accepted/deferred alarms, and release criteria.
scope_in:
- Choose MVP skill set.
- Split broad content, UX, monitoring, and authority clusters into MVP vs backlog.
- Confirm which existing skills are upgraded, left untouched, or replaced.
- Define v1 release criteria and deferred risks.
scope_out:
- Creating skill files.
- Running end-to-end evals.
changed_subsystems:
- planning artifacts
candidate_files:
- future `./plans/seo-llm-skill-cluster/mvp-release-scope.md`
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
forbidden_areas:
- existing skill directories
- external websites/accounts
constraints:
- MVP must be small enough to validate end-to-end.
- Deferred skills must remain explicit backlog, not silently dropped.
- Authority placement cannot enter MVP while A-EXT-001 remains blocking unless dry-run-only and user-approved.
assumptions:
- Approved MVP is orchestrator, semantic core, information architecture, internal link graph, technical SEO/schema, LLM-friendly site architecture, SEO regression validator, trigger map, freshness policy, cluster linter, and eval suite.
open_questions:
- none
risks:
- MVP too broad to finish
- MVP too narrow to prove the workflow
regression_risks:
- deferred skills may be mistaken as dropped unless backlog is explicit
security_privacy_notes:
- MVP must not require secrets or private analytics.
non_functional_requirements:
- MVP definition must be understandable without reading the full 20+ task plan.
acceptance_criteria:
- `mvp-release-scope.md` lists v1 skills, deferred skills, and why.
- Broad tasks T-010/T-011/T-012/T-015 are classified as MVP, follow-up, or deferred.
- Active alarms are classified as resolved, accepted for MVP, or blocking.
- T-016 eval scope matches the MVP list.
acceptance_checks:
- Compare task register dependencies to MVP cut.
- Verify no deferred skill is required by MVP eval.
exit_criteria:
- architecture-review and user-approval passed.
rollback_plan:
- Revert MVP scope document and keep all implementation tasks draft.
active_alarm_ids:
- A-MON-001
- A-EXT-001
resolved_alarm_ids:
- none
agent_sequence:
- planner
- reviewer
- docs_sync
required_approvals:
- architecture-review
- user-approval
max_review_loops: 2
escalation_rule: If MVP scope cannot be approved, default to the smallest useful set: orchestrator, one SEO/LLM architecture skill, regression validator, trigger map, freshness policy, and eval suite.
tests_required: manual-check-needed
test_levels:
- manual-check-needed
test_targets:
- MVP scope and dependencies
test_data_origin: T-000 inventory, T-001 ownership matrix, T-002 artifact contract, T-021 trigger map, T-023 freshness policy
oracle: MVP scope has no unresolved critical dependency on deferred or blocked skills.
negative_tests:
- include authority placement while A-EXT-001 blocks external action
- require Search Console credentials for MVP while A-MON-001 remains active
- include every planned skill in v1
determinism_notes: Planning artifact review only.
flakiness_risk: user priorities may change
stop_on_failure: true
commands_planned:
- `rg -n "T-010|T-011|T-012|T-015|T-016|T-024|A-EXT-001|A-MON-001" ./plans/seo-llm-skill-cluster/TASK-PLAN.md`
commands_run:
- `rg -n "T-010|T-011|T-012|T-015|T-016|T-024|A-EXT-001|A-MON-001" ./plans/seo-llm-skill-cluster/TASK-PLAN.md ./plans/seo-llm-skill-cluster/mvp-release-scope.md`
- `python3 - <<'PY' ... register/block dependency consistency check ... PY`
expected_artifacts:
- MVP release scope document
- updated task dependencies if needed
artifact_locations:
- `./plans/seo-llm-skill-cluster/mvp-release-scope.md`
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
summary_format: MVP skills, deferred skills, active alarms, next implementation task.

completion_notes:
- Created `mvp-release-scope.md` with MVP v0.1 skill list, follow-up v0.2 work, gated backlog, alarm classification, install policy, eval scope, and release criteria.
- Included T-006 internal link graph and T-008 LLM-friendly architecture in MVP because the cluster must model SEO/LLM structure and link graph, not only metadata.
- Reclassified T-010, T-011, and T-012 as follow-up v0.2 work; T-013 and T-015 remain gated backlog under A-MON-001 and A-EXT-001.
- Updated T-008 and T-016 dependencies so eval scope matches the approved MVP list.
- Register/block consistency check passed with no mismatches and no missing task references.

### TASK T-025

task_id: T-025
title: Prepare and publish sanitized GitHub repository
rationale: The completed skill cluster should be published as a public GitHub project with the task plan, motivation, README, and validation evidence, but only after local paths, credentials, private infrastructure details, raw logs, and workstation-specific traces are removed or generalized.
priority: P1
status: done
owner_role: docs_sync
dependencies:
- T-017
- T-018
- T-020
- T-023
blocked_by: []
unblocks: []
task_size: M
goal: Create a public-ready GitHub package for the SEO/LLM skill cluster, write the public README/motivation, sanitize sensitive data, commit, and publish only after explicit user approval.
scope_in:
- Select or confirm target GitHub repository/remote and branch.
- Decide public package scope: skills, TASK-PLAN, validation reports, wiki summary, README, motivation, and publication notes.
- Rewrite public docs to remove absolute local paths and private workstation details.
- Replace local paths such as `<local-user-path>/...` with repo-relative or placeholder paths.
- Remove or redact secrets, API keys, tokens, private IPs, raw logs, account emails, private server paths, and credential references.
- Write README and public motivation based on the user's draft text.
- Mention that the cluster work was managed with `task-plan-v2-dashboard`, linking to `https://github.com/sergekostenchuk/task-plan-v2-dashboard`.
- Explain in the public narrative that `task-plan-v2-dashboard` helps users step away from constant model-monitoring and context checking while long multi-step work continues, including the user's light "go make a cup of coffee" framing in a professional but human tone.
- Include safety boundaries: no automatic external posting, no invented SEO/LLM claims, dry-run authority skills, evidence-first monitoring.
- Run sensitive-data scans and JSON/YAML/skill validation.
- Commit sanitized publication changes.
- Push to GitHub only after explicit approval.
scope_out:
- Publishing before target repo/remote is confirmed.
- Installing staged skills into production Codex skills.
- Real external authority placement, outreach, PRs, DMs, email, or account edits.
- Changing mlllm.io, TG-NEWS, server config, DNS, or production website code.
- Claiming OpenAI grant acceptance or external SEO/LLM ranking outcomes.
changed_subsystems:
- public repository docs
- sanitized task-plan/package artifacts
- Git remote configuration
- README and publication narrative
candidate_files:
- `./README.md`
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
- `./plans/seo-llm-skill-cluster/*`
- `./skills/*`
- `./wiki/seo-llm-skill-cluster.md`
- `./.gitignore`
forbidden_areas:
- secrets
- API keys
- private server credentials
- private analytics rows
- raw IP logs
- external platforms/accounts without approval
- live production site/server changes
constraints:
- Public artifacts must not contain absolute private workstation paths.
- Public artifacts must not contain credentials or private infrastructure details.
- README must not overclaim rankings, grant approval, or assistant citations.
- GitHub push requires explicit target repository and approval.
- If sanitation scan finds unresolved sensitive data, the task cannot move to done.
assumptions:
- The public project can describe mlllm.io as the motivating use case.
- The public project can include the skill cluster and task plan after local paths are generalized.
- User will choose or approve the GitHub repository before push.
open_questions:
- Target repository URL or new repository name.
- Whether to publish the full TASK-PLAN or a sanitized public projection plus archive.
- Whether screenshots should be committed, linked externally, or omitted.
risks:
- leaking local filesystem paths or private infrastructure details
- overclaiming SEO/LLM outcomes
- publishing before user approves the exact repository
- confusing staged skills with installed production Codex skills
regression_risks:
- over-sanitizing may break validation examples if paths are replaced inconsistently
- publishing generated reports may expose implementation context not intended for public readers
security_privacy_notes:
- Never publish secrets, raw private logs, private IP rows, credentials, cookies, tokens, or private analytics rows.
- Treat absolute local paths as sensitive workstation metadata.
- Use repo-relative paths in public docs.
non_functional_requirements:
- Public README should be understandable to a GitHub reader without prior chat context.
- Public motivation should be written in first person but professional enough for grant/reviewer visibility.
- Public motivation should position `task-plan-v2-dashboard` as the operational dashboard that made the two-day multi-agent/task-plan work trackable without constant manual babysitting.
- Sanitized package should remain technically useful and reproducible.
acceptance_criteria:
- README exists with project overview, motivation, architecture, skill list, safety boundaries, validation status, and usage notes.
- Public motivation text is written from the user's draft without private chat residue.
- README or motivation includes a visible link to `https://github.com/sergekostenchuk/task-plan-v2-dashboard` and a concise explanation of why the dashboard matters for human-in-the-loop agent work.
- Sensitive-data scan returns no unresolved local paths, secrets, private IPs, raw logs, or credentials in public files.
- TASK-PLAN or public projection is sanitized and still explains the work.
- Git remote/target repository is recorded.
- Final diff is reviewed before push.
- GitHub URL is returned after successful push.
acceptance_checks:
- Run path/secret scan over files intended for publication.
- Run JSON/YAML validation for manifests and evals.
- Run production skill linter and cluster linter after sanitation.
- Review README for overclaiming and public clarity.
- Verify `git remote -v` before push.
exit_criteria:
- privacy-review, publication-review, and user-approval passed.
- Commit containing sanitized public package exists.
- Push completed to approved GitHub repository.
- Final GitHub URL is provided to the user.
rollback_plan:
- If sensitive data is found before push, fix/redact and recommit before publishing.
- If wrong remote is configured before push, change remote without pushing.
- If sensitive data is pushed, rotate affected secrets if any, remove from public repo, and coordinate history rewrite only after explicit user approval.
active_alarm_ids:
- none
resolved_alarm_ids:
- A-PUB-001
agent_sequence:
- planner
- docs_sync
- reviewer
- tester
- publisher
required_approvals:
- privacy-review
- publication-review
- user-approval
max_review_loops: 3
escalation_rule: If the repository target or sanitation scope remains unclear after review, keep the task draft and do not push.
tests_required: yes
test_levels:
- static-scan
- lint
- manual-check-needed
test_targets:
- README and public motivation
- task-plan-v2-dashboard mention and link
- sanitized task plan/public docs
- all staged skills and eval files
- git remote target
test_data_origin: local staged skill cluster, user-provided motivation text, and user-provided task-plan-v2-dashboard positioning
oracle: Public package is useful, sanitized, evidence-labeled, and pushed only to the approved GitHub repository.
negative_tests:
- local `<local-user-path>/...` paths remain in public docs
- API key/token/private IP appears in published files
- README claims grant acceptance or unverified ranking/citation outcomes
- push attempted without target repository approval
determinism_notes: Sensitive-data scan patterns must be explicit and committed or recorded in commands_run.
flakiness_risk: GitHub authentication, network, and repository permissions may vary.
stop_on_failure: true
commands_planned:
- `git remote -v`
- `rg -n "<local-user-path>/|<server-var-path>/|<server-opt-path>/|sk-[A-Za-z0-9_-]{20,}|API KEY|password|token|secret|raw IP|82\.25\.|66\.154\.|185\." .`
- `find ./skills -name evals.json -print -exec python3 -m json.tool {} >/dev/null \;`
- `python3 ./plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report ./plans/seo-llm-skill-cluster/cluster-lint-report.json`
- production skill linter over staged skills
- `git diff --check`
- `git status --short`
commands_run:
- `git remote -v`
- `gh repo view sergekostenchuk/seo-llm-skill-cluster --json nameWithOwner,isPrivate,url,defaultBranchRef`
- created a fresh export at temporary publication workspace from tracked files plus `README.md` and `PUBLICATION-SANITATION.md`
- sanitized the export to remove local workstation paths, temp paths, private server paths/IP patterns, email/token/key patterns, and local install targets
- `python3 -m json.tool` over all exported JSON files
- YAML syntax validation over exported YAML files
- `python3 plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . --report plans/seo-llm-skill-cluster/cluster-lint-report.json`
- `python3 plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py . --report plans/seo-llm-skill-cluster/evals/mvp-eval-results.json`
- production skill linter over every exported `skills/*` directory
- final sensitive-data scan over the sanitized export
- `git init && git checkout -b main && git add . && git commit -m "Initial public SEO LLM skill cluster"`
- `gh repo create sergekostenchuk/seo-llm-skill-cluster --public --description "Task-plan driven SEO and LLM-friendly website skill cluster" --source . --remote origin --push`
- `gh repo view sergekostenchuk/seo-llm-skill-cluster --json url,nameWithOwner,isPrivate,defaultBranchRef`
expected_artifacts:
- sanitized public README
- public motivation section
- sanitized task plan or public projection
- publication sanitation report
- GitHub remote/URL
- publication commit
artifact_locations:
- `./README.md`
- `./PUBLICATION-SANITATION.md`
- `./plans/seo-llm-skill-cluster/TASK-PLAN.md`
- `https://github.com/sergekostenchuk/seo-llm-skill-cluster`
- initial public commit `8393a08`
- final public head after T-025 status sync `6a764c2`
code_artifacts:
- public GitHub repository `https://github.com/sergekostenchuk/seo-llm-skill-cluster`
- public initial commit `8393a08`
- public status-sync commit `6a764c2`
test_artifacts:
- JSON validation: pass
- YAML validation: pass
- cluster linter: critical 0, warnings 0, skills checked 13
- MVP eval verifier: pass, issues 0, end-to-end cases 3
- production skill linter over 13 skills: pass
- final sensitive-data scan: pass
review_artifacts:
- privacy-review: pass for sanitized export
- publication-review: pass for public README/motivation/safety boundaries
- user-approval: user requested execution and publication in this turn
decision_log:
- 2026-06-11: Published from a fresh sanitized export instead of pushing local git history because source history contains workstation-specific paths.
- 2026-06-11: Created new public repository `sergekostenchuk/seo-llm-skill-cluster` because no existing repository with that name was found.
summary_format: Repository target, sanitized files, scan results, commit hash, GitHub URL, remaining publication risks.
