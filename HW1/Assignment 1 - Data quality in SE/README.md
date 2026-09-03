# HW1: Duplication Detection in The Stack v2

This submission detects near-duplicate Python files with token 5-gram Jaccard
similarity. It is for CSC 591/791 Assignment 1, Data Quality Issues in Code
Corpora.

## Contents

- `solution/detect_duplication.py`: the starter-data detector.
- `data/2/`: the supplied Python starter examples.
- `solution/2-duplication.csv`: the detected starter-data pairs.
- `solution/jaccard_scores.csv`: all starter-data similarity scores.
- `scripts/sample_repositories.py`: creates the reproducible Stack v2 sample.
- `scripts/run_sample_detector.py`: applies the detector within each sampled
  repository.
- `candidates.jsonl`: 12 manually reviewed duplicate-file candidates.

## Requirements

The starter-data detector uses only the Python standard library. Preparing a
Stack v2 sample also needs Python 3 and `pyarrow`:

```bash
python3 -m venv /tmp/hw1-venv
/tmp/hw1-venv/bin/pip install -r scripts/requirements.txt
```

Run the commands below from this directory, `HW1/Assignment 1 - Data quality in
SE`.

## Run the detector on the starter data

```bash
python3 solution/detect_duplication.py data/2 \
  --output /tmp/hw1-starter-pairs.csv \
  --scores-output /tmp/hw1-starter-scores.csv \
  --threshold 0.70
```

The detector tokenizes each Python file, removes comments and layout tokens,
forms unique overlapping token 5-grams, and compares all valid file pairs with
Jaccard similarity. A pair is flagged at similarity 0.70 or above. The run
skips files that cannot be tokenized and reports those errors.

## Reproduce the Stack v2 sample

The sample source is the Python re-host at
`https://huggingface.co/datasets/Reset23/the-stack-v2-python`, pinned to
revision `ee79c0cd3580beba2d627a3a457ae265b0fc979b`. This is an unofficial public
re-host, not the canonical BigCode release.

```bash
/tmp/hw1-venv/bin/python scripts/sample_repositories.py --output /tmp/hw1-sample
/tmp/hw1-venv/bin/python scripts/run_sample_detector.py --sample /tmp/hw1-sample
```

Sampling is deterministic. It reads `data/train-00000-of-00011.parquet`, keeps
eligible UTF-8 Python files of at most 100,000 bytes, chooses 200 repositories
by a SHA-256 ordering seeded with `591`, and keeps at most 50 files per chosen
repository. Comparisons are made only within each sampled repository.

The recorded run sampled 2,496 files, flagged 1,808 unreviewed pairs, skipped
29 files that could not be tokenized, and selected six reviewed pairs. The
committed `candidates.jsonl` therefore contains 12 records from those six
manually reviewed pairs.

## Candidate provenance

Each record in `candidates.jsonl` retains the Stack v2 `blob_id`, `src_encoding`,
`repo_name`, `path`, and `revision_id` from the pinned source. Its `flag_reason`
names the matching blob, path, review-pair identifier, and similarity score.
Together with the pinned dataset revision, these fields let a reader locate the
candidate in the source dataset when it remains available.

Duplicates are represented as file-level relationships, so `line_span` is not
included: this detector flags a pair of whole files rather than a single,
localized defective line range.

## Tests

```bash
/tmp/hw1-venv/bin/python -m unittest discover -s solution -p 'test_*.py'
/tmp/hw1-venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
```
