---
title: Explore performance gains by increasing the Linux kernel page size on Arm

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to modify the Linux kernel page size on Arm-based systems to improve performance for memory-intensive workloads.

learning_objectives:
  - Verify the current memory page size on your Arm-based system.
  - Install and switch to a Linux kernel with 64K page size support.
  - Verify that the new 64K page size is active.
  - Optionally, revert to the default 4K page size kernel.

prerequisites:
  - An Arm-based Linux system running Ubuntu, Debian, or CentOS.

author: Geremy Cohen

skill_level: Introductory
subjects: Performance and Architecture
    
armips:
    - Neoverse

operatingsystems:
    - Linux

tools_software_languages:
    - bash

further_reading:
    - resource:
        title: Understanding Memory Page Sizes on Arm64
        link: https://amperecomputing.com/tuning-guides/understanding-memory-page-sizes-on-arm64
        type: documentation
    - resource:
        title: Page (computer memory) – Wikipedia
        link: https://en.wikipedia.org/wiki/Page_(computer_memory)
        type: documentation
    - resource:
        title: Debian Kernel Source Guide
        link: https://www.debian.org/doc/manuals/debian-reference/ch05.en.html#_kernel_source
        type: documentation
    - resource:
        title: Ubuntu Kernel Build Docs
        link: https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel
        type: documentation
    - resource:
        title: CentOS Documentation
        link: https://docs.centos.org/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---