---
title: "Optimize AArch64 binaries with LLVM BOLT"
description: Learn how to identify optimization candidates and apply LLVM BOLT post-link optimization to AArch64 binaries using BRBE, instrumentation, SPE, ETM, and PMU profiling techniques.

minutes_to_complete: 30

aliases:
    - /learning-paths/servers-and-cloud-computing/bolt-demo/

who_is_this_for: This is an introductory topic for developers who have compiled an AArch64 Linux application and want to evaluate whether LLVM BOLT can improve its runtime performance.

learning_objectives:
    - Identify whether a program is a good candidate for code layout optimization
    - Prepare an environment with LLVM BOLT on Linux
    - Use LLVM BOLT to perform profile-guided post-link optimization of an AArch64 binary with poor spatial locality
    - Collect profile data using multiple techniques, including BRBE, instrumentation, SPE, ETM, and PMU event sampling
    - Evaluate the impact of BOLT optimizations using performance metrics and profiling data

prerequisites:
    - An AArch64 system running Linux, such as an Arm AGI CPU platform, with [LLVM BOLT](/install-guides/llvm/#verify-bolt-tools) and [perf](/install-guides/perf/) installed
    - Linux kernel version 6.17 or later to enable Branch Record Buffer Extension ([BRBE profiling](/learning-paths/servers-and-cloud-computing/bolt/brbe/))
    - Linux kernel version 6.14 or later for Arm Statistical Profiling Extension ([SPE profiling](/learning-paths/servers-and-cloud-computing/bolt/spe/))
    - Linux kernel with Arm CoreSight enabled for Embedded Trace Macrocell ([ETM profiling](/learning-paths/servers-and-cloud-computing/bolt/etm/))
    - GCC version 13.3 or later to compile the example program ([GCC](/install-guides/gcc/) )
    - A system with sufficient hardware performance counters to use the [TopDown](/install-guides/topdown-tool) methodology. This typically requires running on bare metal rather than a virtualized environment.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:37:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8654b656131bf1d529e11d85f874f7a81c01f7207340d2a606b6fd2d80bfad04
  summary_generated_at: '2026-06-30T21:37:54Z'
  summary_source_hash: 8654b656131bf1d529e11d85f874f7a81c01f7207340d2a606b6fd2d80bfad04
  faq_generated_at: '2026-06-30T21:37:54Z'
  faq_source_hash: 8654b656131bf1d529e11d85f874f7a81c01f7207340d2a606b6fd2d80bfad04
  summary: >-
    You'll apply LLVM BOLT post-link optimization to AArch64 binaries
    using profile-guided code layout. Starting with a deliberately inefficient BubbleSort workload
    to make instruction locality issues visible, you'll verify a suitable BOLT
    installation, set up a working directory, and gather profiles with BRBE, instrumentation,
    SPE, ETM, or PMU sampling. Using a small set of Arm TopDown indicators, you'll judge
    whether a program is front-end bound and a good candidate for BOLT. You'll then run BOLT with
    collected profiles to reorganize code layout and evaluate the impact using performance
    metrics and profiling data to confirm improvements in instruction delivery and locality.
  faqs:
  - question: Which BOLT version should I use if my package manager installs an older release?
    answer: >-
      Use LLVM BOLT 22.1.0 or later. If your distribution provides an older version,
      install LLVM from a prebuilt release using the [LLVM install guide](/install-guides/llvm/#install-llvm-releases).
  - question: Where do the example’s build and profiling outputs go?
    answer: >-
      You'll find outputs in three directories: out for binaries, prof for profile data,
      and heatmap for visualization artifacts. Keeping these separate makes it easier to rerun
      steps and compare results.
  - question: How do I know if my program is a good candidate for BOLT?
    answer: >-
      Check a small set of Arm TopDown indicators related to instruction delivery and code locality.
      Programs that appear front-end bound, with inefficient instruction fetch and poor locality,
      are strong candidates for code layout optimization with BOLT.
  - question: What should I use if my system doesn't meet the BRBE, SPE, or ETM requirements?
    answer: >-
      Use the profiling method supported by your system. If BRBE, SPE, or ETM are unavailable,
      you can use instrumentation or PMU event sampling to collect profiles.
  - question: What result should I expect after running BOLT with profiles?
    answer: >-
      You should be able to evaluate changes using performance metrics and profiling data. Look
      for improvements in instruction delivery indicators and evidence of better code locality
      in the optimized binary.
# END generated_summary_faq

author: Paschalis Mpeis, Jonathan Davies

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
    - Arm AGI
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
