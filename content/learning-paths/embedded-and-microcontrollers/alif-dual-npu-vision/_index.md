---
title: Run parallel vision inference on an Alif Ensemble E8 with Zephyr

description: Build a power-conscious live camera demo that drives Ethos-U55 and Ethos-U85 from one Cortex-M55 MCU.

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for embedded ML developers who want to run two ExecuTorch models concurrently on separate Ethos-U NPUs under Zephyr.

learning_objectives:
    - Identify how one microcontroller unit (MCU) can coordinate two neural processing units (NPUs) while avoiding the power and system cost of a second MCU or application processor.
    - Configure an Alif Ensemble E8 DevKit for native Zephyr camera, image signal processor (ISP), display, and dual-NPU operation.
    - Build, package, and flash an ExecuTorch application that targets Ethos-U55 and Ethos-U85.
    - Validate live camera capture, model results, and parallel inference timing.

prerequisites:
    - Experience with C or C++, embedded systems, and Zephyr build concepts
    - A development machine running macOS on Apple silicon with Homebrew and the Xcode Command Line Tools installed
    - An [Alif Ensemble E8 DevKit](https://alifsemi.com/support/kits/ensemble-e8devkit/) with an MT9M114 camera connected to J16 and an MW405 display
    - Alif SEROM 1.105.65 and SERAM 1.110.0 installed on the board
    - Alif SEToolkit 1.10 installed on the development machine

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-09T22:20:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: de9068955d4f9025bb184aa8176f28ac38d452ad8d2768518c921a7c07d87743
  summary_generated_at: '2026-09-09T22:20:41Z'
  summary_source_hash: de9068955d4f9025bb184aa8176f28ac38d452ad8d2768518c921a7c07d87743
  faq_generated_at: '2026-09-09T22:20:41Z'
  faq_source_hash: de9068955d4f9025bb184aa8176f28ac38d452ad8d2768518c921a7c07d87743
  summary: >-
    You'll build and validate a Zephyr camera application that runs face detection on Ethos-U55 and
    image classification on Ethos-U85 from one Cortex-M55. First, you'll connect the camera and
    display, configure the board, and set up a `west` workspace. Next, you'll build, package, and
    flash the application and model payloads. Finally, you'll reset the board and verify the startup
    test, live camera preview, NPU logs, and parallel timing.
  faqs:
  - question: What should I check on the board before flashing?
    answer: >-
      Connect the USB ports for power, SE UART, and U4 UART. Confirm that your board has SEROM
      1.105.65 and SERAM 1.110.0 installed, and set the boot switch to the SE position.
  - question: Which camera connector should I use for the MT9M114 module?
    answer: >-
      Use the bottom-side J16 connector. The supplied overlay targets J16.
  - question: Where should I run the build from and what inputs are expected?
    answer: >-
      Run from the `west` workspace root with your Python virtual environment activated. Define
      `APP` for the dual-NPU sample, `OD` for the object-detection module, and `MODULES` for the
      Zephyr module list. The sample includes compiled `PTE` models for Ethos-U55 and Ethos-U85
      and a startup image.
  - question: How do I point the packaging step to my Alif SEToolkit installation?
    answer: >-
      Set `ALIF_SE_TOOLS_DIR` to your SEToolkit 1.10 application directory, such as
      `app-release-exec-macos` on macOS. The sample’s JSON assigns application and model payloads
      to validated MRAM addresses. Confirm that the toolkit and referenced support objects are available.
  - question: What results indicate both NPUs are working before live camera starts?
    answer: >-
      After you reset the board, the display shows the bundled Grace Hopper image with a green
      face box from the U55 model. The U85 model identifies an ImageNet class such as
      ACADEMIC GOWN. The U4 log reports model preparation, isolated preflight messages, and
      starting parallel worker threads.
# END generated_summary_faq

author: Varun Chari

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: ML
armips:
    - Cortex-M55
    - Ethos-U55
    - Ethos-U85
tools_software_languages:
    - ExecuTorch
    - Zephyr
    - Python
    - GCC
operatingsystems:
    - macOS
    - RTOS

further_reading:
    - resource:
        title: Alif Ensemble E8 DevKit support page
        link: https://alifsemi.com/support/kits/ensemble-e8devkit/
        type: website
    - resource:
        title: Alif SDK pull request 879
        link: https://github.com/alifsemi/sdk-alif/pull/879
        type: website
    - resource:
        title: Ethos-U core driver multi-variant merge
        link: https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver/-/commit/b7cd193afde80afe8bbae9a26d2ca6586554f054
        type: website
    - resource:
        title: ExecuTorch Arm Ethos-U NPU backend tutorial
        link: https://docs.pytorch.org/executorch/stable/tutorial-arm-ethos-u.html
        type: documentation
    - resource:
        title: Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85
        link: /learning-paths/embedded-and-microcontrollers/alif-image-classification/
        type: documentation
    - resource:
        title: Dual-NPU live vision sample source
        link: https://github.com/varunchariArm/sdk-alif/tree/dual-npu-main-integration/samples/modules/executorch/dual_npu_vision
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
