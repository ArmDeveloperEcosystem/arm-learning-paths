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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:15Z'
  generator: template
  source_hash: 8dccdbdd4d9727f3466987ce918d9df0ed9d4d4f28cd613162bacab01d9c18f3
  summary: >-
    Learn how to debug the Arm Zena CSS Reference Software Stack using Arm Development Studio
    on a Fixed Virtual Platform, covering RSE, Safety Island, and Linux kernel debugging workflows.
    It is designed for This introductory topic is for software developers who want to use Arm
    Development Studio to explore and debug the Arm Zena Compute Subsystem (CSS) Reference Software
    Stack on a Fixed Virtual Platform (FVP). By the end, you will be able to set up and save a
    debug configuration for the Arm Zena CSS FVP, start Runtime Security Engine (RSE) debug at
    reset and step through early boot, and attach to and debug Safety Island (SI) firmware. It
    focuses on tools and technologies such as Arm Development Studio, Arm Zena CSS, and FVP, Linux
    environments, and Arm platforms including Cortex-A and Cortex-R. The main steps cover Getting
    started, Launch the FVP, Configure the model, Create debug connections, and Debug RSE from
    reset.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will set up and save a debug configuration for the Arm Zena CSS FVP, start Runtime Security
      Engine (RSE) debug at reset and step through early boot, and attach to and debug Safety
      Island (SI) firmware. Learn how to debug the Arm Zena CSS Reference Software Stack using
      Arm Development Studio on a Fixed Virtual Platform, covering RSE, Safety Island, and Linux
      kernel debugging workflows.
  - question: Who is this Learning Path for?
    answer: >-
      This introductory topic is for software developers who want to use Arm Development Studio
      to explore and debug the Arm Zena Compute Subsystem (CSS) Reference Software Stack on a
      Fixed Virtual Platform (FVP).
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Ubuntu 22.04 host machine; Arm Development
      Studio 2024.1 or later with a valid license - for support see the [Install Guide for Arm
      DS](/install-guides/armds); Basic understanding of the Arm Zena CSS software stack, Armv8-A/Armv9-A
      cores, and Linux.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Arm Development Studio, Arm Zena CSS, and FVP, Linux
      environments, and Arm platforms such as Cortex-A and Cortex-R.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Getting started, Launch the FVP, Configure the model,
      Create debug connections, and Debug RSE from reset.
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

