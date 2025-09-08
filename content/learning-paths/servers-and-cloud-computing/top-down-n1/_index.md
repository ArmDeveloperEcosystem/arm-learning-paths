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

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - perf
    - Telemetry
<<<<<<< HEAD
    - Runbook

=======
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: "Arm Neoverse N1: Core Performance Analysis Methodology"
        link: https://armkeil.blob.core.windows.net/developer/Files/pdf/white-paper/neoverse-n1-core-performance-v2.pdf
        type: documentation
    - resource:
        title: "Arm Neoverse N1 PMU Guide"
        link: https://developer.arm.com/documentation/PJDOC-466751330-547673/r4p1/ 
        type: documentation
    - resource:
        title: "Introduction to Computer Architecture"
        link: https://www.arm.com/resources/education/education-kits/computer-architecture 
        type: book
    - resource:
        title: "Computer Architecture: A Quantitative Approach"
        link: https://www.amazon.com/Computer-Architecture-Quantitative-John-Hennessy/dp/012383872X
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
