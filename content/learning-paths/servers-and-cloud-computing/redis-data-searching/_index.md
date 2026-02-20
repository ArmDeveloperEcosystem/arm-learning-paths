---
title: Deploy Redis for data searching on Google Cloud C4A 

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Redis-based data searching workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install Redis on a SUSE Arm64 (C4A) instance
  - Verify Redis functionality by running the server and performing baseline data insertion and retrieval tests on the Arm64 VM  
  - Measure Redis SET (write) and GET (read) performance using the official redis-benchmark tool to evaluate throughput and latency on Arm64 (AArch64)

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Redis](https://redis.io/) 

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Redis
  - redis-benchmark

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
      title: Redis documentation
      link: https://redis.io/docs/
      type: documentation

  - resource:
      title: Redis benchmark documentation
      link: https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
