---
title: Deploy Ruby on Rails on Arm-based Google Cloud C4A virtual machines

minutes_to_complete: 40

who_is_this_for: This is an introductory topic for developers deploying and optimizing Ruby on Rails workloads in Linux Arm64 environments, specifically using Google Cloud C4A virtual machines (VMs) powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (VM) on Google Cloud.
  - Install Ruby on Rails on a SUSE Arm64 C4A instance.
  - Validate Ruby on Rails functionality using PostgreSQL as the database.
  - Benchmark Rails performance using the built-in Ruby Benchmark library on Arm64 (Aarch64) architecture.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Ruby programming, the Rails framework, and the [PostgreSQL Relational Database](https://www.postgresql.org/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-23T20:57:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 96fa6409fdb418f09ab5ee3fed95c0670cfbbbebd6410f9fa398b4cbaf847a1a
  summary_generated_at: '2026-11-23T20:57:36Z'
  summary_source_hash: 96fa6409fdb418f09ab5ee3fed95c0670cfbbbebd6410f9fa398b4cbaf847a1a
  faq_generated_at: '2026-11-23T20:57:36Z'
  faq_source_hash: 96fa6409fdb418f09ab5ee3fed95c0670cfbbbebd6410f9fa398b4cbaf847a1a
  summary: You'll set up and benchmark Ruby on Rails on a Google Axion C4A VM running
    SUSE Linux. First, you'll provision the instance and install Ruby, Rails, and PostgreSQL dependencies.
    You'll then create a Rails application, configure its database, and run the database setup checks.
    Finally, you'll run a Ruby Benchmark script inside Rails and inspect timings for database and
    CPU work.
  faqs:
  - question: Why should I run the benchmark through Rails?
    answer: Use `rails runner benchmark.rb` from the application directory so that the benchmark loads
      your Rails environment. The benchmark can measure database operations alongside CPU work.
  - question: Which work does the benchmark measure?
    answer: Review the timing output for database inserts, database queries, and CPU computations.
      You can use those timings as a baseline for this instance.
  - question: Which PostgreSQL packages support the Rails pg gem?
    answer: Install `postgresql-server` and `postgresql-devel`. The development headers let you
      compile the `pg` gem that's used by Rails.
  - question: How do I check the Rails database connection?
    answer: Run `rails db:create` after configuring PostgreSQL and the Rails application. You'll then create a scaffold and run a migration to exercise the integration.
  - question: What indicates that the benchmark ran?
    answer: Look for timing output for each measured block, including inserts, queries, and CPU
      computations. Check that the run completed without a database connection error.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Web
platforms:
  - Google Axion

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

