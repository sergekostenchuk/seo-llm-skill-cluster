# E2E Goal Brief

task: T-019
target: `https://mlllm.io`
mode: read-only dry-run
date: 2026-06-11

## Objective

Validate that the staged MVP SEO/LLM skill cluster can reason end-to-end about an
mlllm.io-style website without changing production systems.

## Protected Content Model

- One short news brief per story.
- One expanded longform article per story.
- Homepage and topic pages may summarize and route traffic, but must not create a third
  duplicate article body.
- Brief and longform pages remain independent user-facing surfaces with self-canonical URLs.

## Scope In

- public homepage signals;
- one EN short-news page;
- one EN longform page;
- robots, llms.txt, sitemap, news sitemap, RSS availability;
- semantic core, URL map, internal link graph, schema/LLM audit, and improvement backlog.

## Scope Out

- production deploy;
- code edits to `mlllm.io`;
- Telegram or TG-NEWS changes;
- credentialed analytics;
- Search Console;
- external link placement;
- rank or citation claims.

## Evidence Standard

Facts in this E2E are labeled as:

- `Observed`: directly fetched or produced by a deterministic script.
- `Inferred`: architecture conclusion from observed facts.
- `Open`: not measured in this dry-run.
