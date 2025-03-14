---
title: Build and test a custom Linux image on an FVP

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: >
  This is an advanced topic for developers who wish to run a Linux system (optionally using a custom kernel and
  a C library) on an Arm Fixed Virtual Platform (FVP) model. This learning path might be useful to follow if you want to test patches for the Linux kernel or Glibc prior to having hardware available.

learning_objectives:
  - Build the Linux kernel.
  - Install the Shrinkwrap tool, build firmware for the FVP and run it.
  - Configure and boot a Linux system on the FVP.
  - Configure guest OS and run Glibc tests.
  - Build Glibc and run tests on the system running on the FVP.

prerequisites:
  - An AArch64 or x86_64 Linux machine. The instructions in this Learning Path have been tested on AArch64 Linux machine running Ubuntu 24.04.

author: Yury Khrustalev

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
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
