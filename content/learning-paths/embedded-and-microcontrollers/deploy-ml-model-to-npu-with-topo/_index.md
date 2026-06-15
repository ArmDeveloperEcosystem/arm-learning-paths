---
title: Deploy an ML application to the Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo

description: Use Topo to deploy a Cortex-A web application that sends MobileNetV2 image classification requests to Cortex-M33 firmware accelerated by the Ethos-U65 NPU.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for embedded/edge software developers who want to deploy machine learning workloads to heterogeneous Arm-based Linux targets using Topo, including leveraging Arm Ethos-U NPUs.

learning_objectives:
    - Explain how Topo deploys an application that spans Cortex-A, Cortex-M, and Ethos-U
    - Deploy the topo-imx93-npu-deployment Template, which operates across Cortex-A, Cortex-M, and Ethos-U, to perform image classification using an ExecuTorch MobileNetV2 model
    - Describe how the Template is bootstrapped from Compose services, Remoteproc Runtime metadata, and Topo arguments
    - Understand how to take similar projects and create Topo Templates, including using Agent Skills

prerequisites:
    - A host machine (x86 or Arm) with Linux, macOS, or Windows
    - An NXP FRDM i.MX 93 target board with Linux setup, accessible over SSH with root access. To do this, see [Use Linux on the NXP FRDM i.MX 93 board](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/linux-nxp-board/).
    - Docker installed on the host and target. For installation steps, see [Install Docker](https://learn.arm.com/install-guides/docker/).
    - At least 25 GB of free disk space on the host if you are building without cache images.
    - The Device Tree Compiler (`dtc`) installed on the host.
    - lscpu installed on the target (pre-installed on most Linux distributions)
    - Topo installed on the host. For installation steps, see [Deploy containerized workloads to Arm-based Linux targets with Topo](https://learn.arm.com/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/).
    - Basic familiarity with containers, SSH, and CLI tools
    - (Optional) Access to an Agent, such as Codex, or Claude Code

author: Tomas Agustin Gonzalez Orlando

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Cortex-A
    - Cortex-M
    - Ethos-U
tools_software_languages:
    - Topo
    - Docker
    - SSH
    - ExecuTorch
    - remoteproc-runtime
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
    - resource:
        title: ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
