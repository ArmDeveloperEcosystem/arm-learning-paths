---
title: Run Process watch on your Arm machine

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to build and run the Process Watch tool on an Arm-based machine.
learning_objectives: 
    - Build and run the Process Watch tool on your Arm machine.
    - Describe how Process Watch works.
    - Check in real-time whether any workloads are using specific Arm instructions or features.

prerequisites:
    - An Arm-based system (bare metal server, cloud instance, or developer board) running Linux with kernel version 5.8.0 or later.
    - Root access, or the ability to run the sudo command.

author: Graham Woodward

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
    - C
    - CPP
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Perf for Linux on Arm (LinuxPerf)
        link: /install-guides/perf/
        type: website
    - resource:
        title: Capstone 
        link: https://github.com/capstone-engine/capstone
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
