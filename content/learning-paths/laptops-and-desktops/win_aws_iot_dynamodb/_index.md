---
title: Use Amazon DynamoDB for your IoT applications running on Arm64

description: Learn how to configure AWS IoT Core rules to parse MQTT messages and store IoT data in Amazon DynamoDB from Windows on Arm devices.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers who are interested in using Amazon DynamoDB as a database for storing data.

learning_objectives:
   - Gain familiarity with Amazon DynamoDB.
   - Be able to run the IoT application that streams data to AWS IoT Core.
   - Be able to create the rule that parses messages from AWS IoT Core and writes them to DynamoDB.

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).   
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.
    - Completion of the [Create IoT applications with Windows on Arm and AWS IoT Core](/learning-paths/laptops-and-desktops/win_aws_iot/) Learning Path.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:22:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f25597c6c9e69e09e9a86fa7c02d0ace9c347f293a21a11c00a6d3498300052c
  summary_generated_at: '2026-06-01T22:13:59Z'
  summary_source_hash: f25597c6c9e69e09e9a86fa7c02d0ace9c347f293a21a11c00a6d3498300052c
  faq_generated_at: '2026-06-02T23:22:02Z'
  faq_source_hash: f25597c6c9e69e09e9a86fa7c02d0ace9c347f293a21a11c00a6d3498300052c
  summary: >-
    This Learning Path guides you through configuring AWS IoT Core to parse MQTT messages and
    store IoT data in Amazon DynamoDB from a Windows on Arm environment. Building on the previously
    completed weather-station emulator and AWS IoT setup, you will run the IoT application that
    streams data to AWS IoT Core and create an IoT Core rule (send_message_to_dynamodb) that writes
    parsed messages to DynamoDB. The path targets Windows on Arm devices and uses a code editor
    such as Visual Studio Code; .NET is listed in the metadata. Prerequisites include a Windows
    on Arm PC or VM, any code editor, and completion of the prior “Create IoT applications with
    Windows on Arm and AWS IoT Core” Learning Path.
  faqs:
  - question: What do I need before running these steps?
    answer: >-
      You need a Windows on Arm computer such as the Lenovo ThinkPad X13s running Windows 11,
      or a Windows on Arm virtual machine, and any code editor; Visual Studio Code for Arm64 is
      suitable. Complete the "Create IoT applications with Windows on Arm and AWS IoT Core" Learning
      Path to prepare the weather station emulator and connect it to AWS IoT Core.
  - question: Where do I create the AWS IoT Core rule?
    answer: >-
      In AWS IoT Core, go to Message routing and select Rules. Click Create rule to open the Create
      rule view.
  - question: What should I name the rule?
    answer: >-
      Use send_message_to_dynamodb as the rule name when prompted. Then proceed through the configuration
      views as described in the steps.
  - question: Do I need to modify or rebuild the IoT application for this path?
    answer: >-
      The path expects you to run the existing IoT application from the prerequisite to stream
      data to AWS IoT Core. The focus here is on configuring the AWS IoT Core rule that writes
      to DynamoDB.
  - question: What result should I expect after completing the configuration?
    answer: >-
      The rule parses incoming MQTT messages from AWS IoT Core and writes the data to Amazon DynamoDB.
      This connects your Arm64-based Windows workload to persistent storage in DynamoDB.
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
    - .NET    
    - Visual Studio Code

further_reading:
    - resource:
        title: DynamoDB
        link: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
        type: documentation
    - resource:
        title: Using DynamoDB with other AWS services
        link: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/OtherServices.html
        type: documentation
    - resource:
        title: Rules for AWS IoT 
        link: https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

