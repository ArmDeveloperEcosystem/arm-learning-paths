---
title: Add new debug targets to Arm Development Studio

description: Learn how to create debug configurations for virtual platforms and development boards in Arm Development Studio, including setting up connections for Fast Models and DSTREAM debug probes.

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for embedded software developers new to Arm Development Studio.

learning_objectives: 
    - Create a debug configuration for a virtual platform
    - Create a debug configuration for a development board

prerequisites:
    - Some familiarity with embedded debug

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:35:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d2c403c7fd1001dbd985697c9eb018951a955358c2be39c727183a87a3dfdf51
  summary_generated_at: '2026-06-01T21:47:16Z'
  summary_source_hash: d2c403c7fd1001dbd985697c9eb018951a955358c2be39c727183a87a3dfdf51
  faq_generated_at: '2026-06-02T22:35:33Z'
  faq_source_hash: d2c403c7fd1001dbd985697c9eb018951a955358c2be39c727183a87a3dfdf51
  summary: >-
    This introductory Learning Path shows how to add new debug targets in Arm Development Studio
    for both virtual platforms and physical development boards. You will create debugger connections
    to Arm Fast Models for bare-metal software bring-up and to boards via the Arm DSTREAM family
    of probes. The steps outline when to use each DSTREAM variant and how to connect over USB
    or Ethernet, so you can attach the debugger to Cortex-A, Cortex-R, Cortex-M, or Neoverse based
    systems. It assumes Arm Development Studio and Arm Fast Models are installed and that you
    have some familiarity with embedded debug. After completing the path, you will have working
    debug configurations for your chosen target.
  faqs:
  - question: What do I need installed before creating a Fast Models debug connection in Arm Development
      Studio?
    answer: >-
      It is assumed that Arm Development Studio and Arm Fast Models are installed, and that you
      have some familiarity with embedded debug. Installation steps are not covered in this path.
  - question: Do I need a physical development board to follow this path?
    answer: >-
      Not for the virtual platform step; Fast Models let you connect the debugger to a model as
      if it were real hardware. For the hardware step, you will use an Arm DSTREAM probe with
      a development board.
  - question: Which DSTREAM probe should I choose for my board?
    answer: >-
      DSTREAM-ST provides full debug over JTAG and SWD, plus on-chip and low-bandwidth (4-bit)
      external trace. If you require higher-bandwidth trace and your SoC and platform support
      it, select DSTREAM-PT, DSTREAM-HT, or DSTREAM-XT.
  - question: Should I connect DSTREAM to my host over USB or Ethernet?
    answer: >-
      The DSTREAM family supports both high-speed USB and Ethernet connections to the host. Use
      whichever is available and appropriate for your setup.
  - question: What result should I expect after creating each debug configuration?
    answer: >-
      For Fast Models, the Arm Development Studio debugger should attach to the virtual platform
      and let you interact with it like real hardware. For a development board, the debugger should
      connect through DSTREAM and provide debug (and trace, where supported) according to the
      probe and target capabilities.
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

