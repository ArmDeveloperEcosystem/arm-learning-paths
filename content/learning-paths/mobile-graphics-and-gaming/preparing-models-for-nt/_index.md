---
title: Prepare models for neural graphics with Arm neural technology
description: Learn how to export a PyTorch model through the ExecuTorch VGF backend, inspect the generated artifacts, and use TOSA IR when you need deeper debugging for neural graphics workflows.

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers who want to understand and debug the model preparation flow used by Arm neural technology in neural graphics pipelines.

learning_objectives:
    - Build and export a PyTorch model for ExecuTorch
    - Generate `.vgf` artifacts with the ExecuTorch VGF backend
    - Visualize model structure and generated artifacts using Model Explorer
    - Inspect Tensor Operator Set Architecture (TOSA) intermediate representation when you need to debug operator lowering
    - Validate the generated model with an ExecuTorch runner and connect it to ML Extensions for Vulkan workflows

prerequisites:
    - Basic PyTorch and Python experience
    - A Linux machine or macOS machine with Apple Silicon
    - Python version greater than 3.10 and less than 3.14, and Git installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-21T17:24:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8e7d30587d44cfb79d6568d49115316e2711391c379c3c43b34d1d6a2256d2df
  summary_generated_at: '2026-08-21T17:24:50Z'
  summary_source_hash: 8e7d30587d44cfb79d6568d49115316e2711391c379c3c43b34d1d6a2256d2df
  faq_generated_at: '2026-08-21T17:24:50Z'
  faq_source_hash: 8e7d30587d44cfb79d6568d49115316e2711391c379c3c43b34d1d6a2256d2df
  summary: >-
    You'll prepare a PyTorch model for Arm neural technology by exporting a small `AddSigmoid`
    reference model with the ExecuTorch VGF backend. First, you'll set up the required environment, generate
    `.vgf` and `.pte` artifacts, and optionally validate the `.pte` with the VKML runner. Then, you'll
    inspect the artifacts in Model Explorer and extract TOSA
    artifacts to debug operator lowering, tensor layouts, and shape flow.
  faqs:
  - question: Which Python version do I need, and how do I check it before creating the environment?
    answer: >-
      Use Python 3.10 or later and earlier than 3.14. Run `python3 --version` and confirm that the
      reported version is in that range.
  - question: Why should I start with a minimal AddSigmoid model instead of a production NSS model?
    answer: >-
      Start with a small graph to make the export and conversion flow easier to inspect. You can
      validate PyTorch export, VGF generation, and artifact inspection before you move to a production
      NSS model.
  - question: How do I know the VGF export succeeded?
    answer: >-
      After you run `python export_vgf.py`, check for `.vgf` artifacts in `executorch-model/` and
      the generated `as-vgf.pte` file. For optional runtime validation, build the VKML runner and
      run `python run_vgf_pte.py`.
  - question: How should I launch Model Explorer, and what do I open first?
    answer: >-
      Install Model Explorer and the `pte-adapter-model-explorer`, `tosa-adapter-model-explorer`,
      and `vgf-adapter-model-explorer` packages in your active virtual environment. Run
      `model-explorer --extensions=pte_adapter_model_explorer,tosa_adapter_model_explorer,vgf_adapter_model_explorer`,
      then open a `.vgf` artifact in `executorch-model/` or `as-vgf.pte`.
  - question: When should I use TOSA for debugging?
    answer: >-
      Use TOSA to check operator lowering before backend compilation, confirm tensor layout and
      shape flow, or compare behavior when different backends produce different results.
# END generated_summary_faq

author: Joshua Marshall-Law

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - ExecuTorch
    - PyTorch
    - Model Explorer
    - Jupyter Notebook
    - Vulkan
    - TOSA
    - NX
operatingsystems:
    - Linux
    - macOS

further_reading:
    - resource:
        title: Fine-tune neural graphics models using Model Gym
        link: /learning-paths/mobile-graphics-and-gaming/model-training-gym/
        type: learningpath
    - resource:
        title: Quantize neural upscaling models with ExecuTorch
        link: /learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/
        type: learningpath
    - resource:
        title: Enable neural graphics using ML Extensions for Vulkan
        link: /learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/
        type: learningpath
    - resource:
        title: Enable Neural Super Sampling in Unreal Engine with ML Extensions
        link: /learning-paths/mobile-graphics-and-gaming/nss-unreal/
        type: learningpath
    - resource:
        title: Running a test with the Scenario Runner
        link: /learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/4-scenario-runner/
        type: learningpath
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: VGF library (GitHub)
        link: https://github.com/arm/ai-ml-sdk-vgf-library
        type: code

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
