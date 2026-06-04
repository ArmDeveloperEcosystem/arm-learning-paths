---
title: Build a CI/CD pipeline using GitLab-hosted Arm runners


minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers who want to build CI/CD pipelines on Arm-based infrastructure using GitLab-hosted runners.

description: Learn how to build GitLab CI/CD pipelines using GitLab-hosted Arm64 runners to containerize C applications, store images in GitLab Container Registry, and deploy on Arm infrastructure.

learning_objectives: 
    - Create a GitLab project with CI/CD configuration
    - Configure pipeline stages to use Arm64 runners
    - Build and containerize applications for Arm64 architecture
    - Store container images in GitLab Container Registry
    

prerequisites:
    - A GitLab account (free tier includes Arm64 runner access)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:40:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  summary_generated_at: '2026-06-01T21:07:14Z'
  summary_source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  faq_generated_at: '2026-06-02T21:40:28Z'
  faq_source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  summary: >-
    This introductory Learning Path shows how to build a GitLab CI/CD pipeline that runs on GitLab-hosted
    Arm64 runners. You create or use a GitLab project, write a simple C program, and containerize
    it for Arm64 with Docker. You configure .gitlab-ci.yml to select Arm64 runner tags, build
    and push the image to GitLab Container Registry, and run the pipeline on managed Arm infrastructure.
    You verify execution on Arm64 by reviewing job logs and using lscpu output. The target environment
    is Linux and GitLab, and no runner provisioning is required. Prerequisite: a GitLab account;
    the free tier includes access to Arm64 runners.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a GitLab account. The free tier includes access to GitLab-hosted Arm64 runners;
      no other prerequisites are explicitly listed.
  - question: How do I configure my pipeline to use Arm64 runners?
    answer: >-
      Create a .gitlab-ci.yml in the project root and specify the Arm64 runner tag. GitLab-hosted
      runners are available to your project without additional setup.
  - question: Which executor should I use for the jobs in this path?
    answer: >-
      Use the Docker executor for containerized builds. The path containerizes a C application
      and builds it for the Arm64 architecture.
  - question: What artifact does the pipeline produce and where is it stored?
    answer: >-
      The pipeline builds a container image for Arm64 and pushes it to the GitLab Container Registry.
      After a successful run, you can view the image in your project’s registry.
  - question: How do I verify the jobs actually ran on Arm64?
    answer: >-
      Open the job logs after running the pipeline and check the architecture verification step.
      The lscpu output should indicate an Arm64 (AArch64) environment.
# END generated_summary_faq

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

