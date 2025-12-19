---
title: Memory latency for application software developers
minutes_to_complete: 40

who_is_this_for: This is an introductory topic for Arm developers who want to learn about memory latency and cache usage in application programming. 

learning_objectives: 
    - Explain the importance of memory latency and how to reduce its impact
    - Identify how cache alignment impacts performance
    - Use cache prefetching to improve performance

prerequisites:
    - An Arm computer running Linux with recent versions of Clang or GCC installed.

author: Konstantinos Margaritis

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - GCC
    - Clang
    - Runbook

operatingsystems:
    - Linux

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: Write a Dynamic Memory Allocator
        link: /learning-paths/cross-platform/dynamic-memory-allocator/
        type: website
    - resource:
        title: Memory Latency
        link: https://en.algorithmica.org/hpc/cpu-cache/latency/
        type: website
    - resource:
        title: Latency Numbers Every Programmer Should Know
        link: https://gist.github.com/jboner/2841832?permalink_comment_id=4123064#gistcomment-4123064
        type: website
    - resource:
        title: Colin Scott's Interactive latencies page
        link: https://colin-scott.github.io/personal_website/research/interactive_latency.html
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
