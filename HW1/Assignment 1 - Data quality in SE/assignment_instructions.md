# Assignment 1: Data Quality Issues in Code Corpora

- **Course:** CSC 591/791 - Trustworthy AI for Software Engineering
- **Work type:** Individual
- **Deadline:** September 7, 2026, at 3:00 PM
- **Dataset:** The Stack v2

## Main Tasks

1. Read *StarCoder 2 and The Stack v2: The Next Generation* (arXiv:2402.19173), especially how the dataset was collected, filtered, deduplicated, and prepared.
2. Choose one supported data-quality issue:
   - Syntax errors
   - Duplication
   - Vulnerable code
   - License issues
   - PII/privacy
   - Code smells
3. Clearly define what counts as a problematic instance.
4. Build or adapt an automatic detection method.
   - You may use tools, libraries, static analyzers, parsers, heuristics, or LLMs.
   - Running an existing tool with only its default settings is not enough.
   - Explain what you designed, changed, combined, or configured.
5. Evaluate the detector with the provided starter examples.
   - Report correct and incorrect detections.
   - Analyze false positives and false negatives.
   - Report precision, recall, and F1 when appropriate.
   - Discuss individual examples, especially when the dataset is small.
6. Apply the detector to a reasonable subset of The Stack v2.
   - Explain the selected language, repository, file type, split, sample, or other filter.
   - Report the number of files analyzed, number flagged, and number manually inspected.
7. Explain the method's strengths, weaknesses, missed cases, false positives, confidence level, and implications for trustworthy code datasets.

## Extra Requirements for an LLM-Based Detector

Report:

- Model name
- Prompt
- Relevant inference settings
- How model output becomes a detection decision
- Estimated total cost and, when possible, cost per file or example

## Submission

Submit one ZIP file through Gradescope containing:

- A single-column report of no more than 3 pages
- Detection code or script
- `README.md`
- `candidates.jsonl` with up to 20 representative candidates found in The Stack v2

Each `candidates.jsonl` record must include:

- `blob_id`
- `src_encoding`
- `repo_name`
- `path`
- One available identifier: `revision_id`, `snapshot_id`, or `directory_id`
- `line_span` when the issue occurs on specific lines
- `flag_reason`

## Suggested Report Structure

1. **Data-Quality Issue:** Define and motivate the selected problem.
2. **Detection Method:** Explain the tools, rules, models, signals, logic, and assumptions.
3. **Evaluation and Findings:** Give metrics, errors, sampling details, and Stack v2 results.
4. **Limitations and Implications:** Explain missed cases, unreliable cases, and lessons for trustworthy training data.

Include at least one representative success case and, if available, one representative failure case.

## README Requirements

Explain:

- How to run the detector
- Required dependencies
- Tools or models used
- How the submitted candidates were obtained
- How each candidate can be traced to The Stack v2, when possible

## Privacy and Safety

- The PII starter files contain synthetic replacements, but treat them as real sensitive information.
- Do not expose, redistribute, or validate real credentials, personal information, or other sensitive data found in The Stack v2.
- Redact sensitive values in the report and submitted examples when needed.

## Grading

- Problem definition and motivation: **15%**
- Detection method: **30%**
- Evaluation methodology: **25%**
- Results and error analysis: **20%**
- Reproducibility and presentation: **10%**

Careful reasoning and credible evaluation are more important than method complexity.
