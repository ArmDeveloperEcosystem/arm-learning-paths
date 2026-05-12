---
title: Use Linux on the NXP FRDM i.MX 93 board

description: Learn how to boot and configure the NXP FRDM i.MX 93 Arm board with Linux, create a user with sudo access, connect to WiFi using ConnMan, and transfer files over the network.
    
minutes_to_complete: 120

who_is_this_for: This is an introductory topic for embedded developers and ML engineers who want to boot an NXP FRDM i.MX 93 board, connect over serial, enable WiFi, and transfer files for on-device development on Arm.

learning_objectives:
    - Boot the NXP FRDM i.MX 93 board and log in to Linux over a serial console.
    - Create a non-root Linux user with sudo access for development workflows.
    - Connect the board to WiFi using ConnMan.
    - Transfer files to the board over WiFi (scp) or USB.
    - Load the WiFi driver module on boot to enable automatic reconnection.

prerequisites:
    - An NXP [FRDM i.MX 93](https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93) board.
    - A computer running Linux or macOS.
    - A USB-C cable for the board's **DBG** serial connection.
    - A USB-C power supply/cable for the board's **POWER** port.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: 567387e8e513458a360f74c14d3f4d02c4af392bc573620e605c93976e4d8b4f
  summary: >-
    Learn how to boot and configure the NXP FRDM i.MX 93 Arm board with Linux, create a user with
    sudo access, connect to WiFi using ConnMan, and transfer files over the network. It is designed
    for embedded developers and ML engineers who want to boot an NXP FRDM i.MX 93 board, connect
    over serial, enable WiFi, and transfer files for on-device development on Arm. By the end,
    you will be able to boot the NXP FRDM i.MX 93 board and log in to Linux over a serial console,
    create a non-root Linux user with sudo access for development workflows, and connect the board
    to WiFi using ConnMan. It focuses on tools and technologies such as Bash, systemd, picocom,
    ConnMan, and OpenSSH, Linux and macOS environments, and Arm platforms including Cortex-A.
    The main steps cover Set up the board, Set up a Linux user and connect to WiFi, Transfer files
    to the board, and (Optional) Enable Persistent WiFi.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will boot the NXP FRDM i.MX 93 board and log in to Linux over a serial console, create
      a non-root Linux user with sudo access for development workflows, and connect the board
      to WiFi using ConnMan. Learn how to boot and configure the NXP FRDM i.MX 93 Arm board with
      Linux, create a user with sudo access, connect to WiFi using ConnMan, and transfer files
      over the network.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for embedded developers and ML engineers who want to boot
      an NXP FRDM i.MX 93 board, connect over serial, enable WiFi, and transfer files for on-device
      development on Arm.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An NXP [FRDM i.MX 93](https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93)
      board.; A computer running Linux or macOS.; A USB-C cable for the board's **DBG** serial
      connection.; A USB-C power supply/cable for the board's **POWER** port.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Bash, systemd, picocom, ConnMan, and OpenSSH, Linux
      and macOS environments, and Arm platforms such as Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up the board, Set up a Linux user and connect
      to WiFi, Transfer files to the board, and (Optional) Enable Persistent WiFi.
# END generated_summary_faq

author: Waheed Brown

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A

operatingsystems:
    - Linux
    - macOS

tools_software_languages:
    - Bash
    - systemd
    - picocom
    - ConnMan
    - OpenSSH

further_reading:
    - resource:
        title: Getting Started with FRDM-IMX93
        link: https://www.nxp.com/document/guide/getting-started-with-frdm-imx93:GS-FRDM-IMX93
        type: documentation
    - resource:
        title: TinyML Brings AI to Smallest Arm Devices
        link: https://newsroom.arm.com/blog/tinyml
        type: blog
    - resource:
        title: Arm Machine Learning Resources
        link: https://www.arm.com/developer-hub/embedded-and-microcontrollers/ml-solutions/getting-started
        type: documentation
    - resource:
        title: Arm Developers Guide for Cortex-M Processors and Ethos-U NPU
        link: https://developer.arm.com/documentation/109267/0101
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

