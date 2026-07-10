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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T17:14:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 251b6edf6a016f9fc73eb35216f56b2001465fbca8253bd7b6e6f9f4afcd25e6
  summary_generated_at: '2026-07-02T17:14:08Z'
  summary_source_hash: 251b6edf6a016f9fc73eb35216f56b2001465fbca8253bd7b6e6f9f4afcd25e6
  faq_generated_at: '2026-07-02T17:14:08Z'
  faq_source_hash: 251b6edf6a016f9fc73eb35216f56b2001465fbca8253bd7b6e6f9f4afcd25e6
  summary: >-
    You'll extend Arm Virtual Hardware (AVH) integration by preparing an AWS account with a CloudFormation
    stack and connecting it to a forked GitHub repository that runs automated build and validation
    on AVH. First, you'll fork the `ARM-software/AVH-GetStarted` project, deploy the
    included CloudFormation template, and configure GitHub Actions with repository secrets. The
    settings include the AWS region used by the stack and a valid VPC subnet ID obtained from
    the AWS console. After configuration, you'll run the workflow in GitHub Actions to drive
    tests on AVH, providing a clear sequence from account setup to automated
    validation.
  faqs:
  - question: How do I get the example project used in this workflow?
    answer: >-
      Fork the [repository](https://github.com/ARM-software/AVH-GetStarted/fork) and clone your
      fork. The example includes a template to help set up your AWS account and documentation
      for the CI workflow.
  - question: What do I need to complete in AWS before adding GitHub secrets?
    answer: >-
      Deploy the CloudFormation stack using the template provided in the example project. After
      creating the stack, proceed to define the repository secrets in GitHub.
  - question: Which value should I use for `AWS_DEFAULT_REGION`?
    answer: >-
      Use the same AWS Region where you created the CloudFormation stack. The region must match
      for the workflow to reference the correct resources.
  - question: How do I find the `AWS_SUBNET_ID` required by the workflow?
    answer: >-
      In the AWS console, go to **VPC > Subnets** and select any valid Subnet ID. Copy that ID into
      the `AWS_SUBNET_ID` repository secret.
  - question: Where do I add the required secrets in GitHub, and do names matter?
    answer: >-
      In your forked repository, go to **Settings > Secrets > Actions**, then choose **New repository
      secret**. The secret names must match exactly as specified in the Learning Path.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

