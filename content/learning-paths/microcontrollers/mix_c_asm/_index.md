---
title: Processing Text in Mixed C/Assembly Language

minutes_to_complete: 20

author_primary: Ronan Synnott

who_is_this_for: This is an introductory topic for software developers interested in efficiently programming microcontrollers with C/Assembly.

learning_objectives: 
    - Write a mixed C program and assembly language subroutines for the microcontroller. 
    - Call the subroutines written in assembly in a C function.  
    - Use Arm register calling conventions when writing subroutines in assembly language.  
    - Use the debugger to view and analyse the processor state.  

## Setting to draft = true to hide this LP. Can it be deleted? Replication of content in //asm.
draft: true
cascade:
    draft: true

prerequisites:
    - Keil MDK IDE
    - Some familiarity with C/Assembly


### Tags
skilllevels: Introductory
subjects: Performance and Architecture 
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - Coding
    - Keil

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

---
