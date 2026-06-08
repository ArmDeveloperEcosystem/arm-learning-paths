---
title: Build ML Workflow Pipelines with Flyte and gRPC on Google Cloud C4A Axion processors
description: Learn how to build scalable machine learning workflow pipelines on Google Cloud C4A Axion processors using Flyte for workflow orchestration and gRPC for distributed service communication.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, data engineers, and ML engineers who want to build scalable machine learning workflow pipelines on Arm64-based Google Cloud C4A Axion processors using Flyte workflow orchestration and gRPC-based microservices.

learning_objectives:
 - Deploy Flyte workflow pipelines on Google Cloud C4A Axion processors
 - Build distributed machine learning pipelines using Flyte tasks
 - Implement gRPC-based services for feature engineering
 - Integrate Flyte workflows with distributed services
 - Run scalable ML pipelines on Arm-based cloud infrastructure

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python
  - Basic understanding of machine learning pipelines


generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:53:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 85359b9210812675169f149c86bf11a1736ab838c011d18e876b246463d297ee
  summary_generated_at: '2026-06-02T03:53:08Z'
  summary_source_hash: 85359b9210812675169f149c86bf11a1736ab838c011d18e876b246463d297ee
  faq_generated_at: '2026-06-03T00:53:45Z'
  faq_source_hash: 85359b9210812675169f149c86bf11a1736ab838c011d18e876b246463d297ee
  summary: >-
    This Learning Path shows how to build and run an introductory machine learning workflow on
    Arm-based Google Cloud C4A Axion processors using Flyte for orchestration and gRPC for distributed
    service communication. You will provision a c4a-standard-4 Arm64 VM in Google Cloud, prepare
    a SUSE Linux Enterprise Server (SLES) development environment, install Flyte and gRPC tools,
    implement a gRPC feature engineering service, and create a Flyte workflow that loads data,
    preprocesses it, generates features via the service, trains a model, and evaluates results.
    It targets Linux on Arm infrastructure and takes about 30 minutes. Prerequisites include a
    GCP account with billing enabled, plus basic Python and ML pipeline familiarity.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Google Cloud Platform account with billing enabled, basic familiarity with Python,
      and a basic understanding of machine learning pipelines. No other prerequisites are explicitly
      listed.
  - question: Which Google Cloud VM type should I create for the exercises?
    answer: >-
      Use the c4a-standard-4 machine type on Google Axion C4A, which provides 4 vCPUs and 16 GB
      of memory. This VM hosts the Flyte ML workflow and gRPC applications.
  - question: Which operating system and architecture are used on the VM?
    answer: >-
      The development environment uses a SUSE Linux Enterprise Server (SLES) arm64 virtual machine.
      The tools run natively on the Arm-based Axion C4A processors.
  - question: How does the Flyte workflow interact with the gRPC feature engineering service?
    answer: >-
      The Flyte workflow calls the external gRPC-based feature engineering service during execution
      to generate features used by downstream tasks. This integrates distributed services directly
      into the pipeline.
  - question: What result should I expect after running the workflow?
    answer: >-
      The pipeline loads a dataset, preprocesses it, generates features via the gRPC service,
      trains a machine learning model, and evaluates the model’s performance. You will have a
      working example of a Flyte-orchestrated ML workflow running on Axion C4A.
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

