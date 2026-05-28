---
title: Build RAG applications with LlamaIndex on Google Cloud C4A Axion VM

draft: true
cascade:
    draft: true
    
description: Set up LlamaIndex on Google Cloud C4A Axion Arm VMs running SUSE Linux to build browser-based Retrieval-Augmented Generation (RAG) applications using local LLMs, vector databases, and FastAPI.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers, AI engineers, ML engineers, and software developers who want to build Retrieval-Augmented Generation (RAG) applications using LlamaIndex on SUSE Linux Enterprise Server (SLES) Arm64, integrate vector databases, and query custom documents using local LLMs.

learning_objectives:
    - Install and configure LlamaIndex on Google Cloud C4A Axion processors for Arm64
    - Build indexing and retrieval pipelines using LlamaIndex
    - Integrate ChromaDB vector databases with local LLMs using Ollama
    - Build and test a browser-based RAG application using FastAPI

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and AI/LLM concepts

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - Google Cloud

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

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

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

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
