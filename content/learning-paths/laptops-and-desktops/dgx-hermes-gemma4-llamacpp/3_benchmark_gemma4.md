---
title: Download and benchmark Gemma 4 models on DGX Spark
description: Download Gemma 4 E4B, 26B-A4B MoE, and 31B GGUF weights from Hugging Face and compare Blackwell GPU versus Grace CPU performance on NVIDIA DGX Spark with llama-bench.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the Gemma 4 GGUF models

DGX Spark's 128 GB unified memory lets you benchmark the full range of Gemma 4 architectures on one desktop system: a compact edge model (Gemma 4 E4B), a sparse Mixture-of-Experts (MoE) model (Gemma 4 26B-A4B), and a large dense model (Gemma 4 31B). You'll benchmark all three models here, then serve Gemma 4 E4B with Hermes Agent in the following sections for fast iteration and direct comparison with the macOS workflow.

From inside your `~/hermes-gemma4/llama.cpp` directory, create a `./models` directory and set up a Python virtual environment for the Hugging Face Command-Line Interface (CLI):

```bash
mkdir -p models
python3 -m venv .venv
source .venv/bin/activate
pip install -U huggingface_hub
```

Download the `Q4_0` quantized GGUF weights for all three Gemma 4 models from `ggml-org` (~35 GB total):

```bash
hf download ggml-org/gemma-4-E4B-it-GGUF \
  gemma-4-E4B-it-Q4_0.gguf \
  --local-dir ./models

hf download ggml-org/gemma-4-26B-A4B-it-GGUF \
  gemma-4-26B-A4B-it-Q4_0.gguf \
  --local-dir ./models

hf download ggml-org/gemma-4-31B-it-GGUF \
  gemma-4-31B-it-Q4_0.gguf \
  --local-dir ./models
```

Verify that all three `.gguf` files are present in `./models/`:

```bash
ls -lh ./models/gemma-4-*.gguf
```

The output is similar to:

```output
-rw-rw-r-- 1 user user  14G Nov 25 20:58 ./models/gemma-4-26B-A4B-it-Q4_0.gguf
-rw-rw-r-- 1 user user  17G Nov 25 21:04 ./models/gemma-4-31B-it-Q4_0.gguf
-rw-rw-r-- 1 user user 4.3G Nov 25 20:52 ./models/gemma-4-E4B-it-Q4_0.gguf
```

## Benchmark Blackwell GPU versus Grace CPU performance

Offloading all layers to the NVIDIA GB10 Blackwell GPU with Flash Attention enabled (`-ngl 99 -fa on`) delivers massive speedups over CPU-only execution (`-dev none -ngl 0`) on the 20-core Grace CPU:

- Gemma 4 E4B (`Q4_0`): GPU prompt processing reaches 7,610.39 tok/s (34.9x faster than 20-thread CPU and 42.2x faster than 8-thread CPU) and GPU token generation reaches 71.24 tok/s (2.75x faster than peak 8-thread CPU).
- Gemma 4 26B-A4B MoE (`Q4_0`): GPU prompt processing reaches 3,238.35 tok/s (35.1x faster than CPU) and GPU token generation reaches 61.72 tok/s (2.43x faster than CPU).
- Gemma 4 31B Dense (`Q4_0`): GPU prompt processing reaches 878.18 tok/s (43.8x faster than CPU) and GPU token generation reaches 11.59 tok/s (2.22x faster than CPU).

### Benchmark Gemma 4 E4B on GPU and CPU

Run `llama-bench` on Gemma 4 E4B with full GB10 GPU offload (`-ngl 99`) comparing Flash Attention disabled (`off`) and enabled (`on`), plus a run with `q8_0` KV cache quantization matching the `llama-server` configuration:

```bash
./build/bin/llama-bench \
  -m ./models/gemma-4-E4B-it-Q4_0.gguf \
  -ngl 99 -fa off,on -t 10 -r 3 \
  -p 512 -n 128

./build/bin/llama-bench \
  -m ./models/gemma-4-E4B-it-Q4_0.gguf \
  -ngl 99 -fa on -ctk q8_0 -ctv q8_0 -t 10 -r 3 \
  -p 512 -n 128
```

