---
title: Deploy Open AD Kit containerized autonomous driving simulation on Arm Neoverse

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for automotive developers, aimed at helping them accelerate autonomous driving software development before automotive hardware is available.

learning_objectives: 
    - Understand the SOAFEE architecture and its role in supporting Shift-Left software development strategies to optimize the autonomous driving development process.
    - Use the Autoware Open AD Kit simulation environment.
    - Run containerized workloads on Arm Neoverse processors with Docker, supporting execution on both cloud-based and on-premise servers.
    - Explore advanced configurations and future development prospects.
prerequisites:
    - An Arm Neoverse cloud instance, or a local Arm Neoverse Linux computer with at least 16 CPUs and 32GB of RAM.
    - Familiarity with Docker and Docker Compose.

author: Odin Shen

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
tools_software_languages:
    - Python
    - Docker
    - ROS 2
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Autoware OpenAD Kit demo project
        link: https://github.com/autowarefoundation/openadkit_demo.autoware/
        type: documentation
    - resource:
        title: SOAFEE (Scalable Open Architecture For Embedded Edge)
        link: https://soafee.io/
        type: documentation
    - resource:
        title: Autoware Foundation
        link: https://www.autoware.org/
        type: documentation
    - resource:
        title: ROS 2 Documentation
        link: https://docs.ros.org/en/humble/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
