# AI assistance and author review

The evaluated models are `meta-llama/llama-3.1-8b-instruct` and
`qwen/qwen3.7-flash`. They perform both inverse tasks. Their prompts and inference
settings are in the fork, report, and README. Qwen reasoning is disabled in both
configurations. No separate similarity judge or classification API was run.

An OpenAI Codex coding assistant helped implement the extension, inspect outputs,
prepare proposed failure labels. The session identifies
the assistant as GPT-6-based; its exact served model identifier, sampling settings,
and billing were not exposed. These values are unavailable, not assumed to be
temperature zero or free. They are not included in the OpenRouter cost total.

The code-reading instruction used for the worksheet was:

> Compare each original task, last passing code, description fed into the failed
> cycle, and failing code. Use recorded base/plus outcomes. Propose one primary
> category: representation drift, generation error, syntax error, numeric type
> handling, or unresolved initial coverage gap. Identify the model, loop, task,
> and failed cycle. Distinguish observations from hypotheses. Do not execute
> generated code or infer an unrecorded failing input as fact.

The observations were reviewed in the coding session and entered as static
annotations in `failure_annotations.json`. `analyze_hw4.py` attaches those notes
to the exact saved records; it does not invoke an LLM, infer labels, or use labels
to change success rates or ASL. The audit sample is purposive rather than random.

The author must read `analysis/failure_review.md`, verify the proposed labels,
and own the analysis before submitting. This worksheet is AI-assisted evidence
for that manual review, not a claim that an independent human already completed
the review. This worksheet discloses this limitation. If the course treats
assistant-proposed labels as an auxiliary LLM classifier, the unavailable model
settings and cost must remain disclosed; no fabricated values are supplied.

For the actual evaluation API, the key reported $0.294936364 total usage at the
end. This includes aborted setup/GPT-OSS runs and response diagnostics. Per-run
and per-example token costs cannot be recovered exactly because the upstream
client did not persist usage for every response. That aggregate is an upper
estimate for included-run cost, not a sum of separately measured run costs.
