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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:10:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9cd19738cbe9cde618125b309bd4f2c57ad1799e807251fdaed09707bea2781d
  summary_generated_at: '2026-06-02T03:01:07Z'
  summary_source_hash: 9cd19738cbe9cde618125b309bd4f2c57ad1799e807251fdaed09707bea2781d
  faq_generated_at: '2026-06-03T00:10:44Z'
  faq_source_hash: 9cd19738cbe9cde618125b309bd4f2c57ad1799e807251fdaed09707bea2781d
  summary: >-
    This Learning Path shows how to use Unity’s Machine Learning Agents toolkit inside a Unity
    project that can be deployed to Arm-powered Android devices. You will install Unity (via Unity
    Hub), open the provided Dr Arm sample project, review how observations and actions map to
    a neural network “brain,” and prepare the scene and scripts for the training stage. The toolkit
    includes a C# API and Python scripts; you will need Python and a few extra libraries before
    running training, but you can begin by setting up Unity. Prerequisites include a computer
    capable of running Unity (instructions target Windows), an Android device with a 64-bit processor
    running Android 8 or later, and a USB cable. Deployment and profiling are covered in separate
    Learning Paths.
  faqs:
  - question: Do I need to install Python before I start, or can I begin with Unity only?
    answer: >-
      You will need Python and some additional libraries before the training stage, but to get
      started quickly you can install Unity first. The C# API is used inside Unity, while Python
      scripts run outside Unity during training.
  - question: Which Unity components should I install through Unity Hub?
    answer: >-
      Install Unity via the Unity Hub and include Visual Studio Community Edition with the Unity
      support module. The Hub helps manage multiple Unity installations and add required support
      modules.
  - question: Which scene should I open in the Dr Arm project to follow the steps?
    answer: >-
      Open Assets -> #DevSummit2022 -> Scenes and load the Level DevSummit2022 scene. Ignore the
      “Ready to Play” version and use this incomplete scene to apply the ML setup changes.
  - question: What Android device requirements should I check before proceeding?
    answer: >-
      Use an Android device with a 64-bit processor running Android 8 or later and have a USB
      cable to connect it to your computer. These are the explicitly listed prerequisites.
  - question: Does this Learning Path include Android deployment and profiling steps?
    answer: >-
      No. Instructions for deploying Unity games to Arm-powered Android devices and profiling
      them are provided in separate Learning Paths.
# END generated_summary_faq

author: Arm

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

