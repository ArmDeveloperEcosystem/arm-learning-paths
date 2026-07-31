---
title: Optimize C++ performance with Profile-Guided Optimization and Google Benchmark
description: Learn how to apply profile-guided optimization to C++ applications on Arm systems and measure performance improvements using Google Benchmark.

minutes_to_complete: 15

who_is_this_for: Developers looking to optimize C++ performance based on runtime behavior.

learning_objectives: 
    - Microbenchmark a function using Google Benchmark.
    - Apply profile-guided optimization to build performance-tuned binaries.

prerequisites:
    - Basic C++ understanding
    - Access to an Arm-based Linux machine

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:46:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4e7de348514d0b5a742fa47bb85a2a5814fa9bd587478e7ef08365d16273f6bf
  summary_generated_at: '2026-07-27T18:46:17Z'
  summary_source_hash: 4e7de348514d0b5a742fa47bb85a2a5814fa9bd587478e7ef08365d16273f6bf
  faq_generated_at: '2026-07-27T18:46:17Z'
  faq_source_hash: 4e7de348514d0b5a742fa47bb85a2a5814fa9bd587478e7ef08365d16273f6bf
  summary: >-
    You'll apply profile-guided optimization (PGO) to a C++ microbenchmark on an Arm-based Linux
    system with Google Benchmark. You'll build an instrumented binary with `-fprofile-generate`, run
    it to create `.gcda` files, and recompile with `-fprofile-use`. You'll compare benchmark timings
    before and after PGO, inspect the generated artifacts, and integrate PGO into either a Makefile or a
    continuous integration Github Actions workflow.
  faqs:
  - question: Which compiler flags do I use to collect and then apply profile data?
    answer: >-
      Build the instrumented binary with `-fprofile-generate`, run it to collect runtime data, then
      rebuild with `-fprofile-use`. This two-step cycle enables the compiler to use the collected
      profile during optimization.
  - question: What files should appear after I run the instrumented binary?
    answer: >-
      The run generates profile data files with a `.gcda` extension in the same directory. Use these
      files as inputs for the subsequent `-fprofile-use` build.
  - question: How do I know Google Benchmark is working for the example?
    answer: >-
      Google Benchmark runs managed iterations and reports timing results for the benchmarked
      function. You should see timing output you can compare across the non-PGO and PGO builds.
  - question: What should I check if the optimized build doesn’t seem to use PGO?
    answer: >-
      Verify that you ran the instrumented binary and that `.gcda` files exist in the build
      directory. Then confirm that the recompile used `-fprofile-use` in the same location where the
      the run generated the profile files.
  - question: Where should I apply PGO when adding it to a Makefile or GitHub Actions workflow?
    answer: >-
      Use PGO for performance-critical code that runtime behavior strongly influences. Avoid
      applying it broadly to early-stage code or highly variable workloads because the extra build
      steps add time and may not yield stable benefits.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - Google Benchmark
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: G++ profile-guided optimization documentation 
        link: https://gcc.gnu.org/onlinedocs/gcc-13.3.0/gcc/Instrumentation-Options.html
        type: documentation
    - resource:
        title: Google Benchmark Library 
        link: https://github.com/google/benchmark
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
