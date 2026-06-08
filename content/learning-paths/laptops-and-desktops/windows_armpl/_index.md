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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:34:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f058f628cefb7766ef0728e594c9ef5b57bde97c1850395786d54cc591271503
  summary_generated_at: '2026-06-01T22:21:28Z'
  summary_source_hash: f058f628cefb7766ef0728e594c9ef5b57bde97c1850395786d54cc591271503
  faq_generated_at: '2026-06-02T23:34:43Z'
  faq_source_hash: f058f628cefb7766ef0728e594c9ef5b57bde97c1850395786d54cc591271503
  summary: >-
    This introductory path guides you through setting up Visual Studio 2022 on a Windows on Arm
    device, creating and running a simple console application, and then building and profiling
    a sample that renders a rotating 3D cube. You will install Git for Windows on Arm to clone
    the SpinTheCubeInGDI repository, open its Visual Studio solution, and review core components
    such as shape generation, rotation, and drawing. The final steps install and deploy Arm Performance
    Libraries and explore performance differences after using these math libraries compared to
    multithreaded code. Prerequisite: a Windows on Arm computer such as a Lenovo ThinkPad X13s
    running Windows 11. Estimated time to complete is about 60 minutes.
  faqs:
  - question: Which Visual Studio edition should I install on Windows on Arm?
    answer: >-
      Any of the three Visual Studio 2022 editions can be used. The Community Edition is a free,
      fully featured option suitable for individual developers.
  - question: How do I create the initial Windows on Arm project in Visual Studio?
    answer: >-
      From the Start window, select Create a new project, choose Console App, provide a project
      name, and click Create. Then build and run the project to verify your setup.
  - question: How do I get the SpinTheCubeInGDI example used in this path?
    answer: >-
      Install Git for Windows on Arm if needed, navigate to an empty directory, and clone the
      repository: git clone https://github.com/arm/SpinTheCubeInGDI.git. This repository contains
      the Visual Studio solution for the example.
  - question: How do I open and run the spinning cube example in Visual Studio?
    answer: >-
      In Windows File Explorer, double-click SpinTheCubeInGDI.sln to open the solution in Visual
      Studio. Build and run it to see the rotating 3D cube; the project includes shape generation,
      rotation, and drawing logic implemented in SpinTheCubeInGDI.cpp.
  - question: How do I use Arm Performance Libraries with this example?
    answer: >-
      Follow the Arm Performance Libraries install guide to set up the libraries on Windows. After
      installation, use the project to explore differences when numerical routines are backed
      by Arm Performance Libraries, which provide BLAS, LAPACK, FFT, and sparse implementations
      built with OpenMP.
# END generated_summary_faq

author: Odin Shen

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
tools_software_languages:
    - Visual Studio
    - C#
    - .NET
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

