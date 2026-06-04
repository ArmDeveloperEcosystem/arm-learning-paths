---
title: Learn how to optimize an application with BOLT
description: Learn how to build, profile, and optimize Arm executables using BOLT post-link binary optimization to improve application performance through code layout improvements.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn how to use BOLT on an Arm executable.

learning_objectives:
    - Build an application which is ready to be optimized by BOLT
    - Profile an application and collect performance information
    - Run BOLT to create an optimized executable

prerequisites:
    - An Arm based system running Linux with [BOLT](/install-guides/bolt/) and [Linux Perf](/install-guides/perf/) installed. The Linux kernel should be version 5.15 or later. Earlier kernel versions can be used, but some Linux Perf features may be limited or not available. For [SPE](./bolt-spe) the version should be 6.14 or later.
    - (Optional) A second, more powerful Linux system to build the software executable and run BOLT.

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:25:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  summary_generated_at: '2026-06-02T03:12:45Z'
  summary_source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  faq_generated_at: '2026-06-03T00:25:57Z'
  faq_source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  summary: >-
    This Learning Path shows how to build, profile, and post-link optimize an Arm Linux executable
    with BOLT. You will collect runtime profiles on an Arm-based target using Linux Perf (via
    samples, ETM, or SPE), convert the profile into the format BOLT expects, and run BOLT to produce
    a new optimized binary with improved code layout. You can work on a single Arm Linux system
    or split tasks across two systems, using a second, more powerful Linux host for building and
    running BOLT if preferred. Prerequisites include an Arm system running Linux with BOLT and
    Linux Perf installed, a kernel version 5.15 or later (earlier versions may limit Perf features),
    and for SPE, version 6.14 or later. Estimated time: about 30 minutes.
  faqs:
  - question: Do I need one or two Linux systems for this workflow?
    answer: >-
      You can complete all steps on a single Arm Linux system. Alternatively, profile on an Arm
      Linux target system and use a second, more powerful Linux system to build the executable
      and run BOLT.
  - question: 'Which profiling option should I choose: samples, ETM, or SPE?'
    answer: >-
      Use the samples method for a straightforward profile, ETM if ETM tracing is available, or
      SPE when you need SPE branch information. The SPE workflow requires Linux Perf version 6.14
      or later; follow the dedicated steps for each option.
  - question: What versions of Linux kernel and Perf are required before I start?
    answer: >-
      Use a Linux kernel version 5.15 or later; earlier kernels can work but some Perf features
      may be limited or unavailable. For SPE, use Linux Perf version 6.14 or later, and the prerequisites
      note that 6.14 or later is required for SPE.
  - question: How do I collect the performance profile and verify that it worked?
    answer: >-
      For samples, run: perf record -e cycles:u -o perf.data -- ./executable. For ETM, run: perf
      record -e cs_etm//u -o perf.data -- ./executable. Perf reports the total number of samples
      and/or the perf.data size; confirm that perf.data is created.
  - question: What does BOLT produce after profiling, and how is it used?
    answer: >-
      After collecting perf.data, convert the profile to BOLT’s format and run BOLT to create
      a new optimized executable. The optimized binary is saved separately, and the expected outcome
      is improved performance compared to the original executable.
# END generated_summary_faq

author: Jonathan Davies

### Tags
skilllevels: Introductory
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

