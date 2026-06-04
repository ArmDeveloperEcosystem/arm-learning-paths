---
title: Profile the Performance of AI and ML Mobile Applications on Arm
description: Learn how to profile ML model execution times and application performance on Arm Android devices using Arm Performance Studio and Android Studio Profiler.
minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to learn how to profile the performance of Machine Learning (ML) models running on Arm devices.

learning_objectives: 
    - Profile the execution times of ML models on Arm devices.
    - Profile ML application performance on Arm devices.
    - Describe how profiling can help optimize the performance of Machine Learning applications.

prerequisites:
    - An Arm-powered Android smartphone, and a USB cable to connect to it.
    - For profiling the ML inference, [Arm NN ExecuteNetwork](https://github.com/ARM-software/armnn/releases) or [ExecuTorch](https://github.com/pytorch/executorch).
    - For profiling the application, [Arm Performance Studio with Streamline](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio).
    - Android Studio Profiler.
  

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:04:25Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 01138f6538c655f866fb034a983461b2ac9b793142775465233b2ec8ec18d0c5
  summary_generated_at: '2026-06-02T02:56:03Z'
  summary_source_hash: 01138f6538c655f866fb034a983461b2ac9b793142775465233b2ec8ec18d0c5
  faq_generated_at: '2026-06-03T00:04:25Z'
  faq_source_hash: 01138f6538c655f866fb034a983461b2ac9b793142775465233b2ec8ec18d0c5
  summary: >-
    Learn how to profile ML model execution times and end-to-end application behavior on Arm-powered
    Android devices using Arm Performance Studio (Streamline), Android Studio Profiler, and framework-level
    tools. This introductory path shows how to identify bottlenecks across CPU, memory, cache,
    and GPU counters with a sampling profiler, monitor Android app memory usage and leaks, and
    extract per-layer timings from ML models. You will connect an Arm-based Android smartphone
    via USB, run profiling sessions, and interpret timeline and layer-level outputs. Prerequisites
    include an Arm-powered Android smartphone with a USB cable, Android Studio Profiler, Arm Performance
    Studio with Streamline, and either Arm NN ExecuteNetwork or ExecuTorch. Estimated time to
    complete is about 60 minutes.
  faqs:
  - question: What do I need before running the profiling steps?
    answer: >-
      You need an Arm-powered Android smartphone and a USB cable. For inference profiling, have
      Arm NN ExecuteNetwork or ExecuTorch. For application profiling, install Arm Performance
      Studio with Streamline and use Android Studio Profiler.
  - question: How do I set up Android Studio Profiler to examine memory?
    answer: >-
      Open your project in Android Studio, go to View > Tool Windows > Profiler to open the Profiler
      window. Connect your device in Developer Mode via USB and select your app’s process. You
      can then monitor memory usage and look for leaks.
  - question: Which profiler should I use for system behavior versus memory analysis?
    answer: >-
      Use Streamline (part of Arm Performance Studio) for system-wide sampling of performance
      metrics with low overhead. Use Android Studio Profiler to focus on app memory usage and
      leak detection.
  - question: What output should I expect from Arm NN ExecuteNetwork when profiling a LiteRT model?
    answer: >-
      ExecuteNetwork runs the model outside the rest of the app and reports per-layer timings
      and other useful information. This helps pinpoint bottlenecks inside the network. If you
      are using LiteRT without Arm NN, treat the output as indicative rather than definitive.
  - question: Which performance metrics does Streamline provide during sampling?
    answer: >-
      Streamline samples system counters such as memory, CPU activity and cycles, cache misses,
      and many parts of the GPU. It also provides a timeline view to visualize how these metrics
      evolve during execution.
# END generated_summary_faq

author: Ben Clark

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Mali
    - Immortalis
tools_software_languages:
    - Android Studio
    - LiteRT
    - Hugging Face

operatingsystems:
    - Android
    - Linux


further_reading:
    - resource:
        title: Arm Streamline User Guide  
        link: https://developer.arm.com/documentation/101816/latest/
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

