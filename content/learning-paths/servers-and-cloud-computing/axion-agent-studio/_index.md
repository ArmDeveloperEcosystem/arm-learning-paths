---
title: Run AI coding agents with GKE Agent Sandbox on Google Axion
description: Use hosted Gemini planning and local Gemma inference on Arm-based Axion CPUs to implement, test, and preview an e-commerce checkout change.
lastmod: 2026-11-09
minutes_to_complete: 120
who_is_this_for: This is an advanced topic for developers familiar with Python, containers, and Kubernetes who want to run and validate a bounded coding-agent workflow on Arm-based cloud infrastructure.
learning_objectives:
  - Deploy a manager, three local model workers, and an isolated validator on an existing compatible GKE cluster.
  - Submit a checkout change and inspect the plan, generated files, and independent test results.
  - Verify Arm VM placement and distinguish workload CPU usage from VM capacity.
  - Compare the original and validated checkout, then remove the tutorial workloads.
prerequisites:
  - An existing GKE Standard cluster with Workload Identity Federation, enforced NetworkPolicy, and the compatible Agent Sandbox API described in Prepare your environment
  - Available C4A and N4A node capacity, Artifact Registry access, and a Google Cloud project with billing and Vertex AI model access
  - A Linux or macOS workstation with Bash, Git, Python 3.12, Node.js 22, Google Cloud CLI, the GKE authentication plugin, kubectl, and Docker Buildx
  - Permission to deploy namespaced Kubernetes resources and an administrator who can configure node pools and the required IAM binding
  - The versioned companion source linked in Prepare your environment, plus permission to use the model and application code under their respective licenses
author: Rani Chowdary Mandepudi
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
  - Neoverse
platforms:
  - Google Axion
tools_software_languages:
  - Google Kubernetes Engine
  - gVisor
  - Python
  - Gemma
  - llama.cpp
operatingsystems:
  - Linux
  - macOS
further_reading:
  - resource:
      title: Install Agent Sandbox on GKE
      link: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/how-install-agent-sandbox
      type: documentation
  - resource:
      title: GKE Sandbox isolation model
      link: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods
      type: documentation
  - resource:
      title: Arm workloads on GKE
      link: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke
      type: documentation
  - resource:
      title: Authenticate to Google Cloud APIs from GKE workloads
      link: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity
      type: documentation
  - resource:
      title: Gemma E4B GGUF model files at the recorded revision
      link: https://huggingface.co/ggml-org/gemma-4-E4B-it-GGUF/tree/b8093469224f83f5c38f691eb906c380e9e63114
      type: website
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
draft: true
cascade:
  draft: true
---
