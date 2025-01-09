---
title: Build a CI/CD pipeline with GitLab on Google Axion

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for DevOps professionals who are looking to build a CI/CD pipeline with GitLab on Google Axion based self-hosted GitLab runners. 

learning_objectives: 
    - Create a Google Axion based GitLab self-hosted runner
    - Build a CI/CD pipeline with multi-architecture support
    - Build multi-architecture docker images using native GitLab runners on x86 and Arm
    - Automate the build and deployment of a multi-arch application with GitLab CI/CD

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). Create an account if needed.
    - A computer with [Google Cloud CLI](/install-guides/gcloud) and [kubectl](/install-guides/kubectl/)installed.
    - A valid GitLab account

author_primary: Pranay Bakre

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers: Google Cloud

armips:
    - Neoverse

tools_software_languages:
    - Kubernetes
    - Docker
    - GitLab

operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
