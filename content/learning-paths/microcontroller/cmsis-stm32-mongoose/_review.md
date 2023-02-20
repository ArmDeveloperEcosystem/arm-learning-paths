---
review:
    - questions:
        question: >
            What is Makefile?
        answers:
            - A file used by GCC compiler to compile a firmware
            - A file used by `make` utility to automate firmware build
            - A file used by Git to fetch dependencies
        correct_answer: 2
        explanation: >
            Makefile contains list of commands to build and flash firmware

    - questions:
        question: What is the purpose of `sysinit.c` ?
        answers:
            - Contains firmware startup code
            - Contains `SysInit()` function, called by the startup code
            - Contains actual firmware functionality
        correct_answer: 2                   
        explanation: 

    - questions:
        question: What is the purpose of ARM and ST CMSIS headers?
        answers:
            - ARM CMSIS headers contain Cortex-M hardware desription, whilst ST CMSIS headers contain peripheral definitions for specific ST MCUs
            - ARM and ST CMSIS headers contain API functions to work with a specific MCU
        correct_answer: 1
        explanation: 

    - questions:
        question: What does Mongoose Network Library provide?
        answers:
            - Only API to parse HTTP requess and construct HTTP responses
            - Only API for HTTP and MQTT
            - Network drivers, network stack, API for HTTP/MQTT and more
        correct_answer: 3
        explanation: Mongoose Library provides full network software stack

    - questions:
        question: Is RTOS like FreeRTOS and network stack like lwIP required to use Mongoose Library?
        answers:
            - Yes. Mongoose Library requires a low-level IP stack to run on
            - No. Mongoose Library has its own built-in network stack and can run with or without RTOS. Alternatively, it can run on top of some other stack like lwIP
        correct_answer: 2
        explanation: Mongoose Library is flexible and can run autonomously, or use an external TCP/IP stack


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
title: "Review"                 # Always the same title
weight: 20                      # Set to always be larger than the content in this path
layout: "learningpathall"       # All files under learning paths have this same wrapper
---
