---
title: Deploy GitHub Actions Self-Hosted Runner on Google Axion C4A virtual machine

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to deploy a GitHub Actions self-hosted runner on an Arm-based Google Axion C4A instance.

learning_objectives:
       - Provision an Arm virtual machine on the Google Cloud Platform using the C4A Google Axion instance family
       - Set up and validate a GitHub Actions self-hosted runner on the Arm virtual machine
       - Deploy a basic CI workflow with NGINX and verify execution on Arm infrastructure

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled
  - A GitHub account; you can [sign up for GitHub](https://github.com/signup)

author: Annie Tallund

##### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers: Google Cloud

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
