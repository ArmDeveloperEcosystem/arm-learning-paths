---
title: Getting Started with CPU Affinity

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: Developers, performance engineers and system administrators looking to fine-tune the performance of their workload on many-core Arm-based systems.

learning_objectives: 
    - Create CPU Sets and implement directly into sourcecode
    - Understand the performance tradeoff when pinning threads with CPU affinity masks

prerequisites:
    - Intermediate understanding of multi-threaded object-orientated programming in C++ and Python
    - Foundational understanding of build systems and computer architecture

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - C++
    - Python
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Taskset Manual  
        link: https://man7.org/linux/man-pages/man1/taskset.1.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
