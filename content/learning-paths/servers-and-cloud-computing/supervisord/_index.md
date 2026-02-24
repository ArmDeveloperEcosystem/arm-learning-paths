---
title: Access running containers using Supervisor, SSH, and Remote.It

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to learn how to run multiple services in a container and access running containers using Supervisor, SSH, and Remote.It during the debug and test phases of a project.

learning_objectives:
    - Use Supervisor to run multiple services in a container
    - Access a container running in AWS Fargate without changing the security group for debug and test

prerequisites:
    - An Arm Linux computer running Docker
    - An AWS account
    - A Remote.It account

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
armips:
    - Neoverse 
    - Cortex-A
operatingsystems:
    - Linux 
tools_software_languages:
    - Docker
    - Remote.It
    - Supervisor
    
further_reading:
    - resource:
        title: Run multiple processes in a container
        link: https://docs.docker.com/config/containers/multi-service_container/
        type: documentation
    - resource:
        title: Supervisor with Docker Lessons learned
        link: https://advancedweb.hu/supervisor-with-docker-lessons-learned/
        type: blog
    - resource:
        title: Multiple services in a Docker container with supervisord
        link: https://dev.to/pratapkute/multiple-services-in-a-docker-container-with-supervisord-2g13
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
