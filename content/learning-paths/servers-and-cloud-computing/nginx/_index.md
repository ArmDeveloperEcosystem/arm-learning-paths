---
title: Learn how to deploy Nginx

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for engineers who want to use Nginx on Arm.

learning_objectives:
    - Install and run Nginx on Arm servers
    - Setup Nginx as a web server, reverse proxy, or an API Gateway
    - Verify Nginx is working correctly

prerequisites:
    - To create a file server you will need at least one [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or one on-premises Arm server.
    - To create a reverse proxy or API gateway you will need at least three Arm based instances from a cloud service provider or at least three on-premises Arm servers.
    - Network settings (firewalls and security groups) which allow communication on port 22 (SSH) and port 443 (HTTPS).

author_primary: Julio Suarez

### Tags
skilllevels: Introductory
subjects: Web
armips:
    - Neoverse
tools_software_languages:
    - Nginx
operatingsystems:
    - Linux

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
