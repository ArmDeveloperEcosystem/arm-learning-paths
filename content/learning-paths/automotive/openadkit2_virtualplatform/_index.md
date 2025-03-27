---
title: Early Deployment of Automotive Functional Safety application on Neoverse V3AE

minutes_to_complete: 60

who_is_this_for: This is an advanced automotive software development topic, focusing on the early-stage development of mission-critical software on Arm RD-1 AE. It explores how to leverage virtual platform technology to meet functional safety regulations in software development.

learning_objectives:
    - Introduction to Automotive Functional Safety(ISO-26262). Understand the ISO-26262 architecture and the importance of a structured software development flow in achieving functional safety compliance.
    - Introduction to DDS (Data Distribution Service). Learn how DDS enables real-time, reliable communication between distributed automotive software components.
    - Distributed Development for Functional Safety. Learn how to split the simulation platform into two independent units and leverage distributed development architecture to ensure functional safety.

prerequisites:
    - Two Arm-based Neoverse cloud instances or a local Arm Neoverse Linux computer with at least 16 CPUs and 32GB of RAM.
    - Completion of the previous learning path. http://learn.arm.com/learning-paths/automotive/openadkit1_container/
    - A Corellium virtual platform account. https://www.corellium.com/
    - Basic knowledge of Docker operations.
author: 
    - Odin Shen
    - Julien Jayat

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse V3AE
tools_software_languages:
    - Python
    - Docker
    - ROS2
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: OpenAD Kit learning path
        link: https://learn.arm.com/learning-paths/automotive/openadkit1_container/
        type: documentation
    - resource:
        title: DDS 
        link: https://github.com/autowarefoundation/openadkit_demo.autoware/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
