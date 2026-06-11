# E2E Improvement Backlog

task: T-019
target: `https://mlllm.io`

## P0

No P0 issues were found in the audited MVP surfaces.

## P1

| Item | Owner Layer | Rationale |
| --- | --- | --- |
| Add sitemap-wide SEO/schema regression mode | `seo-regression-validator` | Current E2E checked representative pages, not all 1451 sitemap URLs. |
| Add browser/visual smoke for representative pages | future UX validator | Metadata passes do not prove first viewport quality or media layout. |
| Add credential-free crawler access report template | monitoring layer | E2E checked public files but not real bot log access. |
| Add LLM citation monitor after MVP release | `llm-citation-monitor` | LLM visibility claims need prompt sets, timestamps, and assistant-specific results. |

## P2

| Item | Owner Layer | Rationale |
| --- | --- | --- |
| Add optional Markdown alternate policy | LLM-friendly layer | Useful for agents if noindex and canonical rules are clear. |
| Add external-authority placement workflow | authority layer | Still gated by white-hat policy and user approval. |
| Add Search Console import workflow | monitoring layer | Requires credentials and privacy handling. |

## Not A Regression

- No external posting was performed.
- No ranking or citation claim was made.
- No production website files were changed.
