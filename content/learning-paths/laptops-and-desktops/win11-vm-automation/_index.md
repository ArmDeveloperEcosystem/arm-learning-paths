---
title: Automate Windows on Arm virtual machine deployment with QEMU and KVM on Arm Linux

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers and system administrators who want to automate Windows on Arm virtual machine (VM) creation on Arm Linux systems using QEMU and KVM.

learning_objectives:
    - Understand the process of creating a Windows on Arm virtual machine using Bash scripts
    - Run scripts for VM creation and management
    - Troubleshoot common VM setup and runtime issues
    - Use Windows on Arm virtual machines for software development and testing

prerequisites:
    - An Arm Linux system with KVM support and a minimum of 8GB RAM and 50GB free disk space

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - Windows
tools_software_languages:
    - QEMU
    - KVM
    - Bash
    - RDP

further_reading:
    - resource:
        title: Linaro Wiki - Windows on Arm
        link: https://wiki.linaro.org/LEG/Engineering/Kernel/WindowsOnArm
        type: documentation
    - resource:
        title: Botspot Virtual Machine (BVM) Project
        link: https://github.com/Botspot/bvm
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
