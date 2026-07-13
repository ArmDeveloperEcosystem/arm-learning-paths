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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T18:57:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  summary_generated_at: '2026-07-02T18:57:24Z'
  summary_source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  faq_generated_at: '2026-07-02T18:57:24Z'
  faq_source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  summary: >-
    You'll create a GitLab project and configure a CI/CD pipeline that
    runs on GitLab‑hosted arm64 runners. You'll add a `.gitlab-ci.yml` that targets arm64 by specifying
    the appropriate runner tag and use the Docker executor to containerize a simple C application.
    The pipeline builds the program, produces an arm64 container image, and pushes it to the GitLab
    Container Registry. You'll trigger the workflow from the Pipelines page, inspect job logs to
    follow each stage, and verify the execution environment by checking `lscpu` output for arm64.
    By the end, you'll have a working pipeline and a versioned image visible in the project’s registry.
  faqs:
  - question: Which runner executor should I use for this pipeline?
    answer: >-
      Use the Docker executor to run containerized builds on GitLab‑hosted runners. This path
      configures jobs to run on arm64 by adding the Arm64 runner tag in `.gitlab-ci.yml`.
  - question: How do I target arm64 runners in `.gitlab-ci.yml`?
    answer: >-
      Add the Arm64 runner tag to the job’s tags section in `.gitlab-ci.yml`. Jobs that include
      this tag are scheduled on GitLab‑hosted arm64 runners.
  - question: How do I confirm my job actually ran on Arm64?
    answer: >-
      Open the job log and review the `lscpu` output. The reported architecture should indicate
      Arm64, confirming that the job executed on the intended runner.
  - question: What result should I expect after the pipeline runs?
    answer: >-
      You should see successful build and push stages, with logs showing the C program compilation
      and container image creation. The new image and tag appear in the project’s GitLab Container
      Registry.
  - question: What should I check if the image is not in the GitLab Container Registry?
    answer: >-
      Verify that the push stage finished without errors in the job log. Then open the project’s
      Container Registry page and confirm the expected image tag is listed.
# END generated_summary_faq

author: Mohamed Ismail

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
