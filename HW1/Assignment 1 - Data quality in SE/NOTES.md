# HW1 Notes

This file records decisions and verified results for the final report. It is
not the final report.

## Assignment scope

- Category: duplication.
- The assignment permits a reasonable subset of The Stack v2, provided the
  chosen language, filter, sample, counts, and manual review are reported.
- The final submission still needs a report of no more than three pages, the
  detector code, a README, and up to 20 reviewed records in `candidates.jsonl`.

## Starter-data detector

- Method: tokenize Python code, remove comments and layout tokens, build unique
  overlapping token 5-grams, and score file pairs with Jaccard similarity.
- Duplicate threshold: 0.70.
- The detector found these five starter-data pairs: `0070.py`/`0339.py`,
  `0155.py`/`0322.py`, `0415.py`/`0456.py`, `0287.py`/`0393.py`, and
  `0171.py`/`0278.py`.
- Regeneration on 2026-08-31 reproduced the committed answer CSV exactly.
  Two detector unit tests passed. The run skipped malformed files `0162.py` and
  `0188.py` and scored 123,753 valid pairs.

## Public Stack v2 source

- Source: `https://huggingface.co/datasets/Reset23/the-stack-v2-python`.
- Pinned revision: `ee79c0cd3580beba2d627a3a457ae265b0fc979b`.
- This is an unofficial public re-host, not the canonical BigCode release. The
  final report must state this fact.
- It supplies direct source content and the required provenance fields:
  `blob_id`, `src_encoding`, `repo_name`, `path`, `revision_id`, `snapshot_id`,
  and `directory_id`.

## Reproducible repository sample

- Source slice: only `data/train-00000-of-00011.parquet` from the pinned
  revision, not the complete 2.03 GB dataset.
- Selection unit: repository. Compare files only within a sampled repository.
- Repository selection: choose the 200 eligible repository names with the
  smallest SHA-256 digest of `591:repo_name`.
- Eligibility: non-empty Python file, `src_encoding` is UTF-8 or UTF8, and
  `length_bytes` is at most 100,000.
- A repository needs at least five eligible files. Keep at most 50 eligible
  files per selected repository, ordered by the SHA-256 digest of
  `591:repo_name:blob_id:path`.
- Initial shard inspection on 2026-08-31: 90,910 rows, 90,470 eligible files,
  83,372 eligible repositories, and 230 repositories with at least five
  eligible files.

## How to reproduce the sample

1. Create an isolated environment and install the only dependency:

   ```bash
   python3 -m venv /tmp/hw1-sample-venv
   /tmp/hw1-sample-venv/bin/pip install -r scripts/requirements.txt
   ```

2. From this directory, prepare the data sample:

   ```bash
   /tmp/hw1-sample-venv/bin/python scripts/sample_repositories.py --output /tmp/hw1-sample
   ```

   The script temporarily downloads the pinned 185 MB shard, then removes it
   after it writes selected source files, `/tmp/hw1-sample/manifest.jsonl`, and
   `/tmp/hw1-sample/summary.json`. Use any empty output directory if a different
   location is needed.

3. Run the detector inside each sampled repository:

   ```bash
   /tmp/hw1-sample-venv/bin/python scripts/run_sample_detector.py --sample /tmp/hw1-sample
   ```

   This writes `/tmp/hw1-sample/duplication-pairs.jsonl` for manual inspection.
   Review its candidates before creating the final `candidates.jsonl`.

## Prepared-sample results

- On 2026-08-31, the sampler created 200 repositories containing 2,496 files.
- The per-repository detector produced 1,808 unreviewed pairs at the 0.70
  threshold.
- It skipped 29 files that could not be tokenized. These are excluded from
  comparisons and should be reported as a limitation of this duplication run.
- `scripts/review_candidates.py export` sorts pairs by descending score and
  creates a Markdown review file with a checkbox for each pair. The reviewer
  selects pairs by changing `[ ]` to `[x]`.
- `scripts/review_candidates.py build` turns checked pairs into two individual
  `candidates.jsonl` records per pair. It rejects more than 10 pairs, so the
  output cannot exceed the assignment limit of 20 records.
- On 2026-09-01, `scripts/review_candidates.py export --sample sample --output
  sample/review.md --count 15` produced a ranked 15-pair review file. It is
  ignored with the raw sample data and can be regenerated from the scripts.
- Manual review selected six pairs (IDs 001, 002, 005, 006, 009, and 010).
  The candidate builder therefore produced 12 individual candidate records.
