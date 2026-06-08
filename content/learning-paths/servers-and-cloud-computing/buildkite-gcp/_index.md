---
title: Create multi-architecture Docker images with Buildkite on Google Axion
description: Learn how to configure Buildkite agents on Google Axion C4A VMs to build and publish multi-architecture Docker images using Docker Buildx for Arm and x86 platforms.

minutes_to_complete: 40

who_is_this_for: This is an introductory topic for developers who want to build and run multi-architecture Docker images with Buildkite on Arm-based Google Cloud C4A virtual machines (VM) powered by Google Axion processors.

learning_objectives:
- Provision an Arm-based VM on Google Cloud running either SUSE Linux Enterprise Server or Ubuntu
- Install and configure Docker, Docker Buildx, and the Buildkite agent
- Write a Dockerfile to containerize a simple Flask-based Python application
- Configure a Buildkite pipeline to build a multi-architecture Docker image and push it to Docker Hub
- Start the application and verify that it runs correctly

prerequisites:
  - A [Google Cloud Platform (GCP) account](https://cloud.google.com/free?utm_source=google&hl=en) with billing enabled
  - Basic Linux system administration skills, including how to create users, install packages, and manage services
  - Familiarity with [Docker](https://docs.docker.com/get-started/) and container concepts
  - A [GitHub account](https://github.com/join) to host your application repository

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:27:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4bda206717eef380430009f859826d9bcf820442d13492cd3c22a114561e2917
  summary_generated_at: '2026-06-02T03:15:44Z'
  summary_source_hash: 4bda206717eef380430009f859826d9bcf820442d13492cd3c22a114561e2917
  faq_generated_at: '2026-06-03T00:27:49Z'
  faq_source_hash: 4bda206717eef380430009f859826d9bcf820442d13492cd3c22a114561e2917
  summary: >-
    This Learning Path shows how to use Buildkite on Arm-based Google Axion C4A virtual machines
    to build and publish multi-architecture Docker images. You will provision a c4a-standard-4
    VM on Google Cloud running Ubuntu or SUSE Linux Enterprise Server, install Docker, Docker
    Buildx, and the Buildkite agent, and create a simple Flask-based Python application with a
    Dockerfile. You then configure a Buildkite pipeline to produce a multi-architecture image
    for Arm and x86 and push it to Docker Hub, before starting the application and verifying it
    runs. Prerequisites include a GCP account with billing enabled, a GitHub account, basic Linux
    administration skills, and familiarity with Docker. Estimated time to complete is about 40
    minutes.
  faqs:
  - question: What do I need before provisioning the Google Axion C4A VM?
    answer: >-
      You need a Google Cloud Platform account with billing enabled, basic Linux administration
      skills, familiarity with Docker, and a GitHub account to host your repository. These are
      the only explicit prerequisites listed.
  - question: Which instance type and operating systems does this path use?
    answer: >-
      The steps use a c4a-standard-4 instance with 4 vCPUs and 16 GB of memory in the Google Cloud
      Console. The VM can run either Ubuntu or SUSE Linux Enterprise Server.
  - question: How do I install the Buildkite agent on the C4A VM?
    answer: >-
      Update packages and install the listed prerequisites using your distribution’s package manager
      (apt on Ubuntu, zypper on SUSE), then run the provided one-line Buildkite installer. The
      path shows the exact commands for each supported distribution.
  - question: How do I know my Buildkite agent is ready to run jobs?
    answer: >-
      Create an agent token in your Buildkite organization, configure the agent with that token,
      and assign it to a queue. In the Buildkite UI, verify the agent shows as online and is listed
      in the configured queue.
  - question: What does the pipeline build and where is it published?
    answer: >-
      The pipeline uses Docker Buildx to build a multi-architecture Docker image for Arm and x86
      from your Flask app’s Dockerfile and then pushes it to Docker Hub. The repository contains
      the Dockerfile and app.py used by the build.
# END generated_summary_faq

author: Jason Andrews

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Buildkite
  - Docker
  - Docker Buildx

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Buildkite documentation
      link: https://buildkite.com/docs
      type: documentation

  - resource:
      title: Docker documentation
      link: https://docs.docker.com/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

