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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:17Z'
  generator: template
  source_hash: 4bda206717eef380430009f859826d9bcf820442d13492cd3c22a114561e2917
  summary: >-
    Learn how to configure Buildkite agents on Google Axion C4A VMs to build and publish multi-architecture
    Docker images using Docker Buildx for Arm and x86 platforms. It is designed for developers
    who want to build and run multi-architecture Docker images with Buildkite on Arm-based Google
    Cloud C4A virtual machines (VM) powered by Google Axion processors. By the end, you will be
    able to provision an Arm-based VM on Google Cloud running either SUSE Linux Enterprise Server
    or Ubuntu, install and configure Docker, Docker Buildx, and the Buildkite agent, and write
    a Dockerfile to containerize a simple Flask-based Python application. It focuses on tools
    and technologies such as Buildkite, Docker, and Docker Buildx, Linux environments, Arm platforms
    including Neoverse, and cloud platforms such as Google Cloud. The main steps cover Discover
    Buildkite on Google Axion C4A instances, Create a Google Axion C4A Arm virtual machine on
    GCP, Install Buildkite on a Google Axion C4A Arm VM, Set up and connect Buildkite agent on
    a Google Axion C4A Arm VM, and Create a Flask app and set up the Buildkite pipeline.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based VM on Google Cloud running either SUSE Linux Enterprise
      Server or Ubuntu, install and configure Docker, Docker Buildx, and the Buildkite agent,
      and write a Dockerfile to containerize a simple Flask-based Python application. Learn how
      to configure Buildkite agents on Google Axion C4A VMs to build and publish multi-architecture
      Docker images using Docker Buildx for Arm and x86 platforms.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers who want to build and run multi-architecture
      Docker images with Buildkite on Arm-based Google Cloud C4A virtual machines (VM) powered
      by Google Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP) account](https://cloud.google.com/free?utm_source=google&hl=en)
      with billing enabled; Basic Linux system administration skills, including how to create
      users, install packages, and manage services; Familiarity with [Docker](https://docs.docker.com/get-started/)
      and container concepts; A [GitHub account](https://github.com/join) to host your application
      repository.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Buildkite, Docker, and Docker Buildx, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Discover Buildkite on Google Axion C4A instances,
      Create a Google Axion C4A Arm virtual machine on GCP, Install Buildkite on a Google Axion
      C4A Arm VM, Set up and connect Buildkite agent on a Google Axion C4A Arm VM, and Create
      a Flask app and set up the Buildkite pipeline.
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

