---
title: Understand why token generation is limited by memory bandwidth
description: Learn why llama.cpp token generation on an Arm CPU is limited by how many bytes it reads per token, why prompt processing is not, and what llama-roofline measures to show the difference.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What this Learning Path measures

When llama.cpp runs a model on an Arm CPU, it does two kinds of work:

- **Prompt processing (prefill)** reads your whole prompt at once. Each weight that comes out of memory is used for every prompt token in the batch, so the cores do a lot of arithmetic per byte. Prefill speeds up when you add cores.
- **Token generation (decode)** produces one token at a time. To produce each token, the CPU reads the model weights from DRAM and uses each weight once. The cores do very little arithmetic per byte, so they spend most of each token waiting for memory.

Because decode reads the model weights for every token, its speed follows one equation:

```output
decode tokens/s  =  effective memory bandwidth (bytes/s)  /  bytes read per token
```

This is the memory-bound side of the roofline model. For example, the Raspberry Pi 5 used for this Learning Path sustains 13.8 GB/s, and the smallest model in this Learning Path reads 346 MB per token, so decode on that model cannot go faster than about 40 tokens/s, no matter how fast the cores are.

The equation gives you three practical rules:

- Halving the bytes read per token, with a smaller model or a smaller quantization format, roughly doubles decode speed.
- Adding threads past the point where memory is saturated does not help decode, and it often makes decode slower.
- Prefill is compute-bound, so it keeps scaling with threads. The best thread count for prefill and for decode is often different.

## How llama-roofline helps

[llama-roofline](https://github.com/manunicholasjacob/llama-roofline) is an open-source Python tool that measures both sides of the equation on your machine:

1. It measures the sustained memory-read bandwidth of your system. This is the ceiling.
2. It reads each GGUF file and counts the bytes that decode reads per token.
3. It runs `llama-bench` across a thread sweep.
4. It fits `tokens/s = bandwidth / bytes` across your models and reports how close each model is to the ceiling, in plain language.

The answer tells you which setting moves your tokens per second on this specific Arm system.

## The reference platform

This Learning Path uses a Raspberry Pi 5 as the example platform. Every output shown in the following sections comes from one run on this board:

| Item | Raspberry Pi 5 |
|---|---|
| CPU | 4 x Arm Cortex-A76 at up to 2.4 GHz |
| Architecture features used by llama.cpp | NEON (ASIMD), DotProd |
| Cache | 512 KB L2 per core, 2 MB shared L3 |
| Memory | 2 GB LPDDR4X, 32-bit interface |
| Operating system | 64-bit Raspberry Pi OS (Debian 12), kernel 6.12 |
| CPU frequency governor | `ondemand` |

The same commands work on any Arm Linux system.

## What you've learned

You now know why decode speed depends on bytes and bandwidth, and why prefill behaves differently. Next, you build llama.cpp and install llama-roofline on your Arm system.
