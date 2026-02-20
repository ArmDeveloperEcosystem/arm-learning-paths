---
title: Understand Arm Pointer Authentication

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers interested in understanding Arm Pointer Authentication.

learning_objectives:
    - Create a simple application on an Arm server with Pointer Authentication
    - Compile the application with and without Pointer Authentication to inspect the instructions generated
    - Exploit the applications with and without Pointer Authentication to demonstrate how Pointer Authentication instructions enhance security.

prerequisites:
    - An Arm based instance from a cloud service provider, or an on-premise Arm server.
    - If needed, review [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) to learn how to deploy Arm in the cloud. These learning paths also point to more advanced learning paths that show how to automate the deployment of Arm instances at different cloud providers.
    

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Runbook


further_reading:
    - resource:
        title: Learn the architecture - Providing protection for complex software
        link: https://developer.arm.com/documentation/102433
        type: documentation
    - resource:
        title: Code reuse attacks - the compiler story
        link: https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/code-reuse-attacks-the-compiler-story
        type: blog
    - resource:
        title: Arm A-profile Instruction Set Architecture
        link: https://developer.arm.com/documentation/ddi0602
        type: documentation
    - resource:
        title: pwntools Documentation
        link: https://docs.pwntools.com/en/stable/
        type: documentation
    - resource:
        title: -mbranch-protection (armclang)
        link: https://developer.arm.com/documentation/101754/0620/armclang-Reference/armclang-Command-line-Options/-mbranch-protection
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
