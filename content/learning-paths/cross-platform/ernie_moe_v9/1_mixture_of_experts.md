---
title: Understand Mixture of Experts architecture for edge deployment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Mixture of Experts (MoE)?

As large language models grow to tens of billions of parameters, traditional dense networks that activate all weights for every input become impractical for edge deployment, especially on CPU-only Arm devices. [Mixture of Experts (MoE)](https://en.wikipedia.org/wiki/Mixture_of_experts) offers an alternative approach that makes deploying these large models practical.

Dense networks are simple and uniform, but as model sizes increase into the billions of parameters, this structure becomes both memory-intensive and computationally demanding. For edge environments like mobile devices and embedded systems, deploying large models presents significant challenges.

Instead of activating all parameters for every computation, MoE introduces a conditional computation mechanism where each input token activates only a small subset of model components called experts. Think of it like having a team of specialists where you consult only the relevant experts for a given task. This makes MoE ideal for environments where compute and memory are constrained, such as edge AI or embedded inference.

In a typical MoE setup, the model consists of many expert sub-networks (for example, 64 experts), but for each input, a router selects only a handful to compute the result. The rest remain inactive, conserving memory and compute. The model learns this dynamic routing during training, so during inference, only a fraction of the model is active. This leads to much lower compute and memory usage without sacrificing the total model capacity or diversity of learned behaviors.

## Benefits of MoE architecture

MoE architecture provides several advantages that make it particularly well-suited for edge deployment and large-scale model development:

Scalable model size: you can increase total parameter count without linearly increasing inference cost, allowing for larger, more capable models within the same resource constraints.

Efficient inference: the architecture requires lower memory and FLOPs per input compared to dense models of equivalent capacity, making real-time applications more feasible.

Modularity: each expert can learn domain-specific patterns such as finance, medicine, or language, enabling the model to handle diverse tasks without retraining the entire network.

Specialization: the architecture encourages the model to learn distinct processing behaviors across different experts, improving performance on specialized tasks while maintaining general capability.

Routing flexibility: the dynamic expert selection makes it easier to adapt to specific tasks using fine-tuned routing strategies, allowing for task-specific optimizations without modifying the core model.

## ERNIE-4.5: An MoE model for Chinese NLP

The [ERNIE-4.5](https://huggingface.co/collections/baidu/ernie-45) model family from [Baidu](https://huggingface.co/baidu) introduces a Mixture of Experts (MoE) architecture that enables 21-billion-parameter models to be deployed in constrained environments. The model uses a softmax-based router to dynamically select the top six experts from a pool of 64 per layer, activating only this subset per token. This makes runtime both efficient and adaptive while retaining high performance and generalization.

The ERNIE-4.5 model series includes two variants. The PT (Post-Trained) variant is a general-purpose language model trained on Chinese and English data. The Thinking variant is optimized for reasoning tasks with long context support and structured outputs. Both are designed for Chinese Natural Language Processing (NLP).

This Learning Path focuses on the [ERNIE-4.5 Thinking](https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-Thinking) variant as the primary model because of its enhancements for multi-step reasoning and long-context tasks. However, you also use the [PT (Post-Trained)](https://huggingface.co/baidu/ERNIE-4.5-21B-A3B-PT) variant to compare model behavior across identical prompts, illustrating how task-specific tuning affects output quality.

## Why MoE matters for edge devices

Deploying a 21-billion-parameter dense model on a CPU-only board is impractical, but MoE changes that. The table below compares key characteristics:

| **Feature**           | **Dense Model** | **MoE Model (ERNIE-4.5-21B)** |
|-----------------------|-----------------|-------------------------------|
| Total Parameters      | 21B             | 21B                           |
| Activated Parameters  | 21B             | ~3B                           |
| Memory Usage          | Very high       | Moderate                      |
| Inference Speed       | Slow            | Fast                          |

This efficiency enables powerful language models to run locally on Arm-based platforms, making MoE not just a model design choice, but a deployment enabler.

In the next section, you set up a real Armv9 board, configure llama.cpp, and verify that you can run a 21-billion-parameter MoE model like ERNIE-4.5 efficiently without a GPU.
