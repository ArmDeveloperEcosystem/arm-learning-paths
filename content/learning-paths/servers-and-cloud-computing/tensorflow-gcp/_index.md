---
title: Deploy TensorFlow on Google Cloud C4A (Arm-based Axion VMs)
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers deploying and optimizing TensorFlow workloads on Arm64 Linux environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors)
  - Install TensorFlow on a SUSE Arm64 (C4A) instance
  - Verify TensorFlow by running basic computation and model training tests on Arm64
  - Benchmark TensorFlow using TensorFlow Keras (`tf.keras`) to evaluate inference speed and model performance on Arm64 systems

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [TensorFlow](https://www.tensorflow.org/)

generate_summary_faq: false
rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:10:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2c20d30d25a0bb871bdb935d18f7ad8e0740139948133dbd728e10f0add0f94e
  summary_generated_at: '2026-06-02T05:17:09Z'
  summary_source_hash: 2c20d30d25a0bb871bdb935d18f7ad8e0740139948133dbd728e10f0add0f94e
  faq_generated_at: '2026-06-03T02:10:01Z'
  faq_source_hash: 2c20d30d25a0bb871bdb935d18f7ad8e0740139948133dbd728e10f0add0f94e
  summary: >-
    Provision an Arm-based SUSE Linux Enterprise Server (SLES) VM on Google Cloud C4A (Axion,
    Neoverse-V2) and set up a working TensorFlow environment on Arm64. You will create a c4a-standard-4
    instance, install Python 3.11 with pip and virtual environment support, and install TensorFlow
    on SLES. The path guides you to verify the installation by listing available devices and running
    basic TensorFlow operations and a simple training test on the CPU. You then benchmark ResNet50,
    MobileNetV2, and InceptionV3 with tf.keras using dummy data to measure average inference time
    and throughput. Prerequisites are a GCP account with billing enabled and basic familiarity
    with TensorFlow. Estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running this Learning Path, and how long will it take?
    answer: >-
      You need a Google Cloud Platform (GCP) account with billing enabled and basic familiarity
      with TensorFlow. The path is introductory and is designed to take about 30 minutes.
  - question: Which VM configuration and OS should I select on Google Cloud to match the steps?
    answer: >-
      Choose the C4A series and the c4a-standard-4 machine type (4 vCPUs, 16 GB memory). Use a
      SUSE Linux Enterprise Server (SLES) Arm64 image, then set your region and zone.
  - question: Which Python version is used and how do I install the prerequisites for TensorFlow?
    answer: >-
      The steps install Python 3.11, pip, and virtual environment support using zypper on SLES.
      After that, you install TensorFlow and continue with testing and benchmarking on Arm64.
  - question: How do I verify that TensorFlow is correctly installed and recognizes the hardware?
    answer: >-
      Run: python -c "import tensorflow as tf; print(tf.config.list_physical_devices())". On most
      VMs you should see a CPU device listed; the baseline section also runs simple ops and a
      small training test.
  - question: What models are benchmarked and what metrics are collected in this path?
    answer: >-
      You benchmark ResNet50, MobileNetV2, and InceptionV3 using tf.keras with dummy input data.
      The procedure measures average inference time and throughput on the CPU of the Arm-based
      VM.
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
  - TensorFlow
  - Python
  - Keras

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
      title: TensorFlow documentation
      link: https://www.tensorflow.org/learn
      type: documentation
  - resource:
      title: Phoronix Test Suite (PTS) documentation
      link: https://www.phoronix-test-suite.com/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

