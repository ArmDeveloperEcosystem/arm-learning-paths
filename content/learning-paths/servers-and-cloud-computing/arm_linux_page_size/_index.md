---
title: Explore performance gains by increasing the Linux kernel page size on Arm

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to modify the Linux kernel page size on Arm-based systems to improve performance for memory-intensive workloads.

learning_objectives:
  - Explain the differences in page size configuration between Arm64 and x86 architectures.
  - Understand how page size affects memory efficiency and system performance.
  - Check the current memory page size on an Arm-based Linux system.
  - Install and boot into a Linux kernel configured with 64K page size support.
  - Confirm that the 64K page size is active.
  - Optionally revert to the default 4K page size kernel.

prerequisites:
  - Access to an Arm-based Linux system running Ubuntu, Debian, or CentOS.

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
        title: Computer Memory, Wikipedia page
        link: https://en.wikipedia.org/wiki/Page_(computer_memory)
        type: documentation
    - resource:
        title: Network setup, Debian Kernel Source Guide
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