# 4 — License

**Category.** The low-quality code data category for this task is **licence**:
files that must not appear in a permissively licensed corpus. Nothing is wrong
with the code — what is wrong is that it was collected.

**Recommended reading.** Kocetkov et al., [*The Stack: 3 TB of permissively
licensed source code*](https://arxiv.org/abs/2211.15533) (arXiv:2211.15533).

**Your task.** The 7 files in `data/4` contain 2 that do not belong in a
permissively licensed corpus; the other 5 belong. Work out from the paper how
licences are assigned and which ones the corpus keeps, then submit a CSV
identifying the two and labelling each:

- `copyleft` — under a licence the paper's permissive list excludes
- `no-license` — carries no licence at all

Exactly one file falls under each.

**This task needs internet access.** `data/4/sources.csv` gives, for every file,
the originating repository, the path inside it, the repository URL, and a
Software Heritage permalink — and nothing else. It carries no licence column, so
you have to go and look at each origin.

Check two different things per file: what the repository advertises, and what
the file header itself says. Where a repository advertises nothing but the file
header states a licence, the header decides. `no-license` is only where both are
silent.

**Submission format.** One file named `4-license.csv`, with this header and exactly 2 rows:

```csv
file,finding
example.py,copyleft
```

`file` is the filename as it appears in `data/4`. `finding` is either `copyleft` or `no-license`, written exactly as shown — one row of each. The row above illustrates the format only.
