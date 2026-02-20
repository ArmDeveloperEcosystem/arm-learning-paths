---
title: Autoscale HTTP applications on Kubernetes with KEDA and Kedify

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers running HTTP workloads on Kubernetes who want to enable event-driven autoscaling with KEDA and Kedify.

learning_objectives:
  - Install Kedify (KEDA build, HTTP Scaler, and Kedify Agent) with Helm
  - Verify that Kedify and KEDA components are running in the cluster
  - Deploy a sample HTTP application and test autoscaling behavior

prerequisites:
  - A running Kubernetes cluster (local or cloud)
  - Kubectl and Helm installed 
  - Access to the Kedify Service dashboard to obtain your Organization ID and API key (sign up at [Kedify dashboard](https://dashboard.kedify.io/))

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
