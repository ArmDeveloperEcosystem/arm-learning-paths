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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: 004436cf14ff0056136889c58d676295c6dd2088f06f57f397a07ec9004e6b44
  summary: >-
    Compile and install custom Linux kernels on Arm cloud instances using TuxMake with configurations
    for 64 KB page sizes and Fastpath testing. It is designed for software developers building
    custom Linux kernels on Arm servers and cloud instances. By the end, you will be able to set
    up a build environment for compiling Linux kernels on Arm cloud instances, build custom Linux
    kernels with various configurations using TuxMake, and install and verify custom-built kernels.
    It focuses on tools and technologies such as TuxMake, Linux environments, Arm platforms including
    Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle. The
    main steps cover Set up your Arm instance for kernel building, Build and install custom Linux
    kernels, and Build kernels for Fastpath validation.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will set up a build environment for compiling Linux kernels on Arm cloud instances,
      build custom Linux kernels with various configurations using TuxMake, and install and verify
      custom-built kernels. Compile and install custom Linux kernels on Arm cloud instances using
      TuxMake with configurations for 64 KB page sizes and Fastpath testing.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers building custom Linux kernels on Arm servers
      and cloud instances.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm cloud instance with at least
      24 vCPUs and 200 GB of free storage running Ubuntu 24.04 LTS; Understanding of kernel images
      and modules; Familiarity with GRUB bootloader and initramfs.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including TuxMake, Linux environments, Arm platforms such
      as Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up your Arm instance for kernel building, Build
      and install custom Linux kernels, and Build kernels for Fastpath validation.
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

