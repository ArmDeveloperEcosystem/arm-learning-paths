---
title: Boost C++ performance by optimizing loops with boundary information

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for C++ developers who want to improve the runtime of loops using existing knowledge of the loop size.

learning_objectives: 
    - Learn how to communicate loop size constraints to the compiler for better optimization.
    - Understand how providing compile-time context can improve runtime performance.
    - Implement techniques to express loop boundaries that enable better code generation.
    - Compare and analyze the performance impact of providing loop size context.

prerequisites:
    - An Arm computer running Linux. You can also use a virtual machine from a [cloud service provider](/learning-paths/servers-and-cloud-computing/csp/).

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - CPP
    - Runbook
operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops

further_reading:
    - resource:
        title: GCC Optimization Options Documentation
        link: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
        type: documentation
    - resource:
        title: LLVM Loop Vectorization Guide
        link: https://llvm.org/docs/Vectorizers.html
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
