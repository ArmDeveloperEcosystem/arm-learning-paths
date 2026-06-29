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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:30:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  summary_generated_at: '2026-06-26T17:30:49Z'
  summary_source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  faq_generated_at: '2026-06-26T17:30:49Z'
  faq_source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  summary: >-
    You'll evaluate and change the Linux kernel base page size on Arm, focusing
    on installing and booting a 64K configuration. First, you'll start with page size fundamentals and a
    quick check of the current setting using `getconf` and `uname`. OS-specific steps include Ubuntu
    and CentOS package-based flows, while Debian requires building a 64K kernel from source using
    the Debian source package. After reboot, you'll validate the change by seeing `65536` from `getconf`
    and the expected kernel string. You'll also review common Arm page size options and an optional
    step to revert to the default 4K kernel after testing.
  faqs:
  - question: How do I check the current base page size and kernel in use?
    answer: >-
      Run `getconf PAGESIZE` and `uname -r`. On a 4K configuration, the first line shows `4096`,
      followed by the running kernel version and flavor.
  - question: What should I do if `getconf` does not show `4096` before I begin?
    answer: >-
      A value other than `4096` indicates the system is already using a non-4K page size, such
      as `16384` or `65536`. Note the current value and proceed only if a change is needed.
  - question: Which distribution-specific section should I follow?
    answer: >-
      Use the Ubuntu section for Ubuntu 22.04 LTS or later, the Debian section for Debian 11 or
      later, and the CentOS section for CentOS 9 or later. Debian doesn't provide a 64K kernel
      package, so follow the steps to build from the Debian source package.
  - question: How do I confirm that the 64K page size is active after installation and reboot?
    answer: >-
      Re-run `getconf PAGESIZE` and expect `65536`. Also check `uname -r` to verify the kernel string
      matches the newly installed kernel.
  - question: How can I revert to a 4K page size after testing?
    answer: >-
      Use the optional revert step to return to the distribution’s default 4K kernel, then verify
      with `getconf PAGESIZE` that it shows `4096`. This restores the original base page size.
# END generated_summary_faq

author: Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
