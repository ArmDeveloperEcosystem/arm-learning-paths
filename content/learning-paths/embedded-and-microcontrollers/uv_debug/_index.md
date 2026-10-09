---
title: "Start debugging with µVision"
# Should start with a verb, have no adjectives (amazing, cool, etc.), and be as concise as possible.

description: Learn how to debug microcontrollers using µVision with basic run/stop debug, advanced techniques using Event Recorder and Serial Wire Viewer, ETM Trace for performance analysis, and power measurement with ULINKplus.

minutes_to_complete: 90
# Always measured in minutes. Should be an integer, to complete the learning path (not read it).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:56:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 823db286c98eb076a977912629db4e50b80108ba3542ebec1b985e5b1ccab465
  summary_generated_at: '2026-08-13T18:56:18Z'
  summary_source_hash: 823db286c98eb076a977912629db4e50b80108ba3542ebec1b985e5b1ccab465
  faq_generated_at: '2026-08-13T18:56:18Z'
  faq_source_hash: 823db286c98eb076a977912629db4e50b80108ba3542ebec1b985e5b1ccab465
  summary: >-
    You'll debug a Cortex-M Blinky application in µVision. First, you'll build the project, start a
    debug session, and use hardware breakpoints. Then, you'll use Event Recorder, Serial Wire Viewer (SWV),
    and Embedded Trace Macrocell (ETM) to inspect events, real-time data, execution history, and faults. Finally, you'll
    use ULINKplus to measure core clock, power, and code-section performance.
  faqs:
  - question: How do I know the Blinky project built correctly before I start debugging?
    answer: >-
      Select **Build (F7)** and verify it completes without errors. When the build succeeds, select
      **Start a Debug Session (Ctrl+F5)** and **Run (F5)** the application.
  - question: What should I check if I don't see any SWV data?
    answer: >-
      SWV isn't supported in simulation mode. Connect a debug adapter to real target hardware
      and use SWV there.
  - question: Where do Event Recorder printf messages appear, and what does my project need?
    answer: >-
      Event Recorder text appears in the **Debug (`printf`) Viewer** window. Your code must call the
      Event Recorder API or use components already annotated (such as MDK‑Middleware, Keil RTX5,
      or CMSIS‑FreeRTOS). Event Recorder requires some system RAM.
  - question: How do I limit ETM trace capture to a specific code region?
    answer: >-
      In the **Disassembly** window or C source, add a **TraceRun (ETM)** tracepoint where capture
      should start and a **TraceSuspend (ETM)** tracepoint where it should stop. µVision records
      instructions, branches, exceptions, and interrupts between those tracepoints.
  - question: How do I configure ULINKplus to capture power measurements?
    answer: >-
      ULINKplus adds core clock measurement and power measurement that you can use with Event
      **Event Statistics** to profile code sections. Configure the adapter with a debug initialization script
      that runs when debug mode starts. For board connections, refer to the ULINKplus documentation.
# END generated_summary_faq

author: Christopher Seidl

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
