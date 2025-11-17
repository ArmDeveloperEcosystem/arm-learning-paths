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

## Install LM Evaluation Harness

You will install the LM Evaluation Harness with vLLM backend support, allowing direct evaluation against your running vLLM server.

Install it inside your active Python environment:

```bash
pip install "lm_eval[vllm]"
pip install ray
```

{{% notice Tip %}}
If your benchmarks include gated models or restricted datasets, run `huggingface-cli login`
This ensures the harness can authenticate with Hugging Face and download any protected resources needed for evaluation.
{{% /notice %}}

## Recommended Runtime Settings for Arm CPU

Before running accuracy benchmarks, export the same performance tuned environment variables you used for serving.
These settings ensure vLLM runs with Arm-optimized kernels (via oneDNN + Arm Compute Library) and consistent thread affinity across all CPU cores during evaluation.

```bash
export VLLM_TARGET_DEVICE=cpu
export VLLM_CPU_KVCACHE_SPACE=32
export VLLM_CPU_OMP_THREADS_BIND="0-$(($(nproc)-1))"
export VLLM_MLA_DISABLE=1
export ONEDNN_DEFAULT_FPMATH_MODE=BF16
export OMP_NUM_THREADS="$(nproc)"
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libtcmalloc_minimal.so.4
```

Explanation of settings

| Variable                                            | Purpose                                                                                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **`VLLM_TARGET_DEVICE=cpu`**                        | Forces vLLM to run entirely on CPU, ensuring evaluation results use Arm-optimized oneDNN kernels.                            |
| **`VLLM_CPU_KVCACHE_SPACE=32`**                     | Reserves 32 GB for key/value caches used in attention. Adjust if evaluating with longer contexts or larger batches.          |
| **`VLLM_CPU_OMP_THREADS_BIND="0-$(($(nproc)-1))"`** | Pins OpenMP worker threads to physical cores (0–N-1) to minimize OS thread migration and improve cache locality.             |
| **`VLLM_MLA_DISABLE=1`**                            | Disables GPU/MLA probing for faster initialization in CPU-only mode.                                                         |
| **`ONEDNN_DEFAULT_FPMATH_MODE=BF16`**               | Enables **bfloat16** math mode, using reduced precision operations for faster compute while maintaining numerical stability. |
| **`OMP_NUM_THREADS="$(nproc)"`**                    | Uses all available CPU cores to parallelize matrix multiplications and attention layers.                                     |
| **`LD_PRELOAD`**                                    | Preloads **tcmalloc** (Thread-Caching Malloc) to reduce memory allocator contention under high concurrency.                  |

{{% notice Note %}}
tcmalloc helps reduce allocator overhead when running multiple evaluation tasks in parallel.
If it’s not installed, add it with `sudo apt-get install -y libtcmalloc-minimal4`
{{% /notice %}}

## Accuracy Benchmarking Meta‑Llama‑3.1‑8B‑Instruct (BF16 Model)

To establish a baseline accuracy reference, evaluate a non-quantized BF16 model served through vLLM.
This run measures how the original model performs under Arm-optimized BF16 inference before applying INT4 quantization.
Replace the model ID if you are using a different model variant or checkpoint.

```bash
lm_eval \
  --model vllm \
  --model_args \
    pretrained=meta-llama/Meta-Llama-3.1-8B-Instruct,dtype=bfloat16,max_model_len=4096,enforce_eager=True \
  --tasks mmlu,hellaswag \
  --batch_size auto \
  --output_path results
```
After completing this test, review the results directory for accuracy metrics (e.g., acc_norm, acc) and record them as your BF16 baseline.

Next, you’ll run the same benchmarks on the INT4 quantized model to compare accuracy across precisions.

## Accuracy Benchmarking: INT4 quantized model

Now that you’ve quantized your model using the INT4 recipe and script from the previous module, you can benchmark its accuracy using the same evaluation harness and task set.
This test compares quantized (INT4) performance against your BF16 baseline, revealing how much accuracy is preserved after compression.
Use the quantized directory generated earlier, for example:
Meta-Llama-3.1-8B-Instruct-w4a8dyn-mse-channelwise.

```bash
lm_eval \
  --model vllm \
  --model_args \
    pretrained=Meta-Llama-3.1-8B-Instruct-w4a8dyn-mse-channelwise,dtype=float32,max_model_len=4096,enforce_eager=True \
  --tasks mmlu,hellaswag \
  --batch_size auto \
  --output_path results
```
After this evaluation, compare the results metrics from both runs:

## Interpreting results

After running evaluations, the LM Evaluation Harness prints per-task and aggregate metrics such as acc, acc_norm, and exact_match.
These represent model accuracy across various datasets and question formats—higher values indicate better performance.
Key metrics include:
  * acc – Standard accuracy (fraction of correct predictions).
  * acc_norm – Normalized accuracy; adjusts for multiple-choice imbalance.
  * exact_match – Strict string-level match, typically used for reasoning or QA tasks.

Compare BF16 and INT4 results on identical tasks to assess the accuracy–efficiency trade-off introduced by quantization.
Practical tips:
  * Always use identical tasks, few-shot settings, and seeds across runs to ensure fair comparisons.
  * Add --limit 200 for quick validation runs during tuning. This limits each task to 200 samples for faster iteration.

## Example results for Meta‑Llama‑3.1‑8B‑Instruct model

The following results are illustrative and serve as reference points.
Your actual scores may differ based on hardware, dataset version, or lm-eval-harness release.

| Variant                         | MMLU (acc±err)    | HellaSwag (acc±err) |
|---------------------------------|-------------------|---------------------|
| BF16                            | 0.5897 ± 0.0049   | 0.7916 ± 0.0041     |
| INT4 Groupwise minmax (G=32)    | 0.5831 ± 0.0049   | 0.7819 ± 0.0041     |
| INT4 Channelwise MSE            | 0.5712 ± 0.0049   | 0.7633 ± 0.0042     |

How to interpret:

  * BF16 baseline – Represents near-FP32 accuracy; serves as your quality reference.
  * INT4 Groupwise minmax – Retains almost all performance while reducing model size ~4× and improving throughput substantially.
  * INT4 Channelwise MSE – Slightly lower accuracy, often within 2–3 percentage points of BF16, still competitive for most production use cases.

## Next steps

  * Broaden accuracy testing to cover reasoning, math, and commonsense tasks that reflect your real-world use cases:
GSM8K – Arithmetic and logical reasoning (sensitive to quantization).
Winogrande – Commonsense and pronoun disambiguation.
ARC-Easy / ARC-Challenge – Science and multi-step reasoning questions.
Running multiple benchmarks gives a more comprehensive picture of model robustness under different workloads.

  * Experiment with different quantization configurations to find the best accuracy–throughput trade-off for your hardware. 
  * Record both throughput and accuracy to choose the best configuration for your workload.

By iterating on these steps, you will build a custom performance and accuracy profile for your Arm deployment, helping you select the optimal quantization strategy and runtime configuration for your target workload.
