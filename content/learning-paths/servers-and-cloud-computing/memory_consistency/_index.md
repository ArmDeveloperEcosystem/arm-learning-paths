---
title: Explore Thread Synchronization in the Arm Memory Model

minutes_to_complete: 150

who_is_this_for: This is an advanced topic for engineers seeking practical ways to test thread synchronization approaches in the Arm memory model.

learning_objectives:
    - Test thread synchronization assembly snippets against the formal definition of the Arm Memory Model.
    - Test thread synchronization assembly snippets on Arm hardware to compare against the formal Arm Memory Model, and compare the results. 

prerequisites:
    - An understanding of memory consistency models (such as Sequential Consistency, Weak Ordering, Relaxed Consistency, and Processor Consistency).
    - An understanding of thread synchronization.
    - An understanding of Arm assembly, general-purpose registers, and how to find information on Arm assembly instructions.
    - An understanding of memory barriers including acquire-release semantics.

author: Julio Suarez

skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
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
