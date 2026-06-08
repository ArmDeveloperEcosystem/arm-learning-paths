---
title: "Start Debugging with µVision"
# Should start with a verb, have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: Learn how to debug microcontrollers using µVision with basic run/stop debug, advanced techniques using Event Recorder and Serial Wire Viewer, ETM Trace for performance analysis, and power measurement with ULINKplus.

minutes_to_complete: 90
# Always measured in minutes. Should be an integer, to complete the learning path (not read it).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:47:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 27ced3e9f69dbe51e75dcf13999ae1745a994137f31c86d6f17d4de341c7fa2a
  summary_generated_at: '2026-06-01T21:56:36Z'
  summary_source_hash: 27ced3e9f69dbe51e75dcf13999ae1745a994137f31c86d6f17d4de341c7fa2a
  faq_generated_at: '2026-06-02T22:47:15Z'
  faq_source_hash: 27ced3e9f69dbe51e75dcf13999ae1745a994137f31c86d6f17d4de341c7fa2a
  summary: >-
    This advanced Learning Path guides you through debugging Cortex-M software in Arm Keil µVision
    using a Blinky example on the Corstone-300 Ecosystem FVP. You will build the project, start
    a debug session, and use run/stop with hardware breakpoints. It then introduces Event Recorder,
    including printf to the Debug (printf) Viewer, and Serial Wire Viewer for real-time data (note:
    SWV is not supported in simulation). You will also explore ETM instruction trace on Armv7-M/Armv8-M
    devices for execution profiling and code coverage analysis, and measure power with ULINKplus
    using Event Statistics. Prerequisites include familiarity with embedded programming, a Windows
    machine, an Arm Account, Keil MDK with an active MDK-Community license, and the Corstone-300
    Ecosystem FVP.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm Account, a Windows machine, Arm Keil MDK with an active MDK-Community license,
      and the Corstone-300 Ecosystem FVP installed. Some familiarity with embedded programming
      is assumed. Clone or download the Blinky example project and open Blinky.Debug+AVH.uvprojx
      in µVision.
  - question: How can I print debug text without a UART?
    answer: >-
      Use the Event Recorder’s printf utility and view output in the Debug (printf) Viewer window.
      Event Recorder uses CoreSight DAP for data output and requires some system RAM.
  - question: What should I check if Serial Wire Viewer (SWV) shows no data?
    answer: >-
      SWV is not supported in simulation mode. Connect a debug adapter to real target hardware
      before using SWV.
  - question: When should I enable ETM Trace, and what results should I expect?
    answer: >-
      Enable ETM Trace on Armv7-M/Armv8-M devices that include ETM to capture instruction trace.
      In µVision, you can review historical execution sequences, perform execution profiling and
      performance analysis, and generate code coverage. It also helps diagnose issues like pointer
      problems and illegal instructions or data aborts.
  - question: How do I measure power with ULINKplus and configure it?
    answer: >-
      Use an Arm Keil ULINKplus to add serial-wire debug, CPU core clock measurement, and power
      measurement to your session. You can create power profiles with Event Statistics and configure
      ULINKplus using an initialization file (debug script) that runs when debug mode starts.
# END generated_summary_faq

author: Christopher Seidl

who_is_this_for: >
    This is an advanced topic for software developers who want to debug microcontrollers using µVision.
# One sentence that should indicate exactly who the target audience is (developers in X industries using Y tools/software for Z use-case).

learning_objectives: 
    - Use basic run/stop debug
    - Learn advanced debug techniques using Event Recorder and Serial Wire Viewer
    - Learn to use ETM Trace for optimum performance
    - Measure your power consumption with ULINKplus
# 2-5 bullet points, one sentence each. Should start with a verb (Deploy, Measure) and indicate the value of the objective if possible.

prerequisites:
    - Some familiarity with embedded programming is assumed
    - An [Arm Account](https://developer.arm.com/register) is required
    - A Windows machine
    - Installation of [Arm Keil MDK](/install-guides/mdk/) with an active MDK-Community license
    - Installation of the [Corstone-300 Ecosystem FVP](/install-guides/fm_fvp/eco_fvp/)
# List any prereqs needed before this learning path can be completed. Can include:
    # Online service accounts                                   (An Amazon Web Services account)
    # Prior knowledge                                           (Some familiarity with embedded programming)
    # Previous learning paths                                   (The Learning Path: Getting Started with Arm Virtual Hardware)
    # Particular tools/environments already being initialized   (An EC2 instance with AVH installed)


##### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-M
operatingsystems:
    - RTOS
    - Baremetal
tools_software_languages:
    - Keil MDK
    - FVP



further_reading:
    - resource:
        title: Keil MDK
        link: https://developer.arm.com/Tools%20and%20Software/Keil%20MDK
        type: website
    - resource:
        title: µVision User's guide
        link: https://developer.arm.com/documentation/101407/latest
        type: documentation
    - resource:
        title: ULINKplus User's guide
        link: https://developer.arm.com/documentation/101636/latest
        type: documentation
    - resource:
        title: Arm CoreSight basics for Keil tools
        link: https://developer.arm.com/documentation/kan339/latest
        type: documentation
    - resource:
        title: List of supported boards
        link: https://keil.arm.com/boards
        type: website


# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---

