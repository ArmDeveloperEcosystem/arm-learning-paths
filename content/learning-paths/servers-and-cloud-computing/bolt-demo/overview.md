---
title: Understand BOLT optimization for Arm
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This Learning Path demonstrates how to use [BOLT](https://github.com/llvm/llvm-project/blob/main/bolt/README.md), a post-link binary optimizer from LLVM, to improve the performance of AArch64 applications using profile-guided code layout optimization.

The example is based on a [BOLT tutorial from the 2025 LLVM Developers Conference](https://youtu.be/KdHtOMc5_c8?si=249wZTn_YcTFOjcJ&t=1452).

The input program is a deliberately inefficient implementation based on BubbleSort (described in the [setup section](/learning-paths/servers-and-cloud-computing/bolt-demo/setup/)). This workload exhibits poor instruction locality, making it a useful example for demonstrating how BOLT can improve performance by reorganizing code layout.

You will first evaluate whether the input binary is a good candidate for code layout optimization. If the program shows signs of poor spatial locality, you will then collect runtime profiles that BOLT can use to guide optimization.

BOLT supports several profiling methods, each with different trade-offs:

- [BRBE profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/brbe/) uses the Arm Branch Record Buffer Extension to sample branch history with minimal runtime overhead. When available, this is typically the preferred option.

- [Instrumentation profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/instrumentation/) inserts counters directly into the binary to record execution frequencies. While this produces highly accurate profiles, it introduces runtime overhead during profile collection.

- For systems without BRBE, [SPE profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/spe/) (Statistical Profiling Extension) samples microarchitectural events. BOLT can infer control-flow behavior from these samples, though the resulting profile quality may be lower than BRBE.

- Finally, [PMU profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/pmu/) works on any system with standard performance monitoring support. It samples events like instructions or cycles, providing less detailed control-flow information but serving as a reliable fallback when other methods aren't available.

Arm trace extensions such as ETM and ETE can also generate usable traces, but this Learning Path doesn't cover them.

For each profiling method, you'll collect a profile, convert it to BOLT's format, and generate an optimized binary. After optimization, you'll measure the performance improvement using hardware metrics.

## What you've learned and what's next

You now understand what BOLT is and the four profiling methods available for collecting optimization profiles: BRBE, instrumentation, SPE, and PMU. Each method offers different trade-offs between profiling accuracy and runtime overhead.

In the next section, you'll set up your environment and compile the example program that demonstrates poor code locality.
