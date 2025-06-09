---
title: Optimizing Arm binaries and libraries with LLVM-BOLT and profile merging

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: Performance engineers, software developers working on Arm platforms who want to optimize both application binaries and shared libraries using LLVM-BOLT.

learning_objectives: 
    - Instrument and optimize binaries for individual workload features using LLVM-BOLT.
    - Collect separate BOLT profiles and merge them for comprehensive code coverage.
    - Optimize shared libraries independently.
    - Integrate optimized shared libraries into applications.
    - Evaluate and compare application and library performance across baseline, isolated, and merged optimization scenarios.

prerequisites:
    - An Arm based system running Linux with BOLT and Linux Perf installed. The Linux kernel should be version 5.15 or later.
    - (Optional) A second, more powerful Linux system to build the software executable and run BOLT.

author: Gayathri Narayana Yegna Narayanan

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - BOLT
    - perf
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: BOLT README
        link: https://github.com/llvm/llvm-project/tree/main/bolt
        type: documentation
    - resource:
        title: BOLT - A Practical Binary Optimizer for Data Centers and Beyond
        link: https://research.facebook.com/publications/bolt-a-practical-binary-optimizer-for-data-centers-and-beyond/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

