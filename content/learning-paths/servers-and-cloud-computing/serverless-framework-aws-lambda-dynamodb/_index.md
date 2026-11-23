---
title: Deploy AWS Lambda and DynamoDB using the Serverless Framework

minutes_to_complete: 30

who_is_this_for: This learning path is for software developers interested in learning how to deploy serverless applications using the Serverless Framework and Amazon Web Services. It automates several manual deployment steps that developers typically need to perform when deploying microservice-based or IoT applications.

learning_objectives: 
    - Create a multi-resource Serverless Framework solution.
    - Automate deployment of AWS Lambda function consuming data from DynamoDB.    

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11, or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/)
    - A code editor such as [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user)
    - Completion of [Deploy AWS services using the Serverless Framework](/learning-paths/servers-and-cloud-computing/serverless-framework-aws-intro/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:59:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f0b6c03ff323ba9ef9c1c9a58ac70f458998717883bcd0e9a6af2c868c786e7c
  summary_generated_at: '2026-11-23T20:59:27Z'
  summary_source_hash: f0b6c03ff323ba9ef9c1c9a58ac70f458998717883bcd0e9a6af2c868c786e7c
  faq_generated_at: '2026-11-23T20:59:27Z'
  faq_source_hash: f0b6c03ff323ba9ef9c1c9a58ac70f458998717883bcd0e9a6af2c868c786e7c
  summary: You'll deploy a temperature service with AWS Lambda and DynamoDB using the Serverless
    Framework. First, you'll define a DynamoDB table, two Lambda functions, and their permissions
    in `serverless.yml`. You'll then deploy the service from its project directory and inspect the generated
    API endpoints. Finally, you'll call the POST endpoint to write temperature data, and the GET endpoint
    to retrieve an average value.
  faqs:
  - question: Where do I declare the service resources?
    answer: Edit `serverless.yml` to define the DynamoDB table, the two Lambda functions, and
      the IAM permissions that they need.
  - question: Where do I run the deployment command?
    answer: From the `AwsServerlessDynamoDbLambda` project directory, run `serverless deploy`.
  - question: How do I find the service endpoints?
    answer: After `serverless deploy` completes, inspect its output for the POST `write-temperatures`
      and GET `get-average-temperature` URLs.
  - question: What does each Lambda function do?
    answer: Use the write function to record timestamped, randomly generated temperatures in DynamoDB.
      Use the read function to retrieve their average.
  - question: How do I test the deployed API?
    answer: Send `curl -X POST <YOUR_URL_GOES_HERE>` to the write endpoint, then `curl <YOUR_URL_GOES_HERE>`
      to the read endpoint. Replace each placeholder with the matching URL from the deployment
      output.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Web
platforms:
  - AWS Graviton

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

