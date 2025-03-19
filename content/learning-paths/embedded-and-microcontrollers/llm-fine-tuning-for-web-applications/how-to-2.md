---
title: Set up for fine tuning a large language model 

weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

All of the commands are meant to be copied into a cell in your Jupyter notebook. 

Copy each command into a cell, and use `Shift + Enter` to run the cell. After the cell is run, advance to the next command and enter it in a new cell. 

## Install the required libraries

The following commands install the necessary libraries, including Hugging Face Transformers, Datasets, and fine-tuning methods. These libraries facilitate model loading, training, and fine-tuning. 


Install the Hugging Face transformers library to access pre-trained LLMs.

```python
!pip install transformers
```

Install transformers along with PyTorch, ensuring that models are trained and fine-tuned using the Torch backend.

```python
!pip install transformers[torch]
```

The datasets library (by Hugging Face) provides access to a vast collection of pre-built datasets.

```python
!pip install datasets
```

The evaluate library provides metrics for model performance assessment.

```python
!pip install evaluate
```

### Speed up fine-tuning of Large Language Models (LLMs)

[Unsloth](https://huggingface.co/unsloth) is a library designed to speed up fine-tuning of Large Language Models (LLMs) while reducing computational costs. It optimizes training efficiency, particularly for LoRA (Low-Rank Adaptation) fine-tuning .


First, use the `%%capture` command, a Jupyter Notebook magic command that suppresses the output of a cell.

```python
%%capture
```

Next, uninstall the existing Unsloth and install the latest version directly from the GitHub repository.

```python
!pip uninstall unsloth -y && pip install --upgrade --no-cache-dir "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
```

You have now installed the required software for fine-tuning. 