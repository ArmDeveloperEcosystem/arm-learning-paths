---
title: Deploy GitHub Actions Self-Hosted Runner on Google Axion C4A virtual machine
description: Learn how to provision a Google Axion C4A Arm virtual machine and set up a GitHub Actions self-hosted runner for CI/CD workflows.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to deploy a GitHub Actions self-hosted runner on an Arm-based Google Axion C4A instance.

learning_objectives:
       - Provision an Arm virtual machine on the Google Cloud Platform using the C4A Google Axion instance family
       - Set up and validate a GitHub Actions self-hosted runner on the Arm virtual machine
       - Deploy a basic CI workflow with NGINX and verify execution on Arm infrastructure

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - A GitHub account; you can [sign up for GitHub](https://github.com/signup)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:03:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d5df467355a7792f7a04eafc4a6bbd2410353aca000cd2b1aec74a7ed93a9270
  summary_generated_at: '2026-06-02T04:01:33Z'
  summary_source_hash: d5df467355a7792f7a04eafc4a6bbd2410353aca000cd2b1aec74a7ed93a9270
  faq_generated_at: '2026-06-03T01:03:50Z'
  faq_source_hash: d5df467355a7792f7a04eafc4a6bbd2410353aca000cd2b1aec74a7ed93a9270
  summary: >-
    This Learning Path shows how to provision a Google Axion C4A Arm virtual machine on Google
    Cloud and use it as a self-hosted runner for GitHub Actions. You will create a c4a-standard-4
    instance from the Google Cloud Console, install Git and the GitHub CLI on Linux, authenticate
    with GitHub, and register the runner so workflows execute on Arm infrastructure. To validate
    the setup, you will deploy a basic CI workflow that installs and starts NGINX when changes
    are pushed to the main branch. Prerequisites are a Google Cloud account with billing enabled
    and a GitHub account; no other prerequisites are explicitly listed.
  faqs:
  - question: What do I need before creating the VM and runner?
    answer: >-
      You need a Google Cloud Platform account with billing enabled and a GitHub account. No other
      prerequisites are explicitly listed.
  - question: Which Google Cloud machine type is used in the steps?
    answer: >-
      The path uses the c4a-standard-4 machine type (4 vCPUs, 16 GB memory) from the Google Axion
      C4A family. Other sizes are not covered in the instructions.
  - question: Which operating system is assumed on the VM?
    answer: >-
      The steps assume a Linux VM on an Arm64 Google Axion C4A instance. A specific Linux distribution
      is not explicitly listed.
  - question: How do I set up the self-hosted runner on the VM?
    answer: >-
      Install Git and GitHub CLI with apt, configure your Git identity, authenticate with GitHub,
      and register the runner as shown in the steps. This enables your CI/CD workflows to target
      the self-hosted Arm runner.
  - question: How do I verify that the workflow executed on the Arm runner?
    answer: >-
      Push to the main branch to trigger the provided workflow, which installs and starts NGINX
      on the self-hosted runner. A successful job run and a started NGINX service on the VM indicate
      it executed on your Arm infrastructure.
# END generated_summary_faq

author: Annie Tallund

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
  - GitHub Actions
  - GitHub CLI

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
      title: GitHub Actions documentation
      link: https://docs.github.com/en/actions
      type: documentation

  - resource:
      title: GitHub Actions Arm runners (announcement)
      link: https://github.blog/news-insights/product-news/arm64-on-github-actions-powering-faster-more-efficient-build-systems/
      type: website

  - resource:
        title: GCP Quickstart Guide to Create a virtual machine
        link: https://cloud.google.com/compute/docs/instances/create-start-instance
        type: website


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

