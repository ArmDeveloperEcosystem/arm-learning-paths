---
title: Deploy Ruby on Rails on Arm-based Google Cloud C4A virtual machines

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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:59Z'
  generator: template
  source_hash: 092602df259461e2b22dbf0909a682fbacd59464eea38ab901f38cd0b8c6efd3
  summary: >-
    Deploy Ruby on Rails on Arm-based Google Cloud C4A virtual machines walks you through an end-to-end
    Arm software workflow. It is designed for developers deploying and optimizing Ruby on Rails
    workloads in Linux Arm64 environments, specifically using Google Cloud C4A virtual machines
    powered by Axion processors. By the end, you will be able to provision an Arm-based SUSE SLES
    (SUSE Linux Enterprise Server) virtual machine on Google Cloud (C4A with Axion processors),
    install Ruby on Rails on a SUSE Arm64 (C4A) instance, and validate Ruby on Rails functionality
    using PostgreSQL as the database. It focuses on tools and technologies such as Ruby, Rails,
    and PostgreSQL, Linux environments, Arm platforms including Neoverse, and cloud platforms
    such as Google Cloud. The main steps cover Get started with Ruby on Rails on Google Axion
    C4A, Create a Google Axion C4A Arm virtual machine on GCP, Install Ruby on Rails on SUSE Linux,
    Set up Ruby on Rails baseline testing, and Benchmark Ruby on Rails.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE SLES (SUSE Linux Enterprise Server) virtual machine
      on Google Cloud (C4A with Axion processors), install Ruby on Rails on a SUSE Arm64 (C4A)
      instance, and validate Ruby on Rails functionality using PostgreSQL as the database.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers deploying and optimizing Ruby on Rails workloads
      in Linux Arm64 environments, specifically using Google Cloud C4A virtual machines powered
      by Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with Ruby programming, the Rails framework,
      and the [PostgreSQL Relational Database](https://www.postgresql.org/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Ruby, Rails, and PostgreSQL, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Ruby on Rails on Google Axion C4A,
      Create a Google Axion C4A Arm virtual machine on GCP, Install Ruby on Rails on SUSE Linux,
      Set up Ruby on Rails baseline testing, and Benchmark Ruby on Rails.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - Google Cloud

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

