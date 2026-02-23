---
title: Explore secure device attach in Arm CCA Realms

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for developers who want to understand how Arm CCA Realms interact with I/O devices using VirtIO, bounce buffers, and secure device attach mechanisms.

learning_objectives:
    - Define device attach and distinguish VirtIO paravirtualized attach from secure physical device attach
    - Summarize what a Realm is and how RME isolates Realm memory
    - Describe how VirtIO enables paravirtualized I/O without full device emulation
    - Explain when and why SWIOTLB bounce buffers are used in Realms
    - Describe how PCIe‑TDISP and PCIe‑IDE support secure physical device attach and attestation

prerequisites:
    - An AArch64 or x86_64 computer running Linux or macOS. You can also use a cloud instance from one of these [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).
    - Completion of [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison) Learning Path
    - Completion of the [Run an application in a Realm using the Arm Confidential Computing Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/) Learning Path
    - Completion of the [Run an end-to-end Attestation Flow](/learning-paths/servers-and-cloud-computing/cca-essentials/) Learning Path

author: Arnaud de Grandmaison

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
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - CCA
    - RME
    - Docker

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
