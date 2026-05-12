---
title: Explore performance gains by increasing the Linux kernel page size on Arm
description: Learn how to install and configure a Linux kernel with 64K page size support on Arm systems to improve memory efficiency and performance for memory-intensive workloads.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to modify the Linux kernel page size on Arm-based systems to improve performance for memory-intensive workloads.

learning_objectives:
  - Explain the differences in page size configuration between Arm64 and x86 architectures.
  - Understand how page size affects memory efficiency and system performance.
  - Check the current memory page size on an Arm-based Linux system.
  - Install and boot into a Linux kernel configured with 64K page size support.
  - Confirm that the 64K page size is active.
  - Optionally revert to the default 4K page size kernel.

prerequisites:
  - Access to an Arm-based Linux system running Ubuntu, Debian, or CentOS.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v2
  generated_at: '2026-05-12T18:20:22Z'
  generator: template
  source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  summary_generated_at: '2026-05-12T18:20:22Z'
  summary_source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  faq_generated_at: '2026-05-12T18:20:22Z'
  faq_source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  summary: >-
    Learn how to install and configure a Linux kernel with 64K page size support on Arm systems
    to improve memory efficiency and performance for memory-intensive workloads. It is designed
    for developers who want to modify the Linux kernel page size on Arm-based systems to improve
    performance for memory-intensive workloads. By the end, you will be able to explain the differences
    in page size configuration between Arm64 and x86 architectures, understand how page size affects
    memory efficiency and system performance, and check the current memory page size on an Arm-based
    Linux system. It focuses on tools and technologies such as bash, Linux environments, and Arm
    platforms including Neoverse. The main steps cover Overview, Change page size on Ubuntu, Change
    page size on Debian, and Change page size on CentOS.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will explain the differences in page size configuration between Arm64 and x86 architectures,
      understand how page size affects memory efficiency and system performance, and check the
      current memory page size on an Arm-based Linux system. Learn how to install and configure
      a Linux kernel with 64K page size support on Arm systems to improve memory efficiency and
      performance for memory-intensive workloads.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers who want to modify the Linux kernel page size
      on Arm-based systems to improve performance for memory-intensive workloads.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Access to an Arm-based Linux system
      running Ubuntu, Debian, or CentOS.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including bash, Linux environments, and Arm platforms such
      as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Change page size on Ubuntu, Change page
      size on Debian, and Change page size on CentOS.
# END generated_summary_faq

author: Geremy Cohen

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
    
armips:
    - Neoverse

operatingsystems:
    - Linux

tools_software_languages:
    - bash

further_reading:
    - resource:
        title: Understanding Memory Page Sizes on Arm64
        link: https://amperecomputing.com/tuning-guides/understanding-memory-page-sizes-on-arm64
        type: documentation
    - resource:
        title: Computer Memory, Wikipedia page
        link: https://en.wikipedia.org/wiki/Page_(computer_memory)
        type: documentation
    - resource:
        title: Network setup, Debian Kernel Source Guide
        link: https://www.debian.org/doc/manuals/debian-reference/ch05.en.html#_kernel_source
        type: documentation
    - resource:
        title: Ubuntu Kernel Build Docs
        link: https://wiki.ubuntu.com/Kernel/BuildYourOwnKernel
        type: documentation
    - resource:
        title: CentOS Documentation
        link: https://docs.centos.org/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

