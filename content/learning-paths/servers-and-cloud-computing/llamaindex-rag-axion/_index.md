---
title: Build RAG applications with LlamaIndex on a Google Cloud C4A virtual machine

description: Set up LlamaIndex on Google Axion-based C4A Arm64 VMs running SUSE Linux to build browser-based Retrieval-Augmented Generation (RAG) applications using local LLMs, vector databases, and FastAPI.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers, AI engineers, machine learning engineers, and software developers who want to build retrieval-augmented generation (RAG) applications using LlamaIndex on SUSE Linux Enterprise Server (SLES) Arm64, integrate vector databases, and query custom documents using local large language models (LLMs).

learning_objectives:
    - Install and configure LlamaIndex on Google Cloud C4A Axion processors for Arm64.
    - Build indexing and retrieval pipelines using LlamaIndex.
    - Integrate ChromaDB vector databases with local LLMs using Ollama.
    - Build and test a browser-based RAG application using FastAPI.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python, as well as AI and LLM concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:44:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 216e01cee178fc1e8b9fa67e8a6236909bfe6281dc367d5d988a5d819383791d
  summary_generated_at: '2026-09-28T19:44:58Z'
  summary_source_hash: 216e01cee178fc1e8b9fa67e8a6236909bfe6281dc367d5d988a5d819383791d
  faq_generated_at: '2026-09-28T19:44:58Z'
  faq_source_hash: 216e01cee178fc1e8b9fa67e8a6236909bfe6281dc367d5d988a5d819383791d
  summary: >-
    You'll build a RAG application on a Google Axion C4A virtual machine (VM).
    First, you'll configure SUSE Linux, Python 3.11, LlamaIndex, Ollama, and ChromaDB. Then, you'll create a FastAPI
    backend and browser interface. You'll add sample documents, connect the indexing and retrieval
    pipeline, and submit browser queries. Finally, you'll observe how LlamaIndex retrieves context
    from ChromaDB and sends it to your local model for grounded responses.
  faqs:
  - question: Which firewall port should be opened for the browser-based app?
    answer: >-
      Open TCP port `8000`. After you create the rule, verify that it applies to the VM’s VPC
      network, then open `http://<VM-EXTERNAL-IP>:8000` after the app starts.
  - question: Which C4A machine type should I use?
    answer: >-
      Select `c4a-standard-4`, which provides four vCPUs and 16 GB of memory. 
  - question: Which Python version should I install?
    answer: >-
      Install Python 3.11 after you refresh and update the system packages. 
  - question: How do I know that the RAG pipeline is wired correctly?
    answer: >-
      Submit a query from the browser interface and confirm that the response reflects your sample
      documents. Your FastAPI backend should call LlamaIndex, retrieve context from ChromaDB, and
      send that context to the local LLM through Ollama.
  - question: What should I check if the browser UI doesn't load?
    answer: >-
      Confirm that the FastAPI server is running, the VM’s external IP is reachable, and the firewall
      rule for port `8000` is active. After confirming, open `http://<VM-EXTERNAL-IP>:8000` again.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - Google Axion

armips:
  - Neoverse

tools_software_languages:
  - LlamaIndex
  - Python
  - ChromaDB
  - Ollama
  - FastAPI

operatingsystems:
  - Linux

further_reading:
    - resource:
        title: LlamaIndex official documentation
        link: https://docs.llamaindex.ai/en/stable/
        type: documentation
    - resource:
        title: LlamaIndex GitHub repository
        link: https://github.com/run-llama/llama_index
        type: documentation
    - resource:
        title: Ollama documentation
        link: https://ollama.com/library
        type: documentation
    - resource:
        title: Introducing Google Axion Processors, our new Arm-based CPUs
        link: https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu
        type: documentation
    - resource:
        title: Getting started with Google Cloud Platform
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/csp/google/
        type: documentation

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
