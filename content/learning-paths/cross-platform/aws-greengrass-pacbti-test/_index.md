---
title: Deploy an AWS IoT Greengrass custom component to Arm devices and verify PAC/BTI support

description: Learn how to register Arm devices as AWS IoT Greengrass core devices, build and deploy a custom component, and use MQTT to verify PAC/BTI support across Armv8 and Armv9 platforms.
    
minutes_to_complete: 30   

who_is_this_for: This Learning Path is for IoT and embedded developers who want to deploy and manage components on Arm devices using AWS IoT Greengrass, and verify PAC/BTI security feature support across different Arm platforms.

learning_objectives: 
    - Register Armv8 and Armv9 devices as AWS IoT Greengrass core devices
    - Build an AWS IoT Greengrass custom component that tests PAC/BTI support
    - Deploy the component to multiple Arm devices using a Greengrass Thing Group
    - Use MQTT to trigger PAC/BTI checks and interpret the results for each platform

prerequisites:
    - An [Amazon Web Services (AWS)](https://aws.amazon.com/) account with access to AWS IoT Greengrass and Amazon S3
    - A Raspberry Pi 5 running Raspberry Pi OS
    - An NVIDIA Jetson Thor device running JetPack 7.1 or later
    - Familiarity with AWS IoT Core and basic cloud concepts


author:
    - Varun Chari
    - Doug Anson

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
    - AWS

armips:
    - Cortex-A

tools_software_languages:
    - AWS IoT Greengrass
    - Python
    - Java
    - MQTT
    - YAML

operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - embedded-and-microcontrollers

further_reading:
  - resource:
      title: AWS IoT Greengrass documentation
      link: https://aws.amazon.com/greengrass/
      type: documentation
  - resource:
      title: Develop AWS IoT Greengrass components
      link: https://docs.aws.amazon.com/greengrass/v2/developerguide/develop-greengrass-components.html
      type: documentation
  - resource:
      title: AWS IoT Greengrass v2 Developer Guide
      link: https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html
      type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
