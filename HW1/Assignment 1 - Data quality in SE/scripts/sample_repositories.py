#!/usr/bin/env python3
"""Create the pinned, reproducible repository sample used for HW1."""

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from urllib.request import urlretrieve

import pyarrow.parquet as pq

REVISION = "ee79c0cd3580beba2d627a3a457ae265b0fc979b"
SHARD = "data/train-00000-of-00011.parquet"
DATASET_URL = "https://huggingface.co/datasets/Reset23/the-stack-v2-python"
DEFAULT_SEED = 591
DEFAULT_REPOSITORIES = 200
DEFAULT_FILES_PER_REPOSITORY = 50
MINIMUM_FILES_PER_REPOSITORY = 5
MAX_FILE_BYTES = 100_000
METADATA_COLUMNS = [
    "blob_id",
    "directory_id",
    "path",
    "repo_name",
    "snapshot_id",
    "revision_id",
    "src_encoding",
    "length_bytes",
]


def stable_key(*parts: object) -> str:
    """Return a deterministic ordering key for a selection item."""
    text = ":".join(str(part) for part in parts)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def is_eligible(row: dict[str, object]) -> bool:
    encoding = row.get("src_encoding")
    size = row.get("length_bytes")
    return (
        isinstance(row.get("repo_name"), str)
        and
        isinstance(encoding, str)
        and encoding.lower() in {"utf-8", "utf8"}
        and isinstance(size, int)
        and 0 < size <= MAX_FILE_BYTES
    )


def select_repositories(
    counts: Counter[str], seed: int, repository_count: int
) -> list[str]:
    """Select eligible repositories by a stable seed-derived order."""
    eligible = [
        name for name, count in counts.items() if count >= MINIMUM_FILES_PER_REPOSITORY
    ]
    if len(eligible) < repository_count:
        raise ValueError(
            f"only {len(eligible)} repositories meet the minimum of "
            f"{MINIMUM_FILES_PER_REPOSITORY} eligible files"
        )
    return sorted(eligible, key=lambda name: stable_key(seed, name))[:repository_count]


def select_files(
    rows: list[dict[str, object]], seed: int, files_per_repository: int
) -> list[dict[str, object]]:
    """Select a stable capped set of files from one repository."""
    return sorted(
        rows,
        key=lambda row: stable_key(seed, row["repo_name"], row["blob_id"], row["path"]),
    )[:files_per_repository]


def batches(parquet: pq.ParquetFile, columns: list[str]):
    for batch in parquet.iter_batches(columns=columns, batch_size=20_000):
        yield from batch.to_pylist()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("sample"))
    parser.add_argument("--source", type=Path, help="existing Parquet shard to use")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--repositories", type=int, default=DEFAULT_REPOSITORIES)
    parser.add_argument("--files-per-repository", type=int, default=DEFAULT_FILES_PER_REPOSITORY)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.repositories <= 0 or args.files_per_repository <= 0:
        print("error: sample sizes must be positive", file=sys.stderr)
        return 2
    if args.output.exists() and any(args.output.iterdir()):
        print(f"error: output directory is not empty: {args.output}", file=sys.stderr)
        return 2
    args.output.mkdir(parents=True, exist_ok=True)
    source = args.source or args.output / "source.parquet"
    if not source.exists():
        url = f"{DATASET_URL}/resolve/{REVISION}/{SHARD}"
        print(f"downloading {url}", file=sys.stderr)
        urlretrieve(url, source)

    parquet = pq.ParquetFile(source)
    counts: Counter[str] = Counter()
    for row in batches(parquet, ["repo_name", "src_encoding", "length_bytes"]):
        if is_eligible(row):
            counts[row["repo_name"]] += 1
    selected_repositories = select_repositories(counts, args.seed, args.repositories)
    selected_set = set(selected_repositories)

    selected_rows: dict[str, list[dict[str, object]]] = {name: [] for name in selected_repositories}
    for row in batches(parquet, METADATA_COLUMNS + ["content"]):
        if row["repo_name"] in selected_set and is_eligible(row):
            selected_rows[row["repo_name"]].append(row)

    manifest_path = args.output / "manifest.jsonl"
    total_files = 0
    with manifest_path.open("w", encoding="utf-8") as manifest:
        for repository_index, repository in enumerate(selected_repositories, start=1):
            repository_dir = args.output / "repos" / f"{repository_index:03d}"
            repository_dir.mkdir(parents=True)
            for file_index, row in enumerate(
                select_files(selected_rows[repository], args.seed, args.files_per_repository),
                start=1,
            ):
                local_file = repository_dir / f"{file_index:03d}.py"
                local_file.write_text(row["content"], encoding="utf-8")
                metadata = {
                    key: row[key]
                    for key in METADATA_COLUMNS
                }
                metadata["local_file"] = str(local_file.relative_to(args.output))
                manifest.write(json.dumps(metadata, ensure_ascii=False) + "\n")
                total_files += 1

    summary = {
        "dataset_url": DATASET_URL,
        "revision": REVISION,
        "shard": SHARD,
        "seed": args.seed,
        "eligible_files": sum(counts.values()),
        "eligible_repositories": len(counts),
        "selected_repositories": len(selected_repositories),
        "selected_files": total_files,
        "files_per_repository_cap": args.files_per_repository,
        "minimum_files_per_repository": MINIMUM_FILES_PER_REPOSITORY,
        "max_file_bytes": MAX_FILE_BYTES,
    }
    (args.output / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    if args.source is None:
        source.unlink()
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
