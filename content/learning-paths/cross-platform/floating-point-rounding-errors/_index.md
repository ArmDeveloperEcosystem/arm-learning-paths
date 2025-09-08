---
title: Explore floating-point differences between x86 and Arm

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who are porting applications from x86 to Arm and want to understand how floating-point behavior differs between these architectures - particularly in the context of numerical consistency, performance, and debugging subtle bugs.

learning_objectives: 
    - Identify key differences in floating-point behavior between the x86 and Arm architectures. 
    - Recognize the impact of compiler optimizations and instruction sets on floating-point results.
    - Apply compiler flags and best practices to ensure consistent floating-point behavior across 
      platforms.

prerequisites:
    - Access to an x86 and an Arm Linux machine.
    - Familiarity with floating-point numbers.

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - C++
operatingsystems:
    - Linux
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: G++ Optimization Flags 
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
