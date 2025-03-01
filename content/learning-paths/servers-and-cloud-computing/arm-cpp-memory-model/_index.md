---
title: Learn about the C++ Memory Model when Porting to Arm

minutes_to_complete: 45

who_is_this_for: Intermediate C++ developers who are looking to port and optimise their application from x86 to AArch64.

learning_objectives: 
    - Learn about the C++ memory model
    - Learn about the differences between the Arm and x86 memory model
    - Learn best practices for writing C++ on Arm to avoid race conditions

prerequisites:
    - Access to an x86 and AArch64 cloud instance
    - Intermediate understanding of C++

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - C++
    - ThreadSantizer (TSan)
operatingsystems:
    - Linux
    - Runbook

further_reading:
    - resource:
        title: C++ Memory Order Reference Manual 
        link: https://en.cppreference.com/w/cpp/atomic/memory_order
        type: documentation
    - resource:
        title: Thread Santiser Manual 
        link: Phttps://github.com/google/sanitizers/wiki/threadsanitizercppmanual
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
