# Semantic Core

task: T-019
target: `https://mlllm.io`

## Core Positioning

Observed homepage title and description position the site as:

- live AI news;
- builder-focused explainers;
- English translations with Russian source editions;
- project and workflow context behind the publication system.

## Primary Audience Segments

| Segment | Need | Matching Site Surface |
| --- | --- | --- |
| AI builders | track useful AI infrastructure changes quickly | `/news/`, `/articles/`, `/topics/` |
| Technical readers | understand what changed and why it matters | longform explainers |
| LLM/search agents | retrieve clean facts and page relationships | `llms.txt`, sitemap, schema, static HTML |
| Collaborators/reviewers | inspect author's projects and credibility | `/projects/`, `/about/`, source trails |
| Russian readers | access source-language editions | `/ru/news/`, `/ru/articles/`, `/ru/blog/` |

## Entity Clusters

| Cluster | Entities |
| --- | --- |
| Publication system | mlllm.io, TG-NEWS, AI channel, source trail, longform article |
| AI tooling | LangChain, Deep Agents SDK, LLM-as-a-judge, agents, workflow automation |
| Author and projects | Sergey Kostenchuk, mlllm.io, TG-NEWS, task-plan systems, skill clusters |
| Discovery files | robots.txt, llms.txt, sitemap.xml, news-sitemap.xml, RSS |

## Intent Map

| Intent | Query Shape | Target Surface |
| --- | --- | --- |
| Fresh AI news | "latest AI agent news", "AI infrastructure updates" | `/news/` |
| Explanation | "what is RubricMiddleware", "why LLM-as-a-judge matters" | `/articles/.../` |
| Source verification | "source trail", "where did this news come from" | news/article detail page |
| Site/system understanding | "how mlllm.io works", "AI news pipeline" | `/topics/`, `/projects/` |
| Author trust | "who is Sergey Kostenchuk" | `/about/`, `/projects/` |

## Gaps

- Content quality scoring is not measured in this E2E.
- Query volume and Search Console impressions are open because no credentials were used.
- LLM citation visibility is open because the citation-monitor skill is not part of MVP.
