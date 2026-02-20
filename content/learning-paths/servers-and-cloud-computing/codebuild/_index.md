---
title: Build and share Docker images using AWS CodeBuild

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers interested in using AWS CodeBuild to automate container build tasks.

learning_objectives:
    - Use a GitHub project and AWS CodeBuild to automate Docker image creation
    - Pull and run the created Docker images on any Arm computer with Docker installed

prerequisites:
    - An [AWS account](/learning-paths/servers-and-cloud-computing/csp/aws/) for accessing AWS cloud services.
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or any Arm server, laptop, or single-board computer running [Docker](/install-guides/docker/) used to run the created images

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: CI-CD
cloud_service_providers:
  - AWS

armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Docker
    - AWS CodeBuild

further_reading:
    - resource:
        title: AWS documentation
        link: https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html
        type: documentation
    - resource:
        title: AWS CodeBuild curated Docker images
        link: https://github.com/aws/aws-codebuild-docker-images 
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
