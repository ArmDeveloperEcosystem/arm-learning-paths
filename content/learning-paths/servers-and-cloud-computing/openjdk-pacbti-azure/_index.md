---
title: Build an OpenJDK JVM with PAC/BTI on Azure Cobalt 100

description: Learn how to compile OpenJDK with branch protection on an Azure Cobalt 100 Arm VM and verify PAC/BTI support in the resulting JVM.

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30   

who_is_this_for: This Learning Path is for developers who want to build and validate an OpenJDK JVM with PAC/BTI support on Azure Cobalt 100 Arm-based virtual machines.

learning_objectives: 
    - Provision an Azure Cobalt 100 Arm-based virtual machine with Ubuntu Pro 24.04 LTS.
    - Build OpenJDK on Arm64 with branch protection support enabled.
    - Verify PAC/BTI readiness in the installed JVM runtime.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)


author: Doug Anson

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Java
    - OpenJDK
    - Bash

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: OpenJDK build documentation
      link: https://openjdk.org/groups/build/doc/building.html
      type: documentation
  - resource:
      title: OpenJDK source repository
      link: https://github.com/openjdk/jdk
      type: documentation
  - resource:
      title: Arm A64 instruction reference
      link: https://developer.arm.com/documentation/100076/latest/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
