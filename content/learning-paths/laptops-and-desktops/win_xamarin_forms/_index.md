---
title: Develop cross-platform applications with Xamarin Forms on Windows on Arm

description: Learn how to create and build Xamarin Forms applications using the MVVM pattern and measure code execution performance uplift on Arm64.

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to learn how to create cross-platform applications and leverage performance improvements on Arm64.

learning_objectives:
    - Create and build an Xamarin Forms application
    - Measure code execution performance uplift on Arm64
    - Learn how to use the Model-View-ViewModel (MVVM) architectural pattern

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Visual Studio 2022 with .NET desktop development and Universal Windows Platform development installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:24:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b35d2f5ce175f39a45b3ff44ff41737094e4848cdecd62451a03a957780e4aaf
  summary_generated_at: '2026-08-11T16:24:22Z'
  summary_source_hash: b35d2f5ce175f39a45b3ff44ff41737094e4848cdecd62451a03a957780e4aaf
  faq_generated_at: '2026-08-11T16:24:22Z'
  faq_source_hash: b35d2f5ce175f39a45b3ff44ff41737094e4848cdecd62451a03a957780e4aaf
  summary: >-
    You'll create a Xamarin Forms application on Windows on Arm using the Model-View-ViewModel (MVVM)
    pattern. First, you'll add a model for XY data, organize the project in Visual Studio, and connect the
    view model to the main page. Then, you'll build and run the app, and time a chosen code path to
    measure execution on Arm64.
  faqs:
  - question: Where do I add the DataPoint2d model class?
    answer: >-
      Add it to the `Arm64.MobileApp.XamarinForms` project. Create a `Models` folder and then add
      a new C# class named `DataPoint2d.cs` inside that folder.
  - question: How do I connect the view model to the main page?
    answer: >-
      In `MainPage.xaml`, add the view-model namespace and set `ContentPage.BindingContext` to the
      appropriate view-model class. This makes the view model available to the main page.
  - question: How do I build and run the Xamarin Forms app on Windows on Arm?
    answer: >-
      Use Visual Studio to build the solution, then start debugging to launch the app. A successful
      build completes without errors and opens the app on Windows.
  - question: What should I check if I don't see the option to add a new class or folder?
    answer: >-
      Select the project node (not the solution or a solution folder) in **Solution Explorer**.
      If options are still missing, make sure the project is loaded and not unavailable.
  - question: How can I capture simple execution-time measurements to observe Arm64 uplift?
    answer: >-
      Instrument the relevant code path to record elapsed time, then run the app on the Windows
      on Arm system and note the results. Keep inputs and build configuration the same across
      runs to make comparisons meaningful.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - Xamarin Forms
    - csharp
    - dotnet
    - Visual Studio

further_reading:
    - resource:
        title: Xamarin Forms
        link: https://dotnet.microsoft.com/en-us/apps/xamarin/xamarin-forms
        type: website
    - resource:
        title: The Model-View-ViewModel Pattern
        link: https://learn.microsoft.com/en-us/xamarin/xamarin-forms/enterprise-application-patterns/mvvm
        type: documentation   

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
