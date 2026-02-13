---
title: Understand fine-tuning
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Why fine-tuning matters for domain knowledge

Pre-trained models like Llama 3.1 8B have broad language skills, but they don't know everything. Ask the base model about the maximum clock speed of the RP2350 microcontroller and it confidently answers "1.8 GHz," a completely fabricated number. The actual specification is 150 MHz.

Fine-tuning fixes this by training the model on real data from Raspberry Pi datasheets. After fine-tuning, the same model answers correctly: "The RP2350 supports up to 150 MHz." No hallucination, no guessing.

The process breaks down into three steps:

1. Patch the NVIDIA playbook's fine-tuning script to load a custom dataset, then run training
2. Serve both the original and fine-tuned models using vLLM
3. Compare the outputs side by side to see factual accuracy improve

To understand why this works, you need to know three things: what supervised fine-tuning does, how the training data is structured, and what options you have for making fine-tuning efficient on your hardware.

## How supervised fine-tuning adapts a model

Pre-trained LLMs learn general language patterns from massive text datasets. Supervised fine-tuning (SFT) takes that foundation and reshapes the model's behavior using labeled examples that show it how to respond to specific prompts.

Think of it as teaching by example. You provide pairs of inputs and desired outputs, and the training process adjusts the model's parameters so its responses look more like your examples. The model's original knowledge stays intact, but SFT steers how that knowledge gets applied and fills in gaps where the base model lacks specific domain expertise.

The key benefit is efficiency. Pre-training a model from scratch can take thousands of GPUs and trillions of tokens of data. Fine-tuning achieves targeted improvements with hundreds or thousands of examples on a single GPU, which makes the DGX Spark an ideal platform for the task.

## How the training data is structured

The NVIDIA playbook scripts use the Alpaca prompt format, which structures each training example with three fields:

**Instruction** -- the question or task (for example, "What is the maximum clock speed of the RP2350?")

**Input** -- optional additional context (left empty for most questions)

**Output** -- the correct answer sourced from official datasheets

Here's an example from the dataset you'll use:

```json
{
  "instruction": "How many GPIO pins does the Raspberry Pi Pico 2 provide?",
  "input": "",
  "output": "The Raspberry Pi Pico 2 provides 26 GPIO pins."
}
```

During training, these fields are combined into a prompt template that the model learns to recognize and complete:

```text
Below is an instruction that describes a task, paired with an input
that provides further context. Write a response that appropriately
completes the request.

### Instruction: How many GPIO pins does the Raspberry Pi Pico 2 provide?

### Input:

### Response: The Raspberry Pi Pico 2 provides 26 GPIO pins.
```

The dataset you'll use contains around 250 question-answer pairs extracted from official Raspberry Pi datasheets covering the RP2040, RP2350, Pico, Pico 2, Compute Module 4, and other boards. After training on these examples, the model learns to respond with accurate, datasheet-sourced facts instead of hallucinating specifications.

## Choosing a fine-tuning approach

Not every model fits entirely in GPU memory during training. The fine-tuning scripts you'll work with in the next section offer several approaches to handle this:

**Full fine-tuning** updates every parameter in the model. This gives the best results but needs enough GPU memory to hold the full model plus the optimizer state and gradients. For smaller models like Llama 3.2 3B, the DGX Spark handles this comfortably.

**LoRA (Low-Rank Adaptation)** freezes the original model weights and trains a small set of additional parameters instead. The memory savings are significant because you only store gradients and optimizer state for a fraction of the total parameters. This is practical for 8B-class models.

**QLoRA (Quantized LoRA)** goes a step further by loading the frozen model weights in 4-bit precision. Combined with LoRA's parameter-efficient training, this lets you fine-tune 70B-class models that would otherwise exceed available memory.

The script you'll run in the next section uses full fine-tuning by default, but the playbook includes LoRA and QLoRA scripts for larger models.

## What you've accomplished and what's next

In this section you learned:

- Why fine-tuning is valuable for teaching domain-specific facts to a base model
- How Raspberry Pi datasheet Q&A pairs are structured in the Alpaca prompt format
- The differences between full fine-tuning, LoRA, and QLoRA

In the next section, you'll walk through the fine-tuning script, patch it to load the Raspberry Pi dataset, and run training to produce your own fine-tuned model.
