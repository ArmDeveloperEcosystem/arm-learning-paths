---
title: Build a Void Linux image on an FVP

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: >
  Developers who wish to run a Linux system (optionally using a custom kernel and
  a C library) on an Arm Fixed Virtual Platform (FVP) model. For example, this
  guide might be useful if you want to test patches for the Linux kernel or Glibc.

learning_objectives:
  - Build the Linux kernel.
  - Install the Shrinkwrap tool, build firmware for the FVP and run it.
  - Configure and boot a Linux system on the FVP.
  - Configure guest OS to make running Glibc tests easier.
  - Build Glibc and run tests on the system running on the FVP.

prerequisites:
  - An AArch64 or x86 machine running a Linux system. The instructions in this Learning Path have been tested on AArch64 running Ubuntu 24.02 and Debian 12.

author: Yury Khrustalev

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - AArch64
tools_software_languages:
    - Glibc
    - Shrinkwrap
    - Fast Models
operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
