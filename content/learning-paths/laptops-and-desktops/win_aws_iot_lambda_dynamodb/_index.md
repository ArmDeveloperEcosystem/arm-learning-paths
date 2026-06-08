---
title: Integrate AWS Lambda with DynamoDB for IoT applications running Windows on Arm

description: Learn how to implement AWS Lambda functions that process and aggregate IoT data stored in DynamoDB tables from Windows on Arm devices.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers who are interested in using AWS Lambda for processing data stored in DynamoDB.

learning_objectives:   
   - Implement an AWS Lambda function that processes data stored in a DynamoDB table.
   - Learn how to work with DynamoDB to scan and aggregate records.

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).   
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.
    - Completion of the [Create IoT applications with Windows on Arm and AWS IoT Core](/learning-paths/laptops-and-desktops/win_aws_iot/) Learning Path.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:23:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f5a93346a0fd55659b7c0a6df501db97742ec71755b6443051b654f3ce871cdf
  summary_generated_at: '2026-06-01T22:14:53Z'
  summary_source_hash: f5a93346a0fd55659b7c0a6df501db97742ec71755b6443051b654f3ce871cdf
  faq_generated_at: '2026-06-02T23:23:55Z'
  faq_source_hash: f5a93346a0fd55659b7c0a6df501db97742ec71755b6443051b654f3ce871cdf
  summary: >-
    This Learning Path shows how to implement and test an AWS Lambda function on Windows on Arm
    that scans and aggregates IoT data stored in Amazon DynamoDB. You will create a Lambda function
    in the AWS console using the Node.js 20.x runtime, implement the handler as an ES module (index.mjs)
    to scan a table (SensorReadings) and compute an average temperature value, then deploy and
    invoke a test event to view results. The path assumes your DynamoDB table already contains
    records written by an IoT emulator from a prior exercise. Prerequisites include a Windows
    on Arm computer or VM, a code editor such as Visual Studio Code for Arm64, and completion
    of the earlier Windows on Arm and AWS IoT Core Learning Path. Estimated time: 45 minutes.
  faqs:
  - question: What do I need before running these steps?
    answer: >-
      You need a Windows on Arm computer (for example, a Lenovo ThinkPad X13s running Windows
      11 or a Windows on Arm virtual machine), any code editor such as Visual Studio Code for
      Arm64, and completion of the “Create IoT applications with Windows on Arm and AWS IoT Core”
      Learning Path.
  - question: Which options should I choose when creating the Lambda function?
    answer: >-
      In the AWS Lambda console, select Create function, choose Author from scratch, set the Function
      name to GetAverageTemperature, and select Node.js 20.x as the runtime.
  - question: Where do I add the code and what file name should I use?
    answer: >-
      Paste the code in the Code source section under index.mjs. The .mjs extension indicates
      the Lambda entry file is an ECMAScript (ES) module.
  - question: How do I populate data and test the function?
    answer: >-
      Launch the IoT emulator to write data to your DynamoDB table, then click Deploy in the function
      dashboard. Click Test, create a test event named Test, and run it to see execution status
      and the average temperature in the console.
  - question: What should I check if the function returns no average or errors?
    answer: >-
      Verify the DynamoDB table SensorReadings exists in the eu-central-1 region and contains
      items with a temperature attribute. Also confirm you completed the prior steps that write
      records to the table.
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
    - Visual Studio Code

further_reading:
    - resource:
        title: AWS Lambda
        link: https://aws.amazon.com/lambda/
        type: website
    - resource:
        title: Amazon DynamoDB
        link: https://aws.amazon.com/dynamodb/
        type: website
    - resource:
        title: Overview of Amazon Web Services
        link: https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

