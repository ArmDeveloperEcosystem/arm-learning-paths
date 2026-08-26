---
title: Build and compare benchmarks
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build and benchmark one XNNPACK variant

Create directories for the shared Bazel output and benchmark results:

```bash
cd $HOME/gemma4-prefill-bench
mkdir -p bazel-output-base results
```

Define a shell function that builds one XNNPACK tree and immediately runs the
same three-iteration benchmark:

```bash
set -o pipefail

run_variant() {
  local variant="$1"
  local xnnpack_dir="$2"
  local root="$HOME/gemma4-prefill-bench"
  local output_base="$root/bazel-output-base/ab"
  local model="$root/models/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm"
  local sdk_version
  local binary

  sdk_version="$(xcrun --sdk macosx --show-sdk-version)"

  cd "$root/LiteRT-LM"
  bazelisk --output_base="$output_base" build \
    --config=macos_arm64 \
    --macos_sdk_version="$sdk_version" \
    --override_repository=XNNPACK="$xnnpack_dir" \
    --override_repository=KleidiAI="$root/kleidiai" \
    //runtime/engine:litert_lm_advanced_main

  binary="$(bazelisk --output_base="$output_base" info bazel-bin)/runtime/engine/litert_lm_advanced_main"

  "$binary" \
    --backend=cpu \
    --model_path="$model" \
    --benchmark \
    --benchmark_prefill_tokens=512 \
    --benchmark_decode_tokens=128 \
    --num_cpu_threads=4 \
    --disable_cache=true \
    --async=false \
    --num_iterations=3 \
    --report_peak_memory_footprint \
    --metric_proto_file_path="$root/results/${variant}.pb" \
    2>&1 | tee "$root/results/${variant}.log"
}
```

The first build compiles the full LiteRT-LM dependency graph. Reusing one
Bazel output base means that changing the XNNPACK override rebuilds only the
affected actions for later variants.

Run the historical baseline and the upstream-optimized variant:

```bash
run_variant baseline "$HOME/gemma4-prefill-bench/xnnpack-baseline"
run_variant optimized "$HOME/gemma4-prefill-bench/xnnpack"
```

{{% notice Note %}}
Use `--disable_cache=true` for the A/B comparison. The tested Gemma 4 artifact
contains XNNPACK weight-cache fingerprints that are recognized by the upstream
optimized tree but not by the historical baseline. Enabling caches therefore
makes initialization time and memory use non-comparable.
{{% /notice %}}

## Read the benchmark output

Each iteration prints output similar to:

```output
--------------------------------------------------
  Time to first token: 0.43 s
--------------------------------------------------
  Prefill Turns (Total 1 turns):
    Prefill Turn 1: Processed 512 tokens in 399.049292ms duration.
      Prefill Speed: 1283.05 tokens/sec.
--------------------------------------------------
  Decode Turns (Total 1 turns):
    Decode Turn 1: Processed 128 tokens in 4.037520542s duration.
      Decode Speed: 31.70 tokens/sec.
--------------------------------------------------
```

Treat iteration 1 as a warm-up and compare the mean of iterations 2 and 3.

## Tested results on Apple M4 Pro

The following results were measured on a 12-core Apple M4 Pro with 24 GB of
RAM, macOS SDK 26.5, four CPU threads, and caches disabled. Frequency and
thermal state were not fixed, so use the values as a functional comparison.

| XNNPACK variant | Prefill tokens/s | Change | Decode tokens/s | Change |
| --- | ---: | ---: | ---: | ---: |
| Historical baseline | 930.57 | - | 54.78 | - |
| Upstream SME2 Int4 and Int2 | 1263.22 | +35.7% | 29.76 | -45.7% |

On this system, the upstream SME2 paths provide a clear prefill improvement but
regress decode for the four-thread workload. Results can differ by model
signature, thread count, SoC, operating system, and thermal state. Measure
prefill and decode separately for your target workload.

## Run a prompt sanity check

After building a variant, use its generated binary for a short prompt:

```bash
binary="$(bazelisk --output_base="$HOME/gemma4-prefill-bench/bazel-output-base/ab" info bazel-bin)/runtime/engine/litert_lm_advanced_main"

"$binary" \
  --backend=cpu \
  --model_path="$HOME/gemma4-prefill-bench/models/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm" \
  --input_prompt="What is the capital of France?" \
  --max_output_tokens=16 \
  --num_cpu_threads=4 \
  --async=false
```

The tested model answers that the capital of France is Paris.
