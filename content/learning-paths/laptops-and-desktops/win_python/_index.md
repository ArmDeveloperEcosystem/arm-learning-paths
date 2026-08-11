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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-11T16:21:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c3de02d2b903cb1c32f5c8a2baa828a650563c310289fc86ccd10d4ccb7f4ca9
  summary_generated_at: '2026-08-11T16:21:47Z'
  summary_source_hash: c3de02d2b903cb1c32f5c8a2baa828a650563c310289fc86ccd10d4ccb7f4ca9
  faq_generated_at: '2026-08-11T16:21:47Z'
  faq_source_hash: c3de02d2b903cb1c32f5c8a2baa828a650563c310289fc86ccd10d4ccb7f4ca9
  summary: >-
    You'll use platform-specific Python packages on Windows on Arm to build a small Arm64-native
    application with NumPy. First, you'll create a `sample.py`
    script that synthesizes noisy sine waves, computes fast Fourier transforms (FFTs) for multiple
    input sizes, and records execution times across repeated runs. You'll learn how
    platform dependency affects Python and its libraries, and how to work with Arm-native tooling
    on Windows 11. By the end, you'll run the script, review timing output, and recognize how
    package choice and input size influence runtime behavior when targeting Arm64 on Windows on
    Arm.
  faqs:
  - question: What result should I expect when I run the sample application?
    answer: >-
      The program computes FFTs of synthesized sine waves with added noise for several input lengths
      and prints execution times. Use the printed timings to compare how runtime changes as the
      input size varies on the same device.
  - question: Where can I find the complete sample code if my script differs?
    answer: >-
      A complete version of the code is available on GitHub. Compare your `sample.py` with
      that version if you see unexpected results.
  - question: What should I check if import numpy fails when running sample.py?
    answer: >-
      Confirm that you installed NumPy during setup. Also verify that you're using the
      Windows on Arm environment and Arm64 tooling noted in the setup.
  - question: Which parts of the sample can I change to explore performance differences?
    answer: >-
      Modify the set of input lengths, the number of iterations, or the signal parameters used
      to synthesize the sine waves. Rerun the script and compare the new execution times.
  - question: How do I compare the Arm64 and x64 Python runs?
    answer: >-
      Run `py -3.12-64 sample.py` for x64 emulation, then run `py -3.12-arm64 sample.py` for
      Arm64. Run both commands from the directory containing `sample.py` and compare the execution
      times for the same signal lengths.
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
