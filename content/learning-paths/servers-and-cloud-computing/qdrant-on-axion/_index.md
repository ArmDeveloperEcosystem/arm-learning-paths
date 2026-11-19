---
title: Build semantic search and chat retrieval with Qdrant on Google Axion
description: Learn how to deploy Qdrant on Google Cloud C4A Axion processors, generate vector embeddings with Sentence Transformers, and build a semantic search and chatbot retrieval system on Arm-based infrastructure.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, data engineers, and platform engineers who want to build semantic search systems and chatbot retrieval pipelines on Arm64-based Google Cloud C4A Axion processors using the Qdrant vector database.

learning_objectives:
 - Deploy and run the Qdrant vector database on Google Cloud C4A Axion processors.
 - Generate vector embeddings using transformer models.
 - Store and index embeddings efficiently using Qdrant.
 - Perform semantic similarity search using vector queries.
 - Build a simple chatbot retrieval system powered by vector search.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python
  - Basic understanding of machine learning embeddings
  - Familiarity with Linux command-line operations

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T15:59:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 439ba306b67ab6a2e1f442ab548e8d6eb330b90f52434fa2a8ee6143a1bb944b
  summary_generated_at: '2026-11-19T15:59:16Z'
  summary_source_hash: 439ba306b67ab6a2e1f442ab548e8d6eb330b90f52434fa2a8ee6143a1bb944b
  faq_generated_at: '2026-11-19T15:59:16Z'
  faq_source_hash: 439ba306b67ab6a2e1f442ab548e8d6eb330b90f52434fa2a8ee6143a1bb944b
  summary: >-
    You'll deploy Qdrant on a Google Axion C4A VM and use vector embeddings for semantic search.
    You'll provision a SUSE Linux arm64 instance, prepare Qdrant, and generate embeddings from
    sample text with Sentence Transformers. After storing the vectors in a Qdrant collection,
    you'll run similarity queries and connect retrieval to a chatbot. You can then test whether
    responses use relevant stored content.
  faqs:
  - question: What do I need before provisioning the virtual machine?
    answer: >-
      You need a Google Cloud account with billing enabled. 
  - question: Which C4A machine type should I choose?
    answer: >-
      Select `c4a-standard-4` in the Google Cloud console.
  - question: Which operating system image should I use?
    answer: >-
      Choose a SUSE Linux Enterprise Server arm64 image for the C4A VM.
  - question: What should I see after indexing embeddings?
    answer: >-
      You should have a Qdrant collection containing vectors generated from the sample text.
      You can then query that collection for similar content.
  - question: How do I check whether semantic search is working?
    answer: >-
      Run a similarity query and inspect the ranked matches. If the matches seem unrelated, check
      that you inserted the embeddings. Ensure that you used the same Sentence Transformers model for
      indexing and querying.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Databases
platforms:
- Google Axion

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

