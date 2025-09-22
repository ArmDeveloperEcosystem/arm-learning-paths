---
title: Multi-Architecture Docker Builds with Buildkite on Arm-based GCP C4A Axion VMs

minutes_to_complete: 40

who_is_this_for: This is an introductory guide for software developers learning to build and run multi-architecture Docker images with Buildkite on Arm-based Google Cloud C4A virtual machines powered by Axion processors.


learning_objectives:
- Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
- Install and configure Docker, Buildx, and the Buildkite agent
- Write a Dockerfile to containerize a simple Flask-based Python application
- Configure a Buildkite pipeline to build multi-architecture Docker images and push them to DockerHub
- Run and validate the application to ensure it works as expected


prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled (or another supported cloud provider like Azure or AWS)
  - Basic knowledge of Linux system administration (creating users, installing packages, managing services)
  - Familiarity with [Docker](https://docs.docker.com/get-started/) and container concepts
  - A [GitHub](https://github.com/) account to host your application repository
  - Familiarity with [Buildkite concepts](https://buildkite.com/docs/tutorials/getting-started) such as agents, pipelines, secrets, and queues


author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Buildkite
  - Docker
  - Buildx

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
