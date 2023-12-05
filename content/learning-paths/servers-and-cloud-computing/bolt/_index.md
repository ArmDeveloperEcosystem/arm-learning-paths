---
title: Learn how to optimise an executable with BOLT

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn how to use BOLT on an Arm executable

learning_objectives: 
    - Rebuild executable so that BOLT can optimise it
    - Collect performace profile of executable
    - Create an optimised executable using BOLT

prerequisites:
    - An Arm based system running Linux. Preferably the Linux Kernel needs to be 5.15 or later for all the perf options to work. Earlier versions can be used but you will be limited to what you record.
    - An install of [BOLT](/install-guides/bolt/)
    - An install of [Perf](/install-guides/perf/) preferably 5.15 or later
    - (Optional) A more powerful Linux build system

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
