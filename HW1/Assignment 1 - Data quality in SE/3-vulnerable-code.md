# 3 — Vulnerable Code

**Category.** The low-quality code data category for this task is **vulnerable
code**: files that run correctly and teach an insecure pattern.

**Recommended reading.** Pearce, Ahmad, Tan, Dolan-Gavitt, Karri,
[*Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code
Contributions*](https://arxiv.org/abs/2108.09293) (arXiv:2108.09293;
IEEE S&P 2022).

**Your task.** The 15 files in `data/3` contain **5 findings under the five
target CWEs**, one file per CWE in the table below. No target CWE appears twice,
and no file carries more than one target CWE. Read the paper to work out how
such files are identified, then submit the file-to-CWE mapping.

| CWE | Name |
| --- | --- |
| CWE-79 | Improper Neutralization of Input During Web Page Generation (Cross-site Scripting) |
| CWE-78 | Improper Neutralization of Special Elements used in an OS Command (OS Command Injection) |
| CWE-89 | Improper Neutralization of Special Elements used in an SQL Command (SQL Injection) |
| CWE-22 | Improper Limitation of a Pathname to a Restricted Directory (Path Traversal) |
| CWE-502 | Deserialization of Untrusted Data |

All five are drawn from the list the paper evaluates against. The table is given
so you can target these five rather than read a whole suite's output.

The five positives are inert teaching fixtures. Analyse them; do not run them or
expose them as web services.

**Submission format.** One file named `3-vulnerable-code.csv`, with this header and exactly 5 rows — one per CWE in the table:

```csv
file,cwe
example.py,CWE-000
```

`file` is the filename as it appears in `data/3`; `cwe` is the identifier from the table, written exactly as shown. The row above illustrates the format only.
