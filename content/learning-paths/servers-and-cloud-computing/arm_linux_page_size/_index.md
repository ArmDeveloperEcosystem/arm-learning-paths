---
title: Explore performance gains by increasing the Linux kernel page size on Arm
description: Learn how to install and configure Linux kernels with 16K or 64K page sizes on Arm systems, then evaluate the memory and performance trade-offs.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to modify the Linux kernel page size on Arm-based systems to improve performance for memory-intensive workloads.

learning_objectives:
  - Explain the differences in page size configuration between Arm64 and x86 architectures.
  - Understand how page size affects memory efficiency and system performance.
  - Check the current memory page size on an Arm-based Linux system.
  - Install and boot into a Linux kernel configured with 16K or 64K page size support.
  - Confirm that the selected page size is active.
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
    You'll evaluate and change the Linux kernel base page size on Arm by installing and booting a
    16K or 64K configuration. You'll check the current setting with `getconf` and `uname`, then use
    distribution-specific instructions. Debian provides a packaged 16K kernel and a source-build
    route for 64K, while Ubuntu and CentOS provide packaged 64K kernels. After rebooting, you'll
    validate the selected page size and optionally return to the default 4K kernel.
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
      Use the Ubuntu section for Ubuntu 22.04 LTS or later, the Debian section for Debian 12 or
      later, and the CentOS section for CentOS 9 or later. On Debian, you can install the packaged
      16K kernel or build a 64K kernel from the Debian source package.
  - question: How do I confirm that the selected page size is active after installation and reboot?
    answer: >-
      Re-run `getconf PAGESIZE` and expect `16384` for a 16K kernel or `65536` for a 64K kernel. Also
      check `uname -r` to verify that the running kernel matches the kernel you installed.
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
