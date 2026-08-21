---
title: Run ExecuTorch Llama 3.2 1B Instruct on an Android phone with Vulkan

description: Learn how to export Llama 3.2 1B Instruct with ExecuTorch, build the Android Vulkan runtime, and run the model on a Vivo X300 Pro or similar Android phone.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to export a Llama 3.2 model with ExecuTorch and run it on an Android phone through the Vulkan backend.

learning_objectives:
  - Set up a Linux host for Android cross-compilation, ADB deployment, and Vulkan-backed ExecuTorch builds.
  - Export Meta Llama 3.2 1B Instruct to a Vulkan-enabled `.pte` with the exact quantization settings used in the guide.
  - Build, deploy, measure, and validate the Android `llama_main` runner on a Vivo X300 Pro or similar Android phone.

prerequisites:
  - A Linux host with enough disk space for the ExecuTorch source tree, Android SDK and NDK, Vulkan SDK, and the Llama checkpoint
  - A Vivo X300 Pro or a similar Android phone with USB debugging enabled
  - A Hugging Face account
  - Working familiarity with the shell, Python virtual environments, and Android `adb` workflows

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-19T20:11:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 56f178dd761d2b0aa827e4748f604635373c77222d22d5513e5449aa9433616f
  summary_generated_at: '2026-08-19T20:11:06Z'
  summary_source_hash: 56f178dd761d2b0aa827e4748f604635373c77222d22d5513e5449aa9433616f
  faq_generated_at: '2026-08-19T20:11:06Z'
  faq_source_hash: 56f178dd761d2b0aa827e4748f604635373c77222d22d5513e5449aa9433616f
  summary: >-
    You'll export Meta Llama 3.2 1B Instruct with ExecuTorch, build an Android Vulkan runtime, and
    run it on a Vivo X300 Pro. First, you'll prepare a Linux host and Android device, install ExecuTorch 1.4
    and the gated model files, then export a Vulkan-enabled `.pte` with the specified quantization,
    KV-cache, context, and metadata settings. After exporting, you'll install `glslc`, cross-compile the runtime and
    `llama_main`, deploy the artifacts with `adb`, and verify Vulkan libraries during inference.
  faqs:
  - question: Do I need a GPU on my Linux host for this workflow?
    answer: >-
      No. You can export, quantize, and cross-compile on a Linux host without CUDA, ROCm, or a
      working Vulkan GPU.
  - question: How do I use the correct ExecuTorch source and Python setup?
    answer: >-
      Run `git clone --branch release/1.4 --recursive https://github.com/pytorch/executorch.git` and
      `git submodule update --init --recursive`. Create the environment with `python3.12 -m venv .venv`,
      activate it with `source .venv/bin/activate`, then install the pinned PyTorch version `2.13.0+cpu`
      before continuing.
  - question: How large is the exported Vulkan .pte file?
    answer: >-
      The exported Vulkan `.pte` file is about 1.8 GB.
  - question: How do I verify the Android Vulkan build can find glslc?
    answer: >-
      Install the LunarG Vulkan SDK on the host and source its `setup-env.sh` script. Run
      `which glslc` and `glslc --version` to confirm that the compiler is available to the build.
  - question: Which performance metrics should I record on the phone?
    answer: >-
      Record model load time, prompt and decode throughput, total inference time, time to first
      token, RSS, and sampling time. The `PyTorchObserver` summary also reports
      `prefill_token_per_sec` and `decode_token_per_sec`.
# END generated_summary_faq

author: Ash Naik

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_maintenance: false

skilllevels: Advanced

subjects: ML

operatingsystems:
  - Linux
  - Android

tools_software_languages:
  - ExecuTorch
  - PyTorch
  - Python
  - Android
  - Vulkan
  - glslc
  - Hugging Face
armips:
  - Mali

further_reading:
  - resource:
      title: ExecuTorch repository
      link: https://github.com/pytorch/executorch
      type: documentation
  - resource:
      title: ExecuTorch Llama documentation
      link: https://github.com/pytorch/executorch/blob/main/docs/source/llm/llama.md
      type: documentation
  - resource:
      title: ExecuTorch Android Vulkan documentation
      link: https://github.com/pytorch/executorch/blob/main/docs/source/android-vulkan.md
      type: documentation

# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
