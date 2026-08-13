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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:09:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 75fdc487feb016b4d628382b41518290b53626675c4f9fda6ee5e85bb8681bf6
  summary_generated_at: '2026-08-12T20:09:33Z'
  summary_source_hash: 75fdc487feb016b4d628382b41518290b53626675c4f9fda6ee5e85bb8681bf6
  faq_generated_at: '2026-08-12T20:09:33Z'
  faq_source_hash: 75fdc487feb016b4d628382b41518290b53626675c4f9fda6ee5e85bb8681bf6
  summary: >-
    You'll configure an NXP FRDM i.MX 93 board for Linux development. Through a serial console,
    you'll create a non-root user with `sudo` privileges and connect to Wi-Fi with ConnMan. Then, you'll
    find the board's IP address, transfer files with `scp` or USB, and optionally load the Wi-Fi
    driver at startup for automatic reconnection.
  faqs:
  - question: Which USB-C port do I use for serial and power?
    answer: >-
      Use the DBG port for the serial connection and the POWER port for board power. Connect both ports
      if you need console access while powering the board.
  - question: How do I know the board has booted and I’m on the right console?
    answer: >-
      You should see Linux boot messages followed by a login prompt on the serial console. Log
      in as root initially to complete the bring-up steps.
  - question: How do I confirm the new user actually has sudo access?
    answer: >-
      After adding the user to the `wheel` group and enabling `wheel` in `sudoers`, log in as that user
      and run a command with `sudo`. If the command runs successfully, the configuration is correct.
  - question: Which IP address should I use for `scp`, and how do I find it?
    answer: >-
      Run the provided `ifconfig` command and look for the Wi-Fi interface, often named `mlan0`,
      then note its `inet` address. Use that IP in the `scp` target path.
  - question: What should I check if WiFi doesn’t reconnect after a reboot?
    answer: >-
      Load the Wi-Fi driver with the provided `modprobe` command so ConnMan can reconnect to the
      saved network. After loading, verify the interface has an IP address before continuing.
# END generated_summary_faq

author: Waheed Brown

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
