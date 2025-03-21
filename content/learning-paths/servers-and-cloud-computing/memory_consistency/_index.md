---
title: Explore The Arm Memory Model & Thread Synchronization

minutes_to_complete: 150

who_is_this_for: This is an advanced topic for engineers looking for a practical way to test different thread synchronization approaches within the context of the Arm memory model.

learning_objectives:
    - Test snippets of thread synchronization assembly against the formal definition of the Arm Memory Model
    - Test snippets of thread synchronization assembly on Arm hardware to compare against the formal Arm Memory Model

prerequisites:
    - An understanding of different memory consistency models like Sequential Consistency, Weak Ordering, Relaxed Consistency, Processor Consistency, etc.
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
        title: Armv8 Barriers
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
