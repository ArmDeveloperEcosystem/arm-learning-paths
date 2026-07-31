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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:41:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e7ea48aaea0e25f624ea1d77c6252b0e537fdaeca3aacca560d7bc9d103bbbb3
  summary_generated_at: '2026-07-27T18:41:54Z'
  summary_source_hash: e7ea48aaea0e25f624ea1d77c6252b0e537fdaeca3aacca560d7bc9d103bbbb3
  faq_generated_at: '2026-07-27T18:41:54Z'
  faq_source_hash: e7ea48aaea0e25f624ea1d77c6252b0e537fdaeca3aacca560d7bc9d103bbbb3
  summary: >-
    You'll use AWS CodeBuild and a GitHub repository to build AArch64 Docker images on AWS Graviton.
    You'll publish the images to Docker Hub and Amazon ECR Public Gallery, then pull and run them on an Arm
    Linux machine with Docker. Finally, you'll verify the architecture with `uname -m` and compare the
    images from both registries.
  faqs:
  - question: How do I confirm I’m on an Arm AArch64 machine before running the images?
    answer: >-
      Run `uname -m` on the target Linux system. The expected output is `aarch64`. If you see a different
      value, you're not on a 64-bit Arm machine.
  - question: How do I know the CodeBuild job is finished and images are ready to use?
    answer: >-
      When the CodeBuild project completes successfully, you can pull the images from Docker Hub
      or Amazon ECR Public Gallery and run them on an Arm machine with Docker.
  - question: Which registry should I pull from?
    answer: >-
     Both registries provide the same images. Choose Docker Hub or Amazon ECR Public Gallery based on which registry fits your environment.
  - question: What result should I expect when I run the container to verify the build?
    answer: >-
      Running `uname -m` inside the container should return `aarch64`, and the output should match
      regardless of which registry you used. The example also shows that CodeBuild built the image
      on Amazon Linux 2.
  - question: Do I need to select an Arm or Graviton environment in CodeBuild to target AArch64?
    answer: >-
      Yes. Select an Arm-based environment in CodeBuild to build AArch64 Docker images from a
      GitHub-hosted project.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: CI-CD
platforms:
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
