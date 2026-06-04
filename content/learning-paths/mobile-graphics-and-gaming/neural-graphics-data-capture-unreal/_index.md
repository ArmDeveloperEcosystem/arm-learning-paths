---
title: Generate neural graphics datasets with Neural Graphics Data Capture in Unreal Engine
description: Learn how to capture high-quality frame datasets from Unreal Engine 5.5 gameplay for training and evaluating neural graphics models like Neural Super Sampling.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for Unreal Engine developers who want to generate high-quality frame datasets for training and evaluating neural graphics models.

learning_objectives:
    - Understand why Neural Graphics Data Capture is useful in a neural graphics workflow.
    - Install and enable the Neural Graphics Data Capture plugin in Unreal Engine 5.5.
    - Configure a Level Blueprint to start and stop capture with hotkeys.
    - Run Standalone capture and verify exported dataset outputs.

prerequisites:
    - Windows 11
    - Unreal Engine 5.5 installed
    - Visual Studio with C++ game development tools
    - A C++ Unreal project (such as the Third Person template)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:59:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5ca059af36f0ba375701e76ce82b7803f01ae6beab313336b333bfbdebaa3b1a
  summary_generated_at: '2026-06-02T02:53:51Z'
  summary_source_hash: 5ca059af36f0ba375701e76ce82b7803f01ae6beab313336b333bfbdebaa3b1a
  faq_generated_at: '2026-06-02T23:59:40Z'
  faq_source_hash: 5ca059af36f0ba375701e76ce82b7803f01ae6beab313336b333bfbdebaa3b1a
  summary: >-
    Learn how to capture high-quality frame datasets from Unreal Engine 5.5 gameplay using the
    Neural Graphics Data Capture plugin on Windows. You will install and enable the plugin in
    a C++ Unreal project, wire up a Level Blueprint to start (C) and stop (V) capture, run in
    Standalone Game mode to record frames at the correct dimensions, and verify the exported dataset.
    The path also introduces key capture settings, including UpscalingRatio, SupersamplingRatio,
    FixedFrameRate, camera cut thresholds, and output path controls (DatasetDir, CaptureName).
    Prerequisites include Windows 11, Unreal Engine 5.5, Visual Studio with C++ game development
    tools, and a C++ project. Suitable for developers preparing data for Neural Super Sampling
    and related temporal upscalers.
  faqs:
  - question: What do I need before running the capture workflow?
    answer: >-
      You need Windows 11, Unreal Engine 5.5 installed, Visual Studio with C++ game development
      tools, and a C++ Unreal project. A template project like Third Person is suitable.
  - question: How do I install and enable the Neural Graphics Data Capture plugin in my project?
    answer: >-
      Clone the plugin’s GitHub repository, then copy the NeuralGraphicsDataCapture folder into
      your project’s Plugins directory. Open the project so the module compiles via Visual Studio,
      then enable the plugin in Unreal.
  - question: How do I set up hotkeys to start and stop capture?
    answer: >-
      Open your Level Blueprint and paste the prepared snippet provided by this Learning Path
      (downloaded on Windows via PowerShell wget). The snippet binds C to start capture and V
      to stop capture.
  - question: Where can I configure capture parameters and output locations?
    answer: >-
      Adjust settings in NGDCRenderingSettings and NGDCExportSettings. You can set UpscalingRatio,
      SupersamplingRatio, FixedFrameRate, camera cut thresholds, and control DatasetDir and CaptureName
      for output organization.
  - question: What should I check if my captured frame dimensions look wrong?
    answer: >-
      Use Standalone Game from the Play mode menu instead of New Editor Window (PIE). PIE can
      produce frame dimensions that differ from expected output sizes.
# END generated_summary_faq

author: 
- Annie Tallund
- Richard Burton

### Tags
skilllevels: Introductory
subjects: Graphics
armips:
    - Mali
    - Immortalis
tools_software_languages:
    - Unreal Engine
    - Visual Studio
    - NX
operatingsystems:
    - Windows



further_reading:
    - resource:
        title: Neural Graphics Data Capture Plugin for Unreal Engine
        link: https://github.com/arm/neural-graphics-data-capture-for-unreal
        type: website
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: Neural Super Sampling in Unreal Engine
        link: /learning-paths/mobile-graphics-and-gaming/nss-unreal/
        type: documentation
    - resource:
        title: Generate Unreal Engine project files for your IDE
        link: https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-generate-unreal-engine-project-files-for-your-ide
        type: documentation
    - resource:
        title: Neural Graphics Model Gym - NSS Data Generation
        link: https://github.com/arm/neural-graphics-model-gym/blob/main/docs/nss/nss_data_generation.md
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

