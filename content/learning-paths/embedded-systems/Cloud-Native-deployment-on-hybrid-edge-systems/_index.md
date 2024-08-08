---
title: Deploy firmware on hybrid edge systems using containers

minutes_to_complete: 20

who_is_this_for: This learning path is for developers interested in learning how to deploy software (embedded applications and firmware) onto other processors in the system, using Linux running on the application core.

learning_objectives:
    - Deploy a containerized embedded application onto an Arm Cortex-M core from an Arm Cortex-A core using containerd and K3s.
    - Build a firmware container image.
    - Build the hybrid-runtime components.


prerequisites:
    - A valid account with [Arm Virtual Hardware](https://app.avh.arm.com/login)
    - An Arm Linux host machine (if you want to build your own runtime and container image)

author_primary: Basma El Gaabouri

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Cortex-M
    - Cortex-A
tools_software_languages:
    - Docker
    - AVH
    - K3s
    - Containerd
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
