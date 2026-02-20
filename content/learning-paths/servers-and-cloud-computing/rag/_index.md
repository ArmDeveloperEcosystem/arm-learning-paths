---
title: Deploy a RAG-based Chatbot with llama-cpp-python using KleidiAI on Google Axion processors

minutes_to_complete: 45

who_is_this_for: This Learning Path is for software developers, ML engineers, and those looking to deploy production-ready LLM chatbots with Retrieval Augmented Generation (RAG) capabilities, knowledge base integration, and performance optimization for Arm Architecture.

learning_objectives:
    - Set up llama-cpp-python optimized for Arm servers.
    - Implement RAG architecture using the Facebook AI Similarity Search (FAISS) vector database.
    - Optimize model performance through 4-bit quantization.
    - Build a web interface for document upload and chat.
    - Monitor and analyze inference performance metrics.

prerequisites:
    - A Google Cloud Axion (or other Arm) compute instance with at least 16 cores, 8GB of RAM, and 32GB disk space.
    - Basic understanding of Python and ML concepts.
    - Familiarity with REST APIs and web services.
    - Basic knowledge of vector databases.
    - Understanding of LLM fundamentals.

author: Nobel Chowdary Mandepudi

### Tags
skilllevels: Advanced
cloud_service_providers:
  - Google Cloud
armips:
    - Neoverse
subjects: ML
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - Streamlit
    - Google Axion
    - Demo
    - Hugging Face

further_reading:
    - resource:
        title: Getting started with Llama
        link: https://llama.meta.com/get-started
        type: documentation
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: Democratizing Generative AI with CPU-based inference 
        link: https://blogs.oracle.com/ai-and-datascience/post/democratizing-generative-ai-with-cpu-based-inference
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
