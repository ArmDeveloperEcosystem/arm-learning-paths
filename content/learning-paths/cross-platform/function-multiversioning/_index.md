---
title: Learn about function multiversioning

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers interested in optimizing their C/C++ applications across Arm64 targets.

learning_objectives:
    - Use hardware features to tune your applications at function level.
    - Create multiple versions of C/C++ functions for the targets that you intend to run applications on.
    - Assist the compiler in generating optimal code for the targets, or provide your own optimized versions at source level.
    - Automatically select the most appropriate function version at runtime.
    - Reuse your optimized application binaries across various targets.

prerequisites:
    - Basic knowledge of GNU function attributes. 
    - Familiarity with indirect functions (ifuncs).
    - Basic knowledge of loop vectorization.
    - Familiarity with Arm assembly.
    - A LLVM 19 compiler with runtime library support or GCC 14.

author_primary: Alexandros Lamprineas

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - C/C++
operatingsystems:
    - Linux
    - Android
    - macOS

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming
    - laptops-and-desktops
    - embedded-and-microcontrollers

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
