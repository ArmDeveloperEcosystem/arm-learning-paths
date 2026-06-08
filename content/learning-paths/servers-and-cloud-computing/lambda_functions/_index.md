---
title: Learn how to deploy AWS Lambda functions

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers who want to learn how to deploy Lambda functions on AWS Graviton processors.

description: Deploy AWS Lambda functions on Graviton processors using Terraform for Python and Node.js runtimes.

learning_objectives: 
    - Deploy Lambda functions on Graviton processors using Terraform

prerequisites:
    - A computer with [Terraform](/install-guides/terraform/) and the [AWS CLI](/install-guides/aws-cli/) installed. 
    

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:20:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 22fa96e29143f2e0dc0c204919422914b3f70d63ddf833cf1067fbf67b525aa0
  summary_generated_at: '2026-06-02T04:15:30Z'
  summary_source_hash: 22fa96e29143f2e0dc0c204919422914b3f70d63ddf833cf1067fbf67b525aa0
  faq_generated_at: '2026-06-03T01:20:35Z'
  faq_source_hash: 22fa96e29143f2e0dc0c204919422914b3f70d63ddf833cf1067fbf67b525aa0
  summary: >-
    This introductory Learning Path shows how to deploy AWS Lambda functions on AWS Graviton processors
    using Terraform. From a Linux host with Terraform and the AWS CLI installed, you will provision
    Lambda functions configured with the arm64 architecture and implement examples in both Node.js
    and Python. The steps demonstrate selecting the runtime, specifying the target architecture
    in Terraform, and reusing the workflow across languages, including a simple Python function
    that assembles a greeting message from event fields. By the end, you will be able to deploy
    Lambda functions on Graviton with Terraform and adapt the same approach for either runtime.
    No other prerequisites are explicitly listed. Estimated time: 30 minutes.
  faqs:
  - question: Which architecture should I select in Terraform to run the function on Graviton?
    answer: >-
      Choose arm64 for the function architecture in your Terraform configuration. This setting
      deploys the Lambda function on Graviton processors.
  - question: What do I need before running the steps?
    answer: >-
      You need a computer with Terraform and the AWS CLI installed. No other explicit prerequisites
      are listed, and the path targets Linux.
  - question: Can I reuse the same deployment approach for Python and Node.js?
    answer: >-
      Yes. Follow the Node.js deployment workflow and, for Python, replace the Node.js code with
      the provided Python Lambda function.
  - question: How do I know the sample Python function is behaving as expected?
    answer: >-
      The Python handler constructs a message using the event’s first_name and last_name fields.
      When invoked with those fields, expect a response containing the formatted greeting.
  - question: What should I check if Terraform deployment does not work as expected?
    answer: >-
      Verify that Terraform and the AWS CLI are installed and accessible. Also confirm that the
      Lambda function architecture is set to arm64 as shown in the path.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS

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

