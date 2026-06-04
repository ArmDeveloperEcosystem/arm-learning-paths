---
title: Explore Arm Memory Tagging Extension with example programs
description: Learn how to run example C programs on AArch64 Linux to gain an introductory understanding of the Arm Memory Tagging Extension (MTE).

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for developers who want to gain some experience with the Arm Memory Tagging Extension (MTE).

learning_objectives: 
    - Run an example C program to gain an introductory understanding of MTE
    
prerequisites:
    - An AArch64 Linux development machine. Cloud instances can be used, refer to the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:58:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a25cb73b70716e397d9477f8ab9729f4a094143d276e4de68cf8c33b273bb1ff
  summary_generated_at: '2026-06-02T02:52:58Z'
  summary_source_hash: a25cb73b70716e397d9477f8ab9729f4a094143d276e4de68cf8c33b273bb1ff
  faq_generated_at: '2026-06-02T23:58:26Z'
  faq_source_hash: a25cb73b70716e397d9477f8ab9729f4a094143d276e4de68cf8c33b273bb1ff
  summary: >-
    Learn how to build and run a small C program on AArch64 Linux to explore the Arm Memory Tagging
    Extension (MTE). MTE, available in Armv8.5-A and Armv9-A processors, helps detect memory safety
    issues such as buffer overflows and use-after-free. In about 20 minutes, you will follow practical
    steps to compile and execute an example that illustrates how MTE works on a recent AArch64
    system. The only explicit prerequisite is an AArch64 Linux development machine; cloud instances
    from Arm cloud service providers are suitable. QEMU is listed among the tools. After completing
    the path, you will have an introductory understanding of MTE based on a working example.
  faqs:
  - question: What do I need before running the example C program?
    answer: >-
      You need an AArch64 Linux development machine. No other explicit prerequisites are listed.
  - question: Can I use a cloud-based AArch64 instance for this path?
    answer: >-
      Yes. Cloud instances can be used, and the path references a list of Arm cloud service providers.
  - question: Is QEMU required for this Learning Path?
    answer: >-
      QEMU is listed among the tools. The core activity is to build and run a small C program
      on AArch64 Linux; follow the steps to see if QEMU is used in your setup.
  - question: How do I know if my environment supports MTE?
    answer: >-
      MTE is a feature of Armv8.5-A and Armv9-A processors, and the path suggests using a recent
      AArch64 Linux machine. The steps do not provide a specific detection command.
  - question: What result should I expect when I build and run the example?
    answer: >-
      The example demonstrates how MTE detects memory safety issues like buffer overflows and
      use-after-free. Expect behavior that shows MTE in action; the exact output is determined
      by the provided example.
# END generated_summary_faq

author: Jason Andrews

##### Tags

skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - QEMU

further_reading:
    - resource:
        title: MTE User Guide for Android OS
        link: https://developer.arm.com/documentation/108035/latest/
        type: documentation
    - resource:
        title: Arm Memory Tagging Extension (MTE)
        link: https://developer.android.com/ndk/guides/arm-mte
        type: website
    - resource:
        title: AArch64 TAGGED ADDRESS ABI
        link: https://www.kernel.org/doc/Documentation/arm64/tagged-address-abi.rst
        type: documentation
    - resource:
        title: Memory Tagging Extension on MediaTek Dimensity 9000 dev board
        link: https://youtu.be/Ja9pmZ2NqKE
        type: video




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

