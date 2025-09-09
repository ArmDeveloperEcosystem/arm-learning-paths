---
title: Debug Arm Zena CSS Reference Software Stack with Arm Development Studio

draft: true
cascade:
    draft: true
    
description: Learn how to set up a debug environment for Arm Zena CSS Reference Software Stack

minutes_to_complete: 60

who_is_this_for: This topic is for software developers who wish to use Arm Development Studio to explore and debug the Arm Zena CSS Reference Software Stack.

learning_objectives: 
    - Set up debug configuration for the Arm Zena CSS FVP
    - Debug Runtime Security Engine (RSE) from boot time
    - Debug Safety Island (SI)
    - Debug Linux OS on Primary Compute cores
##    - Debug Linux application

prerequisites:
    - Ubuntu 22.04 host machine
    - Arm Development Studio 2024.1 (or later) and an appropriate license
    - A basic understanding of the Arm Zena CSS software stack and Arm processors

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: 
armips:
    - Arm Zena CSS
operatingsystems:
    - Linux
tools_software_languages:
    - Arm Development Studio


further_reading:
    - resource:
        title: Arm Zena Compute System (CSS)
        link: https://developer.arm.com/Compute%20Subsystems/Arm%20Zena%20Compute%20Subsystem
        type: website
    - resource:
        title: Arm Development Studio
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
