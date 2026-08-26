---
title: Benchmark Gemma 4 LiteRT-LM prefill performance with KleidiAI and SME2 on macOS

minutes_to_complete: 45

draft: true
cascade:
    draft: true

who_is_this_for: This is an advanced topic for software developers and performance engineers who want a reproducible Gemma 4 prefill benchmark workflow using LiteRT-LM, KleidiAI, and XNNPACK on macOS.

learning_objectives:
    - Create a workspace with pinned LiteRT-LM and KleidiAI versions
    - Create upstream-optimized and historical-baseline XNNPACK worktrees
    - Download a LiteRT-LM-compatible Gemma 4 model from Hugging Face
    - Compare baseline and upstream SME2 benchmark results with a cache-neutral workflow

prerequisites:
    - An SME2 device (this tutorial uses macOS on Apple M4)
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
    - Armv9-A
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
