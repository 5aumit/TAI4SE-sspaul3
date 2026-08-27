#!/usr/bin/env python3
"""Find duplicate Python files using token 5-gram Jaccard similarity.

Comments and layout tokens are removed, but exact names and literal values are
preserved. The detector compares every valid file pair. It writes duplicate
pairs at or above the threshold and a separate CSV containing every Jaccard
score, sorted from highest to lowest.
"""

import argparse
import csv
import sys
import tokenize
from itertools import combinations
from pathlib import Path

SKIPPED_TOKENS = {
    tokenize.ENCODING,
    tokenize.COMMENT,
    tokenize.NL,
    tokenize.NEWLINE,
    tokenize.INDENT,
    tokenize.DEDENT,
    tokenize.ENDMARKER,
}


def token_ngrams(path: Path, size: int = 5) -> set[tuple[str, ...]]:
    """Return unique, overlapping token n-grams for one Python file."""
    with tokenize.open(path) as source:
        tokens = [
            token.string
            for token in tokenize.generate_tokens(source.readline)
            if token.type not in SKIPPED_TOKENS
        ]
    return {tuple(tokens[index : index + size]) for index in range(len(tokens) - size + 1)}


def jaccard(left: set[tuple[str, ...]], right: set[tuple[str, ...]]) -> float:
    """Return intersection-over-union similarity for two n-gram sets."""
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def detect(
    folder: Path, threshold: float
) -> tuple[list[tuple[str, str, float]], list[tuple[str, str, float]], list[tuple[str, str]]]:
    """Score every valid pair and return matches, all scores, and read errors."""
    grams = {}
    errors = []

    for path in sorted(folder.glob("*.py")):
        try:
            grams[path.name] = token_ngrams(path)
        except (OSError, SyntaxError, UnicodeError, tokenize.TokenError) as error:
            errors.append((path.name, str(error)))

    scores = [
        (left, right, jaccard(grams[left], grams[right]))
        for left, right in combinations(grams, 2)
    ]
    scores.sort(key=lambda result: (-result[2], result[0], result[1]))
    matches = [result for result in scores if result[2] >= threshold]
    return matches, scores, errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="folder containing Python files")
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("2-duplication.csv"),
        help="duplicate-pair CSV (default: 2-duplication.csv)",
    )
    parser.add_argument(
        "--scores-output", type=Path, default=Path("jaccard_scores.csv"),
        help="sorted all-pairs score CSV (default: jaccard_scores.csv)",
    )
    parser.add_argument(
        "--threshold", type=float, default=0.70,
        help="minimum duplicate score (default: 0.70)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.folder.is_dir():
        print(f"error: not a directory: {args.folder}", file=sys.stderr)
        return 2
    if not 0 <= args.threshold <= 1:
        print("error: threshold must be between 0 and 1", file=sys.stderr)
        return 2

    matches, scores, errors = detect(args.folder, args.threshold)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(("file_a", "file_b"))
        writer.writerows((left, right) for left, right, _ in matches)

    args.scores_output.parent.mkdir(parents=True, exist_ok=True)
    with args.scores_output.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(("file_a", "file_b", "jaccard_similarity"))
        writer.writerows((left, right, f"{score:.12g}") for left, right, score in scores)

    for left, right, score in matches:
        print(f"{score:.3f}  {left}  {right}")
    for filename, error in errors:
        print(f"warning: skipped {filename}: {error}", file=sys.stderr)
    print(f"wrote {len(matches)} pair(s) to {args.output}", file=sys.stderr)
    print(f"wrote {len(scores)} score(s) to {args.scores_output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
