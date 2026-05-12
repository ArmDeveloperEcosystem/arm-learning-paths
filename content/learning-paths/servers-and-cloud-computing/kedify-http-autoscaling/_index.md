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
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 6ff33f6dfaf25e926a0ce8756b4e564e5aa37112e5425f9c3dce13f772b54145
  summary: >-
    Enable event-driven autoscaling for HTTP workloads on Kubernetes by installing Kedify and
    KEDA with Helm and testing autoscaling behavior. It is designed for developers running HTTP
    workloads on Kubernetes who want to enable event-driven autoscaling with KEDA and Kedify.
    By the end, you will be able to install Kedify (KEDA build, HTTP Scaler, and Kedify Agent)
    with Helm, verify that Kedify and KEDA components are running in the cluster, and deploy a
    sample HTTP application and test autoscaling behavior. It focuses on tools and technologies
    such as Kubernetes, Helm, KEDA, and Kedify, Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as AWS, Microsoft Azure, and Google Cloud. The main steps cover Install
    Kedify using Helm, Install an ingress controller, and Autoscale HTTP applications with Kedify
    and Kubernetes Ingress.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install Kedify (KEDA build, HTTP Scaler, and Kedify Agent) with Helm, verify that
      Kedify and KEDA components are running in the cluster, and deploy a sample HTTP application
      and test autoscaling behavior. Enable event-driven autoscaling for HTTP workloads on Kubernetes
      by installing Kedify and KEDA with Helm and testing autoscaling behavior.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers running HTTP workloads on Kubernetes who want
      to enable event-driven autoscaling with KEDA and Kedify.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A running Kubernetes cluster (local
      or cloud); Kubectl and Helm installed; Access to the Kedify Service dashboard to obtain
      your Organization ID and API key (sign up at [Kedify dashboard](https://dashboard.kedify.io/)).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Kubernetes, Helm, KEDA, and Kedify, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as AWS, Microsoft Azure, and Google
      Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Install Kedify using Helm, Install an ingress controller,
      and Autoscale HTTP applications with Kedify and Kubernetes Ingress.
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

