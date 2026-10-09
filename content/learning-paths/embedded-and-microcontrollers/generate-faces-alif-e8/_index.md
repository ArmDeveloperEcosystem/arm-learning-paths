---
title: Generate human faces with a diffusion model on an Alif Ensemble E8

description: Export the pico-faces diffusion model with ExecuTorch, run it on the Alif Ensemble E8 Ethos-U85 NPU, and display generated faces on the DevKit LCD.

minutes_to_complete: 120

who_is_this_for: This topic is for embedded and machine learning developers who want to deploy a Generative AI model on a microcontroller with Arm Ethos-U85 acceleration.

learning_objectives:
    - Explain how ExecuTorch divides pico-faces generation between the Cortex-M55 and Ethos-U85 NPU
    - Export and fully delegate the pico-faces diffusion transformer and decoder to the Ethos-U85 NPU
    - Configure the Alif Ensemble E8 DevKit for loading and debugging the generated application
    - Generate human faces on the DevKit and validate NPU execution through the LCD and UART output

prerequisites:
    - Familiarity with Python, machine learning models, and embedded development
    - An [Alif Ensemble E8 DevKit](https://alifsemi.com/support/kits/ensemble-e8devkit/) with its display and a USB-C data cable
    - A development computer running Linux, macOS, or Windows, with internet access and several GB of free storage
    - An Arm account for the Keil MDK Community license and an Alif account for downloading SETOOLS

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-08T13:45:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c8f269fe31381f71921333cb60d33cf0f9406de630dfac4f424b045428870094
  summary_generated_at: '2026-10-08T13:45:37Z'
  summary_source_hash: c8f269fe31381f71921333cb60d33cf0f9406de630dfac4f424b045428870094
  faq_generated_at: '2026-10-08T13:45:37Z'
  faq_source_hash: c8f269fe31381f71921333cb60d33cf0f9406de630dfac4f424b045428870094
  summary: >-
    You'll export the pico-faces diffusion model with ExecuTorch and deploy it to the Alif Ensemble
    E8 DevKit. First, you'll configure Keil Studio and the CMSIS toolchain, then delegate the diffusion
    transformer and decoder to the Arm Ethos-U85 NPU. Next, you'll provision the Cortex-M55 boot and
    debug flow, build the application, and generate human faces. Finally, you'll verify NPU execution
    through the DevKit LCD, UART output, and performance counters.
  faqs:
  - question: What should I check on the DevKit before connecting it to my computer?
    answer: >-
      Before you connect the DevKit, unplug all USB cables before changing any jumpers. Verify
      that the jumpers match the factory defaults documented in the DK-E8 User Guide. This helps
      you avoid power or boot issues during setup.
  - question: Which USB port do I use for programming, and how do I confirm the board is powered?
    answer: >-
      Connect a USB-C cable to the PRG USB port on the bottom edge of the DevKit. You can confirm
      that the board has power when a green LED illuminates near the E1 device.
  - question: Which repository branch do I need for this example?
    answer: >-
      Clone the CMSIS-ExecuTorch repository using the `hackathon-pico-faces` branch. Use the
      `--branch hackathon-pico-faces --single-branch` options, then open the workspace in VS Code.
  - question: Which serial settings and switch position should I use to view application output?
    answer: >-
      Set **SW4** to **UART4** and open **Serial Monitor** on the **PRG USB** port at `115200` baud,
      eight data bits, no parity, and one stop bit. If the port was open before changing **SW4**,
      close and reopen it.
  - question: What result should I expect when I start a debug session and run the firmware?
    answer: >-
      From the **CMSIS** view, select **Build**, then **Debug**. Keil Studio starts the J-Link GDB
      server over SWD and loads the application into MRAM, stopping at `main`. Press **F5** to
      continue. The DevKit displays a 128 x 128 RGB face, and UART output confirms Arm Ethos-U85
      execution.
# END generated_summary_faq

author: Ash Naik

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-M55
    - Ethos-U85
tools_software_languages:
    - Alif SETOOLS
    - CMSIS-Toolbox
    - ExecuTorch
    - Generative AI
    - Keil Studio
    - Python
    - PyTorch
    - SEGGER JLink
operatingsystems:
    - Baremetal
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: CMSIS-ExecuTorch pico-faces example
        link: https://github.com/Arm-Examples/CMSIS-Executorch/tree/hackathon-pico-faces
        type: website
    - resource:
        title: pico-faces project
        link: https://github.com/cpldcpu/pico-faces
        type: website
    - resource:
        title: ExecuTorch Arm Ethos-U backend
        link: https://docs.pytorch.org/executorch/main/backends-arm-ethos-u.html
        type: documentation
    - resource:
        title: PyTorch ExecuTorch CMSIS Pack
        link: https://www.keil.arm.com/packs/executorch-pytorch/
        type: documentation
    - resource:
        title: CMSIS-Toolbox MLOps information
        link: https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information
        type: documentation
    - resource:
        title: Alif Ensemble E8 DevKit support
        link: https://alifsemi.com/support/kits/ensemble-e8devkit/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

