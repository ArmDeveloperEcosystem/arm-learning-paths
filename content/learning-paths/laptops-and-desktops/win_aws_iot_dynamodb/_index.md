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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:30:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f25597c6c9e69e09e9a86fa7c02d0ace9c347f293a21a11c00a6d3498300052c
  summary_generated_at: '2026-07-28T16:30:05Z'
  summary_source_hash: f25597c6c9e69e09e9a86fa7c02d0ace9c347f293a21a11c00a6d3498300052c
  faq_generated_at: '2026-07-28T16:30:05Z'
  faq_source_hash: f25597c6c9e69e09e9a86fa7c02d0ace9c347f293a21a11c00a6d3498300052c
  summary: >-
    You'll route MQTT telemetry from a Windows on Arm weather-station emulator to Amazon DynamoDB
    with an AWS IoT Core rule. You'll create and name the rule, configure it to parse incoming
    messages and write to DynamoDB, run the emulator, and verify that the destination receives new
    items.
  faqs:
  - question: What do I need before creating the AWS IoT Core rule?
    answer: >-
      Complete the prerequisite path to prepare the weather station emulator and connect it to
      AWS IoT Core. The rule relies on that running message source.
  - question: Where do I create the rule in AWS IoT Core?
    answer: >-
      Open AWS IoT Core, select **Message routing**, then select **Rules** and **Create rule** to start
      configuring it.
  - question: What should I name the rule?
    answer: >-
      Use `send_message_to_dynamodb`. You can choose a different valid name,
      but you should use the suggested name to stay consistent with the Learning Path.
  - question: Which MQTT topic should the rule target?
    answer: >-
      Use the same topic that the weather station emulator uses in the prerequisite Learning Path [Create IoT applications with Windows on Arm and AWS IoT Core](/learning-paths/laptops-and-desktops/win_aws_iot/). 
  - question: How do I know the rule is writing data to DynamoDB?
    answer: >-
      After saving the rule and running the emulator, new items should appear in the DynamoDB
      destination you configured. If nothing appears, confirm the emulator is connected and that
      the rule’s configuration matches the emulator’s message topic.
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
