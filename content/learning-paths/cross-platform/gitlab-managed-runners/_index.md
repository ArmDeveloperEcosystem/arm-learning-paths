---
title: Build a Simple CI/CD pipeline with GitLab-Hosted Runners

draft: true
cascade:
    draft: true


minutes_to_complete: 40

who_is_this_for: This is an Introductory topic for DevOps professionals who are looking to build a CI/CD pipeline with GitLab on Google using GitLab-Hosted runners. 

learning_objectives: 
    - Create a GitLab Project
    - Understand basic pipeline script structure and how to use it
    - Build and test a simple CI/CD pipeline using Gitlab-hosted runners which will build and produce a tiny docker image from a simple "Hello world" "C" language program. The image will be built to run on Arm64 machines and will be saved in Gitlab Registery to be used later. 
    

prerequisites:
    - A valid GitLab account

author: Mohamed Ismail

### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers: Google Cloud

armips:
    - Neoverse-N1

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
        title: GitLab-hosted runners 
        link: https://docs.gitlab.com/ci/runners/hosted_runners/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
