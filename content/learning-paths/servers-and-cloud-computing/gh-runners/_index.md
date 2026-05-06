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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: 642b67e7ca3717f499ab73efedd924eeab29a0055fad81c2d60fda993dcea195
  summary: >-
    Learn how to set up Arm-hosted GitHub runners and train PyTorch ML models using the German
    Traffic Sign Recognition Benchmark dataset with automated workflows. It is designed for software
    developers interested in automation for Machine Learning (ML) tasks. By the end, you will
    be able to set up an Arm-hosted GitHub runner, train and test a PyTorch ML model with the
    German Traffic Sign Recognition Benchmark (GTSRB) dataset, and compare the performance of
    two trained PyTorch ML models; one model compiled with OpenBLAS (Open Basic Linear Algebra
    Subprograms Library) and oneDNN (Deep Neural Network Library), and the other model compiled
    with Arm Compute Library (ACL). It focuses on tools and technologies such as Python, PyTorch,
    ACL, and GitHub, Linux environments, and Arm platforms including Neoverse. The main steps
    cover MLOps background, Understand neural network model training and testing, Automate training
    and testing with GitHub Actions, Compare the performance of PyTorch backends, and Deploy the
    application as a container.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will set up an Arm-hosted GitHub runner, train and test a PyTorch ML model with the
      German Traffic Sign Recognition Benchmark (GTSRB) dataset, and compare the performance of
      two trained PyTorch ML models; one model compiled with OpenBLAS (Open Basic Linear Algebra
      Subprograms Library) and oneDNN (Deep Neural Network Library), and the other model compiled
      with Arm Compute Library (ACL). Learn how to set up Arm-hosted GitHub runners and train
      PyTorch ML models using the German Traffic Sign Recognition Benchmark dataset with automated
      workflows.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers interested in automation for Machine
      Learning (ML) tasks.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A GitHub account with access to Arm-hosted
      GitHub runners.; A Docker Hub account for storing container images.; Familiarity with the
      concepts of ML and continuous integration and deployment (CI/CD).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python, PyTorch, ACL, and GitHub, Linux environments,
      and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around MLOps background, Understand neural network model
      training and testing, Automate training and testing with GitHub Actions, Compare the performance
      of PyTorch backends, and Deploy the application as a container.
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

