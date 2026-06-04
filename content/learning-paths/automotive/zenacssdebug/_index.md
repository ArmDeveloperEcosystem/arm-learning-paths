---
title: Debug Arm Zena CSS Reference Software Stack with Arm Development Studio

description: Learn how to debug the Arm Zena CSS Reference Software Stack using Arm Development Studio on a Fixed Virtual Platform, covering RSE, Safety Island, and Linux kernel debugging workflows.

minutes_to_complete: 60

who_is_this_for: This introductory topic is for software developers who want to use Arm Development Studio to explore and debug the Arm Zena Compute Subsystem (CSS) Reference Software Stack on a Fixed Virtual Platform (FVP).

learning_objectives:
  - Set up and save a debug configuration for the Arm Zena CSS FVP
  - Start Runtime Security Engine (RSE) debug at reset and step through early boot
  - Attach to and debug Safety Island (SI) firmware
  - Attach to the Linux kernel on the primary compute cores and debug user space processes

prerequisites:
  - Ubuntu 22.04 host machine
  - Arm Development Studio 2024.1 or later with a valid license - for support see the [Install Guide for Arm DS](/install-guides/armds) 
  - Basic understanding of the Arm Zena CSS software stack, Armv8-A/Armv9-A cores, and Linux

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:28:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8dccdbdd4d9727f3466987ce918d9df0ed9d4d4f28cd613162bacab01d9c18f3
  summary_generated_at: '2026-06-01T20:59:08Z'
  summary_source_hash: 8dccdbdd4d9727f3466987ce918d9df0ed9d4d4f28cd613162bacab01d9c18f3
  faq_generated_at: '2026-06-02T21:28:53Z'
  faq_source_hash: 8dccdbdd4d9727f3466987ce918d9df0ed9d4d4f28cd613162bacab01d9c18f3
  summary: >-
    This introductory Learning Path shows how to debug the Arm Zena Compute Subsystem (CSS) Reference
    Software Stack on a Fixed Virtual Platform using Arm Development Studio. You will launch the
    Zena CSS FVP with the Iris debug server, create and save a custom debug configuration, and
    set up connections for its heterogeneous subsystems: the Runtime Security Engine (Cortex-M55),
    the Safety Island (Cortex-R82AE), and the primary compute cores (Cortex-A720AE) running Linux.
    You will step the RSE from reset with TF-M symbols, attach to SI firmware, and attach to the
    Linux kernel to debug user space processes. Prerequisites are Ubuntu 22.04, Arm Development
    Studio 2024.1 or later with a valid license, and basic familiarity with Zena CSS, Armv8-A/Armv9-A,
    and Linux.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Ubuntu 22.04 host and Arm Development Studio 2024.1 or later with a valid license.
      A basic understanding of the Arm Zena CSS software stack, Armv8‑A/Armv9‑A cores, and Linux
      is assumed.
  - question: Why can’t Arm Development Studio connect if I launch the FVP from the build environment
      command?
    answer: >-
      Launching with the provided build command does not enable the Iris debug server, so the
      model cannot be debugged from Arm Development Studio. Re‑launch the model with additional
      command‑line options that enable Iris; see FVP_RD_Aspen --help and follow the options shown
      in the Learning Path.
  - question: Which connection method should I choose in Arm Development Studio for this target?
    answer: >-
      Use the Iris interface to create a debug configuration for the Zena CSS FVP. As of Arm Development
      Studio 2025.0 there is no out‑of‑the‑box configuration, so you will create your own and
      save the connections as .launch files.
  - question: How do I hold the RSE at reset and step through early boot?
    answer: >-
      Start a new tmux session if needed, then launch the FVP with the Iris server enabled and
      without running so it stays at reset. Connect from Arm Development Studio, load Trusted
      Firmware‑M symbols, and step from reset through the early boot sequence.
  - question: Can I connect to the Safety Island and the Linux kernel simultaneously?
    answer: >-
      Yes. Arm Development Studio supports heterogeneous systems like Zena CSS, so you can create
      separate connections and attach to all processors at the same time, including the Safety
      Island firmware and the Linux kernel on the primary compute cores.
# END generated_summary_faq

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
  - Cortex-A
  - Cortex-R
operatingsystems:
  - Linux
tools_software_languages:
  - Arm Development Studio
  - Arm Zena CSS
  - FVP

further_reading:
  - resource:
      title: Arm Zena Compute Subsystem (CSS)
      link: https://developer.arm.com/Compute%20Subsystems/Arm%20Zena%20Compute%20Subsystem
      type: website
  - resource:
      title: Arm Development Studio
      link: https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio
      type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

