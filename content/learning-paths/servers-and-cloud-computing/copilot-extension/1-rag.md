---
title: RAG Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is a RAG system?

Retrieval Augmented Generation (RAG) is an AI framework that combines information retrieval with text generation to enhance the quality and accuracy of AI-generated content.

The basic flow of a RAG system includes:

* Retrieval: the system searches a knowledge base using a combination of vector and text search. Dense embeddings capture semantic similarities, while traditional keyword-based methods ensure precision, effectively covering edge cases.
* Augmentation: the retrieved information is added as context to a generative AI model to provide additional context for the user's query.
* Generation: the AI model uses both the retrieved knowledge and its internal understanding to generate a more useful response to the user.

The benefits of a RAG system center around improved factual accuracy of responses and the ability to integrate up-to-date information, as you can update the knowledge base without retraining the model. 

Most importantly, RAG lets you provide reference links to the user, showing the user where the information originates. This not only build trust with users but also serves as a pathway for further exploration of the source material.

## What are the challenges of building a RAG system?

While RAG systems improve AI-generated content, they also introduce several challenges:

* Efficient and Accurate Retrieval: ensuring that the system retrieves the most relevant and high-quality information is critical. Poor retrieval results can lead to irrelevant or misleading responses. Choosing the right similarity search algorithm and data chunking strategy is key here.
* Context Length Limitations: all models, including the GitHub Copilot API, have limitations on the amount of information they can process at once, requiring careful selection and ranking of retrieved data.
* Handling Conflicting Information: if your knowledge base has contradictory information, the system may struggle to reconcile them and generate a coherent response.
* Scalability and Latency: querying large knowledge bases and integrating retrieval with generation can increase response time. This is another place where the choice of similarity search algorithm has an impact.
* Data Freshness and Maintenance: The knowledge base must be regularly updated to ensure the system remains accurate and relevant.

For an example of a production RAG GitHub Copilot Extension, you can check out [Arm for GitHub Copilot](https://github.com/marketplace/arm-for-github-copilot) in the GitHub Marketplace.
