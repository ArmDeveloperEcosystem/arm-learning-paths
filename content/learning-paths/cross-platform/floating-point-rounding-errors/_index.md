---
title: Learn about floating point rounding on Arm

minutes_to_complete: 30

who_is_this_for: Developers porting applications from x86 to Arm who observe different floating point values on each platform.

learning_objectives: 
    - Understand the differences between floating point numbers on x86 and Arm. 
    - Understand factors that affect floating point behavior.
    - How to use compiler flags to produce predictable behavior.

prerequisites:
    - Access to an x86 and an Arm Linux machine.
    - Basic understanding of floating point numbers.

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - C++

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: G++ Optimisation Flags 
        link: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
        type: documentation
    - resource:
        title: Floating-point environment
        link: https://en.cppreference.com/w/cpp/numeric/fenv
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
