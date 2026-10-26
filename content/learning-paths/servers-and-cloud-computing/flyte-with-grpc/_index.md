---
title: Build ML Workflow Pipelines with Flyte and gRPC on Google Cloud C4A Axion processors
description: Learn how to build scalable machine learning workflow pipelines on Google Cloud C4A Axion processors using Flyte for workflow orchestration and gRPC for distributed service communication.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, data engineers, and ML engineers who want to build scalable machine learning workflow pipelines on Arm64-based Google Cloud C4A virtual machines (VMs) using Flyte workflow orchestration and gRPC-based microservices.

learning_objectives:
 - Deploy Flyte workflow pipelines on Google Cloud C4A VMs powered by Axion processors.
 - Build distributed machine learning pipelines using Flyte tasks.
 - Implement gRPC-based services for feature engineering.
 - Integrate Flyte workflows with distributed services.
 - Run scalable ML pipelines on Arm-based cloud infrastructure.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python
  - Basic understanding of machine learning pipelines

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T21:58:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7d3f9f50ba7e0a990fc02e539bbe1c94af2ffaa319ea4da0fd0ed0f028b17a6e
  summary_generated_at: '2026-09-10T21:58:11Z'
  summary_source_hash: 7d3f9f50ba7e0a990fc02e539bbe1c94af2ffaa319ea4da0fd0ed0f028b17a6e
  faq_generated_at: '2026-09-10T21:58:11Z'
  faq_source_hash: 7d3f9f50ba7e0a990fc02e539bbe1c94af2ffaa319ea4da0fd0ed0f028b17a6e
  summary: >-
    You'll build a machine learning pipeline on Google Cloud C4A VMs using Flyte and a gRPC feature-engineering service. First, you'll prepare an Arm64 environment, install the required components, and connect the service to Flyte tasks. The workflow loads and preprocesses data, generates features, trains a model, and evaluates your result on the Axion instance.
  faqs:
  - question: Which Google Cloud instance type should I create?
    answer: >-
      Use the C4A instance family and select `c4a-standard-4` (4 vCPUs, 16 GB memory).
  - question: Which operating system image should I choose for the VM?
    answer: >-
      Use a SUSE Linux Enterprise Server (SLES) arm64 image to prepare the development environment.
  - question: How do I know that the gRPC feature engineering service is integrated correctly with
      the workflow?
    answer: >-
      During execution, the workflow’s feature generation step calls the gRPC service and passes
      the resulting features to downstream tasks. If the service is unreachable or misconfigured,
      the dependent step won't complete.
  - question: Is this environment single-node or multi-node, and where do components run?
    answer: >-
      The development environment uses a single-node setup on the Axion C4A VM. The gRPC feature
      engineering service runs as an external microservice that the Flyte workflow invokes.
  - question: How do I start the gRPC feature service before running the workflow?
    answer: >-
      Activate the `flyte-env` virtual environment and run `python feature_server.py` from the
      project directory. Leave that terminal running, then open a second terminal and run
      `python workflow.py` so that the Flyte workflow can connect to the service on port `50051`.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: ML
platforms:
- Google Axion

armips:
- Neoverse

tools_software_languages:
- Flyte
- Python
- gRPC

operatingsystems:
- Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Flyte documentation
      link: https://docs.flyte.org/
      type: documentation

  - resource:
      title: gRPC documentation
      link: https://grpc.io/docs/
      type: documentation

  - resource:
      title: Flyte GitHub repository
      link: https://github.com/flyteorg/flyte
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
