---
title: Deploy an S3 site with Lambda and DynamoDB using Serverless Framework

minutes_to_complete: 60

who_is_this_for: This learning path is for software developers interested in learning how to deploy serverless applications using the Serverless Framework and Amazon Web Services. 

learning_objectives: 
    - Create a multi-resource Serverless Framework solution.
    - Automate deployment of a static website to Amazon S3.    

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11, or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/)  
    - A code editor such as [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user)
    - Completion of the [Deploy AWS services using the Serverless Framework](/learning-paths/servers-and-cloud-computing/serverless-framework-aws-intro/) Learning Path

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:59:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 59aef978f93bf194e21903d53992f072568d6d4f519a54c5592c775751c6ee4b
  summary_generated_at: '2026-11-23T20:59:58Z'
  summary_source_hash: 59aef978f93bf194e21903d53992f072568d6d4f519a54c5592c775751c6ee4b
  faq_generated_at: '2026-11-23T20:59:58Z'
  faq_source_hash: 59aef978f93bf194e21903d53992f072568d6d4f519a54c5592c775751c6ee4b
  summary: You'll deploy a static website backed by AWS Lambda and DynamoDB with the Serverless Framework.
    First, you'll define the table, functions, permissions, and S3 website resources. You'll add the
    site HTML and assets, then deploy the service. After deployment, you'll run `serverless info
    --verbose` to find `WebsiteURL`. Finally, you'll open the site and use its buttons to write temperature
    records and retrieve an average.
  faqs:
  - question: Where do I run the deployment commands?
    answer: From the service project directory, run `npm install --save-dev` to install the declared
      dependencies, then run `serverless deploy`. Use the directory containing the
      `serverless.yml` for the service.
  - question: Where do I place the website files?
    answer: Create the `website` subdirectory inside the service project. Add `index.html`
      and the `styles.css` file there.
  - question: Where do I find the website address?
    answer: After `serverless deploy`, run `serverless info --verbose` and look for `WebsiteURL`
      in **Stack Outputs**. Open that URL to view the S3 website.
  - question: What does the IAM role allow the functions to do?
    answer: The IAM role gives the Lambda functions DynamoDB permissions. One function can write temperature records to the table, and the other can read them.
  - question: How do I test the deployed website?
    answer: Open `WebsiteURL`, select **Write Temperatures**, then select **Get Average Temperature**.
      Check that the average appears on the page.
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

