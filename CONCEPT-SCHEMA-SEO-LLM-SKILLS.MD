Да, понимаю. Ты хочешь не один “SEO skill”, а **систему skills**, где есть центральный архитектор-оркестратор, отдельные эксперты, валидаторы, тестировщики и feedback loop по реальным данным из поиска, LLM-ответов, логов и аналитики.

Я бы строил так.

**1. Центральный Skill**
`site-growth-orchestrator`

Его роль:

- принимает цель сайта;
- вызывает нужные skills в правильной последовательности;
- не делает всё сам;
- ведет общий `TASK-PLAN`;
- собирает артефакты: semantic core, URL map, internal link graph, schema report, UX journey map, crawler audit, LLM citation report;
- решает, что готово к deploy, а что требует доработки.

**2. SEO / LLM Cluster**
Нужные skills:

- `semantic-core-architect`
  Строит семантическое ядро: queries, intents, entities, clusters, languages, priority.

- `information-architecture-seo`
  Делает структуру сайта: разделы, URL, canonical, hreflang, pillar pages, topic pages, news/article модель.

- `internal-link-graph-architect`
  Проектирует перелинковку: brief ↔ longform, topic → articles, project → articles, author → projects, breadcrumbs.

- `technical-seo-schema-engineer`
  Проверяет title/meta, schema.org, JSON-LD, sitemap, news-sitemap, RSS, robots.txt, llms.txt, OpenGraph.

- `llm-friendly-site-architect`
  Делает сайт понятным для ChatGPT, Perplexity, Claude, Gemini: llms.txt, answer blocks, source trails, entity pages, markdown alternates.

- `seo-regression-validator`
  Проверяет live-сайт, а не “по ощущениям”: schema, canonical, hreflang, OG, sitemap, robots, Rich Results, Lighthouse.

**3. Content / Editorial Cluster**
Это ты почти не назвал, но он критически нужен.

- `content-strategy-architect`
  Решает, какие темы публиковать, где news, где longform, где blog, где project page.

- `editorial-quality-gate`
  Проверяет: нет ли SEO-филлера, повторов, слабых claims, отсутствующих источников.

- `translation-localization-seo`
  Отвечает за EN/RU/FR/ES/DE/ZH/KO/JA: не дословный мусор, а локализованный intent.

- `content-decay-monitor`
  Ищет стареющие страницы, которые надо обновить, объединить или усилить.

**4. UX / UI Cluster**
Связь с SEO обязательна, потому что плохой UX убивает поведение пользователя.

- `ux-journey-architect`
  Строит пути: новый читатель, returning reader, агент, потенциальный партнер, GitHub reviewer.

- `conversion-retention-architect`
  Telegram/RSS/email/community/follow paths.

- `ui-layout-validator`
  Проверяет mobile/desktop, карточки, media, first viewport, CLS, accessibility.

- `onboarding-architect`
  Start here, About, Projects, “why trust this site”.

**5. Authority / Link Placement Cluster**
Будущий skill надо делать аккуратно, не как спам-бот.

Я бы назвал:
`external-authority-placement-scout`

Роль:

- ищет площадки, где ссылка реально полезна;
- проверяет topical relevance, indexability, nofollow/sponsored, правила площадки, качество домена;
- предлагает формат размещения: GitHub README, awesome-list PR, guest post, directory, community post, package registry, Hugging Face, Product Hunt, Indie Hackers, Dev.to, Medium, Reddit/HN только если уместно;
- готовит outreach/post/PR;
- размещает только там, где есть разрешение или твой аккаунт.

Отдельно:
`backlink-quality-validator`

Проверяет, что размещение не токсичное:

- не link farm;
- не PBN;
- не автоматический спам;
- есть тематическая связь;
- страница индексируется;
- ссылка ведет на правильную canonical page;
- есть UTM/monitoring.

**6. Monitoring / Reality Layer**
Это тоже нужно добавить.

- `search-console-analyst`
  Google Search Console, Bing/Yandex Webmaster: impressions, clicks, queries, indexing, crawl errors.

- `llm-citation-monitor`
  Проверяет, цитируют ли сайт ChatGPT/Perplexity/Claude/Gemini по целевым вопросам.

- `server-log-crawler-analyst`
  Реальная картина: кто ходит, какие боты, какие статусы, что блокируется.

- `rank-serp-monitor`
  Позиции, SERP features, конкуренты, snippets.

**7. Общий порядок работы**

1. Goal brief.
2. Semantic core.
3. Entity/topic map.
4. Site architecture.
5. UX journeys.
6. Content model.
7. Internal link graph.
8. Technical SEO/schema.
9. LLM-friendly layer.
10. Publish/deploy.
11. Live validation.
12. Search/LLM monitoring.
13. Backlink/placement campaign.
14. Feedback loop в task-plan.

**Что важно не упустить**

- единый формат артефактов между skills;
- версия каждого аудита;
- evidence-first: не “кажется”, а URL, HTML, скрин, лог, Search Console, Rich Results;
- запрет hidden SEO content;
- запрет плодить дубли;
- отдельный rollback plan;
- отдельный privacy/security gate для аналитики и логов;
- accessibility;
- Core Web Vitals;
- schema должна совпадать с видимым контентом;
- link placement только white-hat.

Оптимальная архитектура: **один orchestrator + 6 кластеров skills**: SEO/LLM, Content, Technical, UX/UI, Authority/Links, Monitoring/Validation. Тогда система будет не просто “делать SEO”, а постоянно строить, проверять, публиковать, измерять и улучшать сайт по реальным сигналам.
