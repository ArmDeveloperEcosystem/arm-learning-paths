---
title: Analyze cache behavior with Perf C2C on Arm

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

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
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
