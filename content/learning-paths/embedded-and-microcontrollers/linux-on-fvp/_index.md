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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:10:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 701a686840371c020ddcdd1b763b27b6c3954317318ec2cb67e0cd9b00ed0f5f
  summary_generated_at: '2026-08-12T20:10:11Z'
  summary_source_hash: 701a686840371c020ddcdd1b763b27b6c3954317318ec2cb67e0cd9b00ed0f5f
  faq_generated_at: '2026-08-12T20:10:11Z'
  faq_source_hash: 701a686840371c020ddcdd1b763b27b6c3954317318ec2cb67e0cd9b00ed0f5f
  summary: >-
    You'll boot a Linux software stack on an Arm FVP and debug it with Arm
    Development Studio. First, you'll configure Trusted Firmware-A for the target CPU, adjust the device
    tree, and verify build outputs. Then, you'll launch the FVP, capture UART logs, create a debug
    configuration, and step through Trusted Firmware-A and the Linux kernel.
  faqs:
  - question: How do I know my Trusted Firmware-A build includes the correct `cpu_ops` support?
    answer: >-
      Enable the `cpu_ops` framework for your target CPU when building TF-A. If `cpu_ops` is missing,
      Linux might fail to start. Confirm that the build selects the CPU-specific implementation
      (for example, `cortex_a55` or `cortex_a53`) from `lib/cpus/aarch64`.
  - question: What should I change in the device tree for an Arm CPU FVP?
    answer: >-
      Remove PCI and SMMU nodes and ensure CPU affinity values are set correctly. Leaving unsupported
      PCI or SMMU entries can cause a kernel panic during boot.
  - question: What result should I expect in the build output before launching the FVP?
    answer: >-
      Expect an output directory such as `output/aemfvp-a/aemfvp-a` containing items such as `Image`
      and `Image.defconfig`, as shown by the `tree` command. Proceed when the expected files and symlinks
      are present.
  - question: How do I capture and review the FVP boot log?
    answer: >-
      Use the provided run command with `<PATH_TO_LOG>` to save UART output. Review the log for
      normal Linux boot messages and confirm there are no PCI or SMMU-related panics.
  - question: Which Arm Development Studio version should I use, and how do I start it?
    answer: >-
      Arm DS `v2022.2` or later is recommended to support DWARF 5 debug information used by GCC
      11 and later. Start it with `/opt/arm/developmentstudio-2022.2/bin/armds_ide`, then create
      a debug configuration to step through Trusted Firmware-A and the Linux kernel.
# END generated_summary_faq

author: Qixiang Xu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
