---
title: Learn how to access hardware counters via the Performance Monitoring Unit (PMU)

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to instrument hardware event counters in their code.

learning_objectives:
    - Learn about the different options for accessing event counters from user space
    - Learn how to use Performance Application Programming Interface (PAPI) to instrument event counters in code
    - Learn how to use the Linux perf_event_open system call to instrument event counters in code
    - Learn how to use the System Counter instead of the Performance Monitoring Unit (PMU) if you just need to measure time/cycles

prerequisites:
    - Before starting, you will need a bare-metal or cloud metal instance as they expose more counters. A VM based cloud instances will also work depending on the events of interest

author_primary: Julio Suarez

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Performance Application Programming Interface (PAPI)
    - Linux Perf
    - perf_events
    - Assembly
    - C/C++
operatingsystems:
    - Linux
    - Bare-metal

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
