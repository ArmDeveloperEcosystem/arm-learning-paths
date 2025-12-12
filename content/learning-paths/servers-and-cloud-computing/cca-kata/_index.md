---
title: Run Confidentail Containers with encrypted images using Arm CCA and Trustee

minutes_to_complete: 60

who_is_this_for: This Learning Path is for software developers who want to understand how Confidential Containers can be run in Arm CCA realm.

learning_objectives:
  - Overview of Confidential Containers
  - Understand how Trustee services are used for CCA realm attestation to unlock the confidential processing of data.
  - Use an encrypted image to deploy a Confidential Containers in a CCA realm on an Armv9-A AEM Base Fixed Virtual Platform (FVP) that has support for RME extensions.

prerequisites:
  - An AArch64 or x86_64 computer running Linux or macOS; you can use cloud instances - see the [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/)
  - Completion of the ["Run an end-to-end Attestation with Arm CCA and Trustee"](https://learn.arm.com/learning-paths/servers-and-cloud-computing/cca-trustee) Learning Path

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
  - Confidential containers
  - Kata containers

further_reading:
  - resource:
      title: Arm Confidential Compute Architecture
      link: https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture
      type: website
  - resource:
      title: Arm Confidential Compute Architecture open-source enablement
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
