# Technical SEO And Schema Audit

task: T-019
target: `https://mlllm.io`

## Regression Validator Results

| Page | Status | Issues | JSON-LD Types | Hreflang |
| --- | --- | --- | --- | --- |
| Homepage | pass | 0 | `CollectionPage`, `Organization`, `Person`, `WebSite` | `en`, `ru`, `x-default` |
| EN short brief | pass | 0 | `BreadcrumbList`, `NewsArticle` | `en`, `ru`, `x-default` |
| EN longform | pass | 0 | `BreadcrumbList`, `TechArticle` | `en`, `ru`, `x-default` |

## Observed Homepage Signals

- title: `mlllm.io - Live AI news and builder lab`
- meta description present;
- one canonical;
- OpenGraph title/description/image present;
- Twitter card present;
- viewport present;
- RSS autodiscovery present.

## Observed EN News Signals

- title present;
- meta description present;
- one self-canonical;
- OpenGraph title/description/image present;
- Twitter card present;
- article published/modified/author meta present;
- `NewsArticle` image is usable.

## Observed EN Longform Signals

- title present;
- meta description present;
- one self-canonical;
- OpenGraph title/description/image present;
- Twitter card present;
- article published/modified/author meta present;
- `TechArticle` schema present.

## Verdict

Observed sample pages pass the current MVP regression validator. This confirms that the staged
validator can detect and report the key SEO/schema layer that previously caused audit disputes.

## Open Checks

- Google Rich Results was not invoked in this E2E.
- Lighthouse/Core Web Vitals were not measured.
- Full sitemap-wide schema audit was not run.
