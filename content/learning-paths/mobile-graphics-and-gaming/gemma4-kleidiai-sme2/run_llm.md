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
same three-iteration benchmark at one and four CPU threads:

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
  local threads
  local result

  sdk_version="$(xcrun --sdk macosx --show-sdk-version)"

  cd "$root/LiteRT-LM"
  bazelisk --output_base="$output_base" build \
    --config=macos_arm64 \
    --macos_sdk_version="$sdk_version" \
    --override_repository=XNNPACK="$xnnpack_dir" \
    --override_repository=KleidiAI="$root/kleidiai" \
    //runtime/engine:litert_lm_advanced_main

  binary="$(bazelisk --output_base="$output_base" info bazel-bin)/runtime/engine/litert_lm_advanced_main"

  for threads in 1 4; do
    result="${variant}-${threads}t"

    "$binary" \
      --backend=cpu \
      --model_path="$model" \
      --benchmark \
      --benchmark_prefill_tokens=1024 \
      --benchmark_decode_tokens=256 \
      --max_num_tokens=4096 \
      --num_cpu_threads="$threads" \
      --disable_cache=true \
      --async=false \
      --num_iterations=3 \
      --report_peak_memory_footprint \
      --metric_proto_file_path="$root/results/${result}.pb" \
      2>&1 | tee "$root/results/${result}.log"
  done
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

The commands create separate logs and metric files for `baseline-1t`,
`baseline-4t`, `optimized-1t`, and `optimized-4t`.

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
  Time to first token: 7.14 s
--------------------------------------------------
  Prefill Turns (Total 1 turns):
    Prefill Turn 1: Processed 1024 tokens in 7.044162s duration.
      Prefill Speed: 145.37 tokens/sec.
--------------------------------------------------
  Decode Turns (Total 1 turns):
    Decode Turn 1: Processed 256 tokens in 23.268829s duration.
      Decode Speed: 11.00 tokens/sec.
--------------------------------------------------
```

Treat iteration 1 as a warm-up and compare the mean of iterations 2 and 3 for
each variant and thread count.

## Tested results on Apple M4

The following representative results use 1024 prefill tokens, 256 decode
tokens, and disabled caches. Frequency and thermal state were not fixed, so use
the values as a functional comparison.

| CPU threads | XNNPACK variant | Prefill tokens/s | Change | Decode tokens/s | Change |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | No SME2 kernels | 142.60 | - | 15.79 | - |
| 1 | SME2 Int4 and Int2 | 215.93 | +51.4% | 23.89 | +51.3% |
| 4 | No SME2 kernels | 411.70 | - | 37.04 | - |
| 4 | SME2 Int4 and Int2 | 562.92 | +36.7% | 30.28 | -18.3% |

### Interpret thread scaling

Prefill and decode expose different amounts of parallel work. Prefill processes
many prompt tokens together, so additional CPU threads can improve throughput.
Autoregressive decode generates one token at a time, and each token depends on
the preceding output. This dependency limits the work available to parallelize
within each decode step.

Decode also reads model weights and key-value (KV) cache data for every token.
As the thread count increases, threads compete for memory bandwidth and add
scheduling overhead. These costs can outweigh the available parallel work,
especially when the system exposes one matrix engine, known as a 1xCME
configuration.

The results illustrate this difference. SME2 improves prefill at both thread
counts. For decode, SME2 throughput increases from 23.89 tokens/s with one
thread to 30.28 tokens/s with four threads, but it scales less than the
non-SME2 path. The one-thread SME2 advantage of 51.3% therefore becomes an
18.3% deficit at four threads.

Results can
differ by model signature, SoC, operating system, memory conditions, and
thermal state.

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
