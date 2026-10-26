---
title: Run Conformer speech recognition on Alif Ensemble E8 with ExecuTorch


description: Prepare Conformer ASR with ExecuTorch, validate it on Corstone-320, and capture and transcribe speech on an Alif E8 with Ethos-U85.

minutes_to_complete: 120

who_is_this_for: This Learning Path is for embedded ML developers who want to capture and transcribe live speech on an Alif Ensemble E8 using ExecuTorch and the Ethos-U85 NPU.

learning_objectives:
    - Prepare a quantized Conformer model with Arm and Alif MLEK for ExecuTorch deployment.
    - Build and run ASR on the Corstone-320 Fixed Virtual Platform (FVP) using recorded audio.
    - Build and flash the E8 application and its external-flash model.
    - Validate live transcription, Ethos-U85 execution, and standalone restart on the E8.

prerequisites:
    - Experience with C or C++, CMake, and embedded baremetal development concepts
    - Familiarity with PyTorch, ExecuTorch, and quantized model deployment
    - A Linux development machine, or an Apple silicon Mac running macOS 15 or later with Homebrew and [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/) installed
    - An Alif Ensemble E8 AI/ML AppKit (AK-E8-AIML), or an E8 DevKit with a compatible attached display, and a USB-C data cable

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-19T18:53:32Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d578cfc715a8053023cefa73fadd12f17f8a7c80482312edb5728285cab7d367
  summary_generated_at: '2026-10-19T18:53:32Z'
  summary_source_hash: d578cfc715a8053023cefa73fadd12f17f8a7c80482312edb5728285cab7d367
  faq_generated_at: '2026-10-19T18:53:32Z'
  faq_source_hash: d578cfc715a8053023cefa73fadd12f17f8a7c80482312edb5728285cab7d367
  summary: >-
    You'll prepare a quantized Conformer speech recognition model for ExecuTorch, validate it on a
    Corstone-320 FVP, and deploy it to an Alif Ensemble E8. First, you'll
    generate model resources and run the FVP application with recorded audio. Then, you'll build the E8
    firmware, program the model in external flash, and capture speech through the onboard
    microphones. Finally, you'll check the displayed transcription, Ethos-U85 activity, and standalone
    restart.
#   faqs:
#   - question: How do I know the FVP ASR application ran correctly before moving to the E8 board?
#     answer: >-
#       Check that the FVP console identifies the audio sample and prints a `Decoded output:` line
#       with recognized text. You can then move on to the E8 build.
#   - question: Which application do I build for the E8 and which core does it target?
#     answer: >-
#       Select the Alif MLEK `alif_asr` application with `-DUSE_CASE_BUILD=alif_asr`, then build
#       the `mlek_alif_asr` target. You deploy it to the E8's high-performance Cortex-M55 subsystem.
#   - question: Which build option selects the Ethos-U85 NPU for the E8 firmware?
#     answer: >-
#       Set `-DETHOS_U_NPU_ID=U85` when you configure the E8 firmware. You can check for nonzero
#       `NPU ACTIVE` and `NPU TOTAL` counters in the UART log after inference.
#   - question: What should I set up on the E8 before opening the serial console, and what settings do I use?
#     answer: >-
#       Keep the **PRG USB** cable connected and set **SW4** to **UART4**. Open the board's serial
#       port at 115200 baud, eight data bits, no parity, and one stop bit. If the port was already
#       open when you changed **SW4**, close and reopen it.
#   - question: How do I know the E8 is ready to capture speech, and how do I record a phrase?
#     answer: >-
#       Press **RESET (SW1)** and wait for `Model initialisation complete` in the UART log and
#       **Conformer ASR (ExecuTorch)** on the display. Hold down the joystick center while you
#       speak, then release it. Check the display for a transcription and the console for a
#       `Decoded output:` line.
# END generated_summary_faq

author:
    - Matt Cossins
    - Kwashie Andoh

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: ML
armips:
    - Cortex-M
    - Ethos-U
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - GCC
    - CMake
    - Python
    - Conformer
operatingsystems:
    - Baremetal
    - Linux
    - macOS

further_reading:
    - resource:
        title: "End-to-End INT8 Conformer on Arm: Training, Quantization, and Deployment on Ethos-U85"
        link: https://developer.arm.com/community/arm-community-blogs/b/internet-of-things-blog/posts/end-to-end-int8-conformer-on-arm-training-quantization-and-deployment-on-ethos-u85
        type: blog
    - resource:
        title: Alif ML Embedded Evaluation Kit
        link: https://github.com/alifsemi/alif_ml-embedded-evaluation-kit/tree/main
        type: repository
    - resource:
        title: Arm ML Embedded Evaluation Kit
        link: https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit
        type: repository
    - resource:
        title: Alif Ensemble E8 AppKit Support Page
        link: https://alifsemi.com/support/kits/ensemble-e8appkit/
        type: website
    - resource:
        title: ExecuTorch Arm Ethos-U NPU Backend Tutorial
        link: https://docs.pytorch.org/executorch/stable/tutorial-arm-ethos-u.html
        type: documentation
### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
