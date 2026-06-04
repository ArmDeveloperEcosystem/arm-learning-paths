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
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:44:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7972fb230273ab1809c6f0917c4bbc49934f495feb2649da665d67bf71a45a3f
  summary_generated_at: '2026-06-02T04:43:07Z'
  summary_source_hash: 7972fb230273ab1809c6f0917c4bbc49934f495feb2649da665d67bf71a45a3f
  faq_generated_at: '2026-06-03T01:44:23Z'
  faq_source_hash: 7972fb230273ab1809c6f0917c4bbc49934f495feb2649da665d67bf71a45a3f
  summary: >-
    Learn how to use Red Hat OpenShift Pipelines (Tekton) on AWS to migrate existing OpenShift
    applications from x86 compute nodes to Arm 64-bit (arm64) nodes and build multi-architecture
    container images. You will assess workload compatibility, enable multi-architecture support
    in OpenShift, configure Arm64 nodes, rebuild and verify images, and transition deployments
    safely. The example uses the OpenShift Pipelines Tutorial as a baseline running on x86 infrastructure.
    Prerequisites include an AWS account with an OpenShift 4.18 cluster on x86 compute nodes,
    the OpenShift Pipelines (Tekton) Operator installed, cluster-admin access, and familiarity
    with the oc CLI, container fundamentals, and core Tekton concepts. Estimated time to complete
    is about 30 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need an AWS account with an OpenShift 4.18 cluster running x86 compute nodes, the Red
      Hat OpenShift Pipelines (Tekton) Operator installed, and cluster-admin or equivalent permissions.
      Familiarity with the oc CLI, container fundamentals, and basic Tekton concepts (Task, Pipeline,
      PipelineRun) is also required.
  - question: Which environment does the example start from?
    answer: >-
      It uses the OpenShift Pipelines Tutorial as the baseline, running on an OpenShift 4.18 cluster
      on AWS with x86 compute nodes. The procedures assume this x86 starting point.
  - question: Do I need Arm64 worker nodes already available?
    answer: >-
      Not explicitly. The Learning Path shows how to configure Arm64 nodes and enable multi-architecture
      support as part of the migration steps.
  - question: How do I know my application can run on Arm (arm64)?
    answer: >-
      Begin with the assessment step to confirm workload compatibility with the 64-bit Arm architecture.
      Proceed only after verifying that your applications can run on arm64.
  - question: What result should I expect after completing the steps?
    answer: >-
      You will rebuild and verify container images with multi-architecture support and transition
      deployments to Arm-based nodes on AWS. The steps focus on a safe migration using OpenShift
      Pipelines.
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

