---
title: Optimize network interrupt handling on Arm servers

   
minutes_to_complete: 20

who_is_this_for: This is an introductory topic for developers and performance engineers who are interested in understanding how network interrupt patterns can impact performance on cloud servers.

learning_objectives:
   - Analyze the current interrupt request (IRQ) layout on an Arm Linux system
   - Experiment with different interrupt options and patterns to improve performance
   - Configure optimal IRQ distribution strategies for your workload
   - Implement persistent IRQ management solutions

prerequisites:
    - An Arm computer running Linux
    - Some familiarity with the Linux command line

author: Kiel Friedt

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Perf for Linux on Arm (LinuxPerf)
        link: https://learn.arm.com/install-guides/perf/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
