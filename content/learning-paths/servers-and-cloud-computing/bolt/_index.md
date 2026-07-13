---
title: Optimize an application with BOLT
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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:38:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  summary_generated_at: '2026-06-30T21:38:54Z'
  summary_source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  faq_generated_at: '2026-06-30T21:38:54Z'
  faq_source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  summary: >-
    You'll use BOLT to post-link optimize an Arm Linux executable
    based on real execution profiles. First, you'll prepare a target system for profiling and optionally
    a separate build/BOLT system, then choose a profiling method — Perf samples, ETM, or SPE — to
    collect runtime behavior into a `perf.data` file. You'll convert the profile for BOLT, and run BOLT to reorder code layout and emit a new optimized executable. Finally, you'll compare the resulting binary against
    the original to observe improvements.
  faqs:
  - question: How should I choose between Perf samples, ETM, and SPE for profiling?
    answer: >-
      Use the dedicated sections for each method. Perf samples provide general sampling data,
      while ETM and SPE record richer branch information. Follow the method that best fits your
      availability and profiling detail needs.
  - question: Can I profile on one Arm Linux system and run BOLT on another?
    answer: >-
      Yes. The target system runs the application and collects the profile, and a separate Linux
      system can build the application and run BOLT. Transfer the executable and the collected
      profile files between systems as needed.
  - question: What file should exist after recording with Perf before converting for BOLT?
    answer: >-
      Expect a `perf.data` file. Perf prints sample counts or data size when recording completes,
      which indicates that profiling output was captured and is ready for conversion.
  - question: What version of Perf do I need for the SPE workflow?
    answer: >-
      Use Linux Perf version 6.14 or later for SPE to capture the required branch stack information.
      Verify the version before recording so the profile contains all needed fields.
  - question: How do I check results after BOLT creates the optimized executable?
    answer: >-
      Run the same workload with the original and the optimized executables and compare outcomes.
      The optimized executable should show improved performance relative to the original after
      the steps are completed.
# END generated_summary_faq

author: Jonathan Davies

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

