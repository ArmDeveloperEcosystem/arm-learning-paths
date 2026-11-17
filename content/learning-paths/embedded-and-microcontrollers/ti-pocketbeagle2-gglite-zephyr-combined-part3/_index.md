---
title: "Part 3: Deploy PocketBeagle 2 temperature sensing to AWS IoT Core with Zephyr and Greengrass Lite"
draft: true
cascade:
    draft: true
description: Extend the Part 1 Yocto image and Part 2 Cortex-M4F work with two S3-backed Greengrass components that manage external temperature sensing and publish JSON to AWS IoT Core.
minutes_to_complete: 120
who_is_this_for: Embedded Linux developers managing a Zephyr application and a Linux telemetry bridge through AWS IoT Greengrass.
learning_objectives:
    - Read calibrated temperature from an external BMP280 over I2C using Zephyr on the Cortex-M4F
    - Implement the mailbox shutdown acknowledgment required by the Part 1 Linux driver
    - Package firmware and a Linux bridge as two S3-backed Greengrass Lite custom components
    - Publish JSON telemetry to ti/pocketbeagle2/temperature/external through Greengrass IPC
    - Remove the components through a revised deployment and verify application cleanup
prerequisites:
    - Complete [Part 1](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/) and [Part 2](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-zephyr-part2/) on PocketBeagle 2 revision A1 with AM6254
    - Keep the Part 1 Yocto image, Nucleus Lite 2.6.0 installation, device identity, Internet connection, and dedicated thing group
    - Keep the Part 2 Ubuntu build host, Zephyr v4.3.0 workspace, and Zephyr SDK 0.17.4
    - The supplied BMP280 I2C breakout with 3.3 V supply and logic, external I2C pull-ups, and jumper wires
    - AWS CLI v2 and permission to publish components, revise deployments, create an S3 bucket, and extend the existing device role and certificate policy
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
    - AWS IoT Greengrass
    - C
    - Python
further_reading:
    - resource:
        title: Part 1 — Yocto Linux and Greengrass Lite
        link: /learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/
        type: learningpath
    - resource:
        title: Part 2 — Zephyr on the Cortex-M4F
        link: /learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-zephyr-part2/
        type: learningpath
    - resource:
        title: Nucleus Lite 2.6.0 recipe support
        link: https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/RECIPE_SUPPORT_CHANGES.md
        type: documentation
### FIXED, DO NOT MODIFY
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
