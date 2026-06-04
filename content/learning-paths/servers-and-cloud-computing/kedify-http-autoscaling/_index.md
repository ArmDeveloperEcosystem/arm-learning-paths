---
title: Autoscale HTTP applications on Kubernetes with KEDA and Kedify

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers running HTTP workloads on Kubernetes who want to enable event-driven autoscaling with KEDA and Kedify.

description: Enable event-driven autoscaling for HTTP workloads on Kubernetes by installing Kedify and KEDA with Helm and testing autoscaling behavior.

learning_objectives:
  - Install Kedify (KEDA build, HTTP Scaler, and Kedify Agent) with Helm
  - Verify that Kedify and KEDA components are running in the cluster
  - Deploy a sample HTTP application and test autoscaling behavior

prerequisites:
  - A running Kubernetes cluster (local or cloud)
  - Kubectl and Helm installed 
  - Access to the Kedify Service dashboard to obtain your Organization ID and API key (sign up at [Kedify dashboard](https://dashboard.kedify.io/))

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:17:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6ff33f6dfaf25e926a0ce8756b4e564e5aa37112e5425f9c3dce13f772b54145
  summary_generated_at: '2026-06-02T04:12:58Z'
  summary_source_hash: 6ff33f6dfaf25e926a0ce8756b4e564e5aa37112e5425f9c3dce13f772b54145
  faq_generated_at: '2026-06-03T01:17:17Z'
  faq_source_hash: 6ff33f6dfaf25e926a0ce8756b4e564e5aa37112e5425f9c3dce13f772b54145
  summary: >-
    This Learning Path shows how to enable event-driven autoscaling for HTTP workloads on Kubernetes
    using KEDA and Kedify. You will use Helm to add the Kedify chart repository and install three
    charts—the KEDA (Kedify build), the HTTP Scaler, and the Kedify Agent—then verify they are
    running. If needed, you will install an ingress controller (NGINX) and target arm64 nodes.
    Next, you will deploy a sample web service, expose it via Kubernetes Ingress, rely on Kedify’s
    autowiring to route traffic, and generate load to observe scale-out, scale-in, and scale-to-zero
    behavior. It targets Linux and works on local or cloud clusters (EKS, GKE, AKS). Prerequisites
    include kubectl, Helm, a running cluster, and Kedify dashboard credentials.
  faqs:
  - question: What do I need before I start the installation?
    answer: >-
      You need a running Kubernetes cluster (local or cloud), kubectl and Helm installed, and
      access to the Kedify Service dashboard to obtain your Organization ID and API key. The path
      targets Linux.
  - question: Do I need an ingress controller, and which one is used here?
    answer: >-
      Yes, an ingress controller is required to handle HTTP traffic. This path installs the NGINX
      Ingress Controller with Helm and targets arm64 nodes; if your cluster already has a working
      ingress controller, you can skip this step.
  - question: Which Helm charts are installed to enable HTTP autoscaling?
    answer: >-
      You install three charts from the Kedify repository: KEDA (Kedify build) for event-driven
      autoscaling, the HTTP Scaler for HTTP-based scaling, and the Kedify Agent to connect your
      cluster to Kedify’s cloud service.
  - question: How do I know Kedify and KEDA are running correctly?
    answer: >-
      The Learning Path includes a verification step to check that the Kedify and KEDA components
      are running in your cluster. Follow those checks before proceeding to application deployment.
  - question: What behavior should I expect when testing the sample HTTP app?
    answer: >-
      After deploying the app and enabling autoscaling with a scaled object, generating HTTP load
      should trigger scale out. When the app becomes idle, you should observe scale in, including
      scale-to-zero.
# END generated_summary_faq

author: Zbynek Roubalik

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
armips:
  - Neoverse
operatingsystems:
  - Linux
tools_software_languages:
  - Kubernetes
  - Helm
  - KEDA
  - Kedify

further_reading:
  - resource:
      title: Kedify HTTP Scaler
      link: https://kedify.io/scalers/http
      type: documentation
  - resource:
      title: Kedify documentation
      link: https://docs.kedify.io
      type: documentation
  - resource:
      title: KEDA project
      link: https://keda.sh/
      type: documentation


### FIXED, DO NOT MODIFY
# =============================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

