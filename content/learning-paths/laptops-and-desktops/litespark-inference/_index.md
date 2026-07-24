---
title: Accelerate LLM inference on Arm CPUs with Litespark-Inference

draft: true
cascade:
    draft: true

description: Learn how to run BitNet-2B ternary LLMs fast on Arm CPUs with Litespark-Inference - no GPU, no PyTorch - and benchmark it against PyTorch for memory, speed, and energy.

minutes_to_complete: 25

who_is_this_for: 
    This is an introductory topic for developers who want to run a
    large language model on CPU - no GPU, no PyTorch, no cloud account.
    If you can `pip install` a package, you can run Litespark-Inference.

learning_objectives:
    - Run BitNet-2B from the `litespark-inference` CLI in one line, and
      from Python in a few lines with the high-level `BitNet` API.
    - Pick the right embed dtype (`bf16` / `int8` / `int4`) for the
      memory versus quality trade-off you want.
    - Benchmark Litespark-Inference head-to-head against `transformers`
      with `torch.bfloat16` and read memory, time-to-first-token,
      throughput, and energy-consumed-per-token results.

prerequisites:
    - A Linux machine (Arm or x86_64) or an Apple silicon macOS machine,
      with Python 3.10 or later. Anything from a Raspberry Pi 5 to a
      Threadripper PRO works - Litespark-Inference auto-detects your CPU
      and picks the right kernel.
    - Litespark-Inference installed using the
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
    - Cortex-X
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
    - Python
    - C++
    - NEON
    - SDOT
    - SVE
    - llama.cpp

further_reading:
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
        title: Litespark-Inference GitHub repository
        link: https://github.com/Mindbeam-AI/Litespark-Inference
        type: website
    - resource:
        title: Litespark-Inference on PyPI
        link: https://pypi.org/project/litespark-inference/
        type: website
    - resource:
        title: microsoft/bitnet-b1.58-2B-4T model on Hugging Face
        link: https://huggingface.co/microsoft/bitnet-b1.58-2B-4T
        type: website
    - resource:
        title: llama.cpp GitHub repository
        link: https://github.com/ggml-org/llama.cpp
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

Litespark-Inference is an open-source CPU inference runtime for
ternary-weight language models, such as
[BitNet b1.58](https://arxiv.org/abs/2402.17764).
It targets the same job as `llama.cpp` for ternary models - load a
model, generate tokens fast on a normal CPU - but takes a different
implementation route. It is a small NumPy-based Python runtime
("torchless") that calls hand-written `extern "C"` matmul kernels through `ctypes`,
with one source file per architecture (NEON for Arm, AVX-512/VNNI or
AVX2+FMA for x86).

This Learning Path assumes you have already installed Litespark-Inference
using the [Litespark-Inference install guide](/install-guides/litespark-inference/),
which auto-detects your CPU - Linux on x86_64, Linux on Arm (Graviton
2/3/4 or Ampere), or macOS on Apple silicon - and compiles the right
kernel for it. Here you will run BitNet-2B from the command line and
from Python, tune the embedding dtype, and (optionally) benchmark it
head-to-head against PyTorch on the same machine.
