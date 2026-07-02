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
  generated_at: '2026-07-02T17:15:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 202dcb3054a983defc04c70315a3329f88ebbb20ca21039d3f24fb44314d1e09
  summary_generated_at: '2026-07-02T17:15:02Z'
  summary_source_hash: 202dcb3054a983defc04c70315a3329f88ebbb20ca21039d3f24fb44314d1e09
  faq_generated_at: '2026-07-02T17:15:02Z'
  faq_source_hash: 202dcb3054a983defc04c70315a3329f88ebbb20ca21039d3f24fb44314d1e09
  summary: >-
    This Learning Path guides you through registering a Raspberry Pi 5 and an NVIDIA Jetson Thor
    as AWS IoT Greengrass core devices, building a custom component that checks for Arm Pointer
    Authentication (PAC) and Branch Target Identification (BTI), and deploying it to both devices
    using a Greengrass thing group. The Raspberry Pi 5 (Armv8.2-A) acts as the negative comparison
    platform, while the Jetson Thor (Armv9-A) provides the positive case. After uploading the
    component artifact to Amazon S3 and completing the deployment, you use MQTT to trigger the
    checks and compare results, confirming the expected difference in PAC/BTI support.
  faqs:
  - question: How do I know both devices are ready before I create the deployment?
    answer: >-
      Check that each device is set up as an AWS IoT Greengrass core device and added to the thing
      group you plan to target (for example, My_PAC_BTI_Test_Devices). If both appear when selecting
      the group during deployment creation, you are ready to proceed.
  - question: Which device should report PAC/BTI support after the test runs?
    answer: >-
      Jetson Thor (Armv9-A) should report support for both PAC and BTI. Raspberry Pi 5 (Armv8.2-A)
      should report that neither feature is supported.
  - question: What should I check after uploading the component artifact to Amazon S3?
    answer: >-
      Confirm the bucket exists and that the artifact file appears in the bucket. Ensure you reference
      the correct bucket and object when creating the custom component.
  - question: How do I trigger the PAC/BTI check once the deployment is complete?
    answer: >-
      Use MQTT as described in the steps to publish the trigger for the component and then review
      the returned messages. The results indicate PAC/BTI support for each device.
  - question: What should I check if one device does not produce results after I publish the MQTT
      message?
    answer: >-
      Verify the device is in the selected thing group and that the deployment targeted that group.
      If the device is not set up as a Greengrass core device, complete that setup and redeploy.
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

