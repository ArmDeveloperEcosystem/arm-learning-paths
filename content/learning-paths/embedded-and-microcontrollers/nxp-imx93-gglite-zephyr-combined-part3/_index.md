---
title: "Part 3: NXP FRDM i.MX93 \u2014 Deploy BMP280 temperature sensing and an AWS IoT Core bridge" 
draft: true
cascade:
    draft: true
description: "Deploy MCU firmware and a Linux bridge as S3-backed custom Greengrass components."
minutes_to_complete: 120
who_is_this_for: Embedded Linux developers connecting an NXP application processor and MCU to AWS IoT Greengrass.
learning_objectives:
    - "Read the external temperature via the BMP280 sensor on the Cortex-M33 using Zephyr RTOS"
    - "Deploy two S3-backed AWS Greengrass components to install and run the Zephyr app and its Yocto bridge component"
    - "Publish JSON messages to nxp/imx93/temperature/external within AWS IoTCore containing the read temperature from the sensor"
    - "Remove both apps and verify cleanup and redeployment capabilities"
prerequisites:
    - "NXP FRDM i.MX 93 with an appropriate power supply, microSD card and reader, wired Ethernet, and its debug USB cable"
    - An Ubuntu 22.04 or 24.04 host on x86_64 (amd64) or arm64 (aarch64) with 32 GB RAM and 300–500 GB free space on a Linux filesystem
    - AWS CLI v2 and an account permitted to manage IoT identities, Greengrass deployments, and component artifacts
    - Complete Part 1 for this same board; retain its image, identity and thing group
    - Python 3.12 or newer, west, CMake, Ninja, and Zephyr SDK 0.17.4 on the Linux development host
    - Complete Part 2 and verify a repeatable application MCU start and stop
    - An external BMP280 I2C module with jumper wires
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
        title: "NXP FRDM i.MX 93 Part 2 \u2014 Zephyr alongside Linux"
        link: /learning-paths/embedded-and-microcontrollers/nxp-imx93-yocto-zephyr-part2/
        type: learningpath
### FIXED, DO NOT MODIFY
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
