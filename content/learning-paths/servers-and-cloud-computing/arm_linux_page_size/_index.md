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
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:19:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  summary_generated_at: '2026-06-02T03:07:24Z'
  summary_source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  faq_generated_at: '2026-06-03T00:19:30Z'
  faq_source_hash: 67004eb9a75926144eb6f75124104972b3cf20a57a22b698c9359d20db3eca02
  summary: >-
    This Learning Path shows how to install and boot a Linux kernel configured for 64K page size
    on Arm-based systems to improve memory efficiency and performance for memory‑intensive workloads.
    You will learn the role of page size, how Arm64 differs from x86, and how page size impacts
    efficiency and performance. The steps cover checking the current page size, switching to a
    64K kernel on Ubuntu 22.04 LTS or later, Debian 11 “Bullseye” or later (compiled from source),
    and CentOS 9 or later, then confirming the change and optionally reverting to a 4K kernel.
    Prerequisite: access to an Arm-based Linux system running Ubuntu, Debian, or CentOS. The path
    uses bash and is introductory.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to an Arm-based Linux system running Ubuntu, Debian, or CentOS. No other
      explicit prerequisites are listed.
  - question: Which Linux distributions and versions are covered?
    answer: >-
      Ubuntu 22.04 LTS or later, Debian 11 “Bullseye” or later, and CentOS 9 or later. The steps
      are distribution-specific.
  - question: How do I check my current memory page size and kernel?
    answer: >-
      Run getconf PAGESIZE and uname -r. A first line of 4096 indicates a 4K base-page-size kernel;
      if it is different, you are already using a non-4K page size.
  - question: On Debian, do I need to compile a 64K kernel and which source should I use?
    answer: >-
      Yes. Debian does not provide a 64K kernel package, so you must compile from source; you
      can use kernel.org or the Debian source package, and this path uses the Debian source package.
  - question: How do I verify the 64K page size is active, and can I revert to 4K?
    answer: >-
      Re-run getconf PAGESIZE after booting the new kernel; it should no longer report 4096 and
      should reflect the 64K configuration. The path includes an optional step to revert to the
      default 4K page size kernel.
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

