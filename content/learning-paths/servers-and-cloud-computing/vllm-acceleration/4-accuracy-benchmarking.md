---
title: Evaluate accuracy with LM Evaluation Harness
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why accuracy benchmarking

The lm-evaluation-harness is the standard way to measure model accuracy across common academic benchmarks (for example, MMLU, HellaSwag, GSM8K) and runtimes (such as Hugging Face, vLLM, and llama.cpp). In this section, you'll run accuracy tests for both BF16 and INT4 deployments of your model served by vLLM on Arm-based servers.

You will:
  * Install lm-eval-harness with vLLM support
  * Run benchmarks on a BF16 model and an INT4 (weight-quantized) model
  * Interpret key metrics and compare quality across precisions

{{% notice Note %}}
Results vary based on your CPU, dataset version, and model selection. For a fair comparison between BF16 and INT4, always use the same tasks and few-shot settings.
{{% /notice %}}


## Prerequisites

Before you start:
  * Complete the optimized build in “Overview and Optimized Build” and validate your vLLM install.
  * Optionally quantize a model using the “Quantize an LLM to INT4 for Arm Platform” module. We’ll reference the output directory name from that step.

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
`LD_PRELOAD` uses TCMalloc to reduce allocator contention. Install it via `sudo apt-get install -y libtcmalloc-minimal4` if you haven’t already.
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

## Benchmark INT4 quantized model accuracy

Run accuracy tests on your INT4 quantized model using the same tasks and settings as the BF16 baseline. Replace the model path with your quantized output directory.

```bash
lm_eval \
  --model vllm \
  --model_args \
    pretrained=Meta-Llama-3.1-8B-Instruct-w4a8dyn-mse-channelwise,dtype=float32,max_model_len=4096,enforce_eager=True \
  --tasks mmlu,hellaswag \
  --batch_size auto \
  --output_path results
```

The expected output includes per-task accuracy metrics. Compare these results to your BF16 baseline to evaluate the impact of INT4 quantization on model quality.

Use the INT4 quantization recipe & script from previous steps to quantize `meta-llama/Meta-Llama-3.1-8B-Instruct` model.

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

## Interpret the results

The harness prints per-task and aggregate scores (for example, `acc`, `acc_norm`, `exact_match`). Higher is generally better. Compare BF16 vs INT4 on the same tasks to assess quality impact.

Practical tips:
  * Use the same tasks and few-shot settings across runs.
  * For quick iteration, you can add `--limit 200` to run on a subset.

## Explore example results for Meta‑Llama‑3.1‑8B‑Instruct model

These illustrative results are representative; actual scores may vary across hardware, dataset versions, and harness releases. Higher values indicate better accuracy.

| Variant                         | MMLU (acc±err)    | HellaSwag (acc±err) |
|---------------------------------|-------------------|---------------------|
| BF16                            | 0.5897 ± 0.0049   | 0.7916 ± 0.0041     |
| INT4 Groupwise minmax (G=32)    | 0.5831 ± 0.0049   | 0.7819 ± 0.0041     |
| INT4 Channelwise MSE            | 0.5712 ± 0.0049   | 0.7633 ± 0.0042     |

Use these as ballpark expectations to check whether your runs are in a reasonable range, not as official targets.

## Next steps

Now that you've completed accuracy benchmarking for both BF16 and INT4 models on Arm-based servers, you're ready to deepen your evaluation and optimize for your specific use case. Expanding your benchmarks to additional tasks helps you understand model performance across a wider range of scenarios. Experimenting with different quantization recipes lets you balance accuracy and throughput for your workload.

- Try additional tasks to match your use case: `gsm8k`, `winogrande`, `arc_easy`, `arc_challenge`.
- Sweep quantization recipes (minmax vs mse; channelwise vs groupwise, group size) to find a better accuracy/performance balance.
- Record both throughput and accuracy to choose the best configuration for your workload.

You've learned how to set up lm-evaluation-harness, run benchmarks for BF16 and INT4 models, and interpret key accuracy metrics on Arm platforms. 

Your results will help you make informed decisions about model deployment and optimization.
