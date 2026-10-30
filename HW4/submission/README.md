# HW4 supporting files: code-to-pseudocode robustness evaluation

The report is not included. Add your report before creating the final Gradescope ZIP.

Public fork: https://github.com/5aumit/EvaLooop/tree/hw4-pseudocode

Published source commit: `ca8388093953dba0c16db608c8b57ad223af20c4`.

Immutable source: https://github.com/5aumit/EvaLooop/tree/ca8388093953dba0c16db608c8b57ad223af20c4

Upstream base: `ce22fe2f80c8f36da85cc8a0cca49c2bcc8b1cb9` in
https://github.com/evalooop/EvaLooop.

## Contents

- `changes.patch`: code and documentation changes against the upstream base.
- `results/`: four complete framework results JSON files, including fresh baselines.
- `summary.csv`: one row per completed model/configuration run.
- `logs/` and `provenance.json`: completed-run logs, settings, durations, and source commits.
- `analysis/`: reproduced metrics, survival plot, paired comparisons, and failure evidence.
- `failure_annotations.json`: 22 traceable, AI-assisted inspection notes for author review.
- `analyze_hw4.py`: offline reproduction of tables, plot, and audit evidence.
- `constraints-hw4.txt` and `environment.txt`: the experiment dependency versions.
- `AI_USAGE.md`: assistant-use disclosure, classification procedure, and cost limits.

The supplied course data, credentials, aborted runs, and diagnostic responses are
not included. Every results JSON here came from our completed experiments.

## Protocol and models

All four runs use the same full set of 378 MBPP Plus tasks; no sampling occurred.
Each configuration has one completed run. Generation uses temperature 0, top-p 1,
1024 maximum new tokens, and a maximum of 10 cycles. Both base and plus tests must
pass for a task to continue. Each model performs both directions with a fresh
context per call. Four API requests run concurrently per configuration.

| Model ID | Configurations | Reasoning setting |
|---|---|---|
| `meta-llama/llama-3.1-8b-instruct` | standard and pseudocode | provider default |
| `qwen/qwen3.7-flash` | standard and pseudocode | explicitly disabled |

The standard generation prompt and tests are identical across loop types. The
standard description task requests a one-sentence prose summary. The extension
requests structured pseudocode with FUNCTION, INPUTS, OUTPUT, STEPS, and END
FUNCTION. It strips whitespace and uses the same docstring/assertion wrapper;
there is no repair pass or external perturbation. Exact templates are in
`EvaluationConfig.get_task_configs()` and `PSEUDOCODE_PROMPT` in the fork.

The runtime generates descriptions before testing code, but only uses a description
in another cycle if the code passes. Formatting is requested, not enforced.
The client keeps the upstream per-request retry behavior. The four submitted
runs have no logged warnings or retries. Earlier incomplete runs were discarded
when the runs were restarted concurrently; GPT-OSS trials were stopped and replaced
by Qwen. No incomplete run is counted as a result or additional replicate.

## Reproduce the evaluation

These commands make paid API calls and execute generated code inside Docker.

```bash
git clone --branch hw4-pseudocode https://github.com/5aumit/EvaLooop.git
cd EvaLooop
git checkout ca8388093953dba0c16db608c8b57ad223af20c4
# Put OPENROUTER_API_KEY in ../.env; do not add it to Git.
docker compose build
docker compose run --rm benchmark
```

The launcher runs all four configurations sequentially, with four parallel
requests within each run. To run separate configurations concurrently, start
each with a distinct container name and output directory. For example:

```bash
docker compose run -d --rm --name hw4-qwen-pseudocode benchmark \
  --models qwen/qwen3.7-flash --loops pseudocode \
  --output-dir /results/parallel/qwen-pseudocode
```

Repeat with the other model/loop pairs in separate directories. Do not also start
the default four-run launcher. Each container has up to four CPUs, 4 GB memory,
256 processes, no extra capabilities, and no privilege escalation. Only the
results directory is mounted. No GPU or local model weights are required.

The runner saves results and per-run logs only after evaluation completes. It
then runs the framework analyzer without a similarity judge and writes a CSV row.
An interrupted configuration cannot resume; existing outputs are not overwritten.
API providers, model updates, and backend nondeterminism can change rerun outputs.

## Reproduce every reported number without API calls

From this unpacked submission directory, using Python with Matplotlib:

```bash
python analyze_hw4.py --results-dir results --output-dir reproduced-analysis \
  --annotations failure_annotations.json
```

Or use the fork's built Docker image, from this unpacked submission directory:

```bash
docker run --rm --network none --entrypoint python \
  --mount "type=bind,source=$PWD,target=/submission" hw4-eval \
  /app/analyze_hw4.py --results-dir /submission/results \
  --output-dir /submission/reproduced-analysis \
  --annotations /submission/failure_annotations.json
```

This validates all task IDs, stop rules, cycle outcomes, retained assertions, and
Qwen's reasoning setting. It emits:

- `summary.csv`: required initial success rates and ASL scores.
- `metrics.json`: retention, conditional ASL, survival counts, and failure counts.
- `survival.csv` and `survival_comparison.png`/`.pdf`: report figure data and plot.
- `paired_comparison.csv`: task-matched better/tied/worse counts.
- `failure_review.csv` and `failure_review.md`: annotations joined to saved evidence.

With T=378, M=10, and i the successful-cycle count for each task:

```text
success_rate = count(i >= 1) / T
asl_score    = sum(i*i) / (T*M)
retention    = count(i == M) / count(i >= 1)
```

The submitted `asl_score` is the framework's `ASL_pow`, matching the supplied
package's `aslScore`. Semantic-weighted `ASL` is not reported. The conditional ASL
in `metrics.json` changes the denominator to initially solved tasks times M.
Matched comparisons include only task IDs that pass cycle 1 in both configurations.

## Failure review and costs

The audit contains 20 later failures (10 Llama pseudocode, five Llama standard,
five Qwen standard) and two Qwen pseudocode initial failures. It spans extension
failure cycles 2 through 10. It is a purposive sample; category counts are not
population prevalence estimates. Qwen pseudocode has no failures after cycle 1.
The worksheet records uncertainty when exact failing test inputs are not saved.

Read and verify the 22 cases before submission. The notes are AI-assisted, not a claim of completed independent human review. See
`AI_USAGE.md` for the review instruction and unavailable assistant metadata.

No auxiliary judge API was used. End-of-session OpenRouter key usage was
$0.294936364, including stopped runs and diagnostics. This is not an isolated
per-run or per-example cost measurement. It also excludes Codex billing, which
was unavailable. Supplied package similarity scores are not used in our metrics.

## Verification

The full source test suite passed: 100 passed and one optional plotting test
was skipped in the host environment. The container built successfully with
the captured dependency constraints. Offline container analysis reproduced
all numeric tables and the audit evidence byte for byte. The original
framework plots were also generated successfully for all four completed runs.
The patch was applied to a clean archive of the upstream base and matched
every changed source file.
