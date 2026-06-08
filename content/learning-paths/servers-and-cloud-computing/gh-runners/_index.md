---
title: Optimize MLOps with Arm-hosted GitHub Runners
description: Learn how to set up Arm-hosted GitHub runners and train PyTorch ML models using the German Traffic Sign Recognition Benchmark dataset with automated workflows.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in automation for Machine Learning (ML) tasks.

learning_objectives:
    - Set up an Arm-hosted GitHub runner.
    - Train and test a PyTorch ML model with the German Traffic Sign Recognition Benchmark (GTSRB) dataset.
    - Compare the performance of two trained PyTorch ML models; one model compiled with OpenBLAS (Open Basic Linear Algebra Subprograms Library) and oneDNN (Deep Neural Network Library), and the other model compiled with Arm Compute Library (ACL).
    - Containerize a ML model and push the container to DockerHub.
    - Automate steps in an ML workflow using GitHub Actions.

prerequisites:
    - A GitHub account with access to Arm-hosted GitHub runners.
    - A Docker Hub account for storing container images.
    - Familiarity with the concepts of ML and continuous integration and deployment (CI/CD).

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:01:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 642b67e7ca3717f499ab73efedd924eeab29a0055fad81c2d60fda993dcea195
  summary_generated_at: '2026-06-02T04:00:17Z'
  summary_source_hash: 642b67e7ca3717f499ab73efedd924eeab29a0055fad81c2d60fda993dcea195
  faq_generated_at: '2026-06-03T01:01:51Z'
  faq_source_hash: 642b67e7ca3717f499ab73efedd924eeab29a0055fad81c2d60fda993dcea195
  summary: >-
    This Learning Path shows how to automate an end-to-end MLOps workflow on Linux using Arm-hosted
    GitHub runners and GitHub Actions. You will fork an example repository, set up workflows to
    train and test a PyTorch model on the German Traffic Sign Recognition Benchmark (GTSRB) dataset,
    and save the trained model as a workflow artifact. You will compare inference performance
    by switching from a PyTorch 2.3.0 Docker image compiled with OpenBLAS to a oneDNN backend
    with the Arm Compute Library (ACL). Finally, you will containerize the model using the provided
    Dockerfile, push the image to Docker Hub, and deploy the container for API-based access. Prerequisites
    include GitHub access to Arm-hosted runners, a Docker Hub account, and familiarity with ML
    and CI/CD.
  faqs:
  - question: What do I need before running the workflows?
    answer: >-
      You need a GitHub account with access to Arm-hosted GitHub runners and a Docker Hub account.
      Familiarity with ML and CI/CD is expected, and the path targets Linux.
  - question: Where should I fork the example repository, and what if the name conflicts?
    answer: >-
      Fork https://github.com/Arm-Labs/gh_armrunner_mlops_gtsrb into a GitHub Organization or
      Team where you have access to Arm-hosted GitHub runners. If a repository with the same name
      already exists there, rename it during the fork.
  - question: Which workflow trains the model and what should I expect as output?
    answer: >-
      The training is automated by .github/workflows/train-model.yml, which runs scripts/train_model.py
      inside a PyTorch 2.3.0 Docker image compiled with OpenBLAS. When it completes, the trained
      model is saved as a workflow artifact.
  - question: How do I compare inference performance across PyTorch backends?
    answer: >-
      Use the comparison step to change the backend used for testing to oneDNN with Arm Compute
      Library (ACL) and run the workflow to measure inference time. Compare those results with
      the OpenBLAS-based run.
  - question: How do I containerize and publish the trained model, and how is deployment validated?
    answer: >-
      Build an image using the Dockerfile in the repository and push it to Docker Hub; the Dockerfile
      uses armswdev/pytorch-arm-neoverse:r24.07-torch-2.3.0-onednn-acl as the base. After deployment,
      access the model using API calls as described in the steps.
# END generated_summary_faq

author:
    - Pareena Verma
    - Annie Tallund

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Neoverse
tools_software_languages:
    - Python
    - PyTorch
    - ACL
    - GitHub
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Arm64 on GitHub Actions - Powering faster, more efficient build systems
        link: https://github.blog/news-insights/product-news/arm64-on-github-actions-powering-faster-more-efficient-build-systems/
        type: blog
    - resource:
        title: Arm Compute Library
        link: https://github.com/ARM-software/ComputeLibrary
        type: website
    - resource:
        title: Streamlining your MLOps pipeline with GitHub Actions and Arm64 runners
        link: https://github.blog/enterprise-software/ci-cd/streamlining-your-mlops-pipeline-with-github-actions-and-arm64-runners/
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

