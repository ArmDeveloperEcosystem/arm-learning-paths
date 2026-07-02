---
title: Run a Minecraft server on OCI A1 Arm64 instances

description: Provision an Arm64 instance on Oracle Cloud Infrastructure, install the Java runtime, and deploy a persistent Minecraft server for multiplayer gameplay.

# draft: true
# cascade:
#    draft: true

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers who are new to OCI and want to provision an Arm64 instance and run a persistent Minecraft server on it.

learning_objectives: 
    - Provision an OCI A1 Arm64 virtual machine instance suitable for running a Minecraft server
    - Deploy and configure Minecraft server software
    - Expose the Minecraft service from OCI by editing the network policy for the instance 
    - Connect to the running Minecraft server from the Minecraft client application

prerequisites:
    - Review [Get started with Oracle Cloud Infrastructure](/learning-paths/servers-and-cloud-computing/csp/oci/) 
    - Install software that allows you to connect to a running instance over SSH
    - You will need a copy of the [Minecraft Java edition 
      client](https://www.minecraft.net/en-us/download) installed, and 
      [a license](https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc)
      for the game.

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
        title: How To Setup And Run A Free Minecraft Server In The Cloud
        link: https://blogs.oracle.com/developers/how-to-setup-and-run-a-free-minecraft-server-in-the-cloud
        type: blog
    - resource:
        title: How to create a powerful Minecraft Server for free using Oracle Cloud
        link: https://www.youtube.com/watch?v=0kFjEUDJexI
        type: video
    - resource:
        title: Deploy Arm instances on Oracle Cloud Infrastructure (OCI) using Terraform
        link: /learning-paths/servers-and-cloud-computing/oci-terraform/
        type: learning-path


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
