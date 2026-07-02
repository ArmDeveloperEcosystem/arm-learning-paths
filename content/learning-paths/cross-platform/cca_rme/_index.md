---
title: Get started with Realm Management Extension (RME)

description: Learn how to use Arm Development Studio to explore Realm Management Extension (RME) and Arm Confidential Compute Architecture (CCA) through a bare-metal example running on the Arm Architecture Envelope Model.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers interested in learning the concepts of Realm Management Extension and the Arm Confidential Compute Architecture (CCA).

learning_objectives: 
    - Understand the Arm Confidential Compute Architecture (CCA)
    - Understand a simple bare-metal example provided with Arm Development Studio

prerequisites:
    - Some understanding of the Arm architecture
    - Arm Development Studio, 2023.0 or later

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T17:16:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  summary_generated_at: '2026-07-02T17:16:42Z'
  summary_source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  faq_generated_at: '2026-07-02T17:16:42Z'
  faq_source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  summary: >-
    This Learning Path introduces Arm Confidential Compute Architecture (CCA) and shows how to
    explore Realm Management Extension (RME) using a bare‑metal example included with Arm Development
    Studio. You import the example into the IDE and run it on the Arm Architecture Envelope Model
    (AEM) Fixed Virtual Platform supplied with Development Studio. With Arm Debugger features,
    you step through execution that demonstrates the Realm world alongside Normal, Secure, and
    Root worlds, and see how a secure monitor in Root world manages transitions. The path focuses
    on building an intuition for CCA’s separation of resource management from access by examining
    concrete code paths and runtime behavior on the model.
  faqs:
  - question: Which example should I import in Arm Development Studio to explore RME?
    answer: >-
      Import the bare‑metal example that illustrates the Realm Management Extension included with
      Arm Development Studio (2023.0 or later). In the IDE, go to File > Import > Arm Development
      Studio > Examples & Programming Libraries and select the RME bare‑metal example.
  - question: What target model should I use to run the example?
    answer: >-
      Use the Arm Architecture Envelope Model (AEM) Fixed Virtual Platform supplied with Arm Development
      Studio. Select the supplied AEM FVP configuration when launching the example.
  - question: What should I check if the example does not appear or fails to import?
    answer: >-
      Verify that you are using Arm Development Studio 2023.0 or later. If the list is empty,
      check that the installation is complete and includes the example content and the AEM FVP
      supplied with Development Studio.
  - question: What behavior should I look for when stepping through the example with the debugger?
    answer: >-
      Expect to step through code paths that exercise the RME architectural feature and transitions
      between security states. The goal is to correlate CCA concepts with the points where execution
      enters and exits those states.
  - question: How does CCA organize security states that this example demonstrates?
    answer: >-
      CCA extends TrustZone by adding a Realm world and an underlying Root world to the existing
      Normal and Secure worlds. A secure monitor runs in Root world and manages transitions between
      these security states.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
    - Armv9-A

operatingsystems:
    - Linux
    - Android

tools_software_languages:
    - Trusted Firmware
    - Arm Development Studio
    - RME
    - CCA
    - Runbook

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

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

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

