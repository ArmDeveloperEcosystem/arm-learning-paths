---

title: Implement Code level Performance Analysis using the PMUv3 plugin 

minutes_to_complete: 60

who_is_this_for: Engineers who want to carry out C/C++ performance analysis by instrumenting code at the block level.

learning_objectives: 
    - Generate a fine-grained, precise measurement of functions and other sections of code.
    - Instrument your code to analyze a single section or multiple sections using the provided instrumentation scenarios.
    - Run and collect performance metrics and raw event values for any of the 15 event groups (bundles) in a single run.
    - Use a tool to plot raw PMU event values along with KPI metric values such as MPKI, stalls, and IPC to aid performance visualization.

prerequisites:
    - An Arm-based computer running Linux.
    - Some familiarity with Linux application performance analysis.

author: Gayathri Narayana Yegna Narayanan

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - C
    - CPP
    - Python
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Arm Neoverse N2 PMU Guide
        link: https://developer.arm.com/documentation/PJDOC-466751330-590448/2-0/?lang=en
        type: documentation
    - resource:
        title: Arm CPU Telemetry Solution Topdown Methodology Specification
        link: https://developer.arm.com/documentation/109542/0100/?lang=en
        type: documentation
    - resource:
        title: Arm Neoverse N2 Core Telemetry Specification
        link: https://developer.arm.com/documentation/109215/0200/?lang=en
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
