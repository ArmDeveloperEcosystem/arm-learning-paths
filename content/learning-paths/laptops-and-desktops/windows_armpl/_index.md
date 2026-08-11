---
title: Optimize Windows applications using Arm Performance Libraries

description: Learn how to develop Windows on Arm applications using Visual Studio and optimize performance with Arm Performance Libraries.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to improve the performance of Windows on Arm applications using Arm Performance Libraries.

learning_objectives: 
    - Develop a Windows on Arm application using Microsoft Visual Studio.
    - Utilize Arm Performance Libraries to optimize the performance of an application.

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:25:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d0fa006b55c54487c17ad6081cc8764b837b5ec0e52ab646c8a8aa5a3836cad4
  summary_generated_at: '2026-08-11T16:25:07Z'
  summary_source_hash: d0fa006b55c54487c17ad6081cc8764b837b5ec0e52ab646c8a8aa5a3836cad4
  faq_generated_at: '2026-08-11T16:25:07Z'
  faq_source_hash: d0fa006b55c54487c17ad6081cc8764b837b5ec0e52ab646c8a8aa5a3836cad4
  summary: >-
    You'll set up Visual Studio 2022 on Windows on Arm, create a starter console app, and profile
    the `SpinTheCubeInGDI` example. First, you'll capture a baseline while it runs a rotating 3D shape,
    then install Arm Performance Libraries and profile again. You'll compare the results to assess
    how library integration and programming options affect execution.
  faqs:
  - question: Which Visual Studio 2022 edition should I use for this path?
    answer: >-
      Use any edition of Visual Studio 2022 that meets your needs. The Community edition is
      free and suitable for students, open source contributors, and individual developers.
  - question: Where should I clone the example, and how do I confirm it cloned correctly?
    answer: >-
      Clone the repository into an empty directory you can write to. After cloning, you should
      see `SpinTheCubeInGDI.sln` and the source file `SpinTheCubeInGDI.cpp` in the repository folder.
  - question: How do I open and run the Spin the Cube example, and what result should I expect?
    answer: >-
      Open `SpinTheCubeInGDI.sln` in Visual Studio, then build and run
      it. A window that draws a spinning 3D cube indicates the application is running correctly.
  - question: What should I check when profiling the application in Visual Studio?
    answer: >-
      Capture a baseline profile while the spinning cube runs, then repeat after changing the
      example’s programming options such as multithreading. Compare the results between runs to
      understand the differences.
  - question: How do I install and apply Arm Performance Libraries in this workflow?
    answer: >-
      Install Arm Performance Libraries for Windows on Arm by following the [install guide](/install-guides/armpl/). Integrate
      the libraries as directed by the guide, rebuild the project, and profile again to compare
      with your baseline.
# END generated_summary_faq

author: Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
tools_software_languages:
    - Visual Studio
    - csharp
    - dotnet
    - Arm Performance Libraries
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: Arm Performance Libraries Reference Guide  
        link: https://developer.arm.com/documentation/101004/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
