---
title: Accelerate LLM inference on Arm CPUs with Litespark-Inference
description: Run and benchmark the BitNet-2B ternary LLM on Arm CPUs using Litespark-Inference without a GPU, then compare memory usage, throughput, and energy consumption against a PyTorch baseline.

minutes_to_complete: 25

who_is_this_for: This is an introductory topic for developers who want to run a Large Language Model (LLM) on a CPU without a GPU by using Litespark-Inference.

learning_objectives:
    - Run BitNet-2B from the Litespark-Inference CLI or
      from Python using the high-level BitNet API.
    - Pick the right embed dtype (BF16, INT8, or INT4) for the
      memory versus quality trade-off you want.
    - Benchmark Litespark-Inference against PyTorch Transformers and
      interpret memory, time-to-first-token, throughput, and
      energy-per-token results.

prerequisites:
    - An Arm Linux machine or macOS machine with Apple Silicon,
      running Python 3.10 or later. The machine can be anything from a Raspberry Pi 5 to
      an Arm server.
    - Litespark-Inference installed by following the instructions in the
      [Litespark-Inference install guide](/install-guides/litespark-inference/).
    - About 5 GB of free disk for the BitNet-2B model that downloads on
      first run.

author: 
    - Nii Osae Osae Dade
    - Tony Morri
    - Sayandip Pal

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - Python
    - C

further_reading:
    - resource:
        title: "Litespark-Inference GitHub repository"
        link: https://github.com/Mindbeam-AI/Litespark-Inference
        type: website
    - resource:
        title: "Litespark Inference For CPUs: Ultra-Fast SIMD Framework for Ternary (1.58-bit) Language Models"
        link: https://arxiv.org/abs/2605.06485
        type: documentation
    - resource:
        title: "The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits (BitNet b1.58 paper)"
        link: https://arxiv.org/abs/2402.17764
        type: documentation
    - resource:
        title: "BitNet: Scaling 1-bit Transformers for Large Language Models"
        link: https://arxiv.org/abs/2310.11453
        type: documentation
    - resource:
        title: "Litespark-Inference on PyPI"
        link: https://pypi.org/project/litespark-inference/
        type: website
    - resource:
        title: "microsoft/bitnet-b1.58-2B-4T model on Hugging Face"
        link: https://huggingface.co/microsoft/bitnet-b1.58-2B-4T
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---