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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:30:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f5a93346a0fd55659b7c0a6df501db97742ec71755b6443051b654f3ce871cdf
  summary_generated_at: '2026-07-28T16:30:39Z'
  summary_source_hash: f5a93346a0fd55659b7c0a6df501db97742ec71755b6443051b654f3ce871cdf
  faq_generated_at: '2026-07-28T16:30:39Z'
  faq_source_hash: f5a93346a0fd55659b7c0a6df501db97742ec71755b6443051b654f3ce871cdf
  summary: >-
    This Learning Path guides you through building a serverless data-processing flow for IoT workloads
    by implementing an AWS Lambda function that scans a DynamoDB table and computes an aggregate
    value. You create a function in the AWS Lambda console using Node.js 20.x, then add ES module
    code in index.mjs to scan records and calculate the average temperature from sensor readings.
    Learners configure the region, table, and attribute directly in the source, deploy the function,
    and generate data using the referenced IoT emulator. The path concludes with testing in the
    Lambda console and reviewing the execution result to confirm the computed average.
  faqs:
  - question: Which runtime and file should I use for the Lambda function?
    answer: >-
      Select Node.js 20.x as the runtime. Add the code in the Code source editor under index.mjs,
      which indicates an ECMAScript module.
  - question: What needs to be in DynamoDB before I run a test?
    answer: >-
      Ensure the table contains records written by the IoT emulator referenced in the prerequisite
      Learning Path. The example code expects a table named SensorReadings with a numeric temperature
      attribute.
  - question: How do I change the DynamoDB table, attribute, or AWS Region the function uses?
    answer: >-
      Edit TABLE_NAME, ATTRIBUTE_NAME, and the region configured in the DynamoDBClient within
      index.mjs. Save and redeploy the function before testing again.
  - question: Where do I paste the Lambda function code?
    answer: >-
      Scroll to the Code source section of the function and paste the code into index.mjs. The
      .mjs extension designates the file as an ES module.
  - question: What result should I expect after running a test event?
    answer: >-
      The Lambda console shows the execution status and a return value that includes the average
      temperature computed from the scanned items.
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

