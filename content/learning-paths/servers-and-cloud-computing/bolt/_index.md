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
rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v2
  generated_at: '2026-05-08T16:31:30Z'
  generator: template
  source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  summary_generated_at: '2026-05-08T16:31:30Z'
  summary_source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  faq_generated_at: '2026-05-08T16:31:30Z'
  faq_source_hash: 2e9ac8a3c73b7d3d59fe6ba20fb6d61fc2b7e5e9320aaadc20af0a8bbb3ff959
  summary: >-
    Learn how to build, profile, and optimize Arm executables using BOLT post-link binary optimization
    to improve application performance through code layout improvements. It is designed for software
    developers who want to learn how to use BOLT on an Arm executable. By the end, you will be
    able to build an application which is ready to be optimized by BOLT, profile an application
    and collect performance information, and run BOLT to create an optimized executable. It focuses
    on tools and technologies such as BOLT, perf, and Runbook, Linux environments, and Arm platforms
    including Neoverse and Cortex-A. The main steps cover Overview of the BOLT optimization process,
    Prepare your BOLT environment, Use BOLT with Samples, Use BOLT with ETM, and Use BOLT with
    SPE.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build an application which is ready to be optimized by BOLT, profile an application
      and collect performance information, and run BOLT to create an optimized executable. Learn
      how to build, profile, and optimize Arm executables using BOLT post-link binary optimization
      to improve application performance through code layout improvements.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers who want to learn how to use BOLT
      on an Arm executable.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm based system running Linux with
      [BOLT](/install-guides/bolt/) and [Linux Perf](/install-guides/perf/) installed. The Linux
      kernel should be version 5.15 or later. Earlier kernel versions can be used, but some Linux
      Perf features may be limited or not available. For [SPE](./bolt-spe) the version should
      be 6.14 or later.; (Optional) A second, more powerful Linux system to build the software
      executable and run BOLT.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including BOLT, perf, and Runbook, Linux environments, and
      Arm platforms such as Neoverse and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview of the BOLT optimization process, Prepare
      your BOLT environment, Use BOLT with Samples, Use BOLT with ETM, and Use BOLT with SPE.
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
