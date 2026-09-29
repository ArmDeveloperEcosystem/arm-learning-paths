---
title: Measure machine learning inference performance on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers interested in benchmarking machine learning workloads on Arm servers.

description: Benchmark machine learning inference performance on Arm servers using TensorFlow and the MLPerf Inference benchmark suite from MLCommons.

learning_objectives:
- Install and run TensorFlow on your Arm-based cloud server.
- Use MLPerf Inference benchmark suite, an open-sourced benchmark from MLCommons, to test ML performance on your Arm server.

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate cloud service provider, or an on-premise Arm server

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:51:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 811148e908194f3a554b84121e223bfa2f29d5f0bf957480142bc691bd6a24f1
  summary_generated_at: '2026-09-28T19:51:15Z'
  summary_source_hash: 811148e908194f3a554b84121e223bfa2f29d5f0bf957480142bc691bd6a24f1
  faq_generated_at: '2026-09-28T19:51:15Z'
  faq_source_hash: 811148e908194f3a554b84121e223bfa2f29d5f0bf957480142bc691bd6a24f1
  summary: >-
    You'll prepare an Arm-based Ubuntu cloud server to run MLPerf Inference benchmarks. First,you set up either an AWS Graviton-based instance
    or OCI Ampere Compute, then install the required build tools, Python packages, and TensorFlow.
    After configuring the environment with `apt` and `pip`, you'll run the MLCommons MLPerf Inference
    suite. With the resulting benchmark output, you can verify the setup and record inference performance
    for your system.
  faqs:
  - question: Which Ubuntu version should I use on my instance?
    answer: >-
      Use Ubuntu 20.04 or Ubuntu 22.04 on your Arm-based server. The Learning Path has been tested
      with both versions.
  - question: Is there any difference in procedures between AWS and OCI?
    answer: >-
      No. You can use the same procedure on AWS Graviton or OCI Ampere Compute with Ubuntu 20.04
      or 22.04.
  - question: How do I select the backend, model, and device for the benchmark?
    answer: >-
      Pass the backend, model, and device to `run_local.sh` in that order. For the example in this
      Learning Path, run `./run_local.sh tf resnet50 cpu` to use TensorFlow with ResNet-50 on the
      CPU. Run `./run_local.sh --help` to view the other supported options.
  - question: Which packages should I install before running the benchmarks?
    answer: >-
      Update your packages, then install `build-essential`, `python3-pip`, and `git` with `apt-get`.
      Install Python dependencies such as `opencv-python-headless` and `Cython` with `pip`.
  - question: What result should I expect after running the MLPerf Inference suite?
    answer: >-
      Confirm that the run produces benchmark output for your tested configuration. Save these
      results to record your system’s inference performance.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - AWS Graviton
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
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
