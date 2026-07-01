---
title: How to use AWS Graviton processors on AWS Fargate with Copilot
description: Learn how to package multi-architecture container applications and deploy them on AWS Fargate with Graviton processors using the AWS Copilot CLI.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to learn how to use the command line to deploy Arm containers on AWS Fargate. 

learning_objectives:
    - Package applications using a multi-architecture containers
    - Deploy containers on AWS Fargate with the AWS Copilot CLI
    - Configure Copilot to use AWS Graviton processors

prerequisites:
    - An Amazon Web Services (AWS) account
    - A local computer with Docker, AWS CLI, and AWS Copilot CLI installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:37:56Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ced3882cf8be11a55304d2697f450a2c862a81d87317ab42298148755e9f272c
  summary_generated_at: '2026-06-26T17:37:56Z'
  summary_source_hash: ced3882cf8be11a55304d2697f450a2c862a81d87317ab42298148755e9f272c
  faq_generated_at: '2026-06-26T17:37:56Z'
  faq_source_hash: ced3882cf8be11a55304d2697f450a2c862a81d87317ab42298148755e9f272c
  summary: >-
    You'll package a containerized application and deploy it to AWS Fargate
    using the AWS Copilot CLI, with a focus on targeting AWS Graviton2 processors. First, you'll containerize
    an example app. Then, you'll run Copilot to initialize a Load Balanced Web Service and configure Copilot for the Arm architecture so the service
    runs on Graviton. You'll also use a Dockerfile to build locally or reference an
    existing multi-architecture image and push it to Amazon ECR. By the end, you'll deploy the
    service on Fargate on Arm.
  faqs:
  - question: What happens when I run the `copilot init` command shown in the steps?
    answer: >-
      By default, Copilot builds the container for `amd64` on your local machine, pushes it to Amazon
      ECR, and creates what is needed to run the application on AWS Fargate. The command initializes
      a Load Balanced Web Service and deploys it.
  - question: When should I change Copilot to use the Arm architecture for Graviton?
    answer: >-
      Change the architecture setting before you build and deploy. Copilot defaults to `amd64`,
      and the steps explain how to set it to Arm so the service runs on Graviton.
  - question: Can I deploy a prebuilt container image instead of building from the Dockerfile?
    answer: >-
      Yes. Use the `--image` option instead of `--dockerfile`, and ensure the image is multi-architecture
      and includes an Arm variant for Graviton.
  - question: What should I check if deployment fails at the start?
    answer: >-
      Verify that Docker and the AWS Copilot CLI are installed and available on your system. This
      guide applies to both Linux and macOS users.
  - question: Where does Copilot push the container image during deployment?
    answer: >-
      Copilot pushes the image to Amazon Elastic Container Registry (ECR). You will see the image
      upload occur before the service is provisioned on Fargate.
# END generated_summary_faq

author: Jason Andrews

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
    - Docker

further_reading:
    - resource:
        title: Introducing AWS Copilot
        link: https://aws.amazon.com/blogs/containers/introducing-aws-copilot/
        type: blog
    - resource:
        title: Developing an application based on multiple microservices using AWS Copilot and AWS Fargate
        link: https://aws.amazon.com/blogs/containers/developing-an-application-based-on-multiple-microservices-using-the-aws-copilot-and-aws-fargate/
        type: blog
    - resource:
        title: AWS Copilot Getting started with containers on AWS
        link: https://youtu.be/hBHf241-D2Y?si=ySm0e4VwbgFSoy3s
        type: video

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
