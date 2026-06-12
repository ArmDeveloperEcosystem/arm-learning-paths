---
title: Deploy a machine learning model to an NPU-capable system with Topo

draft: true
cascade:
    draft: true

description: Use Topo to deploy a web application on Cortex-A that triggers a MobileNetV2 image classifier running as Cortex-M firmware with Ethos-U65 NPU acceleration.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for embedded, edge, and cloud software developers who want to deploy machine learning workloads to heterogeneous Arm-based Linux targets using Topo.

learning_objectives:
    - Explain how Topo deploys an application that spans Cortex-A, Cortex-M, and Ethos-U
    - Prepare an NXP FRDM i.MX 93 board for remoteproc-runtime and shared-memory inference
    - Clone and deploy the topo-imx93-npu-deployment template
    - Describe how the Template is bootstrapped from Compose services, Remoteproc Runtime metadata, and Topo arguments
    - Run image classification from a browser and verify that inference is executed by the Cortex-M33 firmware

prerequisites:
    - A host machine (x86 or Arm) with Linux, macOS, or Windows
    - An NXP FRDM i.MX 93 target board accessible over SSH with root access
    - Docker installed on the host and target. For installation steps, see [Install Docker](/install-guides/docker/).
    - lscpu installed on the target (pre-installed on most Linux distributions)
    - Topo installed on the host. For installation steps, see [Deploy containerized workloads to Arm-based Linux targets with Topo](/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/).
    - Basic familiarity with containers, SSH, and CLI tools

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
