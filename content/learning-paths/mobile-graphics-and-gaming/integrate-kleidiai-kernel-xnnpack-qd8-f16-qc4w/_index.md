---
title: Integrate a KleidiAI SME2 kernel into XNNPACK
description: Integrate a KleidiAI SME2 microkernel into XNNPACK with operand packing and runtime dispatch, then validate correctness on Android.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to integrate a KleidiAI Scalable Matrix Extension 2 (SME2) microkernel into an existing AI inference framework.

learning_objectives:
    - Identify the XNNPACK qd8_f16_qc4w operand formats and select a KleidiAI microkernel with a matching quantization contract.
    - Pack XNNPACK QD8 activations and QC4W weights into the layouts required by a KleidiAI SME2 kernel.
    - Add runtime SME2 dispatch with a safe fallback path.
    - Build and validate the integration on an Arm-based Android device.

prerequisites:
    - Familiarity with C or C++ and basic matrix multiplication
    - Android Debug Bridge (`adb`) and an Arm-based Android device with SME2 support

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T17:02:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2de1e59190ba89dc3b7b7972f813aeb2628ef33799df18ad558cb92cf4c53b86
  summary_generated_at: '2026-09-28T17:02:58Z'
  summary_source_hash: 2de1e59190ba89dc3b7b7972f813aeb2628ef33799df18ad558cb92cf4c53b86
  faq_generated_at: '2026-09-28T17:02:58Z'
  faq_source_hash: 2de1e59190ba89dc3b7b7972f813aeb2628ef33799df18ad558cb92cf4c53b86
  summary: >-
    You'll integrate a KleidiAI SME2 microkernel into XNNPACK's `qd8_f16_qc4w` fully connected
    operator. First, you'll examine operand formats and select a kernel with matching quantization.
    Next, you'll examine how static QC4W weights and dynamic QD8 activations are packed while preserving their numerical
    contracts. You'll then inspect how SME2 runtime dispatch is configured with the existing XNNPACK fallback. Finally,
    you'll build the Android test binary, run correctness tests on an SME2 device, and verify the
    fallback build.
  faqs:
  - question: How do I read the KleidiAI kernel name to verify that it matches qd8_f16_qc4w?
    answer: >-
      Read the name as a description of the output type, operand formats, and instruction family.
      For this operator, confirm `f16` output, a `qai8dxp` left-hand side with asymmetric int8 quantization per
      row, a `qsi4cxp` right-hand side with signed int4 quantization per channel, and `sme2_mopa` instructions.
      Reject the kernel if any part of that contract differs.
  - question: Which kernel should I avoid, and why is it incompatible?
    answer: >-
      Avoid a kernel such as `matmul_clamp_f16_qsi8d32p_qai4c32p` because it requires symmetric
      int8 quantization for each block of 32 K values. XNNPACK QD8 uses asymmetric int8 quantization
      for each row, so you'd have to dequantize and requantize the left-hand side. Instead, select the
      `qai8dxp` and `qsi4cxp` kernel that matches the existing operand contract.
  - question: When should I pack QC4W weights, and what gets stored?
    answer: >-
      Pack the QC4W right-hand side once during `xnn_create_fully_connected_nc_qd8_f16_qc4w`. The
      packed int4 weights, weight sums, per-channel scales, and bias are stored in operator memory or the
      XNNPACK weights cache so that you can reuse them across inference runs.
  - question: How do I pack the QD8 activations without requantizing?
    answer: >-
      Use the `pack_lhs` and `lhs_packed_size` helpers added by patch `0003-pack-qd8-lhs-for-kai-sme2.patch` in
      `src/qd8-f16-qc4w-gemm/qd8-f16-qc4w-gemm-minmax-16x64c4-neonsme2.c`. The patch preserves the QD8
      values, stores each row's negative zero point and scale, and pads K with that row's zero point.
      Patch `0004-dispatch-qd8-f16-qc4w-through-kai-sme2.patch` queries the kernel parameters and calls these helpers at runtime.
  - question: How do I validate the SME2 integration and the fallback build?
    answer: >-
      Build the Android test binary with KleidiAI enabled, then run the filtered
      `FULLY_CONNECTED_NC_QD8_F16_QC4W` correctness suite on an SME2 device and confirm that all 15
      tests pass. Separately, build the `//:packing` target with `xnn_enable_kleidiai=false` to
      verify that the compile-time guards preserve the non-KleidiAI configuration.
# END generated_summary_faq

author: Arm

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1
tools_software_languages:
    - C++
    - Android NDK
    - KleidiAI
    - SME2
    - XNNPACK
operatingsystems:
    - Android
    - Linux

further_reading:
    - resource:
        title: KleidiAI repository
        link: https://github.com/ARM-software/kleidiai
        type: website
    - resource:
        title: XNNPACK repository
        link: https://github.com/google/XNNPACK
        type: website
    - resource:
        title: Arm SME2 introduction, part 4
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: blog
    - resource:
        title: Understand KleidiAI SME2 matmul microkernels
        link: /learning-paths/mobile-graphics-and-gaming/kai_sme2_matmul_ukernel_explained/
        type: learning-path

### FIXED, DO NOT MODIFY
# ==============================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
