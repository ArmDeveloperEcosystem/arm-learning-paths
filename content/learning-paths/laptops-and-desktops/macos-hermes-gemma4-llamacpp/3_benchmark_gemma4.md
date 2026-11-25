---
title: Download and benchmark Gemma 4 E4B on macOS
description: Download Gemma 4 E4B GGUF weights from Hugging Face and compare Metal GPU versus CPU performance on Apple silicon with llama-bench.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the Gemma 4 E4B GGUF model

From inside your `~/hermes-gemma4/llama.cpp` directory, create a `./models` directory if needed and set up a Python virtual environment for the Hugging Face Command-Line Interface (CLI):

```bash
mkdir -p models
python3 -m venv .venv
source .venv/bin/activate
pip install -U huggingface_hub
```

Download Gemma 4 E4B (`Q4_0` quantization, ~4.3 GB), which provides fast prompt prefill, low memory usage, and reliable tool calling for local code-fixing tasks:

```bash
hf download ggml-org/gemma-4-E4B-it-GGUF \
  --include "*Q4_0*.gguf" \
  --local-dir ./models
```

Verify the downloaded `.gguf` file is present in `./models/`:

```bash
ls -lh ./models/gemma-4-E4B-it-Q4_0.gguf
```

The output is similar to:

```output
-rw-r--r--@ 1 user  staff   4.3G Nov 24 15:55 ./models/gemma-4-E4B-it-Q4_0.gguf
```

## Benchmark Metal GPU versus CPU performance

Offloading all model layers to the Apple silicon Metal GPU with Flash Attention enabled (`-ngl 99 -fa 1`) delivers 2.20x (+120%) faster prompt processing and 1.50x (+50%) faster token generation than the fastest CPU-only run (`-ngl 0`) on an Apple M4 Pro. Compared to a prebuilt Homebrew llama.cpp v1.0.0 (`b1b770d90`, build 12359) installation run with identical flags, the source build improves Metal prompt processing by +18.7% and token generation by +17.7%. On CPU-only runs (`-ngl 0` at 8 threads), Arm KleidiAI with SME lifts prompt processing by 2.51x (+151%) over the Homebrew package.

Run `llama-bench` with full Metal GPU offload (`-ngl 99`) across Flash Attention disabled (`0`) and enabled (`1`), setting `-t` to your performance-core count:

```bash
P_CORES=$(sysctl -n hw.perflevel0.physicalcpu)

./build/bin/llama-bench \
  -m ./models/gemma-4-E4B-it-Q4_0.gguf \
  -ngl 99 -fa 0,1 -t "$P_CORES" -r 3 \
  -p 512 -n 128
```

The output is similar to:

```output
ggml_metal_device_init: GPU name:   MTL0 (Apple M4 Pro)
ggml_metal_device_init: GPU family: MTLGPUFamilyApple9  (1009)
ggml_metal_device_init: GPU family: MTLGPUFamilyMetal4  (5002)
ggml_metal_device_init: simdgroup reduction   = true
ggml_metal_device_init: simdgroup matrix mul. = true
ggml_metal_device_init: has unified memory    = true
...
| model                          |       size |     params | backend    | threads |  fa |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --: | --------------: | -------------------: |
| gemma4 E4B Q4_0                |   4.26 GiB |     7.46 B | MTL,BLAS   |       8 |   0 |           pp512 |       1062.75 ± 4.13 |
| gemma4 E4B Q4_0                |   4.26 GiB |     7.46 B | MTL,BLAS   |       8 |   0 |           tg128 |         61.00 ± 0.54 |
| gemma4 E4B Q4_0                |   4.26 GiB |     7.46 B | MTL,BLAS   |       8 |   1 |           pp512 |      1078.39 ± 10.40 |
| gemma4 E4B Q4_0                |   4.26 GiB |     7.46 B | MTL,BLAS   |       8 |   1 |           tg128 |         62.47 ± 0.12 |
```

Next, run a CPU-only sweep (`-ngl 0`) across four threads, your performance-core count, and all physical cores (`hw.physicalcpu`) to measure the CPU baseline and see how efficiency cores affect throughput:

```bash
ALL_CORES=$(sysctl -n hw.physicalcpu)

./build/bin/llama-bench \
  -m ./models/gemma-4-E4B-it-Q4_0.gguf \
  -ngl 0 -t "4,$P_CORES,$ALL_CORES" -r 1 \
  -p 512 -n 128
```

For reference, here are illustrative results measured on an Apple M4 Pro with 24 GB unified memory running macOS 27.2.1. The source build (`33aeb17`, AppleClang 21.0.0, `-DGGML_METAL=ON -DGGML_ACCELERATE=ON -DGGML_CPU_KLEIDIAI=ON`) is compared against Homebrew llama.cpp v1.0.0 (`build 12359`) tested with the same `llama-bench` flags (`-p 512 -n 128`):

