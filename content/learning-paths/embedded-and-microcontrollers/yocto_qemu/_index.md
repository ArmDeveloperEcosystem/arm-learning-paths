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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T19:00:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 10d5a7c5135957134e58afc8b9c6bb19d977c054cd7b984aa46ab0552b833c8f
  summary_generated_at: '2026-08-13T19:00:02Z'
  summary_source_hash: 10d5a7c5135957134e58afc8b9c6bb19d977c054cd7b984aa46ab0552b833c8f
  faq_generated_at: '2026-08-13T19:00:02Z'
  faq_source_hash: 10d5a7c5135957134e58afc8b9c6bb19d977c054cd7b984aa46ab0552b833c8f
  summary: >-
    You'll build a minimal Yocto Linux image for a 64-bit Arm target and run it in QEMU. First,
    you'll start with Poky, configure a generic Arm build, and use Yocto recipes to produce an image.
    Then, you'll launch QEMU with the generated image, verify a successful boot, and use the virtual
    system as a baseline for further iterations.
  faqs:
  - question: Which Yocto distribution should I start with here?
    answer: >-
      Use Poky, the Yocto Project reference distribution. You'll build a minimal image from Poky
      before running it under QEMU.
  - question: How do I configure Yocto for the 64-bit Arm QEMU machine?
    answer: >-
      In `conf/local.conf`, uncomment `MACHINE ?= "qemuarm64"`. This selects the 64-bit Arm
      machine that you'll build and run with QEMU.
  - question: How do I know the build finished correctly before I run QEMU?
    answer: >-
      You'll know the build finished correctly when you have a generated image, and the
      build completes without errors.
  - question: What should I check if QEMU doesn't boot my image?
    answer: >-
      Verify that the build targeted a 64-bit Arm machine and that you're launching QEMU with
      the image produced by the build.
  - question: Can I add packages or customize recipes beyond the minimal image?
    answer: >-
      The steps in the Learning Path are focused on producing a minimal image and don't cover customization.
      You can extend the build later by modifying Yocto recipes.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
