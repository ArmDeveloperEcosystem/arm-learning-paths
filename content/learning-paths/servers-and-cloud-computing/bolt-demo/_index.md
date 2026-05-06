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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 8654b656131bf1d529e11d85f874f7a81c01f7207340d2a606b6fd2d80bfad04
  summary: >-
    Learn how to identify optimization candidates and apply LLVM BOLT post-link optimization to
    AArch64 binaries using BRBE, SPE, instrumentation, and PMU profiling techniques. It is designed
    for developers who have compiled an AArch64 Linux application and want to evaluate whether
    LLVM BOLT can improve its runtime performance. By the end, you will be able to identify whether
    a program is a good candidate for code layout optimization, install LLVM BOLT on Linux, and
    use LLVM BOLT to perform profile-guided post-link optimization of an AArch64 binary with poor
    spatial locality. It focuses on tools and technologies such as BOLT and perf, Linux environments,
    and Arm platforms including Neoverse and Cortex-A. The main steps cover Understand BOLT optimization
    for Arm, Install BOLT on Linux, Prepare your environment, Identify programs for BOLT optimization,
    and Optimize with BRBE profiling.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will identify whether a program is a good candidate for code layout optimization, install
      LLVM BOLT on Linux, and use LLVM BOLT to perform profile-guided post-link optimization of
      an AArch64 binary with poor spatial locality. Learn how to identify optimization candidates
      and apply LLVM BOLT post-link optimization to AArch64 binaries using BRBE, SPE, instrumentation,
      and PMU profiling techniques.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers who have compiled an AArch64 Linux application
      and want to evaluate whether LLVM BOLT can improve its runtime performance.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An AArch64 system running Linux with
      [perf](/install-guides/perf/) installed; Linux kernel version 6.17 or later to enable Branch
      Record Buffer Extension ([BRBE profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/brbe/));
      Linux kernel version 6.14 or later for Arm Statistical Profiling Extension ([SPE profiling](/learning-paths/servers-and-cloud-computing/bolt-demo/spe/));
      GCC version 13.3 or later to compile the example program ([GCC](/install-guides/gcc/) );
      A system with with sufficient hardware performance counters to use the [TopDown](/install-guides/topdown-tool)
      methodology. This typically requires running on bare metal rather than a virtualized environment.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including BOLT and perf, Linux environments, and Arm platforms
      such as Neoverse and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand BOLT optimization for Arm, Install BOLT
      on Linux, Prepare your environment, Identify programs for BOLT optimization, and Optimize
      with BRBE profiling.
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

