---
armips:
- Neoverse
author: Pareena Verma
layout: learningpathall
learning_objectives:
- Install and run TensorFlow on your Arm-based cloud server.
- Use MLPerf Inference benchmark suite, an open-sourced benchmark from MLCommons to
  test ML performance on your Arm server.
learning_path_main_page: 'yes'
minutes_to_complete: 20
operatingsystems:
- Linux
prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider or an on-premise Arm server.
skilllevels: Introductory
subjects: ML
test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true
test_status:
- passed
title: Measure Machine Learning Inference Performance on Arm servers
tools_software_languages:
- TensorFlow
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
        link: https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/machine-learning-inference-on-aws-graviton3
        type: blog



weight: 1
who_is_this_for: This is an introductory topic for software developers interested
  in benchmarking machine learning workloads on Arm servers.
---
