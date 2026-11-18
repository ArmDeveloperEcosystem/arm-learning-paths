---
title: Deploy Unity Machine Learning Agents on Arm Android devices
description: Learn how to integrate Unity's Machine Learning Agents toolkit into games deployable to Arm-powered Android devices.

minutes_to_complete: 60

who_is_this_for: Developers interested in leveraging the Unity Machine Learning Agents toolkit on Arm devices.

learning_objectives:
    - Get the Unity Machine Learning (ML) Agents toolkit running in a game that is deployable to Arm-powered Android devices.
    - Note - Instructions on how to deploy Unity games to an Arm-powered Android device and how to profile them are included in separate Learning Paths.

prerequisites:
- A computer capable of running Unity. (Instructions are for Windows, but could be adapted to other platforms.)
- An Android mobile device that has a 64-bit processor and supports at least Android 8.
- A USB cable to connect the mobile device to your computer.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:31:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2bdc0ddd9b063be742d029a66a6cb2eebd3680f72f38129fd813425c4f75dbac
  summary_generated_at: '2026-08-21T17:31:28Z'
  summary_source_hash: 2bdc0ddd9b063be742d029a66a6cb2eebd3680f72f38129fd813425c4f75dbac
  faq_generated_at: '2026-08-21T17:31:28Z'
  faq_source_hash: 2bdc0ddd9b063be742d029a66a6cb2eebd3680f72f38129fd813425c4f75dbac
  summary: >-
    You'll use Unity ML-Agents to add machine-learning behavior to the Dr Arm fighting game. First, you'll install
    Unity and its required modules, open the ready-to-play scene, and explore how an agent uses
    observations, actions, and rewards. Then, you'll modify the gameplay scene components and scripts,
    set up Python tools, train agents or use supplied training data, and review training optimizations.
  faqs:
  - question: Which Unity scene do I open for the ML steps?
    answer: >-
      In the **Project** tab, open `Assets/#DevSummit2022/Scenes/Level_DevSummit2022`. Use this
      incomplete scene for the walkthrough instead of `Level_DevSummit2022_ReadyToPlay`.
  - question: Do I need Python installed before I can start?
    answer: >-
      You need Python tools for the training stage. To get started, install Unity first
      and return to the Python setup when you begin training.
  - question: What do I install with Unity Hub for this project?
    answer: >-
      Install Unity Hub and a Unity Editor. If you plan to deploy to Android, add **Android Build
      Support**, **OpenJDK**, and **Android SDK & NDK Tools**. You can install Microsoft Visual
      Studio Community 2022 with Unity support, or use another script editor, then download the
      Dr Arm project files.
  - question: How do I control the player on a mobile device during testing?
    answer: >-
      Use the on-screen touch controls to move, roll, and perform attacks on mobile.
  - question: How do I use a trained model in the game?
    answer: >-
      Reopen `Level_DevSummit2022`, select **AgentsSettings**, and assign an `NN Model` asset to
      each Battle Brain property. You can use the supplied pre-trained models or models from your
      completed training.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Gaming
armips:
    - Cortex-A
operatingsystems:
    - Android
tools_software_languages:
    - Unity

further_reading:
    - resource:
        title: Using Unity's Machine Learning Agents on Arm on YouTube
        link: https://www.youtube.com/watch?v=ZZa0faTjwFA
        type: video
    - resource:
        title: Tackling profiling for mobile games with Unity and Arm
        link: https://blog.unity.com/games/tackling-profiling-for-mobile-games-with-unity-and-arm
        type: blog
    - resource:
        title: Arm Mobile Studio 
        link: https://developer.arm.com/Tools%20and%20Software/Arm%20Mobile%20Studio
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
