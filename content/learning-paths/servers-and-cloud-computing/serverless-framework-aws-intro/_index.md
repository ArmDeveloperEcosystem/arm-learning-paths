---
title: Deploy AWS services using the Serverless Framework

minutes_to_complete: 30

who_is_this_for: This learning path is for software developers interested in learning how to deploy AWS cloud resources using the Serverless Framework.

learning_objectives: 
    - Learn how to set up Serverless Framework for AWS.
    - Create a project and deploy AWS Lambda function.    

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).   
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.    

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:04:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0a4dd65c6d0c7eb79479217b351e3d6c5b8917512d510283fd4d8387ff1339f5
  summary_generated_at: '2026-06-02T05:08:42Z'
  summary_source_hash: 0a4dd65c6d0c7eb79479217b351e3d6c5b8917512d510283fd4d8387ff1339f5
  faq_generated_at: '2026-06-03T02:04:56Z'
  faq_source_hash: 0a4dd65c6d0c7eb79479217b351e3d6c5b8917512d510283fd4d8387ff1339f5
  summary: >-
    Learn to set up the Serverless Framework on a Windows on Arm system and deploy an AWS Lambda
    function using an introductory, step-by-step workflow. You will install Node.js (version 18.20.3
    or later) and npm, install the Serverless Framework CLI, configure AWS credentials, and use
    the interactive serverless command to create a new service with the AWS / Node.js / Simple
    Function template. The target environment is Windows 11 on Arm hardware or a Windows on Arm
    virtual machine, using any code editor such as Visual Studio Code for Arm64. By the end, you
    will have created a basic Serverless project and deployed a Lambda function to AWS. Prerequisites
    include a Windows on Arm computer, a code editor, and AWS credentials.
  faqs:
  - question: What do I need before running the setup steps?
    answer: >-
      Use a Windows on Arm computer (or Windows on Arm VM) with Windows 11, and install Node.js
      18.20.3 or later with npm. Any code editor works; Visual Studio Code for Arm64 is suitable.
      You also need AWS credentials to deploy to AWS.
  - question: How do I install the Serverless Framework on Windows on Arm?
    answer: >-
      After installing Node.js 18.20.3 or greater, open a terminal or command prompt and run:
      npm install -g serverless. This adds the Serverless Framework globally so you can use the
      serverless command.
  - question: How do I start creating the project and choose the correct template?
    answer: >-
      Run the serverless command in a terminal to start the wizard. Use the arrow keys to select
      the AWS / Node.js / Simple Function template and press Enter.
  - question: What does the wizard generate for me?
    answer: >-
      It scaffolds a new Serverless service configured for a simple Node.js Lambda function targeting
      AWS. You will then proceed to deploy the function as shown in the steps.
  - question: How do I know my AWS credentials are ready for deployment?
    answer: >-
      This path includes configuring AWS credentials, which are required to deploy to AWS. Ensure
      you have valid AWS credentials created and available locally before running the deployment
      steps.
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

