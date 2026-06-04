---
title: Building and Benchmarking DLRM on Arm Neoverse V2 with MLPerf
description: Learn how to build and benchmark the Deep Learning Recommendation Model using PyTorch and MLPerf on Arm Neoverse V2 processors.


minutes_to_complete: 90

who_is_this_for: This is an introductory topic for software developers who want to set up a pipeline in the cloud for recommendation models. You'll build and run the Deep Learning Recommendation Model (DLRM) and benchmark its performance using MLPerf and PyTorch.

learning_objectives:
    - Build the Deep Learning Recommendation Model (DLRM). 
    - Run a modified performant DLRMv2 benchmark and inspect the results.

prerequisites:
    - Any [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider (CSP), or an on-premise Arm server with at least 400GB of RAM and 800 GB of disk space.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:42:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 82716c2de19d18a154c85d03b7f2ec01839284262914f7bb3ad04b18a105379d
  summary_generated_at: '2026-06-02T03:35:11Z'
  summary_source_hash: 82716c2de19d18a154c85d03b7f2ec01839284262914f7bb3ad04b18a105379d
  faq_generated_at: '2026-06-03T00:42:37Z'
  faq_source_hash: 82716c2de19d18a154c85d03b7f2ec01839284262914f7bb3ad04b18a105379d
  summary: >-
    This Learning Path shows how to build and benchmark the Deep Learning Recommendation Model
    (DLRM) on Arm Neoverse V2 processors using PyTorch and MLPerf. You will prepare a Linux Arm-based
    cloud instance or on‑prem server, obtain data and model weights with rclone, and use provided
    scripts to run a modified DLRMv2 benchmark. The path uses PyTorch 2.9.0+cpu with Arm-focused
    optimizations and Docker-based tooling where applicable. By the end, you will have built DLRM,
    executed the MLPerf benchmark tailored for Arm systems, and inspected the resulting performance
    outputs. Prerequisites include an Arm-based instance (AWS or Google Cloud) or on‑prem Arm
    server with at least 400GB RAM and 800GB of disk space.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      Use any Arm-based instance from a cloud service provider such as AWS or Google Cloud, or
      an on-premise Arm server. The prerequisites are at least 400GB of RAM and 800GB of disk
      space on a Linux system.
  - question: Which operating system and processors does this target?
    answer: >-
      The steps assume Linux and target Arm Neoverse V2 CPUs. The procedures and benchmarks are
      written for Arm-based systems.
  - question: How do I download the DLRM data and model weights?
    answer: >-
      Create data and model directories in your home folder, then install rclone using the provided
      installation script. Run rclone config and use it to download the required datasets and
      weights as shown in the steps.
  - question: Which frameworks and versions are used to run the benchmark?
    answer: >-
      You will run a modified MLPerf benchmark for DLRM using PyTorch 2.9.0+cpu. The steps use
      a repository of scripts tailored for Arm-based systems.
  - question: How do I run the benchmark and confirm it completed successfully?
    answer: >-
      Clone the provided repository and run the included scripts to execute the DLRM benchmark.
      After the run, inspect the generated results as directed in the Learning Path to validate
      completion.
# END generated_summary_faq

author: 
    - Phalani Paladugu
    - Annie Tallund
    - Pareena Verma

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Google Cloud
armips:
    - Neoverse
tools_software_languages:
    - Docker
    - MLPerf
    - Google Cloud
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: MLPerf Inference Benchmarks for Recommendation
        link: https://github.com/mlcommons/inference/tree/master/recommendation/dlrm_v2/pytorch
        type: documentation
    - resource:
        title: MLPerf Inference Benchmark Suite
        link: https://github.com/mlcommons/inference/tree/master
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

