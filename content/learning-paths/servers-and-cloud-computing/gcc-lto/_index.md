---
title: Optimize performance using Link-Time Optimization with GCC

    
minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to improve application performance using link-time optimization (LTO) with the GCC toolchain.

learning_objectives:
    - Understand how link-time optimization (LTO) works and when to apply it
    - Enable and configure LTO with GCC compiler flags
    - Evaluate the performance and code size trade-offs of LTO

prerequisites:
    - An Arm Linux system (cloud instance, on-premises hardware, or a virtual machine)
    - A recent version of the [GCC toolchain](/install-guides/gcc/)

author: Victor Do Nascimento

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - GCC
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: GCC Wiki Link-Time Optimization
        link: https://gcc.gnu.org/wiki/LinkTimeOptimization
        type: website
    - resource:
        title: Gentoo Wiki LTO
        link: https://wiki.gentoo.org/wiki/LTO
        type: website
    - resource:
        title: SPEC CPU 2017 Benchmark Suite
        link: https://www.spec.org/cpu2017/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
