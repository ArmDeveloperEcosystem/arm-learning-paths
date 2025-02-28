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


Here’s an expanded version of your section with added details on challenges, tradeoffs, and example use cases:

## Challenges inherent in building a RAG system

While RAG systems improve AI-generated content, they also introduce several challenges:

* Efficient and Accurate Retrieval: Ensuring that the system retrieves the most relevant and high-quality information is critical. Poor retrieval results can lead to irrelevant or misleading responses. Choosing the right similarity search algorithm and data chunking strategy is key here.
* Context Length Limitations: All models, including the GitHub Copilot API, have limitations on the amount of information they can process at once, requiring careful selection and ranking of retrieved data.
* Handling Conflicting Information: If your knowledge base has contradictory information, the system may struggle to reconcile them and generate a coherent response.
* Scalability and Latency: Querying large knowledge bases and integrating retrieval with generation can increase response time. This is another place where the choice of similarity search algorithm has an impact.
* Data Freshness and Maintenance: The knowledge base must be regularly updated to ensure the system remains accurate and relevant.

For an example of a production RAG GitHub Copilot Extension, you can check out [Arm for GitHub Copilot](https://github.com/marketplace/arm-for-github-copilot) in the GitHub Marketplace.