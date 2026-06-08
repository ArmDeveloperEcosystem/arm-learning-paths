---
title: Build and run Arm Total Solutions for IoT

description: Learn how to build examples from the Open-IoT-SDK and run them on Corstone-300 virtual hardware to understand complete IoT software stack construction.

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for embedded software developers interested in learning how a complete IoT software stack is constructed.

learning_objectives: 
    - Build examples from Open-IoT-SDK
    - Run the examples on Corstone-300 virtual hardware

prerequisites:
    - Some familiarity with embedded programming
    - An AWS account (required for Arm Virtual Hardware)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:25:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 11fc64eb1a0595b1d8e625e465be9fa87a4de04f59492004204ccbe61a92a5b7
  summary_generated_at: '2026-06-01T21:41:45Z'
  summary_source_hash: 11fc64eb1a0595b1d8e625e465be9fa87a4de04f59492004204ccbe61a92a5b7
  faq_generated_at: '2026-06-02T22:25:19Z'
  faq_source_hash: 11fc64eb1a0595b1d8e625e465be9fa87a4de04f59492004204ccbe61a92a5b7
  summary: >-
    This introductory path shows how to build Open-IoT-SDK examples and run them on Corstone-300
    virtual hardware using Arm Virtual Hardware. You set up an AVH instance, install the required
    Python environment, then build and run a keyword example to observe ML inference logs on a
    bare-metal or RTOS stack. The flow highlights how Arm Trusted Firmware-M and the Arm ML Evaluation
    Kit integrate within Arm Total Solutions for IoT, and how the keyword and speech examples
    can connect to AWS IoT. Tools listed include Arm Virtual Hardware, FVP, and Arm Compiler for
    Embedded. Prerequisites are some embedded programming familiarity and an AWS account (required
    for AVH). Estimated time is about 30 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      Some familiarity with embedded programming is expected, and you need an AWS account to use
      Arm Virtual Hardware. No other prerequisites are explicitly listed.
  - question: How do I set up Arm Virtual Hardware and install the required software?
    answer: >-
      Create and set up your AVH instance by following the Arm Virtual Hardware install guide.
      In the AVH instance, run: sudo apt update; sudo apt install python3.8-venv -y; sudo cp /usr/local/bin/pip3.8
      /usr/bin.
  - question: How do I build and run the keyword example?
    answer: >-
      From the project, run: ./ats.sh build-n-run keyword. The build takes a few minutes and runs
      on Corstone-300 virtual hardware within AVH.
  - question: What result should I expect in the terminal when the example runs successfully?
    answer: >-
      Look for logs such as "ML interface initialised" and inference output showing a label and
      score, for example: label: on, score: 0.996127; threshold: 0.700000. You may also see markers
      like ML_HEARD_O.
  - question: How is AWS connectivity used in the examples, and what should I configure?
    answer: >-
      The keyword and speech examples implement AWS cloud connectivity. You can create an AWS
      thing to send data from the simulated Corstone-300 device to AWS IoT cloud services.
# END generated_summary_faq

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
    - Corstone
operatingsystems:
    - Baremetal
    - RTOS
tools_software_languages:
    - Arm Virtual Hardware
    - FVP
    - Arm Compiler for Embedded


further_reading:
    - resource:
        title: Open-IoT-SDK
        link: https://github.com/ARM-software/open-iot-sdk
        type: website
    - resource:
        title: Arm Speech Recognition Total Solution example video, using the Arm Open IoT SDK, Corstone-310 and AVH
        link: https://devsummit.arm.com/flow/arm/devsummit22/sessions-catalog/page/sessions/session/16600464346670018mPQ
        type: website
    - resource:
        title: Learn more about the Corstone reference systems
        link: https://www.arm.com/products/silicon-ip-subsystems/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

