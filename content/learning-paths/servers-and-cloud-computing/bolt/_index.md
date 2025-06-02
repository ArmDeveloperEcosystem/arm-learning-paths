---
title: Learn how to optimize an application with BOLT

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn how to use BOLT on an Arm executable.

learning_objectives: 
    - Build an application which is ready to be optimized by BOLT 
    - Profile an application and collect performance information
    - Run BOLT to create an optimized executable 

prerequisites:
    - An Arm based system running Linux with [BOLT](/install-guides/bolt/) and [Linux Perf](/install-guides/perf/) installed. The Linux kernel should be version 5.15 or later. Earlier kernel versions can be used, but some Linux Perf features may be limited or not available. 
    - (Optional) A second, more powerful Linux system to build the software executable and run BOLT.

author: Jonathan Davies

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
