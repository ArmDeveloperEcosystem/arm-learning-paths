---
title: Build a Retrieval-Augmented Generation (RAG) application using Zilliz Cloud on Arm servers

draft: true
cascade:
    draft: true

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for software developers who want to create a RAG application on Arm servers.

learning_objectives: 
    - Create a simple RAG application using Zilliz Cloud
    - Launch a LLM service on Arm servers

prerequisites:
    - Basic understanding of a RAG pipeline.
    - An AWS Graviton3 c7g.2xlarge instance, or any [Arm based instance](/learning-paths/servers-and-cloud-computing/csp) from a cloud service provider or an on-premise Arm server.
    - A [Zilliz account](https://zilliz.com/cloud), which you can sign up for with a free trial.

author_primary: Chen Zhang

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Python
    - GenAI
    - RAG
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
