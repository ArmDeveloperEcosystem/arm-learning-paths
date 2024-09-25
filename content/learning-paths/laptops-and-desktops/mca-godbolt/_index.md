---
title: Use LLVM Machine Code Analyzer to understand code performance

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for Arm developers who want to diagnose performance issues of Arm programs using LLVM Machine Code Analyzer (MCA) and Compiler Explorer.

learning_objectives:
    - Estimate the hardware resource pressure and the number of cycles taken to execute your code snippet using llvm-mca.
    - Understand how this estimate can help diagnose possible performance issues.
    - Use Compiler Explorer to run llvm-mca.

prerequisites:
    - Familiarity with Arm assembly.
    - LLVM version 16 or newer (to include Neoverse V2 support).

author_primary: Rin Dobrescu

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - assembly
    - llvm-mca
operatingsystems:
    - Linux
    - Windows
    - macOS


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
