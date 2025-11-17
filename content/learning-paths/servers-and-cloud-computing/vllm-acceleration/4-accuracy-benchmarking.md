---
title: Evaluate Accuracy with LM Evaluation Harness
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why accuracy benchmarking

The LM Evaluation Harness (lm-eval-harness) is a widely used open-source framework for evaluating the accuracy of large language models on standardized academic benchmarks such as MMLU, HellaSwag, and GSM8K.
It provides a consistent interface for evaluating models served through various runtimes—such as Hugging Face Transformers, vLLM, or llama.cpp using the same datasets, few-shot templates, and scoring metrics.
In this module, you will measure how quantization impacts model quality by comparing BF16 (non-quantized) and INT4 (quantized) versions of your model running on Arm-based servers.

You will:
  * Install lm-eval-harness with vLLM backend support.
  * Run benchmark tasks on both BF16 and INT4 model deployments.
  * Analyze and interpret accuracy differences between the two precisions.

{{% notice Note %}}
Accuracy results can vary depending on CPU, dataset versions, and model choice. Use the same tasks, few-shot settings and evaluation batch size when comparing BF16 and INT4 results to ensure a fair comparison.
{{% /notice %}}

## Prerequisites

Before you begin, make sure your environment is ready for evaluation.
You should have:
  * Completed the optimized build from the “Overview and Optimized Build” section and successfully validated your vLLM installation.
  * (Optional) Quantized a model using the “Quantize an LLM to INT4 for Arm Platform” module.
  The quantized model directory (for example, DeepSeek-V2-Lite-w4a8dyn-mse-channelwise) will be used as input for INT4 evaluation.
If you haven’t quantized a model, you can still evaluate your BF16 baseline to establish a reference accuracy.

## Install lm-eval-harness

Install the harness with vLLM extras in your active Python environment:

```bash
pip install "lm_eval[vllm]"
pip install ray
```

{{% notice Tip %}}
If your benchmarks include gated models or datasets, run `huggingface-cli login` first so the harness can download what it needs.
{{% /notice %}}

## Recommended runtime settings for Arm CPU

Export the same performance-oriented environment variables used for serving. These enable Arm-optimized kernels through oneDNN+ACL and consistent thread pinning:

```bash
export VLLM_TARGET_DEVICE=cpu
export VLLM_CPU_KVCACHE_SPACE=32
export VLLM_CPU_OMP_THREADS_BIND="0-$(($(nproc)-1))"
export VLLM_MLA_DISABLE=1
export ONEDNN_DEFAULT_FPMATH_MODE=BF16
export OMP_NUM_THREADS="$(nproc)"
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libtcmalloc_minimal.so.4
```

{{% notice Note %}}
`LD_PRELOAD` uses tcmalloc to reduce allocator contention. Install it via `sudo apt-get install -y libtcmalloc-minimal4` if you haven’t already.
{{% /notice %}}

## Accuracy Benchmarking Meta‑Llama‑3.1‑8B‑Instruct BF16 model

Run with a non-quantized model. Replace the model ID as needed.

```bash
lm_eval \
  --model vllm \
  --model_args \
    pretrained=meta-llama/Meta-Llama-3.1-8B-Instruct,dtype=bfloat16,max_model_len=4096,enforce_eager=True \
  --tasks mmlu,hellaswag \
  --batch_size auto \
  --output_path results
```

## Accuracy Benchmarking INT4 quantized model

Use the INT4 quantization recipe & script from previous steps to quantize `meta-llama/Meta-Llama-3.1-8B-Instruct` model

Channelwise INT4 (MSE):

```bash
lm_eval \
  --model vllm \
  --model_args \
    pretrained=Meta-Llama-3.1-8B-Instruct-w4a8dyn-mse-channelwise,dtype=float32,max_model_len=4096,enforce_eager=True \
  --tasks mmlu,hellaswag \
  --batch_size auto \
  --output_path results
```

## Interpreting results

The harness prints per-task and aggregate scores (for example, `acc`, `acc_norm`, `exact_match`). Higher is generally better. Compare BF16 vs INT4 on the same tasks to assess quality impact.

Practical tips:
  * Use the same tasks and few-shot settings across runs.
  * For quick iteration, you can add `--limit 200` to run on a subset.

## Example results for Meta‑Llama‑3.1‑8B‑Instruct model

These illustrative results are representative; actual scores may vary across hardware, dataset versions, and harness releases. Higher values indicate better accuracy.

| Variant                         | MMLU (acc±err)    | HellaSwag (acc±err) |
|---------------------------------|-------------------|---------------------|
| BF16                            | 0.5897 ± 0.0049   | 0.7916 ± 0.0041     |
| INT4 Groupwise minmax (G=32)    | 0.5831 ± 0.0049   | 0.7819 ± 0.0041     |
| INT4 Channelwise MSE            | 0.5712 ± 0.0049   | 0.7633 ± 0.0042     |

Use these as ballpark expectations to check whether your runs are in a reasonable range, not as official targets.

## Next steps

  * Try additional tasks to match your usecase: `gsm8k`, `winogrande`, `arc_easy`, `arc_challenge`.
  * Sweep quantization recipes (minmax vs mse; channelwise vs groupwise, group size) to find a better accuracy/performance balance.
  * Record both throughput and accuracy to choose the best configuration for your workload.
