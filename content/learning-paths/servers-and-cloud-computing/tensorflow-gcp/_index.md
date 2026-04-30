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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: 2c20d30d25a0bb871bdb935d18f7ad8e0740139948133dbd728e10f0add0f94e
  summary: >-
    Deploy TensorFlow on Google Cloud C4A (Arm-based Axion VMs) walks you through an end-to-end
    Arm software workflow. It is designed for software developers deploying and optimizing TensorFlow
    workloads on Arm64 Linux environments, specifically using Google Cloud C4A virtual machines
    powered by Axion processors. By the end, you will be able to provision an Arm-based SUSE Linux
    Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors), install
    TensorFlow on a SUSE Arm64 (C4A) instance, and verify TensorFlow by running basic computation
    and model training tests on Arm64. It focuses on tools and technologies such as TensorFlow,
    Python, and Keras, Linux environments, Arm platforms including Neoverse, and cloud platforms
    such as Google Cloud. The main steps cover Get started with TensorFlow on Google Axion C4A,
    Create a Google Axion C4A Arm virtual machine on GCP, Install TensorFlow, Test TensorFlow
    baseline performance on Google Axion C4A, and Benchmark TensorFlow model performance using
    tf.keras.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google
      Cloud (C4A with Axion processors), install TensorFlow on a SUSE Arm64 (C4A) instance, and
      verify TensorFlow by running basic computation and model training tests on Arm64.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers deploying and optimizing TensorFlow
      workloads on Arm64 Linux environments, specifically using Google Cloud C4A virtual machines
      powered by Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [TensorFlow](https://www.tensorflow.org/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including TensorFlow, Python, and Keras, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with TensorFlow on Google Axion C4A, Create
      a Google Axion C4A Arm virtual machine on GCP, Install TensorFlow, Test TensorFlow baseline
      performance on Google Axion C4A, and Benchmark TensorFlow model performance using tf.keras.
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

