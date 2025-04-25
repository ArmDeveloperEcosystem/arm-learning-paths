---
title: Write NEON intrinsics using GitHub Copilot to improve Adler32 performance

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for C/C++ developers who are interested in using GitHub Copilot to improve performance using NEON intrinsics.

learning_objectives: 
    - Use GitHub Copilot to write NEON intrinsics that accelerate the Adler32 checksum algorithm.

prerequisites:
    - An Arm computer running Linux with the GNU compiler (gcc) installed.
    - Visual Studio Code with the GitHub Copilot extension installed. 

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - GCC
    - Runbook

operatingsystems:
    - Linux
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming


further_reading:
    - resource:
        title: Arm C Language Extensions
        link: https://arm-software.github.io/acle/
        type: Documentation
    - resource:
        title: Adler-32 Checksum Algorithm
        link: https://en.wikipedia.org/wiki/Adler-32
        type: Article
    - resource:
        title: NEON Programming Quick Reference
        link: https://developer.arm.com/documentation/den0018/a
        type: Documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
