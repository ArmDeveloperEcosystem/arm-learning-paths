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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:00:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0103f51d42c230dbe75ff5b78ac15a33dfd2f2c0f4906fb665a8dd681512d2e1
  summary_generated_at: '2026-06-01T21:25:49Z'
  summary_source_hash: 0103f51d42c230dbe75ff5b78ac15a33dfd2f2c0f4906fb665a8dd681512d2e1
  faq_generated_at: '2026-06-02T22:00:01Z'
  faq_source_hash: 0103f51d42c230dbe75ff5b78ac15a33dfd2f2c0f4906fb665a8dd681512d2e1
  summary: >-
    Learn how to get productive with Arm Development Studio by importing and building an example
    bare-metal project, then debugging it on a Fixed Virtual Platform (FVP) or on hardware using
    a DSTREAM debug probe. Starting from a working, licensed installation, you launch the IDE,
    open the workspace, and use the supplied Cortex-M3 FVP (a digital twin of the MPS2+ AN385
    platform) with a ready-to-use .launch configuration to step through the code without target
    hardware. The path also shows how to select a different Arm Compiler for Embedded version
    at the project level. Some familiarity with embedded programming is assumed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Have Arm Development Studio installed with a valid license configured. The path assumes
      some familiarity with embedded programming.
  - question: How do I launch the IDE and set up the workspace?
    answer: >-
      Start the IDE from your OS applications menu or run the armds_ide command. On first launch,
      accept the default workspace configuration by clicking Finish; the workspace is a base directory
      on your host.
  - question: Can I run the example without hardware, and which FVP does it target?
    answer: >-
      Yes. Arm Development Studio provides FVPs, and the supplied Cortex-M FVPs are digital twins
      of the MPS2+ platform programmed for Cortex-M3 (AN385). If you have hardware and a DSTREAM
      probe, you can choose to run on the board instead.
  - question: Where is the FVP debug configuration and how do I use it?
    answer: >-
      The project includes startup_Cortex-M3_AC6_FVP.launch in the project folder. Double-click
      it to inspect settings; it is a ready-to-use configuration to start an FVP debug session
      from the IDE.
  - question: How do I select a different Arm Compiler for Embedded version for my project?
    answer: >-
      Install the required compiler version using the Arm Compiler for Embedded install guide.
      Then open Project Properties and adjust the C/C++ Build settings to select the desired compiler
      version; Development Studio ships with the latest available at its release.
# END generated_summary_faq

author: Ronan Synnott

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

