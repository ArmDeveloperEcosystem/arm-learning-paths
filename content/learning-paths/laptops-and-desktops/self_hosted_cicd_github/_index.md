---
title: Use Self-Hosted Arm64-based runners in GitHub Actions for CI/CD

minutes_to_complete: 20

who_is_this_for: This Learning Path is for software developers and IT practitioners who want to learn how to use GitHub Actions for CI/CD purposes.

learning_objectives:
    - Create a CI/CD pipeline in GitHub.
    - Use a self-hosted runner.
    - Build and push the Docker image to DockerHub.

prerequisites:
    - An Arm64-powered machine, either virtual or physical. This Learning Path demonstration uses an Arm64-powered VM with Ubuntu 22.04.
    - A DockerHub account. You can [set up a free DockerHub account](https://hub.docker.com/signup).
    - A GitHub account. You can [sign up for GitHub](https://github.com/signup).

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - .NET
    - Visual Studio Code

further_reading:
    - resource:
        title: GitHub Actions
        link: https://docs.github.com/en/actions
        type: documentation
    - resource:
        title: Docker Hub
        link: https://hub.docker.com
        type: website
    - resource:
        title: Self-hosted runners
        link: https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
