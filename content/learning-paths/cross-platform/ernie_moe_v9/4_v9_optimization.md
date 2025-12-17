---
title: Optimize performance with Armv9 hardware features
weight: 5
layout: "learningpathall"
---

## Accelerate ERNIE-4.5 with Armv9 optimizations

In previous sections, you learned how MoE enables large model deployment on CPUs, and how to observe inference behavior with ERNIE-4.5. You'll now optimize performance using Armv9 architecture features and benchmark the improvements.

This section shows how to benchmark performance under two scenarios: with and without Armv9 vector instruction optimizations.

You compare a baseline using a regular CPU build against an optimized version that's an Armv9-specific build with SVE, i8mm, and dotprod instructions enabled.

To establish baseline performance, first compile llama.cpp without Armv9 optimizations.

### Disable llama.cpp Armv9 optimizations 

This step builds `llama.cpp` without Armv9 vector features to establish a baseline.

```bash
cd $HOME/llama.cpp
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

Run the benchmark in the `build_v9_off` directory: 

```bash
./bin/llama-bench -m $HOME/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf -pg 128,128 -t 8
```

The output is similar to:

| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |           pp512 |         14.96 ± 0.01 |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |           tg128 |         12.03 ± 0.02 |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |     pp128+tg128 |         13.51 ± 0.03 |

With the baseline captured, recompile with Armv9 vector extensions enabled.

### Enable llama.cpp Armv9 optimizations 

Rebuild with vector extensions enabled (i8mm, dotprod, SVE) using the following configuration settings:

```bash
cd $HOME/llama.cpp
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
This build disables GPU and other backend support to focus on CPU performance and optimization for this Learning Path.
{{% /notice %}}

Re-run the benchmark in the `build_v9_on` directory: 

```bash
./bin/llama-bench -m $HOME/models/ernie-4.5/ERNIE-4.5-21B-A3B-Thinking-Q4_0.gguf -pg 128,128 -t 8
```

The output is similar to:

| model                          |       size |     params | backend    | threads |            test |                  t/s |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | --------------: | -------------------: |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |           pp512 |         38.51 ± 0.11 |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |           tg128 |         15.96 ± 0.08 |
| ernie4_5-moe 21B.A3B Q4_0      |  11.64 GiB |    21.83 B | CPU        |       8 |     pp128+tg128 |         21.58 ± 0.11 |


Compare the results side by side to see the performance gained.

### Compare performance: Armv9 optimization results

After running benchmarks with and without Armv9-specific instructions, the results show significant gains.

| Test          | v9 off          | v9 on          | Gain    |  
|---------------|-----------------|----------------|---------|
| pp512         |  14.96 token/s  |  38.51 token/s | 2.57x   |
| tg128         |  12.03 token/s  |  15.96 token/s | 1.32x   |
| pp128 + tg128 |  13.51 token/s  |  21.58 token/s | 1.59x   |

Vectorized kernels (i8mm, dotprod, SVE) drastically improve inference throughput. The pp512 test shows the most significant acceleration with a 2.57× improvement. Other patterns like tg128 and pp128+tg128 also achieve measurable gains. These results demonstrate the broad benefit of hardware-aware builds and show that Armv9 optimization enables practical real-time inference for 21 B models on edge-class hardware.

### Summary

Throughout this Learning Path, you deployed a 21 B parameter Chinese MoE model on edge-class Armv9 hardware. You started by understanding how MoE reduces memory usage by activating only a small subset of parameters per token. After setting up llama.cpp on a Radxa O6 board, you compared ERNIE-4.5 Thinking and PT model behaviors while examining expert routing logic with debug instrumentation. Finally, you applied Armv9 hardware optimizations and achieved over 2.5× speed improvements in token throughput. 

You can now deploy, profile, and tune Chinese LLMs for efficient inference on modern Arm CPUs.
