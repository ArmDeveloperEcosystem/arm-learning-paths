---
title: Deploy and integrate AWS Lambda with DynamoDB using the Serverless Framework

minutes_to_complete: 30

who_is_this_for: This learning path is for software developers interested in learning how to deploy serverless applications using the Serverless Framework and Amazon Web Services. It automates several manual deployment steps that developers typically need to perform when deploying microservice-based or IoT applications.

learning_objectives: 
    - Create a multi-resource Serverless Framework solution.
    - Automate deployment of AWS Lambda function consuming data from DynamoDB.    

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).   
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.
    - Completion of [Deploy AWS services using the Serverless Framework](/learning-paths/servers-and-cloud-computing/serverless-framework-aws-intro/).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:05:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2120b6bedf6ea5ae02d8b353a6485f307bcb39d0055c29d9e8a39df37a8b946e
  summary_generated_at: '2026-06-02T05:09:22Z'
  summary_source_hash: 2120b6bedf6ea5ae02d8b353a6485f307bcb39d0055c29d9e8a39df37a8b946e
  faq_generated_at: '2026-06-03T02:05:18Z'
  faq_source_hash: 2120b6bedf6ea5ae02d8b353a6485f307bcb39d0055c29d9e8a39df37a8b946e
  summary: >-
    Learn to define and deploy a small AWS serverless application that integrates AWS Lambda with
    DynamoDB using the Serverless Framework. You will declare a service that provisions a DynamoDB
    table for sample sensor data, two Lambda functions (one to write temperatures and one to return
    an average), and an IAM role with the necessary read/write permissions, then deploy everything
    with a single serverless deploy command. This introductory path takes about 30 minutes. Prerequisites
    include a Windows on Arm computer or Windows on Arm virtual machine, a code editor such as
    Visual Studio Code for Arm64, and completion of the prior Serverless Framework on AWS Learning
    Path. The path uses Node.js and Visual Studio Code.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use a Windows on Arm computer or a Windows on Arm virtual machine, and have a code editor;
      Visual Studio Code for Arm64 is suitable. Complete the “Deploy AWS services using the Serverless
      Framework” Learning Path first. This path uses Node.js and Visual Studio Code.
  - question: Which AWS resources does this service create?
    answer: >-
      It creates a DynamoDB table to store timestamps and randomly generated temperatures, two
      AWS Lambda functions, and an IAM role. One Lambda writes temperature data to the table,
      and the other retrieves the average temperature.
  - question: Which command do I use to deploy and where should I run it?
    answer: >-
      Run serverless deploy from a terminal in the AwsServerlessDynamoDbLambda directory. The
      Serverless Framework will validate your serverless.yml and deploy the declared resources
      to AWS.
  - question: What result should I expect after running the deploy command?
    answer: >-
      The deploy command should complete without errors and provision the DynamoDB table, Lambda
      functions, and IAM role as defined in serverless.yml. The framework handles the orchestration
      of these resources for you.
  - question: What should I check if deployment fails?
    answer: >-
      Confirm you are in the AwsServerlessDynamoDbLambda folder and that your service is declared
      as described. Ensure your serverless.yml is valid and that you have completed the prerequisite
      Learning Path.
# END generated_summary_faq

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - AWS

armips:
    - Neoverse
    
tools_software_languages:
    - Node.js
    - Visual Studio Code

operatingsystems:
    - Linux
    - Windows
    - macOS


further_reading:
    - resource:
        title: Terraform on Azure
        link: /learning-paths/servers-and-cloud-computing/azure-terraform/
        type: Tutorial
    - resource:
        title: Azure Virtual Machines with Ampere Altra Arm–based processors—generally available
        link: https://azure.microsoft.com/en-us/blog/azure-virtual-machines-with-ampere-altra-arm-based-processors-generally-available/
        type: Blog
    - resource:
        title: About Azure bastion
        link: https://learn.microsoft.com/en-us/azure/bastion/bastion-overview
        type: Documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

