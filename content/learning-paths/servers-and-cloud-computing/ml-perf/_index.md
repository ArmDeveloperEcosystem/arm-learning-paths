---
title: Measure Machine Learning Inference Performance on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers interested in benchmarking machine learning workloads on Arm servers.

description: Benchmark machine learning inference performance on Arm servers using TensorFlow and the MLPerf Inference benchmark suite from MLCommons.

learning_objectives:
- Install and run TensorFlow on your Arm-based cloud server
- Use MLPerf Inference benchmark suite, an open-sourced benchmark from MLCommons to test ML performance on your Arm server

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider or an on-premise Arm server.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 973ba6c1e00fc67e1702606412124d8172e071b9b677a1df53c3be66210bf704
  summary: >-
    Benchmark machine learning inference performance on Arm servers using TensorFlow and the MLPerf
    Inference benchmark suite from MLCommons. It is designed for software developers interested
    in benchmarking machine learning workloads on Arm servers. By the end, you will be able to
    install and run TensorFlow on your Arm-based cloud server and use MLPerf Inference benchmark
    suite, an open-sourced benchmark from MLCommons to test ML performance on your Arm server.
    It focuses on tools and technologies such as TensorFlow and Runbook, Linux environments, Arm
    platforms including Neoverse, and cloud platforms such as AWS and Oracle. The main steps cover
    Measure ML Inference Performance on Arm servers.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install and run TensorFlow on your Arm-based cloud server and use MLPerf Inference
      benchmark suite, an open-sourced benchmark from MLCommons to test ML performance on your
      Arm server. Benchmark machine learning inference performance on Arm servers using TensorFlow
      and the MLPerf Inference benchmark suite from MLCommons.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers interested in benchmarking machine
      learning workloads on Arm servers.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/)
      from an appropriate cloud service provider or an on-premise Arm server.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including TensorFlow and Runbook, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as AWS and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Measure ML Inference Performance on Arm servers.
# END generated_summary_faq

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

