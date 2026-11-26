---
title: Android Runtime Performance Analysis using ADB

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers exploring performance analysis, particularly for Android applications running LiteRT-LM models on Arm hardware.

learning_objectives: 
    - Wirelessly connect, monitor and push an application to an Android device
    - Extract key runtime performance metrics from an application
    - Visualise performance by plotting graphs from collected data
    - Create a consolidated analysis pipeline using Jupyter Notebook

prerequisites:
    - A working environment with Python 3.10+, Git, curl and Homebrew installed
    - An Android device with developer mode, Android 11 or later and at least 5 GB of free storage
    - Basic understanding of how to create and run Jupyter Notebooks

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-16T14:03:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e37c08b32761ed7070a526ef01709ed90b65020241fdbea1440c54866be8748f
  summary_generated_at: '2026-11-16T14:03:08Z'
  summary_source_hash: e37c08b32761ed7070a526ef01709ed90b65020241fdbea1440c54866be8748f
  faq_generated_at: '2026-11-16T14:03:08Z'
  faq_source_hash: e37c08b32761ed7070a526ef01709ed90b65020241fdbea1440c54866be8748f
  summary: >-
    This Learning Path shows how to measure Android runtime performance on Arm-based devices using
    ADB and Perfetto. You set up a macOS host with Android SDK tools, enable wireless debugging,
    and clone the PhotoTalk LiteRT-LM sample. The app is instrumented by adding logs around its
    Conversation API to expose runtime metrics. Monitoring assets are prepared, including a script
    that a Jupyter Notebook calls to collect device telemetry over wireless ADB for a chosen duration.
    With the app configured and exercised on the device, traces and logs are captured for plotting
    and consolidated analysis in the Notebook, allowing learners to interpret runtime behavior
    from device-side metrics.
  faqs:
  - question: How do I know the device is ready for wireless ADB?
    answer: >-
      Open Developer options and confirm Wireless debugging is enabled and shows an active pairing.
      The screen displays the connection details used for wireless debugging.
  - question: Should I keep the USB cable connected while collecting data?
    answer: >-
      No. Use wireless debugging to avoid USB charging, which can distort power-related measurements
      during monitoring.
  - question: Which parts of PhotoTalk do I modify to log LiteRT-LM metrics?
    answer: >-
      Update the Conversation API call sites to record LiteRT-LM runtime metrics. PhotoTalk does
      not log these metrics by default, so add instrumentation where the API is invoked.
  - question: What should I do in PhotoTalk before starting a capture?
    answer: >-
      Open the app, tap Select Image, and ensure you have at least one non-sensitive image ready.
      Use the settings (cog icon) to configure the model backend you plan to test.
  - question: What result should I expect after running the monitoring script?
    answer: >-
      The script collects device data for the specified duration over wireless ADB. Review the
      script comments to see what files it writes; those artifacts are then used in the Jupyter
      Notebook for plotting.
# END generated_summary_faq

author: Dylan Rees

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
tools_software_languages:
    - Bash
    - Python
    - Jupyter Notebook
    - ADB
    - Perfetto
operatingsystems:
    - Android
    - macOS

further_reading:
    - resource:
        title: Run apps on a hardware device
        link: https://developer.android.com/studio/run/device
        type: documentation
    - resource:
        title: LiteRT for Android
        link: https://ai.google.dev/edge/litert/android
        type: documentation
    - resource:
        title: perfetto
        link: https://developer.android.com/tools/perfetto
        type: documentation
    - resource:
        title: Overview of measuring app performance
        link: https://developer.android.com/topic/performance/measuring-performance
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

