---
title: Navigate Machine Learning development with Ethos-U processors

description: Learn how to understand and select physical and virtual hardware targets for ML application development with Cortex-M and Ethos-U, identify software tools, and find example applications.

armips:
- Cortex-M
- Ethos-U
- Corstone

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:35:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0cfaa21be515b980097232ed38092b80d046df308120887e5503513a3384a1d7
  summary_generated_at: '2026-06-01T21:46:50Z'
  summary_source_hash: 0cfaa21be515b980097232ed38092b80d046df308120887e5503513a3384a1d7
  faq_generated_at: '2026-06-02T22:35:12Z'
  faq_source_hash: 0cfaa21be515b980097232ed38092b80d046df308120887e5503513a3384a1d7
  summary: >-
    This introductory path helps embedded developers plan Machine Learning workflows on Arm Cortex-M
    with Ethos-U by choosing suitable physical and virtual targets, identifying core tools, and
    locating example applications. You will compare development options that include Corstone-based
    designs such as the MPS3 FPGA Prototyping Board and virtual platforms like Arm Virtual Hardware
    and Fixed Virtual Platforms (FVPs). The path outlines host setup on an x86_64 Windows or Linux
    machine, noting that some tools work only on Linux and that the Arm ML Evaluation Kit (MLEK)
    is not fully supported on Windows. By the end, you will be prepared to select a target, set
    up a bare-metal toolchain (GCC or Arm Compiler for Embedded), and find relevant examples to
    study.
  faqs:
  - question: I don’t have an Ethos-U board—what platform should I start with?
    answer: >-
      Use a virtual platform. The path highlights virtual options such as FVP and Arm Virtual
      Hardware, which let you begin ML development without physical hardware.
  - question: Can I follow this path on Windows, or do I need Linux?
    answer: >-
      An x86_64 machine running Windows or Linux is suitable, but the Arm ML Evaluation Kit is
      not fully supported on Windows and some required tools are Linux-only. If you plan to use
      MLEK extensively, Linux is recommended.
  - question: Which compilers can I use to build ML applications for Cortex-M and Ethos-U?
    answer: >-
      You can build C/C++ applications with GCC or Arm Compiler for Embedded. These toolchains
      are appropriate for the targets described in the path.
  - question: What physical hardware options exist today for Ethos-U development?
    answer: >-
      Readily available development boards with Ethos-U are currently limited. The Arm MPS3 FPGA
      Prototyping Board can be programmed with Corstone reference system images to support ML
      development.
  - question: Does this path assume bare-metal or an RTOS, and what prior experience is needed?
    answer: >-
      The path targets bare-metal development. It assumes some familiarity with microcontroller
      software development.
# END generated_summary_faq

author: Jason Andrews

learning_objectives:
- Understand and select physical and virtual hardware targets for ML application development with Cortex-M and Ethos-U
- Identify and install software tools used for machine learning applications on microcontrollers
- Find and learn from existing example applications 

who_is_this_for: This is an introductory topic for embedded software developers interested in learning about machine learning.

minutes_to_complete: 10

operatingsystems:
- Baremetal

prerequisites:
- Some familiarity with microcontroller software development 

skilllevels: Introductory

subjects: ML

test_maintenance: false

tools_software_languages:
    - FVP
    - Arm Virtual Hardware
    - GCC
    - Arm Compiler for Embedded
    - MPS3

further_reading:
    - resource:
        title: Arm Tech Talks
        link: https://www.arm.com/partners/tech-talks
        type: website
    - resource:
        title: CMSIS-NN documentation
        link: https://www.keil.com/pack/doc/CMSIS/NN/html/index.html
        type: documentation
    - resource:
        title: Machine Learning on Arm Cortex-M Microcontrollers
        link: https://armkeil.blob.core.windows.net/developer/Files/pdf/ethos/Arm_ML_on_Cortex-M_Microcontrollers_v2.pdf
        type: documentation


weight: 1

layout: learningpathall
learning_path_main_page: 'yes'
---

