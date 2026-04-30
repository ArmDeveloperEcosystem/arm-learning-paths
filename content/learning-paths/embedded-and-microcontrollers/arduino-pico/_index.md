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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:15Z'
  generator: template
  source_hash: 3ddb97eb97a4c7ede7951410086198ee793a9d452a79b607f211873971bd375d
  summary: >-
    Learn how to build a motion-detection device with Raspberry Pi Pico (RP2040 Cortex-M0+) using
    Arduino IDE, PIR sensors, and interrupt-driven programming on baremetal. It is designed for
    software developers interested in embedded programming. By the end, you will be able to understand
    the basics of embedded programming, know the differences between embedded and application
    development, and write a simple embedded application. It focuses on tools and technologies
    such as Arduino, Baremetal environments, and Arm platforms including Cortex-M. The main steps
    cover About Embedded Programming, Application Programming, Embedded Programming, Embedded
    Programming on Arm, and Build a smart device prototype.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand the basics of embedded programming, know the differences between embedded
      and application development, and write a simple embedded application. Learn how to build
      a motion-detection device with Raspberry Pi Pico (RP2040 Cortex-M0+) using Arduino IDE,
      PIR sensors, and interrupt-driven programming on baremetal.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers interested in embedded programming.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: The [Arduino IDE with the RP2040 board
      support package](/install-guides/arduino-pico/) installed on your computer; A [Raspberry
      Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) board; A [PIR sensor](https://www.amazon.com/HiLetgo-HC-SR501-Infrared-Sensor-Arduino/dp/B07KZW86YR/ref=sr_1_3?keywords=pir+sensor&qid=1698432931&sr=8-3)
      for detecting motion; A [peizo-electric buzzer](https://www.amazon.com/mxuteuk-Electronic-Computers-Printers-Components/dp/B07VK1GJ9X/ref=sr_1_4?crid=2FAXYI17HZKDB&keywords=piezo+buzzer&qid=1698432968&sprefix=peizo%2Caps%2C148&sr=8-4)
      for signaling motion.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Arduino, Baremetal environments, and Arm platforms
      such as Cortex-M.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around About Embedded Programming, Application Programming,
      Embedded Programming, Embedded Programming on Arm, and Build a smart device prototype.
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

