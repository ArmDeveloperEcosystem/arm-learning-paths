---
title: Deploy a RAG chatbot with KleidiAI on Google Axion

minutes_to_complete: 45

who_is_this_for: This Learning Path is for software developers, ML engineers, and those looking to deploy production-ready LLM chatbots with Retrieval Augmented Generation (RAG) capabilities, knowledge base integration, and performance optimization for Arm Architecture.

learning_objectives:
    - Set up llama-cpp-python optimized for Arm servers.
    - Implement RAG architecture using the Facebook AI Similarity Search (FAISS) vector database.
    - Optimize model performance through 4-bit quantization.
    - Build a web interface for document upload and chat.
    - Monitor and analyze inference performance metrics.

prerequisites:
    - A Google Cloud Axion (or other Arm) compute instance with at least 16 cores, 8GB of RAM, and 32GB disk space
    - Basic understanding of Python and ML concepts
    - Familiarity with REST APIs and web services
    - Basic knowledge of vector databases
    - Understanding of LLM fundamentals

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:01:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1f6f741dee3f86b86de1acaf18a51e807b000f19d8da40b0a4dfdb6d356e4d54
  summary_generated_at: '2026-11-19T16:01:02Z'
  summary_source_hash: 1f6f741dee3f86b86de1acaf18a51e807b000f19d8da40b0a4dfdb6d356e4d54
  faq_generated_at: '2026-11-19T16:01:02Z'
  faq_source_hash: 1f6f741dee3f86b86de1acaf18a51e807b000f19d8da40b0a4dfdb6d356e4d54
  summary: >-
    You'll build a retrieval augmented chatbot with KleidiAI on an Arm-based Google Axion server.
    You'll prepare a llama-cpp-python backend with FAISS retrieval and expose its API through
    Flask. Then, you'll start a Streamlit frontend, upload PDF files, and ask questions that use
    retrieved context. Finally, you'll open the app in a browser and verify that the backend and
    frontend communicate.
  faqs:
  - question: How do I check whether backend.py is running?
    answer: >-
      Start `backend.py` and check that Flask listens on port `5000` without errors. You can
      then use the frontend to test a response.
  - question: What should I check when Streamlit loads but chat requests fail?
    answer: >-
      Check that the backend is running and that the `API_URL` in `frontend.py` points to its
      address and port. Restart Streamlit after changing the URL.
  - question: How do I open the app from outside the virtual machine?
    answer: >-
      Open `http://[your instance ip]:8501` in your browser. If you can't connect, allow inbound TCP port `8501` from your IP address.
  - question: Where do I upload content for retrieval?
    answer: >-
      Upload PDF files through the Streamlit interface. You can then ask questions about the
      content indexed in FAISS.
  - question: Do I run the backend and frontend in separate terminals?
    answer: >-
      Yes. Activate the virtual environment and run the Flask backend in one terminal. Open
      another terminal, activate the environment, and start the Streamlit frontend.
# END generated_summary_faq

author: Nobel Chowdary Mandepudi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
armips:
    - Neoverse
subjects: AI/ML
platforms:
  - Google Axion
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

