---
title: "Mapping x86 vector extensions to Arm: a migration overview"

minutes_to_complete: 30

draft: true
cascade:
    draft: true

who_is_this_for: This is an advanced topic for software developers who want to learn how to migrate vectorized code to Arm.

learning_objectives:
     - Understand how Arm vector extensions, including NEON, Scalable Vector Extension (SVE), and Scalable Matrix Extension (SME) map to vector extensions from other architectures.
     - Start planning how to migrate your SIMD code to the Arm architecture.

prerequisites:
    - Familiarity with vector extensions, SIMD programming, and compiler intrinsics.
    - Access to Linux systems with NEON and SVE support. 

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

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming
    - automotive

further_reading:
    - resource:
        title: SVE Programming Examples
        link: https://developer.arm.com/documentation/dai0548/latest
        type: documentation
    - resource:
        title: Port Code to Arm Scalable Vector Extension (SVE)
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/sve
        type: website
    - resource:
        title: Introducing the Scalable Matrix Extension for the Armv9-A Architecture
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture
        type: website
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 1)
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Build adaptive libraries with multiversioning
        link: https://learn.arm.com/learning-paths/cross-platform/function-multiversioning/
        type: website
    - resource:
        title: SME Programmer's Guide
        link: https://developer.arm.com/documentation/109246/latest
        type: documentation
    - resource:
        title: Compiler Intrinsics
        link: https://en.wikipedia.org/wiki/Intrinsic_function
        type: website
    - resource:
        title: ACLE - Arm C Language Extension
        link: https://github.com/ARM-software/acle
        type: website
    - resource:
        title: Application Binary Interface for the Arm Architecture
        link: https://github.com/ARM-software/abi-aa
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
