---
title: Secure Realms during boot using Arm Confidential Compute Architecture (CCA) BootSync
description: Use Arm CCA BootSync to transfer boot-time configuration and secret data when you launch a Realm on an FVP with RME support.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to understand how Arm CCA BootSync supports early Realm boot workflows such as UEFI Secure Boot and encrypted disk boot.

learning_objectives:
  - Understand why BootSync is needed before the Realm guest operating system has networking.
  - Understand how the Boot Injection Protocol uses key exchange, attestation, and Boot Information Blocks to support the BootSync workflow.
  - Use BootSync to inject UEFI variables and secret data into an Arm CCA Realm.
  - Launch Arm CCA Realms with UEFI Secure Boot and an encrypted root file system on an Armv9-A AEM Base Fixed Virtual Platform (FVP) with Realm Management Extension (RME) support.

prerequisites:
  - A cloud-based instance or an AArch64 or x86_64 computer running Linux. For more information about using cloud-based instances, see the [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/) Learning Path.
  - Completion of the [Run an application in a Realm using the Arm Confidential Compute Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/) Learning Path

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
  - resource:
      title: Realm Host Interface Specification
      link: https://developer.arm.com/documentation/den0148/latest/
      type: documentation
  - resource:
      title: ArmCcaBootSync README
      link: https://gitlab.arm.com/linux-arm/edk2-cca/-/blob/cca/4441_measured_boot_v1/ArmVirtPkg/ArmCcaBootSync/Readme.md
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
