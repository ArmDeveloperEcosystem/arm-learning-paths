---
title: Get started with Yocto Linux on Qemu

description: Introduction to building a minimal Yocto Linux image and running it on 64-bit Qemu Arm target

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in learning the basics of building Yocto Linux for embedded Arm targets.

learning_objectives: 
    - Build a minimal Yocto Linux image for generic 64-bit Arm target.
    - Run the built Yocto image on Qemu.

prerequisites:
    - Some familiarity with embedded Linux.
    - A linux machine running Ubuntu 22.04 with at least 60 GB of disk space.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:52:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3bcfc51edbab56e3c8416f27045a61b069333e6f0cd130e8689b9a4d9fde1dd6
  summary_generated_at: '2026-06-01T21:59:52Z'
  summary_source_hash: 3bcfc51edbab56e3c8416f27045a61b069333e6f0cd130e8689b9a4d9fde1dd6
  faq_generated_at: '2026-06-02T22:52:18Z'
  faq_source_hash: 3bcfc51edbab56e3c8416f27045a61b069333e6f0cd130e8689b9a4d9fde1dd6
  summary: >-
    Learn how to build a minimal Yocto Linux image for a generic 64-bit Arm (Cortex-A class) target
    and run it under QEMU. Working on a Linux host (Ubuntu 22.04) with at least 60 GB of disk
    space, you use the Yocto Project—starting from the Poky reference distribution—to configure
    and produce a bootable image, then launch it on a 64-bit Arm QEMU machine. This introductory
    path is aimed at developers who want the basics of Yocto for embedded Arm. By the end, you
    will have built a minimal image and verified it by running it in QEMU. Some familiarity with
    embedded Linux is expected.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use a Linux host running Ubuntu 22.04 with at least 60 GB of disk space. Some familiarity
      with embedded Linux is also expected.
  - question: Which Yocto distribution should I use to start the build?
    answer: >-
      Poky, the Yocto Project reference distribution, is used as the starting point to build a
      minimal image. You will work with Yocto recipes as part of this process.
  - question: Do I need physical Arm hardware to complete this Learning Path?
    answer: >-
      No. The image is run on a 64-bit QEMU Arm target, so you can complete the steps without
      physical Arm hardware.
  - question: Which target architecture is used when running under QEMU?
    answer: >-
      The steps target a generic 64-bit Arm platform (Cortex-A class) and boot the built image
      under QEMU.
  - question: What result should I expect after the build, and how do I run it?
    answer: >-
      Expect a minimal Yocto Linux image produced by the Yocto build system. You will launch QEMU
      and boot this image as shown in the steps to validate the build.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Embedded Linux
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Yocto Project
    - QEMU

further_reading:
    - resource:
        title: Yocto Project Reference Manual
        link: https://docs.yoctoproject.org/ref-manual/index.html
        type: documentation

    - resource:
        title: Poky Reference Manual
        link: https://docs.yoctoproject.org/1.0/poky-ref-manual/poky-ref-manual.html
        type: documentation

    - resource:
        title: QEMU documentation
        link: https://www.qemu.org/docs/master/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

