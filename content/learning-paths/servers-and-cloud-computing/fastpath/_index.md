---
title: Fastpath Kernel Build and Install Guide

draft: true
cascade:
    draft: true

minutes_to_complete: 45

who_is_this_for: Software developers and performance engineers who want to explore benchmarking across different kernel versions with Fastpath on Arm.

learning_objectives:
    - Understand how Fastpath streamlines kernel experimentation workflows
    - Provision an Arm-based build machine and compile Fastpath-enabled kernels on it
    - Provision an Arm-based test system, also known as the System Under Test (SUT)
    - Create a test plan consisting of kernel versions and benchmark suites 
    - Launch an Arm-based Fastpath host to orchestrate the kernel benchmarking process on the SUT

prerequisites:
    - An AWS account with permissions to create EC2 instances
    - Familiarity with basic Linux administration and SSH

author: Geremy Cohen

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
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
