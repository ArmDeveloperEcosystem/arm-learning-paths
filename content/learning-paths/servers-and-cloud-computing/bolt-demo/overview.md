---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Overview

This Learning Path demonstrates how to use [BOLT](https://github.com/llvm/llvm-project/blob/main/bolt/README.md) a post-link binary optimizer from LLVM, to improve the performance of AArch64 applications using profile-guided code layout optimization.
The example used in the Learning Path is based on a demonstration from the 2025 LLVM Developers Conference:  
[BOLT tutorial on AArch64 and how it competes or complements other PGOs](https://youtu.be/KdHtOMc5_c8?si=249wZTn_YcTFOjcJ&t=1452).


The input program is a deliberately inefficient implementation based on [BubbleSort](/learning-paths/servers-and-cloud-computing/bolt-demo/setup/). This workload exhibits poor instruction locality, making it a useful example for demonstrating how BOLT can improve performance by reorganizing code layout.

You will first evaluate whether the input binary is a good candidate for code layout optimization. If the program shows signs of poor spatial locality, you will then collect runtime profiles that BOLT can use to guide optimization.
Several profiling methods are supported:
-	**[BRBE](/learning-paths/servers-and-cloud-computing/bolt-demo/brbe/)**: Uses the Arm Branch Record Buffer Extension to sample branch history with low runtime overhead.
-	**[Instrumentation](/learning-paths/servers-and-cloud-computing/bolt-demo/instrumentation/)**: Inserts counters into the binary to record execution frequencies. This produces highly accurate profiles but introduces runtime overhead during profile collection.
-	**[SPE](/learning-paths/servers-and-cloud-computing/bolt-demo/spe/)**: Uses the Arm Statistical Profiling Extension to sample microarchitectural events. BOLT can infer control-flow behavior from these samples, although the resulting profile quality may be lower than BRBE.
-	**[PMU](/learning-paths/servers-and-cloud-computing/bolt-demo/pmu/)**: Uses standard performance monitoring unit events such as instructions or cycles. This method provides the least detailed information about control flow and is typically used when other profiling options are unavailable.

Arm trace extensions such as **ETM** and **ETE** can also generate traces that are usable by BOLT, but these tracing mechanisms are not covered in this tutorial.

For each profiling method, you will walk through the process of collecting a profile, converting it into a format usable by BOLT, and applying BOLT to generate an optimized binary.

Finally, you will use hardware performance metrics to evaluate how effective the optimization was.