| Configuration | Offload (`-ngl`) | Threads (`-t`) | Flash Attention (`-fa`) | Prompt Processing `pp512` (tok/s) | Token Generation `tg128` (tok/s) |
|---|---|---|---|---|---|
| Metal GPU (source build) | `99` | 8 | `1` | 1078.39 ± 10.40 | 62.47 ± 0.12 |
| Metal GPU (source build) | `99` | 8 | `0` | 1062.75 ± 4.13 | 61.00 ± 0.54 |
| Metal GPU (Homebrew v1.0.0) | `99` | 8 | `1` | 908.86 ± 2.24 | 53.06 ± 1.25 |
| CPU-only (source, KleidiAI + SME) | `0` | 8 | `0` | 489.62 ± 0.00 | 35.79 ± 0.00 |
| CPU-only (source, KleidiAI + SME) | `0` | 4 | `0` | 318.22 ± 0.00 | 41.60 ± 0.00 |
| CPU-only (source, P + E cores) | `0` | 12 | `0` | 163.35 ± 0.00 | 17.79 ± 0.00 |
| CPU-only (Homebrew v1.0.0) | `0` | 8 | `0` | 194.91 ± 0.00 | 34.53 ± 0.00 |

### Verify Metal and KleidiAI usage

Confirm in the `llama-bench` startup lines that `ggml_metal_device_init: GPU name:   MTL0 (Apple M4 Pro)` (or your Mac's chip name) and `has unified memory    = true` appear. The `backend` column in the results table should list `MTL,BLAS`.

For CPU-only runs, `-DGGML_CPU_KLEIDIAI=ON` compiles Arm KleidiAI SME kernels into `libggml-cpu.dylib`, which you can verify directly:

```bash
nm -gU ./build/bin/libggml-cpu.dylib | grep -iE "kleidi|sme" | head -n 6
```

The output is similar to:

```output
00000000000c7d14 T __Z28ggml_kleidiai_select_kernels11cpu_featurePK11ggml_tensor
00000000000c8374 T __Z32ggml_kleidiai_select_kernels_f3211cpu_feature
00000000000c8268 T __Z33ggml_kleidiai_select_kernels_q4_011cpu_feature
00000000000c82f0 T __Z33ggml_kleidiai_select_kernels_q4_k11cpu_feature
00000000000c8308 T __Z33ggml_kleidiai_select_kernels_q8_011cpu_feature
00000000000f40d8 D __ZZN4ggml3cpu8kleidiai17extra_buffer_type17get_tensor_traitsEPK11ggml_tensorE6warned
```

At runtime, `ggml_kleidiai_select_kernels` checks `ggml_cpu_has_sme()` to select SME kernels on M4 and M5 Macs and falls back automatically to Arm Neon, dot-product, and `i8mm` paths on M1–M3 Macs.

### Interpreting Metal, SME, and thread scaling results

Prompt processing (`pp512`, also called prefill) measures how fast the model processes a 512-token input prompt in parallel. Because prefill is compute-bound, Metal GPU processing reaches over 1,078 tok/s—more than double the 489.62 tok/s peak on the 8 performance CPU cores. Fast prefill directly accelerates Hermes Agent because its first turn sends an ~11K-token system prompt and tool schema.

Token generation (`tg128`, also called decode) measures how fast the model produces 128 output tokens one at a time. Decode is memory-bandwidth bound because each generated token streams model weights from unified memory. Metal reaches 62.47 tok/s with Flash Attention enabled (`-fa 1`), whereas CPU-only decode peaks at 41.60 tok/s on four performance cores.

Two Apple silicon behaviors stand out in the CPU-only (`-ngl 0`) sweep:

- **KleidiAI and SME acceleration**: Compiling with `-DGGML_CPU_KLEIDIAI=ON` enables Arm SME matrix kernels on M4 and M5 Macs. At 8 threads, CPU-only `pp512` rises from 194.91 tok/s on Homebrew to 489.62 tok/s on the source build.
- **Avoid efficiency cores (`-t 12`)**: Increasing threads from 8 performance cores to all 12 cores causes the macOS scheduler to place worker threads on slower efficiency cores. That stalls synchronization, cutting CPU prefill from 489.62 to 163.35 tok/s and decode from 35.79 to 17.79 tok/s. Always set `-t` to `hw.perflevel0.physicalcpu` so worker threads stay on performance cores.

## What you've accomplished and what's next

You've downloaded Gemma 4 E4B from Hugging Face and benchmarked Metal GPU and CPU performance with `llama-bench`, confirming that full Metal offload with Flash Attention and performance-core threading yields peak speed.

Next, you'll launch `llama-server` with a 64K context window and verify its OpenAI-compatible API endpoint.
