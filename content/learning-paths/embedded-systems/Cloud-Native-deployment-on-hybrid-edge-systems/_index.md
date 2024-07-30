---
title: Deploy firmware on hybrid edge systems using containers

minutes_to_complete: 20

who_is_this_for: This learning path is dedicated to developers interested in learning how to deploy software (embedded applications and firmware) onto other processors in the system via Linux running on the application core.

learning_objectives: 
    - Deploy a containerized embedded application onto an M-core from an A-core using Containerd and k3s.	
    - Build a firmware container image.
    - Build the Hybrid runtime components.
    

prerequisites:
    - Access to Arm Virtual Hardware to use the i.MX 8M Plus model. AVH provides a free 30-day trial if you do not have a subscription. https://app.avh.arm.com/login
    - If you want to build your own runtime and container image, you will need a Linux host machine with Docker, buildx and Git.

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
