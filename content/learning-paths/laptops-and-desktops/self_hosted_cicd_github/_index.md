---
title: Use Self-Hosted Arm64-based runners in GitHub Actions for CI/CD

description: Learn how to create a CI/CD pipeline in GitHub using self-hosted Arm64 runners to build and push Docker images to DockerHub.

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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:12:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a851b2f81b6aac54aef84acf7537a1cc6b99f66ce31ffd26631d6a966401e4ed
  summary_generated_at: '2026-06-01T22:09:45Z'
  summary_source_hash: a851b2f81b6aac54aef84acf7537a1cc6b99f66ce31ffd26631d6a966401e4ed
  faq_generated_at: '2026-06-02T23:12:53Z'
  faq_source_hash: a851b2f81b6aac54aef84acf7537a1cc6b99f66ce31ffd26631d6a966401e4ed
  summary: >-
    This introductory Learning Path shows how to build a GitHub Actions CI/CD pipeline that uses
    a self-hosted Arm64 runner to compile a .NET application and publish an Arm64 Docker image
    to DockerHub. You will create a private DockerHub repository, import a starter GitHub repository,
    configure repository secrets for Docker credentials, and prepare an Arm64 Ubuntu 22.04 runner
    by installing the .NET SDK and Docker. The workflow builds the container image and pushes
    it to your DockerHub repository. Prerequisites include an Arm64-powered machine, a GitHub
    account, and a DockerHub account. The path targets Linux environments and uses .NET and Visual
    Studio Code.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm64-powered machine (the demonstration uses an Ubuntu 22.04 VM), a DockerHub
      account, and a GitHub account. No other prerequisites are explicitly listed.
  - question: Which DockerHub repository settings should I use, and what push command will I see?
    answer: >-
      Create a repository named sampleapp and set its visibility to Private. You should see a
      push command in the form: docker push <YOUR_ACCOUNT_NAME>/sampleapp:tagname.
  - question: How do I bring the sample application into my GitHub account?
    answer: >-
      Use GitHub’s Import repository and provide https://github.com/dawidborycki/arm-lp-ci-cd-net.git
      as the source URL. Set a repository name (for example, lp-ci-cd-net) and start the import.
  - question: Which secrets should I add to the GitHub repository?
    answer: >-
      Create two secrets that store your DockerHub username and a DockerHub token. These are used
      by the workflow to authenticate when pushing images.
  - question: What software must be installed on the self-hosted Arm64 runner?
    answer: >-
      Install the .NET SDK and Docker on your Arm64 machine, and keep the OS patched. For Ubuntu
      22.04, the Learning Path provides Docker installation steps.
# END generated_summary_faq

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

