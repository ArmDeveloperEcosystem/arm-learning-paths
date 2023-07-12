---
title: Convert uvprojx-based projects to csolution

minutes_to_complete: 10

who_is_this_for: Users of MDK v5 who want to migrate to MDK v6.

learning_objectives: 
    - Import, convert, and build uvprojx-based projects in Keil Studio Desktop.
    - Convert and build uvprojx-based projects on the command line.

prerequisites:
    - Install [Keil Studio Desktop](../../../install-guides/keilstudio_vs/) on your machine.
    - Install [vcpkg](https://vcpkg.io/en/getting-started.html) for the command line flow.
    - The &micro;Vision project must use Arm Compiler 6 as the default toolchain. Arm Compiler 5 is not supported.

author_primary: Christopher Seidl

### Tags
skilllevels: Intermediate
subjects: Performance and Architecture
armips:
    - Cortex-M
tools_software_languages:
    - Keil MDK
    - CMSIS-Toolbox
operatingsystems:
    - Windows
    - Linux
    - macOS



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
