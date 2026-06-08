---
title: Use Amazon S3 for your IoT applications running Windows on Arm

description: Learn how to create a static website hosted on Amazon S3 that interacts with AWS Lambda functions to display IoT data from Windows on Arm devices.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers who are interested in using Amazon Web Services (AWS) S3 for hosting their IoT websites.

learning_objectives:
   - Gain familiarity with Amazon S3.
   - Create a static website that interacts with AWS Lambda.   

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).   
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.    
    - Completion of the [Use AWS Lambda for IoT applications](/learning-paths/laptops-and-desktops/win_aws_iot_lambda/) Learning Path.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:24:33Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 32186a4879e98aa113f461d2a2c705dee099404ed2020ef6fdb981a28bb0c0c3
  summary_generated_at: '2026-06-01T22:15:20Z'
  summary_source_hash: 32186a4879e98aa113f461d2a2c705dee099404ed2020ef6fdb981a28bb0c0c3
  faq_generated_at: '2026-06-02T23:24:33Z'
  faq_source_hash: 32186a4879e98aa113f461d2a2c705dee099404ed2020ef6fdb981a28bb0c0c3
  summary: >-
    This Learning Path guides you through hosting a static IoT website on Amazon S3 from a Windows
    on Arm environment. You will create a simple site (index.html, styles.css, index.js), connect
    it to an existing GetAverageTemperature AWS Lambda function by retrieving its Function URL,
    and deploy the site to S3 using AWS CLI v2. The path is intended for advanced developers and
    takes about 30 minutes. Prerequisites include a Windows on Arm computer or virtual machine,
    a code editor (Visual Studio Code for Arm64 is suitable), and prior completion of the Use
    AWS Lambda for IoT applications Learning Path. Tools referenced include Node.js and Visual
    Studio Code.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer or a Windows on Arm virtual machine, a code editor (Visual
      Studio Code for Arm64 is suitable), and completion of the "Use AWS Lambda for IoT applications"
      Learning Path. Node.js is listed among the tools.
  - question: How should I structure the static website files, and what does each file do?
    answer: >-
      Create a folder (for example, IoTPage) with three files: index.html, styles.css, and index.js.
      The HTML defines the page structure, the CSS handles styling, and index.js contains logic
      to fetch data from AWS Lambda and display it on the page.
  - question: Where do I find the AWS Lambda Function URL to use in my website?
    answer: >-
      In the AWS Lambda console, open the GetAverageTemperature function, go to the Configuration
      tab, and select Function URL, then create the Function URL. Ensure the GetAverageTemperature
      function is prepared as described in the related Learning Path that integrates AWS Lambda
      with DynamoDB.
  - question: How do I set up AWS CLI to deploy to Amazon S3?
    answer: >-
      Install AWS CLI version 2, create an AWS CLI user, and generate access keys following the
      AWS CLI authentication tutorial. Run aws configure and provide your access key details,
      then use the CLI to deploy the website to S3.
  - question: How do I know the website is working after deployment?
    answer: >-
      When the site loads, it should call your configured AWS Lambda Function URL and display
      the retrieved IoT data on the page. If no data appears, verify that the Function URL in
      index.js matches the URL shown in the Lambda console.
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
        title: Amazon S3
        link: https://aws.amazon.com/s3/
        type: documentation
    - resource:
        title: Hosting a static website using Amazon S3
        link: https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html
        type: documentation
    - resource:
        title: Developing with Amazon S3
        link: https://docs.aws.amazon.com/AmazonS3/latest/userguide/developing-s3.html
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

