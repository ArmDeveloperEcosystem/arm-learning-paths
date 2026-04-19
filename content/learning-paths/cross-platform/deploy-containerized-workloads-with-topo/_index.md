---
title: Deploy containerized workloads to Arm-based Linux targets with Topo

description: Learn how to use Topo to detect device capabilities, select a compatible template, and deploy containerized workloads to Arm-based Linux targets over SSH.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for embedded, edge, and cloud software developers who want to easily deploy containerized workloads to Arm-based Linux targets with Topo.

learning_objectives: 
    - Understand what Topo is, and why you would use it to deploy containerixed workloads to Arm Linux targets
    - Use Topo to perform a health-check on the target, generate a target description to capture Arm processor capabilities
    - Clone a compatible Topo template for your hardware and deploy the workload
    - (Optional) Deploy containerized workloads across heterogeneous devices (Cortex-A + Cortex-M) with Topo and remoteproc-runtime
    - (Optional) Use Command-Line-Interface (CLI) Agents with Topo

prerequisites:
    - A host machine (x86 or Arm) with Linux, macOS, or Windows
    - An Arm-based Linux target you can access over SSH, for example AWS Graviton, Raspberry Pi, DGX Spark, i.MX 93
    - Docker installed on host and target. If needed, use [Install Docker](/install-guides/docker/)
    - lscpu installed on target (typically pre-installed with Linux)
    - SSH key-based authentication configured between host and target - if using password-based authentication, Topo can help you setup key-based authentication
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
    - remoteproc-runtime
    - remoteproc
    - CLI
operatingsystems:
    - Linux
    - macOS
    - Windows

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
