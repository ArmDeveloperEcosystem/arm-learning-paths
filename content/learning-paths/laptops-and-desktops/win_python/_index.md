---
title: Build native Windows on Arm applications with Python

description: Learn how to build Python applications on Windows on Arm and leverage native Arm64 performance for platform-dependent packages.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who are interested in building Python applications on Arm.

learning_objectives:
   - Understand the platform-dependency of Python packages
   - Leverage native Arm64 for Python applications   

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/). 
    - Any code editor, we recommend using [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user).
    - Visual Studio 2022 with Arm build tools. [Refer to this guide for the installation steps](https://developer.arm.com/documentation/102528/0100/Install-Visual-Studio)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:30:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d953214fe33ad89a683f79e7c29ce9348e5169e6529b808804329cb35060b431
  summary_generated_at: '2026-06-01T22:18:32Z'
  summary_source_hash: d953214fe33ad89a683f79e7c29ce9348e5169e6529b808804329cb35060b431
  faq_generated_at: '2026-06-02T23:30:23Z'
  faq_source_hash: d953214fe33ad89a683f79e7c29ce9348e5169e6529b808804329cb35060b431
  summary: >-
    This introductory path shows how to build native Python applications on Windows on Arm and
    work with platform-dependent packages using Arm64. Using a Windows on Arm PC or virtual machine,
    a code editor (Visual Studio Code for Arm64 recommended), and Visual Studio 2022 with Arm
    build tools, you will create a small NumPy-based application that synthesizes noisy sine waves,
    runs FFTs for varying input sizes, and measures execution time. You will examine the platform-specificity
    of Python packages and use native Arm64 builds where applicable. By the end, you will have
    a working sample.py and timing results to analyze on an Arm64 Windows environment.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm computer (for example, a Lenovo ThinkPad X13s running Windows
      11) or a Windows on Arm virtual machine, a code editor such as Visual Studio Code for Arm64,
      and Visual Studio 2022 with Arm build tools.
  - question: Can I use a Windows on Arm virtual machine instead of physical hardware?
    answer: >-
      Yes. The prerequisites explicitly list a Windows on Arm virtual machine as an option.
  - question: Do I need Visual Studio 2022 if I plan to edit code in VS Code?
    answer: >-
      Yes. Visual Studio 2022 with Arm build tools is listed as a prerequisite, while Visual Studio
      Code for Arm64 is the recommended editor.
  - question: What should I create and what does the sample application do?
    answer: >-
      Create a file named sample.py. It uses NumPy to generate noisy sine waves, runs FFTs over
      multiple input sizes, and measures execution time.
  - question: Where can I find the complete sample code?
    answer: >-
      The Learning Path references that the complete code is available on GitHub.
# END generated_summary_faq

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - Python
    - Visual Studio Code

further_reading:
    - resource:
        title: CPython
        link: https://github.com/python/cpython/
        type: documentation
    - resource:
        title: Windows on Arm now supported in Python 3.11
        link: https://old.linaro.org/blog/windows-on-arm-now-supported-in-python-3-11-release/
        type: blog    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

