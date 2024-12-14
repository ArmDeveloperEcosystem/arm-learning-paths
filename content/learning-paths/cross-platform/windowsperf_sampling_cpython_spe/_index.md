---
title: Sample CPython with WindowsPerf and Arm SPE
draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who would like to learn about sampling CPU instructions with the Arm Statistical Profiling Extension (SPE).

learning_objectives:
    - Use WindowsPerf with a native Windows on Arm workload.
    - Describe the basic concepts of sampling with Arm SPE.
    - Explore the WindowsPerf command line.
    - Build CPython from sources for Windows on Arm (AArch64).

prerequisites:
    - Windows on Arm desktop or development machine with [WindowsPerf](/install-guides/wperf), [Visual Studio](/install-guides/vs-woa/), and [Git](/install-guides/git-woa/) installed.
    - The Windows on Arm system must have an Arm CPU with SPE support. 

author_primary: Przemyslaw Wirkus

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - WindowsPerf
    - Python
    - perf

## Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
