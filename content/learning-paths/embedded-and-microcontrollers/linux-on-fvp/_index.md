---
title: Debug Trusted Firmware-A and the Linux kernel on Arm FVP with Arm Development Studio 

description: Learn how to boot a Linux software stack on Arm Fixed Virtual Platforms (FVPs), then debug Trusted Firmware-A and the Linux kernel using Arm Development Studio.

minutes_to_complete: 60

who_is_this_for: This topic is for developers who want to run Linux on Arm Fixed Virtual Platforms (FVPs) and debug both Trusted Firmware-A and the Linux kernel using Arm Development Studio.

learning_objectives:
    - Boot and run a Linux software stack on an Arm Fixed Virtual Platform (FVP).
    - Debug Trusted Firmware-A and the Linux kernel using Arm Development Studio.
prerequisites:
    - A Linux-based x86-64 host computer with Arm Development Studio installed.
    - Basic understanding of Assembly and C programming.
   

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:29:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5943d817827bef274f175f7c14249cad769b2160094b3c65d7476aca6cbf0a1d
  summary_generated_at: '2026-06-01T21:43:52Z'
  summary_source_hash: 5943d817827bef274f175f7c14249cad769b2160094b3c65d7476aca6cbf0a1d
  faq_generated_at: '2026-06-02T22:29:22Z'
  faq_source_hash: 5943d817827bef274f175f7c14249cad769b2160094b3c65d7476aca6cbf0a1d
  summary: >-
    This introductory Learning Path shows how to boot a Linux software stack on Arm Fixed Virtual
    Platforms (FVPs) and then debug Trusted Firmware-A (TF-A) and the Linux kernel using Arm Development
    Studio. You will configure TF-A build flags to include cpu_ops for CPU-specific initialization,
    adjust the device tree for CPU FVPs by removing unsupported PCI and SMMU nodes and setting
    correct CPU affinity, launch the stack on an FVP, and verify expected build outputs and UART
    logs. The target environment is a Linux-based x86-64 host with Arm Development Studio installed.
    FVPs are fast, functional simulation models of Arm hardware, so you can develop and debug
    without physical silicon. Estimated time to complete is approximately 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Linux-based x86-64 host computer with Arm Development Studio installed, and a
      basic understanding of Assembly and C programming. No other prerequisites are explicitly
      listed.
  - question: How should I modify the device tree for CPU FVPs?
    answer: >-
      Remove PCI and SMMU nodes and ensure CPU affinity values are set correctly. Leaving PCI
      or SMMU nodes in place can cause a kernel panic during boot on CPU FVPs.
  - question: How do I confirm that cpu_ops is enabled in my TF-A build?
    answer: >-
      Follow the steps to configure TF-A build flags to include cpu_ops support for your CPU.
      If the proper cpu_ops are missing, Linux may fail to boot; the steps describe enabling the
      correct CPU-specific implementations.
  - question: What result should I expect from the build output?
    answer: >-
      In the output directory (for example, output/aemfvp-a/aemfvp-a/), expect files such as Image
      and Image.defconfig, often as symlinks to the component outputs. If these are missing, revisit
      the build and configuration steps.
  - question: How do I run and debug the software stack on an FVP?
    answer: >-
      Use the provided command templates, substituting <SRC_PATH> and <PATH_TO_LOG>, and capture
      the UART output to verify the boot. For debugging, Arm Development Studio v2022.2 or later
      is recommended for DWARF 5 support; launch the IDE and follow the steps to create a debug
      configuration for TF-A and the Linux kernel.
# END generated_summary_faq

author: Qixiang Xu

### Tags
skilllevels: Introductory
subjects: Embedded Linux
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Arm Development Studio
    - C
    - Assembly

further_reading:
    - resource:
        title: Fast Models Fixed Virtual Platforms Reference Guide
        link: https://developer.arm.com/documentation/100966/
        type: documentation
    - resource:
        title: Fixed Virtual Platforms Resources
        link: https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms
        type: website
    - resource:
        title: Fast Models Reference Guide
        link: https://developer.arm.com/documentation/100964/1128/?lang=en
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

