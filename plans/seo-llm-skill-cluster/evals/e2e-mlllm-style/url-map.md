# URL Map

task: T-019
target: `https://mlllm.io`

## Observed Sample URLs

| Role | URL | Result |
| --- | --- | --- |
| Homepage | `https://mlllm.io/` | SEO regression pass, 0 issues |
| EN short brief | `https://mlllm.io/news/948-langchain-introduces-self-checking-module-for-ai-agents/` | SEO regression pass, 0 issues |
| EN longform | `https://mlllm.io/articles/948-langchain-introduces-rubricmiddleware-module-for-ai-agent-self-correction/` | SEO regression pass, 0 issues |

## Section Model

| Section | Role | Indexing Rule |
| --- | --- | --- |
| `/` | English homepage and entry point | index |
| `/news/` | English short-news index | index |
| `/news/{id}-{slug}/` | one short brief per story | self-canonical, index |
| `/articles/` | English longform index | index |
| `/articles/{id}-{slug}/` | one expanded article per story | self-canonical, index |
| `/ru/` | Russian homepage/entry | index |
| `/ru/news/` | Russian short-news index | index |
| `/ru/articles/` | Russian longform index | index |
| `/topics/` | evergreen topic hubs | index |
| `/projects/` | public project credibility layer | index |
| `/about/` | author/entity page | index |
| `/admin/` | private admin | no public SEO surface |
| `/api/` | private/internal API | no public SEO surface |

## Canonical And Alternate Model

Observed audited pages have:

- exactly one canonical;
- `hreflang` values: `en`, `ru`, `x-default`;
- self-canonical brief and longform pages.

## Sitemap Discovery

Observed:

- `sitemap.xml`: HTTP 200, 1451 URL entries.
- `news-sitemap.xml`: HTTP 200, 999 URL entries.
- `rss.xml`: HTTP 200.

## URL Model Verdict

Observed evidence supports the intended URL architecture. The MVP cluster should preserve this
model and validate it after every builder or pipeline change.
