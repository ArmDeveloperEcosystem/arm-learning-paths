---
title: Measure application resource and power usage on Windows on Arm with FFmpeg and PowerShell

description: Learn how to measure application resource usage, benchmark video encoding tasks, and monitor CPU, memory, and power consumption on Windows on Arm using FFmpeg and PowerShell.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to measure resource usage of applications on Windows on Arm devices using FFmpeg.

learning_objectives: 
    - Measure application resource usage using FFmpeg and PowerShell
    - Benchmark a video encoding task
    - Monitor CPU, memory, and power consumption during a video decode task

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11
    - A code editor such as [Visual Studio Code for Windows on Arm](https://code.visualstudio.com/docs/?dv=win32arm64user) 

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:14:27Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: fc0d79605640cc8e7a36070a044323d6e278335484949921d0aa4e9cd163d4bd
  summary_generated_at: '2026-06-01T22:10:37Z'
  summary_source_hash: fc0d79605640cc8e7a36070a044323d6e278335484949921d0aa4e9cd163d4bd
  faq_generated_at: '2026-06-02T23:14:27Z'
  faq_source_hash: fc0d79605640cc8e7a36070a044323d6e278335484949921d0aa4e9cd163d4bd
  summary: >-
    Learn how to measure application resource and power usage on Windows on Arm using FFmpeg and
    PowerShell. You will set up FFmpeg, encode a test video, and run a decoding workload while
    PowerShell scripts record CPU and memory usage to CSV for later analysis. You will also sample
    battery status to measure power consumption without external equipment. The workflow includes
    running the same tests with an x86_64 FFmpeg binary under Windows instruction emulation and
    an Arm64 native build to compare behavior. Prerequisites are a Windows on Arm device such
    as a Lenovo Thinkpad X13s running Windows 11 and a code editor such as Visual Studio Code
    for Windows on Arm. Estimated time: 60 minutes.
  faqs:
  - question: What do I need before running the scripts?
    answer: >-
      You need a Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 and
      a code editor such as Visual Studio Code for Windows on Arm. The Learning Path uses FFmpeg
      and PowerShell.
  - question: Which FFmpeg binaries should I use for the tests?
    answer: >-
      Run the same tests with both the x86_64 binary (using Windows instruction emulation) and
      the Arm64 native binary. This lets you compare results on the same device.
  - question: How do I capture CPU and memory usage during decoding, and what output should I
      expect?
    answer: >-
      Use the provided PowerShell script saved as sample_decoding.ps1. It launches the decoding
      process, periodically records CPU and memory statistics, and writes them to a CSV file.
  - question: How is power usage measured without extra hardware?
    answer: >-
      Use the sample_power.ps1 PowerShell script to sample battery status while the decoding task
      runs. The script logs readings to a CSV file for analysis.
  - question: How should I compare results between Arm64 and x86_64 runs?
    answer: >-
      Execute identical workloads with each binary and compare the generated CSV files for CPU,
      memory, and battery metrics. Use these data to benchmark the encoding task and analyze decoding
      resource usage.
# END generated_summary_faq

author: Ruifeng Wang

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
tools_software_languages:
    - FFmpeg
    - PowerShell
operatingsystems:
    - Windows



further_reading:
    - resource:
        title: Recording for resource-based analysis
        link: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-8.1-and-8/hh448202(v=win.10)
        type: documentation
    - resource:
        title: Get started with Arm64EC
        link: https://learn.microsoft.com/en-us/windows/arm/arm64ec-build
        type: documentation
    - resource:
        title: Arm64EC - Build and port apps for native performance on Arm
        link: https://learn.microsoft.com/en-us/windows/arm/arm64ec
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

