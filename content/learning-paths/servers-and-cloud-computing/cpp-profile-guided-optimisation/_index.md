---
title: Optimize C++ performance with Profile-Guided Optimization and Google Benchmark
description: Learn how to apply profile-guided optimization to C++ applications on Arm systems and measure performance improvements using Google Benchmark.

minutes_to_complete: 15

who_is_this_for: Developers looking to optimize C++ performance based on runtime behavior.

learning_objectives: 
    - Microbenchmark a function using Google Benchmark.
    - Apply profile-guided optimization to build performance-tuned binaries.

prerequisites:
    - Basic C++ understanding.
    - Access to an Arm-based Linux machine.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:37:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4e7de348514d0b5a742fa47bb85a2a5814fa9bd587478e7ef08365d16273f6bf
  summary_generated_at: '2026-06-02T03:29:36Z'
  summary_source_hash: 4e7de348514d0b5a742fa47bb85a2a5814fa9bd587478e7ef08365d16273f6bf
  faq_generated_at: '2026-06-03T00:37:40Z'
  faq_source_hash: 4e7de348514d0b5a742fa47bb85a2a5814fa9bd587478e7ef08365d16273f6bf
  summary: >-
    Learn to measure and tune C++ code on Arm-based Linux systems using Profile-Guided Optimization
    (PGO) and Google Benchmark. You will compile an instrumented binary with GCC/G++ using -fprofile-generate,
    run it to emit profile data (.gcda), and rebuild with -fprofile-use to create a profile-tuned
    executable. An integer division example demonstrates microbenchmarking and comparing baseline
    versus PGO builds with Google Benchmark. The path also shows how to integrate PGO into a Makefile
    and a GitHub Actions workflow, with cautions on when PGO is appropriate. Prerequisites are
    basic C++ knowledge and access to an Arm-based Linux machine. Estimated time is 15 minutes;
    the approach applies to Arm environments, including cloud instances on AWS, Microsoft Azure,
    Google Cloud, or Oracle.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need basic C++ understanding and access to an Arm-based Linux machine. The path uses
      GCC/G++ and Google Benchmark to build and run the examples.
  - question: Which compiler options should I use for PGO with GCC/G++ and in what order?
    answer: >-
      First compile with -fprofile-generate to create an instrumented binary, then run that binary
      to collect profile data. Recompile the program with -fprofile-use to apply the collected
      data during optimization.
  - question: How do I know the profiling run succeeded and where are the files?
    answer: >-
      After running the instrumented binary, expect profile data files (typically .gcda) to appear
      in the same directory. Their presence indicates that execution generated the data needed
      for the -fprofile-use rebuild.
  - question: What will I benchmark in this path and why that example?
    answer: >-
      You will benchmark a simple integer division operation. Division is chosen because it is
      typically more expensive than addition, subtraction, or multiplication, making performance
      differences easier to observe.
  - question: When should I apply PGO in my project or CI workflow?
    answer: >-
      Use PGO for performance-critical code that is heavily influenced by runtime behavior, and
      consider integrating it via a Makefile or GitHub Actions. Be aware that PGO adds build steps
      and time, and it may not be ideal for early-stage development or highly variable workloads.
# END generated_summary_faq

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
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

