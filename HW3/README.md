# Assignment 3: Quantization Robustness

This notebook evaluates whether quantizing **Qwen2.5-Coder-1.5B-Instruct** changes its accuracy and robustness on Python code-generation tasks. The full results, examples, plots, and discussion are in the notebook.

## How to run

Open `A3_Quantization_Robustness.ipynb` in Google Colab with a GPU runtime (the full run used an NVIDIA L4). Run all cells in order with `QUICK = False` to evaluate all 164 HumanEval problems. The notebook downloads the benchmark files, creates the GPTQ checkpoint, runs the evaluations, and displays the results. Intermediate generations are cached under `/content/csc591-a3`, which is temporary Colab storage.

The saved run used PyTorch `2.11.0+cu130`, Transformers `5.17.0`, bitsandbytes `0.50.2`, llmcompressor `0.14.0`, and compressed-tensors `0.19.0`. The setup cell installs the main dependencies.

## Implementation

- **Model loading (TODO 1a):** `load_model` handles FP16, bitsandbytes INT8 (`LLM.int8()`), bitsandbytes 4-bit NF4 with FP16 computation, and the saved GPTQ4 checkpoint. Each model is loaded for inference on the GPU.
- **GPTQ (TODO 1b):** `build_calibration_set` uses the first **256** training examples from [`theblackcat102/evol-codealpaca-v1`](https://huggingface.co/datasets/theblackcat102/evol-codealpaca-v1), formatted as user-assistant conversations and truncated to **512 tokens**. Coding examples were chosen to match the model's task; no HumanEval or ReCode evaluation data was used for calibration. `run_gptq` uses llmcompressor's `GPTQModifier` with **W4A16**, **group size 128**, and `lm_head` excluded. Calibration loads the model in FP32 to reduce numerical issues. The compressed checkpoint and tokenizer are saved, and a warning check detects excessive GPTQ fallback.
- **ReCode metrics (TODO 3):** `recode_metrics` computes robust pass@1, robust drop, robust relative (changed pass/fail outcomes), and conditional robustness among nominally solved tasks. `family_worst_case` requires each problem to pass both transformations in a family.
- **EVALOOOP (TODO 4a):** `run_evaloop` first generates a solution from the original prompt. For each later loop, it strips the prior docstring, asks the model to describe its code, rebuilds the prompt from that description, and regenerates and tests the solution. Only consecutively passing problems continue. `asl` averages the number of loops each problem survives.
- **Statistics (TODO 5):** `bootstrap_ci` uses **10,000 bootstrap samples** for a 95% confidence interval. `paired_compare` compares each quantized model against FP16 on the same tasks, reporting discordant outcomes, the paired pass-rate difference, an exact McNemar p-value, and a bootstrap confidence interval for the difference.

## Benchmark protocol and changes

- **E0:** Clean pass@1 on both standard HumanEval and partial-code HumanEval, using greedy decoding and at most 512 new tokens.
- **E1 (ReCode):** Uses the assignment's fixed subset rather than all ReCode variants: **two transformations per family**, one seed (seed 0), across docstring, function-name, syntax, and formatting perturbations. Docstring and function-name variants are compared with standard HumanEval; syntax and formatting variants use the partial-code nominal set. We also calculate conditional robustness and family worst-case results to avoid misleading comparisons when clean accuracy differs.
- **E2 (EVALOOOP):** **Implemented and run**, using HumanEval instead of the paper's MBPP+ and **3 loops instead of 10**. Three loops keep evaluation practical under greedy decoding, which can cause repeated outputs and early fixed points. The resulting ASL is therefore not directly comparable to the paper's full protocol.
- **E3 (Sclar et al. prompt-template sensitivity):** **Not run**. The assignment requires E2 or E3; E2 was selected. No claim is made to reproduce the Sclar et al. protocol.

## AI assistance

I used **ChatGPT (OpenAI, GPT-6)** to help implement the TODO functions, understand GPTQ and the evaluation metrics, troubleshoot notebook execution, interpret results and flipped examples, and draft parts of the report and this README. I ran the experiments in Google Colab and reviewed the code and results. The notebook contains the actual experimental outputs and analysis.
