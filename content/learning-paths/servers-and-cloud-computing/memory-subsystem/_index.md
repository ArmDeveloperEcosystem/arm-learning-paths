---
title: Characterize the memory subsystem of an Arm Linux system using ASCT

description: Use ASCT to measure cache latency, streaming bandwidth, and coherency latency on Arm Neoverse systems, and compare results across Graviton generations.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to understand and characterize the CPU-side memory subsystem of Arm Linux systems.

learning_objectives:
    - Identify the core topology, cluster layout, and cache hierarchy of an Arm Linux system using standard tools
    - Measure cache and memory latency using a pointer-chase benchmark
    - Measure single-core and multi-core streaming bandwidth at each level of the memory hierarchy
    - Evaluate latency behavior under bandwidth pressure 
    - Compare results across Arm systems and draw conclusions

prerequisites:
    - Two or more Arm Linux systems with root or sudo access. The examples use AWS Graviton2 and Graviton4 instances, but other systems are possible
    - Arm System Characterization Tool (ASCT) installed on each system
    - A good understanding of CPU memory subsystems, including cache hierarchies, cache lines, and DRAM in the memory hierarchy

author: Jason Andrews

skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - ASCT
    - Perf
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Inside Nvidia GB10's Memory Subsystem, from the CPU Side
        link: https://chipsandcheese.com/p/inside-nvidia-gb10s-memory-subsystem
        type: blog
    - resource:
        title: Memory latency for application software developers
        link: /learning-paths/cross-platform/memory-latency/
        type: website
    - resource:
        title: Arm Neoverse N1 Software Optimization Guide
        link: https://developer.arm.com/documentation/109896/latest/
        type: documentation
    - resource:
        title: Arm Neoverse V2 Software Optimization Guide
        link: https://developer.arm.com/documentation/109898/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
