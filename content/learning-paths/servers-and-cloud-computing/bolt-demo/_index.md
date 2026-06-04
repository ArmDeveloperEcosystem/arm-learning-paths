---
title: "Optimize AArch64 binaries with LLVM BOLT"
description: Learn how to identify optimization candidates and apply LLVM BOLT post-link optimization to AArch64 binaries using BRBE, SPE, instrumentation, and PMU profiling techniques.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for developers who have compiled an AArch64 Linux application and want to evaluate whether LLVM BOLT can improve its runtime performance.


learning_objectives:
    - Identify whether a program is a good candidate for code layout optimization
    - Install LLVM BOLT on Linux
    - Use LLVM BOLT to perform profile-guided post-link optimization of an AArch64 binary with poor spatial locality
    - Collect profile data using multiple techniques, including BRBE, instrumentation, SPE, and PMU event sampling
    - Evaluate the impact of BOLT optimizations using performance metrics and profiling data


prerequisites:
    - An AArch64 system running Linux with [perf](/install-guides/perf/) installed
    - Linux kernel version 6.17 or later to enable Branch Record Buffer Extension ([BRBE profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/brbe/))
    - Linux kernel version 6.14 or later for Arm Statistical Profiling Extension ([SPE profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/spe/))
    - GCC version 13.3 or later to compile the example program ([GCC](/install-guides/gcc/) )
    - A system with with sufficient hardware performance counters to use the [TopDown](/install-guides/topdown-tool) methodology. This typically requires running on bare metal rather than a virtualized environment.


generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:26:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8654b656131bf1d529e11d85f874f7a81c01f7207340d2a606b6fd2d80bfad04
  summary_generated_at: '2026-06-02T03:13:32Z'
  summary_source_hash: 8654b656131bf1d529e11d85f874f7a81c01f7207340d2a606b6fd2d80bfad04
  faq_generated_at: '2026-06-03T00:26:35Z'
  faq_source_hash: 8654b656131bf1d529e11d85f874f7a81c01f7207340d2a606b6fd2d80bfad04
  summary: >-
    This introductory Learning Path shows how to assess AArch64 programs for code layout optimization
    and apply LLVM BOLT to a deliberately inefficient, BubbleSort-based example on Linux. You
    install LLVM BOLT (22.1.0 or later), prepare a small workspace, compile the example with GCC
    13.3 or later, and collect profiles using BRBE, SPE, instrumentation, and PMU event sampling.
    Using a subset of Arm TopDown indicators, you check for front-end bound behavior and poor
    instruction locality, then run BOLT to reorganize code layout. You finish by evaluating the
    effect using performance metrics and the collected profiling data. Prerequisites include an
    AArch64 Linux system with perf, recent kernels for BRBE/SPE, and sufficient hardware counters
    (typically on bare metal).
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an AArch64 Linux system with perf installed, GCC 13.3 or later, and sufficient
      hardware performance counters for TopDown analysis. BRBE profiling requires Linux 6.17 or
      later, and SPE profiling requires Linux 6.14 or later.
  - question: Which BOLT version should I install, and what if my package manager provides an
      older one?
    answer: >-
      Use LLVM BOLT 22.1.0 or later to access the required options and SPE profiling support.
      If your package manager is older, install BOLT from a prebuilt LLVM release and verify the
      installed version before continuing.
  - question: How should I set up the example and organize outputs?
    answer: >-
      Download bsort.cpp into a working directory and create subdirectories named out, prof, and
      heatmap. The out directory stores output binaries, while prof and heatmap hold profile data
      and generated visualizations.
  - question: How do I know if my application is a good candidate for BOLT?
    answer: >-
      Use hardware performance metrics and the Arm TopDown methodology to look for front-end bound
      behavior and poor code locality. If instruction delivery is inefficient, the program is
      a strong candidate for BOLT code layout optimization.
  - question: What does BRBE profiling capture and why is it useful here?
    answer: >-
      BRBE records the most recent taken branches in a circular buffer (typically 32 or 64 entries,
      depending on hardware). This edge-based, low-overhead data is well-suited for BOLT to derive
      code layout profiles.
# END generated_summary_faq

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

