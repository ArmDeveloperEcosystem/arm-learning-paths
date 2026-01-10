---
title: Run Confidential Containers with encrypted images using Arm CCA and Trustee

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to understand how Confidential Containers run in Arm CCA Realms.

learning_objectives:
  - Gain an overview of Confidential Containers and their role in confidential computing
  - Understand how Trustee services are used with Arm CCA attestation to authorize and unlock confidential workloads
  - Deploy a Confidential Container from an encrypted image inside an Arm CCA Realm using an Armv9-A AEM Base Fixed Virtual Platform (FVP) with RME support

prerequisites:
  - An AArch64 or x86_64 computer running Linux or macOS. Cloud-based instances can also be used; see the [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/)
  - Completion of the ["Run an end-to-end Attestation with Arm CCA and Trustee"](/learning-paths/servers-and-cloud-computing/cca-trustee) Learning Path

author:
  - Anton Antonov

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
  - Veraison
  - Trustee
  - Confidential Containers
  - Kata Containers

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
