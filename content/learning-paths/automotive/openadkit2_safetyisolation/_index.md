---
title: Prototype safety-critical isolation for autonomous driving systems on Neoverse

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This Learning Path is for experienced automotive engineers developing safety-critical systems. You'll learn how to accelerate ISO 26262-compliant development workflows using Arm-based cloud compute, containerized simulation, and DDS-based communication.

learning_objectives: 
    - Apply functional safety principles, including risk prevention, fault detection, and ASIL compliance, to build robust, certifiable automotive systems
    - Use DDS and a publish-subscribe architecture for low-latency, scalable, and fault-tolerant communication in autonomous driving systems
    - Implement distributed development by separating the simulation platform into independent,     safety-isolated components

prerequisites:
    - Access to two Arm-based Neoverse cloud instances, or a local Arm Neoverse Linux system with at least 16 CPUs and 32 GB of RAM
    - Completion of the [Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse](/learning-paths/automotive/openadkit1_container/) Learning Path
    - Basic familiarity with Docker

author: 
    - Odin Shen
    - Julien Jayat

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - Python
    - Docker
    - ROS2
    - DDS
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Functional Safety compute for the Software-defined Vehicle
        link: https://community.arm.com/arm-community-blogs/b/automotive-blog/posts/functional-safety-compute
        type: blog
    - resource:
        title: SOAFEE
        link: https://www.soafee.io/
        type: website
    - resource:
        title: V-model
        link: https://en.wikipedia.org/wiki/V-model
        type: documentation
    - resource:
        title: ISO 26262
        link: https://www.iso.org/standard/68383.html
        type: documentation
    - resource:
        title: Automotive Safety Integrity Level
        link: https://en.wikipedia.org/wiki/Automotive_Safety_Integrity_Level
        type: documentation
    - resource:
        title: What is Functional Safety?
        link: https://www.youtube.com/watch?v=R0CPzfYHdpQ
        type: video
    - resource:
        title: Eclipse Zenoh
        link: https://github.com/eclipse-zenoh/zenoh
        type: documentation
    - resource:
        title: Eclipse Cyclone DDS 
        link: https://github.com/eclipse-cyclonedds/cyclonedds
        type: documentation
    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
