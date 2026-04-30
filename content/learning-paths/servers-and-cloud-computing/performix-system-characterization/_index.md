---
title: Characterize system performance with Arm Performix

description: Learn how to run the Arm Performix System Characterization recipe to benchmark memory latency and bandwidth on Arm hardware and interpret the generated results.

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers and performance engineers who want to characterize the hardware performance of Arm-based Linux systems using Arm Performix.

learning_objectives:
    - Run Arm Performix's System Characterization recipe to understand hardware configuration and performance
    - Interpret memory latency and bandwidth benchmark results
    - Locate and interpret the generated plots and raw benchmark data in the output directory

prerequisites:
    - An Arm Linux target machine accessible via SSH to characterize.

author:
- Brendan Long
- David Wong

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - Arm System Characterization Tool
    - Runbook

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: "Find CPU Cycle Hotspots with Arm Performix"
        link: /learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/
        type: website
    - resource:
        title: Arm Performix User Guide
        link: https://developer.arm.com/documentation/110163/latest
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
