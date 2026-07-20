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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:01:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 202dcb3054a983defc04c70315a3329f88ebbb20ca21039d3f24fb44314d1e09
  summary_generated_at: '2026-07-02T19:01:20Z'
  summary_source_hash: 202dcb3054a983defc04c70315a3329f88ebbb20ca21039d3f24fb44314d1e09
  faq_generated_at: '2026-07-02T19:01:20Z'
  faq_source_hash: 202dcb3054a983defc04c70315a3329f88ebbb20ca21039d3f24fb44314d1e09
  summary: >-
    You'll configure two Arm devices as AWS IoT Greengrass
    core devices, build a custom component that checks Pointer Authentication (PAC) and Branch
    Target Identification (BTI), and deploy that component to both targets via a Greengrass
    thing group. You'll upload the component artifact to Amazon S3, create a Greengrass deployment
    in the AWS console, and use MQTT to trigger the checks. The Raspberry Pi 5 (Armv8.2-A) serves
    as a negative comparison for PAC/BTI, while the Jetson Thor (Armv9-A) provides a positive
    control. By completing the steps, you'll compare per-device results and recognize unsupported
    versus supported PAC/BTI behavior across Armv8 and Armv9 platforms.
  faqs:
  - question: How do I know each device is ready to receive a Greengrass deployment?
    answer: >-
      In AWS IoT Core, confirm the device is registered as a Greengrass core device and appears
      in the thing group you plan to deploy to. If it isn't in the group, add it before creating
      the deployment.
  - question: What result should I expect from the PAC/BTI test on Raspberry Pi 5 versus Jetson
      Thor?
    answer: >-
      Raspberry Pi 5 (Armv8.2-A) should report PAC and BTI as not supported. Jetson Thor (Armv9-A)
      should report both PAC and BTI as supported.
  - question: Where should I store the custom component artifact before creating the deployment?
    answer: >-
      Upload the component artifact to an Amazon S3 bucket created in the AWS console. Keep the
      default bucket settings for this tutorial and ensure the artifact is available for the component
      to use during deployment.
  - question: Which target should I select to deploy the component to both devices at once?
    answer: >-
      Select a Greengrass thing group (for example, My_PAC_BTI_Test_Devices) as the deployment
      target. This delivers the same component set to both core devices in the group.
  - question: How do I trigger and validate the PAC/BTI checks after deployment?
    answer: >-
      Use MQTT to trigger the checks as described in the steps, then review the results reported
      for each device. Expect outputs that let you interpret PAC/BTI support per platform.
# END generated_summary_faq

author:
    - Varun Chari
    - Doug Anson

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
