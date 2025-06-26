---
title: Building Multi-Architecture Applications with Red Hat OpenShift Pipelines on Red Hat OpenShift 4.18 on AWS

draft: true
cascade:
    draft: true

minutes_to_complete: 30

who_is_this_for: This learning path is for Openshift administrators interested in migrating their applications to  Arm.


learning_objectives: 
    - Migrate existing applications to Arm.

prerequisites:
    - An AWS account with an OpenShift 4.18 cluster with x86 nodes installed and configured.
    - Red Hat OpenShift Pipelines (Tekton) operator installed in your cluster.
    - Familiarity with Red Hat OpenShift (oc CLI), container concepts, and basic Tekton principles (Task, Pipeline, PipelineRun).
    - Access to your Red Hat OpenShift cluster with cluster-admin or equivalent privileges for node configuration and pipeline setup.
    - Your application source code in a Git repository. In this example we assume that you have [pipelines-tutorial](https://www.google.com/url?q=https://github.com/openshift/pipelines-tutorial&sa=D&source=editors&ust=1749822472437927&usg=AOvVaw2P4wUOL5KUV-ePkRiv3jJx) built and running on x86.
    - Ensure that the Red Hat OpenShift cluster is using the multi-arch release payload.

author: Jeff Young

### Tags
skilllevels: Advanced
subjects: CI-CD
armips:
    - Aarch64
tools_software_languages:
    - Tekton
    - OpenShift
operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
