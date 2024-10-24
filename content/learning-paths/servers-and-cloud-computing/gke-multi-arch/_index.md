---
title: Learn how to migrate an x86 application to multi-architecture with Arm-based on Google Axion Processor on GKE

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who are looking to migrate their existing x86 containerized applications to Arm

learning_objectives: 
    - Add Arm-based nodes (Google Axion) to an existing x86-based GKE cluster
    - Rebuild an x86-based application to make it multi-arch and run on Arm
    - Learn how to add taints and tolerations to GKE clusters to schedule application pods on architecture specific nodes
    - Run a multi-arch application across multiple architectures on a single GKE cluster

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). Create an account if needed.
    - A computer with [Google Cloud CLI](/install-guides/gcloud) and [kubectl](/install-guides/kubectl/)installed.
    - An existing Google Kubernetes Engine (GKE) cluster with x86-based nodes

author_primary: Pranay Bakre

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers: Google Cloud

armips:
    - Neoverse

tools_software_languages:
    - Kubernetes

operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
