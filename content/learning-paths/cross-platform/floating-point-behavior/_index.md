---
title: Understand floating-point behavior across x86 and Arm architectures

minutes_to_complete: 30

who_is_this_for: This is a topic for developers who are porting applications from x86 to Arm and want to understand floating-point behavior across these architectures. Both architectures provide reliable and consistent floating-point computation following the IEEE 754 standard.

learning_objectives: 
    - Understand that Arm and x86 produce identical results for all well-defined floating-point operations.
    - Recognize that differences only occur in special undefined cases permitted by IEEE 754.
    - Learn to recognize floating-point differences and make your code portable across architectures.

prerequisites:
    - Access to an x86 and an Arm Linux machine.
    - Familiarity with floating-point numbers.

author: 
    - Kieran Hejmadi
    - Jason Andrews

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - CPP
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
