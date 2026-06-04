---
title: Get started with Keil MDK Code Coverage

description: Learn how to set up and use code coverage in Keil MDK with FVPs to verify that your embedded application tests execute all code paths.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for embedded software developers new to the code-coverage feature in Keil MDK.

learning_objectives: 
    - Set up project execution on FVP
    - Understand basics of the Code Coverage report

prerequisites:
    - Basic familiarity with Keil MDK

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:15:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f989929b11c48df42c2701dc71516cec0b8637b4c639c3dbbf6ac5e7440c8a56
  summary_generated_at: '2026-06-01T21:31:57Z'
  summary_source_hash: f989929b11c48df42c2701dc71516cec0b8637b4c639c3dbbf6ac5e7440c8a56
  faq_generated_at: '2026-06-02T22:15:46Z'
  faq_source_hash: f989929b11c48df42c2701dc71516cec0b8637b4c639c3dbbf6ac5e7440c8a56
  summary: >-
    Learn to configure and run code coverage in Keil MDK using Fixed Virtual Platforms (FVPs)
    for Cortex-M targets. You will import and build the CMSIS-RTOS2 Blinky (uVision Simulator)
    example for ARMCM3 from the Pack Installer, set up debugging on the supplied Cortex-M FVP,
    execute the application, and view the Code Coverage report to see which code paths your tests
    exercise, such as all cases of a C switch statement. This introductory path assumes basic
    familiarity with Keil MDK and takes about 15 minutes. By the end, you can run a project on
    an FVP and understand the basics of the coverage report.
  faqs:
  - question: Do I need real target hardware to follow this path?
    answer: >-
      No. While MDK can perform code coverage with FVPs or real hardware, this Learning Path uses
      the supplied Cortex-M FVP, so you can complete it without hardware.
  - question: What do I need before I start?
    answer: >-
      You must have Keil MDK installed, and basic familiarity with MDK is assumed. No other explicit
      prerequisites are listed.
  - question: Which device and example should I select in the Pack Installer?
    answer: >-
      In the Devices tree, select ARM > ARM Cortex M3 > ARMCM3. Then open the Examples tab and
      copy the CMSIS-RTOS2 Blinky (uVision Simulator) example, open it in MDK, and build.
  - question: Can I use a different project instead of the CMSIS-RTOS2 Blinky example?
    answer: >-
      Yes. You can perform code coverage on any project that runs on a suitable target, but this
      path uses a standard RTX example that runs on the supplied Cortex-M FVP.
  - question: What should I look for in the Code Coverage report?
    answer: >-
      The report highlights which areas of your code were executed by your tests. A common check
      is verifying that all cases in a C switch statement have been exercised.
# END generated_summary_faq

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: Performance and Architecture 
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
    - RTOS
tools_software_languages:
    - Keil MDK
    - FVP

further_reading:
    - resource:
        title: MDK Code Coverage overview
        link: https://www2.keil.com/mdk5/debug/coverage
        type: website
    - resource:
        title: ULINKpro Debug and Trace Unit
        link: https://www2.keil.com/mdk5/ulink/ulinkpro
        type: website
    - resource:
        title: Trace tutorial for Arm Cortex-M
        link: https://www.youtube.com/watch?v=XGmSCVgb6EM
        type: video


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

