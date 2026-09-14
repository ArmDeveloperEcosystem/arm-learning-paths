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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T21:56:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 322453c85ded71ee9e362e1b0a6abf087e48ac10536477f4ff7ffcc0e29ca635
  summary_generated_at: '2026-09-10T21:56:06Z'
  summary_source_hash: 322453c85ded71ee9e362e1b0a6abf087e48ac10536477f4ff7ffcc0e29ca635
  faq_generated_at: '2026-09-10T21:56:06Z'
  faq_source_hash: 322453c85ded71ee9e362e1b0a6abf087e48ac10536477f4ff7ffcc0e29ca635
  summary: >-
    You'll analyze cache behavior on Arm cloud systems with Arm SPE and Perf C2C. First, you'll verify SPE and Linux `perf` access, then build aligned and unaligned versions of a multithreaded C example. Next, you'll compare runtimes with `perf stat` and use Perf C2C to identify contended cache lines and map them to source code. You'll finish by applying alignment changes to reduce false sharing.
  faqs:
  - question: How do I confirm that my Arm-based instance supports Arm SPE before collecting data?
    answer: >-
      Check that both the hardware and the kernel support Arm SPE and verify that Linux `perf` can
      access the relevant events. Run `sudo modprobe arm_spe_pmu` to confirm if the SPE kernel module is loaded. Run `ls /sys/bus/event_source/devices/ | grep arm_spe` to check if SPE is included in the kernel. 
  - question: Which build should I profile first with Perf C2C to observe false sharing?
    answer: >-
      Start with the unaligned version of the example to expose false sharing. Then, profile the
      cache-aligned version to compare results and confirm the impact of alignment.
  - question: What result should I expect when comparing the aligned and unaligned binaries?
    answer: >-
      Expect a runtime and counter difference between the two builds, with the unaligned version
      typically showing more cache-related contention. Exact values vary by system and load.
  - question: How do I know Perf C2C captured useful cache line information?
    answer: >-
      Look for a report that highlights shared or contended cache lines and maps addresses back
      to symbols or source locations. You should be able to identify which structures or lines
      of code are involved in the contention.
  - question: How can I troubleshoot similar performance between the aligned and unaligned builds?
    answer: >-
      Verify that the alignment changes are present in the compiled binaries and that multiple
      threads are actively updating shared data. Repeat measurements with `perf stat -r 3` for
      each binary and confirm that your SPE and `perf` setup is correct.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
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
