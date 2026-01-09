---
title: Optimize C++ performance with Profile-Guided Optimization and Google Benchmark

minutes_to_complete: 15

who_is_this_for: Developers looking to optimize C++ performance on an Arm-based Windows device, based on runtime behavior.

learning_objectives: 
    - Microbenchmark a function using Google Benchmark.
    - Apply profile-guided optimization to build performance-tuned binaries for Windows on Arm.

prerequisites:
    - Basic C++ understanding.
    - Access to an Arm-based Windows machine.

author: Tom Dunkle

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
tools_software_languages:
    - Google Benchmark
    - Runbook
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: MSVC profile-guided optimization documentation
        link: https://learn.microsoft.com/en-us/cpp/build/profile-guided-optimizations?view=msvc-170
        type: documentation
    - resource:
        title: Google Benchmark Library 
        link: https://github.com/google/benchmark
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
