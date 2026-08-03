---
title: Run and benchmark BitNet-2B inference on Arm CPUs with Litespark-Inference
description: Run and benchmark BitNet-2B on Arm CPUs with Litespark-Inference, compare memory use and performance with PyTorch, and measure energy per token on Apple silicon.

minutes_to_complete: 25

who_is_this_for: This is an introductory topic for developers who want to run a large language model (LLM) on a CPU without a GPU using Litespark-Inference.

learning_objectives:
    - Run BitNet-2B from the Litespark-Inference CLI or
      from Python using the high-level BitNet API.
    - Pick the right embed dtype (BF16, INT8, or INT4) for the
      memory versus quality trade-off you want.
    - Compare Litespark-Inference with PyTorch Transformers for memory,
      time to first token, and throughput.
    - Measure energy per token on Apple silicon.

prerequisites:
    - An Arm Linux machine or macOS machine with Apple Silicon,
      running Python 3.10 or later. The machine can be anything from a Raspberry Pi 5 to
      an Arm server.
    - Litespark-Inference installed by following the instructions in the
      [Litespark-Inference install guide](/install-guides/litespark-inference/).
    - About 5 GB of free disk for the BitNet-2B model that downloads on
      first run.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-03T16:54:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0c93a626cbf96526c50b56917cb1a66676648509c9b7c0891b44599a55036def
  summary_generated_at: '2026-08-03T16:54:30Z'
  summary_source_hash: 0c93a626cbf96526c50b56917cb1a66676648509c9b7c0891b44599a55036def
  faq_generated_at: '2026-08-03T16:54:30Z'
  faq_source_hash: 0c93a626cbf96526c50b56917cb1a66676648509c9b7c0891b44599a55036def
  summary: >-
    You'll run BitNet-2B on Arm CPUs with Litespark-Inference from the command line and Python.
    You'll verify the Arm Neon kernel and compare BF16 and INT4 embedding memory use. Then, you'll
    benchmark the torchless runtime against PyTorch for memory, time to first token, and throughput.
    On Apple silicon, you'll also measure energy per token.
  faqs:
  - question: How do I limit the number of tokens generated from the CLI?
    answer: >-
      You can add `--max-tokens` to `litespark-inference generate`. For example, use
      `--max-tokens 64` to limit the response to 64 new tokens.
  - question: Which embedding data type should I start with, and how do I set it?
    answer: >-
      Start with BF16 as the reference by adding `--embed-dtype bf16`. You can use INT8 or INT4
      to reduce memory use, but validate output quality for your workload.
  - question: How do I verify that Litespark-Inference is using the Arm-optimized torchless runtime?
    answer: >-
      Run `python -m litespark_inference.torchless info`. On Arm, confirm that the kernel name
      contains `neon` and that `OpenMP` is `True`. The generation command also identifies the
      torchless runtime at startup.
  - question: How do I compare Litespark-Inference with a PyTorch baseline?
    answer: >-
      Add `--pytorch` to `litespark-benchmark`. The command runs the torchless and PyTorch passes,
      then reports memory use, time to first token, prompt prefill throughput, and token-generation
      throughput for comparison.
  - question: How do I measure energy per token on Apple silicon?
    answer: >-
      Refresh your `sudo` credentials with `sudo -v`, then add `--power` to
      `litespark-benchmark`. If the results report `available: false`, your system doesn't expose
      a supported energy counter.
# END generated_summary_faq

author: 
    - Nii Osae Osae Dade
    - Tony Morri
    - Sayandip Pal

generate_summary_faq: false
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

shared_path: true
shared_between:
    - laptops-and-desktops
    - servers-and-cloud-computing

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
