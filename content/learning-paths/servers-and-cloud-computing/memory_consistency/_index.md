---
title: Explore Thread Synchronization in the Arm memory model

minutes_to_complete: 150

who_is_this_for: This is an advanced topic for developers seeking practical ways to test thread synchronization approaches in the Arm memory model.

learning_objectives:
    - Test thread synchronization assembly snippets against the formal definition of the Arm memory model.
    - Test thread synchronization assembly snippets on Arm hardware.
    - Compare the results of different thread synchronization approaches. 

prerequisites:
    - An understanding of memory consistency models (such as Sequential Consistency, Weak Ordering, Relaxed Consistency, and Processor Consistency).
    - An understanding of thread synchronization.
    - Familiarity with Arm assembly language, and the ability to find relevant information on Arm assembly instructions.
    - Familiarity with general-purpose registers.
    - Familiarity with memory barriers, including Acquire-Release Semantics.

author: Julio Suarez

skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Runbook
    - Herd7
    - Litmus7
    - Arm ISA

further_reading:
    - resource:
        title: Arm Architecture Reference Manual for A-profile architecture
        link: https://developer.arm.com/documentation/ddi0487/la
        type: documentation
    - resource:
        title: "Barriers, Learn the Architecture: Armv8-A Memory Systems."
        link: https://developer.arm.com/documentation/100941/0101/Barriers
        type: documentation
    - resource:
        title: Barrier Litmus Tests and Cookbook
        link: https://developer.arm.com/documentation/100941/0101/Barriers
        type: documentation
    - resource:
        title: diy7 documentation
        link: https://diy.inria.fr/doc/index.html
        type: documentation

weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
