---
title: Get started with the Raspberry Pi 4

description: Learn how to build and run multiple software examples on the Raspberry Pi 4, including TensorFlow and Docker applications, and compare its performance to Arm cloud servers.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for software developers interested in the Raspberry Pi 4.

learning_objectives: 
    - Build and run multiple software examples on the Raspberry Pi 4
    - Compare and contrast the Raspberry Pi 4 to an Arm cloud server

prerequisites:
    - A Raspberry Pi 4 board
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:48:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2d32bde0364b306f839bfa9f77cae9fb7b4262d350c9dac716eab99d332c79ca
  summary_generated_at: '2026-08-13T18:48:57Z'
  summary_source_hash: 2d32bde0364b306f839bfa9f77cae9fb7b4262d350c9dac716eab99d332c79ca
  faq_generated_at: '2026-08-13T18:48:57Z'
  faq_source_hash: 2d32bde0364b306f839bfa9f77cae9fb7b4262d350c9dac716eab99d332c79ca
  summary: >-
    You'll compare a Raspberry Pi 4 and an Arm-based cloud instance by running the same workloads
    on both systems. First, you'll install 64-bit Raspberry Pi OS and verify each system with `uname`.
    Then, you'll build a Linux kernel, install TensorFlow, and run a quickstart example. You'll use
    matching commands to compare platform behavior and build times.
  faqs:
  - question: How do I know both systems are configured for 64-bit Arm before comparing results?
    answer: >-
      Run `uname -a` on each machine and confirm the architecture shows `aarch64`. The exact kernel
      version string might differ, but the architecture should match on both.
  - question: Which Raspberry Pi OS image should I write to the SD card?
    answer: >-
      Use the 64-bit version of Raspberry Pi OS.
  - question: Where should I run the TensorFlow example, and which example should I use?
    answer: >-
      Run it on both the Raspberry Pi 4 and the Arm-based cloud server to compare behavior. Use the
      TensorFlow quickstart example or the quickstart code provided in the Learning Path.
  - question: What outcome should I expect from the Linux kernel compile comparison?
    answer: >-
      Every recent cloud server is faster than a Raspberry Pi 4. Record the
      elapsed build time on both systems to understand the relative difference.
  - question: How do I choose a cloud instance for this comparison?
    answer: >-
      Use an Arm-based instance from a cloud service provider. For instructions to select and provision an instance, follow the [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/).
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Embedded Linux
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Raspberry Pi
    - TensorFlow
    - Docker

further_reading:
    - resource:
        title: Raspberry Pi OS documentation
        link: https://www.raspberrypi.com/documentation/computers/os.html
        type: documentation
    - resource:
        title: Image Classification with MobilenetV2, Arm NN, and TensorFlow Lite Delegate pre-built binaries Tutorial
        link: https://developer.arm.com/documentation/102561
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
