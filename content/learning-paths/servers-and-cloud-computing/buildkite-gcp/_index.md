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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:39:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4bda206717eef380430009f859826d9bcf820442d13492cd3c22a114561e2917
  summary_generated_at: '2026-06-30T21:39:35Z'
  summary_source_hash: 4bda206717eef380430009f859826d9bcf820442d13492cd3c22a114561e2917
  faq_generated_at: '2026-06-30T21:39:35Z'
  faq_source_hash: 4bda206717eef380430009f859826d9bcf820442d13492cd3c22a114561e2917
  summary: >-
    You'll provision an Arm-based Google Cloud C4A virtual machine powered by Google
    Axion, install Docker, Docker Buildx, and the Buildkite agent, and connect the agent to a
    Buildkite queue. First, you'll create a small Flask application and Dockerfile in a GitHub repository,
    then configure a Buildkite pipeline that uses Buildx to build a multi-architecture container
    image, and push it to Docker Hub. You'll use Ubuntu or SUSE on the VM
    and validate that the agent is online. By the end, you'll have a published
    image and a running Flask service to confirm the build.
  faqs:
  - question: Which Google Cloud instance type and OS should I use for the VM?
    answer: >-
      Use a Google Axion C4A Arm VM, specifically `c4a-standard-4` with 4 vCPUs and 16
      GB memory. You can select either Ubuntu or SUSE Linux Enterprise Server as the OS.
  - question: Where do I create the Buildkite agent token, and when do I use it?
    answer: >-
      Create an agent token in your Buildkite organization after signing in (GitHub sign-in is
      supported). You use this token during the agent installation and configuration on the C4A
      VM.
  - question: How do I confirm the Buildkite agent is connected and assigned to the right queue?
    answer: >-
      After configuring the agent and queue, check the Agents page in Buildkite; the agent should
      appear online with the expected queue. If it doesn't, check the agent configuration and
      queue name, then repeat the verification step.
  - question: What files should my GitHub repository contain for the example application?
    answer: >-
      Add a Dockerfile and a Python file named `app.py`. The provided Dockerfile uses `python:3.12-slim`,
      installs Flask, exposes port 5000, and runs the app.
  - question: What result should I expect after the pipeline runs successfully?
    answer: >-
      A multi-architecture Docker image for Arm and x86 is built with Docker Buildx and pushed
      to Docker Hub. You then start the containerized Flask application and verify that it runs
      as the final validation step.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

