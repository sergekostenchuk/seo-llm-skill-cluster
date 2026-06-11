# White-Hat Authority Placement Policy

date: 2026-06-11
task: T-014
status: policy ready; external actions still gated

## Purpose

This policy defines how the skill cluster may evaluate external link and authority opportunities
without drifting into spam, fake authority, or platform-rule violations.

## Allowed Opportunity Types

Allowed only as dry-run recommendations until user approves an external action:

- own profiles and bios where the user controls the account;
- GitHub repository README/profile links for relevant owned projects;
- documentation pages for owned tools or integrations;
- legitimate community posts where the link answers a real question and the platform allows it;
- relevant awesome lists or resource indexes where submission rules allow it;
- product/project launch pages where the target is genuinely relevant;
- guest posts or interviews with editorial review and transparent authorship;
- citations from partner/project docs where there is a real integration or dependency;
- public case studies or project pages connected to actual work.

## Forbidden Opportunity Types

Never recommend:

- PBNs;
- link farms;
- bought links without disclosure;
- fake reviews;
- fake accounts;
- automated forum/comment posting;
- irrelevant directory submissions;
- hidden links;
- cloaked links;
- doorway pages;
- mass profile creation;
- low-quality AI-generated guest posts;
- link exchanges with no editorial relevance;
- pretending to be a user or customer.

## Platform Rule Checklist

Before any external action, the scout must record:

- platform URL;
- official submission/posting rules checked;
- account ownership/authorization;
- whether links are allowed;
- whether promotional links need disclosure;
- whether `nofollow`, `ugc`, or `sponsored` is expected;
- whether the platform forbids automation;
- whether human review is required;
- timestamp and source for the rule check.

Platform-specific rules are unstable. Re-check official rules before each action.

## Opportunity Scoring

Score each opportunity from 0 to 3:

| Dimension | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Relevance | unrelated | broad category | relevant topic | exact audience/problem fit |
| Editorial legitimacy | no review/spam | weak review | clear moderation | strong editorial process |
| User value | no value | thin context | useful context | directly solves user need |
| Risk | high | medium | low | very low |
| Permission clarity | unknown | ambiguous | likely allowed | explicitly allowed |
| Target fit | wrong page | generic homepage | relevant section | exact page/project/article |

Minimum recommendation threshold:

- total score 12+;
- no high-risk dimension;
- explicit platform-rule status;
- user approval before action.

## Approval Gates

No external action may happen until all are true:

1. Opportunity record exists.
2. Platform rules were checked.
3. Target page and anchor are specified.
4. Risk is low or explicitly accepted by user.
5. User approves the specific action.
6. Draft text is reviewed for honesty and usefulness.

## UTM And Monitoring Policy

Use tracking only when it is appropriate and does not make the link ugly or suspicious:

- owned profiles/docs: UTM optional;
- community answers: avoid UTM unless platform norms allow it;
- editorial guest posts: prefer clean canonical URLs unless campaign tracking is agreed;
- project docs: use stable project URLs;
- never use misleading redirects.

Monitoring should record:

- placement URL;
- target URL;
- link attributes (`follow`, `nofollow`, `ugc`, `sponsored`);
- date placed;
- approval reference;
- expected review date.

## Output Rule

The scout produces an opportunity register and optional draft. It must not post, submit, comment,
open PRs, DM, email, or edit external platforms without explicit user approval.
