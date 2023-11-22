---
title: Learn how to optimise an executable with BOLT

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn how to use BOLT on an Arm executable

learning_objectives: 
    - Build executable in a way that BOLT can optimise
    - How to collect profiling information of target executable
    - Optimise an executable using BOLT and the profile information

prerequisites:
    - An Arm based machine running Linux. Preferably the Linux Kernel needs to be 4.20 or later for all the perf options to work. Earlier versions can be used but you will be limited to what you record.
    - An install of [BOLT](/install-guides/bolt/)
    - Install [Perf](/install-guides/perf/) preferably 4.20 or later
    - (Optional) A more powerful build machine, Arm or x86 architecture

author_primary: Jonathan Davies

### Tags
skilllevels: Introductory
subjects: Optimisation
armips:
    - Aarch64
tools_software_languages:
    - BOLT
    - perf
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
