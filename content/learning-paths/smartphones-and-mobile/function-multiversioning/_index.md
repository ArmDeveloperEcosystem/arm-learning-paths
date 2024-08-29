---
title: Function Multiversioning

minutes_to_complete: 30

who_is_this_for: Developers who want to optimize their C/C++ applications across various Arm64 targets.

learning_objectives:
    - Take advantage of hardware features for tuning your applications at function level granularity.
    - Create multiple versions of C/C++ functions for the targets you intend to run your applications on.
    - Assist the compiler in generating better code for those targets, or provide your own optimized versions at the source level.
    - Automatically select the most appropriate function version for your host target at runtime.
    - Reuse your optimized application binaries across various targets.

prerequisites:
    - Basic knowledge of GNU function attributes. Familiarity with indirect functions (ifuncs) is a plus.
    - Basic understanding of loop vectorization.
    - Familiarity with Arm assembly.
    - LLVM 19 compiler with runtime library support or GCC 14.

author_primary: Arm

### Tags
skilllevels: Intermediate
subjects: Tuning
armips:
    - Armv8
    - Armv9
tools_software_languages:
    - C/C++
operatingsystems:
    - Linux
    - Android
    - macOS


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
