---
title: Review benchmark results
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

These benchmarks focus on serving performance only. They compare request throughput, output token throughput, TTFT, and TPOT across BF16 and INT8/W8A8 runs.

Model quality and accuracy are out of scope for this Learning Path and were not evaluated in this benchmark pass.

This section summarizes the ShareGPT ~512 input-token benchmark results. The benchmark requested 512 output tokens and used `vllm bench serve`.

## Gemma4 BF16 MoE

Gemma4 was benchmarked with ShareGPT ~512 input-token prompt subsets.

The optimized BF16 MoE path improves Gemma4 request throughput by around `3.25x` to `3.80x`, depending on concurrency.

| Prompt subset | Req/s speedup | Output tok/s speedup | Mean TPOT reduction |
| --- | ---: | ---: | ---: |
| ShareGPT ~512 input tokens | 3.25x - 3.80x | 3.15x - 3.83x | 68% - 74% |

This shows that the optimized BF16 MoE kernels significantly improve Gemma4 token generation performance on Arm CPUs.

## GPT-OSS BF16 MoE

GPT-OSS was benchmarked with ShareGPT ~512 input-token prompt subsets.

The optimized BF16 MoE path improves GPT-OSS request throughput by around `2.80x` to `3.62x`, depending on concurrency.

| Prompt subset | Req/s speedup | Output tok/s speedup | Mean TPOT reduction |
| --- | ---: | ---: | ---: |
| ShareGPT ~512 input tokens | 2.80x - 3.62x | 2.74x - 3.50x | 64% - 72% |

GPT-OSS required additional Harmony/tiktoken setup during benchmarking.

## Qwen3 BF16 and INT8/W8A8 MoE

The Qwen3 comparison uses pre-optimization BF16 as the baseline. The comparison includes:

- Pre-optimization Qwen BF16 baseline
- New optimized Qwen BF16
- New Qwen INT8/W8A8

| Prompt subset | New BF16 vs pre-optimization BF16 | INT8/W8A8 vs pre-optimization BF16 | INT8/W8A8 vs new BF16 |
| --- | ---: | ---: | ---: |
| ShareGPT ~512 input tokens | 3.25x - 4.83x | 4.25x - 7.00x | 1.31x - 1.45x |

Mean TPOT is also lower with INT8/W8A8 than with optimized BF16.

This shows two improvements:

- BF16 MoE optimization improves regular BF16 MoE models.
- INT8/W8A8 MoE support provides an additional optimized path compared with BF16.

## Plots

The following plots show relative speedups for the ShareGPT ~512 input-token subset with 512 requested output tokens.

### Gemma4 BF16 before and after optimization

![Gemma4 BF16 speedup for ShareGPT 512](images/gemma4_512_new.png)

### GPT-OSS BF16 before and after optimization

![GPT-OSS BF16 speedup for ShareGPT 512](images/gptoss_512_new.png)

### Qwen3 BF16 and INT8/W8A8 comparison

![Qwen3 BF16 and INT8/W8A8 speedup for ShareGPT 512](images/qwen_512_new.png)

## What you've accomplished

You've now reviewed the benchmark results for BF16 and INT8/W8A8 MoE inference with vLLM on Arm CPUs.

The results show that BF16 MoE optimization improves regular MoE model serving performance, and that INT8/W8A8 MoE support provides an additional optimized serving path compared with BF16.