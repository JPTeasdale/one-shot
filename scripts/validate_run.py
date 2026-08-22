#!/usr/bin/env python3
"""Validate One Shot phase contracts and final handoff evidence."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


PHASE_ORDER = ("phase-1", "phase-2", "phase-3", "phase-4", "final")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
PLACEHOLDER_PATTERNS = (
    re.compile(r"(?im)^\s*(?:[-*]\s*)?(?:TODO|TBD)(?:\s|:|$)"),
    re.compile(r"(?i)lorem ipsum"),
    re.compile(r"(?i)\[(?:insert|placeholder)[^\]]*\]"),
)


@dataclass
class Report:
    run_root: Path
    through: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checked: list[str] = field(default_factory=list)

    def require_file(self, relative: str, minimum_bytes: int = 80) -> Path | None:
        path = self.run_root / relative
        self.checked.append(relative)
        if not path.is_file():
            self.errors.append(f"Missing required file: {relative}")
            return None
        if path.stat().st_size < minimum_bytes:
            self.errors.append(f"Required file is not substantive ({path.stat().st_size} bytes): {relative}")
        return path

    def require_dir_content(self, relative: str, pattern: str = "*") -> list[Path]:
        directory = self.run_root / relative
        self.checked.append(relative + "/")
        if not directory.is_dir():
            self.errors.append(f"Missing required directory: {relative}")
            return []
        matches = sorted(path for path in directory.glob(pattern) if path.is_file() and path.stat().st_size > 0)
        if not matches:
            self.errors.append(f"Required directory has no matching content ({pattern}): {relative}")
        return matches

    def scan_placeholders(self, paths: Iterable[Path]) -> None:
        for path in sorted(set(paths)):
            if path.suffix.lower() not in {".md", ".txt", ".html", ".json", ".yaml", ".yml"}:
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in PLACEHOLDER_PATTERNS:
                match = pattern.search(content)
                if match:
                    relative = path.relative_to(self.run_root)
                    excerpt = " ".join(match.group(0).split())
                    self.errors.append(f"Placeholder marker in {relative}: {excerpt}")
                    break

    def require_pass(self, relative: str) -> None:
        path = self.require_file(relative)
        if not path or not path.is_file():
            return
        content = path.read_text(encoding="utf-8", errors="replace")
        if not re.search(r"(?im)^\s*Verdict:\s*PASS\s*$", content):
            self.errors.append(f"Review does not contain an exact PASS verdict: {relative}")


def validate_phase_1(report: Report) -> list[Path]:
    paths = [
        report.require_file("source-manifest.json", 20),
        report.require_file("run-state.json", 20),
        report.require_file("source-digest.md"),
        report.require_file("decision-log.md"),
        report.require_file("phase-1/high-level-project-definition.md", 300),
    ]
    report.require_dir_content("phase-1/reviews", "*.md")
    report.require_pass("phase-1/final-review.md")
    return [path for path in paths if path]


def validate_phase_2(report: Report) -> list[Path]:
    required = (
        "phase-2/product-definition.md",
        "phase-2/experience-principles.md",
        "phase-2/feature-index.md",
        "phase-2/traceability.md",
        "phase-2/mockups/mockup-index.md",
        "phase-2/inspiration/inspiration-index.md",
    )
    paths = [report.require_file(path, 200) for path in required]
    paths.extend(report.require_dir_content("phase-2/features", "F-*.md"))

    for round_number in range(1, 6):
        round_dir = f"phase-2/research/round-{round_number:02d}"
        research = report.require_dir_content(round_dir, "*.md")
        if len(research) < 3:
            report.errors.append(f"Expansion round {round_number:02d} needs three independent research files")
        paths.extend(research)
        review_pattern = f"round-{round_number:02d}-review-*.md"
        reviews = report.require_dir_content("phase-2/reviews", review_pattern)
        if reviews and not any(
            re.search(r"(?im)^\s*Verdict:\s*PASS\s*$", path.read_text(encoding="utf-8", errors="replace"))
            for path in reviews
        ):
            report.errors.append(f"Expansion round {round_number:02d} has no PASS review")
        paths.extend(reviews)

    images = [
        path
        for path in (report.run_root / "phase-2/mockups/generated").glob("**/*")
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES and path.stat().st_size > 0
    ]
    if not images:
        report.errors.append("No generated mockup image found under phase-2/mockups/generated")

    report.require_pass("phase-2/final-review.md")
    return [path for path in paths if path]


def validate_phase_3(report: Report) -> list[Path]:
    required = (
        "phase-3/technical-design.md",
        "phase-3/architecture.md",
        "phase-3/production-plan.md",
        "phase-3/tasks/task-index.md",
        "phase-3/task-reviews.md",
    )
    paths = [report.require_file(path, 200) for path in required]
    tasks = report.require_dir_content("phase-3/tasks", "T-*.md")
    paths.extend(tasks)
    task_reviews = report.run_root / "phase-3/task-reviews.md"
    if task_reviews.is_file():
        review_text = task_reviews.read_text(encoding="utf-8", errors="replace")
        for task in tasks:
            task_id = task.stem.split("-", 2)
            identifier = "-".join(task_id[:2]) if len(task_id) >= 2 else task.stem
            if not re.search(rf"(?is)\b{re.escape(identifier)}\b.*?\bPASS\b", review_text):
                report.errors.append(f"No PASS verdict found for task {identifier} in phase-3/task-reviews.md")
    report.require_pass("phase-3/final-review.md")
    return [path for path in paths if path]


def validate_phase_4(report: Report) -> list[Path]:
    paths = [
        report.require_file("phase-4/local-preview.md", 200),
        report.require_file("phase-4/verification-report.md", 200),
    ]
    product = report.require_dir_content("phase-4/product")
    task_runs = report.require_dir_content("phase-4/task-runs", "**/implementation.md")
    reviews = report.require_dir_content("phase-4/task-runs", "**/review-*.md")
    if reviews and not all(
        re.search(r"(?im)^\s*Verdict:\s*PASS\s*$", path.read_text(encoding="utf-8", errors="replace"))
        for path in reviews
    ):
        report.errors.append("At least one implementation review lacks an exact PASS verdict")
    report.require_pass("phase-4/final-review.md")
    paths.extend(product)
    paths.extend(task_runs)
    paths.extend(reviews)
    return [path for path in paths if path]


def validate_final(report: Report) -> list[Path]:
    return [
        path
        for path in (
            report.require_file("final-delivery/START-HERE.md", 200),
            report.require_file("final-delivery/artifact-inventory.md", 150),
            report.require_file("final-delivery/production-readiness.md", 150),
        )
        if path
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_root", type=Path, help="Path to one-shot-output")
    parser.add_argument("--through", choices=PHASE_ORDER, default="final")
    parser.add_argument("--report", type=Path, help="Optional JSON report path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_root = args.run_root.expanduser().resolve()
    if not run_root.is_dir():
        raise SystemExit(f"Run root does not exist or is not a directory: {run_root}")

    report = Report(run_root=run_root, through=args.through)
    scan_paths: list[Path] = []
    validators = {
        "phase-1": validate_phase_1,
        "phase-2": validate_phase_2,
        "phase-3": validate_phase_3,
        "phase-4": validate_phase_4,
        "final": validate_final,
    }
    for phase in PHASE_ORDER:
        scan_paths.extend(validators[phase](report))
        if phase == args.through:
            break
    report.scan_placeholders(scan_paths)

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "run_root": str(run_root),
        "through": args.through,
        "valid": not report.errors,
        "error_count": len(report.errors),
        "warning_count": len(report.warnings),
        "errors": report.errors,
        "warnings": report.warnings,
        "checked": report.checked,
    }
    if args.report:
        report_path = args.report.expanduser().resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2))
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
