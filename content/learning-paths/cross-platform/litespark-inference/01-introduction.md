---
title: Understand Litespark-Inference and BitNet b1.58
description: Understand how packed ternary weights and Arm Neon SDOT kernels enable Litespark-Inference to run BitNet b1.58 directly on CPUs.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What Litespark-Inference is

Litespark-Inference is an open-source runtime designed to execute ternary-weight language models, such as [BitNet b1.58](https://arxiv.org/abs/2402.17764), directly on host CPUs. It performs inference without using a GPU or PyTorch at runtime. The PyTorch and Transformers packages are declared as dependencies for benchmarking and model-loading utilities, but the torchless inference path relies only on `numpy`, `safetensors`, and `tokenizers`.

Litespark-Inference runs on the following platforms:

| Platform | Kernel selected automatically |
|---|---|
| Linux on Arm Neoverse | NEON + SDOT |
| macOS on Apple Silicon | NEON + SDOT |
| Linux on x86_64 with AVX-512 | AVX-512 + VNNI |
| Linux on x86_64 with Intel Core Ultra | AVX-VNNI (256-bit) |
| Linux on x86_64 (no VNNI) | AVX2 + FMA fallback |

During `pip install`, the build process automatically detects your CPU's hardware feature flags and compiles the appropriate C++ kernel for your machine.

## How BitNet b1.58 accelerates CPU inference

BitNet b1.58 stores each weight as a value in `{-1, 0, +1}` and packs
four weights into one byte. This provides two key benefits:

- Reduced memory footprint: The model file is around 6x smaller than the equivalent BF16 model (around 497 MB packed versus around 4,600 MB unpacked).
- SIMD compute efficiency: Every matrix multiplication reduces to INT8 activation × ternary weight, taking direct advantage of CPU SIMD dot-product instructions, such as `SDOT` on Arm Neon and `VNNI` on x86.

The net effect is that a 2-billion-parameter model fits in under 1 GB of
RAM and generates tokens at interactive speed on a laptop or
cloud CPU instance.

The following charts show Litespark-Inference against a PyTorch baseline
across several Arm and x86 CPUs. Token-generation throughput is roughly
an order of magnitude higher, and resident memory is around 6x smaller,
on every platform tested.

![Token-generation throughput, Litespark-Inference versus PyTorch, on Apple M5 Max, AMD Zen 4, and Intel Core Ultra 9#center](throughput-comparison.png "Cross-platform throughput comparison")

![Resident memory, Litespark-Inference versus PyTorch, on Apple M5 Max, AMD Zen 4, and Intel Core Ultra 9#center](memory-comparison.png "Cross-platform memory usage comparison")

## What you've learned and what's next

You've now learned how Litespark-Inference enables CPU inference without GPU or PyTorch runtime dependencies. You've also learned how ternary quantization (`BitNet b1.58`) compresses resident memory footprint and uses Arm Neon `SDOT` SIMD instructions.

Next, you'll learn how to run BitNet-2B from the CLI and using Python.
