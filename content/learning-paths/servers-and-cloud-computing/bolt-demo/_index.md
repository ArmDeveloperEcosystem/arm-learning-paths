---
title: "Optimize AArch64 binaries with LLVM BOLT"


minutes_to_complete: 20

who_is_this_for: This is an introductory topic for developers who have compiled an AArch64 Linux application and want to evaluate whether LLVM BOLT can improve its runtime performance.


learning_objectives:
    - Identify whether a program is a good candidate for code layout optimization
    - Use LLVM BOLT to perform profile-guided post-link optimization of an AArch64 binary with poor spatial locality
    - Collect profile data using multiple techniques, including BRBE, instrumentation, SPE, and PMU event sampling
    - Evaluate the impact of BOLT optimizations using performance metrics and profiling data


prerequisites:
    - An AArch64 system running Linux with [perf](/install-guides/perf/) installed
    - Linux kernel version 6.17 or later to enable Branch Record Buffer Extension [BRBE](./brbe) profiling
    - Linux kernel version 6.14 or later for Arm Statistical Profiling Extension [SPE](./spe) support
    - GCC version 13.3 or later to compile the example program ([GCC](/install-guides/gcc/) )
    - LLVM BOLT version [21.1.8](https://github.com/llvm/llvm-project/releases/tag/llvmorg-21.1.8) or later (download [zip](https://github.com/llvm/llvm-project/releases/download/llvmorg-21.1.8/LLVM-21.1.8-Linux-ARM64.tar.xz))
    - A system with with sufficient hardware performance counters to use the [TopDown](/install-guides/topdown-tool) methodology. This typically requires running on bare metal rather than a virtualized environment.


author: Paschalis Mpeis

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - BOLT
    - perf

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: BOLT README
        link: https://github.com/llvm/llvm-project/tree/main/bolt
        type: documentation
    - resource:
        title: Arm Statistical Profiling Extension Whitepaper
        link: https://developer.arm.com/documentation/109429/latest/
        type: documentation
    - resource:
        title: Arm Topdown Methodology
        link: https://developer.arm.com/documentation/109542/02/Arm-Topdown-methodology
        type: documentation
    - resource:
        title: Optimizing Clang - A Practical Example of Applying BOLT
        link: https://github.com/llvm/llvm-project/blob/main/bolt/docs/OptimizingClang.md
        type: documentation
    - resource:
        title: Metrics by metric group in Neoverse V2
        link: https://developer.arm.com/documentation/109528/0200/Metrics-by-metric-group-in-Neoverse-V2
        type: documentation
    - resource:
        title: Arm® Architecture Reference Manual, for A-profile architecture
        link: https://developer.arm.com/documentation/ddi0487/latest
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
