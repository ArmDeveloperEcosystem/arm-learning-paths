---
title: MLOps with Arm-based GitHub Runners

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in automation for machine learning (ML) tasks.

learning_objectives:
    - Set up an Arm-based GitHub runner
    - Use GitHub Actions to set up an MLOps workflow
    - Train and deploy a PyTorch ML model with the German Traffic Sign Recognition Benchmark (GTSRB)
    - Use PyTorch compiled with OpenBLAS and oneDNN with Arm Compute Library to compare the performance of your trained model
    - Containerize the model and push your container to DockerHub


prerequisites:
    - A GitHub account with access to Arm-based GitHub runners
    - Some familiarity with ML and continuous integration and deployment (CI/CD) concepts is assumed

author_primary: Pareena Verma, Annie Tallund

### Tags
skilllevels: Introductory
subjects: CI/CD
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
