---
title: Optimize Arm applications and shared libraries with BOLT
description: Learn how to optimize Arm application binaries and shared libraries using BOLT profile instrumentation, merge multiple profiles for improved coverage, and integrate optimized libraries.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for performance engineers and software developers targeting Arm platforms who want to optimize application binaries and shared libraries using BOLT.

learning_objectives: 
  - Instrument and optimize application binaries for individual workload features using BOLT
  - Collect and merge separate BOLT profiles to improve code coverage
  - Optimize shared libraries independently of application binaries
  - Integrate optimized shared libraries into applications
  - Evaluate and compare performance across baseline, isolated, and merged optimization scenarios

prerequisites:
  - An Arm-based Linux system with [BOLT](/install-guides/bolt/) and [Linux Perf](/install-guides/perf/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:38:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 84a8b96fe7df302e0a2a6e4645bbb6170b45a3e0b55e0ea3682ec47663d34819
  summary_generated_at: '2026-06-30T21:38:23Z'
  summary_source_hash: 84a8b96fe7df302e0a2a6e4645bbb6170b45a3e0b55e0ea3682ec47663d34819
  faq_generated_at: '2026-06-30T21:38:23Z'
  faq_source_hash: 84a8b96fe7df302e0a2a6e4645bbb6170b45a3e0b55e0ea3682ec47663d34819
  summary: >-
    You'll use BOLT with Linux Perf profiles to optimize an Arm application
    and its shared libraries. First, you'll instrument a MySQL server build to generate workload-specific
    profiles, create separate traces for read-heavy and write-heavy runs, and merge them to broaden
    code layout guidance. Then, you'll rebuild OpenSSL to make `libssl.so` and
    `libcrypto.so` suitable for BOLT, collect profiles, and apply optimizations independently
    from the main binary. Finally, you'll compare results across baseline, isolated, and merged
    scenarios using a consistent Sysbench configuration to assess the
    impact of application and library-level optimizations on throughput and latency.
  faqs:
  - question: What output should I expect after running an instrumented workload with BOLT?
    answer: >-
      BOLT produces a profile file in `.fdata` format, such as `profile-writeonly.fdata`. These files
      are later used to optimize the binary and can be merged to improve coverage.
  - question: Should I reuse the BOLT-instrumented mysqld binary for additional workloads or create
      a new one?
    answer: >-
      Either approach works. The steps allow reusing the previously instrumented binary or generating
      a new instrumented variant as long as you produce a new `.fdata` profile for each workload.
  - question: Which shared libraries are targeted for optimization, and what if the system copies
      are stripped?
    answer: >-
      The path optimizes `libssl.so` and `libcrypto.so`. If system libraries are stripped, rebuild
      OpenSSL from source with relocations enabled so BOLT can instrument and optimize them.
  - question: Do I need to rebuild the application to benefit from optimized shared libraries?
    answer: >-
      The shared libraries are optimized independently of the application binary. The path focuses
      on rebuilding OpenSSL for symbol information and then integrating the optimized libraries
      with the application.
  - question: What test configuration is used to compare baseline and BOLT-optimized results?
    answer: >-
      Sysbench is run with `--time=0 --events=10000` to complete exactly 10,000 requests per thread.
      Use this consistent configuration to compare baseline, application-only, and merged-with-library
      optimization scenarios.
# END generated_summary_faq

author: Gayathri Narayana Yegna Narayanan

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - BOLT
    - perf
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: BOLT README
        link: https://github.com/llvm/llvm-project/tree/main/bolt
        type: documentation
    - resource:
        title: BOLT - A Practical Binary Optimizer for Data Centers and Beyond
        link: https://research.facebook.com/publications/bolt-a-practical-binary-optimizer-for-data-centers-and-beyond/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

