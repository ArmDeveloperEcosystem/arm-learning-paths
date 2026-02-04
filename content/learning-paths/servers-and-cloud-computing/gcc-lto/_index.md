---
title: Optimize performance using Link-Time Optimization with GCC

draft: true
cascade:
    draft: true
    
minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to improve application performance using link-time optimization (LTO) with the GCC toolchain.

learning_objectives:
    - Learn how link-time optimization works and when to use it
    - Enable and configure LTO with GCC compiler flags
    - Understand the performance and code size trade-offs of LTO

prerequisites:
    - A recent version of the GCC toolchain

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
