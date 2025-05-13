---
title: Analyse cache behaviour with Perf C2C on Arm

minutes_to_complete: 15

who_is_this_for: Cloud developers who are looking to debug and optimise cache access patterns on cloud servers with perf c2c. 

learning_objectives: 
    - Learn basic C++ techniques to avoid false sharing with alignas()
    - Learn how to enable and use Arm_SPE
    - Learn how to investigate cache line performance with perf c2c

prerequisites:
    - Arm-based cloud instance with Arm Statistical Profiling Extension support
    - basic understanding on cache hierarchy and how efficient cache accessing impact performance.
    - Familiarity with the Linux Perf tool

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance
armips:
    - Neoverse
tools_software_languages:
    - Perf
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
