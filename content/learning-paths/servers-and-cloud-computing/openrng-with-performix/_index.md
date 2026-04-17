---
title: Accelerate Random Number Generation with OpenRNG and Performix
description: Learn how to profile an example C++ data-processing workload on Arm Linux with Arm Performix, then accelerate random distribution generation using OpenRNG and Arm Performance Libraries.

draft: true
cascade:
    draft: true

minutes_to_complete: 45

who_is_this_for: This Learning Path is for C++ developers on Arm Linux who want to use profiling data to target optimization and speed up random number generation.

learning_objectives: 
    - Build and run a baseline C++ data-processing workload on Arm Linux
    - Use Arm Performix Code Hotspots to identify the highest-impact optimization target
    - Build the workload with OpenRNG and Arm Performance Libraries
    - Validate speedups with a microbenchmark sweep across multiple data sizes

prerequisites:
    - An Arm Linux (aarch64) system, such as AWS Graviton
    - Basic C++ and CMake knowledge

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
        title: Install Arm Performix
        link: https://learn.arm.com/install-guides/performix/
        type: documentation
    - resource:
        title: Install Arm Performance Libraries
        link: https://learn.arm.com/install-guides/armpl/
        type: documentation
    - resource:
        title: OpenRNG project repository
        link: https://gitlab.arm.com/libraries/openrng
        type: documentation
    - resource:
        title: Find Code Hotspots with Arm Performix
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---