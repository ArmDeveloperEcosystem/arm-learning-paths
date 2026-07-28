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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:31:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 32186a4879e98aa113f461d2a2c705dee099404ed2020ef6fdb981a28bb0c0c3
  summary_generated_at: '2026-07-28T16:31:56Z'
  summary_source_hash: 32186a4879e98aa113f461d2a2c705dee099404ed2020ef6fdb981a28bb0c0c3
  faq_generated_at: '2026-07-28T16:31:56Z'
  faq_source_hash: 32186a4879e98aa113f461d2a2c705dee099404ed2020ef6fdb981a28bb0c0c3
  summary: >-
    You'll build a static website on Windows on Arm and connect it to an existing AWS Lambda Function
    URL. You'll create `index.html`, `styles.css`, and `index.js`, update the JavaScript with the
    endpoint, configure AWS credentials, upload the files to Amazon S3, and verify that the page
    displays IoT data.
  faqs:
  - question: Which files do I need for the static website and what is each one for?
    answer: >-
      Create `index.html` for the page structure, `styles.css` for layout and styling, and `index.js`
      for fetching data from AWS Lambda and updating the page. These three files are the minimum
      required for this path.
  - question: I don’t see a Function URL for my Lambda function—what should I check?
    answer: >-
      Open the GetAverageTemperature function in the AWS Lambda console, go to the Configuration
      tab, and create a Function URL. Make sure the function exists as prepared in the prerequisite
      Learning Path.
  - question: Where do I place the Lambda endpoint in my code?
    answer: >-
      In `index.js`, update the fetch logic to use the Function URL you created for GetAverageTemperature.
      Replace any placeholder with the exact Function URL copied from the Lambda console.
  - question: Which AWS CLI setup does this path use?
    answer: >-
      Use AWS CLI version 2. Run `aws configure` and provide your AWS Access Key ID and AWS Secret
      Access Key as described in the AWS CLI authentication tutorial.
  - question: What result should I expect after deploying to Amazon S3?
    answer: >-
      Loading the site from its S3 endpoint should display `index.html` and show IoT data returned
      by the Lambda function. If data does not appear, confirm that `index.js` points to the correct
      Function URL and that your three files are uploaded.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
