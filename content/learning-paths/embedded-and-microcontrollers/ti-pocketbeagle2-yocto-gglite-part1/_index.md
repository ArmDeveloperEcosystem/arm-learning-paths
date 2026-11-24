---
title: Deploy a component to PocketBeagle 2 with AWS IoT Greengrass 
description: Build a PocketBeagle 2 Yocto image, provision AWS IoT Greengrass nucleus lite, and deploy a Hello World component through an AWS IoT thing group.

minutes_to_complete: 180

who_is_this_for: This is an advanced topic for embedded Linux developers connecting an Arm-based PocketBeagle 2 to AWS IoT Greengrass.

learning_objectives:
    - Build and boot the PocketBeagle 2 Yocto development image.
    - Provision a unique device identity for Greengrass nucleus lite.
    - Publish an inline Hello World component to AWS IoT Greengrass.
    - Deploy the component through a thing group and verify that it runs on the board.

prerequisites:
    - A PocketBeagle 2, a 32 GB or larger microSD card, a card reader, and a USB-C cable
    - A host computer running Ubuntu 24.04 Linux with sudo access, 16 GB or more RAM, and 250–400 GB free disk space
    - An AWS account with permission to manage AWS IoT resources, publish Greengrass components, and create Greengrass deployments
    - The [AWS CLI](/install-guides/aws-cli/) v2 configured with [AWS credentials](/install-guides/aws_access_keys/) and Python 3 installed on the host computer

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
        title: PocketBeagle 2 quick start
        link: https://docs.beagleboard.org/boards/pocketbeagle-2/02-quick-start.html
        type: documentation
    - resource:
        title: Yocto Scarthgap host requirements
        link: https://docs.yoctoproject.org/scarthgap/ref-manual/system-requirements.html
        type: documentation
    - resource:
        title: AWS IoT Greengrass nucleus lite 2.6.0 provisioning
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
