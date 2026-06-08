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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:20:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ced3882cf8be11a55304d2697f450a2c862a81d87317ab42298148755e9f272c
  summary_generated_at: '2026-06-02T03:08:36Z'
  summary_source_hash: ced3882cf8be11a55304d2697f450a2c862a81d87317ab42298148755e9f272c
  faq_generated_at: '2026-06-03T00:20:41Z'
  faq_source_hash: ced3882cf8be11a55304d2697f450a2c862a81d87317ab42298148755e9f272c
  summary: >-
    This Learning Path shows how to package a multi-architecture container and deploy it to AWS
    Fargate using the AWS Copilot CLI, configured to run on AWS Graviton processors. You will
    containerize an example service, use copilot init to build locally, push the image to Amazon
    ECR, and provision a load balanced web service on Fargate. It explains Copilot’s default amd64
    behavior and where to set the architecture to Arm for Graviton. Prerequisites are an AWS account
    and a local machine with Docker, AWS CLI, and AWS Copilot CLI installed. The guide is applicable
    to Linux and macOS users.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an AWS account and a local environment with Docker, AWS CLI, and the AWS Copilot
      CLI installed. The path targets Linux, and the steps note macOS is also applicable.
  - question: What architecture does Copilot use by default, and how does this affect deploying
      on Graviton?
    answer: >-
      Copilot defaults to amd64. To run on AWS Graviton processors with Fargate, you must explicitly
      set the architecture to Arm as described in the steps.
  - question: How do I deploy the sample service with Copilot?
    answer: >-
      Use the copilot init command shown in the path to build from your Dockerfile, create a Load
      Balanced Web Service, and deploy to an environment. Copilot builds locally, pushes the image
      to Amazon ECR, and provisions the Fargate resources.
  - question: Can I use an existing container image instead of building from a Dockerfile?
    answer: >-
      Yes. Use the --image option instead of --dockerfile, and ensure the image is multi-architecture.
  - question: What result should I expect after a successful deployment?
    answer: >-
      A running service on AWS Fargate with the image stored in Amazon ECR, configured as a Load
      Balanced Web Service. Copilot will have created the required infrastructure in the specified
      environment.
# END generated_summary_faq

author: Jason Andrews

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

