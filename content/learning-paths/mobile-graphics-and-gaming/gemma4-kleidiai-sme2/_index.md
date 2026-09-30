---
title: Benchmark Gemma 4 LiteRT-LM prefill performance with KleidiAI and SME2 on macOS
description: Benchmark Gemma 4 prefill performance on macOS by comparing baseline and SME2-optimized XNNPACK paths in LiteRT-LM with KleidiAI.

minutes_to_complete: 45

draft: true
cascade:
    draft: true

who_is_this_for: This is an advanced topic for software developers and performance engineers who want a reproducible Gemma 4 prefill benchmark workflow using LiteRT-LM, KleidiAI, and XNNPACK on macOS.

learning_objectives:
    - Create a workspace with pinned LiteRT-LM and KleidiAI versions.
    - Create upstream-optimized and historical-baseline XNNPACK worktrees.
    - Download a LiteRT-LM-compatible Gemma 4 model from Hugging Face.
    - Compare baseline and upstream SME2 benchmark results.

prerequisites:
    - An SME2 device (macOS on Apple M4 is used in this Learning Path for demonstrative purposes)
    - Git, Homebrew, and Xcode Command Line Tools
    - At least 25 GB of free disk space for model files and local builds

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-14T20:55:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 87d7867854c80eb5b1a520c8958d4251d51e5e33c98f4d7b1890431ca82cfe8b
  summary_generated_at: '2026-09-14T20:55:19Z'
  summary_source_hash: 87d7867854c80eb5b1a520c8958d4251d51e5e33c98f4d7b1890431ca82cfe8b
  faq_generated_at: '2026-09-14T20:55:19Z'
  faq_source_hash: 87d7867854c80eb5b1a520c8958d4251d51e5e33c98f4d7b1890431ca82cfe8b
  summary: >-
    You'll benchmark Gemma 4 prefill performance on macOS by comparing an upstream SME2-optimized
    XNNPACK path with a historical baseline in LiteRT-LM and KleidiAI. First, you'll set up a workspace and
    verify SME and SME2 availability. Then, you'll install Bazelisk and the Hugging Face Hub CLI, and download
    a LiteRT-LM-compatible Gemma 4 E2B `.litertlm` model. You'll build both XNNPACK variants with
    identical settings, then compare three-iteration results at one and four CPU threads.
  faqs:
  - question: How do I check that my device supports SME2 before running the benchmarks?
    answer: >-
      Run `uname -m` and the `sysctl` checks for `hw.optional.arm.FEAT_SME` and
      `hw.optional.arm.FEAT_SME2`. Proceed when the architecture is `arm64` and both feature flags
      report `1`.
  - question: Which Gemma 4 model should I download?
    answer: >-
     Download the Gemma 4 E2B `.litertlm` model from Hugging
      Face. Place it in the shared model directory at `$HOME/gemma4-prefill-bench/models`.
  - question: How do I confirm that Bazel is the version expected by LiteRT-LM?
    answer: >-
      From the LiteRT-LM repository, check `.bazelversion` and run `bazelisk version`. Confirm that the Bazel version is `7.6.1`.
  - question: Why should I create separate baseline and upstream XNNPACK trees?
    answer: >-
      You'll use separate trees to build and benchmark both variants with identical settings while
      recording the exact repository revisions. This enables a clean side-by-side comparison through
      the same LiteRT-LM entrypoint.
  - question: What does the benchmark function run, and where are the results saved?
    answer: >-
      When you run the benchmark function, it builds the selected XNNPACK variant and runs
      three-iteration prefill benchmarks at one and four CPU threads. Results are written under the
      workspace results directory, so you can compare baseline and SME2-optimized runs.
# END generated_summary_faq

author: Annie Tallund

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1
tools_software_languages:
    - SME2
    - Bazel
    - LiteRT-LM
    - KleidiAI
    - XNNPACK
operatingsystems:
    - macOS

further_reading:
    - resource:
        title: Arm Scalable Matrix Extension introduction, part 1
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Arm Scalable Matrix Extension instructions, part 2
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: Arm SME2 introduction, part 4
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: blog
    - resource:
        title: LiteRT-LM repository
        link: https://github.com/google-ai-edge/LiteRT-LM
        type: website
    - resource:
        title: KleidiAI repository
        link: https://github.com/ARM-software/kleidiai
        type: website
    - resource:
        title: XNNPACK repository
        link: https://github.com/google/XNNPACK
        type: website
    - resource:
        title: Gemma 4 E2B for LiteRT-LM on Hugging Face
        link: https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
