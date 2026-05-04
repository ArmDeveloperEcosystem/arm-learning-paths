---
title: Benchmark QuantLib on Azure Cobalt
description: Learn how to build QuantLib on an Arm-based Azure Cobalt virtual machine and run benchmark workloads to evaluate performance on Arm64 cloud infrastructure.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers who want to build and benchmark QuantLib on Arm-based cloud instances.

learning_objectives:
  - Explain why QuantLib is a useful benchmark for Arm-based cloud systems
  - Create and connect to an Arm64 Azure Cobalt virtual machine running Ubuntu
  - Build QuantLib from source with benchmark support enabled
  - Run QuantLib benchmark workloads with different sizes and thread counts
  - Record and compare benchmark results in a repeatable way

prerequisites:
    - An Azure account with permission to create virtual machines
    - Basic familiarity with the Linux command line and SSH
    - Basic experience building C++ software from source
author: Chris Moroney

### Tags
skilllevels: Intermediate
subjects: Servers and Cloud Computing
armips:
    - Neoverse
tools_software_languages:
    - Azure
    - Ubuntu
    - QuantLib
    - GCC
    - CMake
    - Bash
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: QuantLib GitHub repository
        link: https://github.com/lballabio/QuantLib
        type: website
    - resource:
        title: Azure Virtual Machines documentation
        link: https://learn.microsoft.com/azure/virtual-machines/
        type: documentation
    - resource:
        title: Learn about Arm Neoverse processors
        link: /learning-paths/servers-and-cloud-computing/intro/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---