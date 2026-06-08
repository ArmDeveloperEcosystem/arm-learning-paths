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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:56:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d9435cc1dc1fe65432d83934e69993853dd3f294f66f98e9bcfb5f81e6ac6d5f
  summary_generated_at: '2026-06-02T04:54:26Z'
  summary_source_hash: d9435cc1dc1fe65432d83934e69993853dd3f294f66f98e9bcfb5f81e6ac6d5f
  faq_generated_at: '2026-06-03T01:56:43Z'
  faq_source_hash: d9435cc1dc1fe65432d83934e69993853dd3f294f66f98e9bcfb5f81e6ac6d5f
  summary: >-
    Build and deploy a Retrieval Augmented Generation (RAG) chatbot on Arm-based Google Cloud
    Axion processors using llama-cpp-python with KleidiAI. You will provision an Arm server running
    Ubuntu 22.04 LTS, set up a Python backend that integrates an LLM with the FAISS vector database
    and Hugging Face embeddings, apply 4-bit quantization, and expose REST endpoints. You will
    also create a Streamlit web interface for document upload and chat, then access the application
    via your instance’s external URL and review inference performance metrics. This advanced path
    targets an Arm instance with at least 16 cores, 8GB RAM, and 32GB disk, and assumes familiarity
    with Python, ML and LLM fundamentals, REST APIs, and vector databases.
  faqs:
  - question: What do I need before running this on Google Cloud Axion?
    answer: >-
      Use an Arm server instance with at least 16 cores, 8GB of RAM, and 32GB of disk space. The
      instructions target Ubuntu 22.04 LTS. You should also be comfortable with Python, ML concepts,
      REST APIs, vector databases, and LLM fundamentals.
  - question: Which ports and URLs are used by the backend and frontend?
    answer: >-
      The frontend is accessed at http://[your instance ip]:8501. The frontend is configured to
      call the backend at http://localhost:5000. If you access the frontend externally, you may
      need to allow inbound TCP traffic on port 8501.
  - question: How do I know the RAG pipeline is working after I start the servers?
    answer: >-
      Upload documents or PDFs in the Streamlit UI and submit a query that should reference those
      documents. The backend integrates LlamaCpp with FAISS and Hugging Face embeddings, so responses
      should include context drawn from your uploaded content.
  - question: How is model performance addressed in this Learning Path?
    answer: >-
      You will apply 4-bit quantization with llama-cpp-python and monitor/analyze inference performance
      metrics as part of the deployment. The provided scripts include logging and callbacks to
      surface runtime behavior.
  - question: Do I need a specific LLM or a GPU to complete the steps?
    answer: >-
      The path uses open-source LLMs via llama-cpp-python and does not specify a single required
      model. The prerequisites do not list any GPU requirement.
# END generated_summary_faq

author: Nobel Chowdary Mandepudi

### Tags
skilllevels: Advanced
armips:
    - Neoverse
subjects: ML
cloud_service_providers:
  - Google Cloud
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

