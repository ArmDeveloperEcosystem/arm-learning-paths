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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:16:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8b3ee8a0d24866ac73b60bf91b7414d8d73046ff37e89d9f34a2b17e8986b6e0
  summary_generated_at: '2026-08-11T16:16:08Z'
  summary_source_hash: 8b3ee8a0d24866ac73b60bf91b7414d8d73046ff37e89d9f34a2b17e8986b6e0
  faq_generated_at: '2026-08-11T16:16:08Z'
  faq_source_hash: 8b3ee8a0d24866ac73b60bf91b7414d8d73046ff37e89d9f34a2b17e8986b6e0
  summary: >-
    You'll use FFmpeg and PowerShell on Windows on Arm to compare native Arm64 and emulated x86_64
    video workloads. You'll encode a test video, then run scripts that sample CPU, memory, and
    battery data during decoding. You'll save the measurements to CSV files and repeat the runs
    with each FFmpeg build to make side-by-side comparisons.
  faqs:
  - question: Which FFmpeg executable should I pass to the scripts for Arm64 versus x86_64?
    answer: >-
      Set the `exePath` parameter to the specific FFmpeg or FFplay binary that you want to run. Use the
      Arm64-native build for Arm execution, or point to an x86_64 build to run under Windows instruction
      emulation.
  - question: How do I know the resource monitoring script is recording data?
    answer: >-
      While the decode task runs, the script writes samples to a CSV file. Check that the CSV
      file appears and grows over time, and that it contains headers and rows with CPU and memory
      values.
  - question: What should I check if FFmpeg fails to encode or decode the sample video?
    answer: >-
      Verify the input and output file paths and confirm the arguments match the media you are
      using. Ensure `exePath` points to a valid FFmpeg or FFplay binary and review the console output
      for specific errors.
  - question: Where does the script save the CSV files and what should be in them?
    answer: >-
      The output file name and path are defined in each script; open the script to confirm or
      change the location. Expect timestamped rows with the recorded metrics, such as CPU and
      memory for resource sampling, or battery-related fields for power sampling.
  - question: How do I run a like-for-like comparison between the Arm64 and x86_64 builds?
    answer: >-
      Use the same media file, the same command arguments, and the same sampling settings for
      both runs. Point `exePath` to each build in turn and compare the resulting CSV files.
# END generated_summary_faq

author: Ruifeng Wang

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
