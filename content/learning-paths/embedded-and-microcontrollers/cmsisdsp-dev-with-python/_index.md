---
title: Getting started with CMSIS-DSP using Python

description: Learn how to prototype and port DSP algorithms using the CMSIS-DSP Python package, mapping Python code to efficient C implementations for embedded Cortex-M and Cortex-A platforms.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers looking to integrate the CMSIS-DSP library into their applications using Python.


learning_objectives:
    - Use the CMSIS-DSP Python package to prototype DSP algorithms.
    - Understand how the Python API maps to the C implementation.
    - Build and port a complex DSP application using CMSIS-DSP.

prerequisites:
    - Familiarity with Python and digital signal processing concepts.
    - Working knowledge of C.
    - Prior exposure to CMSIS-DSP.
    - Python installed on your machine.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:13:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 69526ee8b840c8f5d77d49349d2f0cc7ff4594fec5e4311984ef72a0672d3462
  summary_generated_at: '2026-06-01T21:31:12Z'
  summary_source_hash: 69526ee8b840c8f5d77d49349d2f0cc7ff4594fec5e4311984ef72a0672d3462
  faq_generated_at: '2026-06-02T22:13:13Z'
  faq_source_hash: 69526ee8b840c8f5d77d49349d2f0cc7ff4594fec5e4311984ef72a0672d3462
  summary: >-
    This advanced Learning Path shows how to prototype DSP algorithms in Python using the CMSIS-DSP
    Python package and understand how the Python API maps to the CMSIS-DSP C implementation for
    Arm Cortex-M and Cortex-A platforms. On Linux, Windows, or macOS, you will set up a Python
    virtual environment, install cmsisdsp, Jupyter, and NumPy, and use a Jupyter notebook to load
    a sample “yes/no” audio file from an Arm repository. You will implement a simple energy-based
    voice activity detector, apply overlapping Hanning windows, and build a NumPy reference for
    a noise-suppression workflow. Prerequisites include familiarity with Python and DSP concepts,
    working knowledge of C, prior exposure to CMSIS-DSP, and Python installed.
  faqs:
  - question: What do I need before running the notebook?
    answer: >-
      You need Python installed, familiarity with Python and DSP concepts, working knowledge of
      C, and prior exposure to CMSIS-DSP. The path targets Linux, Windows, and macOS. No additional
      prerequisites are explicitly listed.
  - question: Should I create a Python virtual environment and which packages do I install?
    answer: >-
      Yes, the steps use a Python virtual environment. Install cmsisdsp (which also installs NumPy)
      and then install the jupyter package.
  - question: Where does the sample audio come from and how is it used?
    answer: >-
      The notebook loads a yesno.wav file from an Arm demo repository on GitHub using urlopen.
      You play it in the notebook with an Audio widget to inspect the noisy speech used in the
      subsequent steps.
  - question: How do I know my VAD and noise suppression steps are working?
    answer: >-
      You implement a simple energy-based VAD with a manually tuned threshold and then build a
      NumPy reference for noise suppression using overlapping windows and a Hanning window via
      dsp.arm_hanning_f32. The path relies on iterative tuning and listening/inspection in the
      notebook; specific validation criteria beyond this are not explicitly listed.
  - question: How does the Python code relate to the CMSIS-DSP C implementation on Arm cores?
    answer: >-
      The CMSIS-DSP Python package provides APIs that map to CMSIS-DSP C functions, helping you
      prototype in Python before building and porting to C. The underlying C library is optimized
      for Arm Cortex-M and Cortex-A, including DSP extensions on M4/M7, Helium on M55/M85, and
      Neon on Cortex-A55 and other Cortex-A cores.
# END generated_summary_faq

author: Christophe Favergeon

### Tags
skilllevels: Advanced
subjects: Libraries
armips:
    - Cortex-M
    - Cortex-A
tools_software_languages:
    - CMSIS-DSP
    - Python
    - C
    - Jupyter Notebook
    - NumPy
operatingsystems:
    - Linux
    - Windows
    - macOS

further_reading:
    - resource:
        title: Biquad Filters with CMSIS-DSP Python Package
        link: https://developer.arm.com/documentation/102463/latest/
        type: documentation
    - resource:
        title: CMSIS-DSP Library (GitHub)
        link: https://github.com/ARM-software/CMSIS-DSP
        type: Open-source project
    - resource:
        title: CMSIS-DSP Python Package (PyPi)
        link: https://pypi.org/project/cmsisdsp/
        type: Open-source project
    - resource:
        title: CMSIS-DSP Python Package Examples and Tests
        link: https://github.com/ARM-software/CMSIS-DSP/tree/main/PythonWrapper/examples
        type: Open-source project
    - resource:
        title: CMSIS-Stream
        link: https://github.com/ARM-software/CMSIS-Stream
        type: Open-source project


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

