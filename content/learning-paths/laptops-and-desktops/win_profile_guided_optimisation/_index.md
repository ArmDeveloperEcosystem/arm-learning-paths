---
title: Optimize C++ applications on Windows on Arm using profile-guided optimization

description: Learn how to apply Profile-Guided Optimization (PGO) to build performance-tuned C++ binaries and measure improvements using Google Benchmark on Windows on Arm.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to optimize C++ application performance on Windows on Arm using profile-guided optimization (PGO).

learning_objectives: 
    - Microbenchmark a function using Google Benchmark
    - Apply profile-guided optimization to build performance-tuned binaries for Windows on Arm
    - Measure and compare performance improvements from PGO-optimized builds

prerequisites:
    - Familiarity with C++ development and compiling programs from the command line
    - A Windows on Arm machine with [Visual Studio](/install-guides/vs-woa/) and the C++ desktop development tools installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:21:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 55e17aeab68897d633eade0c99fa59b122004ab94bc02f0a72efb3dc3aea9787
  summary_generated_at: '2026-08-11T16:21:12Z'
  summary_source_hash: 55e17aeab68897d633eade0c99fa59b122004ab94bc02f0a72efb3dc3aea9787
  faq_generated_at: '2026-08-11T16:21:12Z'
  faq_source_hash: 55e17aeab68897d633eade0c99fa59b122004ab94bc02f0a72efb3dc3aea9787
  summary: >-
    You'll measure the impact of PGO on C++ code for Windows on Arm
    using MSVC and Google Benchmark. First, you'll review PGO concepts,
    create a microbenchmark, and record a baseline for an integer division routine. Then, you'll build an instrumented binary, run the binary to collect execution profiles, and rebuild with
    those profiles applied. Finally, you'll rerun the benchmark and compare results to the baseline
    to validate the effect of PGO and understand where hot paths benefit. By then end, you'll have
    a repeatable process that you can apply to similar C++ code on Windows on Arm.
  faqs:
  - question: Which command prompt should I use to run the build steps on Windows on Arm?
    answer: >-
      Open **ARM64 Native Tools Command Prompt**. Start PowerShell from there if needed, then navigate
      to your project directory before running build and benchmark steps.
  - question: What result should I capture from the baseline run?
    answer: >-
      Record the benchmark measurements for the division routine. You'll compare the same benchmark
      after rebuilding with PGO.
  - question: How do I compare baseline and PGO results?
    answer: >-
      Run the same division benchmark before and after rebuilding with the collected profile data.
      Keep the benchmark setup consistent, then compare the reported measurements to evaluate the
      impact of PGO.
  - question: How do I know that profile data was collected and applied?
    answer: >-
      Build an instrumented binary, run it to generate the execution profile, then rebuild using
      that profile. If you skip the run, the optimized build won't use profile information,
      and your comparison won't reflect PGO.
  - question: Why do the Learning Path benchmark integer division?
    answer: >-
      Division has higher latency and lower throughput than simple arithmetic on most CPU architectures,
      including Arm. The operation provides a clear baseline to observe the effect of PGO on a costlier operation.
# END generated_summary_faq

author: Tom Dunkle

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
tools_software_languages:
    - C
    - MSVC
    - Google Benchmark
    - PGO
operatingsystems:
    - Windows
armips:
    - Cortex-A

further_reading:
    - resource:
        title: MSVC profile-guided optimization documentation
        link: https://learn.microsoft.com/en-us/cpp/build/profile-guided-optimizations?view=msvc-170
        type: documentation
    - resource:
        title: Google Benchmark Library 
        link: https://github.com/google/benchmark
        type: documentation
    - resource:
        title: Windows on Arm developer documentation
        link: https://learn.microsoft.com/en-us/windows/arm/overview
        type: documentation
    - resource:
        title: Arm performance optimization resources
        link: https://learn.arm.com/learning-paths/laptops-and-desktops/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
