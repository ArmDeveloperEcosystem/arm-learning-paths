---
title: Build a multi-architecture Kubernetes cluster running nginx on Azure AKS

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to deploy multi-architecture Kubernetes workloads and compare nginx performance between x86 and Arm-based nodes in Azure Kubernetes Service (AKS) clusters.

learning_objectives:
    - Create a hybrid AKS cluster with both x86 and Arm64 nodes
    - Deploy nginx using multi-architecture container images across different node types
    - Verify nginx deployment and functionality on each architecture
    - Compare performance between x86 and Arm64 nginx instances
    - Learn techniques for deploying multi-architecture Kubernetes workloads

prerequisites:
    - An [Azure account](https://azure.microsoft.com/en-us/free/)
    - A local machine with [`jq`](https://jqlang.org/download/), [`curl`](https://curl.se/download.html), [`wrk`](https://github.com/wg/wrk), [Azure CLI](/install-guides/azure-cli/), and [`kubectl`](/install-guides/kubectl/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:35:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9c684631877441d8756182571940b0aa63797c5adab26c46663b95492bceffbb
  summary_generated_at: '2026-10-01T19:35:41Z'
  summary_source_hash: 9c684631877441d8756182571940b0aa63797c5adab26c46663b95492bceffbb
  faq_generated_at: '2026-10-01T19:35:41Z'
  faq_source_hash: 9c684631877441d8756182571940b0aa63797c5adab26c46663b95492bceffbb
  summary: >-
    Build a hybrid Azure Kubernetes Service (AKS) cluster with x86 and Arm nodes, then deploy
    nginx workloads to both architectures. You create the node pools, connect with `kubectl`,
    and use a utility script to inspect and test each deployment. You then add a multi-architecture
    service, compare its routing with the architecture-specific services, and monitor both workloads
    while you run load tests.
  faqs:
  - question: How do I know the AKS cluster is set up for both architectures before deploying
      nginx?
    answer: >-
      Confirm that the cluster has two node pools, one x86 and one Arm, and that `kubectl` can reach
      the cluster. Check that nodes report the expected CPU architecture so scheduling can target
      each pool.
  - question: Which nginx image should I use to run on both Arm and x86 nodes?
    answer: >-
      The deployments use a multi-architecture nginx image from Docker Hub. The container runtime
      pulls the correct image variant based on the node’s CPU architecture.
  - question: What result should I expect when the nginx services become available?
    answer: >-
      When you request a service's external endpoint, you receive JSON with `message`, `timestamp`,
      `server`, and `request_uri` fields. You see `nginx response` as the message and the serving pod's
      name in `server`.
  - question: How do I confirm that each nginx pod is running on the correct architecture?
    answer: >-
      Use `kubectl` to check each pod’s node assignment and labels. The Arm service selects pods
      with `app: nginx-multiarch` and `arch: arm`; verify that Arm pods run on the Arm node pool
      and x86 pods run on the x86 pool.
  - question: What should I check if the Arm deployment does not start or the service shows no
      endpoints?
    answer: >-
      Verify the Arm node pool exists and is Ready, and ensure the deployment and service selectors
      match, including `app: nginx-multiarch` and `arch: arm`. Also confirm the namespace and shared
      ConfigMap were created before applying the deployment.
# END generated_summary_faq

author:
    - Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory

subjects: Containers and Virtualization
platforms:
  - Microsoft Azure Cobalt

armips:
    - Neoverse

operatingsystems:
    - Linux

tools_software_languages:
    - nginx
    - Web Server
    - Azure
    - Kubernetes

further_reading:
  - resource:
      title: nginx website
      link: https://nginx.org/
      type: website
  - resource:
      title: nginx on Docker Hub
      link: https://hub.docker.com/_/nginx
      type: documentation
  - resource:
      title: Azure Kubernetes Service (AKS) documentation
      link: https://docs.microsoft.com/en-us/azure/aks/
      type: documentation
  - resource:
      title: Learn how to deploy nginx [Arm Learning Path]
      link: /learning-paths/servers-and-cloud-computing/nginx/
      type: documentation
  - resource:
      title: Learn how to tune nginx [Arm Learning Path]
      link: /learning-paths/servers-and-cloud-computing/nginx_tune/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
