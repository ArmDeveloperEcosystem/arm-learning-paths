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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:28:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 567387e8e513458a360f74c14d3f4d02c4af392bc573620e605c93976e4d8b4f
  summary_generated_at: '2026-06-01T21:43:12Z'
  summary_source_hash: 567387e8e513458a360f74c14d3f4d02c4af392bc573620e605c93976e4d8b4f
  faq_generated_at: '2026-06-02T22:28:35Z'
  faq_source_hash: 567387e8e513458a360f74c14d3f4d02c4af392bc573620e605c93976e4d8b4f
  summary: >-
    This Learning Path shows how to bring up Linux on the NXP FRDM i.MX 93 board and prepare it
    for on-device development. You will boot and log in over the DBG serial console, create a
    non-root user with sudo access, connect to WiFi using ConnMan, and transfer files to the board
    with OpenSSH scp or a USB drive. An optional step configures the WiFi driver to load at boot
    so ConnMan can reconnect automatically after a reboot. It targets embedded developers and
    ML engineers working with Arm Cortex-A55–based hardware. Prerequisites include the FRDM i.MX
    93 board, a Linux or macOS host, and USB-C cables for power and serial. Estimated time: 120
    minutes.
  faqs:
  - question: What do I need before powering the board?
    answer: >-
      You need an NXP FRDM i.MX 93 board, a Linux or macOS host computer, a USB-C cable for the
      DBG serial connection, and a USB-C power supply for the POWER port. These are the explicit
      prerequisites.
  - question: How do I access the Linux console on the board?
    answer: >-
      Connect your host to the board’s DBG serial port over USB-C and use a serial console tool
      such as picocom. You will boot the board and log in over the serial console as described
      in the steps.
  - question: Which tool should I use to connect to WiFi, and how do I verify it worked?
    answer: >-
      Use ConnMan (via connmanctl) to join your WiFi network. To verify connectivity, run ifconfig
      and look for the WiFi interface (often mlan0) and its inet address.
  - question: How do I transfer files to the board during development?
    answer: >-
      Use scp over WiFi by targeting the board’s IP address and destination path. If WiFi is unavailable,
      you can move files with a USB drive.
  - question: What should I check if WiFi does not reconnect after a reboot?
    answer: >-
      Load the WiFi driver module after boot using the provided modprobe command so ConnMan can
      reconnect to the saved network. Give it up to a minute to establish a link, then confirm
      with ifconfig.
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

