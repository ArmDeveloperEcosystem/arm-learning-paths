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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:29:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f989929b11c48df42c2701dc71516cec0b8637b4c639c3dbbf6ac5e7440c8a56
  summary_generated_at: '2026-07-08T15:29:26Z'
  summary_source_hash: f989929b11c48df42c2701dc71516cec0b8637b4c639c3dbbf6ac5e7440c8a56
  faq_generated_at: '2026-07-08T15:29:26Z'
  faq_source_hash: f989929b11c48df42c2701dc71516cec0b8637b4c639c3dbbf6ac5e7440c8a56
  summary: >-
    You'll enable and use Keil MDK code coverage on a Cortex-M Fixed
    Virtual Platform (FVP). First, you'll import and build the CMSIS-RTOS2 Blinky example for the `ARMCM3`
    device using **Pack Installer**. Then, you'll configure μVision debug to execute the application on the
    supplied Cortex-M FVP. After running the program, you'll review the coverage results to see which
    lines and branches executed and identify untested paths, such as incomplete `switch` cases.
    You'll focus on running with FVPs and learn how to interpret the basic
    code coverage report and decide what tests to add next.
  faqs:
  - question: Which device and example should I select in Pack Installer?
    answer: >-
      Choose **ARM > ARM Cortex M3 > ARMCM3**, then on the **Examples** tab copy the CMSIS-RTOS2 Blinky
      (uVision Simulator) example. Open the copied project in MDK and build it.
  - question: How do I confirm the project is ready before running coverage?
    answer: >-
      Build the project and check that it completes without errors and produces an image. Ensure
      it runs on the selected target without immediate faults.
  - question: How do I make sure the application runs on the FVP rather than the default simulator
      or a board?
    answer: >-
      In the project’s debug settings, select the supplied Cortex-M FVP as the execution target.
      This Learning Path uses FVPs instead of real hardware.
  - question: What should I look for in the code coverage report?
    answer: >-
      Look for highlighted executed and unexecuted lines or branches. Verify that intended paths,
      such as all cases in a C switch statement, were exercised.
  - question: Can I use real hardware instead of an FVP for code coverage?
    answer: >-
      Yes, MDK supports code coverage on real hardware using instruction trace (ETM trace). You'll use FVPs in this
      Learning Path. If you're configuring hardware trace, follow MDK guidance.
# END generated_summary_faq

author: Ronan Synnott

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
