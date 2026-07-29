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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:51:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 82716c2de19d18a154c85d03b7f2ec01839284262914f7bb3ad04b18a105379d
  summary_generated_at: '2026-07-27T18:51:58Z'
  summary_source_hash: 82716c2de19d18a154c85d03b7f2ec01839284262914f7bb3ad04b18a105379d
  faq_generated_at: '2026-07-27T18:51:58Z'
  faq_source_hash: 82716c2de19d18a154c85d03b7f2ec01839284262914f7bb3ad04b18a105379d
  summary: >-
    You'll prepare an Arm Neoverse V2 server, download the DLRM dataset and model weights with `rclone`,
    and run a modified MLPerf DLRM benchmark. You'll create dedicated directories, clone the provided
    repository, use PyTorch 2.9.0+cpu with Arm-focused optimizations, and execute the benchmark.
    You'll then inspect the output to confirm a successful run and review the results.
  faqs:
  - question: How do I know I’ve installed `rclone` correctly, and do I need to configure it before downloading?
    answer: >-
      After the install script reports that `rclone` installed successfully, run `rclone config`
      before downloading the data and model weights.
  - question: Which directories should contain the downloaded dataset and model weights?
    answer: >-
      Create data and model directories under your home directory, for example `$HOME/data` and
      `$HOME/model`. Download the dataset into `data` and the model weights into `model`.
  - question: Which PyTorch build does the benchmark use?
    answer: >-
      The benchmark uses PyTorch 2.9.0+cpu with optimizations for recommendation models on Arm.
      Use the build referenced by the provided scripts.
  - question: How do I know the benchmark finished correctly, and where do I view the results?
    answer: >-
      The run prints benchmark progress and produces results you can inspect after completion.
      Review the script output and confirm that the run completed without errors.
  - question: What should I check if the download or benchmark fails partway through?
    answer: >-
      Verify the instance meets the stated resource requirements and that sufficient RAM and disk
      space are available. Also confirm that the dataset and model weights reached the expected
      directories before rerunning.
# END generated_summary_faq

author: 
    - Phalani Paladugu
    - Annie Tallund
    - Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
