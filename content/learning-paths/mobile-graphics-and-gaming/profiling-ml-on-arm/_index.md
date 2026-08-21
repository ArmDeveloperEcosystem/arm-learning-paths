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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:25:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e6ab6eb40ee7bed0aa103d317e7bfed612abe7e36a7fe0118371ae3ec89f4d0c
  summary_generated_at: '2026-08-21T17:25:11Z'
  summary_source_hash: e6ab6eb40ee7bed0aa103d317e7bfed612abe7e36a7fe0118371ae3ec89f4d0c
  faq_generated_at: '2026-08-21T17:25:11Z'
  faq_source_hash: e6ab6eb40ee7bed0aa103d317e7bfed612abe7e36a7fe0118371ae3ec89f4d0c
  summary: >-
    Profile the performance of an ML application on an Arm-powered Android device. You use
    Streamline to sample system performance metrics and view them on a timeline, then use Android
    Studio Profiler to investigate memory use and leaks. You also use Arm NN `ExecuteNetwork` to
    run a LiteRT model outside your app, examine its layer timings, and identify model bottlenecks.
    Finally, you adapt ExecuTorch profiling tools for Android.
  faqs:
  - question: How do I know Android Studio is profiling the correct app process?
    answer: >-
      Open the **Profiler** window, attach your device in **Developer Mode** with a USB cable, and
      select your app's process.
  - question: Which profiling approach should I use in Streamline?
    answer: >-
      Streamline is a sampling profiler, which provides a statistical view with lower overhead
      than instrumentation. Use it to capture system counters and timeline data while the app
      runs.
  - question: What results should I expect from `ExecuteNetwork` with a LiteRT model?
    answer: >-
      `ExecuteNetwork` runs the model without the rest of your app and outputs layer timings and
      other information that can help identify bottlenecks. If you use LiteRT without Arm NN,
      treat the output as indicative rather than definitive.
  - question: How do I check whether inference is the main bottleneck?
    answer: >-
      Use Streamline annotations to mark inference, preprocessing, and postprocessing in the
      timeline. You can then see where your app spends time and how hard the CPU or GPU is working
      during each part. For a LiteRT model, use `ExecuteNetwork` to identify bottlenecks within
      the model.
  - question: Can I profile a PyTorch model with ExecuTorch on Android?
    answer: >-
      Yes. ExecuTorch provides profiling tools for PyTorch models. The tools target Linux, but you
      can adapt the Linux instructions for Android by generating the ETDump file on your Android
      device and analyzing it with an ExecuTorch Inspector.
# END generated_summary_faq

author: Ben Clark

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
