---
title: "Part 1: Deploy a Hello World component to PocketBeagle 2 with Greengrass Lite"
aliases:
    - /learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite/
draft: true
cascade:
    draft: true
description: Build a PocketBeagle 2 Yocto image, provision AWS IoT Greengrass nucleus lite, and deploy a Hello World component through an AWS IoT thing group.
minutes_to_complete: 120
who_is_this_for: Embedded Linux developers connecting an Arm-based PocketBeagle 2 to AWS IoT Greengrass.
learning_objectives:
    - Build and boot the PocketBeagle 2 Yocto development image
    - Provision a unique device identity for Greengrass nucleus lite
    - Publish a simple Hello World component to AWS IoT Greengrass
    - Deploy the component through a thing group and verify execution on the board
prerequisites:
    - A PocketBeagle 2, a 32 GB or larger microSD card, a card reader, and a USB-C data cable
    - An x86_64 Ubuntu 22.04 build host with 16–32 GB RAM and 250–400 GB free disk on a Linux filesystem
    - An AWS account with permission to manage IoT resources and Greengrass deployments, plus an approved token-exchange IAM role or permission to create one
    - AWS CLI v2 configured on an administrative workstation and Python 3 for validating JSON and generating deployment documents
    - Internet access for the build host and board, using host Internet sharing or a supported USB Ethernet adapter and host cape
# Build time depends on the host and cache; allow several additional hours for the first image build.
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
        title: Part 2 — Run Zephyr on the PocketBeagle 2 MCU
        link: /learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-zephyr-part2/
        type: learningpath
    - resource:
        title: PocketBeagle 2 quick start
        link: https://docs.beagleboard.org/boards/pocketbeagle-2/02-quick-start.html
        type: documentation
    - resource:
        title: Yocto Scarthgap host requirements
        link: https://docs.yoctoproject.org/scarthgap/ref-manual/system-requirements.html
        type: documentation
    - resource:
        title: Nucleus Lite 2.6.0 provisioning
        link: https://github.com/aws-greengrass/aws-greengrass-lite/blob/v2.6.0/docs/Provisioning.md
        type: documentation
    - resource:
        title: Greengrass component recipe reference
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/component-recipe-reference.html
        type: documentation
    - resource:
        title: Create Greengrass deployments
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html
        type: documentation
### FIXED, DO NOT MODIFY
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
