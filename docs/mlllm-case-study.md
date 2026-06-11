# mlllm.io Case Study

This case study explains why the SEO/LLM skill cluster exists and what kind of output it is expected to produce.

## Context

[mlllm.io](https://mlllm.io) is a public AI news and builder-lab site by Sergey Kostenchuk. It combines:

- short AI news briefs;
- expanded source-backed articles;
- project pages;
- author pages;
- multilingual publishing structure;
- public discovery files such as `robots.txt`, `sitemap.xml`, `news-sitemap.xml`, RSS, and `llms.txt`.

The site became a practical test bed while preparing a public profile for an OpenAI open-source grant application. The work exposed a recurring pattern: classic SEO checks, LLM-readable architecture, UX paths, metadata, crawler access, and task-plan governance should not live in one large prompt. They need a coordinated skill cluster.

## Audit Snapshot

![mlllm.io model-assisted audit snapshot](../assets/mlllm-audit-report-2026-06-11.png)

This screenshot is included as a public case-study snapshot. It is a model-assisted audit result, not a formal third-party certification. The value is in the underlying workflow:

- crawlable static HTML;
- explicit `robots.txt` and `llms.txt`;
- structured sitemap and news sitemap;
- canonical and hreflang model;
- visible source trails;
- schema.org JSON-LD;
- short-brief to longform linking;
- project and author context;
- validation reports and task-plan history.

## Protected Content Model

The site model is intentionally narrow:

- one short news brief per story;
- one expanded longform article per story;
- homepage and topic pages can summarize and link, but should not create duplicate article bodies.

SEO and LLM-friendly additions should strengthen this model with metadata, structured data, source trails, and internal links. They should not multiply near-duplicate pages.

## Skill Cluster Run

The example run produced:

- a goal brief;
- routing and handoff notes;
- semantic core;
- URL map;
- internal link graph;
- technical SEO and schema audit;
- LLM-friendly audit;
- improvement backlog;
- static SEO regression reports.

See [examples/mlllm-case-study](../examples/mlllm-case-study/) for the artifact examples.

## What This Proves

The case study shows that the cluster can turn a real website goal into a structured sequence of auditable artifacts.

It does not claim:

- guaranteed search ranking;
- guaranteed LLM citation;
- full sitemap-wide crawl coverage;
- Search Console evidence without access;
- Lighthouse/Core Web Vitals evidence unless those checks are explicitly run.

That distinction matters. The cluster is designed to separate observed facts, inferred conclusions, and open questions.
