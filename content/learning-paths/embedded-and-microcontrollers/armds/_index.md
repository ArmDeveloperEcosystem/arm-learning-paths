---
title: Get started with Arm Development Studio

minutes_to_complete: 30   
description: Learn how to import and build example projects in Arm Development Studio and debug embedded applications using Fixed Virtual Platforms (FVPs) or hardware with DSTREAM debug probes.

who_is_this_for: This is an introductory topic for embedded software developers new to Arm Development Studio.

learning_objectives: 
    - Import and build an example project
    - Debug the example code running on a Fixed Virtual Platform (FVP)
    - Debug the example code running on a board with a DSTREAM debug probe

prerequisites:
    - Some familiarity with embedded programming is assumed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:20:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0103f51d42c230dbe75ff5b78ac15a33dfd2f2c0f4906fb665a8dd681512d2e1
  summary_generated_at: '2026-07-08T15:20:26Z'
  summary_source_hash: 0103f51d42c230dbe75ff5b78ac15a33dfd2f2c0f4906fb665a8dd681512d2e1
  faq_generated_at: '2026-07-08T15:20:26Z'
  faq_source_hash: 0103f51d42c230dbe75ff5b78ac15a33dfd2f2c0f4906fb665a8dd681512d2e1
  summary: >-
    You'll launch Arm Development Studio, import and
    build a supplied example, and debug it on a Cortex-M Fixed Virtual Platform (FVP) or
    on hardware via a DSTREAM probe. Using the ready-to-use `startup_Cortex-M3_AC6_FVP.launch` configuration,
    you'll inspect the debug settings and start a session that runs without target hardware
    on an MPS2+-based Cortex-M3 (AN385) model. You'll also see where to adjust the project
    to use a different Arm Compiler for Embedded version when required. By the end, you'll
    build and execute under the IDE with a working debug connection on either an FVP or a supported
    board.
  faqs:
  - question: How do I launch Arm Development Studio from the command line?
    answer: >-
      Run `armds_ide` from a terminal to open the IDE.
  - question: What should I do when the workspace configuration pane appears?
    answer: >-
      Click **Finish** to accept the default setup. The workspace is the base directory where the
      IDE stores your projects and build output.
  - question: Do I need target hardware to run the example?
    answer: >-
      No. Use the provided Fixed Virtual Platforms to execute and debug the example without hardware.
      If hardware is available, you can run it on a board using a DSTREAM debug probe.
  - question: Where is the FVP debug configuration for the example?
    answer: >-
      Open `startup_Cortex-M3_AC6_FVP.launch` in the project folder. Double-click the file to inspect
      the predefined settings before starting a debug session.
  - question: How do I select a different Arm Compiler for Embedded version for the project?
    answer: >-
      Install the required compiler version using the Arm Compiler for Embedded install guide.
      Then open **Project > Properties** and change the compiler used by the project in the build
      settings.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Cortex-R
    - Cortex-M
    - Neoverse
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Development Studio
    - Arm Compiler for Embedded
    - Arm Fast Models
    - DSTREAM

further_reading:
    - resource:
        title: Arm Development Studio
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio
        type: website
    - resource:
        title: DSTREAM-ST
        link: https://developer.arm.com/Tools%20and%20Software/DSTREAM-ST
        type: website
    - resource:
        title: DSTREAM-PT
        link: https://developer.arm.com/Tools%20and%20Software/DSTREAM-PT
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
