---
title: Profiling the Linux kernel with Arm Streamline

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: Software developers and performance engineers interested in profiling Linux kernel performance.

learning_objectives: 
    - Understand the importance of profiling Linux kernel modules.
    - Learn how to set up and use Arm Streamline for kernel profiling.
    - Gain hands-on experience in profiling both out-of-tree and in-tree kernel modules.
    - Learn to interpret profiling data to identify performance bottlenecks.
    - Understand the benefits of using the Statistical Profiling Extension (SPE) for enhanced profiling.

prerequisites:
    - Basic understanding of Linux kernel development and module programming
    - Arm-based Linux target device (such as a Raspberry Pi, BeagleBone, or similar board) with SSH access
    - Host machine that meets [Buildroot system requirements](https://buildroot.org/downloads/manual/manual.html#requirement)

author: Yahya Abouelseoud

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - Arm Streamline
    - Arm Performance Studio
    - Linux kernel
    - Performance analysis
operatingsystems:
    - Linux



further_reading:
    - resource:
        title: Streamline user guide 
        link: https://developer.arm.com/documentation/101816/latest/Capture-a-Streamline-profile/
        type: documentation
    - resource:
        title: Arm Performance Studio Downloads
        link: https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer#Downloads
        type: website
    - resource:
        title: Streamline video tutorial
        link: https://developer.arm.com/Additional%20Resources/Video%20Tutorials/Arm%20Mali%20GPU%20Training%20-%20EP3-3
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
