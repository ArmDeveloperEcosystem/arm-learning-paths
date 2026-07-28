---
title: Create IoT applications with Windows on Arm and AWS IoT Core

description: Learn how to create Node.js IoT applications that stream sensor data from Windows on Arm devices to AWS IoT Core using MQTT.

minutes_to_complete: 120

who_is_this_for: This learning path is for developers who want to learn how to create IoT applications using Windows on Arm and AWS IoT Core.

learning_objectives:
    - Create a Node.js that streams synthesized sensor data to AWS cloud.
    - Register a device in AWS IoT Core.    
    - Send data from a device to AWS IoT Core.

prerequisites:
    - A Windows-on-Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows-on-Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Any code editor. Visual Studio Code is suitable.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:51:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cddfb7b83e82f0daa513558b1e7ee09b55c63e2ff95675d67be7d4408d391aa4
  summary_generated_at: '2026-07-28T16:51:54Z'
  summary_source_hash: cddfb7b83e82f0daa513558b1e7ee09b55c63e2ff95675d67be7d4408d391aa4
  faq_generated_at: '2026-07-28T16:51:54Z'
  faq_source_hash: cddfb7b83e82f0daa513558b1e7ee09b55c63e2ff95675d67be7d4408d391aa4
  summary: >-
    This Learning Path guides you through creating a Node.js emulator on Windows on Arm that streams
    synthesized sensor readings to AWS IoT Core over MQTT. Using the AWS IoT Core console, you
    register and secure a device with the Connect one device wizard, verify endpoint reachability
    with the ping command it provides, and connect the emulator to begin publishing. You then
    validate the data flow in the MQTT test client by subscribing to the Emulators/Weather/SensorReadings
    topic and observing incoming messages. The workflow demonstrates an end-to-end device-to-cloud
    path on Windows on Arm, and success is clear when sensor data appears live in the AWS IoT
    Core test client.
  faqs:
  - question: Where do I start in the AWS Console to connect the emulator?
    answer: >-
      Sign in to the AWS Console, search for IoT, and select IoT Core. In the IoT Core console,
      choose Connect one device to open the setup wizard.
  - question: How do I verify connectivity to the AWS IoT Core endpoint before streaming data?
    answer: >-
      Use the ping command shown in the Register and secure your device step of the wizard. Successful
      replies confirm your device can reach the endpoint.
  - question: Which MQTT topic should I subscribe to when testing the stream?
    answer: >-
      Use the MQTT test client and subscribe to Emulators/Weather/SensorReadings. You should see
      the emulator’s messages appear under that topic.
  - question: I subscribed but don’t see any messages. What should I check?
    answer: >-
      Confirm the emulator is running and connected. Verify the topic filter matches exactly and
      recheck endpoint reachability with the ping command.
  - question: How do I know the device-to-cloud path is working end to end?
    answer: >-
      The MQTT test client will display the emulator’s data after you subscribe to the topic.
      Seeing messages arrive confirms the stream is active.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - Node.js    
    - Visual Studio

further_reading:
    - resource:
        title: AWS IoT Core Developer Guide
        link: https://docs.aws.amazon.com/iot/latest/developerguide
        type: documentation
    - resource:
        title: Connecting a device to AWS IoT Core by using the AWS IoT Device SDK
        link: https://docs.aws.amazon.com/iot/latest/developerguide/sdk-tutorials.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

