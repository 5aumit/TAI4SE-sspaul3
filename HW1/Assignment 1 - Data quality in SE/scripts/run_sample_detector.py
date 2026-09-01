#!/usr/bin/env python3
"""Run the duplication detector separately for every prepared repository."""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

SOLUTION_DIR = Path(__file__).resolve().parents[1] / "solution"
sys.path.insert(0, str(SOLUTION_DIR))
from detect_duplication import detect  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sample", type=Path, default=Path("sample"))
    parser.add_argument("--threshold", type=float, default=0.70)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = args.sample / "manifest.jsonl"
    if not manifest_path.is_file():
        print(f"error: missing manifest: {manifest_path}", file=sys.stderr)
        return 2
    by_directory: dict[str, dict[str, dict[str, object]]] = defaultdict(dict)
    with manifest_path.open(encoding="utf-8") as manifest:
        for line in manifest:
            row = json.loads(line)
            local_file = Path(row["local_file"])
            by_directory[str(local_file.parent)][local_file.name] = row

    output_path = args.sample / "duplication-pairs.jsonl"
    match_count = 0
    with output_path.open("w", encoding="utf-8") as output:
        for directory, files in sorted(by_directory.items()):
            matches, _, errors = detect(args.sample / directory, args.threshold)
            for filename, error in errors:
                print(f"warning: skipped {directory}/{filename}: {error}", file=sys.stderr)
            for left, right, score in matches:
                output.write(
                    json.dumps(
                        {
                            "repo_name": files[left]["repo_name"],
                            "left": files[left],
                            "right": files[right],
                            "jaccard_similarity": score,
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
                match_count += 1
    print(f"wrote {match_count} pair(s) to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
