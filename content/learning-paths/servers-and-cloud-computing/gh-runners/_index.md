---
title: Optimize MLOps with Arm-hosted GitHub Runners
description: Learn how to set up Arm-hosted GitHub runners and train PyTorch ML models using the German Traffic Sign Recognition Benchmark dataset with automated workflows.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in automation for Machine Learning (ML) tasks.

learning_objectives:
    - Set up an Arm-hosted GitHub runner.
    - Train and test a PyTorch ML model with the German Traffic Sign Recognition Benchmark (GTSRB) dataset.
    - Compare the performance of two trained PyTorch ML models. One model is compiled with Open Basic Linear Algebra Subprograms Library (OpenBLAS) and oneAPI Deep Neural Network Library (oneDNN). The other model is compiled with Arm Compute Library (ACL).`
    - Containerize a ML model and push the container to DockerHub.
    - Automate steps in an ML workflow using GitHub Actions.

prerequisites:
    - A GitHub account with access to Arm-hosted GitHub runners
    - A Docker Hub account for storing container images
    - Familiarity with the concepts of ML and continuous integration and deployment (CI/CD)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:05:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9921be6d22cb7753386f413c84cbb616dc59c8e32c22f03ca3c78d1c7d654d5e
  summary_generated_at: '2026-09-10T22:05:08Z'
  summary_source_hash: 9921be6d22cb7753386f413c84cbb616dc59c8e32c22f03ca3c78d1c7d654d5e
  faq_generated_at: '2026-09-10T22:05:08Z'
  faq_source_hash: 9921be6d22cb7753386f413c84cbb616dc59c8e32c22f03ca3c78d1c7d654d5e
  summary: >-
    You'll automate an MLOps workflow on Arm-hosted GitHub runners with GitHub Actions. First, you'll train and test a PyTorch model, compare OpenBLAS and oneDNN with ACL, and capture workflow artifacts. Then, you'll containerize the application and push it to DockerHub, deploy the application, and access the model through API calls. You can compare the resulting workflows using repeatable runs.
  faqs:
  - question: Where should I fork the repository to use Arm-hosted GitHub runners?
    answer: >-
      Fork the example into a GitHub Organization or Team that has access to Arm-hosted GitHub
      runners. If a repository with the same name already exists, change the repository
      name when you fork.
  - question: How do I know that the training workflow finished successfully and produced a model?
    answer: >-
      Check the **Actions** tab for a successful run of `.github/workflows/train-model.yml` and verify
      that a model artifact was created. The workflow trains inside a PyTorch 2.3.0 Docker image
      compiled with OpenBLAS and saves the trained model for later steps.
  - question: How do I switch the PyTorch backend for inference testing?
    answer: >-
      Update the testing workflow to use the backend with oneDNN and ACL
      instead of the OpenBLAS-based image, then trigger the run. 
  - question: Where do I find the inference performance results to compare runs?
    answer: >-
      Review the workflow run logs and any artifacts produced by the testing workflow. The artifacts and logs report
      the model’s inference time. Compare outputs from the OpenBLAS and oneDNN+ACL runs to see
      differences.
  - question: Which Docker Hub secrets does the deployment workflow require?
    answer: >-
      Add `DOCKER_USERNAME` with your Docker Hub username and `DOCKER_PASSWORD` with your Docker
      Hub Personal Access Token as repository secrets under **Settings** > **Secrets and variables**
      > **Actions**. 
# END generated_summary_faq

author:
    - Pareena Verma
    - Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
