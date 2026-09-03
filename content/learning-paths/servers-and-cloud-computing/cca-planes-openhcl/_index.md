---
title: Run an auxiliary plane in an Arm CCA Realm
description: Learn how to build a planes-enabled Arm CCA software stack, boot plane 0 Linux in a Realm, and run a test microkernel in an auxiliary plane on an Arm FVP.

minutes_to_complete: 180

who_is_this_for: This advanced topic is for firmware, kernel, and virtualization developers who want to experiment with Arm CCA planes in an emulated environment.

learning_objectives:
    - Build a planes-enabled Arm CCA software stack with Shrinkwrap.
    - Boot plane 0 Linux in a Realm on an Arm Fixed Virtual Platform (FVP).
    - Run a test microkernel in an auxiliary plane from plane 0.
    - Validate that the plane entry test reaches the expected result.

prerequisites:
    - An AArch64 or x86_64 computer running Ubuntu 24.04 LTS with at least 30 GB of free disk space.
    - A user account with `sudo` access to install host packages, or a host where the listed packages are already installed.
    - Completion of the [Run an application in a Realm using the Arm Confidential Compute Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/) Learning Path.
    - Familiarity with Linux kernel builds, Rust builds, Docker, and the Linux command line.

author: Arm

draft: true
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - CCA
    - RME
    - FVP
    - Docker
    - Shrinkwrap
    - Linux
    - Rust
    - OpenHCL
    - OpenVMM
    - kvmtool

further_reading:
    - resource:
        title: Arm Confidential Compute Architecture
        link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
        type: website
    - resource:
        title: Learn the architecture - Realm Management Extension
        link: https://developer.arm.com/documentation/den0126
        type: documentation
    - resource:
        title: Realm Management Monitor specification
        link: https://developer.arm.com/documentation/den0137/latest/
        type: documentation
    - resource:
        title: Shrinkwrap documentation
        link: https://shrinkwrap.docs.arm.com/en/latest/index.html
        type: documentation
    - resource:
        title: OpenVMM and OpenHCL project
        link: https://github.com/microsoft/openvmm
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
