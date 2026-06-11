# LLM-Friendly Audit

task: T-019
target: `https://mlllm.io`

## Observed Discovery Surfaces

| Surface | Result |
| --- | --- |
| `robots.txt` | HTTP 200, 912 bytes |
| `llms.txt` | HTTP 200, 2755 bytes |
| `sitemap.xml` | HTTP 200, 1451 entries |
| `news-sitemap.xml` | HTTP 200, 999 entries |
| `rss.xml` | HTTP 200 |
| static HTML content | regression validator reads titles, metadata, schema, and links without JS rendering |

## Strong Signals

- Public LLM-oriented discovery file exists.
- Static HTML is parseable without browser rendering.
- EN/RU alternates are visible in page metadata.
- JSON-LD exposes page type and authorship on audited samples.
- Brief and longform pages remain separate surfaces and can be connected without duplicate-body pages.

## LLM-Friendly But Not Yet Complete

- LLM citation monitoring is not in the MVP cluster yet.
- No assistant query panel, prompt set, or citation runbook was executed.
- Markdown alternates were not checked.
- HTTP cache headers such as `Last-Modified` and `ETag` were not measured.

## Policy

Do not add hidden text for LLMs. LLM-friendly content must be visible or be a declared alternate
format such as `llms.txt`, RSS, sitemap, or noindex markdown where the target site intentionally
supports it.
