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
  - Arm Development Studio 2024.1 or later with a valid license - for support see the [Install Guide for Arm DS](/install-guides/armds/) 
  - Basic understanding of the Arm Zena CSS software stack, Armv8-A/Armv9-A cores, and Linux

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-24T15:37:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 74740788edbfe7ea09bf955455b4aeaed00e667fa8c9d68467353c1f64528b08
  summary_generated_at: '2026-06-24T15:37:11Z'
  summary_source_hash: 74740788edbfe7ea09bf955455b4aeaed00e667fa8c9d68467353c1f64528b08
  faq_generated_at: '2026-06-24T15:37:11Z'
  faq_source_hash: 74740788edbfe7ea09bf955455b4aeaed00e667fa8c9d68467353c1f64528b08
  summary: >-
    You'll debug the Arm Zena Compute Subsystem (CSS) reference
    software stack on a Fixed Virtual Platform using Arm Development Studio. You'll launch the
    FVP with the Iris debug server enabled, then create and save a custom Arm DS configuration. You'll establish connections
    to each heterogeneous component within Zena CSS to debug the Linux kernel and user processes. By the end, you'll create reusable `.launch`
    files, step through early RSE boot, and attach to Safety Island and Linux targets to inspect
    execution across the system.
  faqs:
  - question: Which FVP launch method should I use for debugging?
    answer: >-
      Use the launch invocation that enables the Iris debug server. The default build-environment
      command runs the stack but does not enable Iris, so Arm Development Studio cannot connect.
  - question: How should I organize and save my debug connections in Arm Development Studio?
    answer: >-
      Create a General Project to store the connection files and save each connection as a `.launch`
      file. This makes it easy to reuse and enhance configurations for each subsystem.
  - question: What is the expected workflow to debug the RSE from reset?
    answer: >-
      Start the FVP with Iris enabled and hold the model at reset, then connect from Arm Development
      Studio. Load Trusted Firmware‑M symbols and step through the early boot code.
  - question: Can I connect to all Zena CSS processors at the same time?
    answer: >-
      Yes. Arm Development Studio supports heterogeneous systems, so you can connect to the RSE,
      Safety Island, and primary compute cores simultaneously, though you might prefer to set up
      one connection fully before adding others.
  - question: Why isn’t there a predefined Zena CSS target in Arm Development Studio?
    answer: >-
      As of Arm Development Studio 2025.0, there is no out-of-the-box configuration for the Zena
      CSS FVP. Create one using the Iris interface as shown in the Learning Path.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

