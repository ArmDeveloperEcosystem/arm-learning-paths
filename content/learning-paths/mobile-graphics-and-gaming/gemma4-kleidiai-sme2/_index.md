---
title: Benchmark Gemma 4 CPU inference with KleidiAI and SME2
description: Benchmark Gemma 4 prefill and decode on macOS with LiteRT-LM and KleidiAI SME2 kernels, and compare results from two devices.

minutes_to_complete: 90

who_is_this_for: Software developers and performance engineers evaluating Gemma 4 CPU inference with LiteRT-LM, KleidiAI, and XNNPACK on SME2 hardware.

learning_objectives:
    - Build LiteRT-LM with baseline and optimized XNNPACK kernels.
    - Download and verify the Gemma 4 E2B LiteRT-LM model.
    - Measure prefill and decode throughput at one and four CPU threads.
    - Compare throughput and verify the accelerated operator.

prerequisites:
    - An [SME2-capable device](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices), such as an M4-family Mac
    - Git, Homebrew, and Xcode Command Line Tools
    - At least 25 GB of free disk space for model files and local builds

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-23T20:56:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4efccbac644dbdafab895fb651cde9d53316a45fee37da98ea615d0fa6d4befe
  summary_generated_at: '2026-10-23T20:56:39Z'
  summary_source_hash: 4efccbac644dbdafab895fb651cde9d53316a45fee37da98ea615d0fa6d4befe
  faq_generated_at: '2026-10-23T20:56:39Z'
  faq_source_hash: 4efccbac644dbdafab895fb651cde9d53316a45fee37da98ea615d0fa6d4befe
  summary: >-
    You'll benchmark Gemma 4 CPU inference on an SME2-capable Mac with LiteRT-LM and KleidiAI. First,
    you'll confirm SME2 support and prepare baseline and optimized XNNPACK sources. Next, you'll install
    the build tools and verify the downloaded model. Then, you'll run three-iteration benchmarks at one
    and four CPU threads and compare prefill and decode throughput.
    Finally, you'll check the model response and use a separate profiled run to verify the accelerated
    operator.
#   faqs:
#   - question: How do I know my Mac supports SME2 before I start building?
#     answer: >-
#       Run `uname -m`, `sysctl hw.optional.arm.FEAT_SME`, and `sysctl hw.optional.arm.FEAT_SME2`.
#       On a supported Apple M4 system, expect `arm64` and a value of `1` for both feature flags.
#       If either flag reports `0`, the macOS performance comparison isn't valid.
#   - question: Where should the Gemma 4 LiteRT-LM model land, and what files should I see after
#       download?
#     answer: >-
#       You'll find the model under `$HOME/gemma4-prefill-bench/models/` in the
#       `gemma-4-E2B-it-litert-lm/` directory. Verify that it contains
#       `gemma-4-E2B-it.litertlm` using the checksum command in the download step.
#   - question: Where do the build outputs and benchmark results get written so I can review them?
#     answer: >-
#       Look under `$HOME/gemma4-prefill-bench/`: `bazel-output-base/` holds Bazel state,
#       `bin/` holds the saved binaries, and `results/` holds benchmark logs and metrics.
#   - question: How do I compare the baseline and optimized XNNPACK variants correctly?
#     answer: >-
#       Run both variants with the provided function, using the same model and settings at one and
#       four CPU threads. For each build and thread count, discard the first iteration as warm-up,
#       then average `Prefill Speed` and `Decode Speed` from the second and third iterations separately.
#   - question: What should I check if the throughput numbers look off or don’t match between runs?
#     answer: >-
#       Check that both variants use the same model, thread counts, and benchmark settings, with
#       caches and profiling disabled for timed runs. To verify the optimized kernel, run the separate
#       short benchmark with profiling enabled and look for `Fully Connected (NC, PQS8, QC2W)` in its
#       summary. Results can vary by device and conditions.
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
