---
title: Use AWS Lambda for IoT applications running on Arm64

description: Learn how to process IoT data using AWS Lambda functions triggered by AWS IoT Core messages from Windows on Arm devices.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers who are interested in using AWS Lambda for processing data streamed by IoT applications and devices.

learning_objectives:
   - Describe how to use AWS Lambda for IoT applications running on Arm64.
   - Process data from IoT devices.
   - Describe the serverless compute services in AWS.
   - Describe the notification services in AWS.

prerequisites:
    - A Windows on Arm computer such as the a Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).   
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.
    - Completion of the [Create IoT applications with Windows on Arm and AWS IoT Core](/learning-paths/laptops-and-desktops/win_aws_iot/) Learning Path.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:31:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f685f45be9e5fc05b278e28590f9d421a920d43cc36ccb572545de4eaf4a799a
  summary_generated_at: '2026-07-28T16:31:05Z'
  summary_source_hash: f685f45be9e5fc05b278e28590f9d421a920d43cc36ccb572545de4eaf4a799a
  faq_generated_at: '2026-07-28T16:31:05Z'
  faq_source_hash: f685f45be9e5fc05b278e28590f9d421a920d43cc36ccb572545de4eaf4a799a
  summary: >-
    This Learning Path shows how to build a serverless workflow on AWS that reacts to IoT telemetry
    published from a Windows on Arm device. You connect the existing weather-station emulator
    to AWS IoT Core, create a rule to invoke an AWS Lambda function on the relevant topic, and
    implement the function to evaluate incoming temperature readings against a predefined threshold.
    The function integrates with Amazon Simple Notification Service (SNS) to send an email when
    the condition is met. Learners configure event routing and function logic and see how IoT
    Core messages trigger notifications end to end on Arm64.
  faqs:
  - question: Do I need to run the same IoT emulator I used in the earlier Learning Path?
    answer: >-
      Yes. Prepare the weather station emulator and connect it to AWS IoT Core by completing the
      Create IoT applications with Windows on Arm and AWS IoT Core Learning Path.
  - question: Which IoT Core topic should my rule subscribe to?
    answer: >-
      Use the same topic your emulator publishes to from the previous Learning Path. Check the
      emulator configuration to confirm the exact topic string.
  - question: Where do I define the temperature threshold for my alerts?
    answer: >-
      Define the threshold inside the Lambda function implementation. The function compares incoming
      temperature values against this predefined value.
  - question: Which AWS service actually sends the notification email?
    answer: >-
      Amazon Simple Notification Service (SNS) is used to send emails. The Lambda function publishes
      a message to an SNS topic configured for email delivery.
  - question: What result should I expect when everything is configured correctly, and what should
      I check if no email arrives?
    answer: >-
      When a message on the configured topic exceeds your threshold, the Lambda function runs
      and an email is sent via SNS. If no email arrives, verify the IoT rule targets your Lambda
      function and that the payload temperature actually exceeds the threshold.
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
        title: AWS Lambda
        link: https://aws.amazon.com/lambda/
        type: website
    - resource:
        title: Amazon SNS
        link: https://aws.amazon.com/sns/
        type: website
    - resource:
        title: Overview of AWS
        link: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

