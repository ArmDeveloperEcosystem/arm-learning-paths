---
title: Use Linux on the NXP FRDM i.MX 93 board

draft: true
cascade:
    draft: true
    
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
