---
title: Implement post-quantum cryptography on Arm Cortex-M4
    
description: Learn how to implement and test post-quantum cryptographic algorithms on Arm Cortex-M4 microcontrollers using the pqm4 library.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for software developers and cryptography enthusiasts interested in implementing and testing post-quantum cryptographic algorithms on Arm Cortex-M4 microcontrollers.

learning_objectives:
    - Describe the design goals and supported algorithms of the pqm4 library.
    - Set up the development environment for Arm Cortex-M4.
    - Implement and test post-quantum cryptographic algorithms.
    - Benchmark and profile cryptographic implementations.
    - Integrate new cryptographic schemes into the pqm4 framework.

prerequisites:
    - Computer with Python 3.8 or higher
    - Arm GNU Toolchain [installed](/install-guides/gcc/arm-gnu/)
    - An Arm Cortex-M4 development board such as NUCLEO-L4R5ZI, NUCLEO-L476RG, or STM32F4 Discovery, with stlink or OpenOCD for flashing. Alternatively, install QEMU to simulate the hardware without a physical board.

author: 
    - Akash Malik
    - Odin Shen

### Tags
skilllevels: Advanced
subjects: Security
armips:
    - Cortex-M
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - C
    - Python
    - GCC
    - stlink
    - QEMU

further_reading:
    - resource:
        title: pqm4 GitHub Repository
        link: https://github.com/mupq/pqm4
        type: repository
    - resource:
        title: PQCRYPTO Project
        link: https://pqcrypto.eu.org
        type: website
    - resource:
        title: PQClean GitHub Repository
        link: https://github.com/PQClean/PQClean
        type: repository
    - resource:
        title: stlink open source STM32 programming toolset
        link: https://github.com/stlink-org/stlink
        type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
