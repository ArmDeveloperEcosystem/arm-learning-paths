---
title: Get started with Arm Accuracy Super Resolution (Arm ASR)

minutes_to_complete: 40

who_is_this_for: This Learning Path is for mobile, gaming, and graphics developers who want to install and configure Arm Accuracy Super Resolution (Arm ASR) to enhance performance on complex game content without sacrificing image quality.

learning_objectives:
    - Describe Arm Accuracy Super Resolution.
    - Integrate Arm ASR into your game project.
    - Manage how Arm ASR upscales content.

prerequisites:
    - A game project that uses advanced rendering features (such as hardware ray tracing) that stretch the performance capabilities of everyday smartphones.
    - A development machine with Git installed.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:51:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b194edd6ff4ffc5e39e7daa995271d2ed81ec31c8e88ddf1b23a54eb06dd1d06
  summary_generated_at: '2026-06-02T02:48:29Z'
  summary_source_hash: b194edd6ff4ffc5e39e7daa995271d2ed81ec31c8e88ddf1b23a54eb06dd1d06
  faq_generated_at: '2026-06-02T23:51:46Z'
  faq_source_hash: b194edd6ff4ffc5e39e7daa995271d2ed81ec31c8e88ddf1b23a54eb06dd1d06
  summary: >-
    Learn how to install and integrate Arm Accuracy Super Resolution (Arm ASR)—a mobile-optimized
    temporal upscaling technique derived from AMD Fidelity Super Resolution 2 v2.2.2—into Android
    game projects. You will add the ASR plugin to an Unreal Engine project (UE 5.3–5.5 recommended)
    and complete common setup tasks, or integrate the generic ASR library into a custom engine
    using either a quick standalone backend or a tight renderer backend. You will manage how ASR
    upscales content by configuring quality presets, shader variants, and input resources. Prerequisites
    are a game project that pushes smartphone performance (for example, with hardware ray tracing)
    and a development machine with Git installed. Estimated completion time is about 40 minutes.
  faqs:
  - question: Which Unreal Engine versions should I use for this Learning Path?
    answer: >-
      Unreal Engine 5.3–5.5 is recommended. The Arm ASR plugin is available for UE 5.3, 5.4, and
      5.5.
  - question: What do I need before running the steps?
    answer: >-
      Have a game project that uses advanced rendering features that push everyday smartphones,
      and a development machine with Git installed. The path targets Android.
  - question: I’m not using Unreal Engine—how can I integrate Arm ASR?
    answer: >-
      Use the generic library. You can choose Quick Integration with the standalone backend or
      Tight Integration using your engine’s backend/renderer.
  - question: What configuration areas will I manage when integrating ASR?
    answer: >-
      You will work with quality presets, shader variants and extensions, and input resources.
      These areas control how ASR upscales your content.
  - question: How is Arm ASR related to AMD FSR2?
    answer: >-
      Arm ASR is a mobile-optimized temporal upscaling technique derived from AMD Fidelity Super
      Resolution 2 v2.2.2, with optimizations for resource-constrained mobile gaming.
# END generated_summary_faq

author: Julie Gaskin

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
    - Immortalis
tools_software_languages:
    - Unreal Engine
operatingsystems:
    - Android



further_reading:
    - resource:
        title: Arm ASR on Arm Developer Hub
        link: https://www.arm.com/developer-hub/mobile-graphics-and-gaming/arm-accuracy-super-resolution
        type: website
    - resource:
        title: Arm ASR Manga Comic
        link: https://developer.arm.com/Mobile%20Graphics%20and%20Gaming/FeaturedContent/Mali%20Manga/FeaturedContent-MaliManga-Volume4
        type: website
    - resource:
        title: Arm Community Blog
        link: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/introducing-arm-accuracy-super-resolution
        type: blog
    - resource:
        title: Arm Accuracy Super Resolution for Unreal Engine Tutorial
        link: https://developer.arm.com/documentation/109993/latest/
        type: documentation
    - resource:
        title: Arm Accuracy Super Resolution for the Generic Library Tutorial
        link: https://developer.arm.com/documentation/110404/latest/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

