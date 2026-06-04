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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:21:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cddfb7b83e82f0daa513558b1e7ee09b55c63e2ff95675d67be7d4408d391aa4
  summary_generated_at: '2026-06-01T22:13:29Z'
  summary_source_hash: cddfb7b83e82f0daa513558b1e7ee09b55c63e2ff95675d67be7d4408d391aa4
  faq_generated_at: '2026-06-02T23:21:33Z'
  faq_source_hash: cddfb7b83e82f0daa513558b1e7ee09b55c63e2ff95675d67be7d4408d391aa4
  summary: >-
    This Learning Path shows how to build a Node.js IoT application on Windows on Arm that streams
    synthesized sensor data to AWS IoT Core over MQTT. You will register a device using the AWS
    IoT Core “Connect one device” wizard, verify connectivity with the provided ping command,
    connect an emulator, and send data to the cloud. You will then validate the stream using the
    MQTT Test Client by subscribing to a specific topic. The path targets developers working on
    Windows on Arm devices or a Windows-on-Arm virtual machine, uses a code editor (Visual Studio
    Code is suitable), and takes about 120 minutes. It assumes access to the AWS Console but lists
    no additional prerequisites.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use a Windows-on-Arm computer such as a Lenovo ThinkPad X13s running Windows 11, or a Windows-on-Arm
      virtual machine, and any code editor (Visual Studio Code is suitable). The path uses Node.js;
      no other explicit prerequisites are listed.
  - question: Where do I register and connect the device in AWS IoT Core?
    answer: >-
      In the AWS Console, open IoT Core and select Connect one device. The wizard guides you through
      Register and secure your device and subsequent steps.
  - question: How do I check network connectivity to AWS IoT Core before sending data?
    answer: >-
      Use the ping command shown in the Connect one device wizard to confirm your device can reach
      the AWS IoT Core endpoint. Verify the ping succeeds before proceeding.
  - question: Which MQTT topic should I subscribe to in the test client to view messages?
    answer: >-
      Subscribe to Emulators/Weather/SensorReadings in the AWS IoT Core MQTT test client. This
      is where the emulator’s synthesized sensor data is published.
  - question: How do I know the data stream from the emulator is working?
    answer: >-
      After subscribing in the MQTT test client, you should see data from the emulator appear
      in the message pane. If no messages appear, re-check the connection steps in the wizard.
# END generated_summary_faq

author: Dawid Borycki

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

