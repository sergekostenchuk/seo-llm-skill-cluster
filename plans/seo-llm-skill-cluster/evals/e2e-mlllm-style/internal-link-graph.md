# Internal Link Graph

task: T-019
target: `https://mlllm.io`

## Intended Graph

```mermaid
flowchart TD
  Home["/ homepage"] --> NewsIndex["/news/"]
  Home --> ArticlesIndex["/articles/"]
  Home --> Topics["/topics/"]
  Home --> Projects["/projects/"]
  Home --> About["/about/"]
  NewsIndex --> Brief["/news/{id}-{slug}/"]
  ArticlesIndex --> Longform["/articles/{id}-{slug}/"]
  Brief <--> Longform
  Brief <--> RuBrief["/ru/news/{id}-{slug}/"]
  Longform <--> RuLongform["/ru/articles/{id}-{slug}/"]
  Brief --> Sources["Source trail"]
  Longform --> Sources
  Topics --> Brief
  Topics --> Longform
  Projects --> Topics
  About --> Projects
```

## Link Rules

- Homepage cards may link to brief, longform, and language alternates.
- Brief pages should link to the matching longform as the deeper read.
- Longform pages should link back to the matching brief as the short summary.
- EN/RU alternates should be visible and also represented in `hreflang`.
- Topic pages should route to collections and examples, not duplicate the full article body.
- Project pages should explain why a project matters and link to related topics or posts.

## Observed From Regression Reports

- Audited homepage exposes `CollectionPage`, `Organization`, `Person`, and `WebSite` schema.
- Audited EN brief exposes `NewsArticle` and `BreadcrumbList`.
- Audited EN longform exposes `TechArticle` and `BreadcrumbList`.
- Audited pages include `en`, `ru`, and `x-default` hreflang values.

## Open Checks

- Full crawl orphan detection across all 1451 sitemap URLs was not run in this E2E.
- Browser visual link verification was not run in this E2E.
- Anchor text distribution was not measured.
