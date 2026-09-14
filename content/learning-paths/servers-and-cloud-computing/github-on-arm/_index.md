---
title: Deploy a GitHub Actions self-hosted runner on a Google Axion C4A virtual machine
description: Learn how to provision a Google Axion C4A Arm virtual machine and set up a GitHub Actions self-hosted runner for CI/CD workflows.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to deploy a GitHub Actions self-hosted runner on an Arm-based Google Axion C4A instance.

learning_objectives:
       - Provision an Arm virtual machine on the Google Cloud Platform using the C4A Google Axion instance family.
       - Set up and validate a GitHub Actions self-hosted runner on the Arm virtual machine (VM).
       - Deploy a basic CI workflow with NGINX and verify execution on Arm infrastructure.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - A [GitHub account](https://github.com/signup)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:06:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5af3064f3ce9fb84a3e7dc6efabeecb89f30fd6e0bb27a4a51f0ceec1f832e89
  summary_generated_at: '2026-09-10T22:06:54Z'
  summary_source_hash: 5af3064f3ce9fb84a3e7dc6efabeecb89f30fd6e0bb27a4a51f0ceec1f832e89
  faq_generated_at: '2026-09-10T22:06:54Z'
  faq_source_hash: 5af3064f3ce9fb84a3e7dc6efabeecb89f30fd6e0bb27a4a51f0ceec1f832e89
  summary: >-
    You'll provision a Google Axion C4A VM and register it as a GitHub Actions self-hosted runner. First, you'll install Git and GitHub CLI, authenticate to GitHub, create a workflow, and configure it to run on the Arm VM. Then, you'll verify the runner by checking workflow logs and the NGINX service.
  faqs:
  - question: Which Google Cloud machine type should I choose for the VM?
    answer: >-
      Select the C4A family with the `c4a-standard-4` machine type (4 vCPUs, 16 GB memory).
  - question: What should I do on the instance before registering the GitHub Actions runner?
    answer: >-
      Install Git and GitHub CLI with the package manager, set your Git identity, then authenticate
      to GitHub. After that, register the runner so that it can accept jobs.
  - question: Where do I create the workflow file and how is it triggered?
    answer: >-
      Create `.github/workflows/deploy-nginx.yaml` in your repository. It runs on a push event to
      the main branch.
  - question: How do I know the job executed on the Arm self-hosted runner?
    answer: >-
      Treat `runs-on: self-hosted` as a match for any eligible self-hosted runner. It doesn't select
      the C4A VM by architecture alone. Check the workflow logs and registered runner details to
      confirm that the job ran on the C4A instance.
  - question: How do I verify that the NGINX deployment completes?
    answer: >-
      Open the VM's external IP address in a browser after the workflow completes. The NGINX welcome
      page should load, confirming that the workflow installed and started NGINX on the self-hosted
      Arm runner.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: CI-CD
platforms:
  - Google Axion

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