The output is similar to:

```output
ggml_cuda_init: found 1 CUDA devices (Total VRAM: 124607 MiB):
  Device 0: NVIDIA GB10, compute capability 12.1, VMM: yes, VRAM: 124607 MiB
| model                          |       size |     params | backend    | ngl | threads |  fa |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | --: | ------: | --: | --------------: | -------------------: |
| gemma4 E4B Q4_0                |   4.26 GiB |     7.46 B | CUDA       |  99 |      10 |   0 |           pp512 |     7130.64 ± 277.80 |
| gemma4 E4B Q4_0                |   4.26 GiB |     7.46 B | CUDA       |  99 |      10 |   0 |           tg128 |         70.10 ± 0.05 |
| gemma4 E4B Q4_0                |   4.26 GiB |     7.46 B | CUDA       |  99 |      10 |   1 |           pp512 |     7610.39 ± 145.17 |
| gemma4 E4B Q4_0                |   4.26 GiB |     7.46 B | CUDA       |  99 |      10 |   1 |           tg128 |         71.24 ± 0.18 |
```

Next, run a true CPU-only sweep across 4, 8, 10, and 20 threads on the Grace CPU. Pass `-dev none` together with `-ngl 0` so `llama-bench` disables automatic CUDA operator offloading (`-nopo 0` by default) and keeps both prompt processing and token generation strictly on the CPU:

```bash
./build/bin/llama-bench \
  -m ./models/gemma-4-E4B-it-Q4_0.gguf \
  -dev none -ngl 0 -t 4,8,10,20 -r 1 \
  -p 512 -n 128
```

{{% notice Note %}}
In a CUDA-enabled llama.cpp build, passing `-ngl 0` alone keeps transformer layers in host buffers but still allows llama.cpp to offload large prompt-processing matrix multiplications to CUDA. Always add `-dev none` when measuring true CPU-only performance on DGX Spark.
{{% /notice %}}

### Benchmark Gemma 4 26B-A4B (MoE) and Gemma 4 31B (Dense)

Run GPU (`-ngl 99 -fa on`) and true CPU-only (`-dev none -ngl 0 -t 8`) benchmarks on the two larger Gemma 4 models to compare MoE versus dense scaling on DGX Spark:

```bash
./build/bin/llama-bench \
  -m ./models/gemma-4-26B-A4B-it-Q4_0.gguf \
  -ngl 99 -fa on -t 10 -r 3 \
  -p 512 -n 128

./build/bin/llama-bench \
  -m ./models/gemma-4-26B-A4B-it-Q4_0.gguf \
  -dev none -ngl 0 -t 8 -r 1 \
  -p 512 -n 128

./build/bin/llama-bench \
  -m ./models/gemma-4-31B-it-Q4_0.gguf \
  -ngl 99 -fa on -t 10 -r 3 \
  -p 512 -n 128

./build/bin/llama-bench \
  -m ./models/gemma-4-31B-it-Q4_0.gguf \
  -dev none -ngl 0 -t 8 -r 1 \
  -p 512 -n 128
```

### Reference benchmark results on NVIDIA DGX Spark

For reference, here are illustrative results measured on an NVIDIA DGX Spark (Grace Blackwell GB10, 10 Cortex-X925 + 10 Cortex-A725 cores, 128 GB unified LPDDR5X memory, Ubuntu 24.04.5 LTS, CUDA 13.0, GCC 13.3.0) using llama.cpp `5917b39ff` (build 12763) compiled with `-DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=121a-real -DGGML_CPU_ARM_ARCH=armv9-a+dotprod+i8mm+bf16+sve+sve2+fp16 -DGGML_CPU_KLEIDIAI=ON` (`-p 512 -n 128`):

