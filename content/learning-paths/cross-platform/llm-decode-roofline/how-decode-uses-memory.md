---
title: Understand why token generation is limited by memory bandwidth
description: Understand how memory bandwidth and bytes read per token limit llama.cpp decode on Arm CPUs, and how prefill differs.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How decode speed depends on bandwidth

When llama.cpp runs a model on an Arm CPU, it does two kinds of work:

- Prompt processing (prefill) reads your whole prompt at once. Each weight that comes out of memory is used for every prompt token in the batch. The cores do a lot of arithmetic per byte, so prefill speeds up when you add cores.
- Token generation (decode) produces one token at a time. To produce each token, the CPU reads the model weights from DRAM and uses each weight once. The cores do very little arithmetic per byte, so they spend most of each token waiting for memory.

Because decode reads the model weights for every token, its speed follows one equation:

```text
decode tokens/s  =  effective memory bandwidth (bytes/s)  /  bytes read per token
```

This is the memory-bound side of the roofline model. 

The Raspberry Pi 5 that was used to test the Learning Path sustains 13.8 GB/s of bandwidth. The smallest model reads 346 MB per token. Decode on that model can't go faster than about 40 tokens/s, no matter how fast the cores are.

The equation gives you three practical rules:

- Halving the bytes read per token, with a smaller model or a smaller quantization format, roughly doubles decode speed.
- Adding threads past the point where memory is saturated doesn't help decode. It often makes decode slower.
- Prefill is compute-bound, so it keeps scaling with threads. The best thread count for prefill and for decode is often different.

## How llama-roofline helps

[llama-roofline](https://github.com/manunicholasjacob/llama-roofline) is an open-source Python tool that measures both sides of the equation on your machine:

1. It measures the sustained memory-read bandwidth of your system. This is the ceiling.
2. It reads each GGUF file and counts the bytes that decode reads per token.
3. It runs `llama-bench` across a thread sweep.
4. It fits `tokens/s = bandwidth / bytes` across your models and reports how close each model is to the ceiling, in plain language.

The answer tells you which setting moves your tokens per second on this specific Arm system.

## The reference platform

The Learning Path was tested on a Raspberry Pi 5. Every output shown in the Learning Path comes from one run on a board with the following configuration:

| Item | Raspberry Pi 5 |
|---|---|
| CPU | 4 x Arm Cortex-A76 at up to 2.4 GHz |
| Architecture features used by llama.cpp | NEON (ASIMD), DotProd |
| Cache | 512 KB L2 per core, 2 MB shared L3 |
| Memory | 2 GB LPDDR4X, 32-bit interface |
| Operating system | 64-bit Raspberry Pi OS (Debian 12), kernel 6.12 |
| CPU frequency governor | `ondemand` |

You can complete the Learning Path on any Arm Linux system.

## What you've learned and what's next 

You now know why decode speed depends on bytes and bandwidth, and why prefill behaves differently.

Next, you'll build llama.cpp and install llama-roofline on your Arm system.
