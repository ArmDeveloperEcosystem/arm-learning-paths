---
title: Learn about floating point rounding errors on Arm and x86

minutes_to_complete: 30

who_is_this_for: Developers porting applications from x86 to AArch64 who observe different results on each platform.

learning_objectives: 
    - Understand the differences between converting floating point numbers on x86 and Arm. 
    - Understand factors that affect floating point behaviour
    - Basic compiler techniques to produce predictable behaviour

prerequisites:
    - Access to an x86 and Arm-based machine
    - Basic understanding of floating point numbers
    - A C++/C compiler

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - C++



further_reading:
    - resource:
        title: G++ Optimisation Flags 
        link: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
