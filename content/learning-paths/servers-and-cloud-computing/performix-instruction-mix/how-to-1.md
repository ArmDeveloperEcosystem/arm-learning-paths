---
title: Understand profiling with Arm Performix Instruction Mix
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What the Arm Performix Instruction Mix recipe is

The Arm Performix Instruction Mix recipe shows the types and proportions of machine instructions your workload executes at runtime and in static analysis, so you can see how efficiently your code uses Arm CPU hardware resources.

The Instruction Mix recipe classifies each instruction into a group. The available groups depend on the Neoverse architecture version you are profiling. Therefore the categories you see might vary depending on the version of Arm Neoverse you are using. Typical categories include:

- integer and floating-point arithmetic
- memory loads and stores (including exclusive operations)
- control flow instructions, such as branches and loops
- specialized instructions, such as cryptographic operations
- SIMD (Single Instruction, Multiple Data) instructions, including Neon (fixed 128-bit) and SVE (scalable vector length)

The Instruction Mix result gives you two complementary views:

- static analysis, which inspects compiled machine code without running it
- dynamic analysis, which measures instruction usage during real execution

Together, these views help you verify whether architecture-specific features are actually active in hot code paths.

Instruction Mix is useful when you need to confirm that performance-critical code uses Arm CPU features effectively. This is especially helpful when you are, for example, validating the effectiveness of compiler autovectorization.

For example, if a hot function is mostly scalar at runtime when you expected Neon or SVE activity, that often indicates missed vectorization opportunities. You can then focus optimization work on compiler flags, data layout, loop structure, and kernel implementation to improve throughput where it matters most.

## GPT-2 as a test workload

You can run the [GPT-2 Medium](https://huggingface.co/openai-community/gpt2-medium) model on a minimal C++ inference engine to analyze instruction mix and throughput. This model is available under a [modified MIT License](https://github.com/openai/gpt-2/blob/master/LICENSE). You will confirm that matrix multiplication (`matmul`) is the hot path, then compare how scalar, Neon, and SVE implementations change instruction behavior and token generation speed. 

You'll implement only the forward inference path, with no back propagation or training. You don't need to understand the full transformer architecture to complete this Learning Path. Familiarity with matrix multiplication is enough. For background on GPT-2, see the original 2019 paper, [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf).

You'll also try implementing your own `matmul` kernels that target Neon and SVE, then use instruction mix data to verify that these vector paths are active and improving throughput.

## What you've learned and what's next

You now know what instruction mix represents and why it matters for LLM inference optimization on Arm.

Next, you'll set up the GPT-2 example, build the binaries, and run a baseline test.
