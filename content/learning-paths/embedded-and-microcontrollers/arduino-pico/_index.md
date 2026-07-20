---
title: Embedded programming with Arduino on the Raspberry Pi Pico

who_is_this_for: This is an introductory topic for software developers interested in embedded programming.
minutes_to_complete: 60
description: Learn how to build a motion-detection device with Raspberry Pi Pico (RP2040 Cortex-M0+) using Arduino IDE, PIR sensors, and interrupt-driven programming on baremetal.

learning_objectives: 
    - Understand the basics of embedded programming
    - Know the differences between embedded and application development
    - Write a simple embedded application
    - Run your embedded application on a Raspberry Pi Pico
    - Understand how hardware interrupts are used in embedded systems to respond to external changes
    - Add interrupt handlers to an embedded application

prerequisites:
    - The [Arduino IDE with the RP2040 board support package](/install-guides/arduino-pico/) installed on your computer
    - A [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) board
    - A [PIR sensor](https://www.amazon.com/HiLetgo-HC-SR501-Infrared-Sensor-Arduino/dp/B07KZW86YR/ref=sr_1_3?keywords=pir+sensor&qid=1698432931&sr=8-3) for detecting motion
    - A [peizo-electric buzzer](https://www.amazon.com/mxuteuk-Electronic-Computers-Printers-Components/dp/B07VK1GJ9X/ref=sr_1_4?crid=2FAXYI17HZKDB&keywords=piezo+buzzer&qid=1698432968&sprefix=peizo%2Caps%2C148&sr=8-4) for signaling motion

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-08T15:19:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3ddb97eb97a4c7ede7951410086198ee793a9d452a79b607f211873971bd375d
  summary_generated_at: '2026-07-08T15:19:51Z'
  summary_source_hash: 3ddb97eb97a4c7ede7951410086198ee793a9d452a79b607f211873971bd375d
  faq_generated_at: '2026-07-08T15:19:51Z'
  faq_source_hash: 3ddb97eb97a4c7ede7951410086198ee793a9d452a79b607f211873971bd375d
  summary: >-
    You'll learn about embedded programming and build a motion detector with a Raspberry Pi Pico (RP2040, Cortex-M0+). First, you'll
    compare application and embedded software stacks, then apply those differences by wiring a
    passive infrared (PIR) sensor and a piezo buzzer to the Pico. Using the Arduino IDE, you'll
    write a simple sketch that configures GPIO, registers an interrupt handler, and reacts to
    external changes without polling. Finally, you'll deploy to bare metal on the Pico
    and validate that motion events trigger the buzzer immediately, demonstrating how hardware
    interrupts drive responsive behavior on a small Arm microcontroller.
  faqs:
  - question: Which board and port should I select in the Arduino IDE before uploading?
    answer: >-
      Select an RP2040-based board from the installed package and choose the USB/serial port associated
      with the Raspberry Pi Pico. If the upload fails, recheck both the board and port selections.
  - question: How should I wire the PIR sensor and buzzer to match the sketch?
    answer: >-
      Connect the PIR output to a digital input pin and the buzzer to a digital output pin with
      a common ground. Make sure the pin numbers in your wiring match the pin definitions used
      in the sketch.
  - question: How do I know the interrupt is working instead of polling?
    answer: >-
      When motion occurs, the buzzer responds immediately without waiting for a timed loop. If
      you see an instant reaction when the PIR output changes, the interrupt handler is being
      invoked.
  - question: What should I check if the buzzer never reacts to motion?
    answer: >-
      Verify power and common ground, confirm the selected GPIO pins match the sketch, and ensure
      the input is configured for the PIR signal and the output drives the buzzer. Also recheck
      that the correct RP2040 board and port are selected and that the upload completed successfully.
  - question: Does this project use an RTOS?
    answer: >-
      No. The example runs on bare metal using Arduino tooling on the RP2040. Any RTOS stack references
      are for context about typical Arm embedded architectures, not for this build.
# END generated_summary_faq

author: Michael Hall

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arduino

further_reading:
    - resource:
        title: Arduino-Pico
        link: https://arduino-pico.readthedocs.io/en/latest/index.html
        type: documentation
    - resource:
        title: Raspberry Pi Pico documentation
        link: https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

