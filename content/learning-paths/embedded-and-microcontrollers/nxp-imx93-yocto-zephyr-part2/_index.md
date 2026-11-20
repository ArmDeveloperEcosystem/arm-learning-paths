---
title: "Part 2: NXP FRDM i.MX 93 \u2014 Run a Zephyr heartbeat alongside Yocto Linux"
draft: true
cascade:
    draft: true
description: "Build a board-specific Zephyr application and manage it through Linux remoteproc while Greengrass keeps running."
minutes_to_complete: 90
who_is_this_for: Embedded Linux developers connecting an NXP application processor and MCU to AWS IoT Greengrass.
learning_objectives:
    - "Build Zephyr for the application Cortex-M33"
    - "Observe an MCU heartbeat alongside Linux"
    - "Quiesce and stop the application core through remoteproc"
prerequisites:
    - "NXP FRDM i.MX 93 with an appropriate power supply, microSD card and reader, wired Ethernet, and its debug USB cable"
    - An Ubuntu 22.04 or 24.04 host on x86_64 (amd64) or arm64 (aarch64) with 32 GB RAM and 300–500 GB free space on a Linux filesystem
    - AWS CLI v2 and an account permitted to manage IoT identities, Greengrass deployments, and component artifacts
    - "Complete Part 1 for this same board; retain its image, identity and thing group"
    - Python 3.12 or newer, west, CMake, Ninja, and Zephyr SDK 0.17.4 on the Linux development host
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
    - AWS IoT Greengrass
    - Python
    - Zephyr
    - C
further_reading:
    - resource:
        title: "NXP FRDM i.MX 93 Part 1 \u2014 Yocto and Greengrass"
        link: /learning-paths/embedded-and-microcontrollers/nxp-imx93-yocto-gglite-part1/
        type: learningpath
    - resource:
        title: "NXP FRDM i.MX 93 Part 3 \u2014 BMP280 telemetry and cloud components"
        link: /learning-paths/embedded-and-microcontrollers/nxp-imx93-gglite-zephyr-combined-part3/
        type: learningpath
### FIXED, DO NOT MODIFY
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
