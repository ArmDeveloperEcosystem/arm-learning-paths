---
title: Arm CCA Boot Sync
description: Learn how to use Arm CCA Boot Sync while launching Arm CCA Realms on an FVP with RME support.

draft: true
cascade:
    draft: true
    
minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to understand how to use Arm CCA Bootsync.

learning_objectives:
  - Gain an overview of Arm CCA Boot Sync and Boot Onjection Protocol.
  - Understand how Arm CCA Boot Sync can be used for defining UEFI variables, enabling Secure Boot and share secure data with Arm CCA Realms.
  - Lanch Arm CCA Realms with Secure Boot enabled and encrypted file system using an Armv9-A AEM Base Fixed Virtual Platform (FVP) with RME support.

prerequisites:
  - An AArch64 or x86_64 computer running Linux or macOS. Cloud-based instances can also be used; see the [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/)
  - Completion of the [Run an application in a Realm using the Arm Confidential Compute Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container) Learning Path

author:
  - Anton Antonov
  - Pareena Verma

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
  - Neoverse
  - Cortex-A
operatingsystems:
  - Linux
  - macOS
tools_software_languages:
  - FVP
  - RME
  - CCA
  - Docker
  - EDK2
  - Cryptsetup

further_reading:
  - resource:
      title: Arm Confidential Compute Architecture
      link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
      type: website
  - resource:
      title: Arm Confidential Compute Architecture Open-Source enablement
      link: https://www.youtube.com/watch?v=JXrNkYysuXw
      type: video
  - resource:
      title: Learn the architecture - Realm Management Extension
      link: https://developer.arm.com/documentation/den0126
      type: documentation
  - resource:
      title: Realm Management Monitor Specification
      link: https://developer.arm.com/documentation/den0137/latest/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

