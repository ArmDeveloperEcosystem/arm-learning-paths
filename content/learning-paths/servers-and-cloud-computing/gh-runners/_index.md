---
title: Optimize MLOps with Arm-hosted GitHub Runners

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

author_primary: Pareena Verma, Annie Tallund

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


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
