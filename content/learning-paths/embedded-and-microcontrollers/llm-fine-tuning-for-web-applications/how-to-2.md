---
title: Fine Tuning Large Language Model - Setup Environment 
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Fine Tuning Large Language Model - Setup Environment

#### Plartform Required 
An AWS Graviton4 r8g.16xlarge instance to test Arm performance optimizations, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server or Arm based laptop.

#### Set Up Required Libraries
The following commands install the necessary libraries for the task, including Hugging Face Transformers, Datasets, and fine-tuning methods. These libraries facilitate model loading, training, and fine-tuning

###### The transformers library (by Hugging Face) provides pre-trained LLMs
```python
!pip install transformers

```
###### This installs transformers along with PyTorch, ensuring that models are trained and fine-tuned using the Torch backend.
```python
!pip install transformers[torch]
```
###### The datasets library (by Hugging Face) provides access to a vast collection of pre-built datasets

```python
!pip install datasets
```
###### The evaluate library provides metrics for model performance assessment

```python
!pip install evaluate
```
###### Speed up fine-tuning of Large Language Models (LLMs)
[Unsloth](https://huggingface.co/unsloth) is a library designed to speed up fine-tuning of Large Language Models (LLMs) while reducing computational costs. It optimizes training efficiency, particularly for LoRA (Low-Rank Adaptation) fine-tuning 
```python
%%capture
# %%capture is a Jupyter Notebook magic command that suppresses the output of a cell.

```
##### Uninstalls the existing Unsloth installation and installs the latest version directly from the GitHub repository

```python
!pip uninstall unsloth -y && pip install --upgrade --no-cache-dir "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
```