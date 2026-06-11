#!/usr/bin/env python3
"""Verify MVP skill eval coverage."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_MVP = [
    "site-growth-orchestrator",
    "semantic-core-architect",
    "information-architecture-seo",
    "internal-link-graph-architect",
    "technical-seo-schema-engineer",
    "llm-friendly-site-architect",
    "seo-regression-validator",
    "cluster-consistency-linter",
]


def extract_mvp(scope_path: Path) -> list[str]:
    if not scope_path.exists():
        return DEFAULT_MVP
    text = scope_path.read_text(encoding="utf-8")
    section = re.search(r"## Eval Scope for T-016(.*?)(?:\n## |\Z)", text, re.S)
    if not section:
        return DEFAULT_MVP
    names = re.findall(r"^- `([a-z0-9-]+)`\s*$", section.group(1), re.M)
    return names or DEFAULT_MVP


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def count_cases(data: dict[str, Any]) -> tuple[int, int]:
    return len(data.get("positive_cases", [])), len(data.get("negative_cases", []))


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify MVP eval coverage.")
    parser.add_argument("cluster_root")
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    root = Path(args.cluster_root).resolve()
    plan_root = root / "plans" / "seo-llm-skill-cluster"
    scope = plan_root / "mvp-release-scope.md"
    suite_path = plan_root / "evals" / "mvp-skill-cluster-evals.json"
    suite = load_json(suite_path)
    mvp = extract_mvp(scope)
    per_skill_extra = suite.get("per_skill_cases", {})

    report: dict[str, Any] = {
        "artifact_type": "mvp_eval_results",
        "generated_at": os.environ.get("MVP_EVAL_TIMESTAMP") or datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "status": "pass",
        "mvp_skills": mvp,
        "skills": {},
        "end_to_end_cases": len(suite.get("end_to_end_cases", [])),
        "issues": [],
    }

    for skill in mvp:
        skill_eval = root / "skills" / skill / "evals.json"
        positive = 0
        negative = 0
        sources: list[str] = []
        if skill_eval.exists():
            p, n = count_cases(load_json(skill_eval))
            positive += p
            negative += n
            sources.append(str(skill_eval))
        if skill in per_skill_extra:
            p, n = count_cases(per_skill_extra[skill])
            positive += p
            negative += n
            sources.append(str(suite_path))
        record = {
            "positive_cases": positive,
            "negative_cases": negative,
            "sources": sources,
            "passed": positive >= 3 and negative >= 3,
        }
        report["skills"][skill] = record
        if not record["passed"]:
            report["issues"].append(
                {
                    "severity": "critical",
                    "code": "eval_coverage_missing",
                    "message": f"{skill} has {positive} positive and {negative} negative cases",
                }
            )

    if report["end_to_end_cases"] < 3:
        report["issues"].append(
            {
                "severity": "critical",
                "code": "e2e_coverage_missing",
                "message": "MVP suite needs at least 3 end-to-end cases",
            }
        )

    if report["issues"]:
        report["status"] = "fail"

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "issues": report["issues"], "end_to_end_cases": report["end_to_end_cases"]}, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
