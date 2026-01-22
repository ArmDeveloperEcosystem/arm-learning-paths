---
title: Fastpath Kernel Build and Install Guide

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
skilllevels: Intermediate
subjects: Operating Systems
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Fastpath
    - tuxmake
    - Linux kernel

further_reading:
    - resource:
        title: Fastpath documentation
        link: https://fastpath.docs.arm.com/en/latest/index.html
        type: documentation
    - resource:
        title: Kernel install guide
        link: /install-guides/kernel-build/
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

*fastpath* accelerates the cycle of building, deploying, and benchmarking Linux kernels on Arm-based infrastructure.

Off-the-shelf distributions ship with general-purpose kernels, but when you want to maximize performance you often need to rebuild the kernel with custom configuration options, experimental patches, or prerelease code. Custom kernels let you validate questions like “does an RC fix my workload regression?” or “do these extra debug settings impose measurable overhead?” without waiting for distro updates.

This learning path focuses on a concrete use case: run the Speedometer browser benchmark on two different kernel versions and determine which kernel delivers the best score. The workflow mirrors what kernel engineers do every day—build, deploy, and compare—while *fastpath* keeps the process reproducible.

To make that manageable we split the work across three Arm-based nodes:

1. **Build host** – compiles the kernels with *fastpath*-specific options.
2. **fastpath host** – orchestrates deployments, plan execution, and result collection.
3. **System Under Test (SUT)** – runs each kernel and executes the benchmark workloads.

Arm’s `arm_kernel_install_guide` repository supplies wrapper scripts that streamline each step. You will use them to compile kernels on the build host, prepare the *fastpath* host and SUT, generate a plan, execute it, and then read the results without having to stitch together the workflow manually.

> **Tip:** The complete *fastpath* reference documentation is available at [fastpath.docs.arm.com](https://fastpath.docs.arm.com/en/latest/index.html).  
