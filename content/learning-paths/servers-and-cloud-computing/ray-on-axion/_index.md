---
title: Scale AI workloads with Ray on Google Cloud C4A Axion VM
description: Deploy and run distributed AI workloads using Ray on Google Cloud Axion C4A Arm-based VMs, covering parallel tasks, hyperparameter tuning, and model serving with Ray Core, Train, Tune, and Serve.
    
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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:57:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0877f5f233ec8a50172f4bb9388ad38ae9b890a4d049679ca6ece083d760d872
  summary_generated_at: '2026-06-02T04:56:29Z'
  summary_source_hash: 0877f5f233ec8a50172f4bb9388ad38ae9b890a4d049679ca6ece083d760d872
  faq_generated_at: '2026-06-03T01:57:59Z'
  faq_source_hash: 0877f5f233ec8a50172f4bb9388ad38ae9b890a4d049679ca6ece083d760d872
  summary: >-
    This Learning Path shows how to deploy and run distributed AI workloads with Ray on Google
    Cloud Axion C4A Arm-based VMs. You will provision a c4a-standard-4 instance (4 vCPUs, 16 GB)
    running SUSE Linux Enterprise Server (SLES) Arm64, configure a firewall rule for the Ray Dashboard
    and Ray Serve API, install Ray and required dependencies, and initialize a single-node Ray
    cluster. You will run parallel tasks with Ray Core, perform distributed training and hyperparameter
    tuning using Ray Train and Ray Tune, and deploy an API with Ray Serve to validate end-to-end
    execution. Prerequisites are a GCP account with billing enabled and basic familiarity with
    Python and distributed systems. Estimated time: 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform (GCP) account with billing enabled and basic familiarity
      with Python and distributed systems concepts. The path provisions the required Arm-based
      VM during the steps.
  - question: Which VM type should I create for this path?
    answer: >-
      Create a Google Axion C4A Arm VM using the c4a-standard-4 machine type, which provides 4
      vCPUs and 16 GB of memory. This instance will host your Ray application.
  - question: Which Ray components will I use, and for what?
    answer: >-
      Use Ray Core to run distributed tasks and parallel workloads. Use Ray Train and Ray Tune
      for distributed training and hyperparameter tuning, and Ray Serve to deploy a scalable API
      and validate end-to-end execution.
  - question: How do I expose the Ray Dashboard and Ray Serve endpoints?
    answer: >-
      In the Google Cloud Console, go to VPC Network > Firewall and create a firewall rule that
      allows the required ports for the Ray Dashboard and Ray Serve API. If you need help with
      GCP setup, see the Learning Path Getting started with Google Cloud Platform.
  - question: How do I verify that Ray is set up correctly?
    answer: >-
      Run the provided Python script that calls a @ray.remote function and aggregates results
      with ray.get. You should see output like “Results: [...]” containing the squared numbers
      from the sample.
# END generated_summary_faq

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

