---
title: "Get started with BOLT"

draft: true
cascade:
    draft: true

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for performance‑minded developers
    who have a compiled aarch64 Linux program and want to see if BOLT can make it run faster.

learning_objectives:
    - Identify whether a program is a good candidate for code layout optimization
    - Apply BOLT to optimize a small program with poor spatial locality
    - Use different profiling techniques, including BRBE, Instrumentation, SPE, and PMU events
    - Verify the impact of BOLT optimization using performance metrics


prerequisites:
    - An AArch64 system running Linux with [Perf](/install-guides/perf/) installed
    - Linux kernel version 6.17 or later for [BRBE](./brbe) profiling
    - Linux kernel version 6.14 or later for [SPE](./spe) profiling
    - GCC version 13.3 or later to compile the demo program ([GCC](/install-guides/gcc/) )
    - BOLT version [21.1.8](https://github.com/llvm/llvm-project/releases/tag/llvmorg-21.1.8) or later (download [zip](https://github.com/llvm/llvm-project/releases/download/llvmorg-21.1.8/LLVM-21.1.8-Linux-ARM64.tar.xz))
    - A system with enough performance counters for the [TopDown](/install-guides/topdown-tool) methodology, typically a non-virtualized instance


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



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
