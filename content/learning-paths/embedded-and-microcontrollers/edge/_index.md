---
title: Learn how to run AI on Edge devices using Arduino Nano RP2040

description: Learn how to collect and preprocess audio data using Edge Impulse, train an audio classification model, and deploy it to the Arduino Nano RP2040 to control LEDs based on voice commands.

minutes_to_complete: 90

who_is_this_for: This Learning Path is for beginners in Edge AI and TinyML, including developers, engineers, hobbyists, AI/ML enthusiasts, and researchers working with embedded AI and IoT.

learning_objectives:
  - Understand the basics of Edge AI and TinyML.
  - Collect and preprocess audio data using Edge Impulse.
  - Train and deploy an audio classification model on the Arduino Nano RP2040.
  - Control LEDs by turning them on and off based on model predictions.

prerequisites:
  - Completion of [Embedded programming with Arduino on the Raspberry Pi Pico](/learning-paths/embedded-and-microcontrollers/arduino-pico/) if you're an absolute beginner.
  - An [Edge Impulse Studio](https://studio.edgeimpulse.com/signup) account.
  - The [Arduino IDE](/install-guides/arduino-pico/) with the RP2040 board support package installed on your computer.
  - An [Arduino Nano RP2040 Connect board](https://store.arduino.cc/products/arduino-nano-rp2040-connect-with-headers).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:04:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5462e69e9e1289cb61815d66c308a94cfae0bbfa690aca19adf07290c6f24e9d
  summary_generated_at: '2026-08-12T20:04:39Z'
  summary_source_hash: 5462e69e9e1289cb61815d66c308a94cfae0bbfa690aca19adf07290c6f24e9d
  faq_generated_at: '2026-08-12T20:04:39Z'
  faq_source_hash: 5462e69e9e1289cb61815d66c308a94cfae0bbfa690aca19adf07290c6f24e9d
  summary: >-
    You'll move from Edge AI and TinyML concepts to a voice-command prototype on an Arduino Nano
    RP2040 Connect. First, you'll collect audio, train a classifier in Edge Impulse, and export its Arduino
    library. Then, you'll add the library to a sketch, flash the board, and validate on-device inference
    by speaking commands that control an LED.
  faqs:
  - question: Which Edge Impulse project type should I choose for voice commands?
    answer: >-
      Create an audio classification project in Edge Impulse. Define classes for the words you
      plan to recognize, such as “on” and “off,” and apply preprocessing before training.
  - question: What do I need to download from Edge Impulse for the Arduino sketch?
    answer: >-
      Download the Arduino library generated from your Edge Impulse project. Add this library
      to your sketch so the trained model and processing steps are available on the device.
  - question: Do I need an internet connection on the board while the model runs?
    answer: >-
      No. Inference runs locally on the device, which is a core principle of Edge AI. You
      need connectivity only when using Edge Impulse Studio to build and export the model.
  - question: What result should I expect after flashing the sketch?
    answer: >-
      The board performs real-time audio inference and controls an LED. When it recognizes the
      trained words “on” and “off,” the LED changes state.
  - question: The LED does not change when I say the command—what should I check?
    answer: >-
      Verify that the correct Edge Impulse library is included, the build succeeds, and the uploaded
      firmware matches your project. Confirm the labels used in the sketch match the classes you
      trained, then rebuild and reflash.
# END generated_summary_faq

author: Bright Edudzi Gershon Kordorwu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
tools_software_languages:
    - Edge Impulse
    - tinyML
    - Edge AI
    - Arduino
operatingsystems:
    - Baremetal

further_reading:
    - resource:
        title: TinyML brings AI to smallest Arm devices
        link: https://newsroom.arm.com/blog/tinyml
        type: blog
    - resource:
        title: What is Edge AI?
        link: https://docs.edgeimpulse.com/nordic/concepts/edge-ai/what-is-edge-ai
        type: blog
    - resource:
        title: Edge Impulse for beginners
        link: https://docs.edgeimpulse.com/docs/readme/for-beginners
        type: doc

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
