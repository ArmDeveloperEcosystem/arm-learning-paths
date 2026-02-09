---
title: How Fine Tuning Works
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why fine-tuning matters

Pre-trained large language models (LLMs) are trained on vast amounts of general text data, giving them broad knowledge and language understanding. However, these models often need specialization to perform well on specific tasks, domains, or to follow particular instruction formats. Fine-tuning adapts a pre-trained model to your specific use case without the computational expense of training from scratch.

Fine-tuning is essential when you need a model to:

- Understand domain-specific terminology and concepts (medical, legal, scientific)
- Follow specific instruction formats or conversation styles
- Perform specialized tasks with higher accuracy than a general-purpose model
- Align with organizational guidelines or safety requirements
- Reduce hallucinations in specific knowledge domains

The process typically requires significantly less data and compute resources than pre-training. While pre-training might use trillions of tokens on thousands of GPUs, fine-tuning can achieve excellent results with thousands or even hundreds of carefully curated examples on a single GPU or small GPU cluster, making it an ideal use case for the NVIDIA DGX Spark.

For a deeper look at LLM fine-tuning with Hugging Face transformers, see the [Hugging Face Fine-tuning Guide](https://huggingface.co/docs/transformers/training).

## How supervised fine-tuning works

Supervised fine-tuning (SFT) continues the training process on a pre-trained model using labeled examples that demonstrate the desired behavior. Unlike pre-training, which predicts the next token from unlabeled text, SFT uses input-output pairs that explicitly teach the model how to respond to specific queries or prompts.

The process works by:

**Data preparation** - You create or collect a dataset of input-output pairs. For instruction tuning, this means pairs of user prompts and desired responses. For example: "Explain photosynthesis" paired with a detailed explanation.

**Loss calculation** - The model generates predictions for the training examples, and the training algorithm calculates how different the predictions are from the target outputs. This difference is quantified using a loss function, typically cross-entropy loss for language models.

**Gradient computation** - A gradient represents the direction and magnitude of change needed for each model parameter to reduce the loss. The training process calculates gradients that indicate how to adjust each model parameter to reduce the loss. These gradients flow backward through the neural network layers via backpropagation.

**Parameter updates** - The optimizer uses the gradients to update the model's weights, making small adjustments that should improve performance on the training examples. This process repeats across many examples and multiple epochs.

**Validation** - Periodically, you evaluate the model on held-out validation data to ensure it's learning to generalize rather than simply memorizing the training set.

The key advantage of SFT is that it preserves the pre-trained model's general knowledge while adapting its behavior to match your specific examples. The model learns the patterns in your data without forgetting what it learned during pre-training.

For technical details on the algorithms behind supervised fine-tuning, refer to the [PyTorch training documentation](https://pytorch.org/tutorials/beginner/introyt/trainingyt.html).

## What instruction tuning does for a model

Instruction tuning is a specific type of supervised fine-tuning that teaches models to follow natural language instructions. Base pre-trained models are excellent at completing text but don't inherently understand how to respond to commands or questions in a conversational format. Instruction tuning bridges this gap.

The transformation happens through training on datasets where each example contains:

**Instruction** - A clear directive or question  
**Input** (optional) - Additional context or data to process  
**Output** - The desired response demonstrating correct behavior

For example:
- Instruction: "Summarize the following article"
- Input: [article text]
- Output: [concise summary]

After instruction tuning, the model learns to:

- Recognize and interpret different instruction formats
- Generate responses that directly address the given task
- Maintain an expected tone and formatting for different request types

This process dramatically improves the model's usability. While a base model might continue a prompt like "Translate this sentence to French: Hello" by generating more English text, an instruction-tuned model understands this is a task request and produces the French translation.

Popular instruction-tuning datasets include Alpaca, Dolly, and FLAN. These datasets contain diverse instructions across many domains and task types, helping models generalize to new instructions they haven't seen during training. In the next step you will use the Alpaca dataset to fine-tune a base pre-trained model.
