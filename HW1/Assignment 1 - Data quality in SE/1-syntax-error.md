# 1 — Syntax Error

**Category.** The low-quality code data category for this task is **syntax
error**: files a corpus ingested and shipped even though they do not parse.

**Recommended reading.** [*Rewriting Pre-Training Data Boosts LLM Performance in
Math and Code*](https://arxiv.org/abs/2505.02881) (the SwallowCode paper;
arXiv:2505.02881).

**Your task.** The 15 files in `data/1` contain **5 files that fail the paper's
syntax check**. Read the paper to work out how such files are identified, then
apply that check and submit a CSV naming those files.

**Submission format.** One file named `1-syntax-error.csv`, with this header and exactly 5 rows — one per file you are claiming:

```csv
file
example.py
```

`file` is the filename as it appears in `data/1`. The row above illustrates the format only — `example.py` is not in the dataset.
