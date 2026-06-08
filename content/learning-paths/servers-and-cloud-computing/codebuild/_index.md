---
title: Build and share Docker images using AWS CodeBuild
description: Learn how to automate Docker image creation for Arm using AWS CodeBuild with GitHub integration and run the images on any Arm system with Docker installed.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers interested in using AWS CodeBuild to automate container build tasks.

learning_objectives:
    - Use a GitHub project and AWS CodeBuild to automate Docker image creation
    - Pull and run the created Docker images on any Arm computer with Docker installed

prerequisites:
    - An [AWS account](/learning-paths/servers-and-cloud-computing/csp/aws/) for accessing AWS cloud services.
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or any Arm server, laptop, or single-board computer running [Docker](/install-guides/docker/) used to run the created images

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:35:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e7ea48aaea0e25f624ea1d77c6252b0e537fdaeca3aacca560d7bc9d103bbbb3
  summary_generated_at: '2026-06-02T03:25:50Z'
  summary_source_hash: e7ea48aaea0e25f624ea1d77c6252b0e537fdaeca3aacca560d7bc9d103bbbb3
  faq_generated_at: '2026-06-03T00:35:39Z'
  faq_source_hash: e7ea48aaea0e25f624ea1d77c6252b0e537fdaeca3aacca560d7bc9d103bbbb3
  summary: >-
    Automate building Arm AArch64 Docker images with AWS CodeBuild using a GitHub project, then
    publish them to Docker Hub and the Amazon ECR Public Gallery and run them on any Arm system
    with Docker installed. The path targets Linux and uses AWS Graviton-backed CodeBuild to create
    images for Arm. You will also validate your runtime environment by checking uname -m returns
    aarch64 and then pull and run the completed images. Prerequisites include an AWS account and
    access to an Arm-based instance or any Arm server, laptop, or single-board computer with Docker
    installed. This advanced, 30‑minute path is aimed at developers comfortable with Docker and
    CI/CD concepts.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an AWS account and an Arm-based system with Docker installed to run the created
      images. The path assumes Linux and mentions prior Docker experience is helpful, but no other
      prerequisites are explicitly listed.
  - question: How do I verify that my machine is Arm AArch64 before running the images?
    answer: >-
      On Linux, run uname -m. The expected output is aarch64; if you see a different result, you
      are not on a 64-bit Arm Linux machine.
  - question: Where will the built Docker images be published?
    answer: >-
      The images are published to the Amazon ECR Public Gallery and Docker Hub. Both images are
      identical.
  - question: When should I pull and run the images on my Arm machine?
    answer: >-
      Wait until the AWS CodeBuild process completes. Once complete, you can pull and run the
      images from either Docker Hub or ECR on any Arm system with Docker installed.
  - question: Do I need a GitHub repository to follow this path?
    answer: >-
      Yes. The path uses a GitHub project integrated with AWS CodeBuild to automate Docker image
      creation.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: CI-CD
cloud_service_providers:
  - AWS

armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Docker
    - AWS CodeBuild

further_reading:
    - resource:
        title: AWS documentation
        link: https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html
        type: documentation
    - resource:
        title: AWS CodeBuild curated Docker images
        link: https://github.com/aws/aws-codebuild-docker-images 
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

