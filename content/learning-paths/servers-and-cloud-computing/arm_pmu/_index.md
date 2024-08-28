---
title: How to use the Arm Performance Monitoring Unit and System Counter

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to instrument hardware event counters or the system counter in software applications.

learning_objectives:
    - Understand different options for accessing counters from user space
    - Use the system counter to measure time in code
    - Use PAPI to instrument event counters in code
    - Use the Linux perf_event_open system call to instrument event counters in code
prerequisites:
    - An Arm computer running Linux. A bare metal or cloud metal instance is best because they expose more counters. You can use a virtual machine (VM), but fewer counters may be available. These instructions have been tested on the `a1.metal` instance type.

author_primary: Julio Suarez

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - PAPI
    - perf
    - Assembly
    - GCC
operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
