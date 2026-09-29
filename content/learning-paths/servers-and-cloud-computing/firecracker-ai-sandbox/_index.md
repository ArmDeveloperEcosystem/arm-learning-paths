---
title: Build an ephemeral AI code sandbox with Firecracker on Arm

draft: true
cascade:
    draft: true
    
description: Create a Firecracker-based runner on an Arm AGI CPU system that executes generated shell code in a disposable microVM with bounded resources and restricted networking.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for developers who want to isolate AI-generated code in disposable microVMs on an Arm Linux server.

learning_objectives:
    - Prepare an Arm Linux KVM host and an `aarch64` Firecracker guest image
    - Run generated shell code in a dedicated disposable microVM
    - Apply CPU, memory, timeout, filesystem, and network boundaries to each execution
    - Verify native Arm execution and confirm that guest filesystem changes do not persist

prerequisites:
    - An Arm AGI CPU platform or another Arm-based bare-metal server, such as an AWS Graviton4-based bare-metal instance, running Ubuntu 24.04 with KVM available as `/dev/kvm`
    - Root or `sudo` access on the server
    - Familiarity with Bash, SSH, and Linux networking
    - Outbound internet access to download Firecracker and guest artifacts

author: Pareena Verma

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
platforms:
  - Arm AGI CPU
  - AWS Graviton
tools_software_languages:
    - Firecracker
    - KVM
    - Bash
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Arm AGI CPU
        link: https://www.arm.com/products/cloud-datacenter/arm-agi-cpu
        type: website
    - resource:
        title: Firecracker getting started guide
        link: https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md
        type: documentation
    - resource:
        title: Firecracker production host setup recommendations
        link: https://github.com/firecracker-microvm/firecracker/blob/main/docs/prod-host-setup.md
        type: documentation
    - resource:
        title: Firecracker design
        link: https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md
        type: documentation
    - resource:
        title: Linux Kernel-based Virtual Machine
        link: https://linux-kvm.org/page/Main_Page
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
