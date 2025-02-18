---
armips: null
author: David Spickett
layout: learningpathall
learning_objectives:
- Explain how dynamic memory allocation and the C heap works
- Write a simple dynamic memory allocator
- Explain some of the risks of heap allocation in general
learning_path_main_page: 'yes'
minutes_to_complete: 120
operatingsystems:
- Linux
prerequisites:
- Familiarity with C programming, with a good understanding of pointers.
- A Linux machine to run the example code.
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: Write a Dynamic Memory Allocator
tools_software_languages:
- C 
- Coding
- Arm Total Performance

further_reading:
    - resource:
        title: C Dynamic Memory Management Functions
        link: https://en.cppreference.com/w/c/memory
        type: documentation
    - resource:
        title: LLSoftSecBook chapter on Memory Vulnerabilities
        link: https://llsoftsec.github.io/llsoftsecbook/#memory-vulnerability-based-attacks
        type: website


weight: 1
who_is_this_for: This is an introductory topic for software developers learning about dynamic memory allocation for the first time,
  and who may have used malloc and free in C programming. It also provides a starting point to explore more advanced memory allocation topics.
shared_path: true
shared_between:
    - laptops-and-desktops
    - embedded-and-microcontrollers
---
