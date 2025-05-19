---
title: Increasing Linux Kernel Page Size on Arm

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to modify the Linux kernel page size on Arm-based systems to improve performance for memory-intensive workloads.

learning_objectives:
  - Verify the current page size on your system.
  - Install the 64K page size kernel specific to your OS.
  - Verify the new 64K page size is active.
  - Revert to the default 4K page size kernel (optional).

prerequisites:
  - Arm-based Linux system  
  - Ubuntu [20.04 LTS or newer](https://releases.ubuntu.com/20.04/)  
  - Debian [11 “Bullseye” or newer](https://www.debian.org/releases/bullseye/)  
  - CentOS [9  or newer](https://www.centos.org/download/)  

author:
    - Geremy Cohen
    
layout: learning-path
author: Geremy Cohen

skill_level: Intermediate
subjects: Performance and Architecture
cloud_service_providers: Google Cloud
    
armips:
    - Neoverse

operatingsystems:
    - Linux

tools_software_languages:
    - bash

further reading:
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
    title: CentOS Kernel Modules Guide
    link: https://docs.centos.org/en-US/centos/install-guide/kernel-modules/
    type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---