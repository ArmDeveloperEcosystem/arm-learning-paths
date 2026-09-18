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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:20:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d70ee3667de6482f2ef9f868f78b9a10d02707c9fbf8346f6da72a87b35694b9
  summary_generated_at: '2026-09-15T21:20:59Z'
  summary_source_hash: d70ee3667de6482f2ef9f868f78b9a10d02707c9fbf8346f6da72a87b35694b9
  faq_generated_at: '2026-09-15T21:20:59Z'
  faq_source_hash: d70ee3667de6482f2ef9f868f78b9a10d02707c9fbf8346f6da72a87b35694b9
  summary: >-
    You'll enable event-driven HTTP autoscaling on an Arm-based Kubernetes cluster with KEDA
    and Kedify. First, you'll install the required Kedify charts, verify their components, and
    configure an NGINX Ingress Controller for arm64 nodes. Then, you'll deploy a web
    service and expose it through ingress. You'll create a scaled object, generate traffic, and
    observe scale-out, scale-in, and scale-to-zero behavior.
  faqs:
  - question: How do I verify that Kedify and KEDA installed correctly?
    answer: >-
      Run `kubectl get pods -n keda` and confirm that the KEDA, HTTP scaler, and Kedify Agent pods
      show `1/1` in `READY` and `Running` in `STATUS` before continuing.
  - question: Do I still need to install NGINX Ingress
      Controller if my cluster already has an ingress controller?
    answer: >-
      No. If an ingress controller is already installed and configured, skip the installation of NGINX Ingress Controller.
  - question: Which deployment target should I use for the ingress controller on Arm-based nodes?
    answer: >-
      Install the NGINX Ingress Controller with Helm and target arm64 nodes to ensure that the controller runs on Arm nodes in your cluster.
  - question: What do I need to connect the cluster to Kedify’s cloud service?
    answer: >-
      Use your `Organization ID` and `API key` from the Kedify Service dashboard. Provide these values
      when installing the Kedify Agent to establish the connection.
  - question: How do I know autoscaling is working after deploying the sample app?
    answer: >-
      Generate HTTP load against the application’s ingress and watch the service scale out. When
      load stops, it should scale back in, including scale-to-zero when idle.
# END generated_summary_faq

author: Zbynek Roubalik

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
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
