---
title: Processwatch 

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to build and run the Process Watch tool on their aarch64 machine. This tool can be used to see whether the system, or an individual workload, is making use of specific arm instructions/features.

learning_objectives: 
    - To be able to clone, build and run the Process Watch tool
    - Understand how Process Watch works
    - To be able to see in real-time whether any workloads are using specific Arm instructions/features

prerequisites:
    - An Arm-based system (bare metal server, cloud instance, developer board) running Linux with kernel version 5.8.0 or later
    - Root access, or the ability to run the sudo command

author_primary: Graham Woodward, Arm

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - bpftool
    - libbpf
    - Capstone
    - C/C++
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
