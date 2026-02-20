---
title: Measure Machine Learning Inference Performance on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers interested
  in benchmarking machine learning workloads on Arm servers.


learning_objectives:
- Install and run TensorFlow on your Arm-based cloud server.
- Use MLPerf Inference benchmark suite, an open-sourced benchmark from MLCommons to
  test ML performance on your Arm server.

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider or an on-premise Arm server.

author: Pareena Verma

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
  - Oracle
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- TensorFlow
- Runbook

further_reading:
    - resource:
        title: MLPerf Inference Suite Source repo 
        link: https://github.com/mlcommons/inference/tree/master/vision/classification_and_detection
        type: documentation
    - resource:
        title: Tutorial on how to use mlperf inference reference benchmark
        link: https://github.com/mlcommons/inference/blob/master/vision/classification_and_detection/GettingStarted.ipynb
        type: documentation
    - resource:
        title: Machine Learning Inference on AWS Graviton3
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/machine-learning-inference-on-aws-graviton3
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
