---
title: Integrate Arm Virtual Hardware into CI/CD workflow 2

description: Learn how to integrate Arm Virtual Hardware with AWS and GitHub Actions for automated CI/CD workflows, including CloudFormation setup and test automation.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for DevOps integrating AVH into their CI/CD flows

learning_objectives: 
    - Prepare AWS account for GitHub integration
    - Integrate Arm Virtual Hardware into CI/CD flow with GitHub Actions

prerequisites:
    - This learning path builds on [Integrate Arm Virtual Hardware into CI/CD workflow 1](/learning-paths/cross-platform/avh_cicd/).
    - Valid AWS and GitHub accounts are required

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:32:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 251b6edf6a016f9fc73eb35216f56b2001465fbca8253bd7b6e6f9f4afcd25e6
  summary_generated_at: '2026-06-01T21:01:44Z'
  summary_source_hash: 251b6edf6a016f9fc73eb35216f56b2001465fbca8253bd7b6e6f9f4afcd25e6
  faq_generated_at: '2026-06-02T21:32:39Z'
  faq_source_hash: 251b6edf6a016f9fc73eb35216f56b2001465fbca8253bd7b6e6f9f4afcd25e6
  summary: >-
    This advanced Learning Path shows how to integrate Arm Virtual Hardware with AWS and GitHub
    Actions to automate test and validation for bare-metal Cortex-M projects. You will fork the
    ARM-software/AVH-GetStarted repository, use its included CloudFormation template to prepare
    your AWS account, and configure repository secrets so GitHub Actions can run an automated
    build-and-validation example on Arm Virtual Hardware. The steps focus on setting up AWS integration
    (including region and subnet) and connecting the example CI workflow in your fork. It builds
    on “Integrate Arm Virtual Hardware into CI/CD workflow 1” and requires valid AWS and GitHub
    accounts. Estimated time to complete is approximately 30 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      It builds on “Integrate Arm Virtual Hardware into CI/CD workflow 1” and requires valid AWS
      and GitHub accounts. No other prerequisites are explicitly listed.
  - question: Which example repository should I use and where do I find it?
    answer: >-
      Fork the Arm example at https://github.com/ARM-software/AVH-GetStarted/fork. It includes
      a CloudFormation template and documentation for the CI workflow.
  - question: When is my AWS account ready to connect to GitHub Actions?
    answer: >-
      After completing the CloudFormation stack step in “Prepare AWS account for GitHub integration.”
      Once that is done, proceed to define the GitHub repository secrets.
  - question: Which GitHub Actions secrets must I create and how do I find their values?
    answer: >-
      Create the secrets exactly as named in the Learning Path. Set AWS_DEFAULT_REGION to the
      same region where the CloudFormation stack was created, and set AWS_SUBNET_ID by selecting
      any valid Subnet ID from AWS Console > VPC > Subnets.
  - question: What result should I expect after configuring the workflow?
    answer: >-
      The GitHub Actions pipeline will automate build, test, and validation of the example on
      Arm Virtual Hardware. You should see the example run under CI using your AWS configuration.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Advanced
subjects: CI-CD
armips:
    - Cortex-M
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Virtual Hardware
    - GitHub

### Cross-platform metadata only
shared_path: true
shared_between:
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: GitHub Actions
        link: https://docs.github.com/en/actions
        type: documentation
    - resource:
        title: Arm Virtual Hardware
        link: https://arm-software.github.io/AVH/main/examples/html/GetStarted.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

