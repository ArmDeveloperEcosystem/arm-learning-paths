---
title: Build and run benchmarks
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---


## Build LiteRT-LM with local XNNPACK and KleidiAI

Build from the LiteRT-LM repository:

```bash
cd $HOME/gemma4-prefill-bench/LiteRT-LM
bazel build \
    --config=macos_arm64 \
    --macos_sdk_version="$(xcrun --sdk macosx --show-sdk-version)" \
    --override_repository=XNNPACK=../xnnpack \
    --override_repository=KleidiAI=../kleidiai \
    //runtime/engine:litert_lm_advanced_main

```

## Run benchmark

```bash
bazel-bin/runtime/engine/litert_lm_advanced_main \
  --backend=cpu \
  --model_path=models/gemma-3n-E4B-it-int4.litertlm \
  --benchmark \
  --benchmark_prefill_tokens=512 \
  --benchmark_decode_tokens=128 \
  --num_cpu_threads=4 \
  --disable_cache=false
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

Run quick output sanity checks:

```bash
bazel-bin/runtime/engine/litert_lm_advanced_main \
  --backend=cpu \
  --model_path=models/gemma-3n-E4B-it-int4.litertlm \
  --input_prompt="What is the capital of France?"

bazel-bin/runtime/engine/litert_lm_advanced_main \
  --backend=cpu \
  --model_path=models/gemma-3n-E4B-it-int4.litertlm \
  --input_prompt="What is the most difficult winter Olympic sport?"
```
