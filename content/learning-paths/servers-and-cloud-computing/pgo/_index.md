---
title: "Optimize AArch64 code with LLVM LTO and PGO"
description: Learn how to use LLVM Link-Time Optimization and Profile-Guided Optimization on AArch64 Linux.
minutes_to_complete: 45
aliases:
    - /learning-paths/servers-and-cloud-computing/pgo-test/

who_is_this_for: This is an introductory topic for developers who compile C or C++ applications on AArch64 Linux and want to use Link-Time Optimization (LTO) with Profile-Guided Optimization (PGO).


learning_objectives:
    - Understand the basics of Link-Time Optimization (LTO) and Profile-Guided Optimization (PGO)
    - Build Thin-LTO and Full-LTO binaries with Clang on AArch64
    - Generate instrumentation-based profile data with Clang on AArch64
    - Generate sample-based profile data with Clang on AArch64
    - Use generated profile data to optimize a small example application


prerequisites:
    - LLVM installed with Clang, LLD, `llvm-profdata`, and `llvm-profgen` available in your `PATH`. For setup instructions, see [LLVM toolchain for Linux on Arm](/install-guides/llvm/).
    - Linux kernel version 6.17 or later for the Branch Record Buffer Extension (BRBE) profile-guided optimization workflow


author: Paschalis Mpeis

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - Clang
    - LLVM
    - LTO
    - PGO
    - perf

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Clang profile-guided optimization
        link: https://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization
        type: documentation
    - resource:
        title: llvm-profdata command guide
        link: https://llvm.org/docs/CommandGuide/llvm-profdata.html
        type: documentation
    - resource:
        title: llvm-profgen command guide
        link: https://llvm.org/docs/CommandGuide/llvm-profgen.html
        type: documentation
    - resource:
        title: LLVM LTO
        link: https://llvm.org/docs/LinkTimeOptimization.html
        type: documentation
    - resource:
        title: LLVM Thin-LTO
        link: https://clang.llvm.org/docs/Thin-LTO.html
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
