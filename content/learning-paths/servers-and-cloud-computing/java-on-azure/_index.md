---
title: Deploy Java applications on Azure Cobalt 100 processors 

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic about Java deployment and benchmarking on Microsoft Azure Cobalt 100 Arm-based virtual machines. It is designed for developers migrating Java applications from x86_64 to Arm architecture.

learning_objectives: 
    - Provision an Azure Arm-based Cobalt 100 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image
    - Deploy Java on the Azure Arm64 virtual machine
    - Perform Java baseline testing and benchmarking on the Arm64 virtual machines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)


author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Java
    - JMH

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
