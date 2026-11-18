---
title: Deploy AWS Lambda functions on AWS Graviton processors

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers who want to learn how to deploy Lambda functions on AWS Graviton processors.

description: Deploy AWS Lambda functions on Graviton processors using Terraform for Python and Node.js runtimes.

learning_objectives: 
    - Deploy Lambda functions on Graviton processors using Terraform.

prerequisites:
    - A computer with [Terraform](/install-guides/terraform/) and the [AWS CLI](/install-guides/aws-cli/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:24:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4d6150ca14e66aa8a539c3dd47ca49b26b3914e44db6148cdb53121306ffa2f6
  summary_generated_at: '2026-09-15T21:24:22Z'
  summary_source_hash: 4d6150ca14e66aa8a539c3dd47ca49b26b3914e44db6148cdb53121306ffa2f6
  faq_generated_at: '2026-09-15T21:24:22Z'
  faq_source_hash: 4d6150ca14e66aa8a539c3dd47ca49b26b3914e44db6148cdb53121306ffa2f6
  summary: >-
    You'll deploy AWS Lambda functions on Graviton with Terraform. First, you'll define Lambda resources and provide Node.js and Python function
    code. Then, you'll apply
    the Terraform configuration to provision functions, and review the small code and
    configuration changes needed to move between Node.js and Python.
  faqs:
  - question: Which architecture setting targets AWS Graviton for Lambda?
    answer: >-
      Use the `arm64` architecture in your Terraform configuration to target Graviton processors.
  - question: How do I verify that the deployed Lambda function uses Arm64?
    answer: >-
      Open AWS Lambda in the AWS console, select **Functions**, and open your function. In **Runtime
      settings**, verify that the **Architecture** field is listed as `arm64`.
  - question: What file name and handler inputs does the Python example use?
    answer: >-
      Save the Python function as `python_lambda.py`. The handler reads `event["first_name"]` and
      `event["last_name"]` to build the returned message.
  - question: How do I test the Python Lambda function in the AWS console?
    answer: >-
      Open the function's **Test** tab, enter `{"first_name": "Arm-", "last_name": "user"}` in
      the **Event JSON** field, and select **Test**. You should see the same output as when you run the
      function with Terraform.
  - question: What result should I expect after applying Terraform?
    answer: >-
      Terraform creates a Lambda function configured to run on arm64. When invoked with the expected
      inputs, the example returns a greeting message.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - AWS Graviton

armips:
    - Neoverse
tools_software_languages:
    - Terraform
    - AWS Lambda

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: AWS Lambda Function Manual
        link: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
        type: documentation
    - resource:
        title: AWS Lambda Getting Started
        link: https://aws.amazon.com/lambda/getting-started/
        type: documentation
    - resource:
        title: AWS Lambda performance with Java 21
        link: https://community.aws/content/2juXXgrDDaUdmi902LHwilBhvNU/aws-lambda-performance-with-java-21-x86-vs-arm64-part-1-initial-measurements-and-comparisons?lang=en
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
