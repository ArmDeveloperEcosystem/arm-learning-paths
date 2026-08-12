---
title: Implement post-quantum cryptography on Arm Cortex-M4

description: Learn how to implement and test post-quantum cryptographic algorithms on Arm Cortex-M4 microcontrollers using the pqm4 library.

minutes_to_complete: 120

who_is_this_for: This is an advanced topic for software developers and cryptography enthusiasts interested in implementing and testing post-quantum cryptographic algorithms on Arm Cortex-M4 microcontrollers.

learning_objectives:
    - Describe the design goals and supported algorithms of the pqm4 library.
    - Set up the development environment for Arm Cortex-M4.
    - Implement and test post-quantum cryptographic algorithms.
    - Benchmark and profile cryptographic implementations.
    - Integrate new cryptographic schemes into the pqm4 framework.

prerequisites:
    - Computer with Python 3.8 or higher
    - Arm GNU Toolchain [installed](/install-guides/gcc/arm-gnu/)
    - An Arm Cortex-M4 development board such as NUCLEO-L4R5ZI, NUCLEO-L476RG, or STM32F4 Discovery, with stlink or OpenOCD for flashing. Alternatively, install QEMU to simulate the hardware without a physical board.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:14:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2e01cd6a59bdd1919f1a842f64d68c46ccea75d20ff3bbe747f70ee8a33fb7ed
  summary_generated_at: '2026-08-12T20:14:29Z'
  summary_source_hash: 2e01cd6a59bdd1919f1a842f64d68c46ccea75d20ff3bbe747f70ee8a33fb7ed
  faq_generated_at: '2026-08-12T20:14:29Z'
  faq_source_hash: 2e01cd6a59bdd1919f1a842f64d68c46ccea75d20ff3bbe747f70ee8a33fb7ed
  summary: >-
    You'll use `pqm4` to test and benchmark post-quantum cryptography on Arm Cortex-M4. You'll set
    up hardware or QEMU, build scheme binaries, and validate implementations against test vectors.
    You'll measure cycles, stack usage, and code size, then add a key encapsulation mechanism under
    `crypto_kem/` so the build system discovers and compiles it.
  faqs:
  - question: 'Which target should I use: a physical Cortex-M4 board or QEMU?'
    answer: >-
      Use a physical board if you have supported hardware and a flashing tool (`stlink` or OpenOCD).
      Choose QEMU to simulate a Cortex-M4 using the `mps2-an386` platform when hardware isn't available.
  - question: How do I know the pqm4 build completed successfully?
    answer: >-
      You should see binaries under `bin/` for each scheme you built. The filenames follow a pattern
      such as `bin/crypto_kem_ml-kem-768_<impl>_<type>.bin`, indicating the scheme and implementation
      variant.
  - question: What do implementation variants such as `m4fspeed` and `m4fstack` indicate?
    answer: >-
      The `<impl>` field identifies each scheme's variant. For example, `m4fspeed`
      is optimized for speed and is used by ML-KEM, while `m4fstack` is another Cortex-M4F variant;
      the exact suffix depends on the scheme.
  - question: What results should I expect when running tests and benchmarks?
    answer: >-
      The test harness validates correctness against known test vectors. Benchmarks report standardized
      metrics, including cycle counts, stack usage, and code size.
  - question: How do I add a new KEM and verify it is picked up by pqm4?
    answer: >-
      Place the new scheme in its own directory under `crypto_kem/`. pqm4's build system automatically
      discovers and compiles it; verify by checking for generated binaries for the new scheme
      and running the tests and benchmarks.
# END generated_summary_faq

author: 
    - Akash Malik
    - Odin Shen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Security
armips:
    - Cortex-M
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - C
    - Python
    - GCC
    - stlink
    - QEMU

further_reading:
    - resource:
        title: pqm4 GitHub Repository
        link: https://github.com/mupq/pqm4
        type: repository
    - resource:
        title: PQCRYPTO Project
        link: https://pqcrypto.eu.org
        type: website
    - resource:
        title: PQClean GitHub Repository
        link: https://github.com/PQClean/PQClean
        type: repository
    - resource:
        title: stlink open source STM32 programming toolset
        link: https://github.com/stlink-org/stlink
        type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
