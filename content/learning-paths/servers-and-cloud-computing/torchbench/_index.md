---
title: Measure and accelerate PyTorch Inference on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to learn how to measure and accelerate the performance of Natural Language Processing (NLP), vision and recommender PyTorch models on Arm-based servers.

learning_objectives:
    - Download and install the PyTorch Benchmarks suite.
    - Evaluate PyTorch model inference performance on an Arm-based server using the PyTorch Benchmark suite.
    - Compare the model inference performance using eager mode and `torch.compile` mode in PyTorch.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:11:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d25121278f9dd40e2fd19d988e35866c6bfa70cfd0b93e2ec4506c8ad8a26d88
  summary_generated_at: '2026-06-02T05:20:50Z'
  summary_source_hash: d25121278f9dd40e2fd19d988e35866c6bfa70cfd0b93e2ec4506c8ad8a26d88
  faq_generated_at: '2026-06-03T02:11:47Z'
  faq_source_hash: d25121278f9dd40e2fd19d988e35866c6bfa70cfd0b93e2ec4506c8ad8a26d88
  summary: >-
    Learn to measure PyTorch inference on Arm-based servers using the PyTorch Benchmarks suite.
    You will install the benchmarks on Ubuntu 22.04 LTS, run model inference tests with Python
    and PyTorch, and compare performance between eager mode and torch.compile across NLP, vision,
    and recommender workloads. The instructions were tested on AWS Graviton3 (c7g.4xlarge) and
    apply to any Arm server meeting a baseline of 4 CPU cores and 8 GB RAM, whether provisioned
    on AWS, Microsoft Azure, Google Cloud, Oracle, or on-premises. Prerequisite: access to an
    Arm-based instance or Arm server. Estimated time to complete: about 20 minutes.
  faqs:
  - question: What do I need before running the benchmarks?
    answer: >-
      You need access to an Arm-based instance from a cloud service provider or an on-premise
      Arm server. The instructions target Ubuntu 22.04 LTS and the example assumes at least four
      cores and 8GB of RAM.
  - question: Can I run this on AWS, Azure, Google Cloud, or Oracle Cloud?
    answer: >-
      Yes. Any Arm-based instance from these cloud providers works, and the steps apply to any
      Arm server running Ubuntu 22.04 LTS.
  - question: How do I know the PyTorch Benchmarks suite installed correctly?
    answer: >-
      After installation, you will be able to run the benchmark suite and see inference timing
      output for selected PyTorch models. The Learning Path guides you through producing and reviewing
      those results.
  - question: Which PyTorch execution modes should I compare?
    answer: >-
      You will compare inference performance between PyTorch eager mode and torch.compile mode.
      Follow the steps to run both and examine the reported latency.
  - question: What results should I expect to collect and for which model types?
    answer: >-
      You will measure inference latency for PyTorch models in NLP, vision, and recommender categories.
      The outcome is a side-by-side comparison of latency between eager and torch.compile runs.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - PyTorch

further_reading:
    - resource:
        title: PyTorch Benchmarks
        link: https://github.com/pytorch/benchmark
        type: website
    - resource:
        title: PyTorch Inference Performance Tuning on AWS Graviton Processors
        link: https://pytorch.org/tutorials/recipes/inference_tuning_on_aws_graviton.html
        type: documentation
    - resource:
        title: ML inference on Graviton CPUs with PyTorch
        link: https://github.com/aws/aws-graviton-getting-started/blob/main/machinelearning/pytorch.md
        type: documentation
    - resource:
        title: PyTorch Documentation
        link: https://pytorch.org/docs/stable/index.html
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

