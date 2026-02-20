---
title: Build a CI/CD pipeline using GitLab-hosted Arm runners

draft: true
cascade:
    draft: true


minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers who want to build CI/CD pipelines on Arm-based infrastructure using GitLab-hosted runners.

learning_objectives: 
    - Create a GitLab project with CI/CD configuration
    - Configure pipeline stages to use Arm64 runners
    - Build and containerize applications for Arm64 architecture
    - Store container images in GitLab Container Registry
    

prerequisites:
    - A GitLab account (free tier includes Arm64 runner access)

author: Mohamed Ismail

### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
    - GitLab
    - Docker
    - C

operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: GitLab CI/CD documentation 
        link: https://docs.gitlab.com/ee/ci/
        type: documentation
    - resource:
        title: GitLab-hosted Arm runners
        link: https://docs.gitlab.com/ci/runners/hosted_runners/linux.html
        type: documentation
    - resource:
        title: Docker install guide
        link: https://learn.arm.com/install-guides/docker/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
