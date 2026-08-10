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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-10T19:36:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 43fec438e2d594603903bb8e8f98f9e2766bc385851ec8d292c090a82e42761f
  summary_generated_at: '2026-08-10T19:36:13Z'
  summary_source_hash: 43fec438e2d594603903bb8e8f98f9e2766bc385851ec8d292c090a82e42761f
  faq_generated_at: '2026-08-10T19:36:13Z'
  faq_source_hash: 43fec438e2d594603903bb8e8f98f9e2766bc385851ec8d292c090a82e42761f
  summary: >-
    You'll combine LLVM LTO with PGO to guide
    Clang optimization of an AArch64 C++ application on Linux. First, you'll prepare the toolchain and example. Then, you'll build Full-LTO and Thin-LTO variants and collect sample profiles with `perf`. You'll create frontend, IR-level, and context-sensitive profiles,
    merge and inspect profiles with LLVM tools, and apply each profile in optimized LTO builds.
  faqs:
  - question: What should I have in my workspace after the setup step?
    answer: >-
      You should have the `bsort.cpp` source file and two directories: `out` for objects and binaries,
      and `prof` for raw and converted profile data. Keep these locations separate so you can distinguish
      build artifacts from profiling data.
  - question: 'Which LTO mode should I use first: Full-LTO or Thin-LTO?'
    answer: >-
      Try both. Each mode emits LLVM bitcode during compilation but performs link-time optimization
      differently. Use the documented commands to build each mode and compare the results.
  - question: How do I know sample-based PGO data collection worked with `perf`?
    answer: >-
      Confirm that `perf` produced recording data that `llvm-profgen` can convert into an LLVM sample
      profile. If collection fails, check that your processor implements BRBE and that `perf` is
      available. You can use other sample sources, such as SPE or PMU events, with their own
      requirements.
  - question: Where does FE-PGO write its profile data and how is it used?
    answer: >-
      FE-PGO writes counters to a path you provide with `-fprofile-instr-generate`, typically under
      the `prof` directory. After running the instrumented binary, use `llvm-profdata` to convert and inspect the profile data.
      Then, use that profile in your next optimized Clang build.
  - question: How can I verify that an optimized build actually used LTO or a profile?
    answer: >-
      Check that your build invoked the appropriate LTO mode and included the profile-use option
      for your profile type, such as `-fprofile-sample-use` for S-PGO. You can also inspect objects
      or binaries with LLVM tools to review emitted bitcode or profile-driven metadata.
# END generated_summary_faq

author: Paschalis Mpeis

generate_summary_faq: false
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
