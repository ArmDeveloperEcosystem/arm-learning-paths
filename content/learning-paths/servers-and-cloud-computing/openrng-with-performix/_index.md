---
title: Accelerate random number generation with OpenRNG and Performix

description: Learn how to profile an example C++ data-processing workload on Arm Linux with Arm Performix, then accelerate random number generation using OpenRNG and Arm Performance Libraries.

draft: true
cascade:
    draft: true

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for C++ developers who want to profile a data-processing workload on Arm Linux, identify performance bottlenecks with Arm Performix, and accelerate random number generation using OpenRNG and Arm Performance Libraries.

learning_objectives:
    - Build and run a baseline C++ data-processing workload on Arm Linux
    - Use Arm Performix Code Hotspots to identify the highest-impact optimization target
    - Accelerate random number generation by integrating OpenRNG and Arm Performance Libraries
    - Measure performance improvements using a microbenchmark across multiple data sizes

prerequisites:
    - An Arm Linux (aarch64) server, such as an AWS Graviton3 instance
    - Basic understanding of C++ and CMake

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - CMake
    - Arm Performix
    - OpenRNG
    - Arm Performance Libraries
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: OpenRNG project repository
        link: https://gitlab.arm.com/libraries/openrng
        type: documentation
    - resource:
        title: Find code hotspots with Arm Performix
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: documentation
    - resource:
        title: Optimize application performance using Arm Performix CPU microarchitecture analysis
        link: /learning-paths/servers-and-cloud-computing/performix-microarchitecture/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---