---
title: Embedded programming with Arduino on the Raspberry Pi Pico

who_is_this_for: This is an introductory topic for software developers interested in embedded programming.
minutes_to_complete: 60

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

author_primary: Michael Hall

### Tags
skilllevels: Introductory
subjects: RTOS Fundamentals
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arduino

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
