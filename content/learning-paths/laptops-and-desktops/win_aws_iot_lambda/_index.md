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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:23:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f685f45be9e5fc05b278e28590f9d421a920d43cc36ccb572545de4eaf4a799a
  summary_generated_at: '2026-06-01T22:14:31Z'
  summary_source_hash: f685f45be9e5fc05b278e28590f9d421a920d43cc36ccb572545de4eaf4a799a
  faq_generated_at: '2026-06-02T23:23:16Z'
  faq_source_hash: f685f45be9e5fc05b278e28590f9d421a920d43cc36ccb572545de4eaf4a799a
  summary: >-
    This Learning Path shows how to process IoT data on Arm64 by connecting AWS IoT Core to an
    AWS Lambda function from a Windows on Arm device. You will reuse the weather-station IoT emulator
    from the prerequisite path, create an AWS IoT Core rule to route temperature messages, and
    implement a Lambda function that checks a threshold and uses Amazon SNS to send email notifications.
    The target environment is Windows on Arm, using tools such as .NET and Visual Studio Code.
    By the end, you will have an event-driven flow from IoT Core to Lambda and SNS. Prerequisites
    include a Windows on Arm machine or VM and completion of the prior AWS IoT Core Learning Path.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer or a Windows on Arm virtual machine, a code editor such
      as Visual Studio Code for Arm64, and completion of the “Create IoT applications with Windows
      on Arm and AWS IoT Core” Learning Path to set up the weather station emulator and connect
      it to AWS IoT Core.
  - question: Where do I create the AWS IoT Core rule that triggers the Lambda function?
    answer: >-
      In AWS IoT Core, open Message routing and select Rules. Click Create rule and configure
      it in the Create rule view.
  - question: Which AWS services are used and how do they interact in this path?
    answer: >-
      AWS IoT Core receives temperature messages from the emulator, an IoT Core rule triggers
      an AWS Lambda function, and the Lambda function uses Amazon Simple Notification Service
      (SNS) to send an email when the temperature exceeds a predefined threshold.
  - question: How do I know the Lambda trigger and notifications are working?
    answer: >-
      Publish a temperature value above the defined threshold from the emulator. You should receive
      an email notification when the Lambda function is invoked by the IoT Core rule.
  - question: What should I check if I do not receive an email after sending a high temperature
      reading?
    answer: >-
      Confirm the emulator is connected to AWS IoT Core and sending data to the expected topic,
      verify the IoT Core rule targets your Lambda function, and review the threshold logic in
      the Lambda implementation and its use of SNS for email delivery.
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

