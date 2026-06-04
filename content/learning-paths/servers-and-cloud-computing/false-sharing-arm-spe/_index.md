---
title: Analyze cache behavior with Perf C2C on Arm
description: Learn how to identify and fix false sharing issues using Perf C2C cache line analysis and Arm Statistical Profiling Extension on Arm-based cloud systems.

minutes_to_complete: 15

who_is_this_for: This topic is for performance-oriented developers working on Arm-based cloud or server systems who want to optimize memory access patterns and investigate cache inefficiencies using Perf C2C and Arm SPE.

learning_objectives: 
    - Identify and fix false sharing issues using Perf C2C, a cache line analysis tool.
    - Enable and use the Arm Statistical Profiling Extension (SPE) on Linux systems.
    - Investigate cache line performance with Perf C2C.

prerequisites:
    - Access to an Arm-based cloud instance with support for the Arm Statistical Profiling Extension (SPE).
    - A basic understanding of cache coherency and its impact on performance.
    - Familiarity with Linux Perf tools.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:50:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: dde32f5d14a877313a8b0aafec58acb09cd1e77f4fc9138b9e1bd6d9fedf250a
  summary_generated_at: '2026-06-02T03:47:24Z'
  summary_source_hash: dde32f5d14a877313a8b0aafec58acb09cd1e77f4fc9138b9e1bd6d9fedf250a
  faq_generated_at: '2026-06-03T00:50:12Z'
  faq_source_hash: dde32f5d14a877313a8b0aafec58acb09cd1e77f4fc9138b9e1bd6d9fedf250a
  summary: >-
    Learn how to detect and address false sharing on Arm-based cloud systems using Linux perf
    C2C and the Arm Statistical Profiling Extension (SPE). You will set up a Linux environment
    on an Arm Neoverse-based instance with SPE support, verify kernel and tool access to the required
    performance events, and compile a multithreaded C example that contrasts cache-aligned and
    unaligned data. Using perf stat and perf c2c, you will compare the two builds, investigate
    cache line behavior, and trace memory contention to source lines. Prerequisites include access
    to an Arm-based cloud instance with SPE, a basic understanding of cache coherency, and familiarity
    with Linux perf tools. No additional prerequisites are explicitly listed.
  faqs:
  - question: How do I know if my cloud instance supports Arm SPE?
    answer: >-
      Follow the setup steps to check both hardware and kernel support for SPE and to validate
      that Linux perf can access the required events. Choose an Arm-based instance that exposes
      SPE to the OS.
  - question: Which cloud platforms can I use for this path?
    answer: >-
      You can use an Arm-based instance on AWS, Microsoft Azure, Google Cloud, or Oracle, as long
      as the instance supports Arm SPE.
  - question: Which perf commands will I use during the analysis?
    answer: >-
      You will use perf stat to compare the runtime and metrics of aligned and unaligned binaries,
      and perf c2c to record and analyze cache line behavior and memory contention.
  - question: What result should I expect from the false sharing example?
    answer: >-
      After compiling and running both versions, expect a runtime difference and c2c analysis
      that highlights cache line contention in the unaligned case. The steps show how to relate
      those findings back to the source code.
  - question: What should I check if perf c2c does not show the expected events?
    answer: >-
      Verify that SPE is enabled and supported by your hardware and kernel, that the perf tools
      are installed, and that perf can access the necessary performance monitoring events as described
      in the setup section.
# END generated_summary_faq

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - perf
    - Runbook
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Arm Statistical Profiling Extension Whitepaper
        link: https://developer.arm.com/documentation/109429/latest/
        type: documentation
    - resource:
        title: Arm Topdown Methodology 
        link: https://developer.arm.com/documentation/109542/0100/Arm-Topdown-methodology
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

