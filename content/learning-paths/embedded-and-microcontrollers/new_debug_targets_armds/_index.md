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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:12:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c4d4ba17dc9308f8a35e5cc8490ce2c385d3a850c5468689d1bc02c2bd91db7d
  summary_generated_at: '2026-08-12T20:12:33Z'
  summary_source_hash: c4d4ba17dc9308f8a35e5cc8490ce2c385d3a850c5468689d1bc02c2bd91db7d
  faq_generated_at: '2026-08-12T20:12:33Z'
  faq_source_hash: c4d4ba17dc9308f8a35e5cc8490ce2c385d3a850c5468689d1bc02c2bd91db7d
  summary: >-
    You'll add virtual and hardware debug targets in Arm Development Studio. You'll configure a
    connection to an Arm Fast Models platform, then create a board target using an Arm DSTREAM
    probe. You'll choose a DSTREAM model based on trace needs, select USB or Ethernet transport,
    define connection details, and verify both debug configurations.
  faqs:
  - question: Which DSTREAM probe should I select for my board connection?
    answer: >-
      DSTREAM-ST provides full debug over JTAG and SWD and supports on-chip plus low bandwidth
      (4-bit) external trace. Choose another DSTREAM family member if you require higher bandwidth
      trace and your SoC and platform support it.
  - question: Should I connect the DSTREAM probe over USB or Ethernet?
    answer: >-
      Both transports are supported. Use the one available in your setup and ensure the Development
      Studio configuration matches how the probe is physically connected.
  - question: What should I verify before creating a Fast Models debug connection?
    answer: >-
      Confirm that Arm Fast Models and Arm Development Studio are installed. Ensure the appropriate
      virtual platform is available and gather the connection details required by your configuration.
  - question: How do I know the debugger is connected to an Arm Fast Models virtual platform?
    answer: >-
      A successful connection lets Development Studio interact with the platform as if it were
      real hardware. If the connection fails, review the virtual platform details entered in the
      debug configuration.
  - question: 'Which debug interface should I use for the DSTREAM connection: JTAG or SWD?'
    answer: >-
      DSTREAM supports both JTAG and Serial Wire Debug. Use the interface provided by your target
      SoC and board.
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
