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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:58:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3ddb97eb97a4c7ede7951410086198ee793a9d452a79b607f211873971bd375d
  summary_generated_at: '2026-06-01T21:25:21Z'
  summary_source_hash: 3ddb97eb97a4c7ede7951410086198ee793a9d452a79b607f211873971bd375d
  faq_generated_at: '2026-06-02T21:58:43Z'
  faq_source_hash: 3ddb97eb97a4c7ede7951410086198ee793a9d452a79b607f211873971bd375d
  summary: >-
    Build a motion-detection device on a Raspberry Pi Pico (RP2040 Cortex‑M0+) using the Arduino
    IDE on baremetal. This introductory Learning Path explains the differences between application
    and embedded stacks, then walks you through writing a simple embedded application, adding
    hardware interrupt handlers for a PIR motion sensor, and running it on the Pico with a piezo‑electric
    buzzer to signal motion. You will practice interrupt-driven programming on Arm Cortex‑M and
    deploy to real hardware in about 60 minutes. Prerequisites: Arduino IDE with the RP2040 board
    support package installed, a Raspberry Pi Pico, a PIR sensor, and a piezo‑electric buzzer.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Install the Arduino IDE with the RP2040 board support package and have a Raspberry Pi Pico,
      a PIR sensor, and a piezo-electric buzzer. No other prerequisites are explicitly listed.
  - question: How do I know the Arduino IDE is ready for RP2040 development?
    answer: >-
      Verify that the RP2040 board support package is installed so you can build and upload for
      the Raspberry Pi Pico. The Learning Path assumes you are using Arduino IDE configured for
      RP2040.
  - question: Is an RTOS used, or is this bare-metal Arduino on RP2040?
    answer: >-
      This project runs on baremetal and uses hardware interrupts. The Learning Path also explains
      how embedded stacks and RTOS-based designs differ from traditional application stacks.
  - question: What result should I expect when I run the program on the Pico?
    answer: >-
      A simple motion-detection device: when the PIR sensor detects movement, the application
      responds via an interrupt and signals using the piezo-electric buzzer. You will run this
      on the Raspberry Pi Pico.
  - question: What should I check if the buzzer doesn’t sound when motion is detected?
    answer: >-
      Confirm you can program the Raspberry Pi Pico from the Arduino IDE and that the PIR sensor
      and buzzer are correctly connected for the GPIOs used in your program. Also check that your
      interrupt handler is attached to the PIR input as described in the steps.
# END generated_summary_faq

author: Michael Hall

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

