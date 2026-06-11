# Freshness And Primary-Source Policy

plan_id: PLAN-SEO-LLM-SKILL-CLUSTER
task_id: T-023
date: 2026-06-11
status: complete

## Purpose

SEO, schema.org, crawler identities, AI-search behavior, platform rules, and ranking/citation surfaces change. Skills in this cluster must verify unstable facts from primary or high-authority sources before making current claims or implementation recommendations.

## Source Tiers

| Tier | Use | Examples |
|---|---|---|
| Tier 1 primary | Required for implementation-affecting current facts. | Google Search Central, schema.org, OpenAI crawler docs, Anthropic crawler docs, Perplexity crawler docs, official platform docs, official API docs. |
| Tier 2 high-signal | Allowed for context or incident awareness, not as sole implementation authority. | Cloudflare reports, official vendor blogs, Search Engine Journal/Search Engine Roundtable when they link to primary docs. |
| Tier 3 community/media | Use only as leads or caveats. | Reddit, HN, forums, non-official bot directories, SEO blogs without primary links. |

## Current Primary Sources To Prefer

These URLs are allowed as starting points, but the skill must still verify they are reachable/current when the task depends on them:

- Google robots.txt: https://developers.google.com/search/docs/crawling-indexing/robots/intro
- Google structured data: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Google Search Central documentation: https://developers.google.com/search/docs
- schema.org vocabulary: https://schema.org/
- OpenAI crawlers and user agents: https://developers.openai.com/api/docs/bots
- Anthropic crawler behavior: https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Anthropic outbound IP addresses for tool/web-fetch contexts: https://docs.anthropic.com/en/api/ip-addresses
- Perplexity crawlers: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- W3C Web Content Accessibility Guidelines: https://www.w3.org/WAI/standards-guidelines/wcag/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Top 10: https://owasp.org/www-project-top-ten/

## Unstable Fact Categories

| Category | Freshness rule | Mandatory evidence |
|---|---|---|
| Search engine crawling/indexing rules | Verify when changing `robots.txt`, sitemap, canonical/noindex, hreflang, or structured-data rules. | Primary source URL, access date, changed file/route. |
| AI crawler names and behavior | Verify before adding/removing bot user agents or making visibility/training claims. | Official crawler docs; server logs can support but not replace docs. |
| Schema.org / JSON-LD requirements | Verify before adding new schema types or rich-result claims. | schema.org plus Google Search Central where Google eligibility matters. |
| Search Console / Bing/Yandex behavior | Verify before interpreting impressions, indexing, manual actions, or crawl errors. | Official docs plus exported report timestamp. |
| Assistant citation behavior | Treat every result as prompt/time/locale-specific. | Assistant name, mode, query, locale, timestamp, cited URL, screenshot/export path when available. |
| Rank/SERP positions | Verify per query, locale, device, personalization state, date, and tool. | Tool/source, query, locale, timestamp, result URL. |
| Platform link-placement rules | Verify before recommending posts, PRs, directories, comments, profiles, or outreach. | Platform docs/rules/contribution guide with URL and date. |
| Security and bot allowlisting | Verify before allowlisting IPs, relaxing WAF/rate limits, or changing admin/API exposure. | Official IP docs, local config evidence, security review. |
| Product/model/API capabilities/pricing | Verify before mentioning latest models, APIs, costs, limits, or product names. | Official vendor docs or pricing page with date. |

## Browse/Verify Required Triggers

A skill must browse or verify primary sources when the user asks or the task implies:

- "latest", "current", "today", "now", "new", "most recent", "as of";
- editing `robots.txt`, crawler allow/block rules, sitemap, canonical/noindex, or hreflang;
- adding or changing schema.org/JSON-LD for rich results;
- claims about Google, Bing, Yandex, ChatGPT, Claude, Perplexity, Gemini, Copilot, or AI Overviews visibility;
- claims about a crawler respecting or ignoring `robots.txt`;
- platform placement, backlink, directory, forum, or community posting rules;
- security, WAF, allowlisting, IP ranges, bot classification, or rate-limit changes;
- model/API names, prices, limits, or provider capabilities;
- legal/compliance, privacy, or policy-sensitive claims.

## No-Network Fallback

If browsing or live verification is unavailable:

1. Mark the fact as `unknown_current_status`.
2. Use only stable architectural guidance.
3. Do not give implementation-final crawler/platform/model claims.
4. Add a `verification_required` item to the output.
5. Do not mark the task `done` when the missing current fact is a release blocker.

## Evidence Labels

Every report must separate:

- `observed`: directly fetched, rendered, logged, tested, or read from a cited source.
- `inferred`: reasoned from observed facts.
- `unknown`: not verified.
- `stale`: based on an old source or prior memory and not safe for current implementation.

## Report Format For Current Facts

```yaml
current_fact:
  claim: "OpenAI crawler policy was checked before editing robots.txt"
  status: observed|inferred|unknown|stale
  source_url: "https://developers.openai.com/api/docs/bots"
  checked_at: "2026-06-11T00:00:00Z"
  method: "browser|curl|web-search|official-doc|manual"
  implementation_impact: "robots.txt policy"
  caveat: "Crawler behavior can change; re-check before deploy"
```

## Skill-Specific Requirements

### `site-growth-orchestrator`

- Must stop or route to a freshness check when a subtask depends on current external facts.
- Must not summarize old conversation findings as current facts without verification.

### `seo-llm-site-architect`

- Must verify current primary docs before crawler policy, rich-result/schema eligibility, indexation, or `hreflang` changes.
- Must distinguish `robots.txt` crawling control from indexing control.

### `llm-friendly-site-optimizer`

- Must treat `llms.txt` as an emerging convention, not a guaranteed ranking/citation standard.
- Must verify AI crawler/user-agent guidance before making bot-specific recommendations.

### `seo-regression-validator`

- Must timestamp every live check.
- Must report skipped checks separately from passed checks.
- Must not turn one assistant/search result into a general visibility claim.

### `external-authority-placement-scout`

- Must verify platform-specific rules before suggesting any placement.
- Must default to draft/review mode; no external posting without explicit approval.

### `web-security-architect`

- Must verify security standards and vendor IP ranges before current hardening/allowlist recommendations.
- Must protect secrets and private logs; raw IP data should be summarized or redacted unless the user explicitly asks for local analysis.

## Stale-Data Handling

If a source is older than the cadence below, re-check before using it for implementation:

| Surface | Cadence |
|---|---|
| AI crawler names/behavior | before every implementation task |
| Google/Search Central implementation rules | before every implementation task |
| schema.org vocabulary/rich-result rules | before every implementation task |
| Platform posting/contribution rules | before every recommendation batch |
| Search Console/rank/citation reports | every report run |
| Security standards and IP ranges | before every production change |
| General UX heuristics | quarterly or when platform-specific |

## Privacy Rules

- Do not store credentials, API keys, cookies, tokens, private Search Console rows, private analytics exports, or raw IP logs in skill files.
- Use aggregate bot categories or redacted samples for public artifacts.
- Store full private evidence only in explicitly approved private local paths.

## T-023 Review Result

- Primary-source categories and browse-required triggers are defined.
- Current crawler/bot docs must be verified again before production edits.
- A-MON-001 remains active for credentialed monitoring because Search Console, rank tools, and assistant surfaces are not confirmed.
