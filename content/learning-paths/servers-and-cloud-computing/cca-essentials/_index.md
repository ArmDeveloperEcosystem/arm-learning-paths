---
title: Run an end-to-end Attestation Flow with Arm CCA

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for software developers who want to learn how to run an end-to-end attestation flow with Arm's Confidential Computing Architecture (CCA).  

learning_objectives:
     - Describe how you can use attestation with Arm's Confidential Computing Architecture (CCA).
     - Deploy a simple workload in a CCA realm on an Armv9-A AEM Base Fixed Virtual Platform (FVP) that has support for RME extensions. 
     - Connect the workload with additional software services to create an end-to-end example that uses attestation to unlock the confidential processing of data.

prerequisites:
    - An AArch64 or x86_64 computer running Linux. You can use cloud instances, see this list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).
    - Completion of [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison) Learning Path.
    - Completion of the [Run an application in a Realm using the Arm Confidential Computing Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/) Learning Path.

author: 
    - Arnaud de Grandmaison
    - Paul Howard
    - Pareena Verma

### Tags
skilllevels: Advanced
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
    - Veraison
    - Runbook

    
further_reading:
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
