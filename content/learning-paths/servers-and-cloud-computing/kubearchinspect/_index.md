---
title: Migrate containers to Arm using KubeArchInspect

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers who want to ensure containers running in a Kubernetes cluster support the Arm architecture.

learning_objectives: 
    - Run KubeArchInspect to generate a report on the containers running in a Kubernetes cluster.
    - Discover which images support the Arm architecture.
    - Understand common reasons for an image not supporting Arm.
    - Make configuration changes to upgrade images with Arm support.

prerequisites:
    - A running Kubernetes cluster accessible with `kubectl`.

author_primary: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
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
