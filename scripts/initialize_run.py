#!/usr/bin/env python3
"""Initialize or safely resume a One Shot project run."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


VERSION = 1
DEFAULT_OUTPUT_NAME = "one-shot-output"
IGNORED_DIRS = {
    ".git",
    ".svn",
    ".hg",
    "node_modules",
    "__pycache__",
    ".DS_Store",
    DEFAULT_OUTPUT_NAME,
}
RUN_DIRS = (
    "phase-1/reviews",
    "phase-2/features",
    "phase-2/research",
    "phase-2/mockups/generated",
    "phase-2/inspiration",
    "phase-2/reviews",
    "phase-3/tasks",
    "phase-4/product",
    "phase-4/task-runs",
    "final-delivery",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def source_files(source_root: Path, run_root: Path) -> list[Path]:
    files: list[Path] = []
    for candidate in source_root.rglob("*"):
        if candidate.is_symlink() or not candidate.is_file():
            continue
        if is_within(candidate, run_root):
            continue
        relative = candidate.relative_to(source_root)
        if any(part in IGNORED_DIRS for part in relative.parts):
            continue
        files.append(candidate)
    return sorted(files, key=lambda item: item.relative_to(source_root).as_posix().lower())


def build_manifest(source_root: Path, run_root: Path) -> dict[str, Any]:
    entries = []
    for path in source_files(source_root, run_root):
        stat = path.stat()
        entries.append(
            {
                "path": path.relative_to(source_root).as_posix(),
                "bytes": stat.st_size,
                "modified_at": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
                "sha256": sha256_file(path),
                "suffix": path.suffix.lower(),
            }
        )
    return {
        "schema_version": VERSION,
        "generated_at": utc_now(),
        "source_root": str(source_root),
        "run_root": str(run_root),
        "file_count": len(entries),
        "files": entries,
    }


def initial_state(source_root: Path, run_root: Path) -> dict[str, Any]:
    return {
        "schema_version": VERSION,
        "source_root": str(source_root),
        "run_root": str(run_root),
        "initialized_at": utc_now(),
        "updated_at": utc_now(),
        "current_phase": "source-synthesis",
        "phases": {
            "phase-1": {"status": "pending", "accepted_review": None},
            "phase-2": {"status": "pending", "accepted_review": None},
            "phase-3": {"status": "pending", "accepted_review": None},
            "phase-4": {"status": "pending", "accepted_review": None},
            "final": {"status": "pending", "accepted_review": None},
        },
        "last_validation": None,
    }


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_root", type=Path, help="Folder containing the transcript and source artifacts")
    parser.add_argument(
        "--run-root",
        type=Path,
        help=f"Output folder (default: <source_root>/{DEFAULT_OUTPUT_NAME})",
    )
    parser.add_argument(
        "--refresh-manifest",
        action="store_true",
        help="Rebuild source-manifest.json without changing project artifacts or state",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.expanduser().resolve()
    if not source_root.is_dir():
        raise SystemExit(f"Source folder does not exist or is not a directory: {source_root}")

    run_root = (args.run_root or source_root / DEFAULT_OUTPUT_NAME).expanduser().resolve()
    if run_root == source_root:
        raise SystemExit("Run root must not be the same directory as source root")

    run_root.mkdir(parents=True, exist_ok=True)
    for relative in RUN_DIRS:
        (run_root / relative).mkdir(parents=True, exist_ok=True)

    manifest_path = run_root / "source-manifest.json"
    if not manifest_path.exists() or args.refresh_manifest:
        write_json(manifest_path, build_manifest(source_root, run_root))

    state_path = run_root / "run-state.json"
    resumed = state_path.exists()
    if not resumed:
        write_json(state_path, initial_state(source_root, run_root))

    result = {
        "status": "resumed" if resumed else "initialized",
        "source_root": str(source_root),
        "run_root": str(run_root),
        "manifest": str(manifest_path),
        "state": str(state_path),
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
