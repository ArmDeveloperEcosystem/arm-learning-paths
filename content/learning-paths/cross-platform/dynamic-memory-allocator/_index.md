---
title: Write a Dynamic Memory Allocator

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for software developers learning about dynamic memory allocation for the first time, and who may have used malloc and free in C programming. It also provides a starting point to explore more advanced memory allocation topics.

learning_objectives:
- Explain how dynamic memory allocation and the C heap works
- Write a simple dynamic memory allocator
- Explain some of the risks of heap allocation in general

prerequisites:
- Familiarity with C programming, with a good understanding of pointers.
- A Linux machine to run the example code.

author_primary: David Spickett

test_images:
- ubuntu:latest
test_link: null
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Cortex-A
  - Neoverse
operatingsystems:
  - Linux
tools_software_languages:
  - C
  - Coding

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops
    - embedded-and-microcontrollers


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---