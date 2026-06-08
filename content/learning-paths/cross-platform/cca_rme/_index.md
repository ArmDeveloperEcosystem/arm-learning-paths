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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:33:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  summary_generated_at: '2026-06-01T21:02:16Z'
  summary_source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  faq_generated_at: '2026-06-02T21:33:15Z'
  faq_source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  summary: >-
    This introductory Learning Path shows how to explore Arm Confidential Compute Architecture
    (CCA) and the Realm Management Extension (RME) using Arm Development Studio. You will import
    a simple bare-metal example provided with Development Studio (2023.0 or later), run it on
    the Arm Architecture Envelope Model (AEM) Fixed Virtual Platform included with the tools,
    and use Arm Debugger features to examine behavior relevant to CCA. The material explains the
    CCA security states—Normal, Secure, Realm, and Root—and the role of a secure monitor in managing
    transitions. Prerequisites are a basic understanding of Arm architecture and access to Arm
    Development Studio. Estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the example?
    answer: >-
      Install Arm Development Studio 2023.0 or later and have some understanding of the Arm architecture.
      The AEM Fixed Virtual Platform and the full bare-metal example are supplied with Development
      Studio.
  - question: How do I import the bare-metal RME example into Arm Development Studio?
    answer: >-
      Open the IDE and choose File > Import. Select Arm Development Studio > Examples & Programming
      Libraries, then locate and import the RME bare-metal example provided with the installation.
  - question: Which target should I run the example on?
    answer: >-
      Run the example on the Arm Architecture Envelope Model (AEM) Fixed Virtual Platform, which
      is supplied with Arm Development Studio.
  - question: How does this example demonstrate CCA concepts?
    answer: >-
      It illustrates RME, the architectural feature needed to implement CCA, highlighting the
      Realm world in addition to Normal, Secure, and Root worlds. A secure monitor in Root world
      manages transitions between these states, which you can examine with the Arm Debugger.
  - question: Do I need Linux or Android to follow this path?
    answer: >-
      No. The example is bare-metal and runs on the AEM FVP provided with Arm Development Studio,
      so no operating system setup is required.
# END generated_summary_faq

author: Ronan Synnott

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

