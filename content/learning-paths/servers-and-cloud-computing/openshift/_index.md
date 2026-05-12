---
title: Build multi-architecture applications with Red Hat OpenShift Pipelines on AWS

minutes_to_complete: 30

who_is_this_for: This topic is for OpenShift administrators who want to migrate their applications to Arm.

learning_objectives: 
  - Migrate existing OpenShift applications to Arm-based nodes

prerequisites:
  - An AWS account with an OpenShift 4.18 cluster running x86 compute nodes
  - Red Hat OpenShift Pipelines (Tekton) Operator installed in your cluster
  - Familiarity with the `oc` CLI, container fundamentals, and basic Tekton concepts (Task, Pipeline, PipelineRun)
  - Cluster access with cluster-admin or equivalent permissions to configure nodes and pipelines

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 7972fb230273ab1809c6f0917c4bbc49934f495feb2649da665d67bf71a45a3f
  summary: >-
    Build multi-architecture applications with Red Hat OpenShift Pipelines on AWS walks you through
    an end-to-end Arm software workflow. It is designed for OpenShift administrators who want
    to migrate their applications to Arm. By the end, you will be able to migrate existing OpenShift
    applications to Arm-based nodes. It focuses on tools and technologies such as Tekton and OpenShift,
    Linux environments, Arm platforms including Neoverse, and cloud platforms such as AWS. The
    main steps cover Migrate an x86 workload to Arm on AWS.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will migrate existing OpenShift applications to Arm-based nodes.
  - question: Who is this Learning Path for?
    answer: >-
      This topic is for OpenShift administrators who want to migrate their applications to Arm.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An AWS account with an OpenShift 4.18
      cluster running x86 compute nodes; Red Hat OpenShift Pipelines (Tekton) Operator installed
      in your cluster; Familiarity with the `oc` CLI, container fundamentals, and basic Tekton
      concepts (Task, Pipeline, PipelineRun); Cluster access with cluster-admin or equivalent
      permissions to configure nodes and pipelines.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Tekton and OpenShift, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as AWS.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Migrate an x86 workload to Arm on AWS.
# END generated_summary_faq

author: Jeff Young

# Tags
skilllevels: Advanced
subjects: CI-CD
cloud_service_providers:
  - AWS
armips:
  - Neoverse
tools_software_languages:
  - Tekton
  - OpenShift
operatingsystems:
  - Linux

further_reading:
  - resource:
      title: Red Hat OpenShift documentation
      link: https://docs.openshift.com/container-platform/latest/welcome/index.html
      type: documentation
  - resource:
      title: OpenShift Pipelines (Tekton) documentation
      link: https://docs.openshift.com/container-platform/latest/cicd/pipelines/understanding-openshift-pipelines.html
      type: documentation
  - resource:
      title: OpenShift multi-architecture compute machines
      link: https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster
      type: documentation
  - resource:
      title: OpenShift ImageStreams documentation
      link: https://docs.openshift.com/container-platform/latest/openshift_images/image-streams-managing.html
      type: documentation
  - resource:
      title: Migrating to multi-architecture compute machines
      link: https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html-single/updating_clusters/#migrating-to-multi-payload
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

