---
title: Autoscaling HTTP applications on Kubernetes

draft: true
cascade:
    draft: true
    
minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers running HTTP-based workloads on Kubernetes who want to enable event-driven autoscaling.

learning_objectives:
  - Install Kedify (KEDA build, HTTP Scaler, and Kedify Agent) via Helm
  - Verify that the components are running in your cluster
  - Deploy a sample HTTP application and test autoscaling behavior

prerequisites:
  - A running Kubernetes cluster (local or cloud)
  - kubectl and helm installed locally
  - Access to the Kedify Service dashboard (https://dashboard.kedify.io/) to obtain Organization ID and API Key. You can log in or create an account if you don’t have one

author: Zbynek Roubalik

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
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
