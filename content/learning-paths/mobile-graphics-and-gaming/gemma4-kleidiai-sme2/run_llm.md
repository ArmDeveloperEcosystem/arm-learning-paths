---
title: Build and compare benchmarks on macOS
description: Build baseline and optimized XNNPACK variants on macOS and compare Gemma 4 prefill and decode throughput.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build and benchmark one XNNPACK variant

Create directories for the shared Bazel output and benchmark results:

```bash
cd $HOME/gemma4-prefill-bench
mkdir -p bazel-output-base bin results
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
    --define=xnn_enable_arm_sme2=true \
    --define=xnn_enable_kleidiai=true \
    --override_repository=XNNPACK="$xnnpack_dir" \
    --override_repository=KleidiAI="$root/kleidiai" \
    //runtime/engine:litert_lm_advanced_main || return

  binary="$root/bin/litert_lm_advanced_main-${variant}-macos"
  cp -L bazel-bin/runtime/engine/litert_lm_advanced_main "$binary" || return

  for threads in 1 4; do
    result="${variant}-${threads}t"

    DYLD_LIBRARY_PATH="$root/LiteRT-LM/prebuilt/macos_arm64" "$binary" \
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
      2>&1 | tee "$root/results/${result}.log" || return
  done
}
```

The first build can take several minutes. `DYLD_LIBRARY_PATH` points each saved
binary to LiteRT-LM's matching Gemma constraint-provider library.

Run the baseline and optimized builds:

```bash
run_variant baseline "$HOME/gemma4-prefill-bench/xnnpack-baseline"
run_variant optimized "$HOME/gemma4-prefill-bench/xnnpack"
```

Each run writes its log and metrics to `results/`. Keep caches disabled and
other applications idle when comparing the builds.

## Compare prefill and decode

Read `Prefill Speed` and `Decode Speed` in tokens per second. Discard the first
iteration as warm-up, then average iterations 2 and 3 for each build and thread
count. Calculate the changes separately:

```text
throughput change (%) = 100 * (optimized throughput / baseline throughput - 1)
```

A positive value means higher throughput; a negative value is a regression.
Prefill and decode scale differently, so compare both phases at both thread
counts.

{{% notice Note %}}
If you see `Failed to get prefill profile summary` or its decode equivalent with
profiling disabled, check that all three iterations finish and the command exits
successfully. Collect operator profiles separately to avoid timing overhead.
{{% /notice %}}

## Compare two device examples

These examples use LiteRT-LM v0.16.1 and KleidiAI v1.31.0 with the same model
and benchmark settings: 1,024 prefill tokens, 256 decode tokens, and disabled
caches and profiling. Values are the mean of iterations 2 and 3; percentage
changes compare the optimized build with the baseline.

| Device | CPU threads | Prefill tokens/s | Prefill change | Decode tokens/s | Decode change |
| --- | ---: | ---: | ---: | ---: | ---: |
| Apple M4 Pro | 1 | 137.79 | −3.4% | 17.40 | +53.6% |
| Apple M4 Pro | 4 | 458.62 | +0.3% | 25.91 | +12.8% |
| Xiaomi 2608BPX34C | 1 | 75.35 | +16.3% | 10.10 | +44.5% |
| Xiaomi 2608BPX34C | 4 | 240.86 | +2.0% | 17.54 | +4.2% |

The Mac uses unrestricted CPU scheduling; Android uses CPUs 4–7. Frequencies
aren't fixed. The small Mac prefill changes and Android four-thread changes are
within observed run variation, so results will vary by device and conditions.

In a separate Android comparison, enabling SME2 improves four-thread prefill by
53.7% and lowers decode by 9.1%. That comparison includes all SME2 kernels;
the table isolates the static INT2 addition.

{{% notice Note %}}
For Android, you also need an SME2-capable phone, the Android SDK, NDK r28b or
newer, and an authorized `adb` connection. Follow the
[Android SME2 development setup](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#android-sme2).
Set `ANDROID_HOME` and `ANDROID_NDK_HOME`, then use `--config=android_arm64` with
the same repository overrides. Copy the Android binary, model, and
`prebuilt/android_arm64/libGemmaModelConstraintProvider.so` to the device.
Run from that directory with `LD_LIBRARY_PATH=.` and choose a valid CPU mask
with `taskset`.
{{% /notice %}}

## Check the output and accelerated operator

After building a variant, use its generated binary for a short prompt:

```bash
root="$HOME/gemma4-prefill-bench"
binary="$root/bin/litert_lm_advanced_main-optimized-macos"
model="$root/models/gemma-4-E2B-it-litert-lm/gemma-4-E2B-it.litertlm"

DYLD_LIBRARY_PATH="$root/LiteRT-LM/prebuilt/macos_arm64" "$binary" \
  --backend=cpu --model_path="$model" \
  --input_prompt="What is the capital of France?" \
  --max_output_tokens=16 --num_cpu_threads=4 \
  --disable_cache=true --async=false
```

Confirm that the answer identifies Paris. Collect operator evidence with a
separate short benchmark:

```bash
DYLD_LIBRARY_PATH="$root/LiteRT-LM/prebuilt/macos_arm64" "$binary" \
  --backend=cpu --model_path="$model" --benchmark \
  --benchmark_prefill_tokens=128 --benchmark_decode_tokens=8 \
  --max_num_tokens=4096 --num_cpu_threads=1 --num_iterations=1 \
  --disable_cache=true --async=false --enable_profiling=true
```

Look for `Fully Connected (NC, PQS8, QC2W)` in the summary to confirm that the
static INT2 SME2 path ran. Keep profiling disabled for timed measurements.

You've benchmarked both builds on macOS, compared prefill and decode, and
verified the accelerated operator. Use the same settings when testing another
SME2 device.
