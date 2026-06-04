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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:03:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 092602df259461e2b22dbf0909a682fbacd59464eea38ab901f38cd0b8c6efd3
  summary_generated_at: '2026-06-02T05:06:21Z'
  summary_source_hash: 092602df259461e2b22dbf0909a682fbacd59464eea38ab901f38cd0b8c6efd3
  faq_generated_at: '2026-06-03T02:03:26Z'
  faq_source_hash: 092602df259461e2b22dbf0909a682fbacd59464eea38ab901f38cd0b8c6efd3
  summary: >-
    This Learning Path guides you through deploying Ruby on Rails on Arm-based Google Cloud C4A
    virtual machines powered by Axion processors. You will provision a SUSE Linux Enterprise Server
    instance—illustrated with the c4a-standard-4 type via Google Cloud Console—install Ruby, Rails,
    and supporting packages, and set up PostgreSQL including development headers required by the
    pg gem. You will validate a Rails app’s connectivity to PostgreSQL and run Ruby’s built-in
    Benchmark library to measure execution time for inserts, queries, and CPU tasks on Arm64.
    Prerequisites are a Google Cloud Platform account with billing enabled and basic familiarity
    with Ruby, Rails, and PostgreSQL. Estimated time to complete is about 40 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Google Cloud Platform (GCP) account with billing enabled. Basic familiarity with
      Ruby, Rails, and PostgreSQL is also expected.
  - question: Which Google Cloud machine type and OS does this path use?
    answer: >-
      You will create a Google Axion C4A Arm VM using the c4a-standard-4 machine type (4 vCPUs,
      16 GB memory) in the Google Cloud Console. The instance runs SUSE Linux Enterprise Server
      (SLES) on Arm64.
  - question: Where in Google Cloud Console do I create the C4A instance?
    answer: >-
      Navigate to Compute Engine > VM Instances and select Create Instance. Choose the C4A Arm-based
      machine type during configuration.
  - question: How should I prepare SUSE SLES for installing Ruby on Rails?
    answer: >-
      Update system packages first using zypper (for example, sudo zypper update). Then install
      Ruby, Rails, and the essential development tools as directed in the steps.
  - question: Which PostgreSQL packages are needed for Rails on SUSE SLES?
    answer: >-
      Install postgresql-server and postgresql-devel. The development headers are required so
      the pg gem can compile and allow Rails to communicate with PostgreSQL.
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

