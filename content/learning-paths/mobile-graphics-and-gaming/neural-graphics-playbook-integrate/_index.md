---
title: Arm Neural Technology Playbook - Integrate
description: Plan an NFRU or NSS integration, evaluate model work with MLIA and Streamline, and scope experimental NSSD exploration with Arm.
minutes_to_complete: 60

who_is_this_for: This Learning Path is for game developers, graphics engineers, and technical leads who understand Arm Neural Technology and want to plan an integration for a mobile game.

learning_objectives:
    - Choose the Arm Neural Technology integration route that matches your game and team
    - Plan an NFRU evaluation using public Arm tools and representative game content
    - Decide when advanced NSSD exploration with Arm fits your visual goals
    - Use Model Gym, MLIA, and Streamline to plan model development and validation for NX

prerequisites:
    - Familiarity with Arm Neural Technology and its NSS, NFRU, and NSSD use cases
    - Basic understanding of real-time rendering, motion vectors, temporal techniques, and denoising
    - Familiarity with your game's frame-rate, image-quality, power, and thermal targets

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-03T20:30:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 53bb7773b2ef4f0886f2a6c7cc10734df7bc7acf70618086ea1461e9780f161f
  summary_generated_at: '2026-09-03T20:30:03Z'
  summary_source_hash: 53bb7773b2ef4f0886f2a6c7cc10734df7bc7acf70618086ea1461e9780f161f
  faq_generated_at: '2026-09-03T20:30:03Z'
  faq_source_hash: 53bb7773b2ef4f0886f2a6c7cc10734df7bc7acf70618086ea1461e9780f161f
  summary: >-
    You choose between public NFRU and NSS integration routes, evaluate whether NFRU meets your
    game's quality and frame-pacing targets, and plan experimental NSSD exploration through Arm's
    Early Access Program. You trace NFRU through the engine, rehearse repeatable testing with Project
    Moku, scope model training for NX, and use MLIA estimates and Streamline device measurements
    to guide model decisions. Finally, you record your decision in a short integration brief.
  faqs:
  - question: Which neural technology should I start with if I need smoother motion without rendering
      every frame?
    answer: >-
      Start with NFRU. If you use Unreal Engine, evaluate the public NFRU plugin against repeatable
      content. If you own a custom engine, use the public Neural Graphics SDK and plan the Vulkan
      inputs, dispatch, presentation, and frame-pacing evaluation.
  - question: What should I capture from Unreal to fairly test NFRU?
    answer: >-
      Use controlled scenes that exercise occlusion, particle effects, lighting changes, and frame-pacing
      stress, as shown in the Project Moku NFRU case study. Keep runs repeatable so you can compare
      output consistently.
  - question: How do I validate that NFRU behaves correctly during evaluation?
    answer: >-
      Validate the workload and pacing with Streamline, and inspect generated frames with RenderDoc
      for Arm GPUs. Look for a consistent intermediate frame between neighboring rendered frames
      and check for visible artifacts.
  - question: When should I consider exploring NSSD instead of focusing on NFRU?
    answer: >-
      Explore NSSD when the goal is to reconstruct a clean, higher-resolution image from low-resolution,
      noisy inputs for advanced lighting or ray-tracing workflows. It is a more ambitious route,
      so decide when collaboration with Arm aligns with your visual targets.
  - question: What should I include in the short integration brief?
    answer: >-
      Record your chosen route, representative test content, measurable targets, and named owners.
      Include relevant captures and measurements, label any MLIA results as estimates, and define
      your fallback.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
tools_software_languages:
    - Unreal Engine
    - Vulkan
    - Arm Performance Studio
    - Streamline
    - MLIA
    - NX
operatingsystems:
    - Windows
    - Android

further_reading:
    - resource:
        title: Neural Network Model Development Best Practices for GPUs with Neural Accelerator
        link: https://developer.arm.com/documentation/112431/latest
        type: documentation
    - resource:
        title: Arm GPU Best Practices Developer Guide
        link: https://support.arm.com/documentation/101897/latest/
        type: documentation
    - resource:
        title: Arm Neural Technology Playbook - Evaluate
        link: /learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/
        type: learningpath
    - resource:
        title: Get Started with profiling Arm Neural Technology workloads with Streamline
        link: /learning-paths/mobile-graphics-and-gaming/streamline-nx/
        type: learningpath
    - resource:
        title: Estimate neural accelerator (NX) performance with ML Inference Advisor
        link: /learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/
        type: learningpath

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
