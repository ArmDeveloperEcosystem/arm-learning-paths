---
title: Optimize SIMD code with vectorization-friendly data layout

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for C/C++ developers who are interested in improving the performance of SIMD code.

learning_objectives: 
    - Comprehend the importance of data layout when writing SIMD code

prerequisites:
    - An Arm computer running Linux and a recent version of Clang or the GNU compiler (gcc) installed.

author: Konstantinos Margaritis

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - GCC
    - Clang
    - Coding
operatingsystems:
    - Linux
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming


further_reading:
    - resource:
        title: Array of Structures (AoS), Structure of Arrays (SoA)
        link: https://en.wikipedia.org/wiki/AoS_and_SoA
        type: documentation
    - resource:
        title: Intrinsics
        link: https://developer.arm.com/architectures/instruction-sets/intrinsics/
        type: documentation
    - resource:
        title: Arm Neon Intrinsics Reference
        link: https://arm-software.github.io/acle/neon_intrinsics/advsimd.html 
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
