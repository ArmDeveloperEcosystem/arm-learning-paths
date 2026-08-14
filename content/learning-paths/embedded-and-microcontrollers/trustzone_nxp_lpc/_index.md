---
title: Get started with TrustZone on NXP LPCXpresso55S69

description: Learn how to install Keil MDK Tools, run a TrustZone hello world example on the NXP LPCXpresso55S69 board, and understand security state switching and secure function calls.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers new to using TrustZone.

learning_objectives: 
    - Install the Keil MDK Tools
    - Run a hello world TrustZone example
    - Understand switching of security states
    - Learn how secure functions are called from a non-secure state

prerequisites:
    - Familiar with C programming on microcontrollers
    - Comfortable with Windows 
    - NXP LPCXpresso55S69 board

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:54:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c4c8c631983a74de0ae8013a12880eea9ad113d000eccde6194ed3370dccb616
  summary_generated_at: '2026-08-13T18:54:46Z'
  summary_source_hash: c4c8c631983a74de0ae8013a12880eea9ad113d000eccde6194ed3370dccb616
  faq_generated_at: '2026-08-13T18:54:46Z'
  faq_source_hash: c4c8c631983a74de0ae8013a12880eea9ad113d000eccde6194ed3370dccb616
  summary: >-
    You'll run and debug a TrustZone hello-world example on an NXP LPCXpresso55S69. First, you'll
    install Keil MDK and Arm Compiler for Embedded, then retrieve the example through the µVision
    Pack Installer. Next, you'll add the secure and non-secure projects to a workspace, build and
    run them, and use debugging to observe security-state transitions and secure-function calls.
  faqs:
  - question: What do I need before building and running the example on hardware?
    answer: >-
      Install Keil MDK and Arm Compiler for Embedded on a Windows machine, and connect the NXP
      LPCXpresso55S69 board.
  - question: How do I get the TrustZone hello world example into µVision?
    answer: >-
      Use the Pack installer widget to select the LPC55S69 device and copy the `hello_ns` and `hello_s` examples
      into your workspace. 
  - question: Which project should I open to start building and debugging?
    answer: >-
      In the IDE, choose **Project -> Open Project** and select the **hello_world_s** example. This secure
      project is the starting point for the build and debug flow.
  - question: Do I need both the secure and non-secure sub-projects in my workspace?
    answer: >-
      Yes. The TrustZone example consists of `hello_s` (secure) and `hello_ns` (non-secure), and both
      should be present in your workspace.
  - question: How do I explore security state switching and secure function calls during debug?
    answer: >-
      Start a debug session and step through execution instead of running to completion. The program
      counter begins at `main()` in `hello_world_s.c`, and the secure startup code has already executed
      at reset.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Security 
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - TrustZone
    - Arm Compiler for Embedded
    - Keil MDK

further_reading:
    - resource:
        title: Secure software guidelines for Armv8-M
        link: https://developer.arm.com/documentation/100720/0100
        type: documentation
    - resource:
        title: Using LPC55S69 SDK TrustZone examples with MCUXpresso IDE
        link: https://community.nxp.com/t5/Blogs/Using-LPC55S69-SDK-TrustZone-examples-with-MCUXpresso-IDE-v11-0/ba-p/1131075
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
