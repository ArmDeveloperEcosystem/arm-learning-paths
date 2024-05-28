---
title: Performance profiling for Neoverse

minutes_to_complete: 15

who_is_this_for: This is a get started guide for developers who want to measure the performance of applications running on Arm-based servers, and discover ways to optimize them.

learning_objectives: 
    - Understand Arm's top-down profiling methodology
    - Use Streamline CLI tools to capture performance data

prerequisites:
    - An Arm Neoverse-based (N1, N2 or V1) computer running Linux. The following host operating systems are supported - Amazon Linux 2023 or newer, Debian 10 or newer, RHEL 8 or newer, Ubuntu 20.04 or newer.

    - Before you begin, you can use the the [Arm Sysreport utility](https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/) to determine whether your system configuration supports hardware-assisted profiling. The `perf counters` entry in the generated report will indicate how many CPU counters are available. The `perf sampling` entry will indicate if SPE is available. You will achieve the best profiles in systems with at least 6 available CPU counters and SPE.

author_primary: Julie Gaskin

### Tags
skilllevels: Beginner, Intermediate
subjects: Performance profiling and optimization
armips:
    - Neoverse
tools_software_languages:
    - Streamline CLI
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
