---
title: Guidance To Enable MySQL PGO

minutes_to_complete: 30

who_is_this_for: for performance engineers who want to optimize the performance of MySQL workload on Arm Server.

learning_objectives:
    - learn steps to enable MySQL PGO on Arm server
    - see how much performance improved after enabling PGO on MySQL

prerequisites:
    - ubuntu 22.04 Linux system
    - gcc compiling tools installed on Linux system
    - MySQL client with sysbench setup

author_primary: Bolt Liu

### Tags
skilllevels: Introductory
subjects: Databases
armips:
    - Neoverse
tools_software_languages:
    - c++/c
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
