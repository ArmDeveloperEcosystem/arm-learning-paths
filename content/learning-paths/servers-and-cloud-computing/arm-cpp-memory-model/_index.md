---
title: Learn about the C++ memory model for porting applications to Arm

draft: true
cascade:
    draft: true

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for C++ developers porting applications from x86 to Arm and optimizing performance.

learning_objectives: 
    - Learn about the C++ memory model.
    - Learn about the differences between the Arm and x86 memory model.
    - Learn best practices for writing C++ on Arm to avoid race conditions.

prerequisites:
    - Access to an x86 and Arm cloud instance (virtual machine).
    - Proficiency in C++ programming.

author: Kieran Hejmadi

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - C++
    - ThreadSanitizer (TSan)
operatingsystems:
    - Linux
    - Runbook

further_reading:
    - resource:
        title: C++ Memory Order Reference Manual 
        link: https://en.cppreference.com/w/cpp/atomic/memory_order
        type: documentation
    - resource:
        title: Thread Sanitizer Manual 
        link: Phttps://github.com/google/sanitizers/wiki/threadsanitizercppmanual
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
