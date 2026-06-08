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
    - Access to Arm Neoverse V2 and Intel x86 Linux systems to run the code example
    - Basic understanding of CPU pipeline concepts and performance bottlenecks

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:53:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5f4b05e3d962476c67c4a4400c8fa71f04412f3f0354d5c3123f38af57791304
  summary_generated_at: '2026-06-01T21:20:45Z'
  summary_source_hash: 5f4b05e3d962476c67c4a4400c8fa71f04412f3f0354d5c3123f38af57791304
  faq_generated_at: '2026-06-02T21:53:36Z'
  faq_source_hash: 5f4b05e3d962476c67c4a4400c8fa71f04412f3f0354d5c3123f38af57791304
  summary: >-
    This advanced Learning Path shows how to compare Arm Neoverse and Intel x86 top-down performance
    analysis on Linux using PMU counters. You will review Intel’s multilevel hierarchical model
    and Arm’s two-stage approach for Neoverse V2, then build and run a backend-bound C benchmark
    with GCC or Clang. Using Linux Perf on x86 and topdown-tool on Arm, you will collect and contrast
    Retiring, Bad Speculation, Frontend Bound, and Backend Bound metrics, and evaluate differences
    in slot-based accounting across the two architectures. Prerequisites include familiarity with
    Perf and PMU counters, access to both an Intel x86 and an Arm Neoverse V2 Linux system, and
    a basic understanding of CPU pipelines. Estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the cross-platform example?
    answer: >-
      You need access to both an Arm Neoverse V2 Linux system and an Intel x86 Linux system. Familiarity
      with Perf and PMU counters, and a basic understanding of CPU pipelines and bottlenecks,
      are expected.
  - question: Which tools should I install on each platform?
    answer: >-
      Install GCC or Clang and Perf on both systems. On Arm systems, also install topdown-tool;
      use your Linux distribution’s package manager for installation information.
  - question: How do I build and run the provided benchmark?
    answer: >-
      Copy the example source to a file named core-bound-div-chain.c and compile it with GCC or
      Clang. Run the resulting executable with an iterations argument as indicated by the code
      comment: ./core-bound-div-chain <iterations>.
  - question: What result should I expect when I run the benchmark?
    answer: >-
      The benchmark is intended to be backend/core-bound via an FP64 divide chain. Collect measurements
      with Perf on x86 and topdown-tool on Arm, and examine the Backend Bound, Frontend Bound,
      Bad Speculation, and Retiring categories.
  - question: How should I compare results across Arm and Intel given different counters and slot
      models?
    answer: >-
      Counter names and formulas differ, and Intel uses issue-slot accounting while Neoverse V2
      uses eight rename slots per cycle. Focus on comparing the shared top-level categories and
      methodology rather than one-to-one event mappings; details will differ for other Neoverse
      processors.
# END generated_summary_faq

author:
    - Jason Andrews

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
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

