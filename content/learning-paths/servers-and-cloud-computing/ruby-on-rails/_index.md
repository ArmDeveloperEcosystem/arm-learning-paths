---
title: Deploy Ruby on Rails on Google Cloud C4A (Arm-based Axion VMs)

minutes_to_complete: 40

who_is_this_for: This is an introductory topic for developers deploying and optimizing Ruby on Rails workloads in Linux Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES (SUSE Linux Enterprise Server) virtual machine on Google Cloud (C4A with Axion processors)
  - Install Ruby on Rails on a SUSE Arm64 (C4A) instance
  - Validate Ruby on Rails functionality using PostgreSQL as the database  
  - Benchmark Rails performance using the built-in Ruby Benchmark library on Arm64 (Aarch64) architecture


prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Ruby programming, the Rails framework, and the [PostgreSQL Relational Database](https://www.postgresql.org/)

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Ruby
  - Rails
  - PostgreSQL

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
      title: Ruby on Rails documentation
      link:  https://guides.rubyonrails.org/
      type: documentation

  - resource:
      title: Ruby built-in Benchmark documentation
      link: https://github.com/ruby/benchmark?tab=readme-ov-file#benchmark
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
