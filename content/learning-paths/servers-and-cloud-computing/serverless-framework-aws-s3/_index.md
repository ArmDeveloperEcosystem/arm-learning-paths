---
title: Deploy a static website to Amazon S3 and integrate with AWS Lambda and DynamoDB using the Serverless Framework

minutes_to_complete: 60

who_is_this_for: This learning path is for software developers interested in learning how to deploy serverless applications using the Serverless Framework and Amazon Web Services. 

learning_objectives: 
    - Create a multi-resource Serverless Framework solution.
    - Automate deployment of a static website to Amazon S3.    

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).   
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.
    - Completion of the Learning Path that shows you how to [Deploy AWS services using the Serverless Framework](/learning-paths/servers-and-cloud-computing/serverless-framework-aws-intro/).

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:05:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a31c6f9d674bf41cee16066708c884ca587289e181b7754ff75cdbd85bdb30e3
  summary_generated_at: '2026-06-02T05:10:00Z'
  summary_source_hash: a31c6f9d674bf41cee16066708c884ca587289e181b7754ff75cdbd85bdb30e3
  faq_generated_at: '2026-06-03T02:05:45Z'
  faq_source_hash: a31c6f9d674bf41cee16066708c884ca587289e181b7754ff75cdbd85bdb30e3
  summary: >-
    Build and deploy a multi-resource serverless application on AWS using the Serverless Framework.
    You will declare a service that provisions an Amazon S3 bucket to host a static website, a
    DynamoDB table for sample sensor data, two AWS Lambda functions (one to write temperatures
    and one to return an average), and the required IAM role. You will add website files (including
    index.html) under your Serverless project and deploy the stack using Serverless Framework
    commands. This introductory path targets developers using Windows on Arm and assumes completion
    of the introductory Serverless Framework on AWS Learning Path. Estimated time to complete
    is about 60 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Have a Windows on Arm computer or a Windows on Arm virtual machine, a code editor such as
      Visual Studio Code for Arm64, and completion of the Learning Path on deploying AWS services
      with the Serverless Framework. This path uses Node.js and npm.
  - question: Where should I create the website files?
    answer: >-
      Create a subfolder under the folder where you created the serverless project (for example,
      AwsServerlessDynamoDbLambdaS3). Inside that website folder, create index.html as shown in
      the steps.
  - question: Which AWS resources does the service declare and deploy?
    answer: >-
      A DynamoDB table for hypothetical sensor data, two AWS Lambda functions (one writes temperatures,
      the other retrieves the average), an IAM role granting the functions access to the table,
      and an S3 bucket to host the static website.
  - question: From which directory and with which commands do I deploy?
    answer: >-
      Open a terminal and navigate to the AwsServerlessDynamoDbLambda folder. Run npm install
      --save-dev serverless, then run serverless deploy.
  - question: What result should I expect after deployment?
    answer: >-
      You should see packaging and deployment logs, including a line like "Deploying 'AwsServerlessDynamoDbLambdaS3'
      to stage 'dev' (us-east-1)". This indicates the service and its AWS resources were deployed.
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

