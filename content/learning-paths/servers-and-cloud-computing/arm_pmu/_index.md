---
title: Learn how to access HW counters via the Performance Monitoring Unit (PMU)

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers who want to instrument HW event counters in their code.

learning_objectives:
    - Learn about the different options for accessing event counters from user space
    - Learn how to use PAPI to instrument event counters in code
    - Learn how to use the Linux perf_event_open system call to instrument event counters in code
    - Learn how to use the System Counter instead of the PMU if you just need to measure time/cycles

prerequisites:
    - Preferably a bare-metal or cloud metal instance because they expose more counters. That said, counting can work with VM based cloud instances depending on the events of interest

author_primary: Julio Suarez

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - PAPI
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
