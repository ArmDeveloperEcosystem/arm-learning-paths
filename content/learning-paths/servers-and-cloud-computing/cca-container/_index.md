---
title: Run an application in a Realm using the Arm Confidential Compute Architecture (CCA)

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for software developers who want to learn how to run their applications in a Realm using the Arm Confidential Compute Architecture (CCA).

learning_objectives:
    - Run the Arm reference CCA software stack on an Armv-A AEM Base FVP (Fixed Virtual Platform) with support for RME extensions.
    - Create a virtual machine in a Realm running guest Linux using a pre-built docker container.
    - Run a simple application in a Realm running guest Linux.
    - Obtain a CCA attestation token from the virtual guest in a Realm.
    - Run the CCA software stack using MEC (Memory Encryption Contexts)

prerequisites:
    - An AArch64 or x86_64 computer running Linux or macOS. You can use cloud instances, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

author:
    - Pareena Verma
    - Arnaud de Grandmaison

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - GCC
    - FVP
    - RME
    - CCA
    - Docker
    - Runbook


further_reading:
    - resource:
        title: Learn the architecture - Introducing Arm Confidential Compute Architecture
        link: https://developer.arm.com/documentation/den0125
        type: documentation
    - resource:
        title: Arm Confidential Compute Architecture
        link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
        type: website
    - resource:
        title: Arm Confidential Compute Architecture open source enablement
        link: https://www.youtube.com/watch?v=JXrNkYysuXw
        type: video
    - resource:
        title: Learn the architecture - Realm Management Extension
        link: https://developer.arm.com/documentation/den0126
        type: documentation
    - resource:
        title: Realm Management Monitor specification
        link: https://developer.arm.com/documentation/den0137/latest/
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
