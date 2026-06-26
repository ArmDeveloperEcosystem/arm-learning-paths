---
title: Deploy containers on Arm-based compute using Amazon ECS and the AWS CDK
description: Learn how to define and deploy a containerized application on Arm-based compute using the AWS Cloud Development Kit.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to use the AWS Cloud Development Kit (AWS CDK) to deploy containerized applications on Arm-based AWS infrastructure.

learning_objectives:
    - Create an example AWS CDK application in JavaScript
    - Define AWS infrastructure using the AWS CDK
    - Deploy application resources on Arm-based AWS compute using Amazon ECS and the AWS CDK

prerequisites:
    - An Amazon Web Services (AWS) account 
    - A local computer with the AWS CLI, AWS CDK CLI, and Node.js installed, with AWS credentials configured.
    - Familiarity with the Linux command line and JavaScript

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:36:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 99f9659f6db887c7389e8cd69e67a5872d738fa72f21b9697a1abe1865808ee1
  summary_generated_at: '2026-06-26T17:36:00Z'
  summary_source_hash: 99f9659f6db887c7389e8cd69e67a5872d738fa72f21b9697a1abe1865808ee1
  faq_generated_at: '2026-06-26T17:36:00Z'
  faq_source_hash: 99f9659f6db887c7389e8cd69e67a5872d738fa72f21b9697a1abe1865808ee1
  summary: >-
    In this Learning Path, you define and deploy a containerized application to Arm-based AWS
    compute using the AWS Cloud Development Kit (CDK). You create a JavaScript CDK application
    that provisions an Amazon ECS service running on Arm-based AWS Fargate. The workflow covers
    synthesizing the application to a CloudFormation template, reviewing the generated output
    in `cdk.out/ArmCdkAppStack.template.json`, bootstrapping the environment, and deploying the
    stack. By following the steps, your infrastructure and service definition target Arm-based
    compute powered by AWS Graviton, using the CDK to manage application resources end-to-end.
    The hands-on flow emphasizes building the app, translating it to infrastructure as code, and
    deploying it with CDK conventions.
  faqs:
  - question: How do I confirm the AWS CDK CLI is installed before starting?
    answer: >-
      Run `cdk --version`. A version string should print to the terminal.
  - question: From which directory should I run the synthesis step?
    answer: >-
      Run the synthesis command from the project directory created for the sample CDK app. The
      generated template appears under `cdk.out`.
  - question: What file should be produced after synthesis, and where is it located?
    answer: >-
      You should see a CloudFormation template named `cdk.out/ArmCdkAppStack.template.json`. This
      is the synthesized output the CDK uses for deployment.
  - question: Do I need to bootstrap before deploying the stack?
    answer: >-
      Yes. After synthesis, bootstrap the environment so the CDK can create required deployment
      resources. When bootstrapping completes without errors, proceed to deploy.
  - question: How do I know the ECS service is configured for Arm-based AWS Fargate?
    answer: >-
      The sample CDK application defines an ECS service running on Arm-based AWS Fargate compute.
      Use the provided definitions and deploy the stack to apply those settings.
# END generated_summary_faq

author: Anupras Mohapatra
generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - AWS CDK CLI
    - Amazon Elastic Container Service (Amazon ECS)
    - AWS CLI
    - Node.js
    - JavaScript

further_reading:
    - resource:
        title: AWS CDK Developer Guide
        link: https://docs.aws.amazon.com/cdk/v2/guide/home.html
        type: documentation
    - resource:
        title: AWS CDK CLI install guide
        link: /install-guides/aws-cdk/
        type: install-guide
    - resource:
        title: AWS CLI install guide
        link: /install-guides/aws-cli/
        type: install-guide
    - resource:
        title: Amazon ECS task definitions for 64-bit Arm workloads
        link: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-arm64.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
