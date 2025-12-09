---
title: Building and Benchmarking DLRM on Arm Neoverse V2 with MLPerf


minutes_to_complete: 90

who_is_this_for: This is an introductory topic for software developers who want to set up a pipeline in the cloud for recommendation models. You'll build and run the Deep Learning Recommendation Model (DLRM) and benchmark its performance using MLPerf and PyTorch.

learning_objectives:
    - Build the Deep Learning Recommendation Model (DLRM). 
    - Run a modified performant DLRMv2 benchmark and inspect the results.

prerequisites:
    - Any [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider (CSP), or an on-premise Arm server with at least 400GB of RAM and 800 GB of disk space.

author: 
    - Phalani Paladugu
    - Annie Tallund
    - Pareena Verma

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Docker
    - MLPerf
    - Google Cloud
operatingsystems:
    - Linux
cloud_service_providers: AWS

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
