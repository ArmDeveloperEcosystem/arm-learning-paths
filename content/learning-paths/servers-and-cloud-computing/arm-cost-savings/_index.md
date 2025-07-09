---
title: Build multi-architecture applications with Red Hat OpenShift Pipelines on AWS

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This topic is for OpenShift administrators interested in migrating their applications to Arm.


learning_objectives: 
    - Migrate existing OpenShift applications to Arm.

prerequisites:
    - An AWS account with an OpenShift 4.18 cluster with x86 nodes installed and configured.
    - Red Hat OpenShift Pipelines (Tekton) operator installed in your cluster.
    - Familiarity with Red Hat OpenShift (oc CLI), container concepts, and basic Tekton principles (Task, Pipeline, PipelineRun).
    - Access to your Red Hat OpenShift cluster with cluster-admin or equivalent privileges for node configuration and pipeline setup.

author: Jeff Young

### Tags
skilllevels: Advanced
subjects: CI-CD
armips:
    - Neoverse
tools_software_languages:
    - Tekton
    - OpenShift
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Red Hat OpenShift Documentation
        link: https://docs.openshift.com/container-platform/latest/welcome/index.html
        type: documentation
    - resource:
        title: OpenShift Pipelines (Tekton) Documentation
        link: https://docs.openshift.com/container-platform/latest/cicd/pipelines/understanding-openshift-pipelines.html
        type: documentation
    - resource:
        title: OpenShift Multi-Architecture Compute Machines
        link: https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster
        type: documentation
    - resource:
        title: OpenShift ImageStreams Documentation
        link: https://docs.openshift.com/container-platform/latest/openshift_images/image-streams-managing.html
        type: documentation
    - resource:
        title: Migrating to Multi-Architecture Compute Machines
        link: https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html-single/updating_clusters/#migrating-to-multi-payload
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---