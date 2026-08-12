---
title: Get Started with Keil Studio Cloud

description: Learn how to import, build, and debug your first Keil Studio Cloud project

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for embedded software developers new to Keil Studio Cloud.

learning_objectives: 
    - Import and build an example project
    - Run the example on Arm Virtual Hardware

prerequisites:
    - Some familiarity with embedded programming is assumed
    - An [Arm Account](https://developer.arm.com/register) is required

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:08:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6886b053c7235a267ce497bdf21ce08143e3aea8b8262ee27587a100252f1955
  summary_generated_at: '2026-08-12T20:08:53Z'
  summary_source_hash: 6886b053c7235a267ce497bdf21ce08143e3aea8b8262ee27587a100252f1955
  faq_generated_at: '2026-08-12T20:08:53Z'
  faq_source_hash: 6886b053c7235a267ce497bdf21ce08143e3aea8b8262ee27587a100252f1955
  summary: >-
    You'll use Keil Studio Cloud to build and debug a CMSIS-based example on Arm Virtual Hardware.
    You'll browse supported hardware, import a ready-to-build project, and compile it with Arm
    Compiler for Embedded. You'll select a virtual target, launch a run or debug session, and
    verify that the application executes without a physical board.
  faqs:
  - question: How do I sign in to Keil Studio Cloud?
    answer: >-
      Go to `keil.arm.com` and sign in with your Arm Account. If you already have an Mbed account,
      you can use it to access Keil Studio Cloud.
  - question: Which browser should I use if I want to connect my board over USB?
    answer: >-
      Use Google Chrome or Microsoft Edge (Chromium) because both browsers support the WebUSB standard.
      Other features work in the latest Chrome, Edge, Opera, Safari, and Firefox.
  - question: Do I need a physical board to run the example?
    answer: >-
      No. You run the example on Arm Virtual Hardware as part of the Learning Path.
  - question: How do I check whether my hardware is supported?
    answer: >-
      Open Keil Studio Cloud and select the **Hardware** menu to view the supported hardware.
      Verify your exact board appears before attempting to connect it.
  - question: What result should I expect after building the example project?
    answer: >-
      A successful build finishes without errors in the IDE. You can then run or debug the project
      on Arm Virtual Hardware as shown in the instructions.
# END generated_summary_faq

author: Christopher Seidl 

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Virtual Hardware
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
    - RTOS
tools_software_languages:
    - Arm Compiler for Embedded
    - Arm Virtual Hardware
    - CMSIS

further_reading:
    - resource:
        title: Keil Studio
        link: https://keil.arm.com
        type: website
    - resource:
        title: List of supported boards
        link: https://keil.arm.com/boards
        type: website
    - resource:
        title: Keil Studio documentation
        link: https://developer.arm.com/documentation/102497/latest/Arm-Keil-Studio
        type: website
    - resource:
        title: Which Keil tool should I care about?
        link: https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/which-keil-tool-should-i-care-about
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
