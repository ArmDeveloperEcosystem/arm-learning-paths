---
title: Learn the Arm Neoverse N1 performance analysis methodology

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to learn about performance analysis methodology for Linux applications running on Arm Neoverse.

learning_objectives:
    - Understand sampling and counting for performance analysis
    - Learn commonly used hardware metrics
    - Analyze a sample application using the Arm Telemetry Solution and Linux Perf
    - Make an application code change and see improved performance

prerequisites:
    - An Arm Neoverse N1 computer running Linux. A bare metal or cloud metal instance is best because they expose more counters. You can use a virtual machine (VM), but it may offer fewer counters and some commands might not succeed. These instructions have been tested on the `a1.metal` instance type.

author_primary: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - perf
    - Telemetry

operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
