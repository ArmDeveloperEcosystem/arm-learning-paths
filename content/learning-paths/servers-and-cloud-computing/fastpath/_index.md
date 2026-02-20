---
title: Benchmark Linux kernel performance on Arm servers with Fastpath

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to benchmark and compare different Linux kernel versions on Arm servers.

learning_objectives:
    - Build custom Linux kernels for Arm systems using tuxmake and Fastpath
    - Configure and provision Arm-based EC2 instances for kernel testing
    - Create and execute test plans that compare kernel performance across versions
    - Analyze benchmark results to identify performance differences between kernels

prerequisites:
    - An AWS account with permissions to create EC2 instances
    - Familiarity with basic Linux administration and SSH

author: Geremy Cohen

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
    - Fastpath
    - tuxmake
    - Linux

further_reading:
    - resource:
        title: Fastpath documentation
        link: https://fastpath.docs.arm.com/en/latest/index.html
        type: documentation
    - resource:
        title: Kernel install guide
        link: /learning-paths/servers-and-cloud-computing/kernel-build/
        type: guide
    - resource:
        title: AWS Compute Service Provider learning path
        link: /learning-paths/servers-and-cloud-computing/csp/
        type: guide

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
