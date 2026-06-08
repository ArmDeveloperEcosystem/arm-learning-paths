---
title: Deploy containerized workloads to Arm-based Linux targets with Topo

description: Use Topo to detect Arm processor capabilities on a target device, select a compatible container template, and deploy containerized workloads to Arm-based Linux targets over SSH.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for embedded, edge, and cloud software developers who want to deploy containerized workloads to Arm-based Linux targets using Topo.

learning_objectives:
    - Install Topo and verify that the host and target environments are ready for deployment
    - Run health checks and generate a target description to identify compatible Arm processor features and templates
    - Clone a Topo template and deploy a containerized workload to an Arm-based Linux target
    - (Optional) Deploy firmware and applications to heterogeneous Cortex-A + Cortex-M devices using remoteproc-runtime

prerequisites:
    - A host machine (x86 or Arm) with Linux, macOS, or Windows
    - An Arm-based Linux target accessible over SSH, for example an Arm-based Linux VM, Raspberry Pi, DGX Spark, or NXP i.MX 93
    - Docker installed on the host and target. For installation steps, see [Install Docker](/install-guides/docker/).
    - lscpu installed on the target (pre-installed on most Linux distributions)
    - Basic familiarity with containers and CLI tools

author: Matt Cossins

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
    - Cortex-A
    - Cortex-M
tools_software_languages:
    - Topo
    - Docker
    - SSH
operatingsystems:
    - Linux
    - macOS
    - Windows

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Topo repository
        link: https://github.com/arm/topo
        type: documentation
    - resource:
        title: Topo template format
        link: https://github.com/arm/topo-template-format
        type: documentation
    - resource:
        title: Topo releases
        link: https://github.com/arm/topo/releases/latest
        type: website
    - resource:
        title: remoteproc-runtime
        link: https://github.com/arm/remoteproc-runtime
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
