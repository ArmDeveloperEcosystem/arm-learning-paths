---
title: Why MoE Models Let Edge Devices Run 21B LLMs
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Mixture of Experts (MoE)?

As large language models grow to tens of billions of parameters, traditional dense networks — which activate all weights for every input — become infeasible for edge deployment, especially on CPU-only Arm devices. [Mixture of Experts (MoE)](https://en.wikipedia.org/wiki/Mixture_of_experts) offers a breakthrough.

This is simple and uniform, but as model sizes increase—into the billions of parameters—this structure becomes both memory-intensive and compute-intensive. For edge environments like mobile devices, embedded systems, this makes deploying large models nearly impossible.

***[Mixture of Experts (MoE)](https://en.wikipedia.org/wiki/Mixture_of_experts)*** offers an alternative. 
Instead of using all parameters all the time, MoE introduces a conditional computation mechanism: each input token only activates a small subset of model components (called ***experts***). 
Think of it like having a team of specialists, and only calling the relevant few for a given task. This makes MoE ideal for environments where compute or memory is constrained, such as edge AI or embedded inference.


In MoE:
- The model consists of many expert sub-networks (e.g., 64 experts).
- For each input, a router selects only 2–4 experts to compute the result.
- The rest of the experts remain inactive, conserving memory and compute.

This dynamic routing is typically learned during training. In inference, only a fraction of the model is active, leading to much lower compute and memory usage ***without sacrificing the total model capacity** or ***diversity of learned behaviors***.


## Benefits of MoE Architecture

- Scalable Model Size: Increase total parameter count without linearly increasing inference cost.
- Efficient Inference: Lower memory and FLOPs per input.
- Modularity: Each expert can learn domain-specific patterns (e.g., finance, medicine, language).
- Specialization: Encourages the model to learn distinct processing behaviors across different experts.
- Routing Flexibility: Makes it easier to adapt to specific tasks using fine-tuned expert selection.

## ERNIE-4.5: A MoE Model for Chinese NLP

The [ERNIE-4.5](https://huggingface.co/collections/baidu/ernie-45) model family from [Baidu](https://huggingface.co/baidu) introduces a Mixture-of-Experts (MoE) architecture, which enables massive models (e.g., 21 billion parameters) to be deployed in constrained environments. MoE models dynamically activate only a small subset of parameters (e.g., 2–4 experts) during inference.
Specifically, ERNIE-4.5 uses a softmax-based router to select the top-6 experts from a pool of 64 per layer, activating only a subset dynamically per token. This makes runtime both efficient and adaptive. This architecture allows the model to retain high performance and generalization while drastically reducing inference-time resource requirements.

ERNIE-4.5 Model Series:
- PT (Post-Trained): General-purpose language model trained on Chinese and English data.
- Thinking: Optimized for reasoning tasks with long context support and structured outputs.

In this learning path, we focus on the [ERNIE-4.5 Thinking](https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-Thinking) variant as our primary model due to its enhancements for multi-step reasoning and long-context tasks. However, we also introduce the [PT (Post-Trained)](https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-PT) variant to allow learners to compare model behavior across identical prompts, illustrating how task-specific tuning affects output quality.

## Why MoE Matters for Edge Devices

Deploying a 21B dense model on a CPU-only board is infeasible. But MoE changes that:

| **Feature**           | **Dense Model** | **MoE Model (e.g., ERNIE-4.5-21B)** |
|-----------------------|-----------------|---------------|
| `Total Parameters`    | 21B             | 21B           |
| `Activated Parameters`| 21B             | ~3B           |
| `Memory Usage`        | Very high       | Moderate      |
| `Inference Speed`     | Slow            | Fast          |

This efficiency enables powerful language models to be run locally on ARM-based platforms — making MoE not just a model design choice, but a deployment enabler.

In the next module, you’ll bring this architecture to life — preparing a real Armv9 board, setting up llama.cpp, and verifying that a 21B MoE model like ERNIE-4.5 can run efficiently with no GPU required.
