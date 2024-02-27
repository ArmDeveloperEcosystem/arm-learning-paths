---
title: Run a 
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this learning path are for any Arm server running Ubuntu 22.04 LTS.

Before you begin, you will need to install [PyTorch](/install-guides/pytorch) on your Arm machine. 
PyTorch is a widely used machine learning framework for Python. You will use PyTorch to deploy a Natural Language Processing (NLP) model on an Arm AArch64 CPU.

## Overview

[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like Natural language processing, audio and computer vision. Hugging face has a huge collection of NLP models for tasks like translation, sentiment analysis, summarization and text generation.

In this learning path, you will download and run a popular [sentiment analysis](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) NLP model from Hugging Face and deploy it using PyTorch on your Arm server.

## Install Hugging Face Transformers for PyTorch

Hugging Face Transformers library provides APIs and tools that let you easily download and train pre-trained models. Huggging Face Transformers support multiple machine learning frameworks like PyTorch, TensorFlow and JAX. You will use transformers with PyTorch.

To install the Transformers library for PyTorch, run the following command:

```bash
pip install 'transformers[torch]'
```
This NLP model uses SciPy, an open source Python library used to solve scientific and mathematical problems.

```bash 
pip install scipy
```
