---
title: Explore secure device attach in Arm CCA Realms
description: Learn how Arm CCA Realms interact with I/O devices using VirtIO paravirtualization, SWIOTLB bounce buffers, and PCIe-TDISP secure device attach mechanisms with attestation.

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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: e21f51feb101ad90245ecceab95fe13e5eb61958faf24dff818eddd11f484b9a
  summary: >-
    Learn how Arm CCA Realms interact with I/O devices using VirtIO paravirtualization, SWIOTLB
    bounce buffers, and PCIe-TDISP secure device attach mechanisms with attestation. It is designed
    for developers who want to understand how Arm CCA Realms interact with I/O devices using VirtIO,
    bounce buffers, and secure device attach mechanisms. By the end, you will be able to define
    device attach and distinguish VirtIO paravirtualized attach from secure physical device attach,
    summarize what a Realm is and how RME isolates Realm memory, and describe how VirtIO enables
    paravirtualized I/O without full device emulation. It focuses on tools and technologies such
    as CCA, RME, and Docker, Linux and macOS environments, and Arm platforms including Neoverse
    and Cortex-A. The main steps cover About CCA Realms, VirtIO for device attach, Bounce buffers
    in Realms, and Exercise: observe bounce buffers in a Realm.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will define device attach and distinguish VirtIO paravirtualized attach from secure
      physical device attach, summarize what a Realm is and how RME isolates Realm memory, and
      describe how VirtIO enables paravirtualized I/O without full device emulation. Learn how
      Arm CCA Realms interact with I/O devices using VirtIO paravirtualization, SWIOTLB bounce
      buffers, and PCIe-TDISP secure device attach mechanisms with attestation.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers who want to understand how Arm CCA Realms interact
      with I/O devices using VirtIO, bounce buffers, and secure device attach mechanisms.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An AArch64 or x86_64 computer running
      Linux or macOS. You can also use a cloud instance from one of these [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).;
      Completion of [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison)
      Learning Path; Completion of the [Run an application in a Realm using the Arm Confidential
      Computing Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/)
      Learning Path; Completion of the [Run an end-to-end Attestation Flow](/learning-paths/servers-and-cloud-computing/cca-essentials/)
      Learning Path.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including CCA, RME, and Docker, Linux and macOS environments,
      and Arm platforms such as Neoverse and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around About CCA Realms, VirtIO for device attach, Bounce
      buffers in Realms, and Exercise: observe bounce buffers in a Realm.
# END generated_summary_faq

author: Arnaud de Grandmaison

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

