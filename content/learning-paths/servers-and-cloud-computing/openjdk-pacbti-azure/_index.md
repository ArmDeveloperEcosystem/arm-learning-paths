---
title: Build OpenJDK with PAC/BTI support on Azure Cobalt 100

description: Learn how to compile OpenJDK with branch protection on an Azure Cobalt 100 Arm VM and verify PAC/BTI support in the resulting JVM.

draft: true
cascade:
    draft: true
    
minutes_to_complete: 60

who_is_this_for: This is an introductory topic for Java developers who want to compile OpenJDK from source with PAC/BTI branch protection enabled and verify the resulting JVM on an Azure Cobalt 100 Arm-based virtual machine.

learning_objectives: 
    - Provision an Azure Cobalt 100 Arm-based virtual machine with Ubuntu Pro 24.04 LTS.
    - Build OpenJDK on Arm with branch protection support enabled.
    - Verify PAC/BTI readiness in the installed JVM runtime.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Familiarity with the Linux command line and SSH
    - Basic familiarity with Java and the JDK toolchain


author: Doug Anson

### Tags
skilllevels: Introductory
subjects: Security
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
      title: Learn the architecture - Providing protection for complex software
      link: https://developer.arm.com/documentation/102433/latest/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
