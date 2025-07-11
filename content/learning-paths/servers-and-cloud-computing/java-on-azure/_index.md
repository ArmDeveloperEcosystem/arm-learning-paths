---
title: Run Java applications on the Microsoft Azure Cobalt 100 processors 

minutes_to_complete: 60   

who_is_this_for: This is an introductory topic for the software developers who are willing to migrate their Java-based applications from x86_64 platforms to Arm-based platforms, or on Microsoft Azure - Cobalt 100 CPU-based VMs specifically.  Most Java applications will run on Cobalt 100 with no changes needed. 

learning_objectives: 
    - Provision an Azure Arm64 VM using Azure console, with Ubuntu as the base image.
    - Learn how to create Azure Linux 3.0 Docker container.
    - Deploy a Java application inside an Azure Linux 3.0 Arm64-based Docker container, as well as Azure Linux 3.0 custom-image based Azure VM. 
    - Perform Java benchmarking inside the container as well as the custom VM.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6). 
    - A machine with [Docker](/install-guides/docker/) installed.

author: Zach Lasiuk

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse-N2

tools_software_languages:
    - Java
    - Docker

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Azure Container Instances documentation
      link: https://learn.microsoft.com/en-us/azure/container-instances/
      type: documentation
  - resource:
      title: Docker overview
      link: https://docs.docker.com/get-started/overview/
      type: documentation
  - resource:
      title: Java on Azure
      link: https://learn.microsoft.com/en-us/java/azure/
      type: documentation
  - resource:
      title: JMH (Java Microbenchmark Harness) documentation
      link: https://openjdk.org/projects/code-tools/jmh/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