| Model (`Q4_0`) | Size | Execution Mode | Flags | Prompt Processing `pp512` (tok/s) | Token Generation `tg128` (tok/s) |
|---|---|---|---|---|---|
| Gemma 4 E4B (7.46 B) | 4.26 GiB | GB10 GPU (CUDA) | `-ngl 99 -fa on -t 10` | 7,610.39 ± 145.17 | 71.24 ± 0.18 |
| Gemma 4 E4B (7.46 B) | 4.26 GiB | GB10 GPU (CUDA, `q8_0` KV) | `-ngl 99 -fa on -ctk q8_0 -ctv q8_0` | 7,460.25 ± 137.79 | 69.32 ± 0.11 |
| Gemma 4 E4B (7.46 B) | 4.26 GiB | GB10 GPU (CUDA) | `-ngl 99 -fa off -t 10` | 7,130.64 ± 277.80 | 70.10 ± 0.05 |
| Gemma 4 E4B (7.46 B) | 4.26 GiB | Grace CPU (KleidiAI) | `-dev none -ngl 0 -t 8` | 180.39 ± 0.00 | 25.90 ± 0.00 |
| Gemma 4 E4B (7.46 B) | 4.26 GiB | Grace CPU (KleidiAI) | `-dev none -ngl 0 -t 10` | 172.16 ± 0.00 | 25.35 ± 0.00 |
| Gemma 4 E4B (7.46 B) | 4.26 GiB | Grace CPU (KleidiAI) | `-dev none -ngl 0 -t 20` | 217.83 ± 0.00 | 5.52 ± 0.00 |
| Gemma 4 26B-A4B MoE (25.23 B) | 13.60 GiB | GB10 GPU (CUDA) | `-ngl 99 -fa on -t 10` | 3,238.35 ± 277.02 | 61.72 ± 0.06 |
| Gemma 4 26B-A4B MoE (25.23 B) | 13.60 GiB | Grace CPU (KleidiAI) | `-dev none -ngl 0 -t 8` | 92.35 ± 0.00 | 25.38 ± 0.00 |
| Gemma 4 31B Dense (30.70 B) | 16.74 GiB | GB10 GPU (CUDA) | `-ngl 99 -fa on -t 10` | 878.18 ± 5.21 | 11.59 ± 0.00 |
| Gemma 4 31B Dense (30.70 B) | 16.74 GiB | Grace CPU (KleidiAI) | `-dev none -ngl 0 -t 8` | 20.04 ± 0.00 | 5.21 ± 0.00 |

### Interpreting GPU, CPU, and model scaling results

Three hardware characteristics on NVIDIA DGX Spark explain the numbers in the table:

- **Massive GPU prefill advantage (`pp512`)**: Prompt processing is compute-bound, so offloading to Blackwell Tensor Cores (`sm_121a`) lifts `pp512` by **34.9x to 43.8x** across all three models. For Hermes Agent, that reduces the cold ~11K-token system prompt prefill from roughly a minute on CPU down to a couple of seconds on GPU.
- **Memory-bandwidth-bound decode (`tg128`) and MoE efficiency**: Token generation streams active model weights from unified LPDDR5X memory on every token. Because Gemma 4 26B-A4B activates only ~4B parameters per token, it achieves **61.72 tok/s** decode on the GB10 GPU—**5.3x faster** than the 31B dense model (11.59 tok/s) despite having 25.2B total parameters.
- **Heterogeneous Grace CPU thread scaling**: When running CPU-only (`-dev none -ngl 0`), staying at 8 to 10 threads keeps worker threads primarily on the 10 Cortex-X925 performance cores (peaking at **25.90 tok/s** on E4B). Raising threads to 20 engages the slower Cortex-A725 cores, which slightly improves compute-bound `pp512` (180.39 to 217.83 tok/s) but drops memory-bound `tg128` from **25.90 to 5.52 tok/s** because fast cores wait on slower cores at synchronization barriers.

## What you've accomplished and what's next

You've downloaded Gemma 4 E4B, 26B-A4B (MoE), and 31B from Hugging Face and benchmarked Blackwell GPU versus Grace CPU performance with `llama-bench`, confirming massive prefill speedups on GPU and strong MoE decode throughput on unified memory.

Next, you'll serve Gemma 4 E4B on the GB10 GPU with a 64K context window and verify its OpenAI-compatible API endpoint for Hermes Agent.
