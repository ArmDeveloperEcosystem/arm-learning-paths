---
title: Learn about context switching on Arm Cortex-M processors

description: Learn how to implement context switching operations on Arm Cortex-M processors using the Memory Protection Unit and SysTick exception in a bare-metal environment.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers who would like to learn about context switching operations on Cortex-M processors in a bare-metal environment.

learning_objectives: 
    - Understand the basics of context switching 
    - Learn how to program the Memory Protection Unit (MPU)
    - Learn how to use the SysTick exception with context switching operations
    - Build and run an example project with Arm Development Studio (Arm DS)

prerequisites:
    - Basic knowledge and familiarity with Cortex-M processors.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:28:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0b7a5895a87de83903c223215845b6c840602663838c0682f46e50d139d69c59
  summary_generated_at: '2026-07-08T15:28:40Z'
  summary_source_hash: 0b7a5895a87de83903c223215845b6c840602663838c0682f46e50d139d69c59
  faq_generated_at: '2026-07-08T15:28:40Z'
  faq_source_hash: 0b7a5895a87de83903c223215845b6c840602663838c0682f46e50d139d69c59
  summary: >-
    You'll build and run an open source example that
    demonstrates context switching on Arm Cortex‑M processors in a bare‑metal environment. Using
    Arm Development Studio, you'll work with a project that configures the Memory Protection Unit
    (MPU) and drives switches with the SysTick exception to alternate execution between two threads.
    You'll compile the code, run it on a Fast Models Fixed Virtual Platform (FVP),
    and examine the behavior to understand how MPU setup and SysTick handling interact during
    a simple real‑time kernel‑style switch. By the end, you'll recognize the expected thread
    switching pattern and relate it to the MPU and SysTick configuration used in the example.
  faqs:
  - question: Where do I get the example project used in this path?
    answer: >-
      Use the open source example projects provided alongside the Armv8‑M Memory Model and
      MPU User Guide. The steps reference the GitHub repository that contains the sources.
  - question: Which tools should I use to build and run the project?
    answer: >-
      Build and run the example with Arm Development Studio, Arm Compiler for Embedded, Fast
      Models Fixed Virtual Platforms (FVP), and CMSIS at the versions listed in the steps. Use
      the same versions to match the expected build files and project settings.
  - question: What result should I expect when I run the example?
    answer: >-
      You'll see a demonstration of simple real‑time kernel context switching between two
      threads, driven by the SysTick exception and protected by MPU regions. The steps explain
      how to observe this behavior when the image runs on the FVP.
  - question: What should I check if the project doesn't build in Arm Development Studio?
    answer: >-
      Verify that the toolchain and component versions match the ones listed in the steps. Also
      confirm that the project references CMSIS correctly and that any include paths align with
      your workspace layout.
  - question: Where is the MPU and SysTick configuration in the project?
    answer: >-
      Configure the MPU and the SysTick exception in the example’s source files as outlined
      in the steps. Review the provided code to see where MPU regions are programmed and where
      the SysTick handler drives the context switch.
# END generated_summary_faq

author: Uma Ramalingam

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - CMSIS
    - Arm Development Studio

further_reading:
    - resource:
        title: Learn the Architecture - M-profile
        link: https://www.arm.com/architecture/learn-the-architecture/m-profile
        type: documentation
    - resource:
        title: Learn the Architecture - M-profile - Open source examples
        link: https://github.com/ARM-software/m-profile-user-guide-examples
        type: Open-source example projects

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
