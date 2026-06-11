# Authority Policy Review

task: T-014
date: 2026-06-11
status: pass

## Negative Case Review

| Scenario | Decision | Reason |
| --- | --- | --- |
| Automated forum posting | block | External action, likely spam, no user approval, platform-rule risk. |
| Irrelevant directory submission | block | No relevance or user value; reputational risk. |
| PBN/link farm recommendation | block | Explicitly forbidden. |
| Fake reviews | block | Misleading and reputationally harmful. |
| Bought link without disclosure | block | Requires disclosure; otherwise forbidden. |
| Mass profile creation | block | Spam pattern and weak authority. |
| Owned GitHub profile link | allow as candidate | Owned account and relevant if honest; still user approval required for edit. |
| Relevant awesome-list PR | allow as candidate | Only if list rules allow it and project is genuinely relevant. |
| Helpful community answer | allow as candidate | Only if the answer solves a real user problem and platform rules allow links. |

## Required Next Gate Before T-015

T-015 may build dry-run scout/validator skills, but external actions remain blocked by `A-EXT-001`.

Before any real placement:

1. User approves exact platform and action.
2. Platform rules are checked from current official/public source.
3. Draft is reviewed for usefulness and honesty.
4. Register record is created.
5. Rollback/removal path is known where applicable.

## Verdict

The policy blocks black-hat and grey-hat patterns and is safe to use as the foundation for dry-run
opportunity scouting. It does not authorize posting, outreach, submissions, PRs, or account edits.
