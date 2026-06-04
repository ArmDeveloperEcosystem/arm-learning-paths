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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:45:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6c81f3c9595df1128ca6f4f89446f093826d2242fa789ffa2d37465854be1f8e
  summary_generated_at: '2026-06-01T21:55:22Z'
  summary_source_hash: 6c81f3c9595df1128ca6f4f89446f093826d2242fa789ffa2d37465854be1f8e
  faq_generated_at: '2026-06-02T22:45:23Z'
  faq_source_hash: 6c81f3c9595df1128ca6f4f89446f093826d2242fa789ffa2d37465854be1f8e
  summary: >-
    This introductory path shows how to set up Keil MDK with Arm Compiler for Embedded on Windows
    and run a bare-metal TrustZone hello world on the NXP LPCXpresso55S69. You will obtain the
    example using the Keil µVision Pack Installer, which provides two sub-projects (hello_ns and
    hello_s) representing the non-secure and secure worlds. You will build, run, and start a debug
    session to examine TrustZone behavior, including security state switching and how non-secure
    code calls secure functions. Prerequisites include familiarity with C programming on microcontrollers,
    comfort with Windows, and access to an LPCXpresso55S69 board. The path is designed to be completed
    in about 20 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Install Keil MDK and Arm Compiler for Embedded on a Windows machine and connect an NXP LPCXpresso55S69
      board. You should also be comfortable with C programming on microcontrollers and using Windows.
  - question: How do I obtain the TrustZone hello world example in Keil μVision?
    answer: >-
      Open the Pack Installer, select the LPC55S69 device, and copy the hello_ns and hello_s examples
      into your workspace. These provide the non-secure and secure sub-projects used in the tutorial.
  - question: Which project should I open to build and run the example?
    answer: >-
      From μVision, choose Project -> Open Project and select the hello_world_s example. This
      example uses the hello_s (secure) and hello_ns (non-secure) sub-projects.
  - question: What result should I expect when starting a debug session?
    answer: >-
      At reset, the secure startup code runs, and the program counter will be at the start of
      main() in hello_world_s.c. You can then run or step through the code as directed.
  - question: How do I explore security state switching and secure function calls?
    answer: >-
      Start another debug session and step through the example as described in the path to observe
      transitions between secure and non-secure states and how secure functions are invoked from
      the non-secure world.
# END generated_summary_faq

author: Pareena Verma

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

