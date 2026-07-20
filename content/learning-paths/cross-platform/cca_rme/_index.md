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
  generated_at: '2026-07-02T19:06:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  summary_generated_at: '2026-07-02T19:06:31Z'
  summary_source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  faq_generated_at: '2026-07-02T19:06:31Z'
  faq_source_hash: a1685fb43efecb9690d03c7f8ee64ab20ae8aece91190e2223705106568b1038
  summary: >-
    You'll learn the key ideas of Arm Confidential Compute Architecture
    (CCA) and see how Realm Management Extension (RME) supports a CCA system. First, you'll review how
    CCA extends TrustZone with Normal, Secure, Realm, and Root worlds, with a secure monitor orchestrating
    transitions. Then, you'll import a bare-metal RME example included with Arm Development
    Studio and run it on the Arm Architecture Envelope Model (AEM) Fixed Virtual Platform supplied
    with the tools. Using the Arm Debugger, you'll explore and debug the example to examine
    system behavior in a controlled model environment and connect the architectural concepts to
    a working RME setup.
  faqs:
  - question: Where do I import the RME bare-metal example in Arm Development Studio?
    answer: >-
      Open the IDE and choose **File > Import... > Arm Development Studio > Examples & Programming
      Libraries**. Then, select the RME bare-metal example that targets the AEM Fixed Virtual Platform.
  - question: Which target should I use to run the example?
    answer: >-
      Run the project on the Arm Architecture Envelope Model (AEM) Fixed Virtual Platform supplied
      with Development Studio. Make sure the launch targets the AEM FVP before starting the
      debugger.
  - question: Do I need an operating system or a physical board to follow the steps?
    answer: >-
      No. The example is bare-metal and runs on the supplied AEM FVP, so you don’t need an OS or
      hardware board.
  - question: How does this example connect to CCA concepts?
    answer: >-
      It demonstrates Realm Management Extension (RME), a processor feature needed to implement
      a CCA system. CCA adds Normal, Secure, Realm, and Root worlds, with a secure monitor in
      Root managing transitions.
  - question: What should I check if the example is missing or fails to import?
    answer: >-
      Confirm you're using Arm Development Studio 2023.0 or later because the example is provided
      with that version or newer. If it still doesn’t appear, verify that the examples and the
      AEM FVP components are installed with your setup.
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
