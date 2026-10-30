---
title: Ask the agent to benchmark TinyStories
description: Describe a TinyStories CPU comparison in natural language and let the agent select stable tools, verify Arm optimizations, report uplift, and release the phone.
weight: 5
layout: learningpathall
---

## Ask for an Arm performance comparison

Use the connected phone to explore how Arm optimizations affect a small language model's inference performance. TinyStories keeps the experiment small enough to build and run on the phone inside Termux, an Android terminal environment. KleidiAI provides optimized Arm CPU kernels that llama.cpp can use for inference.

Continue in the same agent conversation and give it the second prompt:

```text
On our DDP phone, compare a small TinyStories model's CPU inference
with and without Arm KleidiAI optimizations using the latest stable
Termux and llama.cpp releases. Check output agreement and which Arm
kernels actually run, including SVE/SVE2 where usable. Repeat with
the same model and settings, and report prompt-processing and
token-generation uplift. Save the results locally and release the
phone within our approved limits.
```

The prompt gives the agent the workload, comparison, and expected result. It can choose compatible software and model files, prepare the phone, and collect the measurements. You can use it after the connection prompt without attaching these pages or copying version numbers and build settings into the conversation.

## Let the agent prepare and run the experiment

The agent should obtain the latest stable releases from the official [Termux releases](https://github.com/termux/termux-app/releases/latest) and [llama.cpp releases](https://github.com/ggml-org/llama.cpp/releases/latest), then install the tools and build and run the workload on the phone. It records the versions it selected in the saved report so you can revisit the experiment later.

The Arm feature check is part of that work. The agent needs to establish which optimizations the phone exposes, which ones the selected model and runtime can use, and which kernels actually execute. If SVE or SVE2 isn't usable for that combination, it should explain the reason and identify the compatible path it measured.

For a fair comparison, the agent should keep the model, quantization, inputs, thread count, and CPU placement the same, with GPU offload disabled. It should check output agreement before timing and use repeated, warmed-up measurements. You can review the resulting comparison without choosing compiler flags, kernel dispatch settings, or numerical tolerances yourself.

## Review the performance report

Look for separate results for prompt processing and token generation. The report should show the baseline and optimized throughput, the uplift, and the variation across measurements. Check the agent's explanation of the kernels responsible for the result, including any fallback or regression.

The following reference results were measured on November 5, 2026, on a physical Pixel 11 with Tensor G6 and Android 17 (API 37). Each value is the median of five alternating measurement pairs, using the same TinyStories Q4_0 model and one CPU thread:

| Workload | CPU baseline, tokens/s | KleidiAI, tokens/s | Speedup | Throughput uplift |
| --- | ---: | ---: | ---: | ---: |
| Prompt processing, 64 tokens | 4,833.49 | 9,925.77 | 2.05× | +105.4% |
| Token generation, 32 tokens | 1,029.68 | 1,375.95 | 1.34× | +33.6% |

Higher tokens per second is better. Calculate `speedup = optimized / baseline` and `throughput uplift (%) = 100 × (speedup − 1)` from the median throughput for each path. These results measure warmed-up inference and exclude model loading and initial weight packing.

{{% notice Note %}}
These measurements come from a reference run with the versions and settings recorded in the saved evidence. Your agent selects the latest stable releases and a compatible model for your run, so its results can differ.
{{% /notice %}}

In the reference run, the phone exposed SVE and SVE2 with a 128-bit vector length, while that runtime's KleidiAI SVE kernels required 256-bit vectors. The verified path used Neon I8MM matrix-multiplication kernels and Neon dot-product matrix-vector kernels. The uplift in the table is for that KleidiAI path. It doesn't establish an SVE2 performance gain.

The baseline retained its normal Arm CPU optimizations. All eight output test prompts passed the agreed smoke check; this limited check doesn't establish equivalent model quality.

Download the [reference measurements and validation evidence](../files/benchmark-results-2026-11-05.json) to inspect the recorded software versions, model identity, build settings, raw samples, output checks, and kernel trace counts. You only need these details if you want to examine or reproduce that particular run.

## Confirm the results are saved and the phone is released

The prompt includes saving the results and releasing the phone. Check that the agent gives you a readable local report with the measurements, device details, software versions, and kernel evidence.

The agent should cancel the recorded DDP session, confirm that its cloud state is `FINISHED` or `EXPIRED`, and close the viewer and connection. Closing a window alone doesn't stop device-time billing. If the task stops early, ask the agent to release the session and verify that it has ended.

## What you've accomplished

You've used natural language to connect to remote Arm hardware and investigate a performance question. The agent handled device access, software selection, setup, kernel checks, measurement, and cleanup. You chose the task and spending limits, then reviewed the screen, results, and explanation.
