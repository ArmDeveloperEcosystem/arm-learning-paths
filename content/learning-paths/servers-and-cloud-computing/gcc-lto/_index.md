---
title: LTO Optimization With GCC

draft: true
cascade:
    draft: true
    
minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers wishing to optimize code performance via link-time optimization using the GCC toolchain.

learning_objectives:
    - Understand the key concepts behind LTO
    - Understand how to employ the optimization in GCC
    - Develop some intuition as to the potential performance gains achievable

prerequisites:
    - A recent release of the GCC toolchain

author: Victor Do Nascimento, Arm

### Tags
skilllevels: Introductory
subjects: Compiler Optimization
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - GCC
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: GCC Wiki
        link: https://gcc.gnu.org/wiki/LinkTimeOptimization
        type: website
    - resource:
        title: Gentoo Wiki
        link: https://wiki.gentoo.org/wiki/LTO
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
