---
title: Optimize AArch64 code with LLVM Link-Time Optimization and Profile-Guided Optimization
    
description: Build and apply LLVM LTO, sample-based PGO, frontend PGO, IR-PGO, and CSIR-PGO workflows with Clang to optimize an AArch64 C++ application.
minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers who compile C or C++ applications on AArch64 Linux and want to use Link-Time Optimization (LTO) with Profile-Guided Optimization (PGO).


learning_objectives:
    - Understand how LTO and PGO guide LLVM optimizations.
    - Build Full-LTO and Thin-LTO binaries with Clang on AArch64.
    - Generate and inspect sample-based and instrumentation-based profiles.
    - Use each profile type to build and run an optimized example application.


prerequisites:
    - An AArch64 Linux system with LLVM installed. You need Clang, LLD, `llvm-bcanalyzer`, `llvm-profdata`, `llvm-profgen`, and `llvm-readelf` in your `PATH`. For setup instructions, see [LLVM toolchain for Linux on Arm](/install-guides/llvm/).
    - For the sample PGO workflow based on Branch Record Buffer Extension (BRBE), a processor that implements the BRBE, Linux kernel 6.17 or later, and Linux `perf`. Other sample-based PGO workflows can use sources such as Statistical Profiling Extension (SPE) or Performance Monitoring Unit (PMU) events and have different requirements.


author: Paschalis Mpeis

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

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
