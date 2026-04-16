---
title: Enable Arm SPE for Performix memory access analysis

description: Learn how to verify and enable Arm Statistical Profiling Extension (SPE) on Arm Linux machines, including systems hosted through cloud service providers, so the Memory Access recipe in Arm Performix can run on supported environments.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers and performance engineers who want to prepare Arm Linux machines, including cloud-hosted systems, for Arm Performix memory access profiling.

learning_objectives:
    - Check whether Arm SPE is already available on an Arm Linux system using Sysreport and kernel-level checks.
    - Explain the hardware, platform, and kernel requirements that allow Linux to expose the `arm_spe_pmu` driver.
    - Apply Linux-side changes such as loading the SPE PMU module, installing matching kernel modules, or selecting a kernel with SPE support.
    - Identify when a cloud instance does not expose SPE to the guest OS and choose a suitable system for Arm Performix memory access analysis.

prerequisites:
    - Access to a Linux-based Arm system, such as an Arm cloud instance or bare-metal server, with `sudo` or root access.
    - Access to Arm Performix on your host machine and SSH access to the target system. See the [Arm Performix install guide](/install-guides/performix/) for setup instructions.
    - Familiarity with the Linux command line, SSH, and basic kernel module management.

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
    - AWS
    - Google Cloud
    - Microsoft Azure
armips:
    - Neoverse
tools_software_languages:
    - Arm Performix
    - Sysreport
    - Linux kernel
    - perf
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Arm Performix install guide
        link: https://learn.arm.com/install-guides/performix/
        type: documentation
    - resource:
        title: Arm Statistical Profiling Extension documentation
        link: https://developer.arm.com/documentation/100616/0301/debug-descriptions/statistical-profiling-extension
        type: documentation
    - resource:
        title: Arm Performix
        link: https://developer.arm.com/servers-and-cloud-computing/arm-performix
        type: website
    - resource:
        title: Get ready for performance analysis with Sysreport
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/
        type: documentation
    - resource:
        title: Analyze cache behavior with Perf C2C on Arm
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/false-sharing-arm-spe/
        type: learning-path



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
