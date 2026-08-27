# 6 — Code Smell

**Category.** The low-quality code data category for this task is **code
smell**: code that compiles, runs, and is nobody's idea of a good example.

**Recommended reading.** [*Clean Code, Better Models: Enhancing LLM Performance
with Smell-Cleaned Dataset*](https://arxiv.org/abs/2508.11958)
(arXiv:2508.11958).

**Your task.** The 15 files in `data/6` contain **5 findings under the five
target rules**, one file per rule. No target rule appears twice, and no file
carries more than one target rule. Read the paper to work out which analyser it
delegates its definition of a smell to, run that analyser over the folder, and
submit the file-to-rule mapping.

| Rule | Name |
| --- | --- |
| S3776 | Cognitive Complexity of functions should not be too high |
| S107 | Functions, methods and lambdas should not have too many parameters |
| S1192 | String literals should not be duplicated |
| S1481 | Unused local variables should be removed |
| S125 | Sections of code should not be commented out |

Run the default profile at its default thresholds and do not tune them: the
defaults are the definition for this task, and changing one changes the count.

The other ten files are not free of every smell the analyser knows — no real
code is — and a finding under some other rule is not one of the five you are
looking for.

**Submission format.** One file named `6-code-smell.csv`, with this header and exactly 5 rows — one per rule in the table:

```csv
file,rule
example.py,S0000
```

`file` is the filename as it appears in `data/6`; `rule` is the key from the table, written exactly as shown. The row above illustrates the format only.
