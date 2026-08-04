---
title: Compare Arm Neoverse and Intel x86 top-down performance analysis with PMU counters 

minutes_to_complete: 30

description: Learn how to compare Arm Neoverse and Intel x86 top-down performance analysis methodologies using PMU counters, Linux Perf, and topdown-tool to identify bottlenecks across architectures.

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to understand the similarities and differences between Arm Neoverse and Intel x86 top-down performance analysis using PMU counters, Linux Perf, and the topdown-tool. 

learning_objectives:
     - Compare Intel x86 multi-level hierarchical methodology with Arm Neoverse micro-architecture exploration methodology
     - Execute performance analysis using Linux Perf on x86 and topdown-tool on Arm systems
     - Analyze Backend Bound, Frontend Bound, Bad Speculation, and Retiring categories across both architectures

prerequisites:
    - Familiarity with performance analysis on Linux systems using Perf and PMU counters
    - Access to an Arm Neoverse V3 system, such as the Arm AGI CPU platform, and an Intel x86 Linux system to run the comparative code examples
    - Basic understanding of CPU pipeline concepts and performance bottlenecks

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:51:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5f4b05e3d962476c67c4a4400c8fa71f04412f3f0354d5c3123f38af57791304
  summary_generated_at: '2026-07-29T16:51:46Z'
  summary_source_hash: 5f4b05e3d962476c67c4a4400c8fa71f04412f3f0354d5c3123f38af57791304
  faq_generated_at: '2026-07-29T16:51:46Z'
  faq_source_hash: 5f4b05e3d962476c67c4a4400c8fa71f04412f3f0354d5c3123f38af57791304
  summary: >-
    You'll compare Intel x86 and Arm Neoverse top-down performance analysis with PMU counters. You'll examine
    slot-based accounting—four issue slots per cycle on Intel and eight rename slots on Neoverse V2—
    and interpret Retiring, Bad Speculation, Frontend Bound, and Backend Bound. Then, you'll build an FP64
    divide-chain benchmark, collect results with Linux Perf and `topdown-tool`, and compare top-level category
    percentages.
  faqs:
  - question: Which tool should I use to collect top-down metrics on each system?
    answer: >-
      Use Linux Perf on Intel x86 systems and `topdown-tool` on Arm systems. Both systems need Perf.
      Arm systems also need `topdown-tool`.
  - question: How do I build and run the example benchmark?
    answer: >-
      Save the code as `core-bound-div-chain.c`, compile it with GCC or Clang, and run it as
      `./core-bound-div-chain <iterations>`.
  - question: What result should I expect when I profile the example workload?
    answer: >-
      The tools report Retiring, Bad Speculation, Frontend Bound, and Backend Bound. The FP64
      divide-chain example is designed to show a prominent Backend Bound category.
  - question: How do I compare results across Intel and Arm given different slot definitions?
    answer: >-
      Compare the top-level category percentages instead of raw event counts. Intel uses four issue
      slots per cycle, while Neoverse V2 uses eight rename slots. The accounting changes, but the
      category meanings remain comparable.
  - question: What should I check if my Intel and Arm breakdowns look very different?
    answer: >-
      Verify that you ran the same benchmark with the same iteration count, using Perf on x86 and
      `topdown-tool` on Arm. Microarchitecture and event-formula differences are expected, so focus
      on the relative distribution across the four categories.
# END generated_summary_faq

author:
    - Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
platforms:
    - Arm AGI
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - GCC
    - Clang
    - Perf
    - topdown-tool

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - automotive

further_reading:
    - resource:
        title: Arm Neoverse V2 Core Telemetry Specification
        link: https://developer.arm.com/documentation/109528/0200/?lang=en
        type: documentation
    - resource:
        title: Arm Neoverse V2 Software Optimization Guide
        link: https://developer.arm.com/documentation/109898/latest/
        type: documentation
    - resource:
        title: Performance Analysis and Tuning on Modern CPUs
        link: https://www.amazon.com/Performance-Analysis-Tuning-Modern-CPUs/dp/B0DNQZJ92S
        type: documentation
    - resource:
        title: How to use the Arm Performance Monitoring Unit and System Counter
        link: /learning-paths/servers-and-cloud-computing/arm_pmu/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
