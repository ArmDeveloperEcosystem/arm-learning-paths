---
title: Deploy GitHub Actions Self-Hosted Runner on Google Axion C4A virtual machine
 
minutes_to_complete: 30

who_is_this_for: This Learning Path is for DevOps engineers, system administrators, or developers who want to deploy GitHub Actions Self-Hosted Runner on the Google Axion C4A Arm virtual machine.

learning_objectives:
       - Provision an Arm virtual machine on the Google Cloud Platform using the C4A Google Axion instance family.
       - Set up and validate a GitHub Actions self-hosted runner on the Arm virtual machine.
       - Deploy a basic CI workflow with NGINX and verify execution on Arm infrastructure.

prerequisites:
     - A [Google Cloud Platform (GCP)](https://cloud.google.com/free?utm_source=google&hl=en) account with billing enabled.
     - Familiarity with [GitHub Actions](https://github.com/features/actions) and the Linux command line.
     - A GitHub account. You can sign up [here](https://github.com/signup).     

author: Jason Andrews

##### Tags
skilllevels: Advanced
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
        title: Google Cloud official website and documentation
        link: https://cloud.google.com/docs
        type: documentation

    - resource:
        title: Github-action official website and documentation
        link: https://docs.github.com/en/actions
        type: documentation

    - resource:
        title: GitHub Actions Arm runners
        link: https://github.blog/news-insights/product-news/arm64-on-github-actions-powering-faster-more-efficient-build-systems/
        type: website


weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
