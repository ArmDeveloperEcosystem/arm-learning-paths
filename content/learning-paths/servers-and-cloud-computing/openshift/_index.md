---
title: Build multi-architecture apps with Red Hat OpenShift Pipelines on AWS

minutes_to_complete: 30

who_is_this_for: This topic is for OpenShift administrators who want to migrate their applications to Arm.

learning_objectives: 
  - Migrate existing OpenShift applications to Arm-based nodes.

prerequisites:
  - An AWS account with an OpenShift 4.18 cluster running x86 compute nodes
  - Red Hat OpenShift Pipelines (Tekton) Operator installed in your cluster
  - Familiarity with the `oc` CLI, container fundamentals, and basic Tekton concepts (Task, Pipeline, PipelineRun)
  - Cluster access with cluster-admin or equivalent permissions to configure nodes and pipelines

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:20:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6a861fcfd4e3dea4a2709a2c2c14708b65c1a5c99b1fa9bd86107572206aa571
  summary_generated_at: '2026-11-18T20:20:50Z'
  summary_source_hash: 6a861fcfd4e3dea4a2709a2c2c14708b65c1a5c99b1fa9bd86107572206aa571
  faq_generated_at: '2026-11-18T20:20:50Z'
  faq_source_hash: 6a861fcfd4e3dea4a2709a2c2c14708b65c1a5c99b1fa9bd86107572206aa571
  summary: >-
    You'll extend an OpenShift Pipelines workflow on AWS to build and deploy an application for
    arm64. First, you'll assess compatibility and enable multi-architecture support in the cluster.
    Then, you'll add Arm nodes, configure scheduling, and rebuild container images with Tekton.
    Finally, you'll deploy the rebuilt application to Arm nodes and verify that its pods run there
    before removing x86 workers.
  faqs:
  - question: What do I need to check before enabling multi-architecture builds?
    answer: >-
      Confirm that Red Hat OpenShift Pipelines (Tekton) is installed and that you have
      cluster-admin or equivalent permissions. Ensure that the baseline [OpenShift Pipelines Tutorial](https://github.com/openshift/pipelines-tutorial)
      is running on x86 nodes so that you can extend it for arm64.
  - question: How do I know an application is ready to run on Arm64 nodes?
    answer: >-
      After you assess compatibility, rebuild the container image for arm64 with your pipeline
      and deploy it to Arm nodes. Check that the pods start there without image or runtime
      errors.
  - question: Which nodes should host the migrated workloads on AWS?
    answer: >-
      Add and configure Arm nodes on AWS Graviton and join them to your OpenShift cluster.
      Schedule the rebuilt workloads onto these Arm-based nodes after images are verified.
  - question: What result should I expect from the pipeline when targeting arm64?
    answer: >-
      Check that your `PipelineRun` produces and publishes an arm64 container image. Deploy that
      image to Arm nodes and verify that its pods run there.
  - question: When can I remove the x86 worker nodes?
    answer: >-
      Deploy your arm64 image to the Arm nodes and confirm that its pods run successfully. After
      the pods are up, you can remove the x86 worker nodes and. If needed, you can remove the taints from
      the Arm worker nodes.
# END generated_summary_faq

author: Jeff Young

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

# Tags
skilllevels: Advanced
subjects: CI-CD
platforms:
  - AWS Graviton
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

