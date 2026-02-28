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
