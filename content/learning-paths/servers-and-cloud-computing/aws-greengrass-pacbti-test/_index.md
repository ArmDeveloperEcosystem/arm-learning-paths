---
title: Test Arm PAC/BTI instruction readiness with an AWS IoT Greengrass custom component

description: Learn how to deploy an AWS IoT Greengrass custom component to Arm devices and verify PAC/BTI support through MQTT-triggered tests.

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30   

who_is_this_for: This Learning Path is for developers who want to use AWS IoT Greengrass to deploy a PAC/BTI test component to Arm platforms.

learning_objectives: 
    - Create an AWS IoT Greengrass custom component with the PAC/BTI test harness.
    - Register an Armv8 and an Armv9 device as AWS IoT Greengrass core devices.
    - Run PAC/BTI checks through MQTT and interpret the results for each device.

prerequisites:
    - A [Amazon AWS](https://aws.amazon.com/) account with access to AWS IoT Greengrass and AWS S3


author: Varun Chari, Doug Anson

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
    - AWS

armips:
    - Neoverse

tools_software_languages:
    - Python
    - Java
    - MQTT
    - YAML

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: AWS IoT Greengrass documentation
      link: https://aws.amazon.com/greengrass/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
