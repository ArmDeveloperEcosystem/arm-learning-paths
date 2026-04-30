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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:15Z'
  generator: template
  source_hash: 5f4b05e3d962476c67c4a4400c8fa71f04412f3f0354d5c3123f38af57791304
  summary: >-
    Learn how to compare Arm Neoverse and Intel x86 top-down performance analysis methodologies
    using PMU counters, Linux Perf, and topdown-tool to identify bottlenecks across architectures.
    It is designed for software developers and performance engineers who want to understand the
    similarities and differences between Arm Neoverse and Intel x86 top-down performance analysis
    using PMU counters, Linux Perf, and the topdown-tool. By the end, you will be able to compare
    Intel x86 multi-level hierarchical methodology with Arm Neoverse micro-architecture exploration
    methodology, execute performance analysis using Linux Perf on x86 and topdown-tool on Arm
    systems, and analyze Backend Bound, Frontend Bound, Bad Speculation, and Retiring categories
    across both architectures. It focuses on tools and technologies such as GCC, Clang, Perf,
    and topdown-tool, Linux environments, and Arm platforms including Neoverse. The main steps
    cover Analyze Intel x86 and Arm Neoverse top-down performance methodologies, Understand Intel
    x86 multilevel hierarchical top-down analysis, Understand Arm Neoverse top-down analysis,
    Evaluate cross-platform PMU counter differences, and Measure cross-platform performance with
    topdown-tool and Perf PMU counters.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will compare Intel x86 multi-level hierarchical methodology with Arm Neoverse micro-architecture
      exploration methodology, execute performance analysis using Linux Perf on x86 and topdown-tool
      on Arm systems, and analyze Backend Bound, Frontend Bound, Bad Speculation, and Retiring
      categories across both architectures. Learn how to compare Arm Neoverse and Intel x86 top-down
      performance analysis methodologies using PMU counters, Linux Perf, and topdown-tool to identify
      bottlenecks across architectures.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers and performance engineers who want to
      understand the similarities and differences between Arm Neoverse and Intel x86 top-down
      performance analysis using PMU counters, Linux Perf, and the topdown-tool.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Familiarity with performance analysis
      on Linux systems using Perf and PMU counters; Access to Arm Neoverse V2 and Intel x86 Linux
      systems to run the code example; Basic understanding of CPU pipeline concepts and performance
      bottlenecks.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including GCC, Clang, Perf, and topdown-tool, Linux environments,
      and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Analyze Intel x86 and Arm Neoverse top-down performance
      methodologies, Understand Intel x86 multilevel hierarchical top-down analysis, Understand
      Arm Neoverse top-down analysis, Evaluate cross-platform PMU counter differences, and Measure
      cross-platform performance with topdown-tool and Perf PMU counters.
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

