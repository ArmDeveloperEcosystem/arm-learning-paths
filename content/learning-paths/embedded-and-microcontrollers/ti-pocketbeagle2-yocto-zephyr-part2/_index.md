---
title: "Part 2: Run Zephyr on the PocketBeagle 2 MCU alongside Yocto Linux"
draft: true
cascade:
    draft: true
description: Build a Zephyr heartbeat for the PocketBeagle 2 Cortex-M4F, load it from Yocto Linux with remoteproc, and verify Linux and MCU execution together.
minutes_to_complete: 60
who_is_this_for: Embedded Linux developers adding a Zephyr application to the MCU on a PocketBeagle 2 running Yocto Linux.
learning_objectives:
    - Verify that your Yocto image enables the AM6254 M4 remote processor
    - Build a Zephyr UART heartbeat for the Cortex-M4F
    - Load the ELF firmware from Linux into an offline M4
    - Verify MCU heartbeat output while Linux and Greengrass continue running
prerequisites:
    - A PocketBeagle 2 revision A1 with AM6254, running the updated image from [Part 1](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/)
    - SSH access and outbound networking configured as in Part 1
    - An Ubuntu 22.04 or 24.04 build host, from [Part 1](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/), with Git, Python 3, CMake, Ninja, west, and Zephyr SDK support for Arm
    - A 3.3 V logic USB-to-UART adapter, jumper wires, and a serial terminal on your workstation
author: Doug Anson
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: Embedded Linux
armips:
    - Cortex-A
    - Cortex-M
operatingsystems:
    - Linux
    - RTOS
tools_software_languages:
    - Yocto Project
    - Zephyr
    - C
    - AWS IoT Greengrass
further_reading:
    - resource:
        title: Part 1 — Yocto Linux and Greengrass Lite on PocketBeagle 2
        link: /learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/
        type: learningpath
    - resource:
        title: Zephyr PocketBeagle 2 board documentation
        link: https://docs.zephyrproject.org/latest/boards/beagle/pocketbeagle_2/doc/pocketbeagle_2.html
        type: documentation
    - resource:
        title: Zephyr getting started guide
        link: https://docs.zephyrproject.org/latest/develop/getting_started/index.html
        type: documentation
    - resource:
        title: Zephyr v4.3.0 PocketBeagle 2 board sources
        link: https://github.com/zephyrproject-rtos/zephyr/tree/v4.3.0/boards/beagle/pocketbeagle_2
        type: documentation
    - resource:
        title: Linux remoteproc framework
        link: https://docs.kernel.org/staging/remoteproc.html
        type: documentation
### FIXED, DO NOT MODIFY
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
