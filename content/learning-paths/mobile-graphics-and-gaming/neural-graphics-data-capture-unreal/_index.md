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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:10:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0ccaf9c5b055c63e74c2e7ae4c6dc8f5c45f7b1eb3687e9174fae23d45dfaf78
  summary_generated_at: '2026-08-17T22:10:28Z'
  summary_source_hash: 0ccaf9c5b055c63e74c2e7ae4c6dc8f5c45f7b1eb3687e9174fae23d45dfaf78
  faq_generated_at: '2026-08-17T22:10:28Z'
  faq_source_hash: 0ccaf9c5b055c63e74c2e7ae4c6dc8f5c45f7b1eb3687e9174fae23d45dfaf78
  summary: >-
    This Learning Path shows how to add the Neural Graphics Data Capture plugin to a C++ Unreal
    Engine 5.5 project, connect simple Level Blueprint controls, and export a structured frame
    dataset from real gameplay. You clone the repository, place it in the project Plugins folder,
    enable and build it, then bind hotkeys to start and stop capture. Capture runs in Standalone
    Game to preserve expected frame dimensions. After recording, learners verify outputs in the
    configured directory and tune NGDCRenderingSettings and NGDCExportSettings—such as UpscalingRatio,
    SupersamplingRatio, FixedFrameRate, and DatasetDir/CaptureName—to prepare datasets for training
    or evaluating neural upscalers like Neural Super Sampling.
  faqs:
  - question: Do I need a C++ Unreal project to build the plugin?
    answer: >-
      Yes. The plugin targets Unreal Engine 5.5 and requires a C++ Unreal project so the module
      compiles through Visual Studio. Open a C++ project before adding the plugin files.
  - question: Which play mode should I use for capture, and where do I change it?
    answer: >-
      Use Standalone Game. Open the menu next to the Play button and select Standalone Game to
      avoid Play-in-Editor resizing and preserve expected frame dimensions.
  - question: How do I start and stop a capture during gameplay?
    answer: >-
      Press Play, then press C to start capture and V to stop capture. Move through the level
      while recording to gather frames.
  - question: Where are the exported datasets saved, and how do I verify the capture finished?
    answer: >-
      The output directory and capture name come from NGDCExportSettings (DatasetDir and CaptureName).
      After stopping capture, check that directory for the exported capture folder and files.
  - question: How can I adjust capture quality, scaling, or lock the frame rate?
    answer: >-
      Use NGDCRenderingSettings and NGDCExportSettings. Set UpscalingRatio and SupersamplingRatio
      for input/output scaling and quality, and set FixedFrameRate to a value greater than 0 to
      lock the frame rate.
# END generated_summary_faq

author:
    - Annie Tallund
    - Richard Burton

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

