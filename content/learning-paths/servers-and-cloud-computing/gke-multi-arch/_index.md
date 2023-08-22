---
title: Learn how to make an x86-based application multi-arch on GKE

minutes_to_complete: 30

who_is_this_for: Developers who're looking to migrate their existing containerized applications and make them multi-arch

learning_objectives: 
    - Add Arm-based nodes to an existing x86-based GKE cluster
    - Rebuild x86-based application to make it multi-arch and run on Arm
    - Understand how to add taints and tolerations to GKE cluster to schedule application pods on architecture specific nodes
    - Run multi-arch application across multiple architectures in a single GKE cluster

prerequisites:
    - A Google Cloud account
    - Google Cloud CLI (glcoud) and kubectl cli installed on your local machine
    - An existing GKE cluster with x86-based nodes

author_primary: Arm

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse

tools_software_languages:
    - Kubernetes
    - Google Cloud
operatingsystems:
    - Linux


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
