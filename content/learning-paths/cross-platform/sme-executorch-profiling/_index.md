---
title: Profile ExecuTorch models with SME2 on Arm

minutes_to_complete: 90

description: Learn how to profile and optimize ExecuTorch models using SME2 acceleration on Arm platforms, including operator-level analysis and performance bottleneck identification.

who_is_this_for: This is an advanced topic for developers and performance engineers who deploy ExecuTorch models on Arm devices and want to understand and reduce inference latency.

learning_objectives:
  - Understand how SME2 acceleration changes the performance profile of ExecuTorch models by reducing compute-bound bottlenecks
  - Interpret operator-level and operator-category breakdowns (for example, convolution, GEMM, data movement, and other operators)
  - Identify which operators benefit most from SME2 acceleration and which operators become the new performance bottlenecks
  - Apply a model-agnostic profiling workflow that you reuse across different models and deployments
  - Make evidence-based optimization decisions by comparing execution profiles with SME2 enabled and disabled

prerequisites:
  - An Apple Silicon macOS host with Python 3.9 or later and CMake 3.29 or later
  - Basic familiarity with ExecuTorch or PyTorch
  - Optionally, an Android device with Armv9 and SME2 support for on-device testing (if used, configure power management settings to ensure consistent performance measurements)
    

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: 36f7dfe13c8c940abbaad2b61620b3b1c6d97f580de15e573b45ef7760753797
  summary: >-
    Learn how to profile and optimize ExecuTorch models using SME2 acceleration on Arm platforms,
    including operator-level analysis and performance bottleneck identification. It is designed
    for developers and performance engineers who deploy ExecuTorch models on Arm devices and want
    to understand and reduce inference latency. By the end, you will be able to understand how
    SME2 acceleration changes the performance profile of ExecuTorch models by reducing compute-bound
    bottlenecks, interpret operator-level and operator-category breakdowns (for example, convolution,
    GEMM, data movement, and other operators), and identify which operators benefit most from
    SME2 acceleration and which operators become the new performance bottlenecks. It focuses on
    tools and technologies such as ExecuTorch, Python, CMake, and SME2, macOS and Android environments,
    and Arm platforms including Cortex-A and Arm C1. The main steps cover Explore ExecuTorch profiling
    with SME2, Set up the ExecuTorch profiling environment, Export PyTorch models and analyze
    performance, and Automate profiling workflows with AI agents.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will understand how SME2 acceleration changes the performance profile of ExecuTorch
      models by reducing compute-bound bottlenecks, interpret operator-level and operator-category
      breakdowns (for example, convolution, GEMM, data movement, and other operators), and identify
      which operators benefit most from SME2 acceleration and which operators become the new performance
      bottlenecks. Learn how to profile and optimize ExecuTorch models using SME2 acceleration
      on Arm platforms, including operator-level analysis and performance bottleneck identification.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers and performance engineers who deploy ExecuTorch
      models on Arm devices and want to understand and reduce inference latency.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Apple Silicon macOS host with Python
      3.9 or later and CMake 3.29 or later; Basic familiarity with ExecuTorch or PyTorch; Optionally,
      an Android device with Armv9 and SME2 support for on-device testing (if used, configure
      power management settings to ensure consistent performance measurements).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including ExecuTorch, Python, CMake, and SME2, macOS and Android
      environments, and Arm platforms such as Cortex-A and Arm C1.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Explore ExecuTorch profiling with SME2, Set up the
      ExecuTorch profiling environment, Export PyTorch models and analyze performance, and Automate
      profiling workflows with AI agents.
# END generated_summary_faq

author: Jason Zhu, Tyler Mullenbach, Damien Dooley 

### Tags
skilllevels: Advanced
subjects: ML
armips:
  - Cortex-A
  - Arm C1
tools_software_languages:
  - ExecuTorch
  - Python
  - CMake
  - SME2
operatingsystems:
  - macOS
  - Android

shared_path: true
shared_between:
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
  - resource:
      title: ExecuTorch documentation
      link: https://docs.pytorch.org/executorch/stable/index.html
      type: documentation
  - resource:
      title: Arm SME2 overview
      link: https://www.arm.com/technologies/sme2
      type: documentation
  - resource:
      title: Arm Kleidi kernels
      link: https://www.arm.com/markets/artificial-intelligence/software/kleidi
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

