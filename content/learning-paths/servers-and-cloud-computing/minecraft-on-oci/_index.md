---
title: Run a Minecraft server on an Arm-based Oracle Cloud Infrastructure instance

description: Deploy a Minecraft Java Edition server on an Arm-based OCI A1 instance, open port 25565, and connect from the Minecraft client.

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers who are new to OCI and want to provision an arm64 instance and run a persistent Minecraft server on it.

learning_objectives: 
    - Provision an OCI A1 arm64 virtual machine instance suitable for running a Minecraft server
    - Deploy and configure Minecraft server software
    - Expose the Minecraft service from OCI by editing the network policy for the instance and the virtual machine instance firewall 
    - Connect to the running Minecraft server from the Minecraft client application

prerequisites:
    - An Oracle Cloud Infrastructure (OCI) account
    - A copy of the [Minecraft Java Edition client](https://www.minecraft.net/en-us/download) installed, and [a license for the game](https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc)
    - A Microsoft account for starting a Minecraft client application

author: Dave Neary

### Tags
skilllevels: Introductory
subjects: Web
armips:
    - Neoverse
tools_software_languages:
    - Java
    - Minecraft
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: How to create a powerful Minecraft Server for free using Oracle Cloud
        link: https://www.youtube.com/watch?v=0kFjEUDJexI
        type: video
    - resource:
        title: Deploy Arm instances on Oracle Cloud Infrastructure (OCI) using Terraform
        link: /learning-paths/servers-and-cloud-computing/oci-terraform/
        type: learning-path
    - resource:
        title: Getting started with Oracle Cloud Infrastructure 
        link: /learning-paths/servers-and-cloud-computing/csp/oci/
        type: learning-path 


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
