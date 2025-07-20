---
title: Prototyping Safety-Critical Isolation for Autonomous Application on Neoverse

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This Learning Path targets advanced automotive software engineers developing safety-critical systems. It demonstrates how to use Arm Neoverse cloud infrastructure to accelerate ISO-26262 compliant software prototyping and testing workflows.

learning_objectives: 
    - Learn the Functional Safety principles—including risk prevention, fault detection, and ASIL compliance—to design robust and certifiable automotive software systems.
    - Understand how DDS enables low-latency, scalable, and fault-tolerant data communication for autonomous driving systems using a publish-subscribe architecture.
    - Distributed Development for Functional Safety. Learn how to split the simulation platform into two independent units and leverage distributed development architecture to ensure functional safety.

prerequisites:
    - Two Arm-based Neoverse cloud instances or a local Arm Neoverse Linux computer with at least 16 CPUs and 32GB of RAM.
    - To have completed [Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse](/learning-paths/automotive/openadkit1_container/).
    - Basic knowledge of using Docker.

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
