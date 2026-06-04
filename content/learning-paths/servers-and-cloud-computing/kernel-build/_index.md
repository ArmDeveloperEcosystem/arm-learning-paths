---
title: Build Linux kernels for Arm cloud instances

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers building custom Linux kernels on Arm servers and cloud instances.

description: Compile and install custom Linux kernels on Arm cloud instances using TuxMake with configurations for 64 KB page sizes and Fastpath testing.

learning_objectives:
    - Set up a build environment for compiling Linux kernels on Arm cloud instances
    - Build custom Linux kernels with various configurations using TuxMake
    - Install and verify custom-built kernels
    - Configure kernels for specific use cases, including 64 KB page sizes and Fastpath testing

prerequisites:
    - An Arm cloud instance with at least 24 vCPUs and 200 GB of free storage running Ubuntu 24.04 LTS
    - Understanding of kernel images and modules
    - Familiarity with GRUB bootloader and initramfs

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:18:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 004436cf14ff0056136889c58d676295c6dd2088f06f57f397a07ec9004e6b44
  summary_generated_at: '2026-06-02T04:14:17Z'
  summary_source_hash: 004436cf14ff0056136889c58d676295c6dd2088f06f57f397a07ec9004e6b44
  faq_generated_at: '2026-06-03T01:18:47Z'
  faq_source_hash: 004436cf14ff0056136889c58d676295c6dd2088f06f57f397a07ec9004e6b44
  summary: >-
    Learn how to build and install custom Linux kernels on Arm cloud instances using TuxMake.
    You will provision an Ubuntu 24.04 LTS Arm server (minimum 24 vCPUs and 200 GB free storage),
    configure a build environment, compile specific kernel versions, and install or package the
    resulting kernels. The path covers standard workflows for general-purpose kernels as well
    as configurations for 64 KB page sizes. It also explains how to produce Fastpath-enabled builds
    for testing workflows, which are build-only. Examples use AWS, but the steps apply to any
    provider offering 64-bit Arm Ubuntu instances. By the end, you will be able to build, install,
    and prepare kernels for Fastpath validation on Arm cloud machines.
  faqs:
  - question: What do I need on my Arm cloud instance before starting?
    answer: >-
      Use an Ubuntu 24.04 LTS Arm instance with at least 24 vCPUs and 200 GB of free storage,
      and ensure you have SSH access. The example uses AWS, but any provider offering 64-bit Arm
      Ubuntu instances is suitable.
  - question: How do I choose which Linux kernel version to build with TuxMake?
    answer: >-
      Specify your desired version with the --tags flag. The versions shown in the examples (such
      as v6.18.1) are valid but arbitrary, so you can substitute the version you need.
  - question: What result should I expect from a standard TuxMake build workflow?
    answer: >-
      Standard workflows produce general-purpose kernels suitable for production deployment, development
      testing, or packaging. You can build for direct installation on the instance or create artifacts
      for downstream packaging, and configure options such as 64 KB page sizes.
  - question: What is the correct workflow for Fastpath builds?
    answer: >-
      Fastpath builds are build-only; do not combine --fastpath true (or the demo shortcut) with
      --kernel-install or any --install-from commands. Build with Fastpath enabled, then copy
      the flat artifacts (for example, the kernel image and modules) to your Fastpath test environment.
  - question: What should I check if compilation is very slow or runs out of memory?
    answer: >-
      Use a sufficiently large Arm instance because smaller instances take longer or can run out
      of memory during compilation. Meeting the minimum of 24 vCPUs and ample free storage helps
      avoid resource-related build failures.
# END generated_summary_faq

author: Geremy Cohen

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - TuxMake

further_reading:
    - resource:
        title: TuxMake documentation
        link: https://tuxmake.org/
        type: documentation
    - resource:
        title: Linux kernel documentation
        link: https://www.kernel.org/doc/html/latest/
        type: documentation
    - resource:
        title: Arm kernel build repository
        link: https://github.com/geremyCohen/arm_kernel_install_guide
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

