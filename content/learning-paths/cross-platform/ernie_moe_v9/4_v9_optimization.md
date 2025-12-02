---
title: Arm v9 Optimization and MoE Efficiency
weight: 5
layout: "learningpathall"
---

## Accelerate ERNIE-4.5 with Armv9 Optimizations

In previous modules, you've learned how MoE enables large model deployment on CPUs, and how to observe inference behavior with ERNIE-4.5. Now, we'll optimize performance using Armv9 architecture features and benchmark the improvements.

This section shows how to benchmark performance under two scenarios: with and without Armv9 vector instruction optimizations.

We’ll compare:
- Baseline: regular CPU build
- Optimized: Armv9-specific build with SVE/i8mm/dotprod enabled

To establish a baseline performance, let’s first compile llama.cpp without Armv9 optimizations.

### Disable llama.cpp v9 Optimizations 

This step builds `llama.cpp` without Armv9 vector features to establish a baseline.

```bash
cd ~/llama.cpp
mkdir build_v9_off && cd build_v9_off
cmake \
  -DLLAMA_CURL=OFF \
  -DGGML_LLAMAFILE=OFF \
  -DGGML_VULKAN=OFF \
  -DBUILD_SHARED_LIBS=OFF \
  -DCMAKE_SYSTEM_PROCESSOR=arm64 \
  -DCMAKE_OSX_ARCHITECTURES=arm64 \
  -DGGML_NATIVE=OFF \
  -DGGML_AVX=off \
  -DGGML_AVX2=off \
  -DGGML_AVX512=off \
  -DGGML_FMA=off \
  -DGGML_F16C=off \
  -DGGML_CPU_KLEIDIAI=OFF \
  ..

make -j$(nproc)
```

Then run benchmark in `build_v9_off` directory. 

```bash
./bin/llama-bench -m ~/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf -pg 128,128 -t 8
```

The result for 24GB Radxa O6 will be:

| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |           pp512 |         14.96 ± 0.01 |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |           tg128 |         12.03 ± 0.02 |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |     pp128+tg128 |         13.51 ± 0.03 |

With the baseline captured, we now recompile with Armv9 vector extensions enabled.

### Enable llama.cpp v9 Optimizations 

Now rebuild with vector extensions enabled (i8mm, dotprod, SVE) by following configuration setting.

```bash
cd ~/llama.cpp
mkdir build_v9_on && cd build_v9_on
cmake \
  -DLLAMA_CURL=OFF \
  -DGGML_LLAMAFILE=OFF \
  -DGGML_VULKAN=OFF \
  -DBUILD_SHARED_LIBS=OFF \
  -DCMAKE_SYSTEM_PROCESSOR=armv9-a \
  -DCMAKE_OSX_ARCHITECTURES=arm64 \
  -DGGML_NATIVE=OFF \
  -DGGML_AVX=off \
  -DGGML_AVX2=off \
  -DGGML_AVX512=off \
  -DGGML_FMA=off \
  -DGGML_F16C=off \
  -DGGML_CPU_ARM_ARCH=armv9-a+i8mm+dotprod+sve \
  -DGGML_CPU_KLEIDIAI=ON \
  ..

make -j$(nproc)
```

{{% notice Note %}}
We disable GPU and other backend support to focus exclusively on CPU performance and optimization for this learning path.
{{% /notice %}}

Then re-run benchmark in `build_v9_on` directory. 

```bash
./bin/llama-bench -m ~/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf -pg 128,128 -t 8
```

The result for 24GB Radxa O6 will be:

| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |           pp512 |         38.51 ± 0.11 |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |           tg128 |         15.96 ± 0.08 |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |     pp128+tg128 |         21.58 ± 0.11 |


Let’s now compare the results side-by-side to see how much performance is gained.

### Comparing Performance: Armv9 Optimization Results

After running benchmarks with and without Armv9-specific instructions, the results show significant gains.

| Test          | v9 off          | v9 on          | Gain    |  
|---------------|-----------------|----------------|---------|
| pp512         |  14.96 token/s  |  38.51 token/s | 2.57x   |
| tg128         |  12.03 token/s  |  15.96 token/s | 1.32x   |
| pp128 + tg128 |  13.51 token/s  |  21.58 token/s | 1.59x   |

- Vectorized kernels (i8mm, dotprod, SVE) drastically improve inference throughput.
- The pp512 test shows the most significant acceleration, delivering a 2.57× improvement.
- Other patterns like tg128 and pp128+tg128 also achieve measurable gains, demonstrating the broad benefit of hardware-aware builds.
- Armv9 optimization enables practical real-time inference for 21B models on edge-class hardware.


### Summary
Over this learning path, you've walked through every stage of deploying a 21B parameter Chinese MoE model on edge-class Armv9 hardware. You:
- Understood how MoE reduces memory usage by only activating a small subset of parameters per token.
- Set up llama.cpp and deployed ERNIE-4.5 on a Radxa O6 board.
- Compared ERNIE-4.5 Thinking and PT model behaviors and examined expert routing logic with debug instrumentation.
- Applied Armv9 hardware optimizations to unlock over 2.5× speed improvements in token throughput.

You now have the full-stack capabilities to deploy, profile, and tune Chinese LLMs for efficient inference on modern Arm CPUs.
