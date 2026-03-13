---
title: Migrating x86_64 workloads to aarch64

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for embedded software developers looking at migrating Linux workloads to aarch64.

learning_objectives: 
    - Understand software migration methodology
    - Use different Arm compilers and libraries
    - Port applications containing compiler intrinsics

prerequisites:
    - Introductory understanding of software containers
    - Knowledge about building workflows
    - Access to an aarch64 or x86_64 machine running Linux

author: Kasper Mecklenburg

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - GCC
    - Arm Compiler for Linux
    - Docker
    - Neon

further_reading:
    - resource:
        title: Porting architecture specific intrinsics
        link: /learning-paths/cross-platform/intrinsics/
        type: blog
    - resource:
        title: SIMD-everywhere repository
        link: https://github.com/simd-everywhere/simde
        type: website
    - resource:
        title: Migrating applications to Arm servers
        link: /learning-paths/servers-and-cloud-computing/migration
        type: blog
    - resource:
        title: Port Code to Arm Scalable Vector Extension (SVE)
        link: /learning-paths/servers-and-cloud-computing/sve/
        type: blog

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---
