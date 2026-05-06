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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: d5df467355a7792f7a04eafc4a6bbd2410353aca000cd2b1aec74a7ed93a9270
  summary: >-
    Learn how to provision a Google Axion C4A Arm virtual machine and set up a GitHub Actions
    self-hosted runner for CI/CD workflows. It is designed for developers who want to deploy a
    GitHub Actions self-hosted runner on an Arm-based Google Axion C4A instance. By the end, you
    will be able to provision an Arm virtual machine on the Google Cloud Platform using the C4A
    Google Axion instance family, set up and validate a GitHub Actions self-hosted runner on the
    Arm virtual machine, and deploy a basic CI workflow with NGINX and verify execution on Arm
    infrastructure. It focuses on tools and technologies such as GitHub Actions and GitHub CLI,
    Linux environments, Arm platforms including Neoverse, and cloud platforms such as Google Cloud.
    The main steps cover About Google Axion and GitHub Actions, Create the instance, Set up a
    GitHub Self-Hosted Runner, and Deploy NGINX with the GitHub runner.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm virtual machine on the Google Cloud Platform using the C4A Google
      Axion instance family, set up and validate a GitHub Actions self-hosted runner on the Arm
      virtual machine, and deploy a basic CI workflow with NGINX and verify execution on Arm infrastructure.
      Learn how to provision a Google Axion C4A Arm virtual machine and set up a GitHub Actions
      self-hosted runner for CI/CD workflows.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers who want to deploy a GitHub Actions self-hosted
      runner on an Arm-based Google Axion C4A instance.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en)
      account with billing enabled; A GitHub account; you can [sign up for GitHub](https://github.com/signup).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including GitHub Actions and GitHub CLI, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around About Google Axion and GitHub Actions, Create the
      instance, Set up a GitHub Self-Hosted Runner, and Deploy NGINX with the GitHub runner.
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

