#!/usr/bin/env python3
"""Deterministic structural linter for the SEO/LLM skill cluster."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_MVP_SKILLS = [
    "site-growth-orchestrator",
    "semantic-core-architect",
    "information-architecture-seo",
    "internal-link-graph-architect",
    "technical-seo-schema-engineer",
    "llm-friendly-site-architect",
    "seo-regression-validator",
    "cluster-consistency-linter",
]

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b", re.I),
    re.compile(r"\bFIXME\b", re.I),
    re.compile(r"\bTBD\b", re.I),
    re.compile(r"\bREPLACE_ME\b", re.I),
    re.compile(r"\bINSERT_[A-Z0-9_]+\b"),
    re.compile(r"\{\{[^}]+\}\}"),
    re.compile(r"<skill-name>", re.I),
    re.compile(r"lorem ipsum", re.I),
]

SECRET_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bghp_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
]


def add_issue(report: dict[str, Any], severity: str, code: str, message: str, path: str | None = None) -> None:
    report["issues"].append(
        {
            "severity": severity,
            "code": code,
            "message": message,
            "path": path,
        }
    )


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_trigger_skill_names(path: Path) -> set[str]:
    if not path.exists():
        return set()
    text = read_text(path)
    return set(re.findall(r"^\s*-\s+name:\s+([a-z0-9-]+)\s*$", text, flags=re.M))


def extract_mvp_skills(scope_path: Path) -> list[str]:
    if not scope_path.exists():
        return DEFAULT_MVP_SKILLS
    text = read_text(scope_path)
    section_match = re.search(r"## Eval Scope for T-016(.*?)(?:\n## |\Z)", text, flags=re.S)
    if not section_match:
        return DEFAULT_MVP_SKILLS
    names = re.findall(r"^- `([a-z0-9-]+)`\s*$", section_match.group(1), flags=re.M)
    return names or DEFAULT_MVP_SKILLS


def parse_frontmatter(skill_md: Path) -> dict[str, str] | None:
    text = read_text(skill_md)
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    frontmatter = text[4:end]
    data: dict[str, str] = {}
    for key in ("name", "description"):
        match = re.search(rf"^{key}:\s*(.+?)\s*$", frontmatter, flags=re.M)
        if match:
            data[key] = match.group(1).strip().strip('"')
    return data


def scan_placeholders(path: Path) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".txt", ".py"}:
        return hits
    text = read_text(path)
    for idx, line in enumerate(text.splitlines(), 1):
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(line):
                hits.append((idx, line.strip()[:180]))
                break
    return hits


def scan_secrets(path: Path) -> list[tuple[int, str]]:
    hits: list[tuple[int, str]] = []
    if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".txt", ".py"}:
        return hits
    text = read_text(path)
    for idx, line in enumerate(text.splitlines(), 1):
        for pattern in SECRET_PATTERNS:
            if pattern.search(line):
                hits.append((idx, pattern.pattern))
                break
    return hits


def placeholder_severity(file_path: Path) -> str:
    parts = set(file_path.parts)
    if file_path.name == "SKILL.md" or "references" in parts or "agents" in parts:
        return "critical"
    if "scripts" in parts or "assets" in parts:
        return "warning"
    return "critical"


def iter_skill_dirs(skills_root: Path, only: set[str]) -> list[Path]:
    if only:
        return [skills_root / name for name in sorted(only)]
    if not skills_root.exists():
        return []
    return sorted([p for p in skills_root.iterdir() if p.is_dir() and not p.name.startswith(".")])


def lint_skill_dir(skill_dir: Path, report: dict[str, Any], trigger_names: set[str], mvp_names: set[str]) -> None:
    skill_name = skill_dir.name
    skill_record: dict[str, Any] = {
        "path": str(skill_dir),
        "exists": skill_dir.exists(),
        "issues": [],
    }
    report["skills"][skill_name] = skill_record

    def skill_issue(severity: str, code: str, message: str, path: str | None = None) -> None:
        item = {
            "severity": severity,
            "code": code,
            "message": message,
            "path": path,
        }
        skill_record["issues"].append(item)
        report["issues"].append(item)

    if not skill_dir.exists():
        skill_issue("critical", "skill_dir_missing", f"Skill directory is missing: {skill_name}", str(skill_dir))
        return

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        skill_issue("critical", "skill_md_missing", "Missing SKILL.md", str(skill_md))
        return

    fm = parse_frontmatter(skill_md)
    if not fm:
        skill_issue("critical", "frontmatter_missing", "SKILL.md must start with YAML frontmatter", str(skill_md))
    else:
        if fm.get("name") != skill_name:
            severity = "critical" if skill_name in mvp_names else "warning"
            skill_issue(severity, "frontmatter_name_mismatch", f"Frontmatter name does not match folder name: {fm.get('name')}", str(skill_md))
        description = fm.get("description", "")
        if len(description) < 80:
            severity = "critical" if skill_name in mvp_names else "warning"
            skill_issue(severity, "description_too_short", "Frontmatter description is too short for reliable triggering", str(skill_md))

    if skill_name not in trigger_names:
        severity = "critical" if skill_name in mvp_names else "warning"
        skill_issue(severity, "trigger_map_missing", "Skill has no trigger-map entry", str(skill_dir))

    if not (skill_dir / "agents" / "openai.yaml").exists():
        skill_issue("warning", "openai_agent_missing", "Missing agents/openai.yaml", str(skill_dir / "agents" / "openai.yaml"))

    text = read_text(skill_md)
    eval_signal = re.search(r"\b(evals?|forward[- ]tests?|negative tests?|benchmarks?)\b", text, flags=re.I)
    if not eval_signal and skill_name in mvp_names:
        skill_issue("critical", "eval_signal_missing", "MVP skill lacks eval or forward-test guidance", str(skill_md))
    elif not eval_signal:
        skill_issue("warning", "eval_signal_missing", "Skill lacks eval or forward-test guidance", str(skill_md))

    validation_signal = re.search(r"\b(lint|validate|test|verification|commands?)\b", text, flags=re.I)
    if not validation_signal and skill_name in mvp_names:
        skill_issue("critical", "validation_signal_missing", "MVP skill lacks validation command/guidance", str(skill_md))
    elif not validation_signal:
        skill_issue("warning", "validation_signal_missing", "Skill lacks validation command/guidance", str(skill_md))

    for file_path in sorted(skill_dir.rglob("*")):
        if not file_path.is_file():
            continue
        for line, snippet in scan_placeholders(file_path):
            skill_issue(placeholder_severity(file_path), "placeholder_found", f"Unresolved placeholder at line {line}: {snippet}", str(file_path))
        for line, pattern in scan_secrets(file_path):
            skill_issue("critical", "possible_secret_found", f"Possible secret pattern at line {line}: {pattern}", str(file_path))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Lint the SEO/LLM skill cluster structure.")
    parser.add_argument("cluster_root", help="Cluster workspace root, usually .")
    parser.add_argument("--skills-root", help="Skill directories root. Defaults to CLUSTER_ROOT/skills.")
    parser.add_argument("--trigger-map", help="Trigger map path. Defaults to plan trigger-map.yaml.")
    parser.add_argument("--mvp-scope", help="MVP scope path. Defaults to plan mvp-release-scope.md.")
    parser.add_argument("--artifact-contract", help="Artifact contract path. Defaults to plan assets/artifact-schemas.md.")
    parser.add_argument("--report", help="Write JSON report to this path.")
    parser.add_argument("--only", action="append", default=[], help="Only lint this skill directory name. Can be repeated.")
    parser.add_argument("--no-mvp-required", action="store_true", help="Do not require MVP trigger coverage. Useful for fixtures.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    cluster_root = Path(args.cluster_root).resolve()
    plan_root = cluster_root / "plans" / "seo-llm-skill-cluster"
    skills_root = Path(args.skills_root).resolve() if args.skills_root else cluster_root / "skills"
    trigger_map = Path(args.trigger_map).resolve() if args.trigger_map else plan_root / "trigger-map.yaml"
    mvp_scope = Path(args.mvp_scope).resolve() if args.mvp_scope else plan_root / "mvp-release-scope.md"
    artifact_contract = Path(args.artifact_contract).resolve() if args.artifact_contract else plan_root / "assets" / "artifact-schemas.md"
    only = set(args.only or [])

    report: dict[str, Any] = {
        "artifact_type": "cluster_lint_report",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "cluster_root": str(cluster_root),
        "skills_root": str(skills_root),
        "trigger_map": str(trigger_map),
        "mvp_scope": str(mvp_scope),
        "artifact_contract": str(artifact_contract),
        "status": "pass",
        "issues": [],
        "skills": {},
        "summary": {},
    }

    trigger_names = extract_trigger_skill_names(trigger_map)
    if not trigger_map.exists():
        add_issue(report, "critical", "trigger_map_missing", "Trigger map file is missing", str(trigger_map))

    if not artifact_contract.exists():
        add_issue(report, "critical", "artifact_contract_missing", "Artifact schema contract is missing", str(artifact_contract))

    mvp_names = set(extract_mvp_skills(mvp_scope))
    if not args.no_mvp_required:
        for name in sorted(mvp_names):
            if name not in trigger_names:
                add_issue(report, "critical", "mvp_trigger_missing", f"MVP skill has no trigger-map entry: {name}", str(trigger_map))

    skill_dirs = iter_skill_dirs(skills_root, only)
    if not skills_root.exists() and not only:
        add_issue(report, "warning", "skills_root_missing", "No staged skills root exists yet; run again after skill creation", str(skills_root))
    elif not skill_dirs and not only:
        add_issue(report, "warning", "no_skill_dirs", "No skill directories found under skills root", str(skills_root))

    for skill_dir in skill_dirs:
        lint_skill_dir(skill_dir, report, trigger_names, mvp_names)

    critical_count = sum(1 for item in report["issues"] if item["severity"] == "critical")
    warning_count = sum(1 for item in report["issues"] if item["severity"] == "warning")
    report["status"] = "fail" if critical_count else "pass"
    report["summary"] = {
        "critical": critical_count,
        "warnings": warning_count,
        "skills_checked": len(skill_dirs),
        "mvp_skills_expected": sorted(mvp_names),
        "trigger_map_entries": sorted(trigger_names),
    }

    if args.report:
        report_path = Path(args.report).resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    if report["status"] == "fail":
        for issue in report["issues"]:
            if issue["severity"] == "critical":
                print(f"CRITICAL {issue['code']}: {issue['message']} ({issue.get('path')})", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
