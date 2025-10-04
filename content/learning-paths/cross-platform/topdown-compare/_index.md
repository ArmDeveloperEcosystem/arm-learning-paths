---
title: Compare Arm Neoverse and Intel x86 top-down performance analysis with PMU counters 

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to understand the similarities and differences between Arm Neoverse and Intel x86 top-down performance analysis using PMU counters, Linux Perf, and the topdown-tool. 

learning_objectives:
     - Compare Intel x86 4-level hierarchical top-down methodology with Arm Neoverse 2-stage approach using PMU counters
     - Execute performance analysis using Linux Perf on x86 and topdown-tool on Arm systems
     - Analyze Backend Bound, Frontend Bound, Bad Speculation, and Retiring categories across both architectures

prerequisites:
    - Familiarity with performance analysis on Linux systems using Perf and PMU counters
    - Access to Arm Neoverse and Intel x86 Linux systems for hands-on examples
    - Basic understanding of CPU pipeline concepts and performance bottlenecks

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
        title: Arm Neoverse V1 Top-down Methodology for Performance Analysis & Telemetry Specification
        link: https://community.arm.com/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/arm-neoverse-v1-top-down-methodology
        type: blog
    - resource:
        title: Performance Analysis and Tuning on Modern CPUs
        link: https://www.amazon.com/Performance-Analysis-Tuning-Modern-CPUs/dp/B0DNQZJ92S
        type: documentation
    - resource:
        title: How to use the Arm Performance Monitoring Unit and System Counter
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/arm_pmu/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
