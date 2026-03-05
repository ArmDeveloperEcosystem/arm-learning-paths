---
title: Deploy ML models to Arm edge devices using Edge Impulse and AWS IoT Greengrass

draft: true
cascade:
    draft: true

description: Learn how to deploy Edge Impulse ML models to Arm-based Linux edge devices using AWS IoT Greengrass custom components.

minutes_to_complete: 180

who_is_this_for: This Learning Path is for embedded and IoT engineers who want to deploy Edge Impulse ML models to Arm-based edge devices at scale using AWS IoT Greengrass.

learning_objectives:
    - Set up an Arm-based edge device for ML inference with Edge Impulse
    - Install and configure AWS IoT Greengrass on the edge device
    - Deploy an Edge Impulse ML model as a Greengrass custom component
    - Verify model inference results through AWS IoT Core

prerequisites:
    - An [Edge Impulse Studio](https://studio.edgeimpulse.com/signup) account
    - An [AWS account](https://aws.amazon.com/) with administrator access
    - A supported Arm-based edge device (Raspberry Pi 5, Nvidia Jetson, Qualcomm Dragonwing QC6490) or an AWS EC2 Arm instance
    - An SSH client and familiarity with the Linux command line
    - Basic understanding of ML concepts

author: Doug Anson

### Tags
skilllevels: Introductory
cloud_service_providers:
    - AWS
subjects: ML
armips:
    - Cortex-M
    - Cortex-A
    - Neoverse

tools_software_languages:
    - Edge Impulse
    - AWS IoT Greengrass
    - GStreamer

operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
    - resource:
        title: Edge Impulse for beginners
        link: https://docs.edgeimpulse.com/docs/readme/for-beginners
        type: documentation
    - resource:
        title: AWS IoT Greengrass developer guide
        link: https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html
        type: documentation
    - resource:
        title: Edge Impulse AWS Greengrass integration
        link: https://docs.edgeimpulse.com/docs/integrations/aws-greengrass
        type: documentation
    - resource:
        title: Edge Impulse Greengrass components repository
        link: https://github.com/edgeimpulse/aws-greengrass-components
        type: website

weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
