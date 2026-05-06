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

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: dde32f5d14a877313a8b0aafec58acb09cd1e77f4fc9138b9e1bd6d9fedf250a
  summary: >-
    Learn how to identify and fix false sharing issues using Perf C2C cache line analysis and
    Arm Statistical Profiling Extension on Arm-based cloud systems. It is designed for performance-oriented
    developers working on Arm-based cloud or server systems who want to optimize memory access
    patterns and investigate cache inefficiencies using Perf C2C and Arm SPE. By the end, you
    will be able to identify and fix false sharing issues using Perf C2C, a cache line analysis
    tool, enable and use the Arm Statistical Profiling Extension (SPE) on Linux systems, and investigate
    cache line performance with Perf C2C. It focuses on tools and technologies such as perf and
    Runbook, Linux environments, Arm platforms including Neoverse, and cloud platforms such as
    AWS, Microsoft Azure, Google Cloud, and Oracle. The main steps cover Arm Statistical Profiling
    Extension and false sharing, Set up your environment for Arm SPE and Perf C2C profiling, False
    sharing example, and Perform root cause analysis with Perf C2C.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will identify and fix false sharing issues using Perf C2C, a cache line analysis tool,
      enable and use the Arm Statistical Profiling Extension (SPE) on Linux systems, and investigate
      cache line performance with Perf C2C. Learn how to identify and fix false sharing issues
      using Perf C2C cache line analysis and Arm Statistical Profiling Extension on Arm-based
      cloud systems.
  - question: Who is this Learning Path for?
    answer: >-
      This topic is for performance-oriented developers working on Arm-based cloud or server systems
      who want to optimize memory access patterns and investigate cache inefficiencies using Perf
      C2C and Arm SPE.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Access to an Arm-based cloud instance
      with support for the Arm Statistical Profiling Extension (SPE).; A basic understanding of
      cache coherency and its impact on performance.; Familiarity with Linux Perf tools.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including perf and Runbook, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Arm Statistical Profiling Extension and false sharing,
      Set up your environment for Arm SPE and Perf C2C profiling, False sharing example, and Perform
      root cause analysis with Perf C2C.
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

