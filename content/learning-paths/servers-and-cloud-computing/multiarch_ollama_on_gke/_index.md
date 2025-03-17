---
title: Run ollama in a multi-architecture nodes and containers environment with on GKE.

minutes_to_complete: 30

who_is_this_for: |
  This learning path is for those interested in learning how to easily migrate from a single platform (x86) Kubernetes cluster to a hybrid (Arm and x86) cluster with multi-architectural images on GKE, specifically with ollama.
  
    Although tutorial will be GKE-specific with ollama, the provided YAML will work with any deployment on any on any cloud. 

  In this learning path, you will learn how to setup a GKE cluster with both x86 and Arm-based nodes. With nodes running both architectures, you'll next deploy a popular free, open source tool called Ollama which makes it easy to run popular AIML models on any platform (on-prem, locally on your laptop, and on a cloud provider).
  
  Once you are running a multi-architecture cluster, you can take it to the next level to see price performance advantages of running your workloads on Arm vs x86.  Experiment further by researching which existing, and upcoming workloads could benefit most from single, or multi-architectural clusters.
 

learning_objectives:
  - Spin up a GKE cluster with an x86 node.
  - Apply an ollama-x86-based Deployment and Service.
  - Add a new, Arm-based Axion node to the cluster.
  - Apply an ollama-arm-based Deployment to the existing Service.
  - Learn how to use taints and tolerations on GKE clusters to schedule application pods on architecture-specific nodes
  - Benchmark price/performance advantages of running your workloads on Arm vs x86.
  - Experiment further by researching which existing, and upcoming workloads could benefit most from single, or multi-architectural clusters.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). Create an account if needed.
    - A computer with [Google Cloud CLI](/install-guides/gcloud) and [kubectl](/install-guides/kubectl/)installed.

author:
    - Geremy Cohen

### Tags
skilllevels: Introductory

subjects: Containers and Virtualization
cloud_service_providers: Google Cloud

    
armips:
    - Neoverse

operatingsystems:
    - Linux

tools_software_languages:
    - LLM
    - ollama
    - GenAI

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
    - resource: 
        title: Llama-2-7B-Chat-GGUF
        link: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
