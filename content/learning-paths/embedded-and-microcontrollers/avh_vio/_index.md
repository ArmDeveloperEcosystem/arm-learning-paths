---
title: Implement an example Virtual Peripheral with Arm Virtual Hardware

description: Learn how to create and integrate a virtual LED peripheral using the Virtual IO interface of Arm Virtual Hardware to simulate real-world peripherals.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers new to Arm Virtual Hardware and its features.

learning_objectives: 
    - Create and integrate an LED peripheral with the Virtual IO (VIO) interface of AVH.

prerequisites:
    - A valid [AWS](https://aws.amazon.com/) account
    - Some familiarity with Python

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:24:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aaff31b8917320c53825f3e7410b703bc7c7e273b1963fd80727b6b874f50566
  summary_generated_at: '2026-07-08T15:24:18Z'
  summary_source_hash: aaff31b8917320c53825f3e7410b703bc7c7e273b1963fd80727b6b874f50566
  faq_generated_at: '2026-07-08T15:24:18Z'
  faq_source_hash: aaff31b8917320c53825f3e7410b703bc7c7e273b1963fd80727b6b874f50566
  summary: >-
    You'll implement a simple virtual LED peripheral and connect it to
    Arm Virtual Hardware using the Virtual Input/Output (VIO) interface. First, you'll start an Arm
    Virtual Hardware Amazon Machine Image (AMI) in AWS, install the Tkinter package for Python
    in the AVH terminal, and clone the example project. You'll focus on wiring the virtual
    peripheral to VIO and running the example in the `leds_example` directory to observe the interaction
    between the simulated device and the application. By the end, you'll recognize how VIO routes
    peripheral I/O between AVH and a small Python UI to emulate real-world stimuli.
  faqs:
  - question: Which AVH interface should I use to connect the LED example?
    answer: >-
      You'll use the Virtual Input/Output (VIO) interface provided by Arm Virtual Hardware to connect
      the example peripheral.
  - question: What do I need to install to run the example’s Python UI?
    answer: >-
      Install the Tkinter package for Python in the AVH terminal with: `sudo apt install -y
      python3-tk`.
  - question: Where is the LED example located after I clone the repository?
    answer: >-
      After cloning, navigate into the `leds_example` directory to work with the sample.
  - question: I haven’t launched Arm Virtual Hardware yet — what should I do first?
    answer: >-
      Start the Arm Virtual Hardware AMI in an AWS account and follow the Arm Virtual Hardware
      install guide to reach the AVH terminal.
  - question: How do I know the environment is ready before running the example?
    answer: >-
      Verify that `python3-tk` installs without errors and that the repository is cloned, with
      the current directory set to `leds_example`.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Virtual Hardware
armips:
    - Cortex-M
    - Corstone
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Virtual Hardware

further_reading:
    - resource:
        title: AVH Virtual Interfaces
        link: https://arm-software.github.io/AVH/main/simulation/html/group__arm__cmvp.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

