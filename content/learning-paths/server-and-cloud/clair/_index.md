---
title: Learn how to generate vulnerability reports using Clair on Arm servers

description: Learn how to run Clair in the combined and the distributed mode, submit the containers to Clair and generate the Vulnerability report that can affect the content.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers interested in checking container images for vulnerabilities.

learning_objectives:
    - Install and run Clair in both combined and distributed mode
    - Submit container images to Clair using clairctl and generate a vulnerability report

prerequisites:
    - A computer with the latest versions of docker, docker-compose, and go installed.

author_primary: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Docker
    - Docker Compose
    - Go 
    - Clair

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
