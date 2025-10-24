---
title: Create multi-architecture Docker images with Buildkite on Google Axion

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

author: Jason Andrews

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers: Google Cloud

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
