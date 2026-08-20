---
title: Build and run benchmarks
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Build LiteRT-LM with local XNNPACK and KleidiAI

Build the SME2-enabled benchmark binary from the LiteRT-LM repository:

```bash
cd $HOME/gemma4-prefill-bench/LiteRT-LM
bazel build \
    --config=macos_arm64 \
    --define=xnn_enable_arm_sme=true \
    --define=xnn_enable_arm_sme2=true \
    --define=xnn_enable_kleidiai=true \
    --macos_sdk_version="$(xcrun --sdk macosx --show-sdk-version)" \
    --override_repository=XNNPACK=../xnnpack \
    --override_repository=KleidiAI=../kleidiai \
    //runtime/engine:litert_lm_advanced_main

cp bazel-bin/runtime/engine/litert_lm_advanced_main \
   ./litert_lm_advanced_main_sme2_on
```

Build a second binary with KleidiAI SME and SME2 paths disabled so you can compare the same workload against the XNNPACK fallback on the same machine:

```bash
bazel build \
    --config=macos_arm64 \
    --define=xnn_enable_arm_sme=false \
    --define=xnn_enable_arm_sme2=false \
    --define=xnn_enable_kleidiai=false \
    --macos_sdk_version="$(xcrun --sdk macosx --show-sdk-version)" \
    --override_repository=XNNPACK=../xnnpack \
    --override_repository=KleidiAI=../kleidiai \
    //runtime/engine:litert_lm_advanced_main

cp bazel-bin/runtime/engine/litert_lm_advanced_main \
   ./litert_lm_advanced_main_sme2_off
```

{{% notice Note %}}
TODO before publication: rerun both binaries on the final pinned upstream XNNPACK and KleidiAI commits, then replace the sample benchmark output with measured Gemma 4 numbers from the same SME2-capable macOS system.
{{% /notice %}}

## Run benchmarks with and without SME2

Run the SME2-enabled benchmark:

```bash
./litert_lm_advanced_main_sme2_on \
  --backend=cpu \
  --model_path=models/gemma-4-E4B-it.litertlm \
  --benchmark \
  --benchmark_prefill_tokens=512 \
  --benchmark_decode_tokens=128 \
  --num_cpu_threads=4 \
  --disable_cache=false | tee benchmark-sme2-on.txt
```

Run the SME2-disabled benchmark:

```bash
./litert_lm_advanced_main_sme2_off \
  --backend=cpu \
  --model_path=models/gemma-4-E4B-it.litertlm \
  --benchmark \
  --benchmark_prefill_tokens=512 \
  --benchmark_decode_tokens=128 \
  --num_cpu_threads=4 \
  --disable_cache=false | tee benchmark-sme2-off.txt
```

Example output pattern:

```text
--------------------------------------------------
  Time to first token: 0.51 s
--------------------------------------------------
  Prefill Turns (Total 1 turns):
    Prefill Turn 1: Processed 512 tokens in 477.85ms duration.
      Prefill Speed: 1071.47 tokens/sec.
--------------------------------------------------
  Decode Turns (Total 1 turns):
    Decode Turn 1: Processed 128 tokens in 3.917262s duration.
      Decode Speed: 32.68 tokens/sec.
--------------------------------------------------
```

## Verify the SME2 performance uplift

Compare the prefill throughput from both runs:

```bash
SME2_ON=$(awk '/Prefill Speed/ {print $3; exit}' benchmark-sme2-on.txt)
SME2_OFF=$(awk '/Prefill Speed/ {print $3; exit}' benchmark-sme2-off.txt)

SME2_ON="$SME2_ON" SME2_OFF="$SME2_OFF" \
python3 -c 'import os; on=float(os.environ["SME2_ON"]); off=float(os.environ["SME2_OFF"]); print(f"SME2 prefill uplift: {on/off:.2f}x ({off:.2f} -> {on:.2f} tokens/sec)")'
```

For a reliable comparison:

- Use the same model, token counts, thread count, power state, and terminal session for both runs.
- Run each binary at least three times and compare the median `Prefill Speed`.
- Treat decode throughput separately. This Learning Path focuses on prefill because the SME2-optimized matrix multiplication path has the clearest effect during the prompt-processing phase.

## Run sample prompts

Run quick output sanity checks:

```bash
./litert_lm_advanced_main_sme2_on \
  --backend=cpu \
  --model_path=models/gemma-4-E4B-it.litertlm \
  --input_prompt="What is the capital of France?"

./litert_lm_advanced_main_sme2_on \
  --backend=cpu \
  --model_path=models/gemma-4-E4B-it.litertlm \
  --input_prompt="What is the most difficult winter Olympic sport?"
```
