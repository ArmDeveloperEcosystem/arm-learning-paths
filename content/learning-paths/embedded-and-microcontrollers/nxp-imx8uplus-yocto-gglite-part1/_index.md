---
title: "Part 1: NXP FRDM i.MX 8M Plus: Build Yocto and deploy a Greengrass Lite Hello World"
draft: true
cascade:
    draft: true
description: "Build a board-specific NXP Yocto image, provision its identity, and deploy Hello World through a thing group."
minutes_to_complete: 120
who_is_this_for: Embedded Linux developers connecting an NXP application processor and MCU to AWS IoT Greengrass.
learning_objectives:
    - "Build the imx8mp-lpddr4-frdm image with Greengrass Lite and MCU integration"
    - "Provision a unique AWS IoTCore/Greengrass identity for NXP FRDM i.MX 8M Plus"
    - "Publish and deploy a board-specific Hello World component"
prerequisites:
    - "NXP FRDM i.MX 8M Plus with an appropriate power supply, microSD card and reader, wired Ethernet, and its debug USB cable"
    - An Ubuntu 22.04 or 24.04 host on x86_64 (amd64) or arm64 (aarch64) with 32 GB RAM and 300–500 GB free space on a Linux filesystem
    - AWS CLI v2 and an account permitted to manage IoT identities, Greengrass deployments, and component artifacts
author: Doug Anson
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: Embedded Linux
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Yocto Project
    - AWS IoT Greengrass
    - Python
further_reading:
    - resource:
        title: "NXP FRDM i.MX 8M Plus Part 2 \u2014 Zephyr alongside Linux"
        link: /learning-paths/embedded-and-microcontrollers/nxp-imx8uplus-yocto-zephyr-part2/
        type: learningpath
    - resource:
        title: "NXP FRDM i.MX 8M Plus Part 3 \u2014 BMP280 telemetry and cloud components"
        link: /learning-paths/embedded-and-microcontrollers/nxp-imx8uplus-gglite-zephyr-combined-part3/
        type: learningpath
### FIXED, DO NOT MODIFY
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
