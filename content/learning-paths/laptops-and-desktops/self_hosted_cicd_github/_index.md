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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-28T16:25:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a851b2f81b6aac54aef84acf7537a1cc6b99f66ce31ffd26631d6a966401e4ed
  summary_generated_at: '2026-07-28T16:25:40Z'
  summary_source_hash: a851b2f81b6aac54aef84acf7537a1cc6b99f66ce31ffd26631d6a966401e4ed
  faq_generated_at: '2026-07-28T16:25:40Z'
  faq_source_hash: a851b2f81b6aac54aef84acf7537a1cc6b99f66ce31ffd26631d6a966401e4ed
  summary: >-
    This Learning Path shows how to set up a GitHub Actions CI/CD pipeline on a self-hosted Arm64
    Linux runner to build a .NET application and publish an Arm64 Docker image to DockerHub. You
    create a private DockerHub repository, import a prepared sample repository into GitHub, and
    add repository secrets for DockerHub credentials. On an Arm64 machine running Ubuntu 22.04,
    you install Docker and the .NET SDK to prepare the runner. The workflow builds the application
    for Arm64 and pushes the resulting image to your DockerHub repository. After completing the
    steps, you should see a successful workflow run and a new image tag in DockerHub.
  faqs:
  - question: Do I need to create any GitHub secrets for DockerHub authentication?
    answer: >-
      Yes. Create two repository secrets: one for your DockerHub username and one for your DockerHub
      token so the workflow can log in and push the image.
  - question: Where can I find the exact docker push command for my new DockerHub repository?
    answer: >-
      DockerHub shows the push command after you create the repository. It looks like: docker
      push <YOUR_ACCOUNT_NAME>/sampleapp:tagname.
  - question: What software must I install on the self-hosted Arm64 runner before running the
      workflow?
    answer: >-
      Install the .NET SDK and Docker. The Learning Path provides Docker installation steps for
      Ubuntu 22.04.
  - question: Which project should I import into GitHub to follow the steps?
    answer: >-
      Use GitHub’s import tool with the repository URL https://github.com/dawidborycki/arm-lp-ci-cd-net.git
      and choose a name for your new repository.
  - question: What result should I expect when the pipeline finishes successfully?
    answer: >-
      An Arm64 Docker image of the .NET application is built and pushed to your DockerHub repository.
      You should see a new image tag in the repository you created.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

