---
title: Deploy AWS services using the Serverless Framework

minutes_to_complete: 30

who_is_this_for: This learning path is for software developers interested in learning how to deploy AWS cloud resources using the Serverless Framework.

learning_objectives: 
    - Identify how to set up Serverless Framework for AWS.
    - Create a project and deploy an AWS Lambda function.    

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11, or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/)  
    - A code editor such as [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:59:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 41edc365bf9e1f9882b7a8859ee32d319af8c306f1f1be9d497aacd1ceb4241f
  summary_generated_at: '2026-11-23T20:59:04Z'
  summary_source_hash: 41edc365bf9e1f9882b7a8859ee32d319af8c306f1f1be9d497aacd1ceb4241f
  faq_generated_at: '2026-11-23T20:59:04Z'
  faq_source_hash: 41edc365bf9e1f9882b7a8859ee32d319af8c306f1f1be9d497aacd1ceb4241f
  summary: You'll deploy an AWS Lambda function from a Windows on Arm machine with the Serverless
    Framework. First, you'll install Node.js, npm, and the Serverless Framework, then configure AWS credentials.
    You'll use the interactive wizard to create a Node.js service, inspect the generated project
    files, and deploy the function. Finally, you'll invoke the `hello` function locally and check
    the deployed function in the AWS console.
  faqs:
  - question: Which template should I select in the Serverless wizard?
    answer: Select **AWS / Node.js / Simple Function** to create the example Lambda service.
  - question: What do I need to set up before deploying to AWS?
    answer: Configure AWS credentials that the Serverless Framework can use for the deployment.
  - question: How do I test the Lambda function?
    answer: Run `serverless invoke local --function hello` and check for a response with `statusCode`
      `200` and the example message.
  - question: Where do I inspect the generated service?
    answer: Open the project directory created by the wizard. Review its files before running
      `serverless deploy`.
  - question: Where can I find the deployed Lambda function?
    answer: After deployment, open the AWS Lambda dashboard in the selected region. In the dashboard, locate
      the function created for your service.
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
    - Windows

further_reading:
    - resource:
        title: Serverless Framework
        link: https://www.serverless.com
        type: website
    - resource:
        title: Serverless Framework documentation
        link: https://www.serverless.com/framework/docs
        type: Documentation
    - resource:
        title: AWS Lambda
        link: https://aws.amazon.com/lambda/
        type: Documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

