---
title: Debug Neoverse N2 Reference Design with Arm Development Studio

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who are interested in debugging the Arm Neoverse N2 Reference Firmware Stack.

learning_objectives: 
    - Create a debug connection.
    - Debug a System Control Processor (SCP).
    - Debug Arm TF-A (Trusted Firmware-A).

prerequisites:
    - Arm Development Studio, and a license to use it.
    - An Arm Neoverse Reference Design (RD) Software Stack.
    - A Fixed Virtual Platform (FVP).
    - A basic understanding of Neoverse Reference Design (RD) platform boot.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:00:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d060151c5f6ac7a743fb53cd3d2a10aa23f8f09245122a199a84ae17a8ab5ff9
  summary_generated_at: '2026-06-02T05:00:55Z'
  summary_source_hash: d060151c5f6ac7a743fb53cd3d2a10aa23f8f09245122a199a84ae17a8ab5ff9
  faq_generated_at: '2026-06-03T02:00:58Z'
  faq_source_hash: d060151c5f6ac7a743fb53cd3d2a10aa23f8f09245122a199a84ae17a8ab5ff9
  summary: >-
    Learn how to debug the Neoverse N2 Reference Design firmware stack using Arm Development Studio
    on Linux. This path shows how to create a debug connection to an associated Fixed Virtual
    Platform (FVP), step through early firmware stages, and work with SCP/LCP/RSE and Arm TF-A
    (BL1 and BL31). You adjust SCP build settings for easier debugging, apply a BL1 workaround
    to allow early attachment, and use the Functions view to set precise breakpoints. The path
    is advanced, takes about 30 minutes, and assumes Arm Development Studio with a valid license,
    the Neoverse RD-N2 Software Stack, an FVP, and a basic understanding of the Neoverse RD platform
    boot sequence.
  faqs:
  - question: What do I need before running the debug steps?
    answer: >-
      You need Arm Development Studio with a valid license, the Neoverse RD-N2 Reference Design
      Software Stack, an associated FVP, and a basic understanding of RD platform boot. The environment
      targets Linux.
  - question: Which optimization flag should I use for SCP firmware debug, and how do I change
      it?
    answer: >-
      SCP firmware debug uses -Og by default, which can optimize variables in ways that hinder
      debugging. To switch to -O0, edit rd-infra/scp/cmake/Toolchain/<compiler>-Baremetal.cmake
      and change string(APPEND CMAKE_${language}_FLAGS_DEBUG_INIT "-Og") to use "-O0".
  - question: Why can’t I start the debugger at BL1, and what’s the workaround?
    answer: >-
      RSE CPU wait hold means AP cores are powered off, so you cannot start the debugger until
      RSE powers them. As a workaround, modify BL1 to spin on entry by adding a "b ." in the bl1_entrypoint
      function at <workspace>/rd-infra/tf-a/bl1/aarch64/bl1_entrypoint.S.
  - question: How do I set a breakpoint for BL31?
    answer: >-
      Open the Functions view in Arm Development Studio, search for bl31_entrypoint, and set a
      breakpoint there. Continue execution and observe the console as TF-A advances from BL1 to
      BL2 to BL31, where the breakpoint will be hit.
  - question: How do I add symbols to debug BL33/UEFI?
    answer: >-
      First boot the FVP once without debugging to capture symbol locations and relocation addresses
      from the Non-secure AP console. Repeat the same actions in the same order during debugging,
      and use the recorded addresses; the log files are stored under your workspace in the rd-infr
      directory as indicated in the steps.
# END generated_summary_faq

author: Daniel Nguyen

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Arm Development Studio

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Neoverse Reference Design Platform Software Documentation
        link: https://neoverse-reference-design.docs.arm.com/en/latest/index.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

