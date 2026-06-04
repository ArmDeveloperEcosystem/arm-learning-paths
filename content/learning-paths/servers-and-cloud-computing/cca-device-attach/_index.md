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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:29:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e21f51feb101ad90245ecceab95fe13e5eb61958faf24dff818eddd11f484b9a
  summary_generated_at: '2026-06-02T03:17:31Z'
  summary_source_hash: e21f51feb101ad90245ecceab95fe13e5eb61958faf24dff818eddd11f484b9a
  faq_generated_at: '2026-06-03T00:29:35Z'
  faq_source_hash: e21f51feb101ad90245ecceab95fe13e5eb61958faf24dff818eddd11f484b9a
  summary: >-
    This advanced Learning Path explains how Arm CCA Realms interact with I/O devices, contrasting
    VirtIO paravirtualized attach with secure physical device attach. You will review what a Realm
    is, how the Realm Management Extension (RME) isolates Realm memory, and when SWIOTLB bounce
    buffers are used. A hands-on exercise uses Docker to run the CCA Key Broker demo inside a
    Realm and employs kernel tracing to confirm bounce buffer activity for VirtIO network I/O.
    The path also describes how PCIe‑TDISP and PCIe‑IDE support secure device attach and attestation.
    It targets developers on AArch64 or x86_64 systems running Linux or macOS, including Arm cloud
    instances, and assumes completion of three prerequisite CCA Learning Paths.
  faqs:
  - question: What do I need before running the exercise?
    answer: >-
      Use an AArch64 or x86_64 computer running Linux or macOS, or a cloud instance from the Arm
      cloud service providers page. Complete the CCA Attestation and Veraison, Run an application
      in a Realm using CCA, and Run an end-to-end Attestation Flow Learning Paths.
  - question: How is attestation covered when discussing secure physical device attach?
    answer: >-
      The Learning Path describes how PCIe‑TDISP and PCIe‑IDE support secure physical device attach
      with attestation. It builds on prior attestation knowledge from the prerequisite Learning
      Paths.
  - question: How do I start the Key Broker server (KBS) used in the exercise?
    answer: >-
      Pull and run the Docker image armswdev/cca-learning-path:cca-key-broker-v2. The steps provide
      the exact docker pull and docker run commands.
  - question: How do I confirm that SWIOTLB bounce buffers are being used inside the Realm?
    answer: >-
      Follow the exercise to enable kernel tracing in the Realm while generating VirtIO network
      I/O with the Key Broker demo. You should observe trace evidence indicating SWIOTLB activity
      for the transfers.
  - question: How can I check network interfaces during the exercise?
    answer: >-
      Use the ip -c a command as shown in the steps to list network interfaces and verify the
      environment during the demo.
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

