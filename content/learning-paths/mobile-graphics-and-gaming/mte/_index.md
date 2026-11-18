---
title: Explore Arm Memory Tagging Extension with an example C program
description: Learn how to run an example C program on AArch64 Linux to gain an introductory understanding of the Arm Memory Tagging Extension (MTE).

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for developers who want to gain experience with the Arm Memory Tagging Extension (MTE).

learning_objectives:
    - Build an MTE-enabled C program on AArch64 Linux
    - Run the program to observe MTE detecting an invalid memory access
    - Use QEMU to run the example when MTE hardware is unavailable

prerequisites:
    - An AArch64 Linux development machine. You can also use a cloud instance. For more information, see the list of [Arm cloud service providers](/learning-paths/servers-and-cloud-computing/csp/).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:09:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cdf48a76a0d88e2c7756eb01c48aa81b341366bcb5d224ba710e74c15d5b1f21
  summary_generated_at: '2026-08-17T22:09:08Z'
  summary_source_hash: cdf48a76a0d88e2c7756eb01c48aa81b341366bcb5d224ba710e74c15d5b1f21
  faq_generated_at: '2026-08-17T22:09:08Z'
  faq_source_hash: cdf48a76a0d88e2c7756eb01c48aa81b341366bcb5d224ba710e74c15d5b1f21
  summary: >-
    You'll explore Arm MTE on an `aarch64` Linux system. First, you'll build and run
    a small C program that triggers buffer-overflow and use-after-free errors, then observe the
    resulting faults or diagnostics. You'll use a recent Arm system or supported Arm-based cloud instance
    to relate MTE behavior to invalid memory accesses.
  faqs:
  - question: How do I know if my system can demonstrate MTE?
    answer: >-
      MTE is implemented in Armv8.5-A and Armv9-A processors. Verify that you're using an AArch64
      Linux system with hardware that supports MTE. Otherwise, the example might not show tagging-related
      behavior.
  - question: What result should I expect when running the example program?
    answer: >-
      Expect behavior that illustrates MTE catching memory safety issues, such as a fault or diagnostic
      triggered by an invalid access. The outcome should align with the bug the program intentionally
      exercises.
  - question: Can I run the example without MTE hardware?
    answer: >-
      Yes. Install `qemu-user` and run the example with `qemu-aarch64 ./mte-example`. This lets
      you exercise MTE behavior when the processor doesn't implement MTE.
  - question: What should I check if the program runs without showing any MTE effects?
    answer: >-
      Confirm you're on AArch64 Linux and that the processor implements MTE (Armv8.5-A or Armv9-A).
      If the processor lacks MTE support, install `qemu-user` and run `qemu-aarch64 ./mte-example`
      to exercise the MTE behavior through emulation.
  - question: What invalid memory access does the example demonstrate?
    answer: >-
      The example writes beyond a 16-byte allocation granule at offset `0x10`. MTE detects the
      tag mismatch and should generate an exception.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
