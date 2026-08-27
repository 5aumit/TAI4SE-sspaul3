# 2 — Duplication

**Category.** The low-quality code data category for this task is
**duplication**: the same code appearing more than once in a corpus, whether
byte-identical or lightly edited.

**Recommended reading.** [*StarCoder 2 and The Stack v2: The Next
Generation*](https://arxiv.org/abs/2402.19173) (arXiv:2402.19173), for how
duplicates are identified; and Allamanis, [*The Adverse Effects of Code
Duplication in Machine Learning Models of
Code*](https://doi.org/10.1145/3359591.3359735) (Onward! 2019), for why it
matters.

**Your task.** The 500 files in `data/2` contain **5 duplicate pairs, involving
10 files** — some exact, some near-duplicates. Read the paper to work out how
such files are identified, then submit the five pairs.

**Submission format.** One file named `2-duplication.csv`, with this header and exactly 5 rows — one per pair you are claiming:

```csv
file_a,file_b
0001.py,0002.py
```

Both columns are filenames as they appear in `data/2`. The order within a row does not matter: a duplicate pair is symmetric, and naming only one file of a pair does not identify anything. The row above illustrates the format only.
