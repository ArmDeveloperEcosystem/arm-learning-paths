---
title: MLOps with Arm-hosted GitHub Runners
draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in automation for machine learning (ML) tasks.

learning_objectives:
    - Set up an Arm-hosted GitHub runner.
    - Train and test a PyTorch ML model with the German Traffic Sign Recognition Benchmark (GTSRB) dataset.
    - Use PyTorch compiled with OpenBLAS and oneDNN with Arm Compute Library to compare the performance of a trained model.
    - Containerize the model and push the container to DockerHub.
    - Automate all the steps in the ML workflow using GitHub Actions.

prerequisites:
    - A GitHub account with access to Arm-hosted GitHub runners.
    - A Docker Hub account for storing container images.
    - Some familiarity with ML and continuous integration and deployment (CI/CD) concepts.

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
