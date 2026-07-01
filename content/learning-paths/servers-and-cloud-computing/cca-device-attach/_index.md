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
    - Completion of [Get Started with CCA Attestation and Veraison](/learning-paths/servers-and-cloud-computing/cca-veraison/) Learning Path
    - Completion of the [Run an application in a Realm using the Arm Confidential Computing Architecture (CCA)](/learning-paths/servers-and-cloud-computing/cca-container/) Learning Path
    - Completion of the [Run an end-to-end Attestation Flow](/learning-paths/servers-and-cloud-computing/cca-essentials/) Learning Path

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:41:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2fca6f2863b4909021d529f868fde7c6abe5393a0d7c229477645b261436e705
  summary_generated_at: '2026-06-30T21:41:31Z'
  summary_source_hash: 2fca6f2863b4909021d529f868fde7c6abe5393a0d7c229477645b261436e705
  faq_generated_at: '2026-06-30T21:41:31Z'
  faq_source_hash: 2fca6f2863b4909021d529f868fde7c6abe5393a0d7c229477645b261436e705
  summary: >-
    You'll examine how Arm CCA Realms attach to I/O devices through two models: paravirtualized
    VirtIO and secure physical device attach. First, you'll learn about Realm isolation with RME,
    how VirtIO enables mediated device access, and why SWIOTLB bounce buffers are used
    when devices can't DMA directly to Realm memory. You'll also explore how PCIe‑TDISP and PCIe‑IDE
    provide secure device attach with attestation. Then, you'll run a pre-built Key Broker
    demo inside a Realm and use kernel tracing to observe SWIOTLB activity during VirtIO network
    I/O. By the end, you can recognize when data paths rely on bounce buffers and how this relates
    to the chosen device attach method.
  faqs:
  - question: How do I know that bounce buffers are being used in the Realm?
    answer: >-
      Use kernel tracing during the exercise to observe activity indicating SWIOTLB usage while
      the Key Broker demo generates network I/O through VirtIO. Seeing trace output associated
      with SWIOTLB during traffic confirms that data is bouncing through DMA-capable buffers.
  - question: What should I expect after starting the Key Broker container image?
    answer: >-
      The container runs a pre-built Key Broker demo used in the exercise. After it starts, list
      network interfaces to confirm connectivity before proceeding to kernel tracing.
  - question: When is VirtIO the right choice versus secure physical device attach?
    answer: >-
      VirtIO is the first level of device attach, mediated by the hypervisor with paravirtualized
      drivers, and is sufficient for many Realm I/O needs. Secure physical device attach using
      PCIe‑TDISP and PCIe‑IDE applies when hardware-backed isolation and attestation for the device
      are required.
  - question: Why do Realms rely on SWIOTLB bounce buffers for I/O?
    answer: >-
      Bounce buffers are used when a device cannot DMA to the original buffer, including when
      memory is not accessible to the device or does not meet alignment or contiguity constraints.
      In Realms, SWIOTLB enables data transfer between Realm-protected memory and devices during
      VirtIO I/O.
  - question: Will I learn to perform attestation of a physically attached device?
    answer: >-
      You'll learn how PCIe‑TDISP and PCIe‑IDE support secure physical device attach and
      attestation. The hands-on exercise focuses on VirtIO and observing SWIOTLB behavior, not
      on performing a physical device attestation workflow.
# END generated_summary_faq

author: Arnaud de Grandmaison

generate_summary_faq: false
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

