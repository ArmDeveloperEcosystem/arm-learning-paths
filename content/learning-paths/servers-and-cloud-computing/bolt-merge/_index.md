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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:27:14Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 84a8b96fe7df302e0a2a6e4645bbb6170b45a3e0b55e0ea3682ec47663d34819
  summary_generated_at: '2026-06-02T03:14:28Z'
  summary_source_hash: 84a8b96fe7df302e0a2a6e4645bbb6170b45a3e0b55e0ea3682ec47663d34819
  faq_generated_at: '2026-06-03T00:27:14Z'
  faq_source_hash: 84a8b96fe7df302e0a2a6e4645bbb6170b45a3e0b55e0ea3682ec47663d34819
  summary: >-
    This advanced path shows how to instrument and optimize Arm application binaries and shared
    libraries on Linux using BOLT and Linux perf. You will build the MySQL server (mysqld) from
    source, create an instrumented binary, run read- and write-heavy workloads to collect profiles,
    and merge the profiles to broaden coverage before applying BOLT optimizations. You will also
    rebuild OpenSSL to produce instrumentable libssl.so and libcrypto.so, optimize these libraries
    with BOLT, and integrate them into the application. Finally, you will use Sysbench with --time=0
    --events=10000 to compare baseline, isolated, and merged optimization scenarios. Prerequisite:
    an Arm-based Linux system with BOLT and Linux perf installed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm-based Linux system with BOLT and Linux Perf installed. The path builds and
      instruments MySQL and OpenSSL from source during the steps.
  - question: How do I generate profiles for BOLT to use with mysqld?
    answer: >-
      Instrument the MySQL server binary with BOLT, then run targeted workloads to collect profile
      data. The result is workload-specific .fdata files that BOLT uses to optimize code layout.
  - question: When should I merge profiles, and what does that produce?
    answer: >-
      After creating separate profiles for read-heavy and write-only workloads, merge them to
      broaden code coverage. The merged profile is then used to optimize the final mysqld binary.
  - question: What should I do if libssl.so or libcrypto.so are stripped and lack relocations?
    answer: >-
      Rebuild OpenSSL from source and include relocations so BOLT can instrument and optimize
      the libraries. The path shows configuring OpenSSL with the linker option -Wl,--emit-relocs.
  - question: How do I compare baseline and BOLT-optimized results?
    answer: >-
      Use Sysbench with --time=0 --events=10000 and run consistent read-only, write-only, and
      read+write tests. Compare the baseline binaries to BOLT-optimized binaries and to runs that
      include optimized shared libraries.
# END generated_summary_faq

author: Gayathri Narayana Yegna Narayanan

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

