---
title: Build Semantic Search and Chatbot Retrieval Systems with Qdrant on Google Cloud C4A Axion processors
description: Learn how to deploy Qdrant on Google Cloud C4A Axion processors, generate vector embeddings with Sentence Transformers, and build a semantic search and chatbot retrieval system on Arm-based infrastructure.

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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:55:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 8b180acd30b3b00484b6e7302b61fd8c3669ef83ff7fca41972d24c5df2682b7
  summary_generated_at: '2026-06-02T04:52:49Z'
  summary_source_hash: 8b180acd30b3b00484b6e7302b61fd8c3669ef83ff7fca41972d24c5df2682b7
  faq_generated_at: '2026-06-03T01:55:47Z'
  faq_source_hash: 8b180acd30b3b00484b6e7302b61fd8c3669ef83ff7fca41972d24c5df2682b7
  summary: >-
    This Learning Path shows how to deploy the Qdrant vector database on Arm-based Google Cloud
    C4A Axion processors, generate text embeddings with Sentence Transformers in Python, and run
    semantic similarity search to power a simple chatbot retrieval system. You will provision
    a c4a-standard-4 Arm64 VM in Google Compute Engine, prepare a SLES Linux environment, install
    and run Qdrant, create and index embeddings, and issue vector queries. Tools used include
    Qdrant, Python, Sentence Transformers, and Docker. Prerequisites are a GCP account with billing
    enabled, basic Python skills, a basic understanding of embeddings, and familiarity with the
    Linux command line. The path is introductory and designed to complete in about 30 minutes.
  faqs:
  - question: Do I need anything set up in Google Cloud before I start?
    answer: >-
      Yes. You need a Google Cloud Platform account with billing enabled to provision the Axion
      C4A VM used in this Learning Path.
  - question: Which Google Cloud instance and operating system should I create?
    answer: >-
      Create a c4a-standard-4 Arm-based VM (4 vCPUs, 16 GB memory) and use a SUSE Linux Enterprise
      Server (SLES) arm64 image to host Qdrant.
  - question: How do I confirm that Qdrant is installed and running on the VM?
    answer: >-
      Start Qdrant and check that the service or container initializes without errors and is reachable
      from your client code on the VM. The steps guide you through deploying Qdrant on the Arm64
      instance.
  - question: Which Sentence Transformers model should I use to generate embeddings?
    answer: >-
      A specific model is not explicitly listed. Use a Sentence Transformers model suitable for
      text embeddings to follow the embedding and indexing steps.
  - question: What result should I expect when I run a semantic similarity query?
    answer: >-
      You should see a ranked list of the most relevant documents by meaning and context rather
      than exact keyword matches. Successful results indicate your embeddings were stored and
      indexed correctly in Qdrant.
# END generated_summary_faq

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

