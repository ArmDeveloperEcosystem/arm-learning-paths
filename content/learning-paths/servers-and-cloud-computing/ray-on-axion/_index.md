---
title: Scale AI workloads with Ray on Google Cloud C4A Axion VM
description: Deploy and run distributed AI workloads using Ray on Google Cloud Axion C4A Arm-based VMs, covering parallel tasks, hyperparameter tuning, and model serving with Ray Core, Train, Tune, and Serve.

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers, ML engineers, and software developers who want to deploy and run distributed workloads using Ray on SUSE Linux Enterprise Server (SLES) Arm64, execute parallel tasks, perform hyperparameter tuning, and serve models at scale.

learning_objectives:
    - Install and configure Ray on Google Cloud C4A Axion processors for Arm64
    - Run distributed tasks and parallel workloads using Ray Core
    - Perform distributed training and hyperparameter tuning using Ray Train and Ray Tune
    - Deploy scalable APIs using Ray Serve and validate end-to-end execution

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and distributed systems concepts

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Ray
  - Python
  - PyTorch

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

further_reading:
  - resource:
      title: Ray official documentation
      link: https://docs.ray.io/
      type: documentation

  - resource:
      title: Ray GitHub repository
      link: https://github.com/ray-project/ray
      type: documentation

  - resource:
      title: PyTorch documentation
      link: https://pytorch.org/docs/stable/index.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
