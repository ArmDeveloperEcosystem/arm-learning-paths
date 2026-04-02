---
title: Build Semantic Search and Chatbot Retrieval Systems with Qdrant on Google Cloud C4A Axion processors
description: Learn how to deploy Qdrant on Google Cloud C4A Axion processors, generate vector embeddings with Sentence Transformers, and build a semantic search and chatbot retrieval system on Arm-based infrastructure.

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, data engineers, and platform engineers who want to build semantic search systems and chatbot retrieval pipelines on Arm64-based Google Cloud C4A Axion processors using the Qdrant vector database.

learning_objectives:
 - Deploy and run the Qdrant vector database on Google Cloud C4A Axion processors
 - Generate vector embeddings using transformer models
 - Store and index embeddings efficiently using Qdrant
 - Perform semantic similarity search using vector queries
 - Build a simple chatbot retrieval system powered by vector search

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python
  - Basic understanding of machine learning embeddings
  - Familiarity with Linux command-line operations

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers: 
- Google Cloud

armips:
- Neoverse

tools_software_languages:
- Qdrant
- Python
- Sentence Transformers
- Docker

operatingsystems:
- Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Qdrant documentation
      link: https://qdrant.tech/documentation/
      type: documentation

  - resource:
      title: Sentence Transformers documentation
      link: https://www.sbert.net/
      type: documentation

  - resource:
      title: Vector Databases Explained
      link: https://qdrant.tech/articles/what-is-a-vector-database/
      type: documentation
    
weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
