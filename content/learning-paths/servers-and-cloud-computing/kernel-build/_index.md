---
title: Build Linux kernels for Arm cloud instances

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers building custom Linux kernels on Arm servers and cloud instances.

learning_objectives:
    - Set up a build environment for compiling Linux kernels on Arm cloud instances
    - Build custom Linux kernels with various configurations using TuxMake
    - Install and verify custom-built kernels
    - Configure kernels for specific use cases, including 64 KB page sizes and Fastpath testing

prerequisites:
    - An Arm cloud instance with at least 24 vCPUs and 200 GB of free storage running Ubuntu 24.04 LTS
    - Understanding of kernel images and modules
    - Familiarity with GRUB bootloader and initramfs

author: Geremy Cohen

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - TuxMake

further_reading:
    - resource:
        title: TuxMake documentation
        link: https://tuxmake.org/
        type: documentation
    - resource:
        title: Linux kernel documentation
        link: https://www.kernel.org/doc/html/latest/
        type: documentation
    - resource:
        title: arm_kernel_install_guide repository
        link: https://github.com/geremyCohen/arm_kernel_install_guide
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
