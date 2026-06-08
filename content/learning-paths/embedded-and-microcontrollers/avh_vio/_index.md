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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:06:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aaff31b8917320c53825f3e7410b703bc7c7e273b1963fd80727b6b874f50566
  summary_generated_at: '2026-06-01T21:28:41Z'
  summary_source_hash: aaff31b8917320c53825f3e7410b703bc7c7e273b1963fd80727b6b874f50566
  faq_generated_at: '2026-06-02T22:06:31Z'
  faq_source_hash: aaff31b8917320c53825f3e7410b703bc7c7e273b1963fd80727b6b874f50566
  summary: >-
    This introductory Learning Path guides you to create and integrate a virtual LED peripheral
    using the Virtual IO (VIO) interface in Arm Virtual Hardware (AVH) to simulate real-world
    peripherals. You will work in an AWS environment by launching the AVH Amazon Machine Image
    (AMI), install the Tkinter Python package, and use an example project that demonstrates connecting
    a virtual LED to a bare-metal application. The steps focus on using AVH virtual interfaces
    and navigating the provided leds_example project. Intended for developers new to AVH and relevant
    to Cortex-M and Corstone use cases, prerequisites include a valid AWS account and some familiarity
    with Python; no other requirements are explicitly listed. Estimated completion time is about
    20 minutes.
  faqs:
  - question: What do I need before running the example?
    answer: >-
      You need a valid AWS account and some familiarity with Python. No other prerequisites are
      explicitly listed.
  - question: How do I launch the environment used in this Learning Path?
    answer: >-
      Launch the Arm Virtual Hardware AMI in your AWS account. For full instructions, refer to
      the Arm Virtual Hardware install guide.
  - question: How do I install the Tkinter dependency in the AVH instance?
    answer: >-
      In the AVH terminal, install it with: sudo apt install -y python3-tk. This provides the
      Tkinter Python interface to Tcl/Tk used by the example.
  - question: How do I obtain the example project files?
    answer: >-
      In your AVH terminal, clone the example project repository and navigate into the leds_example
      directory. The steps guide you through cloning and changing to the correct directory.
  - question: Do I need physical hardware to test the LED peripheral?
    answer: >-
      No. The example uses AVH Virtual Interfaces, specifically the Virtual IO (VIO) interface,
      to simulate a real-world LED peripheral.
# END generated_summary_faq

author: Pareena Verma

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

