---
title: Optimize Unity applications on Android using Neon intrinsics

minutes_to_complete: 90

description: Learn how to use Arm Neon intrinsics in Unity C# scripts to optimize code on Android and collect performance data using Unity Profiler.

who_is_this_for: Developers interested in leveraging the Unity Machine Learning Agents toolkit on Arm devices.

learning_objectives:
    - Use Arm Neon intrinsics in your Unity C# scripts
    - Optimize your code
    - Collect and compare performance data using the Unity Profiler and Analyzer tools

prerequisites:
    - Basic knowledge of Unity and C#
    - Recent Android device, such as a mobile phone or tablet
    - Desktop computer capable of running Unity
    - Unity version compatible with Unity Burst compiler 1.5 or later

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:30:49Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 283e3c9b4dc599acb533237ea9147f206198e4ce4ddf78aabcb6fd5039fd141d
  summary_generated_at: '2026-08-21T17:30:49Z'
  summary_source_hash: 283e3c9b4dc599acb533237ea9147f206198e4ce4ddf78aabcb6fd5039fd141d
  faq_generated_at: '2026-08-21T17:30:49Z'
  faq_source_hash: 283e3c9b4dc599acb533237ea9147f206198e4ce4ddf78aabcb6fd5039fd141d
  summary: >-
    You'll optimize Unity collision detection for Android by comparing plain, Burst, and hand-written
    Arm Neon implementations. First, you'll set up Unity and the collision sample, review character-wall
    and character-character detection, and apply Burst and Neon changes. You'll build and profile
    each mode on your Android device, then use Unity Profile Analyzer to compare the captured data
    and follow profiling practices.
  faqs:
  - question: Where do I switch the project to the unoptimized version?
    answer: >-
      Open `Assets/BurstNeonCollisions/Scripts/CollisionCalculationScript.cs` and change line 66
      to `public const Mode codeMode = Mode.Plain;` to select the unoptimized mode for your initial
      measurements.
  - question: How do I enable or update the Burst compiler in Unity?
    answer: >-
      From **Window**, select **Packet Management > Package Manager**. Set **Packages** to **Unity
      Registry**, search for **Burst**, select it, and select **Install** if it's not already ticked.
  - question: Which Unity and Burst versions should I use?
    answer: >-
      To match the environment used here, use Unity v6.3 and Burst 1.8.28. 
  - question: Which parts of the sample are affected by the optimization steps?
    answer: >-
      Review the character-wall and character-character collision functions. In Plain mode,
      `DoWallsPlain()` loops through all characters and walls, while `DoCharactersPlain()` checks
      each character against the others; the code assumes a character can hit up to two walls.
  - question: What should I check if the Neon version doesn't run on my computer?
    answer: >-
      If your computer doesn't support Neon, don't run the Neon version. In your own code, use
      `if (IsNeonSupported)` to fall back to non-Neon code.
# END generated_summary_faq

author:
    - Ben Clark
    - Joshua Marshall-Law

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Gaming
armips:
    - Cortex-A
tools_software_languages:
    - Unity
    - csharp
    - Neon
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Arm Neon documentation
        link: https://developer.arm.com/Architectures/Neon
        type: documentation
    - resource:
        title: Unity Burst compiler documentation
        link: https://docs.unity3d.com/Manual/com.unity.burst.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
