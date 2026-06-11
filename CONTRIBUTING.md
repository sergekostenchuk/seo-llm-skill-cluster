# Contributing

Contributions are welcome when they improve the cluster without weakening its safety boundaries.

## What Fits

Good contributions usually add or improve:

- narrowly scoped Codex skills;
- validation scripts;
- example artifacts;
- schema, metadata, crawlability, or LLM-readable website checks;
- task-plan governance patterns;
- documentation that makes the cluster easier to run and verify.

## What Does Not Fit

Do not contribute:

- black-hat SEO tactics;
- PBN, link farm, comment spam, fake review, or doorway-page workflows;
- hidden bot-only content patterns;
- automated external posting without explicit user approval;
- fake rankings, fake citations, or unverifiable audit claims;
- examples containing real secrets, private logs, private analytics rows, or private infrastructure details.

## Validation Before A Pull Request

Run:

```bash
python3 plans/seo-llm-skill-cluster/scripts/lint_skill_cluster.py . \
  --report .reports/seo-llm-cluster-lint.json

python3 plans/seo-llm-skill-cluster/scripts/verify_mvp_evals.py . \
  --report .reports/seo-llm-mvp-evals.json

for f in skills/*/evals.json; do
  python3 -m json.tool "$f" >/dev/null
done
```

Also check that public files do not contain local paths, secrets, raw private logs, private IPs, account emails, or private server details.

## Evidence Rules

Reports should label evidence as:

- `Observed`: directly checked fact;
- `Inferred`: conclusion drawn from observed facts;
- `Open`: not verified yet.

Do not present model output as external proof unless it is clearly labeled as model-assisted analysis.
