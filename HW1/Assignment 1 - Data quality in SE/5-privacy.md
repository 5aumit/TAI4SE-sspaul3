# 5 — Personally Identifiable Information

**Category.** The low-quality code data category for this task is **personally
identifiable information (PII)**: addresses, names, account handles and
credentials that developers committed and a scraper then collected.

**Recommended reading.** Yang, Velasco, Fang, Xu, Poshyvanyk, [*Understanding
Privacy Risks in Code Models Through Training Dynamics: A Causal
Approach*](https://arxiv.org/abs/2512.07814) (arXiv:2512.07814).

**Your task.** The 206 Java files in `data/5` contain **6 files with PII**, one
file for each type in the table below. No type appears twice, and no file
carries more than one target type. Read the paper to work out how such data is
identified, then submit the file-to-type mapping.

| Type | What counts here |
| --- | --- |
| `email` | An email address belonging to a person |
| `name` | A person's full name |
| `username` | A personal account handle — an identifier that names a person without being their full name |
| `password` | A password written into the source |
| `key` | A provider-issued credential such as an API key, app key, or access token |
| `ip_address` | A hard-coded IP address, private ranges included |

Three scoping rules for this folder, because they decide the answer:

- A value counts wherever a scraper would have ingested it — comments, Javadoc
  tags and commented-out lines are all in scope.
- `name` and `username` are told apart by the identifier itself, not by where it
  sits.
- The value has to be a value, not a placeholder. Tutorial filler
  (`user@example.com`, `John Doe`, `changeme`) and loopback or wildcard addresses
  are not PII; private-range addresses are.

**Submission format.** One file named `5-privacy.csv`, with this header and exactly 6 rows — one per type in the table:

```csv
file,pii_type
Example.java,email
```

`file` is the filename as it appears in `data/5`; `pii_type` is the identifier from the table, written exactly as shown. The row above illustrates the format only.

**Safety — read this before you open the folder.** These files are real blobs
from The Stack v2, collected because personal data had been committed into them.
**The six values have since been replaced with synthetic ones** of the same kind
and shape, so nothing here reaches anyone — but a detector cannot tell, and
neither can you at a glance. Work the folder as though the values were live:

- **Never** use, test, or validate a credential you find here.
- **Never** contact a person whose address or name appears in these files.
- **Never** paste a value into your CSV, your `README.md`, a chat, or an issue.
  Cite by file, line, and type: "API key, line 26".
- If you believe a credential is live and high-impact, tell the TA. Do not
  contact the repository owner yourself.
