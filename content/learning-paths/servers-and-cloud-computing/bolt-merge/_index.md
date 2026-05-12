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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 84a8b96fe7df302e0a2a6e4645bbb6170b45a3e0b55e0ea3682ec47663d34819
  summary: >-
    Learn how to optimize Arm application binaries and shared libraries using BOLT profile instrumentation,
    merge multiple profiles for improved coverage, and integrate optimized libraries. It is designed
    for performance engineers and software developers targeting Arm platforms who want to optimize
    application binaries and shared libraries using BOLT. By the end, you will be able to instrument
    and optimize application binaries for individual workload features using BOLT, collect and
    merge separate BOLT profiles to improve code coverage, and optimize shared libraries independently
    of application binaries. It focuses on tools and technologies such as BOLT, perf, and Runbook,
    Linux environments, and Arm platforms including Neoverse and Cortex-A. The main steps cover
    Overview, Instrument MySQL with BOLT, Run a new workload using BOLT and merge the results,
    Instrument shared libraries with BOLT, and Review the performance results.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will instrument and optimize application binaries for individual workload features using
      BOLT, collect and merge separate BOLT profiles to improve code coverage, and optimize shared
      libraries independently of application binaries. Learn how to optimize Arm application binaries
      and shared libraries using BOLT profile instrumentation, merge multiple profiles for improved
      coverage, and integrate optimized libraries.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for performance engineers and software developers targeting Arm
      platforms who want to optimize application binaries and shared libraries using BOLT.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm-based Linux system with [BOLT](/install-guides/bolt/)
      and [Linux Perf](/install-guides/perf/) installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including BOLT, perf, and Runbook, Linux environments, and
      Arm platforms such as Neoverse and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Instrument MySQL with BOLT, Run a new workload
      using BOLT and merge the results, Instrument shared libraries with BOLT, and Review the
      performance results.
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

