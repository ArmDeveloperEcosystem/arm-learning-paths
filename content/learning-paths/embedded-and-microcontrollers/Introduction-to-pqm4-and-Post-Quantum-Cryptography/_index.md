---
title: Collection of Post-Quantum Cryptographic Algorithms for the ARM Cortex-M4

description: Learn how to implement and test post-quantum cryptographic algorithms on ARM Cortex-M4 microcontrollers using the pqm4 library.

minutes_to_complete: 120

who_is_this_for: This tutorial is for software developers and cryptography enthusiasts interested in implementing and testing post-quantum cryptographic algorithms on ARM Cortex-M4 microcontrollers.

learning_objectives:
    - Understand the design goals of the pqm4 library.
    - Set up the development environment for ARM Cortex-M4.
    - Implement and test post-quantum cryptographic algorithms.
    - Benchmark and profile cryptographic implementations.
    - Integrate new cryptographic schemes into the pqm4 framework.

prerequisites:
    - ARM Cortex-M4 development board (e.g., NUCLEO-L4R5ZI, STM32F4 Discovery)
    - Computer with Python 3.8 or higher
    - ARM toolchain (arm-none-eabi)
    - stlink and OpenOCD for flashing binaries
    - QEMU 5.2 or higher for simulation

author: 
    - Akash Malik

### Tags
skilllevels: Advanced
subjects: Performance and Architecture,cryptography
armips:
    - Cortex-M
operatingsystems:
    - Embedded Linux
    - macOS
tools_software_languages:
    - C
    - Python
    - ARM toolchain
    - stlink
    - QEMU

further_reading:
    - resource:
        title: PQCRYPTO Project
        link: https://pqcrypto.eu.org
        type: website
    - resource:
        title: PQClean GitHub Repository
        link: https://github.com/PQClean/PQClean
        type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
