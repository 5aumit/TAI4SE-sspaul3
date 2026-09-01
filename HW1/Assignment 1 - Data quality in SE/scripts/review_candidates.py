#!/usr/bin/env python3
"""Export duplicate pairs for review and build assignment candidate records.

Use ``export`` to create a Markdown file. Mark chosen pairs by changing their
checkbox from ``[ ]`` to ``[x]``. Then use ``build`` to create candidates.jsonl.
Each checked pair creates two file records, so at most ten pairs may be checked.
"""

import argparse
import json
import re
import sys
from pathlib import Path

CHECKBOX = re.compile(r"^- \[(?P<selected>[ xX])\] Candidate pair (?P<id>\d+)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)

    export = subcommands.add_parser("export", help="write a Markdown review file")
    export.add_argument("--sample", type=Path, default=Path("sample"))
    export.add_argument("--output", type=Path, default=Path("sample/review.md"))
    export.add_argument("--count", type=int, default=15)

    build = subcommands.add_parser("build", help="write assignment candidate records")
    build.add_argument("--review", type=Path, default=Path("sample/review.md"))
    build.add_argument("--pairs", type=Path, default=Path("sample/duplication-pairs.jsonl"))
    build.add_argument("--output", type=Path, default=Path("candidates.jsonl"))
    return parser.parse_args()


def load_pairs(path: Path) -> list[dict[str, object]]:
    with path.open(encoding="utf-8") as source:
        pairs = [json.loads(line) for line in source if line.strip()]
    return sorted(
        pairs,
        key=lambda pair: (
            -float(pair["jaccard_similarity"]),
            str(pair["repo_name"]),
            str(pair["left"]["path"]),
            str(pair["right"]["path"]),
        ),
    )


def selected_pair_ids(review: Path) -> set[int]:
    selected = set()
    for line in review.read_text(encoding="utf-8").splitlines():
        match = CHECKBOX.match(line)
        if match and match["selected"].lower() == "x":
            selected.add(int(match["id"]))
    return selected


def source_text(sample: Path, record: dict[str, object]) -> str:
    path = sample / str(record["local_file"])
    return path.read_text(encoding="utf-8")


def write_review(pairs: list[dict[str, object]], sample: Path, output: Path, count: int) -> None:
    if count < 1:
        raise ValueError("count must be at least 1")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as review:
        review.write("# Duplicate-pair review\n\n")
        review.write("Change `[ ]` to `[x]` for pairs to submit. Each checked pair creates ")
        review.write("two records, so check no more than 10 pairs.\n\n")
        for pair_id, pair in enumerate(pairs[:count], start=1):
            left = pair["left"]
            right = pair["right"]
            review.write(f"## Pair {pair_id}\n\n")
            review.write(f"- [ ] Candidate pair {pair_id:03d}\n")
            review.write(f"- Similarity: {float(pair['jaccard_similarity']):.3f}\n")
            review.write(f"- Repository: `{pair['repo_name']}`\n")
            for label, record in (("Left", left), ("Right", right)):
                review.write(f"- {label} source path: `{record['path']}`\n")
                review.write(f"- {label} local file: `{record['local_file']}`\n")
            review.write("\n### Left file\n\n```python\n")
            review.write(source_text(sample, left))
            review.write("\n```\n\n### Right file\n\n```python\n")
            review.write(source_text(sample, right))
            review.write("\n```\n\n")


def candidate_record(
    record: dict[str, object], counterpart: dict[str, object], pair_id: int, score: float
) -> dict[str, object]:
    return {
        "blob_id": record["blob_id"],
        "src_encoding": record["src_encoding"],
        "repo_name": record["repo_name"],
        "path": record["path"],
        "revision_id": record["revision_id"],
        "flag_reason": (
            f"Token 5-gram Jaccard similarity {score:.3f} with "
            f"{counterpart['blob_id']} at {counterpart['path']} (review pair {pair_id:03d})."
        ),
    }


def write_candidates(selected: set[int], pairs: list[dict[str, object]], output: Path) -> int:
    if len(selected) > 10:
        raise ValueError("at most 10 pairs may be selected because each pair creates two records")
    if not selected:
        raise ValueError("no checked candidate pairs found")
    if min(selected) < 1 or max(selected) > len(pairs):
        raise ValueError("a checked pair ID is not present in duplication-pairs.jsonl")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as destination:
        for pair_id in sorted(selected):
            pair = pairs[pair_id - 1]
            score = float(pair["jaccard_similarity"])
            destination.write(json.dumps(candidate_record(pair["left"], pair["right"], pair_id, score)) + "\n")
            destination.write(json.dumps(candidate_record(pair["right"], pair["left"], pair_id, score)) + "\n")
    return len(selected) * 2


def main() -> int:
    args = parse_args()
    try:
        if args.command == "export":
            pairs = load_pairs(args.sample / "duplication-pairs.jsonl")
            write_review(pairs, args.sample, args.output, args.count)
            print(f"wrote {min(args.count, len(pairs))} pair(s) to {args.output}")
        else:
            selected = selected_pair_ids(args.review)
            count = write_candidates(selected, load_pairs(args.pairs), args.output)
            print(f"wrote {count} candidate record(s) to {args.output}")
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
