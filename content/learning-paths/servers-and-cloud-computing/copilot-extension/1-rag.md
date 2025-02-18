---
title: RAG Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a RAG system?

RAG stands for "Retrieval Augmented Generation". It describes an AI framework that combines information retrieval with text generation to improve the quality and accuracy of AI-generated content.

The basic flow of a RAG system looks like this:

1. Retrieval: The system searches a knowledge base, usually using some combination of vector and/or text search.
2. Augmentation: The retrieved information is then provided as context to a generative AI model to provide additional context for the user's query.
3. The AI model uses both the retrieved knowledge and its internal understanding to generate a more useful response to the user.

The benefits of a RAG system revolve around improved factual accuracy of responses. It also allows a system to understand more up-to-date information, since you can add additional knowledge to the knowledge base much more easily than you could retrain the model.

Most importantly, RAG lets you provide reference links to the user, showing the user where the system is getting its information.

## The GitHub repository

Arm has provided a companion GitHub repo for this Learning Path that serves as a Python-based Copilot RAG Extension example.

To clone the repo for later reference, run

```bash
git clone https://github.com/ArmDeveloperEcosystem/python-rag-extension.git
```