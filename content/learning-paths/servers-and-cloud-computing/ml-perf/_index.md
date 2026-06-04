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
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:31:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 973ba6c1e00fc67e1702606412124d8172e071b9b677a1df53c3be66210bf704
  summary_generated_at: '2026-06-02T04:26:55Z'
  summary_source_hash: 973ba6c1e00fc67e1702606412124d8172e071b9b677a1df53c3be66210bf704
  faq_generated_at: '2026-06-03T01:31:54Z'
  faq_source_hash: 973ba6c1e00fc67e1702606412124d8172e071b9b677a1df53c3be66210bf704
  summary: >-
    Set up an Arm-based Linux server and benchmark machine learning inference using TensorFlow
    and the MLPerf Inference benchmark suite from MLCommons. You will launch an Arm instance running
    Ubuntu 20.04 or 22.04, install required system and Python packages, then configure and run
    TensorFlow with the MLPerf Inference suite to measure performance. This introductory path
    has been tested on AWS and Oracle cloud platforms and also applies to on-premise Arm servers.
    The only explicit prerequisite is access to an Arm-based instance. By the end, you will have
    executed MLPerf Inference on your Arm server and obtained benchmark results in about 20 minutes.
  faqs:
  - question: What do I need before running the benchmarks?
    answer: >-
      You need an Arm-based instance from a cloud service provider or an on-premise Arm server
      running Ubuntu 20.04 or Ubuntu 22.04. This path has been tested on AWS and Oracle. No other
      explicit prerequisites are listed.
  - question: Which Ubuntu version should I choose for this path?
    answer: >-
      Use Ubuntu 20.04 or Ubuntu 22.04, as shown in the steps. Both were tested on AWS and Oracle.
  - question: Which packages do I install to prepare the environment?
    answer: >-
      Update apt and install build-essential, python3-pip, and git, then use pip to install the
      Python packages listed in the steps (for example, opencv-python-headless and Cython). Follow
      the exact apt-get and pip commands provided.
  - question: How are TensorFlow and MLPerf Inference used here?
    answer: >-
      You will install and run TensorFlow on your Arm server, then use the MLPerf Inference benchmark
      suite from MLCommons to test ML inference performance.
  - question: How long will this take and what result should I expect?
    answer: >-
      The path is estimated to take about 20 minutes. On completion, you will have run TensorFlow
      and executed the MLPerf Inference suite to produce benchmark output on your Arm server.
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

