---
title: Benchmark Gemma 4 CPU inference with KleidiAI and SME2
description: Benchmark Gemma 4 prefill and decode on macOS with LiteRT-LM and KleidiAI SME2 kernels, and compare results from two devices.

minutes_to_complete: 90

draft: false
cascade:
    draft: false

who_is_this_for: Software developers and performance engineers evaluating Gemma 4 CPU inference with LiteRT-LM, KleidiAI, and XNNPACK on SME2 hardware.

learning_objectives:
    - Build LiteRT-LM with baseline and optimized XNNPACK kernels
    - Download and verify the Gemma 4 E2B LiteRT-LM model
    - Measure prefill and decode throughput at one and four CPU threads
    - Compare throughput and verify the accelerated operator

prerequisites:
    - An [SME2-capable device](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices), such as an M4-family Mac
    - Git, Homebrew, and Xcode Command Line Tools
    - At least 25 GB of free disk space for model files and local builds
author: Annie Tallund

generate_summary_faq: true
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
