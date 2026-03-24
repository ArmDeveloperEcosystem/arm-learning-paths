---
title: Optimize application performance using Arm Performix CPU microarchitecture analysis


minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to learn performance analysis methodologies for Linux applications on Arm Neoverse-based servers.

learning_objectives:
    - Identify CPU pipeline bottlenecks using the Arm Performix CPU Microarchitecture recipe
    - Analyze instruction types and SIMD utilization using the Instruction Mix recipe
    - Optimize application performance using vectorization and compiler flags
    - Compare performance profiles to measure execution improvements

prerequisites:
    - An Arm Neoverse-based server running Linux (bare-metal or cloud bare-metal instance preferred for access to hardware performance counters)
    - Familiarity with Linux command line
    - Basic understanding of CPU performance concepts

author:
- Brendan Long
- Kieran Hejmadi
- Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - C
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: "Find CPU Cycle Hotspots with Arm Performix"
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: documentation
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest
        type: documentation
    - resource:
        title: "Port Code to Arm Scalable Vector Extension (SVE)"
        link: /learning-paths/servers-and-cloud-computing/sve/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
